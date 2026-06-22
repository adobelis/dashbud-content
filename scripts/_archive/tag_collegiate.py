#!/usr/bin/env python3
"""Tag Collegiate School (high school) friends."""
import csv
from pathlib import Path

CONTACTS = Path("/Users/arthur/www/dashbud/content/outreach/contacts.csv")

COLLEGIATE = [
    ("jonathan", "wachtel"),
    ("maura", "madden"),
    ("seth", "lissak"),
    ("bart", "sayer"),
    ("olivier", "manuel"),
    ("michael", "donohue"),
    ("armando", "ramirez"),
    ("peter", "evans"),
    ("enrique", "luna"),  # Enrique-Sebastian Luna Holder
    ("haresh", "yalamanchili"),
    ("alex", "mann"),
    ("zachary", "taylor"),
    ("thor", "denmark"),
    ("cris", "cicala"),
    ("jeff", "pressman"),
    ("ben", "procter"),
    ("daisy", "de plume"),  # also seminary
    ("leah", "frances"),
    ("alex", "lehmann"),
    ("jamie", "houghtlin"),
    ("peter", "sayer"),
    ("joshua", "resnick"),
]

with open(CONTACTS) as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames or [])
    rows = list(reader)

tagged = 0
for row in rows:
    first = row["first_name"].lower().split()[0] if row["first_name"] else ""
    last = row["last_name"].lower() if row["last_name"] else ""

    for pf, pl in COLLEGIATE:
        if first == pf and last.startswith(pl):
            existing = row.get("relationship", "")
            if "friends_collegiate" not in existing:
                row["relationship"] = (existing + "|friends_collegiate").strip("|") if existing else "friends_collegiate"
                tagged += 1
                print(f"  {row['first_name']} {row['last_name']} | {row['position']} @ {row['company']}")
            break

with open(CONTACTS, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"\nTagged {tagged} as friends_collegiate")
