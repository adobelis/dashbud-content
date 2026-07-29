#!/usr/bin/env python3
"""
Scrape specific competitor connector/data-source pages using Zyte API.
Targeted at verifying ERP/legacy system claims in our research articles.

Usage: .venv/bin/python scripts/research/scrape_connector_pages_v2.py
"""
import json
import os
import sys
from datetime import datetime
from pathlib import Path

import requests
from bs4 import BeautifulSoup

CONTENT_ROOT = Path("/Users/arthur/www/dashbud/content")
OUTPUT_DIR = CONTENT_ROOT / "wiki" / "dashbud" / "research" / "erp-connectivity" / "competitor-scrapes"
ENV_PATH = CONTENT_ROOT / ".env"

# More targeted pages — specific connector detail and listing pages
TARGETS = {
    # ThoughtSpot — their actual supported connection types docs
    "thoughtspot_sap_hana": "https://docs.thoughtspot.com/cloud/latest/connections-sap-hana",
    "thoughtspot_oracle": "https://docs.thoughtspot.com/cloud/latest/connections-oracle",
    "thoughtspot_sqlserver": "https://docs.thoughtspot.com/cloud/latest/connections-sql-server",

    # Sigma — their full connection docs
    "sigma_sqlserver": "https://help.sigmacomputing.com/docs/connect-to-sql-server",
    "sigma_mysql": "https://help.sigmacomputing.com/docs/connect-to-mysql",
    "sigma_postgresql": "https://help.sigmacomputing.com/docs/connect-to-postgresql",

    # Fivetran — specific ERP connector pages
    "fivetran_sap": "https://fivetran.com/docs/connectors/applications/sap",
    "fivetran_netsuite": "https://fivetran.com/docs/connectors/applications/netsuite",
    "fivetran_sage_intacct": "https://fivetran.com/docs/connectors/applications/sage-intacct",
    "fivetran_oracle_ebs": "https://fivetran.com/docs/connectors/applications/oracle-ebs",
    "fivetran_dynamics365": "https://fivetran.com/docs/connectors/applications/dynamics-365",
    "fivetran_epicor": "https://fivetran.com/docs/connectors/applications/epicor",
    "fivetran_square": "https://fivetran.com/docs/connectors/applications/square",
    "fivetran_toast": "https://fivetran.com/docs/connectors/applications/toast",
    "fivetran_lightspeed": "https://fivetran.com/docs/connectors/applications/lightspeed",

    # Airbyte — specific connector pages
    "airbyte_netsuite": "https://docs.airbyte.com/integrations/sources/netsuite",
    "airbyte_sap": "https://docs.airbyte.com/integrations/sources/sap-business-bydesign",
    "airbyte_square": "https://airbyte.com/connectors/square",
    "airbyte_oracle": "https://docs.airbyte.com/integrations/sources/oracle",
    "airbyte_mssql": "https://docs.airbyte.com/integrations/sources/mssql",
    "airbyte_mysql": "https://docs.airbyte.com/integrations/sources/mysql",

    # Power BI — full connector list (different page)
    "powerbi_connector_list": "https://learn.microsoft.com/en-us/power-query/connectors/",
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
    resp = requests.post(endpoint, auth=(api_key, ""), json=payload, timeout=90)
    if resp.status_code == 404:
        return None
    resp.raise_for_status()
    return resp.json().get("browserHtml", "")


def extract_page_info(html):
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "noscript", "svg"]):
        tag.decompose()

    title_tag = soup.find("title")
    title = title_tag.get_text(strip=True) if title_tag else ""
    text = soup.get_text(separator=" ", strip=True)

    # Get headings for structure
    headings = []
    for level in range(1, 4):
        for tag in soup.find_all(f"h{level}"):
            t = tag.get_text(strip=True)
            if t and len(t) < 200:
                headings.append(f"{'#' * level} {t}")

    return title, headings, text


def main():
    api_key = load_api_key()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    results = {}

    for name, url in TARGETS.items():
        print(f"\n{'='*60}")
        print(f"Scraping: {name}")
        print(f"URL: {url}")
        try:
            html = fetch_page(url, api_key)
            if html is None:
                print(f"  → 404 Not Found")
                results[name] = {"url": url, "status": "404", "exists": False}
                continue

            title, headings, text = extract_page_info(html)

            # Check if this is a real connector page or a 404/redirect
            text_lower = text.lower()
            is_real = not any(phrase in text_lower for phrase in [
                "page not found", "404", "this page doesn't exist",
                "we couldn't find", "no longer available"
            ])

            status = "exists" if is_real else "not_found_or_error"
            print(f"  → Title: {title}")
            print(f"  → Status: {status}")
            print(f"  → {len(headings)} headings")

            results[name] = {
                "url": url,
                "status": status,
                "exists": is_real,
                "title": title,
                "headings": headings[:15],
                "text_snippet": text[:2000],
            }

            # Write individual file
            lines = [
                f"# {name}",
                f"_URL: {url}_",
                f"_Scraped: {datetime.now().isoformat()[:19]}_",
                f"_Status: {status}_",
                f"_Title: {title}_",
                "",
                "## Headings",
            ]
            for h in headings[:15]:
                lines.append(f"- {h}")
            lines.append("")
            lines.append("## Content (first 3000 chars)")
            lines.append("```")
            lines.append(text[:3000])
            lines.append("```")

            out_path = OUTPUT_DIR / f"{name}.md"
            out_path.write_text("\n".join(lines))

        except Exception as e:
            print(f"  → ERROR: {e}")
            results[name] = {"url": url, "status": "error", "error": str(e)}

    # Write summary
    summary_path = OUTPUT_DIR / "_v2_summary.json"
    summary_path.write_text(json.dumps(results, indent=2))

    # Print verification table
    print("\n\n" + "=" * 80)
    print("CONNECTOR EXISTENCE VERIFICATION")
    print("=" * 80)
    print(f"\n{'Name':<30} {'Exists?':<10} {'Title/Notes'}")
    print("-" * 80)
    for name, data in results.items():
        exists = "✓ YES" if data.get("exists") else "✗ NO"
        title = data.get("title", data.get("error", data.get("status", "")))[:50]
        print(f"{name:<30} {exists:<10} {title}")


if __name__ == "__main__":
    main()
