#!/usr/bin/env python3
"""Explore the Claude export data structure and summarize conversations."""
import json
import os
from pathlib import Path
from collections import Counter

BASE = Path("/Users/arthur/www/dashbud/content")

# --- Conversations ---
with open(BASE / "conversations.json") as f:
    convos = json.load(f)

print(f"=== CONVERSATIONS ===")
print(f"Total conversations: {len(convos)}")
if isinstance(convos, list):
    print(f"Keys in first item: {list(convos[0].keys()) if convos else 'empty'}")
elif isinstance(convos, dict):
    print(f"Top-level keys: {list(convos.keys())[:20]}")

# Try to extract names/titles and dates
print("\n--- Conversation summaries ---")
for i, c in enumerate(convos if isinstance(convos, list) else [convos]):
    name = c.get("name") or c.get("title") or c.get("subject") or "(untitled)"
    created = c.get("created_at") or c.get("created") or c.get("date") or "?"
    updated = c.get("updated_at") or c.get("updated") or ""
    num_msgs = len(c.get("chat_messages", c.get("messages", [])))
    project = c.get("project_uuid") or c.get("project_id") or c.get("project") or ""
    print(f"  [{i}] {created[:10] if len(str(created))>=10 else created} | msgs={num_msgs:>4} | project={project[:12] if project else '-':>12} | {name}")

# --- Projects ---
print(f"\n=== PROJECTS ===")
project_dir = BASE / "projects"
for pf in sorted(project_dir.glob("*.json")):
    with open(pf) as f:
        proj = json.load(f)
    name = proj.get("name") or proj.get("title") or pf.stem
    desc = proj.get("description") or ""
    created = proj.get("created_at") or ""
    print(f"  {pf.stem[:12]}... | {created[:10] if len(str(created))>=10 else created} | {name} — {desc[:80]}")

# --- Users ---
print(f"\n=== USERS ===")
with open(BASE / "users.json") as f:
    users = json.load(f)
if isinstance(users, list):
    for u in users:
        print(f"  {u.get('email') or u.get('name') or u.get('id', '?')}")
elif isinstance(users, dict):
    print(f"  Keys: {list(users.keys())[:10]}")
