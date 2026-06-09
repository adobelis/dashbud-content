#!/usr/bin/env python3
"""Prepare markdown files for Starlight by copying to src/content/docs/
with proper frontmatter and slugified filenames."""
import re
from pathlib import Path

WIKI = Path("/Users/arthur/www/dashbud/content/wiki")
DOCS = WIKI / "src" / "content" / "docs"


def slugify(name):
    """Convert a filename to a URL-friendly slug."""
    name = name.replace(".md", "")
    # Remove leading numbers like "01_"
    name = re.sub(r"^\d+_", "", name)
    # Replace spaces and special chars with hyphens
    name = re.sub(r"[^\w-]", "-", name)
    # Collapse multiple hyphens
    name = re.sub(r"-+", "-", name)
    # Lowercase and strip
    return name.lower().strip("-")


def extract_title(content):
    """Pull the first H1 from markdown content, or return None."""
    for line in content.split("\n"):
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return None


def add_frontmatter(content, title):
    """Add Starlight frontmatter. If there's already frontmatter, replace it."""
    if content.startswith("---"):
        # Already has frontmatter — replace
        end = content.index("---", 3)
        content = content[end + 3:].lstrip("\n")

    return f"---\ntitle: \"{title}\"\n---\n\n{content}"


def process_file(src, dest_dir, custom_title=None):
    """Process a single markdown file into Starlight format."""
    content = src.read_text()
    title = custom_title or extract_title(content) or src.stem.replace("-", " ").replace("_", " ").title()

    # Remove the H1 if it matches the title (Starlight renders title from frontmatter)
    lines = content.split("\n")
    new_lines = []
    removed_h1 = False
    for line in lines:
        if not removed_h1 and line.strip().startswith("# ") and line.strip()[2:].strip() == title:
            removed_h1 = True
            continue
        new_lines.append(line)
    content = "\n".join(new_lines)

    content = add_frontmatter(content, title)
    slug = slugify(src.name)
    dest = dest_dir / f"{slug}.md"
    dest.write_text(content)
    print(f"  {src.name} -> {dest.relative_to(DOCS)}")


# ── Dashbud docs ──────────────────────────────────────────────────────

print("=== dashbud/ ===")
DASHBUD_SRC = WIKI / "dashbud"
DASHBUD_DEST = DOCS / "dashbud"

file_titles = {
    "product_reality_june2026.md": "Product Reality — June 2026",
    "offer_framework.md": "Offer Framework",
    "elevator_pitches.md": "Elevator Pitches",
    "messaging_workstreams.md": "Messaging Workstreams",
    "research_bi_competitors.md": "BI Competitor Research",
    "research_b2b_saas_messaging.md": "B2B SaaS Messaging Research",
    "INVENTORY.md": "Deliverables Inventory",
    "project_context.md": "Project Context",
    "Dashbud - Product and Company Overview.md": "Product & Company Overview",
    "Blueprint Conversation UX design.md": "Blueprint / Semantic Model UX Design",
    "First Blog Post - The Lost Promise of BI.md": "The Lost Promise of Business Intelligence",
    "Dashbud website - How It Works page.md": "How It Works Page (2025)",
}

for src in sorted(DASHBUD_SRC.glob("*.md")):
    title = file_titles.get(src.name)
    process_file(src, DASHBUD_DEST, custom_title=title)


# ── Website docs ──────────────────────────────────────────────────────

print("\n=== website/ ===")
WEBSITE_SRC = WIKI / "website"
WEBSITE_DEST = DOCS / "website"

# Top-level website files
for src in sorted(WEBSITE_SRC.glob("*.md")):
    process_file(src, WEBSITE_DEST)

# Features
print("\n=== website/features/ ===")
for src in sorted((WEBSITE_SRC / "features").glob("*.md")):
    process_file(src, WEBSITE_DEST / "features")

# Blog
print("\n=== website/blog/ ===")
for src in sorted((WEBSITE_SRC / "blog").glob("*.md")):
    process_file(src, WEBSITE_DEST / "blog")

# Info
print("\n=== website/info/ ===")
for src in sorted((WEBSITE_SRC / "info").glob("*.md")):
    process_file(src, WEBSITE_DEST / "info")

print("\nDone.")
