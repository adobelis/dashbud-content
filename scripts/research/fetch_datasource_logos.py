#!/usr/bin/env python3
"""
Fetch square icon-only SVG logos from Simple Icons for data source panel.
Simple Icons are MIT-licensed, square, and consistent.

Usage: .venv/bin/python scripts/research/fetch_datasource_logos.py
"""
import os
import sys
from pathlib import Path

import requests

OUTPUT_DIR = Path("/Users/arthur/www/dashbud/website/dashbud-home-astro-01/src/assets/api-logos/square")

# Simple Icons CDN — returns raw SVG
# Format: https://cdn.simpleicons.org/{slug}
# With color: https://cdn.simpleicons.org/{slug}/{color}
LOGOS = {
    "google-sheets": {
        "slug": "googlesheets",
        "filename": "Google_Sheets_square.svg",
        "color": "34A853",
    },
    "airtable": {
        "slug": "airtable",
        "filename": "Airtable_square.svg",
        "color": "18BFFF",
    },
    "mysql": {
        "slug": "mysql",
        "filename": "MySQL_square.svg",
        "color": "4479A1",
    },
    "oracle": {
        "slug": "oracle",
        "filename": "Oracle_square.svg",
        "color": "F80000",
    },
    "bigquery": {
        "slug": "googlebigquery",
        "filename": "BigQuery_square.svg",
        "color": "669DF6",
    },
    "snowflake": {
        "slug": "snowflake",
        "filename": "Snowflake_square.svg",
        "color": "29B5E8",
    },
    "redshift": {
        "slug": "amazonredshift",
        "filename": "Redshift_square.svg",
        "color": "8C4FFF",
    },
}


def fetch_logo(slug, color=None):
    """Fetch SVG from Simple Icons CDN."""
    if color:
        url = f"https://cdn.simpleicons.org/{slug}/{color}"
    else:
        url = f"https://cdn.simpleicons.org/{slug}"

    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    return resp.text


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for name, info in LOGOS.items():
        out_path = OUTPUT_DIR / info["filename"]
        print(f"Fetching {name} ({info['slug']})...")

        try:
            svg = fetch_logo(info["slug"], info.get("color"))

            # Verify it's actually SVG
            if "<svg" not in svg:
                print(f"  ERROR: Response doesn't look like SVG")
                print(f"  First 200 chars: {svg[:200]}")
                continue

            out_path.write_text(svg)
            print(f"  → Saved {out_path.name} ({len(svg)} bytes)")

        except Exception as e:
            print(f"  ERROR: {e}")


if __name__ == "__main__":
    main()
