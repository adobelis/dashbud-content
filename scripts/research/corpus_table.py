"""Summary table of the enriched tutorial corpus, sorted by views.

Only rows with date_source=video_info are included; search-derived dates are
wrong by up to a year and must never enter a dated analysis.

On normalising reach across dates: "views in the first N months" is NOT
computable -- YouTube exposes only cumulative views, with no time series, so a
2023 video's early trajectory cannot be reconstructed. Two things that do work:

  age_cohort     compare only within an age band (apples to apples)
  per-1k ratios  likes and comments per 1,000 views are roughly age-stable,
                 since they accrue alongside views, so they ARE comparable
                 across eras -- unlike any per-month figure

`v/mo` is reported for reference but is a lifetime average, dominated by the
launch spike for older videos. Comparable within an age cohort, not across,
and suppressed under one month where the arithmetic explodes.

Usage: python corpus_table.py SHORTLIST.tsv [--out FILE.md] [--limit N]
"""
import csv
import argparse
import datetime
from collections import Counter

TODAY = datetime.date(2026, 11, 9)

ERAS = [
    ("E1", "2000-01", "2023-07", "chat only; data pasted as text"),
    ("E2", "2023-07", "2025-01", "file upload, sandboxed code execution"),
    ("E3", "2025-01", "2026-01", "custom GPTs, n8n/Make, vibe-coding arrives"),
    ("E4", "2026-01", "9999-99", "connectors, scheduled reports, agent modes"),
]

COHORTS = [(0, 3, "0-3mo"), (3, 6, "3-6mo"), (6, 12, "6-12mo"),
           (12, 24, "1-2yr"), (24, 9999, "2yr+")]


def to_int(value):
    try:
        return int(str(value).strip())
    except (TypeError, ValueError):
        return 0


def era_of(published):
    for name, start, end, _note in ERAS:
        if start <= published[:7] < end:
            return name
    return "?"


def age_months(published):
    try:
        date = datetime.date.fromisoformat(published)
    except (ValueError, TypeError):
        return 0.0
    return max(0.1, (TODAY - date).days / 30.44)


def cohort_of(months):
    for low, high, label in COHORTS:
        if low <= months < high:
            return label
    return "?"


def median(values):
    values = sorted(values)
    return values[len(values) // 2] if values else 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("--out")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--since", default="2022-11-30",
                        help="drop videos published before this (ChatGPT launch)")
    parser.add_argument("--drop-levels", default="",
                        help="comma-separated levels to exclude")
    args = parser.parse_args()

    with open(args.path, newline="") as handle:
        rows = [r for r in csv.DictReader(handle, delimiter="\t")
                if r.get("date_source") == "video_info"]

    for row in rows:
        published = row.get("published", "")
        views = to_int(row.get("views"))
        months = age_months(published)
        row["_views"] = views
        row["_era"] = era_of(published)
        row["_age"] = months
        row["_cohort"] = cohort_of(months)
        # under a month, a few days of views over a fraction of a month
        # explodes into a meaningless number -- suppress it
        row["_vpm"] = f"{int(views / months):,}" if months >= 1 else "—"
        row["_lk"] = (to_int(row.get("likes")) * 1000 / views) if views else 0
        row["_ck"] = (to_int(row.get("comment_count")) * 1000 / views) if views else 0
        # likes genuinely absent is a data gap, not a real zero
        row["_lk_s"] = f"{row['_lk']:.1f}" if to_int(row.get("likes")) else "n/a"

    rows = [r for r in rows if r.get("published", "") >= args.since]
    dropped = {x for x in args.drop_levels.split(",") if x}
    rows = [r for r in rows if r.get("level") not in dropped]

    rows.sort(key=lambda r: r["_views"], reverse=True)
    if args.limit:
        rows = rows[:args.limit]

    lines = []
    add = lines.append
    add(f"# Tutorial corpus — enriched pool ({len(rows)} videos)")
    add("")
    add(f"Generated {TODAY.isoformat()}. Sorted by views. "
        "All dates verified via `video_info`.")
    add("")
    add("`L/1k` = likes per 1,000 views, `C/1k` = comments per 1,000 views — "
        "age-stable, so comparable across eras. `v/mo` is a lifetime average: "
        "compare only within an age cohort, and it is suppressed under one "
        "month old. Title links to the video.")
    add("")
    add("| # | views | v/mo | age | era | level | L/1k | C/1k | dur | published | channel | title |")
    add("|--:|--:|--:|:--|:--|:--|--:|--:|--:|:--|:--|:--|")
    for index, row in enumerate(rows, 1):
        duration = to_int(row.get("duration_s"))
        title = (row.get("title") or "").replace("|", "/").replace("[", "(").replace("]", ")")
        # always canonical: the search-result url carries &pp= tracking params
        url = "https://www.youtube.com/watch?v=" + (row.get("video_id") or "")
        add(f"| {index} | {row['_views']:,} | {row['_vpm']} | "
            f"{row['_cohort']} | {row['_era']} | "
            f"{(row.get('level') or '').replace('-', ' ', 1)} | "
            f"{row['_lk_s']} | {row['_ck']:.2f} | "
            f"{duration // 60}m | {row.get('published')} | "
            f"{(row.get('channel') or '')[:20]} | "
            f"[{title[:62]}]({url}) |")
    add("")

    add("## By era")
    add("")
    add("| era | window | n | median views | median L/1k | median C/1k | what was available |")
    add("|:--|:--|--:|--:|--:|--:|:--|")
    for name, start, end, note in ERAS:
        group = [r for r in rows if r["_era"] == name]
        if not group:
            add(f"| {name} | {start}..{end} | 0 | — | — | — | {note} |")
            continue
        add(f"| {name} | {start}..{end} | {len(group)} | "
            f"{median([r['_views'] for r in group]):,} | "
            f"{median([r['_lk'] for r in group]):.1f} | "
            f"{median([r['_ck'] for r in group]):.2f} | {note} |")
    add("")

    add("## By age cohort")
    add("")
    add("Within a cohort, raw views are directly comparable.")
    add("")
    add("| cohort | n | median views | max views |")
    add("|:--|--:|--:|--:|")
    for _, _, label in COHORTS:
        group = [r for r in rows if r["_cohort"] == label]
        if not group:
            continue
        views = sorted(r["_views"] for r in group)
        add(f"| {label} | {len(group)} | {median(views):,} | {views[-1]:,} |")
    add("")

    add("## By level")
    add("")
    add("Level is descriptive here, not a sampling key — the pool is sorted by "
        "views regardless of level. A thin level means few of its videos are "
        "watched much, which is itself a finding.")
    add("")
    add("| level | n | total views | median views |")
    add("|:--|--:|--:|--:|")
    counts = Counter(r.get("level") for r in rows)
    for level in sorted(counts):
        group = [r for r in rows if r.get("level") == level]
        views = [r["_views"] for r in group]
        add(f"| {level} | {counts[level]} | {sum(views):,} | {median(views):,} |")
    add("")

    text = "\n".join(lines)
    if args.out:
        with open(args.out, "w") as handle:
            handle.write(text + "\n")
        print(f"wrote {args.out} ({len(rows)} videos)")
    else:
        print(text)


if __name__ == "__main__":
    main()
