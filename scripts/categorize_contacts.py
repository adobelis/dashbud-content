#!/usr/bin/env python3
"""Auto-categorize contacts based on company, position, and connection date."""
import csv
from pathlib import Path

CONTACTS = Path("/Users/arthur/www/dashbud/content/outreach/contacts.csv")

# ── Category rules ──

LAW_FIRMS = [
    "cahill", "gordon", "reindel", "sullivan & cromwell", "cravath", "davis polk",
    "skadden", "wachtell", "cleary", "simpson thacher", "paul weiss", "debevoise",
    "milbank", "white & case", "willkie", "proskauer", "kirkland", "latham",
    "dla piper", "norton rose", "morrison foerster", "goodwin", "cooley",
    "fenwick", "wilson sonsini", "orrick", "pillsbury", "shearman",
    "akin gump", "arnold & porter", "baker mckenzie", "baker botts",
    "buhler duggal", "herrick", "paul hastings", "sidley", "jones day",
    "morgan lewis", "hogan lovells", "reed smith", "greenberg traurig",
    "dentons", "k&l gates", "seyfarth", "gibson dunn", "weil gotshal",
    "fried frank", "ropes & gray", "mayer brown", "dechert", "schulte roth",
    "cadwalader", "kramer levin", "katten", "cozen", "fox rothschild",
    "thompson hine", "foley", "steptoe", "vedder", "mintz",
    "law office", "law firm", "legal", "attorney", "esq",
    "u.s. attorney", "district attorney", "public defender",
    "securities and exchange commission", "sec ", "doj", "department of justice",
]

LEGAL_POSITIONS = [
    "attorney", "lawyer", "counsel", "partner", "associate", "paralegal",
    "legal", "of counsel", "juris", "j.d.", "esq",
]

ADVANCE_LOCAL_VARIANTS = [
    "advance local", "advance digital", "advance.com", "condé nast",
    "newhouse", "staten island advance", "nj.com", "al.com",
    "cleveland.com", "oregonlive", "masslive", "pennlive", "syracuse.com",
]

TECH_COMPANIES = [
    "google", "amazon", "meta", "facebook", "apple", "microsoft",
    "ibm", "oracle", "salesforce", "adobe", "netflix", "spotify",
    "uber", "lyft", "airbnb", "stripe", "square", "shopify",
    "slack", "dropbox", "twitter", "snap", "pinterest",
    "palantir", "datadog", "snowflake", "databricks", "mongodb",
    "twilio", "cloudflare", "vercel", "github", "gitlab",
    "hubspot", "zendesk", "intercom", "segment", "amplitude",
    "figma", "notion", "linear", "airtable", "asana",
    "new york times", "nytimes", "buzzfeed", "vice media", "vox media",
    "bloomberg", "reuters", "conde nast",
]

STARTUP_MEDIA_KEYWORDS = [
    "startup", "stealth", "founder", "co-founder", "ceo", "cto", "coo",
    "venture", "angel", "incubator", "accelerator", "ycombinator", "y combinator",
    "techstars", "seed", "series a",
    "freelance", "self-employed", "self employed", "consultant", "independent",
    "media", "content", "editorial", "journalist", "producer", "creative",
]

FINANCE_KEYWORDS = [
    "jpmorgan", "goldman", "morgan stanley", "citigroup", "bank of america",
    "barclays", "credit suisse", "ubs", "deutsche bank", "hsbc",
    "blackrock", "blackstone", "kkr", "carlyle", "apollo",
    "bridgewater", "citadel", "two sigma", "de shaw", "point72",
    "pwc", "deloitte", "ey ", "ernst & young", "kpmg", "mckinsey",
    "bain", "bcg", "boston consulting",
    "s&p global", "moody", "fitch",
]


def categorize(row):
    company = (row["company"] or "").lower()
    position = (row["position"] or "").lower()
    connected = row["connected_on"] or ""
    year = int(connected[:4]) if connected and connected[:4].isdigit() else 0

    categories = []

    # Advance Local
    if any(term in company for term in ADVANCE_LOCAL_VARIANTS):
        categories.append("advance_local")

    # Law firms and legal roles
    is_legal = False
    if any(term in company for term in LAW_FIRMS):
        is_legal = True
    if any(term in position for term in LEGAL_POSITIONS):
        is_legal = True
    if is_legal:
        categories.append("lawyer")

    # Tech companies
    if any(term in company for term in TECH_COMPANIES):
        categories.append("tech")

    # Finance
    if any(term in company for term in FINANCE_KEYWORDS):
        categories.append("finance")

    # Startup/media era (2011-2014 connections with relevant signals)
    is_startup_media = False
    if any(term in company.lower() + " " + position.lower() for term in STARTUP_MEDIA_KEYWORDS):
        is_startup_media = True
    if is_startup_media:
        if 2011 <= year <= 2014:
            categories.append("startup_media_era")
        else:
            categories.append("startup_entrepreneur")

    # If nothing matched
    if not categories:
        categories.append("uncategorized")

    return "|".join(categories)


def classify_seniority(position):
    """Rough seniority classification from title."""
    pos = (position or "").lower()

    # C-suite
    if any(t in pos for t in ["chief", "ceo", "cto", "cfo", "coo", "cmo", "cro", "cio", "cpo"]):
        return "c_suite"

    # Founders
    if any(t in pos for t in ["founder", "co-founder", "cofounder", "owner"]):
        return "founder"

    # VP+
    if any(t in pos for t in ["vice president", "vp ", "vp,", "svp", "evp", "president"]):
        return "vp_plus"

    # Director
    if "director" in pos:
        return "director"

    # Head of
    if "head of" in pos or "head," in pos:
        return "director"

    # Partner (law/consulting/vc)
    if "partner" in pos:
        return "partner"

    # Manager / Lead
    if any(t in pos for t in ["manager", "lead", "supervisor", "team lead"]):
        return "manager"

    # Senior individual contributor
    if any(t in pos for t in ["senior", "sr.", "sr ", "principal", "staff"]):
        return "senior_ic"

    # Associate / analyst / entry
    if any(t in pos for t in ["associate", "analyst", "coordinator", "specialist", "assistant"]):
        return "junior"

    # Student / intern
    if any(t in pos for t in ["student", "intern", "fellow", "candidate"]):
        return "student"

    return "unknown"


def assess_dashbud_relevance(row, category, seniority):
    """Rough assessment of potential Dashbud relevance."""
    company = (row["company"] or "").lower()
    position = (row["position"] or "").lower()

    # Directly relevant roles (data, analytics, ops, finance at companies)
    relevant_roles = ["data", "analytics", "operations", "finance", "revenue",
                      "business intelligence", "reporting", "insights", "strategy"]

    has_relevant_role = any(term in position for term in relevant_roles)

    # Connector potential (VCs, founders, tech leaders)
    is_connector = seniority in ("c_suite", "founder", "vp_plus", "partner")

    # At a potentially relevant company (mid-market, not BigLaw/BigTech)
    is_big_firm = any(term in company for term in LAW_FIRMS + ["google", "amazon", "meta", "facebook", "apple", "microsoft"])

    if has_relevant_role and is_connector:
        return "high"
    elif has_relevant_role or (is_connector and "startup" in category):
        return "medium"
    elif is_connector and not is_big_firm:
        return "medium"
    else:
        return ""


# ── Process ──

rows = []
with open(CONTACTS) as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row in reader:
        category = categorize(row)
        seniority = classify_seniority(row["position"])
        relevance = assess_dashbud_relevance(row, category, seniority)

        row["category"] = category
        row["dashbud_relevance"] = relevance
        # Add seniority as a new field
        row["seniority"] = seniority
        rows.append(row)

# Update fieldnames to include seniority
fieldnames = list(fieldnames) + ["seniority"] if "seniority" not in fieldnames else fieldnames

with open(CONTACTS, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

# ── Stats ──
print(f"Processed {len(rows)} contacts\n")

# Category breakdown
cat_counts = {}
for r in rows:
    for c in r["category"].split("|"):
        cat_counts[c] = cat_counts.get(c, 0) + 1
print("Categories:")
for cat, count in sorted(cat_counts.items(), key=lambda x: -x[1]):
    print(f"  {count:4d}  {cat}")

# Seniority breakdown
sen_counts = {}
for r in rows:
    s = r["seniority"]
    sen_counts[s] = sen_counts.get(s, 0) + 1
print("\nSeniority:")
for sen, count in sorted(sen_counts.items(), key=lambda x: -x[1]):
    print(f"  {count:4d}  {sen}")

# Relevance breakdown
rel_counts = {}
for r in rows:
    rv = r["dashbud_relevance"] or "unscored"
    rel_counts[rv] = rel_counts.get(rv, 0) + 1
print("\nDashbud relevance:")
for rel, count in sorted(rel_counts.items(), key=lambda x: -x[1]):
    print(f"  {count:4d}  {rel}")

# Show high-relevance contacts
print("\n=== HIGH RELEVANCE CONTACTS ===")
high = [r for r in rows if r["dashbud_relevance"] == "high"]
for r in high:
    print(f"  {r['first_name']} {r['last_name']} | {r['position']} @ {r['company']} | {r['category']} | {r['seniority']}")

print(f"\n=== MEDIUM RELEVANCE (first 30) ===")
medium = [r for r in rows if r["dashbud_relevance"] == "medium"]
for r in medium[:30]:
    print(f"  {r['first_name']} {r['last_name']} | {r['position']} @ {r['company']} | {r['category']} | {r['seniority']}")
print(f"  ... and {len(medium) - 30} more" if len(medium) > 30 else "")
