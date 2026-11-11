"""Fill exact dates, likes and comment counts into any TSV with a video_id column.

DataForSEO's YouTube *search* `timestamp` is derived from the page's relative
label ("2 years ago") computed against the fetch date, so search-only dates are
wrong by up to a year. `video_info` returns the true publication date, plus the
likes and comment counts that search does not carry at all. This pass is
therefore what makes a date-framed corpus possible.

All existing columns are preserved; `likes`, `comment_count`, `published` and
`date_source` are filled.

Robustness, learned the hard way: the API read-times-out often enough that a
single long run will die partway. So requests retry with backoff, and the TSV
is flushed every --flush-every rows and again on exit, so a crash never loses
completed work. Every response is cached under output/, so a re-run costs
nothing for rows already done.

Usage:
  python enrich_youtube.py FILE.tsv [--top-per 8] [--group-by level]
                           [--limit N] [--flush-every 5] [--retries 3]
"""
import os
import csv
import json
import time
import argparse
import requests
from collections import defaultdict
from dotenv import load_dotenv

HERE = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(os.path.dirname(HERE), ".env"))
API_KEY = os.getenv("DATAFORSEO_API_KEY")
OUTPUT_DIR = os.path.join(HERE, "output")
ENDPOINT = ("https://api.dataforseo.com/v3/serp/youtube/"
            "video_info/live/advanced")


def to_int(value):
    try:
        return int(str(value).strip())
    except (TypeError, ValueError):
        return 0


def fetch_with_retry(video_id, retries, timeout):
    headers = {"Content-Type": "application/json",
               "Authorization": f"Basic {API_KEY}"}
    payload = dict(video_id=video_id, location_code=2840, language_code="en")
    last_error = None
    for attempt in range(1, retries + 1):
        try:
            resp = requests.post(ENDPOINT, data=json.dumps([payload]),
                                 headers=headers, timeout=timeout)
            return resp.json(), None
        except requests.exceptions.RequestException as error:
            last_error = f"{type(error).__name__}"
            if attempt < retries:
                backoff = 2 ** attempt
                print(f"       retry {attempt}/{retries - 1} after "
                      f"{last_error}, waiting {backoff}s")
                time.sleep(backoff)
    return None, last_error


def cached_or_fetch(video_id, retries, timeout):
    """Return (item, cached, error). Cache hit costs nothing."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, f"ytinfo_{video_id}.json")
    if os.path.exists(path):
        try:
            with open(path) as handle:
                body = json.load(handle)
            cached = True
        except json.JSONDecodeError:
            os.remove(path)          # truncated by an earlier crash
            body, cached = None, False
    else:
        body, cached = None, False

    if body is None:
        body, error = fetch_with_retry(video_id, retries, timeout)
        if body is None:
            return None, False, error
        with open(path, "w") as handle:
            json.dump(body, handle, indent=2)
        time.sleep(0.25)

    try:
        task = body["tasks"][0]
        if task.get("status_code") != 20000:
            return None, cached, task.get("status_message")
        return task["result"][0]["items"][0], cached, None
    except (KeyError, IndexError, TypeError):
        return None, cached, "unparsed"


def write(path, columns, rows):
    tmp = f"{path}.tmp"
    with open(tmp, "w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns,
                                delimiter="\t", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmp, path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("--top", type=int,
                        help="global top N by views, ignoring groups")
    parser.add_argument("--top-per", type=int)
    parser.add_argument("--group-by", default="level")
    parser.add_argument("--group", help="comma-separated group values to restrict to")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--flush-every", type=int, default=5)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--timeout", type=int, default=120)
    args = parser.parse_args()

    if not API_KEY:
        raise SystemExit("DATAFORSEO_API_KEY not found in scripts/.env")

    with open(args.path, newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        rows = list(reader)
        columns = list(reader.fieldnames or [])
    for extra in ("likes", "comment_count", "date_source"):
        if extra not in columns:
            columns.append(extra)

    targets = [r for r in rows if r.get("video_id")
               and r.get("date_source") != "video_info"]
    if args.group:
        wanted = set(args.group.split(","))
        targets = [r for r in targets if r.get(args.group_by) in wanted]
    if args.top_per:
        grouped = defaultdict(list)
        for row in targets:
            grouped[row.get(args.group_by, "")].append(row)
        selected = []
        for group in sorted(grouped):
            ranked = sorted(grouped[group],
                            key=lambda r: to_int(r.get("views")), reverse=True)
            selected.extend(ranked[:args.top_per])
        targets = selected
    if args.top:
        targets = sorted(targets, key=lambda r: to_int(r.get("views")),
                         reverse=True)[:args.top]
    if args.limit:
        targets = targets[:args.limit]

    print(f"{len(rows)} rows; enriching {len(targets)}\n")
    fetched = cache_hits = failed = 0
    try:
        for index, row in enumerate(targets, 1):
            video_id = row["video_id"]
            item, cached, error = cached_or_fetch(
                video_id, args.retries, args.timeout)
            if item is None:
                failed += 1
                row["date_source"] = "lookup-failed"
                print(f"  [{index}/{len(targets)}] {video_id} !! {error}")
            else:
                if cached:
                    cache_hits += 1
                else:
                    fetched += 1
                row["likes"] = item.get("likes_count") or ""
                row["comment_count"] = item.get("comments_count") or ""
                if item.get("views_count"):
                    row["views"] = item["views_count"]
                timestamp = item.get("timestamp") or ""
                if timestamp:
                    row["published"] = timestamp[:10]
                    row["date_source"] = "video_info"
                flag = "cache" if cached else "  api"
                print(f"  [{index}/{len(targets)}] {flag} {video_id}  "
                      f"{row['published']}  {to_int(row['likes']):>7,} likes  "
                      f"{to_int(row['comment_count']):>5,} comments  "
                      f"{(row.get('title') or '')[:46]}")
            if index % args.flush_every == 0:
                write(args.path, columns, rows)
    finally:
        write(args.path, columns, rows)
        done = sum(1 for r in rows if r.get("date_source") == "video_info")
        print(f"\nfetched {fetched}, cached {cache_hits}, failed {failed}")
        print(f"{done}/{len(rows)} rows now carry a real date")
        print(f"approx spend this run: ${fetched * 0.006:.2f}  ->  {args.path}")


if __name__ == "__main__":
    main()
