#!/usr/bin/env python3
"""
Normalize scrape filenames to the content's published date, and keep references in sync.

Convention: scrapes/<published>-<domain>-<slug>.md. The access date stays in frontmatter (`fetched:`).

Usage (venv activated, from repo root):
  python scripts/research/scrape_rename.py                      # dry run: show what would change
  python scripts/research/scrape_rename.py --apply              # rename files (+ _html twins), update refs
  python scripts/research/scrape_rename.py --set FILE DATE [NEWSLUG] ... --apply
        write `published: DATE` into FILE's frontmatter (and optionally replace its slug), then rename

A file whose frontmatter has no `published:` and no --set is left alone and listed.
References updated: any `scrapes/<old name>` string under website/blog/_feed/ and outreach/crm/.
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from repo_env import REPO_ROOT  # noqa: E402

SCRAPES = REPO_ROOT / "scrapes"
HTML = SCRAPES / "_html"
REF_DIRS = [REPO_ROOT / "website" / "blog" / "_feed", REPO_ROOT / "outreach" / "crm"]
NAME_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-([a-z0-9]+)-(.+)\.md$")


def read_front(path: Path) -> tuple[dict, str, str]:
    text = path.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}, "", text
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm, m.group(0), text[m.end():]


def set_published(path: Path, day: str) -> None:
    text = path.read_text()
    if re.search(r"^published:.*$", text, re.M):
        text = re.sub(r"^published:.*$", f"published: {day}", text, count=1, flags=re.M)
    else:
        text = text.replace("---\n", f"---\npublished: {day}\n", 1)
    path.write_text(text)


def update_refs(old: str, new: str) -> int:
    n = 0
    for d in REF_DIRS:
        for p in d.rglob("*.md"):
            t = p.read_text()
            if f"scrapes/{old}" in t:
                p.write_text(t.replace(f"scrapes/{old}", f"scrapes/{new}"))
                n += 1
    return n


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--set", nargs="+", action="append", default=[], metavar=("FILE DATE [NEWSLUG]"),
                    help="FILE DATE [NEWSLUG]; repeatable")
    a = ap.parse_args()

    overrides: dict[str, tuple[str, str | None]] = {}
    for item in a.set:
        if len(item) < 2:
            ap.error("--set needs FILE DATE [NEWSLUG]")
        overrides[Path(item[0]).name] = (item[1], item[2] if len(item) > 2 else None)

    plan, skipped = [], []
    for path in sorted(SCRAPES.glob("*.md")):
        m = NAME_RE.match(path.name)
        if not m:
            skipped.append((path.name, "name not in convention"))
            continue
        cur_date, domain, slug = m.groups()
        fm, _, _ = read_front(path)
        pub, new_slug = overrides.get(path.name, (fm.get("published", ""), None))
        if not pub:
            skipped.append((path.name, "no published date"))
            continue
        slug = new_slug or slug
        if slug.startswith(domain + "-"):
            slug = slug[len(domain) + 1:]
        new_name = f"{pub}-{domain}-{slug}.md"
        if new_name != path.name or path.name in overrides:
            plan.append((path, new_name, pub))

    for path, new_name, pub in plan:
        print(f"{path.name}\n  -> {new_name}")
        if a.apply:
            if path.name in overrides:
                set_published(path, pub)
            new_path = path.with_name(new_name)
            path.rename(new_path)
            old_html = HTML / f"{path.stem}.html"
            if old_html.exists():
                old_html.rename(HTML / f"{new_path.stem}.html")
            n = update_refs(path.name, new_name)
            print(f"     refs updated: {n}")
    for name, why in skipped:
        print(f"skip  {name}  ({why})")
    if not a.apply and plan:
        print("\n(dry run; add --apply)")


if __name__ == "__main__":
    main()
