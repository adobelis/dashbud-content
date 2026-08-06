#!/usr/bin/env python3
"""
Save full text content of Dashbud dev site pages locally via Zyte.

Usage:
  python3 scripts/research/save_site_content.py

Saves to website/_snapshots/
"""
import os
import sys
from pathlib import Path
from datetime import datetime

import requests
from bs4 import BeautifulSoup, NavigableString

CONTENT_ROOT = Path("/Users/arthur/www/dashbud/content")
ENV_PATH = CONTENT_ROOT / ".env"
OUTPUT_DIR = CONTENT_ROOT / "website" / "_snapshots"
BASE_URL = "https://dashbud-home-dev.vercel.app"

PAGES = [
    ("homepage", ""),
    ("why-dashbud", "why-dashbud"),
    ("who-its-for", "who-its-for"),
    ("pricing", "pricing"),
]


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


def extract_content(html):
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup.find_all(["script", "style", "noscript", "svg", "iframe"]):
        tag.decompose()

    lines = []

    body = soup.find("body")
    if not body:
        return "No body found"

    for element in body.descendants:
        if isinstance(element, NavigableString):
            continue
        if not hasattr(element, 'name'):
            continue
        if element.name in ["script", "style", "noscript", "svg", "iframe", "img",
                            "video", "source", "link", "meta", "br", "hr"]:
            continue

        if element.name in ["h1", "h2", "h3", "h4", "h5"]:
            text = element.get_text(separator=" ", strip=True)
            if text and len(text) < 300:
                level = int(element.name[1])
                lines.append("")
                lines.append(f"{'#' * level} {text}")
                lines.append("")

        elif element.name in ["p"]:
            text = element.get_text(separator=" ", strip=True)
            if text and len(text) > 10:
                parent_heading = element.find_parent(["h1", "h2", "h3", "h4"])
                if not parent_heading:
                    lines.append(text)
                    lines.append("")

        elif element.name == "li":
            text = element.get_text(separator=" ", strip=True)
            if text and len(text) > 5 and len(text) < 500:
                # Only direct li, not nested
                if not element.find_parent("li"):
                    lines.append(f"- {text}")

        elif element.name in ["td", "th"]:
            text = element.get_text(separator=" ", strip=True)
            if text and len(text) > 2:
                lines.append(f"| {text}")

        elif element.name == "tr":
            lines.append("")

        elif element.name == "code":
            text = element.get_text(strip=True)
            if text and len(text) < 100:
                lines.append(f"`{text}`")

    return "\n".join(lines)


def main():
    api_key = load_api_key()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d")

    for name, path in PAGES:
        url = f"{BASE_URL}/{path}".rstrip("/")
        print(f"Fetching {name} ({url})...")
        try:
            html = fetch_page(url, api_key)
            content = extract_content(html)

            out_path = OUTPUT_DIR / f"{name}_{timestamp}.md"
            out_path.write_text(f"# {name} — {url}\n_Snapshot: {timestamp}_\n\n{content}")
            print(f"  Saved to {out_path.name} ({len(content)} chars)")
        except Exception as e:
            print(f"  ERROR: {e}")


if __name__ == "__main__":
    main()
