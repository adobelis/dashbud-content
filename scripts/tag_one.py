#!/usr/bin/env python3
"""Tag a single contact by partial name match. Usage: python3 tag_one.py <first> <last> <tag>"""
import csv, sys
from pathlib import Path

CONTACTS = Path("/Users/arthur/www/dashbud/content/outreach/contacts.csv")
first_q, last_q, tag = sys.argv[1].lower(), sys.argv[2].lower(), sys.argv[3]

with open(CONTACTS) as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames or [])
    rows = list(reader)

tagged = 0
for row in rows:
    first = row["first_name"].lower()
    last = row["last_name"].lower()
    if first_q in first and last.startswith(last_q):
        existing = row.get("relationship", "")
        if tag not in existing:
            row["relationship"] = (existing + "|" + tag).strip("|") if existing else tag
            tagged += 1
            print(f"  Tagged: {row['first_name']} {row['last_name']} ({row['company']})")

with open(CONTACTS, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Tagged {tagged}")
