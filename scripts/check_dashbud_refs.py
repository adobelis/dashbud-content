#!/usr/bin/env python3
"""Check all conversations for Dashbud/marketing references."""
import json
from pathlib import Path

BASE = Path("/Users/arthur/www/dashbud/content")

all_convos = []

# Original export
with open(BASE / "conversations.json") as f:
    for c in json.load(f):
        c["_source"] = "original"
        all_convos.append(c)

# Oct-Feb export
with open(BASE / "export_oct_feb" / "conversations.json") as f:
    for c in json.load(f):
        c["_source"] = "oct-feb"
        all_convos.append(c)

def get_text(msg):
    text = msg.get("text") or msg.get("content") or ""
    if isinstance(text, list):
        return " ".join(b.get("text", "") for b in text if isinstance(b, dict))
    return text

keywords = ["dashbud", "marketing", "content series", "blog post", "linkedin",
            "website", "landing page", "use case", "positioning", "branding",
            "ad strategy", "seo", "conversion", "prospect", "customer profile",
            "target audience", "go-to-market", "GTM"]

for c in all_convos:
    name = c.get("name") or "(untitled)"
    created = c.get("created_at", "?")[:10]
    msgs = c.get("chat_messages", [])
    source = c["_source"]

    # Gather all text
    full_text = " ".join(get_text(m) for m in msgs).lower()

    if not full_text.strip():
        continue

    hits = [kw for kw in keywords if kw.lower() in full_text]
    if hits:
        # Count occurrences of "dashbud"
        dashbud_count = full_text.count("dashbud")
        print(f"\n[{source}] {created} | {len(msgs)} msgs | {name}")
        print(f"  Keywords: {', '.join(hits)}")
        print(f"  'dashbud' mentions: {dashbud_count}")
