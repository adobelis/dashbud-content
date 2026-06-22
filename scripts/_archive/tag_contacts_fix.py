#!/usr/bin/env python3
"""Fix: tag Natasha Encarnacion as friends_seminary."""
import csv
from pathlib import Path

CONTACTS = Path("/Users/arthur/www/dashbud/content/outreach/contacts.csv")

with open(CONTACTS) as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

for row in rows:
    if "natasha" in row["first_name"].lower() and "encarnacion" in row["last_name"].lower():
        row["relationship"] = "friends_seminary"
        print(f"  Tagged: {row['first_name']} {row['last_name']}")

with open(CONTACTS, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
