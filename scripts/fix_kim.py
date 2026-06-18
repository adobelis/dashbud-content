#!/usr/bin/env python3
"""Remove the duplicate Kim entry and update Kimberly Howard's notes."""
import csv
from pathlib import Path

CONTACTS = Path("/Users/arthur/www/dashbud/content/outreach/contacts.csv")

with open(CONTACTS) as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames or [])
    rows = list(reader)

# Remove the blank Kim entry we just added
rows = [r for r in rows if not (r["first_name"] == "Kim" and r["last_name"] == "" and r["source"] == "ad_manual")]

# Update Kimberly Howard
for row in rows:
    if row["first_name"] == "Kimberly" and row["last_name"] == "Howard":
        row["relationship"] = "colleagues_advance_local"
        row["notes"] = "Reach out when website is updated. Director of Ad and Data Platforms."
        row["dashbud_relevance"] = "high"
        print(f"  Updated: {row['first_name']} {row['last_name']}")

with open(CONTACTS, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("Done")
