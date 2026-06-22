#!/usr/bin/env python3
"""Tag Harvard college friends."""
import csv
from pathlib import Path

CONTACTS = Path("/Users/arthur/www/dashbud/content/outreach/contacts.csv")

HARVARD = [
    ("arkadi", "gerney"),
    ("timothy", "cullen"),
    ("john", "trinidad"),
    ("isaac", "taylor"),
    ("brendan", "reilly"),
    ("gillian", "morris"),
    ("daniel", "bisgeier"),
    ("anurima", "bhargava"),
    ("nancy", "meakem"),
    ("kitt", "hirasaki"),
    ("cas", "holloway"),
    ("chris", "nicholson"),
    ("zachary", "taylor"),  # also collegiate
    ("larry", "hardesty"),
    ("ketan", "jhaveri"),
    ("jason", "watkins"),
    ("bethany", "leeman"),
    ("zeeshan", "zaidi"),
    ("priya", "aiyar"),
    ("maria", "gambale"),
    ("quentin", "palfrey"),
    ("vanessa", "liu"),
]

# NOT tagging: Raffi Freeman (friend of friend), Heidi Curran (deceased)

with open(CONTACTS) as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames or [])
    rows = list(reader)

tagged = 0
for row in rows:
    first = row["first_name"].lower().split()[0] if row["first_name"] else ""
    last = row["last_name"].lower() if row["last_name"] else ""

    for pf, pl in HARVARD:
        if first == pf and last.startswith(pl):
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
