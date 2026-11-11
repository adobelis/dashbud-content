"""Summarise a YouTube sampling frame (TSV from search_youtube.py).

Date-first: a tutorial's publication date determines which product it was
describing, so the corpus has to be read by era, not as one undated pile.

Usage: python frame_stats.py MANIFEST.tsv [--top N]
"""
import csv
import sys
import argparse
from collections import Counter, defaultdict


def to_int(value):
    try:
        return int(str(value).strip())
    except (TypeError, ValueError):
        return 0


def load(path):
    with open(path, newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def dedupe(rows):
    """One row per video, keeping its best rank and all queries that found it."""
    best = {}
    queries = defaultdict(list)
    for row in rows:
        video_id = row.get("video_id")
        if not video_id:
            continue
        queries[video_id].append(row.get("query", ""))
        rank = to_int(row.get("rank")) or 999
        if video_id not in best or rank < (to_int(best[video_id].get("rank")) or 999):
            best[video_id] = row
    for video_id, row in best.items():
        row["found_by"] = len(queries[video_id])
        row["queries"] = "; ".join(sorted(set(queries[video_id])))
    return list(best.values())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest")
    parser.add_argument("--top", type=int, default=25)
    args = parser.parse_args()

    rows = load(args.manifest)
    unique = dedupe(rows)
    print(f"{len(rows)} result rows -> {len(unique)} unique videos\n")

    print("== by publication year ==")
    years = Counter((row.get("published") or "")[:4] or "unknown" for row in unique)
    for year in sorted(years):
        views = sum(to_int(r.get("views")) for r in unique
                    if (r.get("published") or "")[:4] == year)
        bar = "#" * min(60, years[year])
        print(f"  {year}  {years[year]:4d}  {bar}  {views:>12,} views")

    print("\n== by publication half-year (2024 onward) ==")
    halves = Counter()
    for row in unique:
        published = row.get("published") or ""
        if len(published) >= 7 and published[:4] >= "2024":
            month = to_int(published[5:7])
            halves[f"{published[:4]}-H{1 if month <= 6 else 2}"] += 1
    for key in sorted(halves):
        print(f"  {key}  {halves[key]:4d}  {'#' * min(60, halves[key])}")

    print("\n== shorts vs long-form ==")
    shorts = Counter(str(row.get("is_shorts")) for row in unique)
    for key, count in shorts.most_common():
        print(f"  is_shorts={key:<6} {count}")

    print(f"\n== top {args.top} by views ==")
    ranked = sorted(unique, key=lambda r: to_int(r.get("views")), reverse=True)
    print(f"  {'views':>10}  {'published':<10} {'dur':>5}  {'q':>2}  channel / title")
    for row in ranked[:args.top]:
        duration = to_int(row.get("duration_s"))
        print(f"  {to_int(row.get('views')):>10,}  "
              f"{(row.get('published') or '?')[:10]:<10} "
              f"{duration:>5}  {row.get('found_by', 1):>2}  "
              f"{(row.get('channel') or '?')[:22]:<22} | {(row.get('title') or '')[:70]}")

    print("\n== channels appearing most ==")
    channels = Counter(row.get("channel") or "?" for row in unique)
    for channel, count in channels.most_common(12):
        print(f"  {count:3d}  {channel}")


if __name__ == "__main__":
    main()
