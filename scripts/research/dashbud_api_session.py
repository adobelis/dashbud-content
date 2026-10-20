#!/usr/bin/env python3
"""
Run natural-language queries against a Dashbud workspace via the agent API.

Credentials come from the content repo's .env (DASHBUD_API_KEY) via python-dotenv.
The key is never printed or logged. Every API response is saved as JSON under
scripts/research/output/ so results can be cited later.

Usage (from the content repo root, with the venv):
  .venv/bin/python scripts/research/dashbud_api_session.py workspaces
  .venv/bin/python scripts/research/dashbud_api_session.py model <ws_id>
  .venv/bin/python scripts/research/dashbud_api_session.py sources <ws_id>
  .venv/bin/python scripts/research/dashbud_api_session.py ask <ws_id> "question" [--convo <id>]

Env:
  DASHBUD_API_KEY   required
  DASHBUD_BASE      optional, default https://api.getdashbud.com/api
"""

import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

import requests
from dotenv import load_dotenv

REPO_ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = Path(__file__).resolve().parent / "output"
load_dotenv(REPO_ROOT / ".env")

API_KEY = os.environ.get("DASHBUD_API_KEY")
BASE = os.environ.get("DASHBUD_BASE", "https://app-22ib.getdashbud.com/api").rstrip("/")

if not API_KEY:
    sys.exit("DASHBUD_API_KEY not set in .env")

HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}


def save(label: str, payload) -> Path:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    path = OUT_DIR / f"{stamp}_{label}.json"
    path.write_text(json.dumps(payload, indent=2, default=str))
    return path


def get(path: str):
    r = requests.get(f"{BASE}{path}", headers=HEADERS, timeout=60)
    r.raise_for_status()
    return r.json()


def post(path: str, body: dict):
    r = requests.post(f"{BASE}{path}", headers=HEADERS, json=body, timeout=60)
    r.raise_for_status()
    return r.json()


def cmd_workspaces():
    data = get("/orgs/current/api-key/workspaces")
    p = save("workspaces", data)
    for ws in data["data"]["workspaces"]:
        print(f"{ws['id']:>5}  {ws['name']}  ({ws['slug']})")
    print(f"saved: {p}")


def cmd_model(ws_id: str):
    data = get(f"/workspaces/{ws_id}/blueprint/latest")
    p = save(f"model_ws{ws_id}", data)
    print(json.dumps(data, indent=2, default=str)[:6000])
    print(f"saved: {p}")


def cmd_sources(ws_id: str):
    data = get(f"/data-sources?scope=workspace&workspace_id={ws_id}")
    p = save(f"sources_ws{ws_id}", data)
    print(json.dumps(data, indent=2, default=str)[:4000])
    print(f"saved: {p}")


def poll(job_id: int, timeout_s: int = 180):
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        time.sleep(3)
        r = get(f"/jobs/{job_id}")["data"]
        if r["status"] == "completed":
            return r
        if r["status"] == "failed":
            return r
    return {"status": "timeout", "job_id": job_id}


def print_result(res: dict):
    data = res.get("data") or {}
    cols = data.get("columns") or []
    rows_by_col = data.get("data") or {}
    rows = list(zip(*[rows_by_col[c] for c in cols])) if cols else []
    print(f"status: {res.get('status')}  confidence: {data.get('confidence', '?')}  rows: {len(rows)}")
    if cols:
        print(" | ".join(cols))
        for row in rows[:25]:
            print(" | ".join(str(v) for v in row))
        if len(rows) > 25:
            print(f"... {len(rows) - 25} more rows")
    sql = data.get("sql") or data.get("query")
    if sql:
        print("\n-- SQL --")
        print(sql)
    msg = data.get("assistant_message") or data.get("message")
    if msg:
        print("\n-- assistant --")
        print(msg if isinstance(msg, str) else json.dumps(msg, indent=2, default=str)[:3000])
    convo = (data.get("user_message") or {}).get("conversation_id")
    if convo:
        print(f"\nconversation_id: {convo}")


def cmd_ask(ws_id: str, question: str, convo: str | None):
    body = {"user_text": question, "conversation_id": int(convo) if convo else None}
    job = post(f"/workspaces/{ws_id}/query/job", body)
    job_id = job["data"]["job_id"]
    print(f"job {job_id} submitted: {question!r}")
    res = poll(job_id)
    p = save(f"ask_ws{ws_id}_job{job_id}", {"question": question, "conversation_id": convo, "result": res})
    print_result(res)
    print(f"\nsaved: {p}")


def main(argv):
    if not argv:
        sys.exit(__doc__)
    cmd, args = argv[0], argv[1:]
    if cmd == "workspaces":
        cmd_workspaces()
    elif cmd == "model":
        cmd_model(args[0])
    elif cmd == "sources":
        cmd_sources(args[0])
    elif cmd == "ask":
        convo = None
        if "--convo" in args:
            i = args.index("--convo")
            convo = args[i + 1]
            args = args[:i] + args[i + 2:]
        cmd_ask(args[0], args[1], convo)
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
