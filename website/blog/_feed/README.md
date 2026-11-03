# Incoming content feed

Posts by other people, kept for inspiration, reference, and response. One file per piece. Underscore directory: never published.

**Filename:** `YYYY-MM-DD-<author-slug>-<short-slug>.md` (date = publication date)

**Frontmatter:**
```yaml
---
title:
author:
author_slug:        # matches outreach/crm/people/<slug>.md when the author is in the CRM
org:
url:
published: YYYY-MM-DD
added: YYYY-MM-DD
scrape:             # path under scrapes/ holding the full local text; fetch once, never again
series:             # which Dashbud series or post it informs, e.g. downstream-01
tags: []
---
```

**Body:** summary; relevance to our content (what it supports, what it argues against, what we'd respond to; "limited" is a valid rating); quotable lines verbatim with attribution; data points worth citing with their original source.

Rule: quote exactly or paraphrase clearly. Never present a paraphrase as a quote. Never read a light post as if it carried an argument it doesn't make.

## Local copies: `scrapes/`

Full text lives in `scrapes/` at the repo root so nothing is fetched twice.

- **Filename = content date, not fetch date:** `scrapes/<published>-<domain>-<slug>.md`. The access date is in frontmatter as `fetched:`. If no publication date can be found, the fetch date is used in the name and `published:` is left blank; fix it later with `scrape_rename.py --set FILE DATE`.
- `scripts/research/scrape_url.py URL --slug name [--published YYYY-MM-DD]` saves the markdown plus raw HTML under `scrapes/_html/`. Batch lists live in `scrapes/_batches/`, one `URL [slug] [published]` per line. Don't repeat the domain in the slug; the script adds it.
- `scripts/research/scrape_rename.py` renormalizes names to the published date and updates `scrape:` references in this folder and in the CRM. Dry run by default; `--apply` to execute.
- `scripts/research/fetch_youtube_transcript.py URL scrapes/<published>-youtube-<slug>.md` for video transcripts (DataForSEO). Name the file by the video's publish date and add a `**Fetched:**` line under `**Published:**`.
- Run everything from the repo root with the venv activated: `source .venv/bin/activate && python scripts/research/...`
- **LinkedIn posts can't be scraped** (Zyte returns 451). Capture the text by hand into `scrapes/<published>-linkedin-<slug>.md` with `method: manual` and the capture date in `fetched:`.
- Paywalled or bot-blocked pages (HBR, Brookings) save thin. Keep the stub so the attempt is recorded; add the text by hand if it's worth it.
