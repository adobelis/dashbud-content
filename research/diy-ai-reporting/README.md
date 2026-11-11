# What "I built it myself with AI" actually means

**Status:** Stub. One finding recorded, research not yet started.
**Created:** 2026-11-09

Working research project. **This is a working directory, not published output.** A cleaned summary goes to `wiki/dashbud/research/` when there is something worth sharing.

---

## The question

When a non-developer says *"I built it myself using GPT"* — what is the actual artifact, mechanically?

This is the competitive set, and it keeps showing up:

- A lost prospect chose "ChatGPT instead" and never opened the product
- A prospect at another account arrived with a GPT reconciliation workflow he had built and asked whether Dashbud could reproduce it. We did. He went quiet, then asked for something else
- An advisor story: a company handed out unlimited vibe-coding tokens, everyone built their own data apps, every app reported different numbers

Three instances of the same alternative, and we have characterized it loosely — "vibe code nobody can read" — without actually knowing what people build.

### The blind spot this exists to fix

Arthur is a Python/JS developer and a data person. Given GPT and a dataset he would produce something reasonable: version-controlled, re-runnable, inspectable. **That is not what the people choosing this alternative are producing**, and assuming otherwise means arguing against the wrong thing.

The research has to characterize what a non-developer actually ends up with, which means asking and watching rather than reasoning from one's own practice.

## What to map

### The spectrum of "building it with AI"

Each level has a different artifact, a different failure mode, and a different answer to "what happens when this person leaves."

- Paste numbers into a chat, read the answer
- Upload a spreadsheet, ask questions about it
- Hosted data-analysis features that run code on an uploaded file
- Custom GPTs or saved prompts with instructions
- API scripts, hand-written or AI-written
- Agent frameworks and automation tools
- Vibe-coded apps — Lovable, Replit, and similar

For each: **what is the artifact?** A chat thread. A downloaded spreadsheet. A script. A deployed app nobody owns. That answer determines whether the thing survives a month, a staff change, or an audit.

### Per approach

- Where does the data physically go, and what does the vendor say about it?
- What is re-runnable next month, and what has to be redone by hand?
- When it is wrong, how would anyone find out?
- Who can maintain it besides the person who made it?

### The frame to test it against

An advisor, relaying Tymofiy Mylovanov: AI lets you outsource **generation**, not **specification** or **validation** — which makes those two more valuable, not less.

Applied here: most DIY approaches outsource generation while leaving specification implicit and validation absent. Worth checking whether that holds across the spectrum, or whether some levels handle it better than the framing suggests.

## Method

### 1. Tutorial corpus — what people are actually taught

The primary source. "Build your own data dashboard with GPT!" tutorials are a better proxy for practice than asking people to describe their own process, because non-developers largely do what the tutorial says.

**The omissions are the finding.** A twelve-minute video that gets someone from spreadsheet to chart almost certainly never mentions:

- What happens next month when the data changes
- Whether anyone else can reproduce it
- What "revenue" means, and who decided
- How you would know if a number were wrong
- Where the data went, and whether that was allowed
- Who maintains it when the person who made it leaves

Catalogue what the tutorials promise, what steps they actually give, and what they skip. That gap, documented across a dozen videos, is a stronger argument than any assertion about vibe coding — it is what the market is being taught, in its own words.

Also worth noting: view counts and comment sentiment. A tutorial with 400k views is telling us about the size of this alternative. Comments saying "this broke when I tried it on my own data" are telling us about the failure rate.

**Tooling:** `scripts/research/fetch_youtube_transcript.py <url_or_id> [output_file]` (DataForSEO). Transcripts and notes go in `tutorials/`.

Search directions: build a dashboard with ChatGPT, GPT for data analysis, ChatGPT Excel reporting, AI business intelligence no code, automate reporting with AI, Lovable or Replit dashboard builds.

### 2. Hands-on trials

Use the tools the way a non-developer would — not the way a developer would — and record what happens in `trials/`. Each trial: what was attempted, what the tool said, what came out, what would break. Following a tutorial step-by-step on real-shaped data is the highest-value version of this.

### 3. Ask real people

What they used, what they ended up with, whether they still use it, whether anyone else can run it. Non-developers specifically.

Plain desk research is the weakest leg. Published material describes what the tools can do; the question is what people actually do with them.

## Findings so far

### GPT workspace Data feature pushes PHI handling onto the user (2026-11-09, first-hand)

Arthur tried the new GPT workspace Data feature. It responded, in substance, that **all PHI must be filtered out before anything is given to it.**

Worth confirming and recording precisely, because it matters in two directions:

1. **For healthcare prospects** this is the whole argument in one line. The alternative requires the customer to de-identify their data first — which is manual, error-prone, and exactly the work they were trying to avoid. Dashbud's architecture means the AI never sees row-level data at all, so the question does not arise.
2. **It is a concrete, checkable claim** rather than a positioning assertion. Worth capturing the exact wording, the date, and the context — vendor behaviour changes, and a dated screenshot ages better than a paraphrase.

To check: what the other major tools say about sensitive data, whether the stated limit is enforced or advisory, and what happens in practice.

---

## Layout

```
research/diy-ai-reporting/
  README.md              # this file — question, spectrum, method, findings
  tutorials/             # YouTube transcripts and tutorial analysis — what people are taught
  trials/                # hands-on attempts: what was tried, what the tool said, what broke
  notes/                 # working notes and observations
  interviews/            # conversation notes, especially non-developers
  draft/                 # content drafts
  scrapes/               # source material, same structure as the repo-wide scrapes/
    <published>-<domain>-<slug>.md
    _html/
    _batches/
```

Scrapes convention, fetching, and the `scrape_url.py` output-path caveat are the same as the other research projects — see `research/pe-data-and-ai/README.md`.

## Where this feeds

- The unfinished "why not just use ChatGPT" page — this is the evidence it has been missing
- The vibe-coding career argument queued for the blog
- The build-it-themselves qualification signal in the outbound targeting criteria
- Positioning generally: the honest version of "we are not that" requires knowing what that is

---

## Corpus build log — tutorial corpus

**2026-11-09.** Sampling frame built and screened. Not yet coded.

### Tooling added

All in `scripts/research/`, all caching raw responses to `scripts/research/output/`
so re-extraction costs nothing.

| Script | Does |
|---|---|
| `search_youtube.py` | YouTube search via DataForSEO → TSV manifest; also `--probe`, `--enrich`, `--comments` |
| `screen_frame.py` | rule-based screening of the frame → candidate shortlist, every exclusion reasoned |
| `enrich_youtube.py` | fills exact date, likes, comment count from `video_info`; `--top-per N --group-by level` bounds spend |
| `frame_stats.py` | date/view/channel distribution of a manifest |
| `youtube_video_dates.py` | `--inspect` a video's `video_info` fields; Zyte watch-page date fallback |
| `fetch_youtube_transcript.py` | pre-existing; transcript + metadata |

DataForSEO YouTube endpoints confirmed live on the account: `organic`,
`video_info`, `video_subtitles`, `video_comments`. Search takes `block_depth`,
**not** `depth`.

### The date gotcha — worth not rediscovering

**DataForSEO's YouTube search `timestamp` is derived from the page's relative
label** ("2 years ago"), so it is computed from the fetch date. In the first
frame nearly every row landed on `*-11-09`, the day it was fetched, and the
year was wrong by up to twelve months.

`video_info` returns the true date (`publication_date: Apr 4, 2023`,
`timestamp: 2023-04-05`). So **any date-framed claim requires the enrich pass**;
search-only dates are good for nothing finer than "recent vs. old". Rows carry
`date_source` so derived and real dates are never silently mixed.

### Funnel

- 18 queries, stratified by level (`tutorials/_queries.txt` — kept as the record
  of how the corpus was found; re-running it later measures drift in what the
  market is taught)
- → 375 result rows, 340 unique videos (`tutorials/_frame.tsv`)
- → 272 candidates after screening (`tutorials/_shortlist.tsv`)
- exclusions: 35 too-short, 14 too-long (courses, not tutorials),
  5 business-opportunity, 4 news/opinion, 4 off-topic, 3 shorts, 3 dev-course

Screening deliberately removes the **developer** path — Python/SQL bootcamps —
because the question is what *non-developers* produce. It also removes
"build & sell AI agents" business-opportunity content, which is a different
market entirely.

### Coding

`tutorials/_coding-scheme.md` and `tutorials/_template.md`. The governing rule
is that **date frames everything**: tutorials are coded by capability era, and
omissions are split into era-invariant (metric definition, error detection,
reproducibility, maintenance — equally answerable in 2023 and 2026) and
era-dependent (re-runnability, data permission — genuinely changed by tooling).

The strongest available finding would be era-invariant omissions staying flat
from 2023 to 2026: the tooling improved and the practice did not move.
