#!/usr/bin/env python3
"""
Scrape competitor homepages to extract navigation links and build site maps.
Then optionally fetch each discovered page.

Phase 1: Fetch homepage, extract all internal nav/menu links
Phase 2: Fetch each discovered page with full text

Usage:
  .venv/bin/python scripts/research/scrape_competitor_sitemaps.py --discover
  .venv/bin/python scripts/research/scrape_competitor_sitemaps.py --fetch --name thoughtspot
  .venv/bin/python scripts/research/scrape_competitor_sitemaps.py --fetch --all

Requires: zyte-api beautifulsoup4
"""
import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

CONTENT_ROOT = Path("/Users/arthur/www/dashbud/content")
OUTPUT_DIR = CONTENT_ROOT / "wiki" / "dashbud" / "comparators" / "site-maps"
PAGES_DIR = CONTENT_ROOT / "wiki" / "dashbud" / "comparators" / "full-pages"
ENV_PATH = CONTENT_ROOT / ".env"

COMPETITORS = {
    "thoughtspot": "https://www.thoughtspot.com",
    "sigma": "https://www.sigmacomputing.com",
    "zenlytic": "https://www.zenlytic.com",
    "omni": "https://omni.co",
}

# Skip these path patterns — not useful for positioning research
SKIP_PATTERNS = [
    r"/blog/", r"/blog$", r"/press", r"/news", r"/careers", r"/jobs",
    r"/legal", r"/privacy", r"/terms", r"/cookie", r"/security",
    r"/login", r"/signin", r"/signup", r"/register", r"/app",
    r"/docs/", r"/documentation", r"/help/", r"/support",
    r"/api/", r"/developers", r"/changelog", r"/release-notes",
    r"/partners/", r"/partner-directory", r"/marketplace",
    r"/events", r"/webinars", r"/podcast",
    r"/community", r"/forum",
    r"\.\w+$",  # file extensions
    r"#",  # anchors
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
    endpoint = "https://api.zyte.com/v1/extract"
    payload = {"url": url, "browserHtml": True}
    resp = requests.post(endpoint, auth=(api_key, ""), json=payload, timeout=120)
    if resp.status_code == 404:
        return None
    resp.raise_for_status()
    return resp.json().get("browserHtml", "")


def should_skip(path):
    for pattern in SKIP_PATTERNS:
        if re.search(pattern, path, re.IGNORECASE):
            return True
    return False


def extract_nav_links(html, base_url):
    """Extract navigation/menu links from homepage HTML."""
    soup = BeautifulSoup(html, "html.parser")
    parsed_base = urlparse(base_url)
    base_domain = parsed_base.netloc.replace("www.", "")

    links = {}

    # Look for nav elements first, then fall back to all links
    nav_elements = soup.find_all(["nav", "header"])
    if not nav_elements:
        nav_elements = [soup]

    for nav in nav_elements:
        for a in nav.find_all("a", href=True):
            href = a["href"].strip()
            text = a.get_text(strip=True)

            if not text or len(text) > 100 or len(text) < 2:
                continue

            # Resolve relative URLs
            full_url = urljoin(base_url, href)
            parsed = urlparse(full_url)

            # Only keep same-domain links
            link_domain = parsed.netloc.replace("www.", "")
            if link_domain != base_domain:
                continue

            # Clean the URL
            clean_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
            if clean_url.endswith("/"):
                clean_url = clean_url[:-1]

            path = parsed.path
            if not path or path == "/":
                continue

            if should_skip(path):
                continue

            # Deduplicate by URL
            if clean_url not in links:
                links[clean_url] = {
                    "url": clean_url,
                    "path": path,
                    "text": text,
                    "in_nav": any(nav.name in ["nav", "header"] for nav in [nav]),
                }

    return links


def extract_full_text(html):
    """Extract clean full text from HTML."""
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "noscript", "svg", "iframe", "footer"]):
        tag.decompose()

    # Try to find main content area
    main = soup.find("main") or soup.find("article") or soup.find(role="main")
    if main:
        source = main
    else:
        source = soup.find("body") or soup

    # Extract headings separately
    headings = []
    for level in range(1, 5):
        for tag in source.find_all(f"h{level}"):
            text = tag.get_text(separator=" ", strip=True)
            if text and len(text) < 300:
                headings.append({"level": level, "text": text})

    # Extract meta
    title_tag = soup.find("title")
    title = title_tag.get_text(strip=True) if title_tag else ""

    meta_desc = ""
    meta_tag = soup.find("meta", attrs={"name": "description"})
    if meta_tag:
        meta_desc = meta_tag.get("content", "")

    full_text = source.get_text(separator="\n", strip=True)

    return {
        "title": title,
        "meta_description": meta_desc,
        "headings": headings,
        "full_text": full_text,
    }


def discover(api_key):
    """Phase 1: Discover nav links for each competitor."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for name, base_url in COMPETITORS.items():
        print(f"\n{'='*60}")
        print(f"Discovering: {name} ({base_url})")

        try:
            html = fetch_page(base_url, api_key)
            if not html:
                print("  → Failed to fetch homepage")
                continue

            links = extract_nav_links(html, base_url)

            # Also try sitemap.xml
            sitemap_url = f"{base_url}/sitemap.xml"
            print(f"  Checking sitemap: {sitemap_url}")
            try:
                sitemap_html = fetch_page(sitemap_url, api_key)
                if sitemap_html:
                    sitemap_soup = BeautifulSoup(sitemap_html, "html.parser")
                    for loc in sitemap_soup.find_all("loc"):
                        url_text = loc.get_text(strip=True)
                        parsed = urlparse(url_text)
                        if not should_skip(parsed.path) and parsed.path and parsed.path != "/":
                            clean = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
                            if clean.endswith("/"):
                                clean = clean[:-1]
                            if clean not in links:
                                links[clean] = {
                                    "url": clean,
                                    "path": parsed.path,
                                    "text": f"[sitemap] {parsed.path}",
                                    "in_nav": False,
                                }
                    print(f"  → Sitemap found, added URLs")
            except Exception as e:
                print(f"  → Sitemap: {e}")

            # Sort by path
            sorted_links = dict(sorted(links.items(), key=lambda x: x[1]["path"]))

            # Write sitemap
            out = {
                "competitor": name,
                "base_url": base_url,
                "discovered": datetime.now().isoformat()[:19],
                "page_count": len(sorted_links),
                "pages": sorted_links,
            }

            json_path = OUTPUT_DIR / f"{name}.json"
            json_path.write_text(json.dumps(out, indent=2))

            # Write readable version
            md_lines = [
                f"# {name} — Site Map",
                f"_Base: {base_url} | Discovered: {out['discovered']} | {len(sorted_links)} pages_",
                "",
            ]
            for url, info in sorted_links.items():
                nav_marker = " [NAV]" if info["in_nav"] else ""
                md_lines.append(f"- `{info['path']}`{nav_marker} — {info['text']}")

            md_path = OUTPUT_DIR / f"{name}.md"
            md_path.write_text("\n".join(md_lines))

            print(f"  → {len(sorted_links)} pages discovered")
            print(f"  → Wrote {json_path.name} and {md_path.name}")

        except Exception as e:
            print(f"  → ERROR: {e}")


def fetch_pages(api_key, name):
    """Phase 2: Fetch full content for discovered pages."""
    PAGES_DIR.mkdir(parents=True, exist_ok=True)

    json_path = OUTPUT_DIR / f"{name}.json"
    if not json_path.exists():
        print(f"No sitemap found for {name}. Run --discover first.")
        return

    sitemap = json.loads(json_path.read_text())
    pages = sitemap["pages"]

    comp_dir = PAGES_DIR / name
    comp_dir.mkdir(exist_ok=True)

    print(f"\nFetching {len(pages)} pages for {name}...")

    for url, info in pages.items():
        # Create filename from path
        path = info["path"].strip("/").replace("/", "_") or "homepage"
        out_path = comp_dir / f"{path}.md"

        if out_path.exists():
            print(f"  SKIP (exists): {info['path']}")
            continue

        print(f"  Fetching: {info['path']}")
        try:
            html = fetch_page(url, api_key)
            if not html:
                print(f"    → 404")
                out_path.write_text(f"# {url}\n\n_404 Not Found_\n")
                continue

            content = extract_full_text(html)

            lines = [
                f"# {content['title'] or info['text']}",
                f"_URL: {url}_",
                f"_Fetched: {datetime.now().isoformat()[:19]}_",
                f"_Meta: {content['meta_description']}_",
                "",
                "## Headings",
            ]
            for h in content["headings"]:
                indent = "  " * (h["level"] - 1)
                lines.append(f"{indent}- **h{h['level']}:** {h['text']}")

            lines.append("")
            lines.append("## Content")
            lines.append("")
            lines.append(content["full_text"])

            out_path.write_text("\n".join(lines))
            print(f"    → {len(content['headings'])} headings, "
                  f"{len(content['full_text'])} chars")

        except Exception as e:
            print(f"    → ERROR: {e}")
            out_path.write_text(f"# {url}\n\n_Error: {e}_\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--discover", action="store_true",
                        help="Phase 1: discover nav links and sitemaps")
    parser.add_argument("--fetch", action="store_true",
                        help="Phase 2: fetch full page content")
    parser.add_argument("--name", help="Single competitor to fetch")
    parser.add_argument("--all", action="store_true", help="All competitors")
    args = parser.parse_args()

    api_key = load_api_key()

    if args.discover:
        discover(api_key)
    elif args.fetch:
        if args.all:
            for name in COMPETITORS:
                fetch_pages(api_key, name)
        elif args.name:
            if args.name not in COMPETITORS:
                print(f"Unknown: {args.name}. Available: {', '.join(COMPETITORS)}")
                sys.exit(1)
            fetch_pages(api_key, args.name)
        else:
            print("Specify --name or --all with --fetch")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
