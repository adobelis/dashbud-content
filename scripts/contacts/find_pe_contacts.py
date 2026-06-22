#!/usr/bin/env python3
"""Find contacts with private equity connections."""
import csv
from pathlib import Path

CONTACTS = Path("/Users/arthur/www/dashbud/content/outreach/contacts.csv")

PE_KEYWORDS = [
    "private equity", "pe ", "buyout", "portfolio",
    "blackstone", "kkr", "carlyle", "apollo", "warburg", "bain capital",
    "advent", "thoma bravo", "vista equity", "silver lake", "hellman",
    "cerberus", "ares", "permira", "cinven", "eqt", "ardian",
    "general atlantic", "insight partners", "summit partners",
    "welsh carson", "golden gate", "leonard green", "roark",
    "fund", "lbo", "leveraged",
]

# Also look for VC/investment that could overlap
INVESTMENT_KEYWORDS = [
    "venture", "capital", "investment", "investor", "managing director",
    "principal", "partner",  # at investment firms
]

with open(CONTACTS) as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print("=== DIRECT PE MATCHES ===\n")
pe_matches = []
for row in rows:
    company = (row["company"] or "").lower()
    position = (row["position"] or "").lower()
    combined = company + " " + position

    if any(kw in combined for kw in PE_KEYWORDS):
        pe_matches.append(row)
        rel = row.get("relationship", "") or "-"
        print(f"  {row['first_name']} {row['last_name']}")
        print(f"    {row['position']} @ {row['company']}")
        print(f"    Connected: {row['connected_on']} | Relationship: {rel}")
        print()

print(f"Total direct PE matches: {len(pe_matches)}\n")

print("=== INVESTMENT / VC / FUND MANAGEMENT ===\n")
inv_matches = []
for row in rows:
    if row in pe_matches:
        continue
    company = (row["company"] or "").lower()
    position = (row["position"] or "").lower()
    combined = company + " " + position

    # Must match at least one investment keyword AND have a senior title
    has_inv = any(kw in combined for kw in INVESTMENT_KEYWORDS)
    seniority = row.get("seniority", "")
    is_senior = seniority in ("c_suite", "founder", "vp_plus", "partner", "director")

    if has_inv and is_senior:
        inv_matches.append(row)
        rel = row.get("relationship", "") or "-"
        print(f"  {row['first_name']} {row['last_name']}")
        print(f"    {row['position']} @ {row['company']}")
        print(f"    Connected: {row['connected_on']} | Relationship: {rel}")
        print()

print(f"Total investment/VC matches: {len(inv_matches)}")
