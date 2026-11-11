# Community health and safety-net providers — data and reporting

**Status:** Stub. Research not yet started.
**Created:** 2026-11-09
**Ticket:** sector data analysis and AI usage trends research

Working research project. **This is a working directory, not published output.** A cleaned summary goes to `wiki/dashbud/research/` when there is something worth sharing; raw material, notes, and interim drafts stay here.

---

## The segment

**Community health and safety-net providers:** FQHCs, community health centers, and the value-based care organizations serving Medicaid and underserved populations.

Why it holds together as a segment rather than just "healthcare":

- **Multi-site by nature** — clinics, not a single location. That is the "cannot understand operations by being in the room" pattern from the ICP work.
- **Reporting with money attached.** Federal data reporting obligations and value-based contract quality measures mean the data work is compulsory and deadline-driven, not discretionary analytics.
- **No data teams, thin margins.** Grant- and reimbursement-funded.
- **EMRs built for clinical workflow, not operational reporting.**
- **Privacy is non-negotiable** — which is where "the AI never sees your raw data" lands hardest.

### The thing worth testing

On *need*, this may be a stronger fit than the manufacturing/distribution segment chosen for round-1 outbound, because the reporting is obligatory. On *ability to buy*, it is likely harder — boards, grant cycles, compliance review, little discretionary budget.

If need is high and purchasing capacity is low, that is worth knowing early rather than after building a target list.

## First pass: Zocalo Health as the worked example

Start with **Zocalo Health** specifically, before generalizing.

They may not be typical of the segment — venture-backed, virtual-first, Latino-focused primary care, rather than a bricks-and-mortar FQHC. That is an acceptable tradeoff for a first pass: a concrete example makes the abstract questions answerable, and there is a live relationship to learn from.

**Carry the caveat forward.** Anything learned from Zocalo should be marked as possibly atypical until checked against a more conventional community health organization. Specifically, a venture-backed virtual provider probably has engineers, which bears on the ICP disqualifier about organizations that can build their own.

### Zocalo questions

- What systems do they run — EMR, billing, scheduling, and what reports come out of them?
- Who does reporting today, and how much of it is manual?
- What has to be reported externally, to whom, on what cadence?
- Where does AI currently sit, if anywhere?
- Do they have engineering capacity that would make them build rather than buy?

## Segment questions, once there is a baseline

- What reporting is actually mandatory, to whom, and on what schedule? **Verify this rather than assuming** — the compulsory-reporting thesis rests on it.
- What do these organizations use today, and what does it cost them in staff time?
- Which EMRs dominate, and what is their reporting story? (The existing ERP/EMR connectivity research covers some of this.)
- How do they buy? Who signs, what approvals, what budget line, how long?
- Is there a grant or program funding angle that pays for data infrastructure?
- Where does AI sit — appetite, anxiety, or policy prohibition?

## Naming note

"FQHC" is a precise and filterable category. "Community health" is broader and fuzzier. Worth settling which one defines the segment before any target list gets built, because it changes both the size and the message.

---

## Layout

```
research/community-health/
  README.md              # this file — segment definition, questions, status
  notes/                 # working notes, observations, running thoughts
  interviews/            # conversation notes
  draft/                 # content drafts
  scrapes/               # source material, same structure as the repo-wide scrapes/
    <published>-<domain>-<slug>.md    # extracted text with provenance frontmatter
    _html/                            # raw HTML, same stem, kept for re-extraction
    _batches/                         # fetch manifests: lines of `URL [slug] [published]`
```

### Scrapes convention

Mirrors the repo-wide `scrapes/` exactly, so files move between them with a `mv`.

- **Filename** is `<published>-<domain>-<slug>.md` — the *content's* own date, not the fetch date. If no published date is available, the fetch date is used and `published:` left blank.
- **Frontmatter** carries provenance: `title`, `url`, `author`, `published`, `fetched`, `method`, `chars`.
- **`_html/`** keeps the original HTML under the same stem, so extraction can be redone without re-fetching.
- **`_batches/`** holds input manifests, one `URL [slug] [published]` per line, `#` comments allowed.

Treat `_html/` as untrusted: no scripts in it, pass paths as arguments.

Material worth reading beyond this project belongs in the repo-wide `scrapes/` instead.

### Fetching

`scripts/research/scrape_url.py` produces this structure (Zyte + BeautifulSoup):

```
.venv/bin/python scripts/research/scrape_url.py URL [--slug SLUG] [--published YYYY-MM-DD] [--browser]
.venv/bin/python scripts/research/scrape_url.py --batch FILE
```

**Note:** its output path is hardcoded to the repo-wide `scrapes/`. Targeting this directory needs an `--out` flag, or files moved after fetching.

Other scripts go in `scripts/research/`, with data output to `scripts/research/output/`.

## Related

- Existing EMR connectivity research covers Epic, Cerner, and athenahealth paths
- The privacy and security material written for a regulated provider is directly reusable here
