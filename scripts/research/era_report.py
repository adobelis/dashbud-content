"""Report the enriched corpus by capability era and level, to guide sampling.

Only rows with date_source=video_info are included: derived dates are wrong by
up to a year and must never enter a dated analysis.

Eras (see tutorials/_coding-scheme.md):
  E1-prefile      before 2023-07   chat only, data pasted as text
  E2-codeinterp   2023-07..2024-12 file upload, sandboxed code execution
  E3-gpts-agents  2025             custom GPTs, n8n/Make, vibe-coding arrives
  E4-connectors   2026             connectors, scheduled reports, agent modes

Usage: python era_report.py SHORTLIST.tsv [--by level|era]
"""
import csv
import argparse
import datetime
from collections import defaultdict, Counter

TODAY = datetime.date(2026, 11, 9)


def to_int(value):
    try:
        return int(str(value).strip())
    except (TypeError, ValueError):
        return 0


def era_of(published):
    if not published or len(published) < 7:
        return "unknown"
    if published < "2023-07":
        return "E1-prefile"
    if published < "2025-01":
        return "E2-codeinterp"
    if published < "2026-01":
        return "E3-gpts-agents"
    return "E4-connectors"


def months_live(published):
    try:
        date = datetime.date.fromisoformat(published)
    except (ValueError, TypeError):
        return 0
    return max(1, (TODAY - date).days / 30.44)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("--by", default="level", choices=["level", "era"])
    args = parser.parse_args()

    with open(args.path, newline="") as handle:
        rows = [r for r in csv.DictReader(handle, delimiter="\t")
                if r.get("date_source") == "video_info"]

    for row in rows:
        row["era"] = era_of(row.get("published", ""))
        row["vpm"] = int(to_int(row.get("views")) / months_live(row.get("published", "")))

    print(f"{len(rows)} rows with verified dates\n")

    print("== era x level ==")
    eras = ["E1-prefile", "E2-codeinterp", "E3-gpts-agents", "E4-connectors", "unknown"]
    levels = sorted({r["level"] for r in rows})
    header = "  " + " ".join(f"{e.split('-')[0]:>6}" for e in eras)
    print(f"  {'level':<20}{header}   total")
    for level in levels:
        counts = [sum(1 for r in rows if r["level"] == level and r["era"] == era)
                  for era in eras]
        cells = " ".join(f"{c:>6}" for c in counts)
        print(f"  {level:<20}  {cells}   {sum(counts):>5}")
    totals = [sum(1 for r in rows if r["era"] == era) for era in eras]
    print(f"  {'TOTAL':<20}  {' '.join(f'{t:>6}' for t in totals)}   {len(rows):>5}")

    key = args.by
    print(f"\n== detail by {key} ==")
    grouped = defaultdict(list)
    for row in rows:
        grouped[row[key]].append(row)
    for group in sorted(grouped):
        print(f"\n--- {group} ({len(grouped[group])}) ---")
        for row in sorted(grouped[group], key=lambda r: r.get("published", "")):
            print(f"  {row.get('published')}  {row['era']:<14} "
                  f"{to_int(row.get('views')):>9,}v {row['vpm']:>7,}/mo "
                  f"{to_int(row.get('likes')):>7,}L {to_int(row.get('comment_count')):>5,}C  "
                  f"{row.get('video_id')}  {(row.get('title') or '')[:52]}")


if __name__ == "__main__":
    main()
