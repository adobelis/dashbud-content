#!/usr/bin/env python3
"""Extract marketing deliverables from conversations into organized files."""
import json
import re
import os
from pathlib import Path

BASE = Path("/Users/arthur/www/dashbud/content")
OUT = BASE / "extracted"
OUT.mkdir(exist_ok=True)

with open(BASE / "conversations.json") as f:
    convos = json.load(f)

# Marketing-related conversation indices
MARKETING_INDICES = [0, 8, 10, 11, 14, 15, 16, 17, 18]

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
    """Find substantial assistant responses that likely contain deliverables."""
    blocks = []
    for j, msg in enumerate(msgs):
        sender = msg.get("sender") or msg.get("role") or "?"
        if sender != "assistant":
            continue
        text = get_text(msg)
        if len(text) > 500:  # substantial content
            # Get the preceding human message for context
            context = ""
            if j > 0:
                prev = msgs[j-1]
                prev_sender = prev.get("sender") or prev.get("role") or "?"
                if prev_sender == "human":
                    context = get_text(prev)[:300]
            blocks.append({
                "index": j,
                "context": context,
                "text": text,
                "length": len(text)
            })
    return blocks

# Process each marketing conversation
for idx in MARKETING_INDICES:
    c = convos[idx]
    name = c.get("name") or f"untitled_{idx}"
    msgs = c.get("chat_messages", [])
    created = c.get("created_at", "?")[:10]
    summary = c.get("summary") or ""

    # Clean name for filename
    safe_name = re.sub(r'[^\w\s-]', '', name).strip().replace(' ', '_')[:60]
    conv_dir = OUT / f"{idx:02d}_{safe_name}"
    conv_dir.mkdir(exist_ok=True)

    # Write full conversation as readable text
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

    # Extract substantial deliverables
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

    print(f"[{idx:02d}] {name}: {len(msgs)} msgs, {len(blocks)} deliverable blocks → {conv_dir.name}/")

# Also process the non-marketing ones for completeness
OTHER_INDICES = [i for i in range(len(convos)) if i not in MARKETING_INDICES and i not in [1,2,3,4]]
for idx in OTHER_INDICES:
    c = convos[idx]
    name = c.get("name") or f"untitled_{idx}"
    msgs = c.get("chat_messages", [])
    created = c.get("created_at", "?")[:10]
    summary = c.get("summary") or ""

    safe_name = re.sub(r'[^\w\s-]', '', name).strip().replace(' ', '_')[:60]
    conv_dir = OUT / f"{idx:02d}_{safe_name}"
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
    print(f"[{idx:02d}] {name}: {len(msgs)} msgs, {len(blocks)} deliverable blocks → {conv_dir.name}/ (other)")

print(f"\nAll extracted to: {OUT}")
