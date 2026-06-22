#!/usr/bin/env python3
"""Tag Harvard batch 2. Also tag Jamie Knox and Norm Cappell as colleagues_cahill."""
import csv
from pathlib import Path

CONTACTS = Path("/Users/arthur/www/dashbud/content/outreach/contacts.csv")

HARVARD_2 = [
    ("marco", "torres"),
    ("joseph", "mullin"),
    ("jen", "leong"),
    ("robin", "goldstein"),
    ("david", "bonfili"),
    ("charles", "imohiosen"),
    ("john", "mitchell"),
    ("nadia", "croes"),
    ("garance", "franke"),
    ("kermit", "roosevelt"),
    ("jeremy", "faro"),
    ("candace", "brown"),
    ("philip", "munger"),
    ("evelyn", "kim"),
    ("david", "sollors"),
    ("ali", "zarrinpar"),
    ("allan", "piper"),
    ("braxton", "robbason"),
]

CAHILL = [
    ("jamie", "knox"),
    ("norm", "cappell"),
]

# CT Tamura → friend (not harvard) — skip for now, can tag as personal later

with open(CONTACTS) as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames or [])
    rows = list(reader)

def tag_group(rows, people, tag_name):
    tagged = 0
    for row in rows:
        first = row["first_name"].lower().split()[0] if row["first_name"] else ""
        # Also check if first name contains the search term (for hyphenated names etc)
        first_full = row["first_name"].lower() if row["first_name"] else ""
        last = row["last_name"].lower() if row["last_name"] else ""

        for pf, pl in people:
            if (first == pf or pf in first_full) and last.startswith(pl):
                existing = row.get("relationship", "")
                if tag_name not in existing:
                    row["relationship"] = (existing + "|" + tag_name).strip("|") if existing else tag_name
                    tagged += 1
                    print(f"  [{tag_name}] {row['first_name']} {row['last_name']} | {row['position']} @ {row['company']}")
                break
    return tagged

t1 = tag_group(rows, HARVARD_2, "friends_harvard")
t2 = tag_group(rows, CAHILL, "colleagues_cahill")

with open(CONTACTS, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"\nTagged {t1} as friends_harvard, {t2} as colleagues_cahill")
