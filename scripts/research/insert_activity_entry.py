#!/usr/bin/env python3
"""Insert a new dated entry into sales/activity-log.md above an existing heading.

Usage: .venv/bin/python scripts/research/insert_activity_entry.py
"""
from pathlib import Path

LOG = Path(__file__).resolve().parents[2] / "sales" / "activity-log.md"
ANCHOR = "## 2026-10-08 (Thursday)"

ENTRY = """## 2026-10-21–22 (Wednesday–Thursday)

### Marketing — LinkedIn launch
- **Founder announcement posted** Wed 10/21 2:00pm — "Data is born free" (Rousseau hook). First public association of Arthur with Dashbud. Full stats and running log in `outreach/linkedin-post-tracker.md`.
- **~21h performance:** 965 impressions, 507 members reached, 48% out-of-network, 40 engagements (23 reactions / 13 comments / 2 reposts). ~4.1% engagement rate; comment-to-reaction ratio 0.57, well above typical — the likely driver of the out-of-network reach.
- **Promotion legwork:** ~30 of 50 planned personal outreaches done (text + DM). Escalating to high-value promoters only once the post is ~a day old, so the ask comes with visible traction attached rather than as a cold favor. Post written to be non-time-sensitive for exactly this reason.
- Outcomes (DMs, profile→site traffic, notable commenters) still to be filled in.

---

"""


def main() -> None:
    text = LOG.read_text(encoding="utf-8")
    if "## 2026-10-21–22" in text:
        print("Entry already present — no change.")
        return
    if ANCHOR not in text:
        raise SystemExit(f"Anchor not found: {ANCHOR!r}")
    LOG.write_text(text.replace(ANCHOR, ENTRY + ANCHOR, 1), encoding="utf-8")
    print(f"Inserted entry above {ANCHOR!r}")


if __name__ == "__main__":
    main()
