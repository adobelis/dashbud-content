#!/usr/bin/env python3
"""Rename files with underscores to hyphens for Starlight slug compatibility."""
from pathlib import Path

DOCS = Path("/Users/arthur/www/dashbud/content/wiki/src/content/docs")

for f in DOCS.rglob("*.md"):
    if "_" in f.name:
        new_name = f.name.replace("_", "-")
        new_path = f.parent / new_name
        f.rename(new_path)
        print(f"  {f.name} -> {new_name}")

print("\nFinal slugs:")
for f in sorted(DOCS.rglob("*.md")):
    slug = str(f.relative_to(DOCS)).replace(".md", "").replace("/", "/")
    print(f"  {slug}")
