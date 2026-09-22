#!/usr/bin/env python3
"""
Push a local info-page markdown file to the Sanity production dataset.

Reads website/info/{slug}.md, parses it into Portable Text, backs up
the current Sanity document, then patches the body and updated fields.

Usage:
  python3 push_info_page.py terms-of-use
  python3 push_info_page.py privacy
  python3 push_info_page.py cookie-policy
  python3 push_info_page.py terms-of-use --dry-run   # show what would change
"""
import argparse
import json
import random
import re
import string
import urllib.request
from datetime import datetime
from pathlib import Path

PROJECT_ID = "89a9k63v"
DATASET = "production"
INFO_DIR = Path("/Users/arthur/www/dashbud/content/website/info")
BACKUP_DIR = Path("/Users/arthur/www/dashbud/content/website/_raw/sanity_backups")
ENV_PATH = Path("/Users/arthur/www/dashbud/content/.env")


def load_token():
    for line in ENV_PATH.read_text().splitlines():
        if line.startswith("SANITY_WRITE_TOKEN="):
            return line.split("=", 1)[1].strip()
    raise RuntimeError("SANITY_WRITE_TOKEN not found in .env")


def make_key():
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=12))


# ── Sanity API helpers ───────────────────────────────────────────────────

def sanity_get(doc_id, token):
    url = f"https://{PROJECT_ID}.api.sanity.io/v2024-01-01/data/doc/{DATASET}/{doc_id}"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def sanity_mutate(mutations, token):
    url = f"https://{PROJECT_ID}.api.sanity.io/v2024-01-01/data/mutate/{DATASET}"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    data = json.dumps({"mutations": mutations}).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


# ── Markdown → Portable Text ─────────────────────────────────────────────

def parse_inline(text):
    """Parse **bold**, *italic*, and [link](url) into PT spans."""
    spans = []
    mark_defs = []
    pos = 0

    # Combined pattern: bold, italic, or link
    pattern = re.compile(
        r'\*\*(.+?)\*\*'        # **bold**
        r'|\*(.+?)\*'           # *italic*
        r'|\[([^\]]+)\]\(([^)]+)\)'  # [text](url)
    )

    for m in pattern.finditer(text):
        # Text before this match
        if m.start() > pos:
            spans.append({
                "_type": "span", "_key": make_key(),
                "marks": [], "text": text[pos:m.start()],
            })

        if m.group(1) is not None:  # bold
            spans.append({
                "_type": "span", "_key": make_key(),
                "marks": ["strong"], "text": m.group(1),
            })
        elif m.group(2) is not None:  # italic
            spans.append({
                "_type": "span", "_key": make_key(),
                "marks": ["em"], "text": m.group(2),
            })
        elif m.group(3) is not None:  # link
            link_key = make_key()
            mark_defs.append({"_key": link_key, "_type": "link", "href": m.group(4)})
            spans.append({
                "_type": "span", "_key": make_key(),
                "marks": [link_key], "text": m.group(3),
            })
        pos = m.end()

    # Remaining text
    if pos < len(text):
        spans.append({
            "_type": "span", "_key": make_key(),
            "marks": [], "text": text[pos:],
        })

    if not spans:
        spans.append({
            "_type": "span", "_key": make_key(),
            "marks": [], "text": text,
        })

    return spans, mark_defs


def md_to_portable_text(md_body):
    """Convert markdown body (after frontmatter) to Portable Text blocks."""
    blocks = []
    lines = md_body.strip().split("\n")
    i = 0

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Skip blank lines
        if not stripped:
            i += 1
            continue

        # Headings
        heading_match = re.match(r'^(#{1,6})\s+(.+)$', stripped)
        if heading_match:
            level = len(heading_match.group(1))
            text = heading_match.group(2)
            spans, mark_defs = parse_inline(text)
            blocks.append({
                "_type": "block", "_key": make_key(),
                "style": f"h{level}",
                "markDefs": mark_defs,
                "children": spans,
            })
            i += 1
            continue

        # Bullet list items
        bullet_match = re.match(r'^[-*]\s+(.+)$', stripped)
        if bullet_match:
            text = bullet_match.group(1)
            spans, mark_defs = parse_inline(text)
            blocks.append({
                "_type": "block", "_key": make_key(),
                "style": "normal",
                "markDefs": mark_defs,
                "listItem": "bullet", "level": 1,
                "children": spans,
            })
            i += 1
            continue

        # Numbered list items
        num_match = re.match(r'^\d+\.\s+(.+)$', stripped)
        if num_match:
            text = num_match.group(1)
            spans, mark_defs = parse_inline(text)
            blocks.append({
                "_type": "block", "_key": make_key(),
                "style": "normal",
                "markDefs": mark_defs,
                "listItem": "number", "level": 1,
                "children": spans,
            })
            i += 1
            continue

        # Normal paragraph
        spans, mark_defs = parse_inline(stripped)
        blocks.append({
            "_type": "block", "_key": make_key(),
            "style": "normal",
            "markDefs": mark_defs,
            "children": spans,
        })
        i += 1

    return blocks


# ── Parse the local markdown file ────────────────────────────────────────

def parse_info_md(slug):
    """Read website/info/{slug}.md, extract Sanity ID, updated date, and body."""
    path = INFO_DIR / f"{slug}.md"
    if not path.exists():
        raise FileNotFoundError(f"No file at {path}")

    text = path.read_text()

    # Extract Sanity ID
    id_match = re.search(r'Sanity ID:\s*([a-f0-9-]+)', text)
    if not id_match:
        raise ValueError(f"No Sanity ID found in {path}")
    doc_id = id_match.group(1)

    # Extract updated date (strip trailing _ from markdown italic wrapper)
    updated_match = re.search(r'Updated:\s*(\S+)', text)
    updated = updated_match.group(1).rstrip("_") if updated_match else None

    # Body is everything after the first --- separator line
    # (The --- appears on its own line after the header metadata)
    lines = text.split("\n")
    body_start = None
    for i, line in enumerate(lines):
        if line.strip() == "---":
            body_start = i + 1
            break
    if body_start is None:
        raise ValueError(f"No --- separator found in {path}")
    body_md = "\n".join(lines[body_start:]).strip()

    return doc_id, updated, body_md


# ── Main ─────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Push an info page to Sanity production")
    parser.add_argument("slug", help="Page slug (e.g. terms-of-use, privacy, cookie-policy)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would change without pushing")
    args = parser.parse_args()

    token = load_token()
    slug = args.slug

    # Parse local markdown
    print(f"Reading website/info/{slug}.md...")
    doc_id, updated, body_md = parse_info_md(slug)
    print(f"  Sanity ID: {doc_id}")
    print(f"  Updated: {updated}")

    new_body = md_to_portable_text(body_md)
    print(f"  Parsed {len(new_body)} Portable Text blocks from markdown")

    # Fetch current doc for backup
    print(f"\nFetching current document from Sanity ({DATASET})...")
    result = sanity_get(doc_id, token)
    doc = result["documents"][0]
    old_body = doc.get("body", [])
    print(f"  Current doc has {len(old_body)} blocks")

    # Backup
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    backup_file = BACKUP_DIR / f"{slug}_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(backup_file, "w") as f:
        json.dump(doc, f, indent=2)
    print(f"  Backed up to: {backup_file.name}")

    if args.dry_run:
        print("\n[DRY RUN] Would push these blocks:")
        for i, b in enumerate(new_body):
            children_text = "".join(c.get("text", "") for c in b.get("children", []))
            style = b.get("style", "normal")
            li = b.get("listItem", "")
            label = f"[{i}] {style}"
            if li:
                label += f" ({li})"
            print(f"  {label}: {children_text[:90]}")
        print("\n[DRY RUN] No changes pushed.")
        return

    # Build mutation
    patch_set = {"body": new_body}
    if updated:
        patch_set["updated"] = updated

    mutations = [{"patch": {"id": doc_id, "set": patch_set}}]

    print(f"\nPushing {len(new_body)} blocks to {DATASET}...")
    result = sanity_mutate(mutations, token)
    print(f"  Result: {result['results'][0]['operation']}")

    # Verify
    print("\nVerifying...")
    updated_result = sanity_get(doc_id, token)
    updated_doc = updated_result["documents"][0]
    updated_body_text = " ".join(
        "".join(c.get("text", "") for c in b.get("children", []))
        for b in updated_doc.get("body", []) if b.get("_type") == "block"
    )

    # Check a few key phrases from the new content
    checks = {
        "Provider": "Provider" in updated_body_text,
        "No Evolytix": "Evolytix" not in updated_body_text,
    }
    all_ok = all(checks.values())
    for label, passed in checks.items():
        print(f"  {'✓' if passed else '✗'} {label}")

    if all_ok:
        print("\nDone. Info page updated successfully.")
    else:
        print("\nWARNING: Some verification checks failed. Review the live page.")


if __name__ == "__main__":
    main()
