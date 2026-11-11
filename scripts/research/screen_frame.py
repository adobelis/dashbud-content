"""Screen a YouTube sampling frame down to codeable tutorial candidates.

The frame is raw search output: it contains shorts, developer bootcamps,
business-opportunity content and product ads alongside the actual
"here is how you build your own reporting" tutorials.

Screening is rule-based and every exclusion is recorded with its reason, so
the funnel is auditable and the rules can be argued with later.

Level is inferred from the query that surfaced the video (queries are grouped by
level in _queries.txt), then overridden by title signals where those are clearer.

Usage:
  python screen_frame.py FRAME.tsv --out SHORTLIST.tsv [--report]
"""
import csv
import re
import argparse
from collections import Counter, defaultdict

# query -> level of the spectrum in research/diy-ai-reporting/README.md
QUERY_LEVEL = {
    "chatgpt data analysis tutorial": "2-chat-upload",
    "analyze excel data with chatgpt": "2-chat-upload",
    "upload spreadsheet to chatgpt analysis": "2-chat-upload",
    "chatgpt advanced data analysis tutorial": "3-hosted-analysis",
    "claude analyze csv data": "3-hosted-analysis",
    "gemini analyze spreadsheet data": "3-hosted-analysis",
    "custom gpt for data analysis": "4-custom-gpt",
    "build a custom gpt for business reporting": "4-custom-gpt",
    "openai api python data analysis tutorial": "5-api-script",
    "automate reports with openai api": "5-api-script",
    "n8n ai reporting automation": "6-agent-automation",
    "make.com automate reporting ai": "6-agent-automation",
    "lovable build dashboard": "7-vibe-coded-app",
    "replit build data dashboard": "7-vibe-coded-app",
    "build internal tool with ai no code": "7-vibe-coded-app",
    "build a dashboard with chatgpt": "x-cross-level",
    "ai business intelligence no code": "x-cross-level",
    "automate business reporting with ai": "x-cross-level",
}

# Exclusions. Order matters -- first match wins, so the reason is the most
# specific one. Each is (reason, regex over the lowercased title).
TITLE_EXCLUSIONS = [
    ("dev-course", re.compile(
        r"\b(full course|bootcamp|complete course|crash course|full tutorial for beginners"
        r"|learn (python|sql|r\b)|python for|sql for|pandas|numpy|data structures"
        r"|roadmap|certification|interview questions)\b")),
    ("biz-opportunity", re.compile(
        r"(build (&|and) sell|make \$|\$\d+[k,]|/month|per month|side hustle"
        r"|agency|freelanc|get clients|rich|passive income|solo ai business"
        r"|how i made|earn money)")),
    ("career-commentary", re.compile(
        r"(will ai replace|is data analy\w+ dead|should you learn|career|get a job"
        r"|you'?re not behind|hired|salary)")),
    ("news-opinion", re.compile(
        r"(introducing |announc|keynote|what'?s new|changelog|vs\.? |comparison"
        r"|review:|reaction|explained in)")),
    ("not-reporting", re.compile(
        r"(resume|cover letter|email|instagram|youtube channel|thumbnail|logo"
        r"|song|music|video edit|game|chatbot for customer|trading bot|stock"
        r"|crypto|seo|blog post|content calendar)")),
]

MIN_DURATION = 150      # under ~2.5 min cannot show a build end to end
MAX_DURATION = 5400     # over 90 min is a course, not a tutorial


def to_int(value):
    try:
        return int(str(value).strip())
    except (TypeError, ValueError):
        return 0


def infer_level(row, queries):
    title = (row.get("title") or "").lower()
    signals = [
        (r"\blovable\b|\breplit\b|\bbolt\.new\b|\bv0\b|vibe", "7-vibe-coded-app"),
        (r"\bn8n\b|make\.com|\bzapier\b|\bagent\b|automation", "6-agent-automation"),
        (r"\bapi\b|\bpython script\b", "5-api-script"),
        (r"custom gpt|\bgpts\b|project instructions", "4-custom-gpt"),
        (r"advanced data analysis|code interpreter|\bcsv\b|data analyst mode",
         "3-hosted-analysis"),
    ]
    for pattern, level in signals:
        if re.search(pattern, title):
            return level
    levels = [QUERY_LEVEL.get(q, "") for q in queries]
    levels = [r for r in levels if r and r != "x-cross-level"]
    if levels:
        return Counter(levels).most_common(1)[0][0]
    return "x-cross-level"


def screen(row):
    """Return exclusion reason, or None to keep."""
    if str(row.get("is_shorts")).lower() == "true":
        return "shorts"
    duration = to_int(row.get("duration_s"))
    if duration and duration < MIN_DURATION:
        return "too-short"
    if duration > MAX_DURATION:
        return "too-long"
    title = (row.get("title") or "").lower()
    for reason, pattern in TITLE_EXCLUSIONS:
        if pattern.search(title):
            return reason
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("frame")
    parser.add_argument("--out", required=True)
    parser.add_argument("--report", action="store_true")
    args = parser.parse_args()

    with open(args.frame, newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))

    # collapse to one record per video, remembering every query that found it
    by_video = {}
    found_by = defaultdict(list)
    for row in rows:
        video_id = row.get("video_id")
        if not video_id:
            continue
        found_by[video_id].append(row.get("query", ""))
        rank = to_int(row.get("rank")) or 999
        if video_id not in by_video or rank < (to_int(by_video[video_id].get("rank")) or 999):
            by_video[video_id] = dict(row)

    kept, excluded = [], []
    for video_id, row in by_video.items():
        queries = sorted(set(found_by[video_id]))
        row["queries"] = "; ".join(queries)
        row["found_by"] = len(queries)
        row["level"] = infer_level(row, queries)
        reason = screen(row)
        if reason:
            row["excluded"] = reason
            excluded.append(row)
        else:
            row["excluded"] = ""
            kept.append(row)

    kept.sort(key=lambda r: (r["level"], -to_int(r.get("views"))))

    columns = ["level", "video_id", "published", "views", "likes", "comment_count",
               "duration_s", "channel", "title", "found_by", "queries", "url",
               "date_source", "excluded"]
    for row in kept:
        row.setdefault("date_source", "derived-from-relative-label")
    with open(args.out, "w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns,
                                delimiter="\t", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(kept)

    print(f"{len(by_video)} unique videos -> {len(kept)} candidates, "
          f"{len(excluded)} excluded")
    print(f"wrote {args.out}\n")

    print("== exclusions by reason ==")
    for reason, count in Counter(r["excluded"] for r in excluded).most_common():
        print(f"  {count:4d}  {reason}")

    print("\n== candidates by level ==")
    for level, count in sorted(Counter(r["level"] for r in kept).items()):
        print(f"  {count:4d}  {level}")

    if args.report:
        print("\n== candidates ==")
        current = None
        for row in kept:
            if row["level"] != current:
                current = row["level"]
                print(f"\n--- {current} ---")
            print(f"  {to_int(row.get('views')):>9,}  {to_int(row.get('duration_s')):>5}s  "
                  f"{(row.get('channel') or '')[:20]:<20} | {(row.get('title') or '')[:68]}")


if __name__ == "__main__":
    main()
