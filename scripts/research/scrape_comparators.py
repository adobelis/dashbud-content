#!/usr/bin/env python3
"""
Scrape comparator homepages using Zyte API + BeautifulSoup.
Extracts heading structure (h1-h3), meta description, and key text sections.

Usage: python3 scrape_comparators.py [--url URL] [--all]

Requires:
  pip install zyte-api beautifulsoup4
  ZYTE_API_KEY in .env (in content repo root)
"""
import argparse
import base64
import json
import os
import sys
from datetime import datetime
from pathlib import Path

import requests
from bs4 import BeautifulSoup

# ── Config ──

CONTENT_ROOT = Path("/Users/arthur/www/dashbud/content")
OUTPUT_DIR = CONTENT_ROOT / "wiki" / "dashbud" / "comparators" / "auto-scraped"
ENV_PATH = CONTENT_ROOT / ".env"

COMPARATOR_URLS = {
    "snowflake": "https://www.snowflake.com",
    "databricks": "https://www.databricks.com",
    "fivetran": "https://www.fivetran.com",
    "dbt": "https://www.getdbt.com",
    "hex": "https://hex.tech",
    "omni": "https://www.omni.co",
    "stripe": "https://stripe.com",
    "datadog": "https://www.datadoghq.com",
    "brex": "https://www.brex.com",
    "cloudflare": "https://www.cloudflare.com",
    "toast": "https://pos.toasttab.com",
    "thoughtspot": "https://www.thoughtspot.com",
    "sigma": "https://www.sigmacomputing.com",
    "metabase": "https://www.metabase.com",
    "zenlytic": "https://www.zenlytic.com",
    "ramp": "https://ramp.com",
    "mercury": "https://mercury.com",
    "linear": "https://linear.app",
    "attio": "https://attio.com",
    "databricks-bi": "https://www.databricks.com/product/business-intelligence",
    "holistics": "https://www.holistics.io",
    "tableau": "https://www.tableau.com",
    "tableau-next":"https://www.tableau.com/products/tableau-next",
    "looker": "https://cloud.google.com/looker",
}


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


def fetch_page(url, api_key, use_browser=True):
    """Fetch a page via Zyte API. Returns HTML string."""
    endpoint = "https://api.zyte.com/v1/extract"

    payload = {"url": url}
    if use_browser:
        payload["browserHtml"] = True
    else:
        payload["httpResponseBody"] = True

    resp = requests.post(
        endpoint,
        auth=(api_key, ""),
        json=payload,
        timeout=60,
    )
    resp.raise_for_status()
    data = resp.json()

    if use_browser:
        return data.get("browserHtml", "")
    else:
        body_b64 = data.get("httpResponseBody", "")
        return base64.b64decode(body_b64).decode("utf-8", errors="replace")


def extract_structure(html, url):
    """Extract heading structure and key text from HTML."""
    soup = BeautifulSoup(html, "html.parser")

    # Meta
    title_tag = soup.find("title")
    title = title_tag.get_text(strip=True) if title_tag else ""

    meta_desc = ""
    meta_tag = soup.find("meta", attrs={"name": "description"})
    if meta_tag:
        meta_desc = meta_tag.get("content", "")

    og_title = ""
    og_tag = soup.find("meta", attrs={"property": "og:title"})
    if og_tag:
        og_title = og_tag.get("content", "")

    og_desc = ""
    og_desc_tag = soup.find("meta", attrs={"property": "og:description"})
    if og_desc_tag:
        og_desc = og_desc_tag.get("content", "")

    # Headings
    headings = []
    for level in range(1, 4):
        for tag in soup.find_all(f"h{level}"):
            text = tag.get_text(separator=" ", strip=True)
            if text and len(text) < 500:  # skip absurdly long "headings"
                headings.append({
                    "level": level,
                    "tag": f"h{level}",
                    "text": text,
                })

    # Hero section heuristic: first large text block
    hero_candidates = []
    for tag in soup.find_all(["h1", "p", "span", "div"]):
        text = tag.get_text(strip=True)
        classes = " ".join(tag.get("class", []))
        if any(kw in classes.lower() for kw in ["hero", "headline", "banner", "masthead"]):
            if text and len(text) < 500:
                hero_candidates.append({"tag": tag.name, "class": classes, "text": text})

    # CTA buttons
    ctas = []
    for a in soup.find_all("a"):
        text = a.get_text(strip=True)
        href = a.get("href", "")
        classes = " ".join(a.get("class", []))
        if any(kw in (text + classes).lower() for kw in ["get started", "try", "demo", "sign up", "start free", "book"]):
            if text and len(text) < 100:
                ctas.append({"text": text, "href": href})

    return {
        "url": url,
        "scraped": datetime.now().isoformat()[:19],
        "title": title,
        "meta_description": meta_desc,
        "og_title": og_title,
        "og_description": og_desc,
        "headings": headings,
        "hero_candidates": hero_candidates[:5],
        "ctas": ctas[:10],
    }


def write_report(name, data):
    """Write a structured markdown report."""
    lines = [
        f"# {name.title()} — Homepage Structure",
        f"_URL: {data['url']} | Scraped: {data['scraped']}_\n",
        f"## Meta",
        f"- **Title:** {data['title']}",
        f"- **Meta description:** {data['meta_description']}",
        f"- **OG title:** {data['og_title']}",
        f"- **OG description:** {data['og_description']}",
        "",
        "## Heading Structure",
    ]

    for h in data["headings"]:
        indent = "  " * (h["level"] - 1)
        lines.append(f"{indent}- **{h['tag']}:** {h['text']}")

    if data["hero_candidates"]:
        lines.append("\n## Hero Candidates (by CSS class)")
        for hc in data["hero_candidates"]:
            lines.append(f"- `{hc['tag']}.{hc['class']}`: {hc['text'][:200]}")

    if data["ctas"]:
        lines.append("\n## CTAs")
        for cta in data["ctas"]:
            lines.append(f"- **{cta['text']}** → {cta['href']}")

    report = "\n".join(lines)

    out_path = OUTPUT_DIR / f"{name}_structure.md"
    out_path.write_text(report)
    print(f"  Wrote {out_path.name}")

    # Also save raw JSON
    json_path = OUTPUT_DIR / f"{name}_structure.json"
    json_path.write_text(json.dumps(data, indent=2))

    return out_path


def main():
    parser = argparse.ArgumentParser(description="Scrape comparator homepages")
    parser.add_argument("--url", help="Scrape a single URL (provide name:url)")
    parser.add_argument("--all", action="store_true", help="Scrape all comparators")
    parser.add_argument("--name", help="Scrape a single comparator by name")
    parser.add_argument("--no-browser", action="store_true", help="Use HTTP mode instead of browser rendering")
    args = parser.parse_args()

    api_key = load_api_key()
    use_browser = not args.no_browser
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    targets = {}

    if args.all:
        targets = COMPARATOR_URLS
    elif args.name:
        name = args.name.lower()
        if name not in COMPARATOR_URLS:
            print(f"Unknown comparator: {name}")
            print(f"Available: {', '.join(sorted(COMPARATOR_URLS.keys()))}")
            sys.exit(1)
        targets = {name: COMPARATOR_URLS[name]}
    elif args.url:
        if ":" not in args.url or not args.url.startswith("http"):
            # name:url format
            parts = args.url.split(":", 1)
            if len(parts) == 2 and not parts[1].startswith("//"):
                targets = {parts[0]: parts[1]}
            else:
                print("Use --url name:https://example.com")
                sys.exit(1)
        else:
            print("Use --url name:https://example.com")
            sys.exit(1)
    else:
        parser.print_help()
        sys.exit(1)

    for name, url in targets.items():
        print(f"\nScraping {name} ({url})...")
        try:
            html = fetch_page(url, api_key, use_browser=use_browser)
            data = extract_structure(html, url)
            write_report(name, data)
            print(f"  {len(data['headings'])} headings, {len(data['ctas'])} CTAs found")
        except Exception as e:
            print(f"  ERROR: {e}")


if __name__ == "__main__":
    main()
