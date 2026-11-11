# Private equity — data analysis and AI usage

**Status:** Stub. Research not yet started.
**Created:** 2026-11-09
**Ticket:** sector data analysis and AI usage trends research

Working research project. PE-backed ownership transitions are one of the strongest patterns in the ICP, and there is no researched material tailored to that audience.

**This is a working directory, not published output.** When the research is done, a cleaned summary goes to `wiki/dashbud/research/`; raw material, notes, and interim drafts stay here.

---

## Working thesis (to test, not assume)

**The need is governed data with shared rules, and that is not an AI story.**

Portfolio companies get bought with numbers nobody can reconcile. The firm spends the first year arguing about what EBITDA means at each site, what counts as a unit, which revenue figure is the real one. That problem predates AI entirely and PE has always wanted it solved.

**What AI changed is the cost of not solving it.** Cheap generation means five people can produce five confident, well-formatted, contradictory answers in an afternoon. Ungoverned data moved from annoying to actively dangerous.

So the argument to a PE audience is not *adopt AI analytics*. It is *your existing problem just got more expensive*. That asks them to believe nothing new about AI — only to notice a change in stakes.

**Why this framing may be more sellable:** it does not depend on the audience being "ready for AI." They are already sold on governance. The research question is whether they see the connection.

## What to find out

- How firms approach data and reporting across a portfolio — what gets standardized, what is left to each company
- Where AI currently sits in portfolio operations and value creation plans
- What firms are publishing, and what the prevailing view is
- What portfolio company operators actually do, as distinct from firm-level intent
- Whether governance and shared definitions are treated as a priority, a solved problem, or an afterthought
- Whether anyone frames the problem the way the thesis above does

## Method

Desk research plus primary conversations. For this audience, conversations are the better source — published PE content on AI is abundant and mostly undifferentiated.

### Grounding available without new research

- **Our own pipeline.** A paying customer who does not log in. A prospect who chose ChatGPT and never opened the product. These are field observations, not theory.
- **The Lovable story** (via an advisor): a company handed out unlimited tokens, everyone built their own data apps, every app reported different numbers, the analytics lead went under. The single best illustration of the thesis.
- **Specification / generation / validation** (via an advisor, relaying Tymofiy Mylovanov): AI lets you outsource generation, not specification or validation — so those become *more* valuable. Theoretical spine for the argument, but borrowed, and worth attaching to observed cases rather than asserting.
- **ERP connectivity research** already contains a PE portfolio company pitch angle.

### Primary sources in the network

Several contacts sit close to this question — a PE talent executive, and PE contacts already flagged in outreach as needing a tailored pitch. Specific names are in the CRM, not here.

## A caution worth keeping

The honest version of this research might conclude something inconvenient: that most portfolio companies are not ready, that the bottleneck is organizational rather than tooling, or that firms have no institutional view at all. Any of those would be worth publishing, and credibility with this audience depends on being willing to.

## Layout

```
research/pe-data-and-ai/
  README.md              # this file — thesis, questions, method, status
  notes/                 # working notes, observations, running thoughts
  interviews/            # conversation notes
  draft/                 # POV piece drafts
  scrapes/               # source material, same structure as the repo-wide scrapes/
    <published>-<domain>-<slug>.md    # extracted text with provenance frontmatter
    _html/                            # raw HTML, same stem, kept for re-extraction
    _batches/                         # fetch manifests: lines of `URL [slug] [published]`
```

### Scrapes convention

Mirrors the repo-wide `scrapes/` exactly, so files can move between them with a `mv`.

- **Filename** is `<published>-<domain>-<slug>.md` — the *content's* own date, not the fetch date. If no published date can be found, the fetch date is used and `published:` is left blank.
- **Frontmatter** carries provenance: `title`, `url`, `author`, `published`, `fetched`, `method`, `chars`.
- **`_html/`** keeps the original HTML under the same stem. This is the original source material — kept so extraction can be redone without re-fetching.
- **`_batches/`** holds the input manifests, one `URL [slug] [published]` per line, `#` comments allowed.

Treat `_html/` as untrusted: no scripts in it, pass paths as arguments.

### Which scrapes directory to use

- **Here** — material gathered specifically for this project.
- **Repo-wide `scrapes/`** — anything worth reading beyond this project. A piece on AI in investing serves this research, the blog, and positioning at once.

One-off reads go shared; bulk material from one project stays local. The comparators research followed the same pattern with its own raw directories.

### Fetching

`scripts/research/scrape_url.py` produces this structure (Zyte + BeautifulSoup):

```
.venv/bin/python scripts/research/scrape_url.py URL [--slug SLUG] [--published YYYY-MM-DD] [--browser]
.venv/bin/python scripts/research/scrape_url.py --batch FILE
```

**Note:** its output path is currently hardcoded to the repo-wide `scrapes/`. To target this directory it needs an `--out` flag, or files have to be moved after fetching.

Other scripts go in `scripts/research/` per repo convention, with data output to `scripts/research/output/`.

## Output

- **Interim:** notes and findings in this directory
- **Published:** cleaned summary to `wiki/dashbud/research/` once there is something worth sharing
- **Content:** a POV piece for PE operating partners. Working direction — the cost of disagreement rather than the promise of AI.
