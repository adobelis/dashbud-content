#!/usr/bin/env python3
"""Inspect the untitled conversations [1-4] to see what's actually in them."""
import json
from pathlib import Path

BASE = Path("/Users/arthur/www/dashbud/content")

with open(BASE / "conversations.json") as f:
    convos = json.load(f)

for i in [1, 2, 3, 4]:
    c = convos[i]
    name = c.get("name") or "(untitled)"
    msgs = c.get("chat_messages", [])
    created = c.get("created_at", "?")[:10]
    summary = c.get("summary") or "(no summary)"

    print(f"\n{'='*80}")
    print(f"[{i}] {created} | {len(msgs)} msgs | {name}")
    print(f"Summary: {summary}")
    print(f"{'='*80}")

    for j, msg in enumerate(msgs):
        sender = msg.get("sender") or msg.get("role") or "?"
        text = msg.get("text") or msg.get("content") or ""

        # Check for attachments/files
        attachments = msg.get("attachments") or msg.get("files") or msg.get("images") or []
        content_parts = msg.get("content") if isinstance(msg.get("content"), list) else []

        if isinstance(text, list):
            parts_info = []
            for part in text:
                if isinstance(part, dict):
                    ptype = part.get("type", "?")
                    if ptype == "text":
                        parts_info.append(f"text({len(part.get('text',''))} chars)")
                    else:
                        parts_info.append(f"{ptype}({json.dumps({k:v for k,v in part.items() if k != 'text'})})")
            text_preview = f"[CONTENT BLOCKS: {', '.join(parts_info)}]"
        else:
            text_preview = text[:300].replace("\n", " ").strip() if text else "(empty)"

        attach_info = ""
        if attachments:
            attach_info = f" | ATTACHMENTS: {json.dumps(attachments)[:200]}"
        if content_parts:
            attach_info += f" | CONTENT_PARTS: {len(content_parts)} blocks"

        # Check all keys for anything unusual
        extra_keys = [k for k in msg.keys() if k not in ('sender', 'role', 'text', 'content', 'uuid', 'created_at', 'updated_at', 'index')]
        extra_info = f" | extra_keys: {extra_keys}" if extra_keys else ""

        print(f"\n  msg[{j}] {sender}{attach_info}{extra_info}")
        print(f"    {text_preview[:400]}")
