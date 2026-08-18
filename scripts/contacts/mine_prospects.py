"""
Mine contacts.csv for potential Dashbud prospects.

Usage:
    python scripts/contacts/mine_prospects.py --help
    python scripts/contacts/mine_prospects.py --category finance
    python scripts/contacts/mine_prospects.py --seniority c_suite,vp
    python scripts/contacts/mine_prospects.py --company "Advance Local"
    python scripts/contacts/mine_prospects.py --keyword "analytics"
    python scripts/contacts/mine_prospects.py --era startup_era
    python scripts/contacts/mine_prospects.py --not-in-crm
    python scripts/contacts/mine_prospects.py --era-summary
"""

import argparse
import csv
import sys
from pathlib import Path

CONTACTS_PATH = Path(__file__).resolve().parents[2] / "outreach" / "linkedin_export.csv"
CRM_CONTACTS_PATH = Path(__file__).resolve().parents[2] / "outreach" / "crm" / "contacts.csv"

# Arthur's career timeline mapped to LinkedIn connection date ranges.
# Contacts connected during an era likely originated from that networking context.
# Boundaries are approximate — someone from college may have connected in 2012.
ERA_RANGES = [
    ("college",        None,   1999),  # pre-career connections
    ("pfm",            1997,   2000),
    ("empirix",        2000,   2002),
    ("nyu_law",        2002,   2005),
    ("cahill_gordon",  2005,   2009),
    ("startup_era",    2009,   2013),  # Evivio and other startup activities
    ("advance_local",  2014,   2022),
    ("gale",           2022,   2023),
    ("dashbud",        2024,   2030),
]


def infer_era(connected_on):
    """Infer networking era from LinkedIn connection date."""
    if not connected_on or not connected_on.strip():
        return "unknown"
    try:
        year = int(connected_on[:4])
    except (ValueError, IndexError):
        return "unknown"
    # Walk backwards through eras — later eras take precedence
    for era_name, start, end in reversed(ERA_RANGES):
        if start and end and start <= year <= end:
            return era_name
        if start is None and year <= end:
            return era_name
    return "unknown"


def load_contacts():
    with open(CONTACTS_PATH, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    # Enrich with inferred era
    for r in rows:
        r["_era"] = infer_era(r.get("connected_on", ""))
    return rows


def load_prospect_linkedin_urls():
    """Get linkedin_urls already in the CRM so we can filter them out."""
    urls = set()
    try:
        with open(CRM_CONTACTS_PATH, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                url = row.get("linkedin_url", "").strip()
                if url:
                    urls.add(url.rstrip("/").lower())
    except FileNotFoundError:
        pass
    return urls


def matches(contact, args):
    if args.era:
        if contact["_era"] not in [e.strip() for e in args.era.split(",")]:
            return False

    if args.category:
        cats = contact.get("category", "").lower()
        if not any(c.strip() in cats for c in args.category.split(",")):
            return False

    if args.seniority:
        sen = contact.get("seniority", "").lower()
        if not any(s.strip() == sen for s in args.seniority.split(",")):
            return False

    if args.company:
        comp = contact.get("company", "").lower()
        if args.company.lower() not in comp:
            return False

    if args.keyword:
        searchable = " ".join([
            contact.get("company", ""),
            contact.get("position", ""),
            contact.get("notes", ""),
            contact.get("category", ""),
        ]).lower()
        if args.keyword.lower() not in searchable:
            return False

    if args.relevance:
        rel = contact.get("dashbud_relevance", "").lower()
        if rel not in [r.strip() for r in args.relevance.split(",")]:
            return False

    return True


def print_era_summary(contacts):
    """Print a breakdown of contacts by inferred era."""
    from collections import Counter
    eras = Counter(c["_era"] for c in contacts)
    print("\nContacts by networking era:\n")
    for era_name, _, _ in ERA_RANGES:
        count = eras.get(era_name, 0)
        if count:
            bar = "#" * (count // 10)
            print(f"  {era_name:20s} {count:5d}  {bar}")
    unknown = eras.get("unknown", 0)
    if unknown:
        print(f"  {'unknown':20s} {unknown:5d}")
    print(f"\n  {'TOTAL':20s} {len(contacts):5d}")


def main():
    parser = argparse.ArgumentParser(description="Mine contacts.csv for prospects")
    parser.add_argument("--category", help="Filter by category (comma-separated, partial match)")
    parser.add_argument("--seniority", help="Filter by seniority (comma-separated: c_suite,vp,director,manager,founder)")
    parser.add_argument("--company", help="Filter by company name (partial match)")
    parser.add_argument("--keyword", help="Search across company, position, notes, category")
    parser.add_argument("--relevance", help="Filter by dashbud_relevance (high,medium,low)")
    parser.add_argument("--era", help="Filter by networking era (college,pfm,empirix,nyu_law,cahill_gordon,startup_era,advance_local,gale,dashbud)")
    parser.add_argument("--not-in-crm", action="store_true", help="Exclude contacts already in crm/contacts.csv")
    parser.add_argument("--era-summary", action="store_true", help="Show breakdown of contacts by era")
    parser.add_argument("--limit", type=int, default=50, help="Max results (default 50)")
    args = parser.parse_args()

    contacts = load_contacts()

    if args.era_summary:
        print_era_summary(contacts)
        return

    crm_urls = load_prospect_linkedin_urls() if args.not_in_crm else set()

    results = []
    for c in contacts:
        if not matches(c, args):
            continue
        if args.not_in_crm:
            url = c.get("linkedin_url", "").strip().rstrip("/").lower()
            if url and url in crm_urls:
                continue
        results.append(c)

    if not results:
        print("No contacts matched your filters.")
        sys.exit(0)

    print(f"\n{len(results)} contacts matched:\n")
    for i, c in enumerate(results[:args.limit], 1):
        name = f"{c.get('first_name', '')} {c.get('last_name', '')}".strip()
        company = c.get("company", "") or "—"
        position = c.get("position", "") or "—"
        category = c.get("category", "") or "—"
        seniority = c.get("seniority", "") or "—"
        relevance = c.get("dashbud_relevance", "") or "—"
        era = c.get("_era", "") or "—"
        linkedin = c.get("linkedin_url", "") or "—"
        connected = c.get("connected_on", "") or "—"
        print(f"  {i:3}. {name}")
        print(f"       {position} @ {company}")
        print(f"       era={era}  category={category}  seniority={seniority}  relevance={relevance}")
        print(f"       connected={connected}  {linkedin}")
        notes = c.get("notes", "")
        if notes:
            print(f"       notes: {notes}")
        print()

    if len(results) > args.limit:
        print(f"  ... and {len(results) - args.limit} more (use --limit to see all)")


if __name__ == "__main__":
    main()
