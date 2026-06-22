#!/usr/bin/env python3
"""
Push the updated privacy policy to Sanity.
1. Reads the current document as a backup
2. Builds the updated Portable Text body with the Google Sheets section
3. PATCHes just the body field
"""
import json
import os
import subprocess
from pathlib import Path
from datetime import datetime

PROJECT_ID = "89a9k63v"
DATASET = "production"
DOC_ID = "3c4bf370-559c-453a-b429-de0e5248bd50"
BACKUP_DIR = Path("/Users/arthur/www/dashbud/content/website/_raw/sanity_backups")

# Load token from .env
env_path = Path("/Users/arthur/www/dashbud/content/.env")
token = None
if env_path.exists():
    for line in env_path.read_text().splitlines():
        if line.startswith("SANITY_WRITE_TOKEN="):
            token = line.split("=", 1)[1].strip()
            break

if not token:
    print("ERROR: SANITY_WRITE_TOKEN not found in .env")
    exit(1)

API_BASE = f"https://{PROJECT_ID}.api.sanity.io/v2024-01-01"
HEADERS_READ = {"Authorization": f"Bearer {token}"}
HEADERS_WRITE = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}


def sanity_get(doc_id):
    """Fetch a document by ID."""
    import urllib.request
    url = f"{API_BASE}/data/doc/{DATASET}/{doc_id}"
    req = urllib.request.Request(url, headers=HEADERS_READ)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def sanity_mutate(mutations):
    """Send mutations to Sanity."""
    import urllib.request
    url = f"{API_BASE}/data/mutate/{DATASET}"
    data = json.dumps({"mutations": mutations}).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=HEADERS_WRITE, method="POST")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


# ── Step 1: Backup current document ──
print("Step 1: Fetching current privacy policy from Sanity...")
result = sanity_get(DOC_ID)
doc = result["documents"][0]
print(f"  Found: {doc.get('title', '?')} (rev: {doc.get('_rev', '?')})")

BACKUP_DIR.mkdir(parents=True, exist_ok=True)
backup_file = BACKUP_DIR / f"privacy_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
with open(backup_file, "w") as f:
    json.dump(doc, f, indent=2)
print(f"  Backed up to: {backup_file}")

# ── Step 2: Find insertion point ──
# We want to insert after Section 6 (Third-Party Services) and before Section 7 (Data Retention)
body = doc["body"]

# Find the block that contains "7. Data Retention"
insert_index = None
for i, block in enumerate(body):
    if block.get("_type") == "block":
        children_text = "".join(c.get("text", "") for c in block.get("children", []))
        if "7. Data Retention" in children_text or "Data Retention" in children_text:
            if block.get("style", "").startswith("h"):
                insert_index = i
                break

if insert_index is None:
    print("ERROR: Could not find Section 7 (Data Retention) to insert before")
    exit(1)

print(f"  Will insert new section before block {insert_index} (Section 7)")

# ── Step 3: Build the new Portable Text blocks ──
import random
import string

def make_key():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))

def text_block(text, style="normal", marks=None):
    """Create a simple text block."""
    children = [{"_type": "span", "_key": make_key(), "marks": marks or [], "text": text}]
    return {"_type": "block", "_key": make_key(), "style": style, "markDefs": [], "children": children}

def bold_text_block(bold_part, rest, style="normal"):
    """Create a block with a bold prefix."""
    children = [
        {"_type": "span", "_key": make_key(), "marks": ["strong"], "text": bold_part},
        {"_type": "span", "_key": make_key(), "marks": [], "text": rest},
    ]
    return {"_type": "block", "_key": make_key(), "style": style, "markDefs": [], "children": children}

def bullet_block(text, level=1):
    """Create a bullet list item."""
    return {
        "_type": "block", "_key": make_key(), "style": "normal",
        "markDefs": [], "listItem": "bullet", "level": level,
        "children": [{"_type": "span", "_key": make_key(), "marks": [], "text": text}]
    }

def link_block(pre_text, link_text, href, post_text=""):
    """Create a block with a link."""
    link_key = make_key()
    children = [
        {"_type": "span", "_key": make_key(), "marks": [], "text": pre_text},
        {"_type": "span", "_key": make_key(), "marks": [link_key], "text": link_text},
    ]
    if post_text:
        children.append({"_type": "span", "_key": make_key(), "marks": [], "text": post_text})
    return {
        "_type": "block", "_key": make_key(), "style": "normal",
        "markDefs": [{"_key": link_key, "_type": "link", "href": href}],
        "children": children
    }

new_blocks = [
    text_block("6a. Third-Party Integrations", style="h2"),
    text_block("Google Sheets & Google Drive", style="h3"),
    text_block("Dashbud allows you to connect your Google account to import spreadsheet data as a data source. When you connect, Dashbud requests read-only access to your Google Sheets and Google Drive through Google's OAuth 2.0 authorization flow."),
    bold_text_block("What we access:", ""),
    bullet_block("A list of your Google Sheets spreadsheet names, owners, and modification dates (to display the spreadsheet picker)"),
    bullet_block("The contents of spreadsheets you explicitly select for import"),
    bold_text_block("What we store:", ""),
    bullet_block("An encrypted OAuth refresh token, used to re-access your selected spreadsheets for data updates. This token is encrypted at rest and never exposed to other users or third parties."),
    bullet_block("A copy of the spreadsheet data you import, materialized into your Dashbud workspace for querying"),
    bold_text_block("What we do not do:", ""),
    bullet_block("We do not access spreadsheets you have not selected"),
    bullet_block("We do not modify, write to, or delete any Google Sheets or Drive files"),
    bullet_block("We do not share your Google data with third parties"),
    bullet_block("We do not use your Google data for advertising or profiling"),
    bold_text_block("Revoking access:", ""),
    link_block(
        "You can disconnect your Google account at any time by removing the data source from your Dashbud workspace. You can also revoke Dashbud's access directly from your ",
        "Google Account Permissions",
        "https://myaccount.google.com/permissions",
        "."
    ),
]

# ── Step 4: Insert and push ──
new_body = body[:insert_index] + new_blocks + body[insert_index:]

mutations = [{
    "patch": {
        "id": DOC_ID,
        "set": {
            "body": new_body
        }
    }
}]

print(f"\nStep 4: Pushing update ({len(new_blocks)} new blocks, {len(new_body)} total blocks)...")
result = sanity_mutate(mutations)
print(f"  Result: {json.dumps(result, indent=2)}")

# ── Step 5: Verify ──
print("\nStep 5: Verifying...")
updated = sanity_get(DOC_ID)
updated_doc = updated["documents"][0]
updated_body_text = " ".join(
    "".join(c.get("text", "") for c in b.get("children", []))
    for b in updated_doc.get("body", []) if b.get("_type") == "block"
)
if "Google Sheets" in updated_body_text and "Third-Party Integrations" in updated_body_text:
    print("  ✓ Verified: Google Sheets section is live.")
else:
    print("  ✗ WARNING: Could not verify the new section in the live document.")
