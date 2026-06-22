#!/usr/bin/env python3
"""Survey all three exports to build a complete picture."""
import json
from pathlib import Path

BASE = Path("/Users/arthur/www/dashbud/content")

exports = {
    "original (Jun 1 - Oct 30)": BASE / "conversations.json",
    "export_jan_jun": BASE / "export_jan_jun" / "conversations.json",
    "export_oct_feb": BASE / "export_oct_feb" / "conversations.json",
}

all_convos = {}

for label, path in exports.items():
    with open(path) as f:
        convos = json.load(f)

    print(f"\n{'='*80}")
    print(f"{label}: {path}")
    print(f"  Conversations: {len(convos)}")

    if not convos:
        print("  (empty)")
        continue

    for i, c in enumerate(convos):
        name = c.get("name") or "(untitled)"
        created = c.get("created_at", "?")[:10]
        updated = c.get("updated_at", "?")[:10]
        uuid = c.get("uuid", "?")
        msgs = c.get("chat_messages", [])
        num_msgs = len(msgs)

        # Check if text is actually present
        has_text = any(
            (m.get("text") or m.get("content") or "") != ""
            for m in msgs
        )

        print(f"  [{i:2d}] {created}→{updated} | {num_msgs:>4} msgs | text={'Y' if has_text else 'N'} | {uuid[:8]}... | {name}")

        if uuid not in all_convos:
            all_convos[uuid] = {
                "name": name, "created": created, "updated": updated,
                "msgs": num_msgs, "has_text": has_text, "sources": [label]
            }
        else:
            all_convos[uuid]["sources"].append(label)

print(f"\n{'='*80}")
print(f"COMBINED: {len(all_convos)} unique conversations")
print(f"\nDuplicates (appear in multiple exports):")
for uuid, info in sorted(all_convos.items(), key=lambda x: x[1]["created"]):
    if len(info["sources"]) > 1:
        print(f"  {info['created']} | {info['name']} | in: {', '.join(info['sources'])}")

print(f"\nTimeline of unique conversations:")
for uuid, info in sorted(all_convos.items(), key=lambda x: x[1]["created"]):
    text_flag = "+" if info["has_text"] else "EMPTY"
    src = info["sources"][0][:20]
    print(f"  {info['created']} | {info['msgs']:>4} msgs | {text_flag:>5} | {src:<20} | {info['name']}")
