#!/usr/bin/env python3
"""Extract project doc details."""
import json
from pathlib import Path

BASE = Path("/Users/arthur/www/dashbud/content")
project_dir = BASE / "projects"

for pf in sorted(project_dir.glob("*.json")):
    with open(pf) as f:
        proj = json.load(f)

    docs = proj.get("docs", [])
    if not docs:
        continue

    name = proj.get("name", pf.stem)
    print(f"\n{'='*80}")
    print(f"Project: {name} ({pf.stem[:12]}...)")
    print(f"Docs: {len(docs)}")

    for i, d in enumerate(docs):
        print(f"\n  Doc [{i}]:")
        if isinstance(d, dict):
            for k, v in d.items():
                if isinstance(v, str) and len(v) > 500:
                    print(f"    {k}: ({len(v)} chars) {v[:200]}...")
                else:
                    print(f"    {k}: {v}")
        else:
            print(f"    {str(d)[:200]}")
