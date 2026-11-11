"""Resolve exact YouTube upload dates, and inspect video_info fields.

Why this exists: DataForSEO's YouTube `timestamp` is derived from the page's
RELATIVE label ("2 years ago"), so every older video lands on today's month and
day. For a corpus where publication date frames the finding, that is not good
enough -- the real date comes from the watch page's `uploadDate` microformat.

Usage:
  python youtube_video_dates.py --inspect VIDEO_ID
  python youtube_video_dates.py --manifest FILE.tsv [--limit N] [--only IDS]
  python youtube_video_dates.py --ids ID1,ID2

--manifest rewrites the TSV, adding `published_exact` and `date_source`
columns and leaving the original derived `published` untouched for comparison.
"""
import os
import re
import sys
import csv
import json
import time
import asyncio
import argparse
import requests
from dotenv import load_dotenv

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_DIR = os.path.dirname(HERE)
REPO_ROOT = os.path.dirname(SCRIPTS_DIR)
OUTPUT_DIR = os.path.join(HERE, "output")

load_dotenv(os.path.join(SCRIPTS_DIR, ".env"))
load_dotenv(os.path.join(REPO_ROOT, ".env"))

DFS_KEY = os.getenv("DATAFORSEO_API_KEY")
ZYTE_KEY = os.getenv("ZYTE_API_KEY")

UPLOAD_DATE_PATTERNS = [
    re.compile(r'"uploadDate"\s*:\s*"([0-9]{4}-[0-9]{2}-[0-9]{2})'),
    re.compile(r'itemprop="uploadDate"[^>]*content="([0-9]{4}-[0-9]{2}-[0-9]{2})'),
    re.compile(r'"publishDate"\s*:\s*"([0-9]{4}-[0-9]{2}-[0-9]{2})'),
]


def inspect(video_id):
    """Dump every scalar field video_info returns, to see what dates it has."""
    headers = {"Content-Type": "application/json",
               "Authorization": f"Basic {DFS_KEY}"}
    payload = dict(video_id=video_id, location_code=2840, language_code="en")
    resp = requests.post(
        "https://api.dataforseo.com/v3/serp/youtube/video_info/live/advanced",
        data=json.dumps([payload]), headers=headers, timeout=90)
    body = resp.json()
    task = body.get("tasks", [{}])[0]
    print(f"task {task.get('status_code')} {task.get('status_message')}")
    try:
        item = task["result"][0]["items"][0]
    except (KeyError, IndexError, TypeError):
        print(json.dumps(body)[:800])
        return
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, f"ytinfo_{video_id}.json"), "w") as handle:
        json.dump(body, handle, indent=2)
    for key in sorted(item):
        value = item[key]
        if isinstance(value, (str, int, float, bool, type(None))):
            print(f"  {key}: {str(value)[:100]}")
        else:
            length = len(value) if hasattr(value, "__len__") else "?"
            print(f"  {key}: <{type(value).__name__} len={length}>")


async def fetch_upload_dates(video_ids):
    """Exact upload dates from the watch page microformat, via Zyte."""
    from zyte_api import AsyncZyteAPI

    if not ZYTE_KEY:
        print("Error: ZYTE_API_KEY not found in .env", file=sys.stderr)
        sys.exit(1)
    client = AsyncZyteAPI(api_key=ZYTE_KEY)
    dates = {}
    for index, video_id in enumerate(video_ids, 1):
        url = f"https://www.youtube.com/watch?v={video_id}"
        found = None
        for mode in ("httpResponseBody", "browserHtml"):
            try:
                result = await client.get({"url": url, mode: True})
            except Exception as error:
                print(f"  [{index}/{len(video_ids)}] {video_id} {mode} error: "
                      f"{str(error)[:90]}", file=sys.stderr)
                continue
            if mode == "httpResponseBody":
                import base64
                raw = result.get("httpResponseBody") or ""
                html = base64.b64decode(raw).decode("utf-8", "replace") if raw else ""
            else:
                html = result.get("browserHtml") or ""
            for pattern in UPLOAD_DATE_PATTERNS:
                match = pattern.search(html)
                if match:
                    found = match.group(1)
                    break
            if found:
                break
        dates[video_id] = found or ""
        print(f"  [{index}/{len(video_ids)}] {video_id} -> {found or 'NOT FOUND'}")
        time.sleep(0.2)
    return dates


def update_manifest(path, limit, only):
    with open(path, newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        rows = list(reader)
        columns = list(reader.fieldnames or [])

    for extra in ("published_exact", "date_source"):
        if extra not in columns:
            columns.append(extra)

    wanted = []
    seen = set()
    for row in rows:
        video_id = row.get("video_id")
        if not video_id or video_id in seen:
            continue
        if only and video_id not in only:
            continue
        if row.get("published_exact"):
            continue
        seen.add(video_id)
        wanted.append(video_id)
    if limit:
        wanted = wanted[:limit]

    print(f"Resolving {len(wanted)} unique video ids\n")
    dates = asyncio.run(fetch_upload_dates(wanted)) if wanted else {}

    for row in rows:
        video_id = row.get("video_id")
        if video_id in dates and dates[video_id]:
            row["published_exact"] = dates[video_id]
            row["date_source"] = "watch_page_uploadDate"
        else:
            row.setdefault("published_exact", "")
            row.setdefault("date_source", "")

    with open(path, "w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns,
                                delimiter="\t", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    resolved = sum(1 for row in rows if row.get("published_exact"))
    print(f"\n{resolved}/{len(rows)} rows now carry an exact date -> {path}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--inspect")
    parser.add_argument("--manifest")
    parser.add_argument("--ids")
    parser.add_argument("--only", help="comma-separated video ids to restrict to")
    parser.add_argument("--limit", type=int)
    args = parser.parse_args()

    if args.inspect:
        return inspect(args.inspect)
    if args.ids:
        dates = asyncio.run(fetch_upload_dates(args.ids.split(",")))
        for video_id, date in dates.items():
            print(f"{video_id}\t{date}")
        return
    if args.manifest:
        only = set(args.only.split(",")) if args.only else None
        return update_manifest(args.manifest, args.limit, only)
    parser.print_help()


if __name__ == "__main__":
    main()
