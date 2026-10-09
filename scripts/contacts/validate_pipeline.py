#!/usr/bin/env python3
"""Validate pipeline.csv parses cleanly and report deal stages.

Usage: .venv/bin/python scripts/contacts/validate_pipeline.py
"""
import csv
from pathlib import Path

PIPELINE = Path(__file__).resolve().parents[2] / "outreach" / "crm" / "pipeline.csv"

# Must match the deal stages documented in outreach/crm/README.md
VALID_STAGES = {
    "exploratory",
    "demo_done",
    "poc",
    "trial",
    "proposal",
    "security_review",
    "closed_won",
    "closed_lost",
    "dormant",
}


def main() -> None:
    with PIPELINE.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))

    header_len = len(rows[0].keys()) if rows else 0
    print(f"Parsed {len(rows)} rows, {header_len} columns\n")

    for row in rows:
        if None in row.values() or any(v is None for v in row.values()):
            print(f"  !! RAGGED ROW: {row.get('deal_id')}")
        print(
            f"  {row['deal_id']:<5} {row['company']:<32} "
            f"{row['stage']:<16} arr={row['arr'] or '-':<12} "
            f"last_activity={row['last_activity'] or '-'}"
        )

    bad = [r for r in rows if r["stage"] not in VALID_STAGES]
    if bad:
        print("\n!! UNDOCUMENTED STAGES (not in README enum):")
        for row in bad:
            print(f"  {row['deal_id']} {row['company']}: '{row['stage']}'")
    else:
        print("\nAll stages valid per README enum.")

    stages = {}
    for row in rows:
        stages[row["stage"]] = stages.get(row["stage"], 0) + 1
    print("\nStage counts:")
    for stage, count in sorted(stages.items()):
        print(f"  {stage}: {count}")


if __name__ == "__main__":
    main()
