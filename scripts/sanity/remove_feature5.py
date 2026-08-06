#!/usr/bin/env python3
"""
Remove the old "Connect Anything, Use Anywhere" feature (5th) from production Sanity.
Step 1: Patch homepage to remove the reference.
Step 2: Delete the feature document.

Usage:
  python3 scripts/sanity/remove_feature5.py --dry-run
  python3 scripts/sanity/remove_feature5.py
"""
import argparse
import json
import urllib.request
from pathlib import Path

PROJECT_ID = "89a9k63v"
DATASET = "production"
ENV_PATH = Path("/Users/arthur/www/dashbud/content/.env")

HOMEPAGE_ID = "f691ab1a-c9ff-40d0-bc80-0cd3a92c53ea"
FEATURE5_ID = "11e6db09-82cb-4188-a008-4d43ea907672"

# The 4 features to keep (in order)
KEEP_FEATURES = [
    "f511cdf6-cfb1-4906-a82d-e404844d808e",  # Connect Any Data Source
    "353166e1-2171-4557-a9f1-2c5186e8e312",  # Model Your Data Through Conversation
    "aada85c2-bedf-4f07-9e7c-55d004241700",  # Ask Questions, Get Real Answers
    "3e0abf06-4e77-4fdc-aae7-58db5b439c26",  # The Right Tools for Every Role
]


def load_token():
    for line in ENV_PATH.read_text().splitlines():
        if line.startswith("SANITY_WRITE_TOKEN="):
            return line.split("=", 1)[1].strip()
    raise RuntimeError("SANITY_WRITE_TOKEN not found in .env")


def mutate(mutations, token, dry_run=False):
    if dry_run:
        print("DRY RUN — would send:")
        print(json.dumps({"mutations": mutations}, indent=2))
        return

    url = f"https://{PROJECT_ID}.api.sanity.io/v2023-01-01/data/mutate/{DATASET}"
    payload = json.dumps({"mutations": mutations}).encode()
    req = urllib.request.Request(url, data=payload, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read().decode())
        print(json.dumps(result, indent=2))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    token = load_token()

    # Step 1: Patch homepage — replace features array with only the 4 we want
    features_array = [{"_type": "reference", "_ref": fid, "_key": fid[:8]} for fid in KEEP_FEATURES]

    print("Step 1: Patching homepage to remove feature 5 reference...")
    mutate([{
        "patch": {
            "id": HOMEPAGE_ID,
            "set": {
                "features": features_array
            }
        }
    }], token, dry_run=args.dry_run)

    # Step 2: Delete the feature 5 document
    print("\nStep 2: Deleting feature 5 document...")
    mutate([{
        "delete": {
            "id": FEATURE5_ID
        }
    }], token, dry_run=args.dry_run)

    print("\nDone." if not args.dry_run else "\nDry run complete.")


if __name__ == "__main__":
    main()
