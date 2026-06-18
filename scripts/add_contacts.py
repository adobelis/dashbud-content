#!/usr/bin/env python3
"""Add manual contacts to the master contacts file."""
import csv
from pathlib import Path

CONTACTS = Path("/Users/arthur/www/dashbud/content/outreach/contacts.csv")

# Read existing
with open(CONTACTS) as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames or [])
    rows = list(reader)

NEW_CONTACTS = [
    {
        "first_name": "Mozam",
        "last_name": "Hosein",
        "company": "Advance Local",
        "position": "Senior Director, Architecture",
        "linkedin_url": "",
        "source": "ad_manual",
        "category": "advance_local|tech",
        "relationship": "colleagues_advance_local",
        "seniority": "director",
        "dashbud_relevance": "high",
        "notes": "Arthur reported to Mozam. Strong relationship. Senior tech leader.",
    },
    {
        "first_name": "Scott",
        "last_name": "Culver",
        "company": "Advance Local",
        "position": "Senior Director, Content / Technical Product Manager",
        "linkedin_url": "https://www.linkedin.com/in/scculver",
        "source": "ad_manual",
        "category": "advance_local|tech",
        "relationship": "colleagues_advance_local",
        "seniority": "director",
        "dashbud_relevance": "high",
        "notes": "Arthur reported to Scott. Strong relationship.",
    },
    {
        "first_name": "Matt",
        "last_name": "Jaeger",
        "company": "Advance Local",
        "position": "SVP Product & Technology",
        "linkedin_url": "https://www.linkedin.com/in/matt-jaeger-7741a2",
        "source": "ad_manual",
        "category": "advance_local|tech",
        "relationship": "colleagues_advance_local",
        "seniority": "vp_plus",
        "dashbud_relevance": "high",
        "notes": "Senior tech leader at Advance Local. Former colleague.",
    },
    {
        "first_name": "Zoltan",
        "last_name": "Gerts",
        "company": "Advance Local",
        "position": "Senior Director, Product Management",
        "linkedin_url": "https://www.linkedin.com/in/zoltangerts/",
        "source": "ad_manual",
        "category": "advance_local|tech",
        "relationship": "colleagues_advance_local",
        "seniority": "director",
        "dashbud_relevance": "high",
        "notes": "Reach out when website is updated. Ad platform / product management.",
    },
    {
        "first_name": "Kim",
        "last_name": "",
        "company": "Advance Local",
        "position": "",
        "linkedin_url": "",
        "source": "ad_manual",
        "category": "advance_local",
        "relationship": "colleagues_advance_local",
        "seniority": "",
        "dashbud_relevance": "high",
        "notes": "Reach out when website is updated.",
    },
]

# Fill in missing fields
for contact in NEW_CONTACTS:
    for field in fieldnames:
        if field not in contact:
            contact[field] = ""
    rows.append(contact)

with open(CONTACTS, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Added {len(NEW_CONTACTS)} contacts")
for c in NEW_CONTACTS:
    print(f"  {c['first_name']} {c['last_name']} | {c['position']} @ {c['company']}")
