#!/usr/bin/env python3
"""Derive CRM status from the append-only event log.

Reads outreach/crm/events/*.md and outreach/crm/accounts/*.md, then prints a
status board. Nothing is written — status is always derived, never stored, so
it cannot drift from the events the way pipeline.csv did.

Usage:
    .venv/bin/python scripts/crm/rollup.py              # status board
    .venv/bin/python scripts/crm/rollup.py --timeline   # full journal
    .venv/bin/python scripts/crm/rollup.py --stale 30   # quiet accounts
    .venv/bin/python scripts/crm/rollup.py --validate   # schema check
"""
from __future__ import annotations

import argparse
import datetime as dt
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("pyyaml required: .venv/bin/pip install pyyaml")

ROOT = Path(__file__).resolve().parents[2]
EVENTS = ROOT / "outreach" / "crm" / "events"
ACCOUNTS = ROOT / "outreach" / "crm" / "accounts"
PEOPLE = ROOT / "outreach" / "crm" / "people"

VALID_TYPES = {
    "meeting", "call", "email", "linkedin", "text", "demo", "poc_work",
    "payment", "contract", "internal_note", "marketing_post",
    "metrics_reading", "stage_change",
}
VALID_STAGES = {
    "exploratory", "demo_done", "poc", "trial", "proposal",
    "security_review", "closed_won", "closed_lost", "dormant",
}
OPEN_STAGES = VALID_STAGES - {"closed_won", "closed_lost"}


def parse(path: Path) -> dict | None:
    """Split YAML frontmatter from body. Returns None if no frontmatter."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    _, fm, *rest = text.split("---", 2)
    meta = yaml.safe_load(fm) or {}
    meta["_body"] = rest[0].strip() if rest else ""
    meta["_path"] = path
    return meta


def load(directory: Path) -> list[dict]:
    out = []
    for path in sorted(directory.glob("*.md")):
        if path.name in {"README.md", "SCHEMA.md"}:
            continue
        if (meta := parse(path)) is not None:
            out.append(meta)
    return out


def rollup(events: list[dict]) -> dict[str, dict]:
    """Reduce the event stream into per-account current state."""
    state: dict[str, dict] = {}
    for ev in sorted(events, key=lambda e: str(e.get("date", ""))):
        acct = ev.get("account")
        if not acct:
            continue
        cur = state.setdefault(acct, {"events": 0})
        cur["events"] += 1
        cur["last_activity"] = ev.get("date")
        cur["last_summary"] = ev.get("summary", "")
        if ev.get("stage_after"):
            cur["stage"] = ev["stage_after"]
        if ev.get("next_action"):
            cur["next_action"] = ev["next_action"]
            cur["next_action_date"] = ev.get("next_action_date")
    return state


def board(events: list[dict], accounts: list[dict]) -> None:
    state = rollup(events)
    names = {a["account_id"]: a.get("name", a["account_id"]) for a in accounts}
    today = dt.date.today()

    print(f"\n{'ACCOUNT':<28} {'STAGE':<16} {'LAST':<12} {'EV':>3}  NEXT ACTION")
    print("-" * 110)
    for acct, s in sorted(state.items(), key=lambda kv: str(kv[1].get("last_activity", "")), reverse=True):
        na = s.get("next_action", "") or ""
        nad = s.get("next_action_date")
        if nad:
            overdue = " [OVERDUE]" if str(nad) < str(today) else ""
            na = f"{na[:48]} (due {nad}{overdue})"
        else:
            na = na[:60]
        print(f"{names.get(acct, acct):<28} {s.get('stage', '?'):<16} "
              f"{str(s.get('last_activity', '?')):<12} {s['events']:>3}  {na}")

    open_deals = {k: v for k, v in state.items() if v.get("stage") in OPEN_STAGES}
    won = [k for k, v in state.items() if v.get("stage") == "closed_won"]
    lost = [k for k, v in state.items() if v.get("stage") == "closed_lost"]
    no_acct = sum(1 for e in events if not e.get("account"))

    print(f"\n{len(events)} events across {len(state)} accounts "
          f"({no_acct} non-account events: marketing, metrics)")
    print(f"open: {len(open_deals)}  won: {len(won)}  lost: {len(lost)}")

    overdue = [(k, v) for k, v in state.items()
               if v.get("next_action_date") and str(v["next_action_date"]) < str(today)]
    if overdue:
        print(f"\n!! {len(overdue)} OVERDUE next action(s):")
        for acct, v in overdue:
            print(f"   {names.get(acct, acct)} — due {v['next_action_date']}: {v['next_action']}")


def timeline(events: list[dict]) -> None:
    print()
    for ev in sorted(events, key=lambda e: str(e.get("date", "")), reverse=True):
        acct = ev.get("account") or "-"
        print(f"{ev.get('date')}  {ev.get('type', '?'):<17} {acct:<24} {ev.get('summary', '')}")


def stale(events: list[dict], days: int) -> None:
    state = rollup(events)
    cutoff = dt.date.today() - dt.timedelta(days=days)
    print(f"\nAccounts with no activity since {cutoff} ({days} days):\n")
    found = False
    for acct, s in sorted(state.items(), key=lambda kv: str(kv[1].get("last_activity", ""))):
        last = s.get("last_activity")
        if last and str(last) < str(cutoff) and s.get("stage") in OPEN_STAGES:
            print(f"  {acct:<28} last activity {last}  stage={s.get('stage')}")
            found = True
    if not found:
        print("  (none)")


def validate(events: list[dict], accounts: list[dict], people: list[dict]) -> int:
    errors = []
    known = {a.get("account_id") for a in accounts}
    known_people = {p.get("person_id") for p in people}
    seen_ids = set()

    for ev in events:
        path = ev["_path"].name
        eid = ev.get("event_id")
        if not eid:
            errors.append(f"{path}: missing event_id")
        elif eid != ev["_path"].stem:
            errors.append(f"{path}: event_id '{eid}' != filename stem")
        elif eid in seen_ids:
            errors.append(f"{path}: duplicate event_id '{eid}'")
        else:
            seen_ids.add(eid)

        if not ev.get("date"):
            errors.append(f"{path}: missing date")
        if not ev.get("summary"):
            errors.append(f"{path}: missing summary")
        if (t := ev.get("type")) not in VALID_TYPES:
            errors.append(f"{path}: invalid type '{t}'")
        if (s := ev.get("stage_after")) and s not in VALID_STAGES:
            errors.append(f"{path}: invalid stage_after '{s}'")
        if (a := ev.get("account")) and a not in known:
            errors.append(f"{path}: account '{a}' has no accounts/{a}.md")
        for person in ev.get("people") or []:
            if person not in known_people:
                errors.append(f"{path}: person '{person}' has no people/{person}.md")

    for acct in accounts:
        if not acct.get("account_id"):
            errors.append(f"{acct['_path'].name}: missing account_id")
        elif acct["account_id"] != acct["_path"].stem:
            errors.append(f"{acct['_path'].name}: account_id != filename stem")

    for person in people:
        name = person["_path"].name
        if not person.get("person_id"):
            errors.append(f"{name}: missing person_id (see SCHEMA.md person frontmatter)")
        elif person["person_id"] != person["_path"].stem:
            errors.append(f"{name}: person_id != filename stem")
        if not person.get("name"):
            errors.append(f"{name}: missing name")
        if (a := person.get("account")) and a not in known:
            errors.append(f"{name}: account '{a}' has no accounts/{a}.md")

    if errors:
        print(f"\n{len(errors)} problem(s):\n")
        for e in errors:
            print(f"  {e}")
        return 1
    print(f"\nOK - {len(events)} events, {len(accounts)} accounts, {len(people)} people, no problems.")
    return 0


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--timeline", action="store_true", help="print all events by date")
    ap.add_argument("--stale", type=int, metavar="DAYS", help="open accounts quiet for N days")
    ap.add_argument("--validate", action="store_true", help="check schema compliance")
    args = ap.parse_args()

    events, accounts, people = load(EVENTS), load(ACCOUNTS), load(PEOPLE)

    if args.validate:
        sys.exit(validate(events, accounts, people))
    if args.timeline:
        timeline(events)
    elif args.stale is not None:
        stale(events, args.stale)
    else:
        board(events, accounts)


if __name__ == "__main__":
    main()
