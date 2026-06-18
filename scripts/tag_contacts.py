#!/usr/bin/env python3
"""Tag specific contacts with relationship context.
Edit the TAGS dict below to add new relationship tags."""
import csv
from pathlib import Path

CONTACTS = Path("/Users/arthur/www/dashbud/content/outreach/contacts.csv")

# ── Define tags: relationship_name -> list of (first, last) tuples ──
# Last names are matched as "starts with" to handle suffixes like "J.D."

TAGS = {
    "friends_seminary": [
        ("william", "lara"),
        ("thor", "garcia"),
        ("natasha", "encarnacion"),
        ("jessica", "rovello"),
        ("michael", "bachrach"),
        ("david", "borla"),
        ("eric", "lane"),
        ("zach", "roth"),
        ("noah", "gaynin"),
        ("paul", "falkenstein"),
        ("jessica", "wapner"),
        ("mandla", "nkosi"),
        ("cara", "cibener"),
        ("daisy", "de plume"),
        ("alexandra", "zissu"),
        ("jonathan", "jacoby"),
        ("aundrea", "fares"),
    ],
}

# ── Process ──

with open(CONTACTS) as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames or [])
    rows = list(reader)

if "relationship" not in fieldnames:
    fieldnames.append("relationship")
    for row in rows:
        row["relationship"] = ""

total_tagged = 0
for tag_name, people in TAGS.items():
    for row in rows:
        first = row["first_name"].lower().split()[0] if row["first_name"] else ""
        last = row["last_name"].lower() if row["last_name"] else ""

        matched = False
        for pf, pl in people:
            if first == pf and last.startswith(pl):
                matched = True
                break

        if matched:
            existing = row.get("relationship", "")
            if tag_name not in existing:
                row["relationship"] = (existing + "|" + tag_name).strip("|") if existing else tag_name
                total_tagged += 1
                print(f"  [{tag_name}] {row['first_name']} {row['last_name']} ({row['company']})")

with open(CONTACTS, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"\nTagged {total_tagged} contacts")
