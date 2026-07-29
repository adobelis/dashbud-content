#!/usr/bin/env python3
"""
Scrape competitor data source / connector pages using Zyte API + BeautifulSoup.
Checks what connectors ThoughtSpot, Sigma, Fivetran, Airbyte, Power BI, and Tableau
currently claim to support — focused on ERP/legacy systems relevant to our research.

Usage: .venv/bin/python scripts/research/scrape_connector_pages.py

Requires:
  pip install zyte-api beautifulsoup4
  ZYTE_API_KEY in .env (in content repo root)
"""
import base64
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

import requests
from bs4 import BeautifulSoup

# ── Config ──

CONTENT_ROOT = Path("/Users/arthur/www/dashbud/content")
OUTPUT_DIR = CONTENT_ROOT / "wiki" / "dashbud" / "research" / "erp-connectivity" / "competitor-scrapes"
ENV_PATH = CONTENT_ROOT / ".env"

# Pages to scrape — data source / connector listing pages
TARGETS = {
    # BI Tools — data source pages
    "thoughtspot_connections": "https://docs.thoughtspot.com/cloud/latest/connections",
    "thoughtspot_connectors": "https://www.thoughtspot.com/connectors",
    "sigma_connections": "https://help.sigmacomputing.com/docs/connect-to-data-sources",
    "sigma_integrations": "https://www.sigmacomputing.com/integrations",
    "powerbi_connectors": "https://learn.microsoft.com/en-us/power-bi/connect-data/power-bi-data-sources",

    # ETL Tools — connector catalogs
    "fivetran_connectors": "https://www.fivetran.com/connectors",
    "fivetran_erp": "https://www.fivetran.com/connectors/connector-types/erp",
    "airbyte_connectors": "https://airbyte.com/connectors",
}

# ERP/legacy keywords to search for in page content
ERP_KEYWORDS = [
    "informix", "sap", "hana", "oracle", "ebs", "e-business",
    "jd edwards", "jde", "dynamics", "dynamics gp", "dynamics nav",
    "business central", "sage", "intacct", "netsuite",
    "epicor", "kinetic", "prophet 21", "infor", "syteline",
    "cloudsuite", "lawson", "epic", "cerner", "athenahealth",
    "square", "toast", "lightspeed", "clover",
    "sql server", "postgresql", "mysql", "google sheets",
    "snowflake", "bigquery", "redshift", "databricks",
]


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
    """Fetch a page via Zyte API with browser rendering. Returns HTML string."""
    endpoint = "https://api.zyte.com/v1/extract"
    payload = {"url": url, "browserHtml": True}

    resp = requests.post(
        endpoint,
        auth=(api_key, ""),
        json=payload,
        timeout=90,
    )
    resp.raise_for_status()
    data = resp.json()
    return data.get("browserHtml", "")


def extract_text_content(html):
    """Extract all visible text from HTML."""
    soup = BeautifulSoup(html, "html.parser")

    # Remove script/style elements
    for tag in soup(["script", "style", "noscript", "svg"]):
        tag.decompose()

    return soup.get_text(separator=" ", strip=True)


def find_erp_mentions(text, url):
    """Search for ERP-related keywords in page text."""
    text_lower = text.lower()
    found = {}
    for kw in ERP_KEYWORDS:
        # Find all occurrences with surrounding context
        pattern = re.compile(
            r'(.{0,80}' + re.escape(kw) + r'.{0,80})',
            re.IGNORECASE
        )
        matches = pattern.findall(text)
        if matches:
            # Deduplicate and limit
            unique = list(dict.fromkeys(m.strip() for m in matches))[:5]
            found[kw] = unique
    return found


def extract_connector_list(html):
    """Try to extract a structured list of connectors/data sources from the page."""
    soup = BeautifulSoup(html, "html.parser")
    connectors = []

    # Look for list items, cards, or links that might be connector names
    # Common patterns: <li>, <a> with connector-like classes, cards with titles
    for tag in soup.find_all(["li", "a", "h3", "h4", "span", "div"]):
        text = tag.get_text(strip=True)
        classes = " ".join(tag.get("class", []))

        # Skip very long text (not a connector name) or very short
        if not text or len(text) > 80 or len(text) < 3:
            continue

        # Check if it matches any ERP keyword
        text_lower = text.lower()
        for kw in ERP_KEYWORDS:
            if kw in text_lower:
                connectors.append({"text": text, "keyword": kw, "tag": tag.name})
                break

    # Deduplicate
    seen = set()
    unique = []
    for c in connectors:
        key = c["text"].lower()
        if key not in seen:
            seen.add(key)
            unique.append(c)

    return unique


def write_report(name, url, mentions, connector_list, raw_text_snippet):
    """Write a structured report for one scraped page."""
    lines = [
        f"# {name} — Connector/Data Source Page Scrape",
        f"_URL: {url}_",
        f"_Scraped: {datetime.now().isoformat()[:19]}_",
        "",
    ]

    if connector_list:
        lines.append("## ERP/Legacy Connectors Found on Page")
        lines.append("")
        for c in connector_list:
            lines.append(f"- **{c['text']}** (matched keyword: `{c['keyword']}`, tag: `{c['tag']}`)")
        lines.append("")

    lines.append("## Keyword Mentions in Page Content")
    lines.append("")

    if not mentions:
        lines.append("_No ERP/legacy keywords found on this page._")
    else:
        for kw, contexts in sorted(mentions.items()):
            lines.append(f"### `{kw}`")
            for ctx in contexts:
                # Clean up whitespace
                ctx_clean = " ".join(ctx.split())
                lines.append(f"- ...{ctx_clean}...")
            lines.append("")

    # Include a text snippet for manual review
    lines.append("## Raw Text Snippet (first 3000 chars)")
    lines.append("```")
    lines.append(raw_text_snippet[:3000])
    lines.append("```")

    report = "\n".join(lines)
    out_path = OUTPUT_DIR / f"{name}.md"
    out_path.write_text(report)
    print(f"  Wrote {out_path.name}")
    return out_path


def main():
    api_key = load_api_key()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    results_summary = {}

    for name, url in TARGETS.items():
        print(f"\nScraping {name} ({url})...")
        try:
            html = fetch_page(url, api_key)
            text = extract_text_content(html)
            mentions = find_erp_mentions(text, url)
            connector_list = extract_connector_list(html)
            write_report(name, url, mentions, connector_list, text)

            # Track for summary
            results_summary[name] = {
                "url": url,
                "keywords_found": list(mentions.keys()),
                "connector_matches": [c["text"] for c in connector_list],
                "page_length": len(text),
            }

            print(f"  Found {len(mentions)} keyword matches, {len(connector_list)} connector entries")
        except Exception as e:
            print(f"  ERROR: {e}")
            results_summary[name] = {"url": url, "error": str(e)}

    # Write combined summary JSON
    summary_path = OUTPUT_DIR / "_summary.json"
    summary_path.write_text(json.dumps(results_summary, indent=2))
    print(f"\nSummary written to {summary_path}")

    # Print quick overview
    print("\n" + "=" * 60)
    print("QUICK OVERVIEW — ERP keyword coverage by competitor")
    print("=" * 60)
    for name, data in results_summary.items():
        if "error" in data:
            print(f"\n{name}: ERROR — {data['error']}")
        else:
            kws = data["keywords_found"]
            print(f"\n{name}:")
            if kws:
                print(f"  Keywords found: {', '.join(kws)}")
            else:
                print("  No ERP/legacy keywords found")
            if data["connector_matches"]:
                print(f"  Connector entries: {', '.join(data['connector_matches'][:10])}")


if __name__ == "__main__":
    main()
