#!/usr/bin/env python3
"""Show full project details including creation dates, descriptions, and prompt instructions."""
import json
from pathlib import Path

BASE = Path("/Users/arthur/www/dashbud/content")

# Use original projects dir (same UUIDs in all exports)
project_dir = BASE / "projects"

for pf in sorted(project_dir.glob("*.json")):
    with open(pf) as f:
        proj = json.load(f)

    print(f"\n{'='*80}")
    print(f"UUID: {pf.stem}")
    print(f"Name: {proj.get('name', '?')}")
    print(f"Created: {proj.get('created_at', '?')}")
    print(f"Updated: {proj.get('updated_at', '?')}")
    print(f"Description: {proj.get('description', '')[:200]}")

    # Check for project instructions/prompt
    instructions = proj.get("prompt_instructions") or proj.get("instructions") or proj.get("system_prompt") or ""
    if instructions:
        print(f"Instructions: {instructions[:300]}...")

    # Check for project knowledge/docs
    docs = proj.get("docs") or proj.get("knowledge") or proj.get("files") or []
    if docs:
        print(f"Attached docs: {len(docs)}")
        for d in docs[:5]:
            if isinstance(d, dict):
                print(f"  - {d.get('file_name', d.get('name', '?'))} ({d.get('file_size', '?')} bytes)")

    # Show all top-level keys
    print(f"All keys: {list(proj.keys())}")
