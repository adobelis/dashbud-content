#!/usr/bin/env python3
"""
Push local content (hero + features) to a Sanity dataset.

Usage:
  python3 push_content.py                  # push to staging (default)
  python3 push_content.py --dataset production  # push to production
  python3 push_content.py --hero-only      # push only hero
  python3 push_content.py --features-only  # push only features
"""
import argparse
import json
import random
import string
import urllib.request
from pathlib import Path

import yaml

PROJECT_ID = "89a9k63v"
CONTENT_DIR = Path("/Users/arthur/www/dashbud/content/website")
ENV_PATH = Path("/Users/arthur/www/dashbud/content/.env")


def load_token():
    for line in ENV_PATH.read_text().splitlines():
        if line.startswith("SANITY_WRITE_TOKEN="):
            return line.split("=", 1)[1].strip()
    raise RuntimeError("SANITY_WRITE_TOKEN not found in .env")


def make_key():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))


def text_to_pt(text):
    """Convert a plain text string (with markdown bold) to Portable Text blocks."""
    blocks = []
    for para in text.strip().split("\n\n"):
        para = para.strip()
        if not para:
            continue

        # Check for bullet list
        lines = para.split("\n")
        if all(line.strip().startswith("- ") or line.strip().startswith("* ") for line in lines if line.strip()):
            for line in lines:
                line = line.strip().lstrip("- ").lstrip("* ").strip()
                blocks.append({
                    "_type": "block", "_key": make_key(), "style": "normal",
                    "markDefs": [], "listItem": "bullet", "level": 1,
                    "children": parse_inline(line),
                })
            continue

        blocks.append({
            "_type": "block", "_key": make_key(), "style": "normal",
            "markDefs": [],
            "children": parse_inline(para.replace("\n", " ")),
        })

    return blocks


def parse_inline(text):
    """Parse **bold** markers into Portable Text spans."""
    children = []
    parts = text.split("**")
    for i, part in enumerate(parts):
        if not part:
            continue
        if i % 2 == 1:
            # Bold
            children.append({
                "_type": "span", "_key": make_key(),
                "marks": ["strong"], "text": part,
            })
        else:
            children.append({
                "_type": "span", "_key": make_key(),
                "marks": [], "text": part,
            })
    if not children:
        children.append({
            "_type": "span", "_key": make_key(),
            "marks": [], "text": text,
        })
    return children


def sanity_mutate(mutations, dataset, token):
    url = f"https://{PROJECT_ID}.api.sanity.io/v2024-01-01/data/mutate/{dataset}"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    data = json.dumps({"mutations": mutations}).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def push_hero(dataset, token):
    config = yaml.safe_load((CONTENT_DIR / "hero.yaml").read_text())

    mutations = [{
        "patch": {
            "id": config["sanity_id"],
            "set": {
                "headline": config["headline"],
                "subheadLine": text_to_pt(config["subheadline"]),
                "primaryCtaText": config["primary_cta"]["text"],
                "primaryCtaUrl": config["primary_cta"]["url"],
                "secondaryCtaText": config["secondary_cta"]["text"],
                "secondaryCtaUrl": config["secondary_cta"]["url"],
            }
        }
    }]

    print(f"Pushing hero to {dataset}...")
    print(f"  Headline: {config['headline'][:60]}...")
    result = sanity_mutate(mutations, dataset, token)
    print(f"  OK: {result['results'][0]['operation']}")


def push_features(dataset, token):
    config = yaml.safe_load((CONTENT_DIR / "features.yaml").read_text())

    mutations = []
    for feature in config["features"]:
        mutations.append({
            "patch": {
                "id": feature["sanity_id"],
                "set": {
                    "title": feature["title"],
                    "slug": {"_type": "slug", "current": feature["slug"]},
                    "order": feature["order"],
                    "shortDescription": text_to_pt(feature["short"]),
                    "longDescription": text_to_pt(feature["long"]),
                    "imageAlt": feature["image_alt"],
                }
            }
        })

    print(f"Pushing {len(mutations)} features to {dataset}...")
    result = sanity_mutate(mutations, dataset, token)
    for i, r in enumerate(result["results"]):
        print(f"  {config['features'][i]['order']}. {config['features'][i]['title']}: {r['operation']}")


def main():
    parser = argparse.ArgumentParser(description="Push website content to Sanity")
    parser.add_argument("--dataset", default="staging", help="Target dataset (default: staging)")
    parser.add_argument("--hero-only", action="store_true")
    parser.add_argument("--features-only", action="store_true")
    args = parser.parse_args()

    token = load_token()
    do_hero = not args.features_only
    do_features = not args.hero_only

    if do_hero:
        push_hero(args.dataset, token)
    if do_features:
        push_features(args.dataset, token)

    print(f"\nDone. Content pushed to '{args.dataset}'.")


if __name__ == "__main__":
    main()
