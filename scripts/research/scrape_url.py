#!/usr/bin/env python3
"""
Save a web page as local markdown in scrapes/, so feed entries and research
never need to re-fetch it. Uses the Zyte API and BeautifulSoup.

Filename convention: <published>-<domain>-<slug>.md, where <published> is the
content's own date (from page metadata, or given explicitly). The access date
is recorded in frontmatter as `fetched:`. If no published date can be found,
the fetch date is used in the name and `published:` is left blank.

Usage (from the content repo root, venv activated):
  python scripts/research/scrape_url.py URL [--slug SLUG] [--published YYYY-MM-DD] [--browser]
  python scripts/research/scrape_url.py --batch FILE   # lines: URL [slug] [published]; # comments allowed

Output:
  scrapes/<published>-<domain>-<slug>.md     extracted text with frontmatter
  scrapes/_html/<same stem>.html             raw HTML, kept for re-extraction

Default fetch is the plain HTTP body; --browser renders JavaScript (slower, costs more).
If a plain fetch yields under 500 characters of text, the script retries with the browser.
Key: ZYTE_API_KEY, loaded by repo_env.
"""
import argparse
import base64
import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup, NavigableString, Tag

sys.path.insert(0, str(Path(__file__).resolve().parent))
from repo_env import REPO_ROOT, require_key  # noqa: E402

API_KEY = require_key("ZYTE_API_KEY")
OUT = REPO_ROOT / "scrapes"
HTML_OUT = OUT / "_html"
ENDPOINT = "https://api.zyte.com/v1/extract"
MIN_TEXT = 500
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}")

SKIP = {"script", "style", "nav", "footer", "header", "aside", "form", "noscript", "svg", "button", "iframe"}


def fetch(url: str, browser: bool) -> str:
    payload = {"url": url, ("browserHtml" if browser else "httpResponseBody"): True}
    r = requests.post(ENDPOINT, auth=(API_KEY, ""), json=payload, timeout=90)
    r.raise_for_status()
    d = r.json()
    if browser:
        return d.get("browserHtml", "")
    return base64.b64decode(d.get("httpResponseBody", "")).decode("utf-8", errors="replace")


def meta(soup, **attrs) -> str:
    t = soup.find("meta", attrs=attrs)
    return (t.get("content") or "").strip() if t else ""


def find_published(soup) -> str:
    """Best-effort publication date, ISO yyyy-mm-dd or ''. Checked in order of reliability."""
    candidates = [
        meta(soup, property="article:published_time"),
        meta(soup, name="article:published_time"),
        meta(soup, itemprop="datePublished"),
        meta(soup, name="date"),
        meta(soup, name="pubdate"),
        meta(soup, name="publish_date"),
        meta(soup, name="dc.date"),
        meta(soup, name="citation_publication_date"),
        meta(soup, name="parsely-pub-date"),
    ]
    for s in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(s.string or "")
        except Exception:
            continue
        items = data if isinstance(data, list) else [data]
        for item in items:
            if isinstance(item, dict):
                for key in ("datePublished", "dateCreated", "uploadDate"):
                    if item.get(key):
                        candidates.append(str(item[key]))
                graph = item.get("@graph") or []
                for g in graph:
                    if isinstance(g, dict) and g.get("datePublished"):
                        candidates.append(str(g["datePublished"]))
    t = soup.find("time", attrs={"datetime": True})
    if t:
        candidates.append(t["datetime"])
    for c in candidates:
        if c and DATE_RE.match(c.strip()):
            return c.strip()[:10]
    return ""


def slugify(s: str, n: int = 60) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s[:n].rstrip("-") or "page"


def to_md(node, depth: int = 0) -> str:
    """Minimal HTML to markdown: headings, paragraphs, lists, quotes, emphasis. Links kept as text."""
    out = []
    for child in node.children:
        if isinstance(child, NavigableString):
            txt = re.sub(r"\s+", " ", str(child))
            if txt.strip():
                out.append(txt)
            continue
        if not isinstance(child, Tag) or child.name in SKIP:
            continue
        name = child.name
        if name in ("h1", "h2", "h3", "h4", "h5", "h6"):
            out.append(f"\n\n{'#' * int(name[1])} {child.get_text(' ', strip=True)}\n\n")
        elif name == "p":
            out.append(f"\n\n{to_md(child).strip()}\n\n")
        elif name in ("ul", "ol"):
            items = []
            for i, li in enumerate(child.find_all("li", recursive=False), 1):
                bullet = f"{i}." if name == "ol" else "-"
                items.append(f"{'  ' * depth}{bullet} {to_md(li, depth + 1).strip()}")
            out.append("\n\n" + "\n".join(items) + "\n\n")
        elif name == "blockquote":
            out.append("\n\n> " + to_md(child).strip().replace("\n", "\n> ") + "\n\n")
        elif name == "pre":
            out.append(f"\n\n```\n{child.get_text()}\n```\n\n")
        elif name == "br":
            out.append("\n")
        elif name in ("strong", "b"):
            out.append(f"**{to_md(child).strip()}**")
        elif name in ("em", "i"):
            out.append(f"*{to_md(child).strip()}*")
        elif name == "table":
            out.append("\n\n" + child.get_text("\n", strip=True) + "\n\n")
        else:
            out.append(to_md(child, depth))
    return "".join(out)


def extract(html: str):
    soup = BeautifulSoup(html, "html.parser")
    published = find_published(soup)  # before stripping scripts (JSON-LD lives there)
    for t in soup.find_all(list(SKIP)):
        t.decompose()
    title = meta(soup, property="og:title") or (soup.title.get_text(strip=True) if soup.title else "")
    author = meta(soup, name="author") or meta(soup, property="article:author") or meta(soup, name="twitter:creator")
    desc = meta(soup, property="og:description") or meta(soup, name="description")
    main = soup.find("article") or soup.find("main") or soup.body or soup
    md = to_md(main)
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    return title, author, published, desc, md


def save(url: str, slug: str | None, published_override: str | None, browser: bool) -> Path:
    fetched = date.today().isoformat()
    html = fetch(url, browser)
    title, author, published, desc, md = extract(html)
    method = "browser" if browser else "http"
    if len(md) < MIN_TEXT and not browser:
        html = fetch(url, True)
        title, author, published, desc, md = extract(html)
        method = "http,browser"
    if published_override:
        published = published_override
    name_date = published or fetched
    domain = slugify(urlparse(url).netloc.replace("www.", "").split(".")[0], 20)
    slug = slug or slugify(title)
    if slug.startswith(domain + "-"):
        slug = slug[len(domain) + 1:]
    stem = f"{name_date}-{domain}-{slug}"
    OUT.mkdir(parents=True, exist_ok=True)
    HTML_OUT.mkdir(parents=True, exist_ok=True)
    (HTML_OUT / f"{stem}.html").write_text(html)
    fm = [
        "---",
        f'title: "{title.replace(chr(34), chr(39))}"',
        f"url: {url}",
        f"author: {author}",
        f"published: {published}",
        f"fetched: {fetched}",
        f"method: {method}",
        f"chars: {len(md)}",
        "---",
        "",
    ]
    if desc:
        fm.append(f"_{desc}_\n")
    path = OUT / f"{stem}.md"
    path.write_text("\n".join(fm) + md + "\n")
    flag = "" if published else "  (no published date found; named by fetch date)"
    print(f"{len(md):>7}  {method:<13} {path.relative_to(REPO_ROOT)}{flag}")
    return path


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("url", nargs="?")
    ap.add_argument("--slug")
    ap.add_argument("--published", help="YYYY-MM-DD; overrides what the page reports")
    ap.add_argument("--browser", action="store_true")
    ap.add_argument("--batch", help="file with one 'URL [slug] [published]' per line")
    a = ap.parse_args()

    jobs: list[tuple[str, str | None, str | None]] = []
    if a.batch:
        for line in Path(a.batch).read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            jobs.append((parts[0], parts[1] if len(parts) > 1 else None, parts[2] if len(parts) > 2 else None))
    elif a.url:
        jobs.append((a.url, a.slug, a.published))
    else:
        ap.error("URL or --batch required")

    failures = 0
    for url, slug, pub in jobs:
        try:
            save(url, slug, pub, a.browser)
        except Exception as e:
            failures += 1
            print(f"  FAIL  {url}  ({e})")
    if failures:
        sys.exit(1)


if __name__ == "__main__":
    main()
