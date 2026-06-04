#!/usr/bin/env python3
"""Parse the Sanity API responses (fetched via curl) and save as organized local JSON + readable markdown."""
import json
from pathlib import Path

BASE = Path("/Users/arthur/www/dashbud/content/website_content/sanity_current")

# Read the curl-fetched JSON files
with open(BASE / "all_docs.json") as f:
    data = json.load(f)
docs = data["result"]

# Also load blog posts
with open(BASE / "blogposts.json") as f:
    blog_data = json.load(f)
docs.extend(blog_data["result"])

# Group by type
by_type = {}
for doc in docs:
    t = doc["_type"]
    by_type.setdefault(t, []).append(doc)

print(f"Total documents: {len(docs)}")
for t, items in sorted(by_type.items()):
    print(f"  {t}: {len(items)}")

# Save raw JSON per type
for t, items in by_type.items():
    with open(BASE / f"{t}.json", "w") as f:
        json.dump(items, f, indent=2)


# Helper to extract plain text from Portable Text blocks
def pt_to_text(blocks):
    if not blocks:
        return ""
    lines = []
    for block in blocks:
        if block.get("_type") != "block":
            continue
        children = block.get("children", [])
        text = "".join(c.get("text", "") for c in children)
        style = block.get("style", "normal")
        li = block.get("listItem")
        if style.startswith("h"):
            level = int(style[1]) if len(style) > 1 else 2
            text = "#" * level + " " + text
        if li == "number":
            text = "1. " + text
        elif li == "bullet":
            text = "- " + text
        lines.append(text)
    return "\n\n".join(lines)


# Create readable summary
with open(BASE / "SUMMARY.md", "w") as f:
    f.write("# Sanity CMS Current Content\n\n")
    f.write("Pulled from project 89a9k63v, dataset production\n\n")

    # Hero
    f.write("## Hero\n\n")
    for doc in by_type.get("hero", []):
        f.write(f"**Headline:** {doc.get('headline', '?')}\n\n")
        f.write(f"**Subheadline:** {pt_to_text(doc.get('subheadLine', []))}\n\n")
        f.write(f"**Primary CTA:** {doc.get('primaryCtaText', '?')} -> {doc.get('primaryCtaUrl', '?')}\n\n")
        f.write(f"**Secondary CTA:** {doc.get('secondaryCtaText', '?')} -> {doc.get('secondaryCtaUrl', '?')}\n\n")

    # Features
    f.write("## Features\n\n")
    features = sorted(by_type.get("feature", []), key=lambda x: x.get("order", 999))
    for doc in features:
        f.write(f"### {doc.get('order', '?')}. {doc.get('title', '?')}\n\n")
        f.write(f"**Short:** {pt_to_text(doc.get('shortDescription', []))}\n\n")
        f.write(f"**Long:** {pt_to_text(doc.get('longDescription', []))}\n\n")
        f.write(f"**Image alt:** {doc.get('imageAlt', '')}\n\n")
        f.write(f"**ID:** {doc.get('_id', '')}\n\n")
        f.write("---\n\n")

    # How It Works Steps
    f.write("## How It Works Steps\n\n")
    for doc in by_type.get("howItWorksStep", []):
        f.write(f"### {doc.get('title', '?')}\n\n")
        f.write(f"{pt_to_text(doc.get('description', []))}\n\n")
        f.write(f"**ID:** {doc.get('_id', '')}\n\n")

    # Homepage structure
    f.write("## Homepage Structure\n\n")
    for doc in by_type.get("homepage", []):
        f.write(f"**Title:** {doc.get('title', '?')}\n\n")
        f.write(f"**Hero ref:** {doc.get('hero', {}).get('_ref', '?')}\n\n")
        steps = doc.get("howItWorksSteps", [])
        f.write(f"**How It Works Steps:** {len(steps)} refs\n\n")
        feats = doc.get("features", [])
        f.write(f"**Features:** {len(feats)} refs\n\n")
        audiences = doc.get("audiences", [])
        f.write(f"**Audiences:** {len(audiences)}\n\n")
        for a in audiences:
            f.write(f"  - {a.get('audienceTitle', '?')}: {pt_to_text(a.get('message', []))[:200]}...\n\n")
        cta = doc.get("ctaSection", {})
        if cta:
            f.write(f"**CTA Section:** {cta.get('headline', '?')} / {cta.get('subhead', '?')}\n\n")

    # Info pages
    if "infopage" in by_type:
        f.write("## Info Pages\n\n")
        for doc in by_type["infopage"]:
            f.write(f"### {doc.get('title', '?')}\n\n")
            f.write(f"**Slug:** {doc.get('slug', {}).get('current', '?')}\n\n")
            body_text = pt_to_text(doc.get("body", []))
            f.write(f"{body_text[:500]}...\n\n")

    # Blog posts
    f.write("## Blog Posts\n\n")
    for doc in by_type.get("blogpost", []):
        f.write(f"### {doc.get('title', '?')}\n\n")
        f.write(f"**Slug:** {doc.get('slug', {}).get('current', '?')}\n\n")
        f.write(f"**Published:** {doc.get('published', '?')}\n\n")
        f.write(f"**Subtitle:** {doc.get('subTitle', '')}\n\n")
        f.write(f"**Snippet:** {doc.get('snippet', '')}\n\n")
        f.write(f"**Topics:** {doc.get('topics', [])}\n\n")
        f.write(f"**Featured:** {doc.get('isFeatured', False)}\n\n")
        body_text = pt_to_text(doc.get("body", []))
        f.write(f"**Body:**\n\n{body_text}\n\n")
        f.write("---\n\n")

    # Authors
    f.write("## Authors\n\n")
    for doc in by_type.get("author", []):
        f.write(f"- {doc.get('name', '?')}: {doc.get('description', '')}\n")

    # Sections
    f.write("\n## Sections (blog categories)\n\n")
    for doc in by_type.get("section", []):
        f.write(f"- {doc.get('name', '?')}: {doc.get('description', '')}\n")

print(f"\nSaved to {BASE}")
print(f"  - Individual JSON files per type")
print(f"  - SUMMARY.md with readable content")
