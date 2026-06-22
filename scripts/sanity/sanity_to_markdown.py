#!/usr/bin/env python3
"""Convert all Sanity CMS content to clean, readable Markdown files.

Reads the raw JSON fetched from the Sanity API and produces:
- website/hero.md
- website/features/ (one file per feature, ordered)
- website/how-it-works-steps.md
- website/homepage.md (structure + audiences + CTA)
- website/blog/ (one file per post)
- website/info/ (privacy, terms, cookie policy)
- website/authors.md
- website/sections.md
"""
import json
from pathlib import Path

SANITY_DIR = Path("/Users/arthur/www/dashbud/content/website/sanity_current")
OUT = Path("/Users/arthur/www/dashbud/content/website")

# ── Portable Text → Markdown ──────────────────────────────────────────────

def pt_to_md(blocks):
    """Convert Sanity Portable Text block array to Markdown string."""
    if not blocks:
        return ""
    lines = []
    prev_was_list = False
    for block in blocks:
        if not isinstance(block, dict):
            continue
        btype = block.get("_type", "")

        # Image blocks
        if btype == "image":
            ref = block.get("asset", {}).get("_ref", "")
            alt = block.get("alt", "")
            lines.append(f"![{alt}]({ref})")
            prev_was_list = False
            continue

        if btype != "block":
            continue

        children = block.get("children", [])
        mark_defs = {m["_key"]: m for m in block.get("markDefs", [])}
        text = _render_children(children, mark_defs)

        style = block.get("style", "normal")
        li = block.get("listItem")
        level = block.get("level", 1)

        # Headings
        if style.startswith("h") and len(style) == 2 and style[1].isdigit():
            depth = int(style[1])
            if prev_was_list:
                lines.append("")
            lines.append(f"{'#' * depth} {text}")
            prev_was_list = False
            continue

        # Blockquote
        if style == "blockquote":
            lines.append(f"> {text}")
            prev_was_list = False
            continue

        # List items
        if li:
            indent = "  " * (level - 1)
            if li == "number":
                lines.append(f"{indent}1. {text}")
            else:
                lines.append(f"{indent}- {text}")
            prev_was_list = True
            continue

        # Normal paragraph
        if prev_was_list:
            lines.append("")
        if text.strip():
            lines.append(text)
        else:
            lines.append("")
        prev_was_list = False

    return "\n\n".join(lines)


def _render_children(children, mark_defs):
    """Render inline spans with marks (bold, italic, code, links)."""
    parts = []
    for child in children:
        if child.get("_type") != "span":
            continue
        text = child.get("text", "")
        marks = child.get("marks", [])
        for mark in marks:
            if mark in mark_defs:
                md = mark_defs[mark]
                if md.get("_type") == "link":
                    text = f"[{text}]({md.get('href', '')})"
            elif mark == "strong":
                text = f"**{text}**"
            elif mark == "em":
                text = f"*{text}*"
            elif mark == "code":
                text = f"`{text}`"
        parts.append(text)
    return "".join(parts)


# ── Load data ─────────────────────────────────────────────────────────────

with open(SANITY_DIR / "all_docs.json") as f:
    all_docs = json.load(f)["result"]

with open(SANITY_DIR / "blogposts.json") as f:
    blog_docs = json.load(f)["result"]

by_type = {}
for doc in all_docs + blog_docs:
    by_type.setdefault(doc["_type"], []).append(doc)

# Index by ID for reference resolution
by_id = {doc["_id"]: doc for doc in all_docs + blog_docs}


# ── Hero ──────────────────────────────────────────────────────────────────

hero_dir = OUT
for doc in by_type.get("hero", []):
    md = []
    md.append("# Hero Section")
    md.append(f"_Sanity ID: {doc['_id']}_\n")
    md.append(f"## Headline\n{doc.get('headline', '')}")
    md.append(f"## Subheadline\n{pt_to_md(doc.get('subheadLine', []))}")
    md.append(f"## CTAs")
    md.append(f"- **Primary:** {doc.get('primaryCtaText', '')} -> {doc.get('primaryCtaUrl', '')}")
    md.append(f"- **Secondary:** {doc.get('secondaryCtaText', '')} -> {doc.get('secondaryCtaUrl', '')}")
    if doc.get("heroImage"):
        ref = doc["heroImage"].get("asset", {}).get("_ref", "")
        md.append(f"\n## Hero Image\n`{ref}`")
    (OUT / "hero.md").write_text("\n\n".join(md))
    print("  hero.md")


# ── Features ──────────────────────────────────────────────────────────────

feat_dir = OUT / "features"
feat_dir.mkdir(exist_ok=True)

features = sorted(by_type.get("feature", []), key=lambda x: x.get("order", 999))
for doc in features:
    order = doc.get("order", 0)
    slug = doc.get("slug", {}).get("current", "feature")
    title = doc.get("title", "Untitled")

    md = []
    md.append(f"# {order}. {title}")
    md.append(f"_Slug: {slug} | Sanity ID: {doc['_id']}_\n")
    md.append(f"## Short Description\n{pt_to_md(doc.get('shortDescription', []))}")
    md.append(f"## Long Description\n{pt_to_md(doc.get('longDescription', []))}")
    if doc.get("imageAlt"):
        md.append(f"## Image\n**Alt:** {doc['imageAlt']}")
    if doc.get("image"):
        ref = doc["image"].get("asset", {}).get("_ref", "")
        md.append(f"**Asset:** `{ref}`")
    if doc.get("ctaText"):
        md.append(f"\n## CTA\n{doc['ctaText']} -> {doc.get('ctaUrl', '')}")

    fname = f"{order:02d}_{slug}.md"
    (feat_dir / fname).write_text("\n\n".join(md))
    print(f"  features/{fname}")


# ── How It Works Steps ────────────────────────────────────────────────────

# Get order from homepage references
homepage = by_type.get("homepage", [{}])[0]
step_order = [ref.get("_ref") for ref in homepage.get("howItWorksSteps", [])]

md = ["# How It Works Steps\n"]
steps = by_type.get("howItWorksStep", [])
# Sort by homepage reference order
steps_sorted = sorted(steps, key=lambda s: step_order.index(s["_id"]) if s["_id"] in step_order else 999)

for i, doc in enumerate(steps_sorted, 1):
    md.append(f"## {i}. {doc.get('title', '?')}")
    md.append(f"_Sanity ID: {doc['_id']}_\n")
    md.append(pt_to_md(doc.get("description", [])))
    if doc.get("icon"):
        ref = doc["icon"].get("asset", {}).get("_ref", "")
        md.append(f"\n**Icon:** `{ref}`")
    md.append("")

(OUT / "how-it-works-steps.md").write_text("\n\n".join(md))
print("  how-it-works-steps.md")


# ── Homepage structure ────────────────────────────────────────────────────

md = ["# Homepage Structure"]
md.append(f"_Title: {homepage.get('title', '?')}_")
md.append(f"_Sanity ID: {homepage.get('_id', '?')}_\n")

# Hero ref
hero_ref = homepage.get("hero", {}).get("_ref", "")
hero_doc = by_id.get(hero_ref, {})
md.append(f"## Hero\nRef: `{hero_ref}` ({hero_doc.get('headline', '?')})")

# Features
md.append("\n## Features (in order)")
for ref in homepage.get("features", []):
    fdoc = by_id.get(ref.get("_ref", ""), {})
    md.append(f"- {fdoc.get('order', '?')}. {fdoc.get('title', '?')} (`{ref.get('_ref', '')}`)")

# Steps
md.append("\n## How It Works Steps (in order)")
for ref in homepage.get("howItWorksSteps", []):
    sdoc = by_id.get(ref.get("_ref", ""), {})
    md.append(f"- {sdoc.get('title', '?')} (`{ref.get('_ref', '')}`)")

# Audiences
audiences = homepage.get("audiences", [])
if audiences:
    md.append(f"\n## Audiences ({len(audiences)})")
    for a in audiences:
        md.append(f"### {a.get('audienceTitle', '?')}")
        md.append(pt_to_md(a.get("message", [])))

# CTA
cta = homepage.get("ctaSection", {})
if cta:
    md.append(f"\n## CTA Section")
    md.append(f"**Headline:** {cta.get('headline', '')}")
    md.append(f"**Subhead:** {cta.get('subhead', '')}")
    md.append(f"**CTA:** {cta.get('ctaText', '')} -> {cta.get('ctaUrl', '')}")

(OUT / "homepage.md").write_text("\n\n".join(md))
print("  homepage.md")


# ── Blog posts ────────────────────────────────────────────────────────────

blog_dir = OUT / "blog"
blog_dir.mkdir(exist_ok=True)

for doc in by_type.get("blogpost", []):
    slug = doc.get("slug", {}).get("current", "untitled")
    title = doc.get("title", "Untitled")

    md = []
    md.append(f"# {title}")
    md.append(f"_Slug: {slug} | Published: {doc.get('published', '?')} | Featured: {doc.get('isFeatured', False)}_")
    md.append(f"_Sanity ID: {doc['_id']}_\n")
    if doc.get("subTitle"):
        md.append(f"**Subtitle:** {doc['subTitle']}\n")
    if doc.get("snippet"):
        md.append(f"**Snippet:** {doc['snippet']}\n")
    if doc.get("topics"):
        md.append(f"**Topics:** {', '.join(doc['topics'])}\n")
    if doc.get("leadImage"):
        alt = doc["leadImage"].get("alt", "")
        ref = doc["leadImage"].get("asset", {}).get("_ref", "")
        md.append(f"**Lead image:** {alt} (`{ref}`)\n")

    # Author
    author_ref = doc.get("author", {}).get("_ref", "")
    author_doc = by_id.get(author_ref, {})
    if author_doc:
        md.append(f"**Author:** {author_doc.get('name', '?')}\n")

    md.append("---\n")
    md.append(pt_to_md(doc.get("body", [])))

    (blog_dir / f"{slug}.md").write_text("\n\n".join(md))
    print(f"  blog/{slug}.md")


# ── Info pages ────────────────────────────────────────────────────────────

info_dir = OUT / "info"
info_dir.mkdir(exist_ok=True)

for doc in by_type.get("infopage", []):
    slug = doc.get("slug", {}).get("current", "untitled")
    title = doc.get("title", "Untitled")

    md = []
    md.append(f"# {title}")
    md.append(f"_Slug: {slug} | Updated: {doc.get('updated', '?')}_")
    md.append(f"_Sanity ID: {doc['_id']}_\n")
    md.append("---\n")
    md.append(pt_to_md(doc.get("body", [])))

    (info_dir / f"{slug}.md").write_text("\n\n".join(md))
    print(f"  info/{slug}.md")


# ── Authors & Sections ────────────────────────────────────────────────────

md = ["# Authors\n"]
for doc in by_type.get("author", []):
    md.append(f"## {doc.get('name', '?')}")
    md.append(f"_Sanity ID: {doc['_id']}_")
    md.append(f"{doc.get('description', '')}")
md_text = "\n\n".join(md)

md2 = ["\n\n# Blog Sections\n"]
for doc in by_type.get("section", []):
    slug = doc.get("slug", {}).get("current", "")
    md2.append(f"## {doc.get('name', '?')}")
    md2.append(f"_Slug: {slug} | Sanity ID: {doc['_id']}_")
    md2.append(f"{doc.get('description', '')}")

(OUT / "authors_and_sections.md").write_text(md_text + "\n\n".join(md2))
print("  authors_and_sections.md")

print(f"\nDone. All Sanity content converted to Markdown in {OUT}/")
