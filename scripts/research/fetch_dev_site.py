#!/usr/bin/env python3
"""
Fetch Dashbud dev site pages via Zyte API for review.
Extracts headings, section text, and page structure.

Usage:
  python3 scripts/research/fetch_dev_site.py                  # homepage
  python3 scripts/research/fetch_dev_site.py --page why-dashbud
  python3 scripts/research/fetch_dev_site.py --page pricing

Requires: zyte-api beautifulsoup4 (in .venv)
"""
import argparse
import os
import sys
from pathlib import Path

import requests
from bs4 import BeautifulSoup

CONTENT_ROOT = Path("/Users/arthur/www/dashbud/content")
ENV_PATH = CONTENT_ROOT / ".env"
BASE_URL = "https://dashbud-home-dev.vercel.app"


def load_api_key():
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text().splitlines():
            if line.startswith("ZYTE_API_KEY="):
                return line.split("=", 1)[1].strip()
    key = os.environ.get("ZYTE_API_KEY")
    if key:
        return key
    print("ERROR: ZYTE_API_KEY not found in .env or environment")
    sys.exit(1)


def fetch_page(url, api_key):
    resp = requests.post(
        "https://api.zyte.com/v1/extract",
        auth=(api_key, ""),
        json={"url": url, "browserHtml": True},
        timeout=60,
    )
    resp.raise_for_status()
    return resp.json().get("browserHtml", "")


def extract_content(html):
    soup = BeautifulSoup(html, "html.parser")

    # Remove nav, header, footer, script, style
    for tag in soup.find_all(["nav", "header", "footer", "script", "style", "noscript"]):
        tag.decompose()

    sections = []

    # Walk through headings and collect content between them
    all_headings = soup.find_all(["h1", "h2", "h3", "h4"])

    for i, heading in enumerate(all_headings):
        level = int(heading.name[1])
        heading_text = heading.get_text(separator=" ", strip=True)

        # Collect text content until next heading
        content_parts = []
        for sibling in heading.find_next_siblings():
            if sibling.name in ["h1", "h2", "h3", "h4"]:
                break
            text = sibling.get_text(separator=" ", strip=True)
            if text and len(text) > 5:
                content_parts.append(text)

        sections.append({
            "level": level,
            "heading": heading_text,
            "content": content_parts[:10],  # cap to avoid huge dumps
        })

    # Also get any tables
    tables = []
    for table in soup.find_all("table"):
        rows = []
        for tr in table.find_all("tr"):
            cells = [td.get_text(separator=" ", strip=True) for td in tr.find_all(["th", "td"])]
            if any(cells):
                rows.append(cells)
        if rows:
            tables.append(rows)

    return sections, tables


def print_report(url, sections, tables):
    print(f"\n{'='*80}")
    print(f"PAGE: {url}")
    print(f"{'='*80}\n")

    for s in sections:
        indent = "  " * (s["level"] - 1)
        print(f"{indent}{'#' * s['level']} {s['heading']}")
        for line in s["content"]:
            # Truncate long lines
            if len(line) > 200:
                line = line[:200] + "..."
            print(f"{indent}  | {line}")
        print()

    if tables:
        print(f"\n--- TABLES ({len(tables)}) ---\n")
        for i, table in enumerate(tables):
            print(f"Table {i+1}:")
            for row in table:
                print(f"  | {' | '.join(row)}")
            print()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--page", default="", help="Page path (e.g. why-dashbud, pricing)")
    args = parser.parse_args()

    url = f"{BASE_URL}/{args.page}".rstrip("/")
    api_key = load_api_key()

    print(f"Fetching {url} via Zyte...")
    html = fetch_page(url, api_key)
    print(f"Got {len(html)} bytes")

    sections, tables = extract_content(html)
    print_report(url, sections, tables)


if __name__ == "__main__":
    main()
