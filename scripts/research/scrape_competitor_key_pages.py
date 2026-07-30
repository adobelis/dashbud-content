#!/usr/bin/env python3
"""
Fetch specific key pages from competitor sites for positioning research.
Curated list — product, solutions, comparison, and positioning pages only.

Usage: .venv/bin/python scripts/research/scrape_competitor_key_pages.py [--name NAME] [--all]
"""
import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path

import requests
from bs4 import BeautifulSoup

CONTENT_ROOT = Path("/Users/arthur/www/dashbud/content")
PAGES_DIR = CONTENT_ROOT / "wiki" / "dashbud" / "comparators" / "full-pages"
ENV_PATH = CONTENT_ROOT / ".env"

# Curated key pages per competitor — positioning-relevant only
KEY_PAGES = {
    "thoughtspot": [
        "https://www.thoughtspot.com",
        "https://www.thoughtspot.com/product/agents",
        "https://www.thoughtspot.com/product/agents/spotter",
        "https://www.thoughtspot.com/product/agents/spottermodel",
        "https://www.thoughtspot.com/product/agents/spotterviz",
        "https://www.thoughtspot.com/product/analytics",
        "https://www.thoughtspot.com/product/spotter-semantics",
        "https://www.thoughtspot.com/product/connect",
        "https://www.thoughtspot.com/product/visualize",
        "https://www.thoughtspot.com/product/automated-analytics",
        "https://www.thoughtspot.com/product/actionable-analytics",
        "https://www.thoughtspot.com/why-thoughtspot",
        "https://www.thoughtspot.com/compare",
        "https://www.thoughtspot.com/business-leader",
        "https://www.thoughtspot.com/data-leader",
        "https://www.thoughtspot.com/analyst",
        "https://www.thoughtspot.com/pricing",
        "https://www.thoughtspot.com/solutions/financial-analytics",
        "https://www.thoughtspot.com/solutions/healthcare-life-sciences-analytics",
        "https://www.thoughtspot.com/solutions/retail-cpg-analytics",
        "https://www.thoughtspot.com/solutions/supply-chain-analytics",
    ],
    "sigma": [
        "https://www.sigmacomputing.com",
        "https://www.sigmacomputing.com/product/why-sigma",
        "https://www.sigmacomputing.com/product/business-intelligence",
        "https://www.sigmacomputing.com/product/ai",
        "https://www.sigmacomputing.com/product/ai-applications",
        "https://www.sigmacomputing.com/product/agents",
        "https://www.sigmacomputing.com/product/architecture",
        "https://www.sigmacomputing.com/product/data-modeling",
        "https://www.sigmacomputing.com/product/self-service",
        "https://www.sigmacomputing.com/product/spreadsheets",
        "https://www.sigmacomputing.com/product/dashboards",
        "https://www.sigmacomputing.com/product/reporting",
        "https://www.sigmacomputing.com/product/embedded-analytics",
        "https://www.sigmacomputing.com/comparison",
        "https://www.sigmacomputing.com/comparison/sigma-vs-tableau",
        "https://www.sigmacomputing.com/comparison/sigma-vs-power-bi",
        "https://www.sigmacomputing.com/comparison/sigma-vs-thoughtspot",
        "https://www.sigmacomputing.com/comparison/sigma-vs-looker",
        "https://www.sigmacomputing.com/use-cases/finance",
        "https://www.sigmacomputing.com/use-cases/healthcare",
        "https://www.sigmacomputing.com/use-cases/manufacturing",
        "https://www.sigmacomputing.com/use-cases/sales",
    ],
    "omni": [
        "https://omni.co",
        "https://omni.co/ai",
        "https://omni.co/business-intelligence",
        "https://omni.co/embedded-analytics",
        "https://omni.co/context-modeling",
        "https://omni.co/data-modeling",
        "https://omni.co/data-input",
        "https://omni.co/calculations",
        "https://omni.co/integrations",
        "https://omni.co/compare",
        "https://omni.co/omni-vs-looker",
        "https://omni.co/omni-vs-tableau",
        "https://omni.co/omni-vs-power-bi",
        "https://omni.co/omni-vs-sigma",
        "https://omni.co/omni-vs-thoughtspot",
        "https://omni.co/omni-vs-hex",
        "https://omni.co/industry/financial-services",
        "https://omni.co/industry/retail",
        "https://omni.co/industry/saas",
        "https://omni.co/industry/media-advertising",
        "https://omni.co/about",
        "https://omni.co/snowflake",
        "https://omni.co/databricks",
    ],
}


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
    endpoint = "https://api.zyte.com/v1/extract"
    payload = {"url": url, "browserHtml": True}
    resp = requests.post(endpoint, auth=(api_key, ""), json=payload, timeout=120)
    if resp.status_code == 404:
        return None
    resp.raise_for_status()
    return resp.json().get("browserHtml", "")


def extract_content(html):
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "noscript", "svg", "iframe"]):
        tag.decompose()

    title_tag = soup.find("title")
    title = title_tag.get_text(strip=True) if title_tag else ""

    meta_desc = ""
    meta_tag = soup.find("meta", attrs={"name": "description"})
    if meta_tag:
        meta_desc = meta_tag.get("content", "")

    # Try main content area
    main = soup.find("main") or soup.find("article") or soup.find(role="main")
    source = main if main else (soup.find("body") or soup)

    headings = []
    for level in range(1, 5):
        for tag in source.find_all(f"h{level}"):
            text = tag.get_text(separator=" ", strip=True)
            if text and len(text) < 300:
                headings.append({"level": level, "text": text})

    full_text = source.get_text(separator="\n", strip=True)

    return title, meta_desc, headings, full_text


def fetch_competitor(api_key, name):
    urls = KEY_PAGES[name]
    comp_dir = PAGES_DIR / name
    comp_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n{'='*60}")
    print(f"Fetching {len(urls)} key pages for {name}")
    print(f"{'='*60}")

    for url in urls:
        from urllib.parse import urlparse
        parsed = urlparse(url)
        path = parsed.path.strip("/").replace("/", "_") or "homepage"
        out_path = comp_dir / f"{path}.md"

        if out_path.exists():
            print(f"  SKIP (exists): {parsed.path or '/'}")
            continue

        print(f"  Fetching: {parsed.path or '/'}")
        try:
            html = fetch_page(url, api_key)
            if not html:
                print(f"    → 404")
                out_path.write_text(f"# {url}\n\n_404 Not Found_\n")
                continue

            title, meta, headings, text = extract_content(html)

            lines = [
                f"# {title}",
                f"_URL: {url}_",
                f"_Fetched: {datetime.now().isoformat()[:19]}_",
                f"_Meta: {meta}_",
                "",
                "## Headings",
            ]
            for h in headings:
                indent = "  " * (h["level"] - 1)
                lines.append(f"{indent}- **h{h['level']}:** {h['text']}")

            lines.append("")
            lines.append("## Content")
            lines.append("")
            lines.append(text)

            out_path.write_text("\n".join(lines))
            print(f"    → {len(headings)} headings, {len(text)} chars")

        except Exception as e:
            print(f"    → ERROR: {e}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", help="Single competitor")
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()

    api_key = load_api_key()

    if args.all:
        for name in KEY_PAGES:
            fetch_competitor(api_key, name)
    elif args.name:
        if args.name not in KEY_PAGES:
            print(f"Unknown: {args.name}. Available: {', '.join(KEY_PAGES)}")
            sys.exit(1)
        fetch_competitor(api_key, args.name)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
