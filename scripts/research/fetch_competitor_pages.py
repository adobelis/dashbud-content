#!/usr/bin/env python3
"""
Fetch competitor pages via Zyte for comparison analysis.
Returns full text content structure for review.

Usage:
  python3 scripts/research/fetch_competitor_pages.py URL [URL ...]

Requires: zyte-api beautifulsoup4 (in .venv)
"""
import os
import sys
from pathlib import Path

import requests
from bs4 import BeautifulSoup

CONTENT_ROOT = Path("/Users/arthur/www/dashbud/content")
ENV_PATH = CONTENT_ROOT / ".env"


def load_api_key():
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text().splitlines():
            if line.startswith("ZYTE_API_KEY="):
                return line.split("=", 1)[1].strip()
    key = os.environ.get("ZYTE_API_KEY")
    if key:
        return key
    print("ERROR: ZYTE_API_KEY not found")
    sys.exit(1)


def fetch_page(url, api_key):
    resp = requests.post(
        "https://api.zyte.com/v1/extract",
        auth=(api_key, ""),
        json={"url": url, "browserHtml": True},
        timeout=90,
    )
    resp.raise_for_status()
    return resp.json().get("browserHtml", "")


def extract_full_text(html, url):
    soup = BeautifulSoup(html, "html.parser")

    # Remove noise
    for tag in soup.find_all(["script", "style", "noscript", "svg", "iframe"]):
        tag.decompose()

    print(f"\n{'='*80}")
    print(f"PAGE: {url}")
    print(f"{'='*80}")

    # Meta
    title = soup.find("title")
    if title:
        print(f"TITLE: {title.get_text(strip=True)}")
    meta = soup.find("meta", attrs={"name": "description"})
    if meta:
        print(f"META: {meta.get('content', '')}")
    print()

    # Walk all headings and their following content
    for heading in soup.find_all(["h1", "h2", "h3", "h4"]):
        level = int(heading.name[1])
        text = heading.get_text(separator=" ", strip=True)
        if not text or len(text) > 300:
            continue

        indent = "  " * (level - 1)
        print(f"{indent}{'#' * level} {text}")

        # Get the parent section's direct text content
        parent = heading.parent
        if parent:
            for child in parent.children:
                if child == heading:
                    continue
                if hasattr(child, 'name') and child.name in ["h1", "h2", "h3", "h4"]:
                    break
                if hasattr(child, 'get_text'):
                    t = child.get_text(separator=" ", strip=True)
                    if t and len(t) > 10 and t != text:
                        if len(t) > 300:
                            t = t[:300] + "..."
                        print(f"{indent}  | {t}")

        # Also check next siblings
        for sib in heading.find_next_siblings():
            if sib.name in ["h1", "h2", "h3", "h4"]:
                break
            t = sib.get_text(separator=" ", strip=True)
            if t and len(t) > 10 and t != text:
                if len(t) > 300:
                    t = t[:300] + "..."
                print(f"{indent}  | {t}")
        print()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 fetch_competitor_pages.py URL [URL ...]")
        sys.exit(1)

    api_key = load_api_key()

    for url in sys.argv[1:]:
        print(f"\nFetching {url}...")
        try:
            html = fetch_page(url, api_key)
            print(f"Got {len(html)} bytes")
            extract_full_text(html, url)
        except Exception as e:
            print(f"ERROR fetching {url}: {e}")


if __name__ == "__main__":
    main()
