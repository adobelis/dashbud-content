#!/usr/bin/env python3
"""
Fetch full raw HTML from a URL using Zyte API (browser rendering).
Saves to wiki/dashbud/comparators/raw-html/<name>.html

Usage: python3 fetch_raw_html.py <name> <url>
       python3 fetch_raw_html.py sigma https://www.sigmacomputing.com
"""
import base64
import json
import os
import sys
from pathlib import Path

import requests

CONTENT_ROOT = Path("/Users/arthur/www/dashbud/content")
OUTPUT_DIR = CONTENT_ROOT / "wiki" / "dashbud" / "comparators" / "raw-html"
ENV_PATH = CONTENT_ROOT / ".env"


def load_api_key():
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text().splitlines():
            if line.startswith("ZYTE_API_KEY="):
                return line.split("=", 1)[1].strip()
    return os.environ.get("ZYTE_API_KEY")


def fetch_html(url, api_key):
    resp = requests.post(
        "https://api.zyte.com/v1/extract",
        auth=(api_key, ""),
        json={"url": url, "browserHtml": True},
        timeout=90,
    )
    resp.raise_for_status()
    return resp.json().get("browserHtml", "")


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 fetch_raw_html.py <name> <url>")
        sys.exit(1)

    name = sys.argv[1]
    url = sys.argv[2]
    api_key = load_api_key()

    if not api_key:
        print("ERROR: ZYTE_API_KEY not found")
        sys.exit(1)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Fetching {name} ({url})...")
    html = fetch_html(url, api_key)

    out_path = OUTPUT_DIR / f"{name}.html"
    out_path.write_text(html)
    print(f"Saved {len(html)} chars to {out_path}")


if __name__ == "__main__":
    main()
