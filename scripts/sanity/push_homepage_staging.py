#!/usr/bin/env python3
"""
Push updated homepage content to Sanity STAGING dataset.
Updates: hero (headline, subhead, CTAs), features (4 pillars), howItWorks steps, CTA section.
"""
import json
import random
import string
import urllib.request
from pathlib import Path

PROJECT_ID = "89a9k63v"
DATASET = "staging"

# Load token
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


def make_key():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))


def sanity_mutate(mutations):
    url = f"{API_BASE}/data/mutate/{DATASET}"
    data = json.dumps({"mutations": mutations}).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=HEADERS, method="POST")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def text_block(text, style="normal"):
    return {
        "_type": "block", "_key": make_key(), "style": style, "markDefs": [],
        "children": [{"_type": "span", "_key": make_key(), "marks": [], "text": text}]
    }


def bold_span(text):
    return {"_type": "span", "_key": make_key(), "marks": ["strong"], "text": text}


def plain_span(text):
    return {"_type": "span", "_key": make_key(), "marks": [], "text": text}


def mixed_block(spans, style="normal"):
    return {
        "_type": "block", "_key": make_key(), "style": style, "markDefs": [],
        "children": spans
    }


def bullet_block(text, level=1):
    return {
        "_type": "block", "_key": make_key(), "style": "normal",
        "markDefs": [], "listItem": "bullet", "level": level,
        "children": [{"_type": "span", "_key": make_key(), "marks": [], "text": text}]
    }


# ── Document IDs (from production) ──
HERO_ID = "b8feb522-f902-4fa6-bbc1-92724e3df508"
FEATURE_IDS = {
    1: "f511cdf6-cfb1-4906-a82d-e404844d808e",  # was: Plain Language Queries
    2: "353166e1-2171-4557-a9f1-2c5186e8e312",  # was: Smart Report Recommendations
    3: "aada85c2-bedf-4f07-9e7c-55d004241700",  # was: Clean Professional Outputs
    4: "3e0abf06-4e77-4fdc-aae7-58db5b439c26",  # was: Organized Workspaces
    5: "11e6db09-82cb-4188-a008-4d43ea907672",  # was: Connect Anything — will repurpose
}

mutations = []

# ── HERO ──
print("Updating hero...")
mutations.append({
    "patch": {
        "id": HERO_ID,
        "set": {
            "headline": "AI-powered analytics *that scales*",
            "subheadLine": [
                text_block("From a single spreadsheet to your company's entire data ecosystem, give everyone access to trusted, modern data tools.")
            ],
            "primaryCtaText": "Try Dashbud free",
            "primaryCtaUrl": "/signup",
            "secondaryCtaText": "Book a demo",
            "secondaryCtaUrl": "https://calendly.com/arthur-evolytix/dashbud-demo-and-setup",
        }
    }
})

# ── FEATURE 1: Connect Any Data Source ──
print("Updating feature 1: Connect Any Data Source...")
mutations.append({
    "patch": {
        "id": FEATURE_IDS[1],
        "set": {
            "title": "Connect Any Data Source",
            "slug": {"_type": "slug", "current": "connect-any-data-source"},
            "order": 1,
            "shortDescription": [
                text_block("Upload spreadsheets, connect directly to databases, or sync from cloud sources like Google Sheets. No data warehouse required.")
            ],
            "longDescription": [
                text_block("Dashbud's smart data loading handles the messy parts automatically — type casting, date parsing, currency formatting — so your data is clean and queryable from the start. Every import is versioned and can be rolled back."),
                text_block("No data lake. No ETL pipeline. No migration project. Just connect what you have and start working."),
                mixed_block([bold_span("Works with: "), plain_span("CSV uploads, PostgreSQL, MySQL, IBM Informix, Google Sheets, and more.")]),
            ],
            "imageAlt": "Data source connection interface showing upload and database options",
        }
    }
})

# ── FEATURE 2: Model Your Data Through Conversation ──
print("Updating feature 2: Model Your Data Through Conversation...")
mutations.append({
    "patch": {
        "id": FEATURE_IDS[2],
        "set": {
            "title": "Model Your Data Through Conversation",
            "slug": {"_type": "slug", "current": "model-your-data"},
            "order": 2,
            "shortDescription": [
                text_block("Set up a Semantic Model by telling Dashbud about your data in plain language. No code, no configuration files, no query language.")
            ],
            "longDescription": [
                text_block("Tell Dashbud what your columns mean, how your tables relate, and what the business rules are. The AI asks questions, you answer them. Your semantic model becomes the foundation for every query — grounding the AI in your business context."),
                text_block("Model once, then clone and customize for different teams or projects. Your sales team gets their view. Finance gets theirs. Each workspace carries only the context it needs — no clutter, no confusion."),
            ],
            "imageAlt": "Semantic model conversation showing data context being defined through natural language",
        }
    }
})

# ── FEATURE 3: Explore and Analyze ──
print("Updating feature 3: Explore and Analyze...")
mutations.append({
    "patch": {
        "id": FEATURE_IDS[3],
        "set": {
            "title": "Ask Questions, Get Real Answers",
            "slug": {"_type": "slug", "current": "explore-and-analyze"},
            "order": 3,
            "shortDescription": [
                text_block("Type a question in plain English and get back tables, charts, and insights — grounded in your semantic model, accurate every time.")
            ],
            "longDescription": [
                text_block("Dashbud's Data Explorer writes the query, then produces a traditional, deterministic report — stable, accurate, and repeatable. Smart chart formatting automatically picks the right visualization, handles time series, and keeps legends readable."),
                text_block("Need interactive controls? Just ask Dashbud to parametrize any dimension — region, product line, date range — and your report becomes a live tool your team can use without touching a query."),
            ],
            "imageAlt": "Data Explorer showing a natural language question producing a professional chart",
        }
    }
})

# ── FEATURE 4: Share With Everyone ──
print("Updating feature 4: Share With Everyone...")
mutations.append({
    "patch": {
        "id": FEATURE_IDS[4],
        "set": {
            "title": "Share With Your Whole Team",
            "slug": {"_type": "slug", "current": "share-with-your-team"},
            "order": 4,
            "shortDescription": [
                text_block("Save outputs to dashboards, control who sees what, and share live-updating reports with stakeholders who never need to touch a query.")
            ],
            "longDescription": [
                text_block("Drag and drop saved reports into dashboards. Share with stakeholders who may never use the conversational interface — they just see polished, live-updating results. Control access at every level: who sees which data sources, which workspaces, which dashboards."),
                text_block("Some users build. Some users explore. Some users just read the dashboard every Monday morning. Dashbud works for all of them."),
            ],
            "imageAlt": "A shared dashboard with charts, KPIs, and interactive controls",
        }
    }
})

# ── Remove feature 5 from homepage (we want 4 pillars, not 5) ──
# We do this by updating the homepage document's features array
print("Updating homepage feature references (4 pillars)...")
HOMEPAGE_ID = "f691ab1a-c9ff-40d0-bc80-0cd3a92c53ea"
mutations.append({
    "patch": {
        "id": HOMEPAGE_ID,
        "set": {
            "features": [
                {"_key": make_key(), "_ref": FEATURE_IDS[1], "_type": "reference"},
                {"_key": make_key(), "_ref": FEATURE_IDS[2], "_type": "reference"},
                {"_key": make_key(), "_ref": FEATURE_IDS[3], "_type": "reference"},
                {"_key": make_key(), "_ref": FEATURE_IDS[4], "_type": "reference"},
            ]
        }
    }
})

# ── Push all mutations ──
print(f"\nPushing {len(mutations)} mutations to STAGING...")
result = sanity_mutate(mutations)
print(f"Result: {json.dumps(result, indent=2)}")
print("\nDone! Check the staging site.")
