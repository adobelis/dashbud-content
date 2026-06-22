#!/usr/bin/env python3
"""Add Richard Diamond and Aimee Bigham to contacts."""
import csv
from pathlib import Path

CONTACTS = Path("/Users/arthur/www/dashbud/content/outreach/contacts.csv")

with open(CONTACTS) as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames or [])
    rows = list(reader)

NEW = [
    {
        "first_name": "Richard",
        "last_name": "Diamond",
        "company": "Advance Local / MV Digital",
        "position": "Executive (Advance ownership family)",
        "linkedin_url": "",
        "source": "ad_manual",
        "category": "advance_local",
        "relationship": "colleagues_advance_local",
        "seniority": "c_suite",
        "dashbud_relevance": "medium",
        "notes": "Advance family, 3rd generation. Arthur worked on projects for Richard, seconded by Matt Jaeger. For later outreach.",
    },
    {
        "first_name": "Aimee",
        "last_name": "Bigham",
        "company": "MV Digital Group",
        "position": "CSO (Chief Strategy Officer)",
        "linkedin_url": "",
        "source": "ad_manual",
        "category": "advance_local|tech",
        "relationship": "colleagues_advance_local",
        "seniority": "c_suite",
        "dashbud_relevance": "high",
        "notes": "Hardcore targeted advertising expert. Arthur was her tech liaison at Advance. For later outreach.",
    },
]

for contact in NEW:
    for field in fieldnames:
        if field not in contact:
            contact[field] = ""
    rows.append(contact)

with open(CONTACTS, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

for c in NEW:
    print(f"  Added: {c['first_name']} {c['last_name']} | {c['position']} @ {c['company']}")
