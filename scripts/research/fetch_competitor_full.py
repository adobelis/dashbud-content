#!/usr/bin/env python3
"""
Fetch competitor pages via Zyte — full text extraction for content analysis.
Outputs heading structure + all meaningful text content.

Usage:
  python3 scripts/research/fetch_competitor_full.py URL [URL ...]

Requires: beautifulsoup4 requests (in .venv)
"""
import os
import sys
from pathlib import Path

import requests
from bs4 import BeautifulSoup, NavigableString

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


def extract_text(html, url):
    soup = BeautifulSoup(html, "html.parser")

    # Remove noise
    for tag in soup.find_all(["script", "style", "noscript", "svg", "iframe"]):
        tag.decompose()

    # Get title and meta
    title = soup.find("title")
    meta = soup.find("meta", attrs={"name": "description"})

    print(f"\n{'='*80}")
    print(f"PAGE: {url}")
    print(f"TITLE: {title.get_text(strip=True) if title else 'N/A'}")
    print(f"META: {meta.get('content', '') if meta else 'N/A'}")
    print(f"{'='*80}\n")

    # Walk the DOM in order, extracting meaningful text blocks
    body = soup.find("body")
    if not body:
        print("No body found")
        return

    for element in body.descendants:
        if isinstance(element, NavigableString):
            continue
        if element.name in ["script", "style", "noscript", "svg", "iframe", "img", "video", "source", "link", "meta"]:
            continue

        # Headings
        if element.name in ["h1", "h2", "h3", "h4", "h5"]:
            text = element.get_text(separator=" ", strip=True)
            if text and len(text) < 300:
                level = int(element.name[1])
                indent = "  " * (level - 1)
                print(f"{indent}{'#' * level} {text}")
                print()

        # Paragraphs and list items with direct text
        elif element.name in ["p", "li"]:
            text = element.get_text(separator=" ", strip=True)
            if text and len(text) > 15 and len(text) < 500:
                # Check it's not just a child of something we already printed
                parent_heading = element.find_parent(["h1", "h2", "h3", "h4"])
                if not parent_heading:
                    print(f"  | {text}")
                    print()

        # Buttons and CTAs
        elif element.name in ["a", "button"]:
            text = element.get_text(strip=True)
            href = element.get("href", "")
            classes = " ".join(element.get("class", []))
            if text and len(text) < 60 and any(kw in (text + classes).lower() for kw in ["demo", "try", "start", "get started", "sign up", "book", "request", "contact", "cta", "btn-primary", "button-primary"]):
                print(f"  [CTA] {text} → {href}")
                print()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 fetch_competitor_full.py URL [URL ...]")
        sys.exit(1)

    api_key = load_api_key()

    for url in sys.argv[1:]:
        print(f"\nFetching {url}...")
        try:
            html = fetch_page(url, api_key)
            print(f"Got {len(html)} bytes")
            extract_text(html, url)
        except Exception as e:
            print(f"ERROR fetching {url}: {e}")


if __name__ == "__main__":
    main()
