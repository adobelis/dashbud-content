#!/usr/bin/env python3
"""Check conversation boundaries - do any start midway or end abruptly?"""
import json
from pathlib import Path

BASE = Path("/Users/arthur/www/dashbud/content")

with open(BASE / "conversations.json") as f:
    convos = json.load(f)

for i, c in enumerate(convos):
    name = c.get("name") or "(untitled)"
    msgs = c.get("chat_messages", [])
    created = c.get("created_at", "?")[:10]
    updated = c.get("updated_at", "?")[:10]

    if not msgs:
        print(f"\n[{i}] {created} | {name} — NO MESSAGES")
        continue

    # Get first and last messages
    first = msgs[0]
    last = msgs[-1]

    first_sender = first.get("sender") or first.get("role") or "?"
    last_sender = last.get("sender") or last.get("role") or "?"

    first_text = first.get("text") or first.get("content") or ""
    last_text = last.get("text") or last.get("content") or ""

    # Handle content that might be a list of blocks
    if isinstance(first_text, list):
        first_text = " ".join(b.get("text", "") for b in first_text if isinstance(b, dict))
    if isinstance(last_text, list):
        last_text = " ".join(b.get("text", "") for b in last_text if isinstance(b, dict))

    first_preview = first_text[:150].replace("\n", " ").strip()
    last_preview = last_text[-200:].replace("\n", " ").strip()

    # Check for signs of mid-conversation start
    mid_start = False
    if first_text.lower().startswith(("ok ", "okay ", "yes", "right", "sure", "continuing", "as i", "as we", "going back", "let's continue", "picking up")):
        mid_start = True

    # Check for abrupt ending - last message from human (no AI response) or very short
    abrupt_end = False
    if last_sender == "human":
        abrupt_end = True

    print(f"\n[{i}] {created}→{updated} | {len(msgs)} msgs | {name}")
    if mid_start:
        print(f"  ⚠️  POSSIBLE MID-START")
    if abrupt_end:
        print(f"  ⚠️  ENDS ON HUMAN MESSAGE (no AI response)")
    print(f"  FIRST ({first_sender}): {first_preview}")
    print(f"  LAST  ({last_sender}): ...{last_preview[-150:]}")
