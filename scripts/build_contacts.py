#!/usr/bin/env python3
"""Build a master contacts file from LinkedIn export, with source field and enrichment-ready structure."""
import csv
from pathlib import Path
from datetime import datetime

SRC = Path("/Users/arthur/www/dashbud/content/outreach/arthur_personal/Complete_LinkedInDataExport_06-13-2026.zip/Connections.csv")
OUT = Path("/Users/arthur/www/dashbud/content/outreach/contacts.csv")

# Read LinkedIn connections, skipping the notes header
rows = []
with open(SRC) as f:
    # Skip the first 3 lines (notes + blank line)
    for _ in range(3):
        next(f)
    reader = csv.DictReader(f)
    for row in reader:
        # Parse connection date
        connected_on = row.get("Connected On", "").strip()
        try:
            dt = datetime.strptime(connected_on, "%d %b %Y")
            connected_iso = dt.strftime("%Y-%m-%d")
        except (ValueError, TypeError):
            connected_iso = connected_on

        rows.append({
            "first_name": row.get("First Name", "").strip(),
            "last_name": row.get("Last Name", "").strip(),
            "company": row.get("Company", "").strip(),
            "position": row.get("Position", "").strip(),
            "email": row.get("Email Address", "").strip(),
            "linkedin_url": row.get("URL", "").strip(),
            "connected_on": connected_iso,
            "source": "ad_linkedin",
            "category": "",  # to be enriched: tech_colleague, lawyer, personal, networking, startup_media, advance_local, etc.
            "notes": "",
            "outreach_priority": "",  # high, medium, low, skip
            "dashbud_relevance": "",  # prospect, connector, advisor, none
        })

# Sort by connection date descending (most recent first)
rows.sort(key=lambda r: r["connected_on"] if r["connected_on"] else "0000-00-00", reverse=True)

# Write master contacts file
fieldnames = ["first_name", "last_name", "company", "position", "email", "linkedin_url",
              "connected_on", "source", "category", "notes", "outreach_priority", "dashbud_relevance"]

with open(OUT, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Wrote {len(rows)} contacts to {OUT}")

# Print some stats
companies = {}
for r in rows:
    c = r["company"]
    if c:
        companies[c] = companies.get(c, 0) + 1

print(f"\nTop 20 companies:")
for company, count in sorted(companies.items(), key=lambda x: -x[1])[:20]:
    print(f"  {count:3d}  {company}")

# Connection date distribution
years = {}
for r in rows:
    y = r["connected_on"][:4] if r["connected_on"] else "unknown"
    years[y] = years.get(y, 0) + 1

print(f"\nConnections by year:")
for year, count in sorted(years.items()):
    print(f"  {year}: {count}")
