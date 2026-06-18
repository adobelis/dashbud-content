#!/usr/bin/env python3
"""Update Tiana Maher's record."""
import csv
from pathlib import Path

CONTACTS = Path("/Users/arthur/www/dashbud/content/outreach/contacts.csv")

with open(CONTACTS) as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames or [])
    rows = list(reader)

for row in rows:
    if row["first_name"] == "Tiana" and row["last_name"] == "Maher":
        row["relationship"] = "colleagues_advance_local"
        row["category"] = "advance_local|tech"
        row["notes"] = "May still be at Advance Local (Sr Dir, Digital Ops & Infrastructure) or K1X (VP Ops). Either way, strong Advance connection."
        row["dashbud_relevance"] = "high"
        print(f"  Updated: {row['first_name']} {row['last_name']}")

with open(CONTACTS, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
