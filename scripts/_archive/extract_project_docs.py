#!/usr/bin/env python3
"""Extract project docs from the Dashbud content development project into standalone files."""
import json
from pathlib import Path

BASE = Path("/Users/arthur/www/dashbud/content")
PROJECT_FILE = BASE / "raw_exports" / "projects" / "019924cb-8a6c-7202-9616-45a434e5dbda.json"
OUT = BASE / "dashbud"

with open(PROJECT_FILE) as f:
    proj = json.load(f)

docs = proj.get("docs", [])
print(f"Project: {proj.get('name')}")
print(f"Docs: {len(docs)}")

for d in docs:
    filename = d.get("filename", "untitled")
    content = d.get("content", "")
    created = d.get("created_at", "")[:10]

    # Create a safe filename
    safe = filename.replace(":", " -").replace("/", "-").strip()
    outpath = OUT / f"{safe}.md"

    with open(outpath, "w") as f:
        f.write(f"# {filename}\n")
        f.write(f"_Project doc, created {created}_\n\n")
        f.write(content)

    print(f"  -> {outpath.name} ({len(content)} chars)")

# Also extract the project description/prompt template if substantial
desc = proj.get("description", "")
prompt = proj.get("prompt_template", "")
if desc or prompt:
    outpath = OUT / "project_context.md"
    with open(outpath, "w") as f:
        f.write("# Dashbud Content Development — Project Context\n\n")
        if desc:
            f.write(f"## Description\n{desc}\n\n")
        if prompt:
            f.write(f"## Prompt Template\n{prompt}\n")
    print(f"  -> project_context.md ({len(desc) + len(prompt)} chars)")
