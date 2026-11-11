# Coding scheme — tutorial corpus

Every tutorial in this corpus gets coded against the same fields. Fixed fields
are the point: they make the roll-up countable, so the output is "14 of 19
tutorials never mention what happens when the data changes" rather than an
impression that they mostly don't.

Use `_template.md`. One file per tutorial, named
`<published>-<channel-slug>-<title-slug>.md`.

---

## Date frames everything

This is the governing rule of the whole corpus, not a caveat at the end.

A tutorial is a snapshot of what a product could do on the day it was recorded,
taught to an audience with that day's assumptions. ChatGPT could not accept a
file before mid-2023. Scheduled reports, connectors and agent modes are recent.
Vibe-coding tools did not exist for most of the period. So:

**Judge every tutorial against what was possible when it was published, not
against what is possible now.** A 2023 tutorial that pastes numbers into a chat
window was not being lazy; that was the available method.

### Capability eras

Assign one. Boundaries are approximate and exist to group, not to adjudicate.

| Era | Window | What was available |
|---|---|---|
| `E1-prefile` | before ~2023-07 | chat only; data arrives as pasted text |
| `E2-codeinterp` | ~2023-07 to ~2024-12 | file upload, sandboxed code execution |
| `E3-gpts-agents` | ~2025 | custom GPTs mature; n8n/Make mainstream; vibe-coding tools arrive |
| `E4-connectors` | 2026 | live connectors, scheduled reports, agent modes, MCP |

### Two classes of omission

Separating these is what keeps the analysis honest.

- **Era-invariant omissions** — questions that were equally answerable in 2023
  and 2026, because they are about organisational practice, not product
  capability: what the metric means, how you would know a number is wrong, who
  else can run this, what happens when the author leaves. **An omission here is
  a finding at any date.**

- **Era-dependent omissions** — things the tooling genuinely changed:
  re-runnability (hard in E1, scheduled natively in E4), data residency and
  permission (enterprise controls arrived late). **An omission here has to be
  read against its era** before it counts for anything.

If the era-invariant omissions turn out to be just as absent in 2026 as in 2023,
that is the strongest single finding this research can produce: the tooling got
better and the practice did not move.

### Dates also decay

A tutorial's instructions rot as the product's interface changes. Record
`still_accurate` — whether the steps shown would still work today. High view
counts on instructions that no longer execute is itself a cost of the DIY path,
and a thing comments reveal well.

---

## Metadata fields

All from `video_info` (`date_source: video_info`), never from search results —
search dates are derived from relative labels like "2 years ago" and are wrong
by up to a year.

| Field | Note |
|---|---|
| `published` | exact date. **Required.** Everything else is read through it |
| `era` | one of the four above |
| `channel` | plus whether it is a vendor channel, which changes the incentive |
| `views` | cumulative — so always report alongside age, never alone |
| `views_per_month` | crude age-normalisation; lets a new video be compared to an old one |
| `likes`, `comment_count` | engagement; comment count also predicts whether there is failure-report material to mine |
| `duration_s` | the time budget is the mechanical cause of most omissions |

## Content fields

| Field | What to record |
|---|---|
| `level` | position on the spectrum in `../README.md` |
| `promise` | the title's claim, **verbatim**. This is what the market is being sold |
| `tools` | every product actually used |
| `artifact` | what exists when the video ends: chat thread / downloaded file / saved config / script / deployed app / nothing |
| `data_path` | where the data physically goes, and whether the video says anything about it |
| `still_accurate` | would these steps work today — yes / no / partly / unknown |

## The six omission fields

Each coded `mentioned` / `not mentioned`, with a timestamp when mentioned.
Mark each as era-invariant (I) or era-dependent (D).

1. `om_data_changes` (D) — what happens next month when the data is different
2. `om_reproducible` (I) — whether anyone else could reproduce this
3. `om_definition` (I) — what the metric *means*, and who decided
4. `om_error_detection` (I) — how you would know if a number were wrong
5. `om_data_permission` (D) — where the data went, and whether that was allowed
6. `om_maintenance` (I) — who maintains this when the author leaves

### Scoring rule

**Read, do not grep.** Keyword search finds candidate windows; the score comes
from reading the surrounding transcript. "Save this so you can use it again"
is not an answer to re-runnability, and a grep for "reuse" would score it as
though it were. Auto-captions also mangle product names badly.

Credit a mention only if the tutorial *addresses* the question. Naming it and
moving on ("of course you'd want to validate this") is coded `gestured`, a
third value, because the gesture without the method is its own finding.

## Comment signal

Up to three verbatim comments reporting that the method broke, with like counts
and dates. A dated comment saying "this doesn't work any more" is the decay
evidence. Absence of such comments is also recordable.

## Counter-evidence

**Required field, and the corpus is weaker without it.** The thesis is that
these approaches outsource generation while leaving specification implicit and
validation absent. Some level will handle one of those better than predicted —
a custom GPT with written instructions is a real, if thin, specification
artifact; an n8n workflow is genuinely re-runnable.

Record every instance. An argument that concedes its best counter-example is
harder to dismiss than one that does not.
