#!/usr/bin/env python3
"""Push updated hero headline to Sanity STAGING dataset."""
import json
import urllib.request
from pathlib import Path

PROJECT_ID = "89a9k63v"
DATASET = "staging"
DOC_ID = "b8feb522-f902-4fa6-bbc1-92724e3df508"

env_path = Path("/Users/arthur/www/dashbud/content/.env")
token = None
for line in env_path.read_text().splitlines():
    if line.startswith("SANITY_WRITE_TOKEN="):
        token = line.split("=", 1)[1].strip()
        break

if not token:
    print("ERROR: SANITY_WRITE_TOKEN not found")
    exit(1)

API_BASE = f"https://{PROJECT_ID}.api.sanity.io/v2024-01-01"
HEADERS = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

def sanity_mutate(mutations):
    url = f"{API_BASE}/data/mutate/{DATASET}"
    data = json.dumps({"mutations": mutations}).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=HEADERS, method="POST")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())

new_headline = "AI-powered analytics for <br> *all your data*"

mutations = [{
    "patch": {
        "id": DOC_ID,
        "set": {
            "headline": new_headline
        }
    }
}]

print(f"Pushing to STAGING: headline = '{new_headline}'")
result = sanity_mutate(mutations)
print(f"Result: {json.dumps(result, indent=2)}")
