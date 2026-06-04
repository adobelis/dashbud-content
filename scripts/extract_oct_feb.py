#!/usr/bin/env python3
"""Extract deliverables from the Oct-Feb export."""
import json
import re
from pathlib import Path

BASE = Path("/Users/arthur/www/dashbud/content")
OUT = BASE / "extracted"
OUT.mkdir(exist_ok=True)

with open(BASE / "export_oct_feb" / "conversations.json") as f:
    convos = json.load(f)

def get_text(msg):
    text = msg.get("text") or msg.get("content") or ""
    if isinstance(text, list):
        parts = []
        for p in text:
            if isinstance(p, dict) and p.get("type") == "text":
                parts.append(p.get("text", ""))
        return "\n".join(parts)
    return text

def extract_long_assistant_blocks(msgs):
    blocks = []
    for j, msg in enumerate(msgs):
        sender = msg.get("sender") or msg.get("role") or "?"
        if sender != "assistant":
            continue
        text = get_text(msg)
        if len(text) > 500:
            context = ""
            if j > 0:
                prev = msgs[j-1]
                prev_sender = prev.get("sender") or prev.get("role") or "?"
                if prev_sender == "human":
                    context = get_text(prev)[:300]
            blocks.append({"index": j, "context": context, "text": text, "length": len(text)})
    return blocks

for idx, c in enumerate(convos):
    name = c.get("name") or f"untitled_{idx}"
    msgs = c.get("chat_messages", [])
    created = c.get("created_at", "?")[:10]
    summary = c.get("summary") or ""

    safe_name = re.sub(r'[^\w\s-]', '', name).strip().replace(' ', '_')[:60]
    # Use 20+ prefix to distinguish from original export
    conv_dir = OUT / f"{20+idx:02d}_{safe_name}"
    conv_dir.mkdir(exist_ok=True)

    full_text = []
    full_text.append(f"# {name}")
    full_text.append(f"Date: {created}")
    full_text.append(f"Summary: {summary}")
    full_text.append(f"Messages: {len(msgs)}")
    full_text.append("=" * 80)

    for j, msg in enumerate(msgs):
        sender = msg.get("sender") or msg.get("role") or "?"
        text = get_text(msg)
        ts = (msg.get("created_at") or "")[:19]
        full_text.append(f"\n--- [{sender.upper()}] {ts} ---")
        full_text.append(text)

    with open(conv_dir / "full_conversation.md", "w") as f:
        f.write("\n".join(full_text))

    blocks = extract_long_assistant_blocks(msgs)
    if blocks:
        deliverables = []
        deliverables.append(f"# Key Content from: {name}")
        deliverables.append(f"Date: {created}")
        deliverables.append(f"Total substantial assistant responses: {len(blocks)}\n")
        for b in blocks:
            deliverables.append("=" * 80)
            if b["context"]:
                deliverables.append(f"**User asked:** {b['context'][:200]}...")
            deliverables.append(f"**Response (msg #{b['index']}, {b['length']} chars):**\n")
            deliverables.append(b["text"])
            deliverables.append("")
        with open(conv_dir / "key_content.md", "w") as f:
            f.write("\n".join(deliverables))

    print(f"[{20+idx:02d}] {created} | {name}: {len(msgs)} msgs, {len(blocks)} deliverable blocks")
