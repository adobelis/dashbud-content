#!/usr/bin/env python3
"""
Fetch current content from Sanity and save locally as a snapshot.

Usage:
  python3 scripts/sanity/fetch_current_content.py                  # fetch from production
  python3 scripts/sanity/fetch_current_content.py --dataset staging
"""
import argparse
import json
import urllib.request
from datetime import datetime
from pathlib import Path

PROJECT_ID = "89a9k63v"
OUTPUT_DIR = Path("/Users/arthur/www/dashbud/content/website/_archive/sanity-snapshots")

DOCUMENT_IDS = {
    "hero": "b8feb522-f902-4fa6-bbc1-92724e3df508",
    "homepage": "f691ab1a-c9ff-40d0-bc80-0cd3a92c53ea",
    "feature-01-connect": "f511cdf6-cfb1-4906-a82d-e404844d808e",
    "feature-02-model": "353166e1-2171-4557-a9f1-2c5186e8e312",
    "feature-03-explore": "aada85c2-bedf-4f07-9e7c-55d004241700",
    "feature-04-share": "3e0abf06-4e77-4fdc-aae7-58db5b439c26",
}


def fetch_document(doc_id, dataset):
    query = f'*[_id == "{doc_id}"][0]'
    encoded = urllib.parse.quote(query)
    url = f"https://{PROJECT_ID}.api.sanity.io/v2023-01-01/data/query/{dataset}?query={encoded}"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())["result"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", default="production")
    args = parser.parse_args()

    timestamp = datetime.now().strftime("%Y-%m-%d")
    out_dir = OUTPUT_DIR / f"{args.dataset}_{timestamp}"
    out_dir.mkdir(parents=True, exist_ok=True)

    for name, doc_id in DOCUMENT_IDS.items():
        print(f"Fetching {name} from {args.dataset}...")
        try:
            doc = fetch_document(doc_id, args.dataset)
            out_path = out_dir / f"{name}.json"
            out_path.write_text(json.dumps(doc, indent=2))
            print(f"  Saved to {out_path.name}")
        except Exception as e:
            print(f"  ERROR: {e}")

    print(f"\nSnapshot saved to {out_dir}")


if __name__ == "__main__":
    main()
