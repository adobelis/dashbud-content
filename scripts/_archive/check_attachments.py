#!/usr/bin/env python3
"""Check attachments/files fields in untitled conversations."""
import json
from pathlib import Path

BASE = Path("/Users/arthur/www/dashbud/content")

with open(BASE / "conversations.json") as f:
    convos = json.load(f)

for i in [1, 2, 3, 4]:
    c = convos[i]
    msgs = c.get("chat_messages", [])
    print(f"\n[{i}] {c.get('created_at','?')[:10]} | {len(msgs)} msgs")
    for j, msg in enumerate(msgs):
        attachments = msg.get("attachments", [])
        files = msg.get("files", [])
        # Also check content field structure
        content = msg.get("content")
        if attachments or files or (isinstance(content, list) and content):
            sender = msg.get("sender", "?")
            print(f"  msg[{j}] {sender}:")
            if attachments:
                print(f"    attachments: {json.dumps(attachments, indent=2)[:500]}")
            if files:
                print(f"    files: {json.dumps(files, indent=2)[:500]}")
            if isinstance(content, list):
                for p, part in enumerate(content):
                    if isinstance(part, dict):
                        ptype = part.get("type", "?")
                        if ptype != "text":
                            print(f"    content[{p}]: type={ptype}, keys={list(part.keys())}")
                        else:
                            t = part.get("text", "")
                            print(f"    content[{p}]: text ({len(t)} chars) = {t[:100]}...")

# Also check if conversation [14] has attachments (it had empty first msg)
c14 = convos[14]
msgs14 = c14.get("chat_messages", [])
first = msgs14[0]
print(f"\n[14] first msg attachments: {first.get('attachments', [])}")
print(f"[14] first msg files: {first.get('files', [])}")
