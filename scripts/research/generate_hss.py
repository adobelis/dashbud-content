#!/usr/bin/env python3
"""
Generate an HSS (HTML Screenshot) YAML config from a real Dashbud conversation.

Connects to local Postgres, reads conversation messages, and outputs a YAML
config file for the HSSConversation Astro component.

Usage:
  python3 generate_hss.py <conversation_id> [--workspace-name NAME] [--output PATH]
  python3 generate_hss.py 102 --output forge-frame-revenue.yaml
  python3 generate_hss.py --list   # list available conversations

Requires: psycopg2, pyyaml
Docker Postgres must be running.
"""
import argparse
import sys
import yaml

try:
    import psycopg2
except ImportError:
    print("ERROR: pip install psycopg2-binary")
    sys.exit(1)

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "dashbud_local",
    "user": "postgres",
    "password": "postgres",
}

HSS_OUTPUT_DIR = "/Users/arthur/www/dashbud/website/dashbud-home-astro-01/src/content/hss"


def get_conn():
    return psycopg2.connect(**DB_CONFIG)


def list_conversations():
    """List all query conversations with workspace context."""
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT c.id, c.title, w.name AS workspace, count(cm.id) AS msgs,
               c.last_activity_at::date
        FROM conversation c
        JOIN blueprint b ON b.id = c.blueprint_id
        JOIN workspace w ON w.id = b.workspace_id
        JOIN conversation_message cm ON cm.conversation_id = c.id
        WHERE c.topic = 'query'
        GROUP BY c.id, c.title, w.name, c.last_activity_at
        ORDER BY c.last_activity_at DESC
    """)
    rows = cur.fetchall()
    print(f"{'ID':>5} | {'Title':<25} | {'Workspace':<20} | {'Msgs':>4} | Last Active")
    print("-" * 90)
    for r in rows:
        print(f"{r[0]:>5} | {(r[1] or '-'):<25} | {r[2]:<20} | {r[3]:>4} | {r[4]}")
    conn.close()


def fetch_conversation(conv_id):
    """Fetch messages and workspace info for a conversation."""
    conn = get_conn()
    cur = conn.cursor()

    # Get workspace info
    cur.execute("""
        SELECT w.name, u.email
        FROM conversation c
        JOIN blueprint b ON b.id = c.blueprint_id
        JOIN workspace w ON w.id = b.workspace_id
        LEFT JOIN users u ON u.id = c.started_by
        WHERE c.id = %s
    """, (conv_id,))
    row = cur.fetchone()
    if not row:
        print(f"ERROR: Conversation {conv_id} not found")
        sys.exit(1)

    workspace_name = row[0]
    user_email = row[1] or ""

    # Derive initials from email
    local = user_email.split("@")[0] if user_email else "U"
    # Try to get first+last initials
    parts = local.replace(".", " ").replace("+", " ").split()
    initials = "".join(p[0].upper() for p in parts[:2]) if parts else "U"

    # Get messages
    cur.execute("""
        SELECT cm.role, cm.content_text, cm.content_type, cm.content_struct
        FROM conversation_message cm
        WHERE cm.conversation_id = %s
        ORDER BY cm.created_at
    """, (conv_id,))
    messages = cur.fetchall()
    conn.close()

    return workspace_name, initials, messages


def build_config(conv_id, workspace_override=None, max_messages=None):
    """Build an HSS YAML config from a conversation."""
    workspace_name, initials, raw_messages = fetch_conversation(conv_id)

    if workspace_override:
        workspace_name = workspace_override

    messages = []
    for role, content_text, content_type, content_struct in raw_messages:
        if max_messages and len(messages) >= max_messages:
            break

        msg = {"role": role, "text": content_text.strip()}

        # If assistant message has query results, add result config
        if role == "assistant" and content_struct:
            has_data = content_struct.get("data") or content_struct.get("sql")
            has_chart = content_struct.get("chartSuggestion")

            if has_data:
                result = {
                    "type": "chart" if has_chart else "table",
                    "active_tab": "visualize" if has_chart else "table",
                    "placeholder": "[Chart — replace with image]" if has_chart else "[Table — replace with image]",
                    "tabs": ["visualize", "table", "sql", "csv"],
                    "saveable": True,
                }

                # Check for params
                params = content_struct.get("params")
                if params and isinstance(params, dict):
                    result["params"] = [
                        {"label": k, "options": [f"[{k} values]"]}
                        for k in params.keys()
                    ]

                msg["result"] = result

        messages.append(msg)

    config = {
        "id": f"conv-{conv_id}",
        "workspace": workspace_name,
        "section": "Data Explorer",
        "user_initials": initials,
        "badge": "Live",
        "max_height": 520,
        "messages": messages,
    }

    return config


def main():
    parser = argparse.ArgumentParser(description="Generate HSS YAML from Dashbud conversation")
    parser.add_argument("conversation_id", nargs="?", type=int, help="Conversation ID")
    parser.add_argument("--list", action="store_true", help="List available conversations")
    parser.add_argument("--workspace-name", help="Override workspace name")
    parser.add_argument("--max-messages", type=int, help="Limit number of messages")
    parser.add_argument("--output", "-o", help="Output filename (in HSS content dir)")
    args = parser.parse_args()

    if args.list:
        list_conversations()
        return

    if not args.conversation_id:
        parser.print_help()
        sys.exit(1)

    config = build_config(
        args.conversation_id,
        workspace_override=args.workspace_name,
        max_messages=args.max_messages,
    )

    output = yaml.dump(config, default_flow_style=False, sort_keys=False, allow_unicode=True)

    if args.output:
        from pathlib import Path
        out_path = Path(HSS_OUTPUT_DIR) / args.output
        out_path.write_text(output)
        print(f"Wrote {out_path}")
    else:
        print(output)


if __name__ == "__main__":
    main()
