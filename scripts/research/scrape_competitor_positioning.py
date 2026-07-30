#!/usr/bin/env python3
"""
Scrape competitor product/positioning pages using Zyte API + BeautifulSoup.
Captures hero messaging, product framing, "who it's for" arguments, and
differentiator claims.

Usage: .venv/bin/python scripts/research/scrape_competitor_positioning.py [--name NAME] [--all]

Requires:
  pip install zyte-api beautifulsoup4
  ZYTE_API_KEY in .env (in content repo root)
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
OUTPUT_DIR = CONTENT_ROOT / "wiki" / "dashbud" / "comparators" / "positioning-scrapes"
ENV_PATH = CONTENT_ROOT / ".env"

# Competitor pages to scrape — focused on positioning/arguments, not connector lists
COMPETITORS = {
    "thoughtspot": {
        "label": "ThoughtSpot",
        "pages": {
            "homepage": "https://www.thoughtspot.com",
            "product": "https://www.thoughtspot.com/product",
            "spotter": "https://www.thoughtspot.com/product/spotter",
            "solutions": "https://www.thoughtspot.com/solutions",
            "why": "https://www.thoughtspot.com/why-thoughtspot",
            "customers": "https://www.thoughtspot.com/customers",
        },
    },
    "sigma": {
        "label": "Sigma Computing",
        "pages": {
            "homepage": "https://www.sigmacomputing.com",
            "product": "https://www.sigmacomputing.com/product",
            "platform": "https://www.sigmacomputing.com/product/platform",
            "solutions": "https://www.sigmacomputing.com/solutions",
            "why": "https://www.sigmacomputing.com/why-sigma",
        },
    },
    "zenlytic": {
        "label": "Zenlytic",
        "pages": {
            "homepage": "https://www.zenlytic.com",
            "product": "https://www.zenlytic.com/product",
            "why": "https://www.zenlytic.com/why-zenlytic",
            "solutions": "https://www.zenlytic.com/solutions",
            "agents": "https://www.zenlytic.com/product/agents",
        },
    },
    "omni": {
        "label": "Omni Analytics",
        "pages": {
            "homepage": "https://omni.co",
            "product": "https://omni.co/product",
            "why": "https://omni.co/why-omni",
            "solutions": "https://omni.co/solutions",
        },
    },
    "powerbi": {
        "label": "Microsoft Power BI",
        "pages": {
            "homepage": "https://www.microsoft.com/en-us/power-platform/products/power-bi",
            "product": "https://www.microsoft.com/en-us/power-platform/products/power-bi/features",
        },
    },
    "tableau": {
        "label": "Tableau",
        "pages": {
            "homepage": "https://www.tableau.com",
            "product": "https://www.tableau.com/products",
            "tableau_next": "https://www.tableau.com/products/tableau-next",
            "why": "https://www.tableau.com/why-tableau",
        },
    },
    "hex": {
        "label": "Hex",
        "pages": {
            "homepage": "https://hex.tech",
            "product": "https://hex.tech/product",
            "why": "https://hex.tech/why-hex",
            "use_cases": "https://hex.tech/use-cases",
        },
    },
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
    """Fetch a page via Zyte API with browser rendering."""
    endpoint = "https://api.zyte.com/v1/extract"
    payload = {"url": url, "browserHtml": True}
    resp = requests.post(endpoint, auth=(api_key, ""), json=payload, timeout=120)
    if resp.status_code == 404:
        return None
    resp.raise_for_status()
    return resp.json().get("browserHtml", "")


def extract_page_content(html):
    """Extract structured content from HTML."""
    soup = BeautifulSoup(html, "html.parser")

    # Remove noise
    for tag in soup(["script", "style", "noscript", "svg", "iframe"]):
        tag.decompose()

    # Title
    title_tag = soup.find("title")
    title = title_tag.get_text(strip=True) if title_tag else ""

    # Meta description
    meta_desc = ""
    meta_tag = soup.find("meta", attrs={"name": "description"})
    if meta_tag:
        meta_desc = meta_tag.get("content", "")

    # OG description
    og_desc = ""
    og_tag = soup.find("meta", attrs={"property": "og:description"})
    if og_tag:
        og_desc = og_tag.get("content", "")

    # All headings h1-h3
    headings = []
    for level in range(1, 4):
        for tag in soup.find_all(f"h{level}"):
            text = tag.get_text(separator=" ", strip=True)
            if text and len(text) < 300:
                headings.append({"level": level, "text": text})

    # Hero candidates — large text near top
    hero_texts = []
    for tag in soup.find_all(["h1", "p", "span", "div"]):
        text = tag.get_text(strip=True)
        classes = " ".join(tag.get("class", []))
        if any(kw in classes.lower() for kw in
               ["hero", "headline", "banner", "masthead", "header",
                "title", "heading", "intro", "lead"]):
            if text and 10 < len(text) < 500:
                hero_texts.append(text)

    # CTA buttons
    ctas = []
    for a in soup.find_all("a"):
        text = a.get_text(strip=True)
        href = a.get("href", "")
        combined = (text + " ".join(a.get("class", []))).lower()
        if any(kw in combined for kw in
               ["get started", "try", "demo", "sign up", "start free",
                "book", "request", "contact", "see it"]):
            if text and len(text) < 100:
                ctas.append({"text": text, "href": href})

    # Full visible text
    full_text = soup.get_text(separator=" ", strip=True)

    return {
        "title": title,
        "meta_description": meta_desc,
        "og_description": og_desc,
        "headings": headings,
        "hero_texts": list(dict.fromkeys(hero_texts))[:10],
        "ctas": ctas[:10],
        "full_text": full_text,
    }


def write_page_report(competitor, page_name, url, content):
    """Write a single page scrape report."""
    lines = [
        f"# {competitor} — {page_name}",
        f"_URL: {url}_",
        f"_Scraped: {datetime.now().isoformat()[:19]}_",
        "",
        f"**Title:** {content['title']}",
        f"**Meta:** {content['meta_description']}",
        f"**OG:** {content['og_description']}",
        "",
        "## Headings",
    ]
    for h in content["headings"]:
        indent = "  " * (h["level"] - 1)
        lines.append(f"{indent}- **h{h['level']}:** {h['text']}")

    if content["hero_texts"]:
        lines.append("\n## Hero / Lead Text")
        for t in content["hero_texts"]:
            lines.append(f"- {t}")

    if content["ctas"]:
        lines.append("\n## CTAs")
        for cta in content["ctas"]:
            lines.append(f"- **{cta['text']}** → {cta['href']}")

    lines.append("\n## Full Text (first 5000 chars)")
    lines.append("```")
    lines.append(content["full_text"][:5000])
    lines.append("```")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", help="Scrape one competitor by key")
    parser.add_argument("--all", action="store_true", help="Scrape all competitors")
    args = parser.parse_args()

    if not args.name and not args.all:
        parser.print_help()
        print(f"\nAvailable: {', '.join(sorted(COMPETITORS.keys()))}")
        sys.exit(1)

    api_key = load_api_key()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    targets = COMPETITORS if args.all else {args.name: COMPETITORS[args.name]}

    for comp_key, comp in targets.items():
        label = comp["label"]
        print(f"\n{'='*60}")
        print(f"SCRAPING: {label}")
        print(f"{'='*60}")

        all_pages = {}

        for page_name, url in comp["pages"].items():
            print(f"\n  {page_name}: {url}")
            try:
                html = fetch_page(url, api_key)
                if html is None:
                    print("    → 404")
                    all_pages[page_name] = {"url": url, "status": "404"}
                    continue

                content = extract_page_content(html)
                all_pages[page_name] = {
                    "url": url,
                    "status": "ok",
                    "content": content,
                }

                print(f"    → {len(content['headings'])} headings, "
                      f"{len(content['hero_texts'])} hero texts, "
                      f"{len(content['ctas'])} CTAs")

            except Exception as e:
                print(f"    → ERROR: {e}")
                all_pages[page_name] = {"url": url, "status": "error", "error": str(e)}

        # Write combined report for this competitor
        report_lines = [
            f"# {label} — Positioning Scrape",
            f"_Scraped: {datetime.now().isoformat()[:19]}_",
            "",
        ]

        for page_name, data in all_pages.items():
            if data["status"] == "ok":
                report_lines.append("---")
                report_lines.append("")
                report_lines.append(
                    write_page_report(label, page_name, data["url"], data["content"])
                )
                report_lines.append("")
            else:
                report_lines.append(f"## {page_name}")
                report_lines.append(f"_URL: {data['url']}_")
                report_lines.append(f"_Status: {data['status']}_")
                if "error" in data:
                    report_lines.append(f"_Error: {data['error']}_")
                report_lines.append("")

        report_path = OUTPUT_DIR / f"{comp_key}.md"
        report_path.write_text("\n".join(report_lines))
        print(f"\n  → Wrote {report_path}")

        # Also save raw JSON
        json_path = OUTPUT_DIR / f"{comp_key}.json"
        # Strip full_text from JSON to keep size reasonable
        json_data = {}
        for pn, pd in all_pages.items():
            if pd["status"] == "ok":
                c = pd["content"].copy()
                c["full_text"] = c["full_text"][:3000]
                json_data[pn] = {"url": pd["url"], "content": c}
            else:
                json_data[pn] = pd
        json_path.write_text(json.dumps(json_data, indent=2))


if __name__ == "__main__":
    main()
