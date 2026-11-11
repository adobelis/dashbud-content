"""Search YouTube via DataForSEO and build a reproducible sampling manifest.

Companion to fetch_youtube_transcript.py; same auth pattern (scripts/.env).

Pipeline:
  1. search   -- queries -> manifest of candidate videos (TSV)
  2. enrich   -- fill likes + comment_count + exact date from video_info
  3. comments -- pull comments for one video (failure-report mining)

Usage:
  python search_youtube.py --probe
  python search_youtube.py --query "build a dashboard with chatgpt" --out FILE
  python search_youtube.py --batch QUERIES_FILE --depth 20 --out FILE
  python search_youtube.py --enrich MANIFEST_FILE
  python search_youtube.py --comments VIDEO_ID [--depth 50]

A queries file holds one query per line; '#' comments allowed.

Manifest columns -- published sits first among the metadata because date frames
everything: a 2024 tutorial and a 2026 tutorial describe different products.
  query, rank, video_id, published, published_rel, views, likes, comment_count,
  channel, duration_s, is_shorts, title, url
"""
import os
import sys
import json
import csv
import time
import argparse
import datetime
import requests
from dotenv import load_dotenv

SCRIPTS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(SCRIPTS_DIR, ".env"))

API_KEY = os.getenv("DATAFORSEO_API_KEY")
BASE = "https://api.dataforseo.com/v3"
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")

COLUMNS = ["query", "rank", "video_id", "published", "published_rel", "views",
           "likes", "comment_count", "channel", "duration_s", "is_shorts",
           "title", "url"]


def headers():
    return {"Content-Type": "application/json",
            "Authorization": f"Basic {API_KEY}"}


def post(path, payload):
    resp = requests.post(f"{BASE}/{path}", data=json.dumps([payload]),
                         headers=headers(), timeout=120)
    return resp.status_code, resp.json()


def get(path):
    resp = requests.get(f"{BASE}/{path}", headers=headers(), timeout=60)
    return resp.status_code, resp.json()


def task_status(body):
    try:
        task = body["tasks"][0]
        return task.get("status_code"), task.get("status_message")
    except (KeyError, IndexError, TypeError):
        return body.get("status_code"), body.get("status_message")


def first_result_items(body):
    try:
        return body["tasks"][0]["result"][0]["items"] or []
    except (KeyError, IndexError, TypeError):
        return []


def save_raw(name, body):
    """Keep every response so extraction can be redone without re-spending."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, name)
    with open(path, "w") as handle:
        json.dump(body, handle, indent=2)
    return path


def slugify(text, limit=60):
    return "".join(c if c.isalnum() else "-" for c in text.lower())[:limit].strip("-")


def probe():
    print("== account ==")
    status, body = get("appendix/user_data")
    print(f"HTTP {status}")
    try:
        user = body["tasks"][0]["result"][0]
        print(f"  login:   {user.get('login')}")
        print(f"  balance: {user.get('money', {}).get('balance')}")
    except (KeyError, IndexError, TypeError):
        print(f"  unparsed: {json.dumps(body)[:400]}")

    print("\n== endpoint availability ==")
    probes = [
        ("serp/youtube/organic/live/advanced",
         dict(keyword="test", location_code=2840, language_code="en", block_depth=20)),
        ("serp/youtube/video_info/live/advanced",
         dict(video_id="dQw4w9WgXcQ", location_code=2840, language_code="en")),
        ("serp/youtube/video_subtitles/live/advanced",
         dict(video_id="dQw4w9WgXcQ", location_code=2840, language_code="en")),
        ("serp/youtube/video_comments/live/advanced",
         dict(video_id="dQw4w9WgXcQ", location_code=2840, language_code="en", depth=10)),
    ]
    for path, payload in probes:
        status, body = post(path, payload)
        code, message = task_status(body)
        flag = "OK  " if code == 20000 else "FAIL"
        print(f"  [{flag}] {path}  (HTTP {status}, task {code} {message})")


def search(query, depth):
    payload = dict(keyword=query, location_code=2840,
                   language_code="en", block_depth=depth)
    status, body = post("serp/youtube/organic/live/advanced", payload)
    code, message = task_status(body)
    if code != 20000:
        print(f"  !! {query}: task {code} {message}", file=sys.stderr)
        return []

    rows = []
    for item in first_result_items(body):
        if item.get("type") != "youtube_video":
            continue
        video_id = item.get("video_id")
        timestamp = item.get("timestamp") or ""
        rows.append({
            "query": query,
            "rank": item.get("rank_absolute"),
            "video_id": video_id,
            # absolute date, sliced to YYYY-MM-DD; the API's publication_date
            # is relative ("2 years ago") and useless for a dated corpus
            "published": timestamp[:10],
            "published_rel": item.get("publication_date") or "",
            "views": item.get("views_count") or "",
            "likes": "",
            "comment_count": "",
            "channel": item.get("channel_name") or "",
            "duration_s": item.get("duration_time_seconds") or "",
            "is_shorts": item.get("is_shorts"),
            "title": (item.get("title") or "").replace("\t", " ").strip(),
            "url": item.get("url") or (
                f"https://www.youtube.com/watch?v={video_id}" if video_id else ""),
        })
    stamp = datetime.date.today().isoformat()
    raw = save_raw(f"ytsearch_{stamp}_{slugify(query)}.json", body)
    print(f"  {len(rows):3d} videos  <- {query}\n       raw: {raw}")
    return rows


def enrich(manifest_path):
    """Fill likes and comment_count from video_info, in place."""
    with open(manifest_path, newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))

    seen = {}
    for index, row in enumerate(rows, 1):
        video_id = row.get("video_id")
        if not video_id:
            continue
        if row.get("likes") and row.get("comment_count"):
            continue
        if video_id in seen:
            row.update(seen[video_id])
            continue

        payload = dict(video_id=video_id, location_code=2840, language_code="en")
        status, body = post("serp/youtube/video_info/live/advanced", payload)
        code, message = task_status(body)
        if code != 20000:
            print(f"  !! {video_id}: task {code} {message}", file=sys.stderr)
            continue
        items = first_result_items(body)
        info = items[0] if items else {}
        save_raw(f"ytinfo_{video_id}.json", body)

        patch = {
            "likes": info.get("likes_count") or "",
            "comment_count": info.get("comments_count") or "",
        }
        # video_info carries the authoritative timestamp; prefer it
        timestamp = info.get("timestamp") or ""
        if timestamp:
            patch["published"] = timestamp[:10]
        if info.get("views_count"):
            patch["views"] = info.get("views_count")
        seen[video_id] = patch
        row.update(patch)
        print(f"  [{index}/{len(rows)}] {video_id}  "
              f"{patch['likes']} likes, {patch['comment_count']} comments, "
              f"published {row.get('published')}")
        time.sleep(0.3)

    with open(manifest_path, "w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=COLUMNS,
                                delimiter="\t", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    print(f"\nEnriched {len(rows)} rows in {manifest_path}")


def comments(video_id, depth):
    payload = dict(video_id=video_id, location_code=2840,
                   language_code="en", depth=depth)
    status, body = post("serp/youtube/video_comments/live/advanced", payload)
    code, message = task_status(body)
    if code != 20000:
        print(f"task {code} {message}", file=sys.stderr)
        sys.exit(1)
    raw = save_raw(f"ytcomments_{video_id}.json", body)
    items = first_result_items(body)
    for item in items:
        author = item.get("author_name", "?")
        likes = item.get("likes_count") or 0
        published = item.get("publication_date") or ""
        text = (item.get("comment") or "").replace("\n", " ")
        print(f"[{likes:>5} likes] {author} ({published}): {text}")
    print(f"\n{len(items)} comments  (raw: {raw})", file=sys.stderr)


def write_manifest(rows, out_path):
    target = open(out_path, "w", newline="") if out_path else sys.stdout
    try:
        writer = csv.DictWriter(target, fieldnames=COLUMNS,
                                delimiter="\t", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    finally:
        if out_path:
            target.close()
            print(f"\nWrote {len(rows)} rows to {out_path}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--probe", action="store_true")
    parser.add_argument("--query")
    parser.add_argument("--batch")
    parser.add_argument("--enrich")
    parser.add_argument("--comments")
    parser.add_argument("--depth", type=int, default=20)
    parser.add_argument("--out")
    args = parser.parse_args()

    if not API_KEY:
        print("Error: DATAFORSEO_API_KEY not found in scripts/.env", file=sys.stderr)
        sys.exit(1)

    if args.probe:
        return probe()
    if args.enrich:
        return enrich(args.enrich)
    if args.comments:
        return comments(args.comments, args.depth)

    queries = []
    if args.query:
        queries.append(args.query)
    if args.batch:
        with open(args.batch) as handle:
            for line in handle:
                line = line.strip()
                if line and not line.startswith("#"):
                    queries.append(line)
    if not queries:
        parser.print_help()
        sys.exit(1)

    rows = []
    for query in queries:
        rows.extend(search(query, args.depth))
    write_manifest(rows, args.out)


if __name__ == "__main__":
    main()
