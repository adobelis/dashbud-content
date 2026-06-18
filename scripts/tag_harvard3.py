#!/usr/bin/env python3
"""Tag Harvard batch 3."""
import csv
from pathlib import Path

CONTACTS = Path("/Users/arthur/www/dashbud/content/outreach/contacts.csv")

# Excluding: Heidi Curran (deceased), Theresa Esquerra (deceased), Raffi Freeman (friend of friend)
# Priya Aiyar, Maria Gambale, Vanessa Liu already tagged in prior batches

HARVARD_3 = [
    ("vanessa", "ryan"),
    ("valerie", "goldburt"),
    ("rafi", "loiederman"),
    ("matt", "donahue"),
    ("seth", "gassman"),
    ("renee", "soto"),
    ("mark", "yokoyama"),
    ("umbereen", "nehal"),
    ("lucy", "bisognano"),  # loose connection
    ("scarlet", "marquette"),
    ("frank", "pasquale"),
    ("lawrence", "lee"),
]

with open(CONTACTS) as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames or [])
    rows = list(reader)

tagged = 0
for row in rows:
    first = row["first_name"].lower().split()[0] if row["first_name"] else ""
    first_full = row["first_name"].lower() if row["first_name"] else ""
    last = row["last_name"].lower() if row["last_name"] else ""

    for pf, pl in HARVARD_3:
        if (first == pf or pf in first_full) and last.startswith(pl):
            existing = row.get("relationship", "")
            if "friends_harvard" not in existing:
                row["relationship"] = (existing + "|friends_harvard").strip("|") if existing else "friends_harvard"
                tagged += 1
                print(f"  {row['first_name']} {row['last_name']} | {row['position']} @ {row['company']}")
            break

with open(CONTACTS, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"\nTagged {tagged} as friends_harvard")
