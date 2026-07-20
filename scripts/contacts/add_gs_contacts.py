#!/usr/bin/env python3
"""Add GS 10KSB presentation contacts."""
import csv
from pathlib import Path

CONTACTS = Path("/Users/arthur/www/dashbud/content/outreach/contacts.csv")

with open(CONTACTS) as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames or [])
    rows = list(reader)

NEW = [
    {
        "first_name": "Eric",
        "last_name": "",
        "company": "",
        "position": "",
        "linkedin_url": "",
        "source": "ad_manual",
        "category": "prospect",
        "relationship": "gs_10ksb_ambassadors",
        "seniority": "",
        "dashbud_relevance": "high",
        "notes": "GS 10KSB ambassadors presentation 7/16/26. Asked about ERP/API connectivity in chat. Follow up via Sonja for contact info.",
    },
    {
        "first_name": "Rakesh",
        "last_name": "Pargohart",
        "company": "LaGuardia Community College",
        "position": "",
        "linkedin_url": "",
        "source": "ad_manual",
        "category": "prospect",
        "relationship": "gs_10ksb_ambassadors",
        "seniority": "",
        "dashbud_relevance": "high",
        "notes": "GS 10KSB ambassadors presentation 7/16/26. Has 5000 files/90K pages of data. Asked about data accuracy, forensic analysis, and data portability. Possibly legal/compliance use case.",
    },
    {
        "first_name": "Rachel",
        "last_name": "",
        "company": "Interactive (AV integration)",
        "position": "",
        "linkedin_url": "",
        "source": "ad_manual",
        "category": "prospect",
        "relationship": "gs_10ksb_ambassadors",
        "seniority": "",
        "dashbud_relevance": "high",
        "notes": "GS 10KSB ambassadors presentation 7/16/26. Woman-owned AV/systems integration firm. Already uses Claude for daily service ticket analysis. Sophisticated AI user. Was in Scott's cohort. Great prospect for comparison/conversion. Wants to meet with Scott and Arthur.",
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
    print(f"  Added: {c['first_name']} {c['last_name']} | {c['notes'][:60]}...")
