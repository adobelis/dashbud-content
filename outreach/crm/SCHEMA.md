---
title: "CRM Data Shape and Rules"
visibility: private
---

# CRM data shape and rules

Plain markdown files in this repo. The shape is kept portable so these records could later be loaded into a database-backed tool without a rewrite.

**Design rule:** files are the source of truth. Any tool built on top indexes them rather than replacing them — so everything stays greppable, git-versioned, hand-editable, and writable by an agent without credentials.

**Core principle: append-only.** New facts are new files. Never rewrite history — if something changes, write a new event. Status is *derived* from the event stream, never hand-maintained. This is what kept Omega sitting "unpaid" in two documents for two months.

---

## Directory layout

```
outreach/crm/
  events/      # one file per interaction — append-only, never edited
  accounts/    # one file per company — stable facts only
  people/      # one file per person — stable facts only
  SCHEMA.md    # this file
  contacts.csv # KEEP: ~1,500 LinkedIn rows, genuinely tabular, used by mine_prospects.py
```

Entity docs (`accounts/`, `people/`) hold **stable facts**: what the company is, what systems they run, who someone is. Anything with a date goes in `events/`.

---

## Event files

**Filename:** `events/YYYY-MM-DD-<account-or-topic>-<short-slug>.md`
Chronologically sortable, unique, and readable in a directory listing.

```markdown
---
event_id: 2026-10-22-omega-scott-deconfliction
date: 2026-10-22
type: internal_note
account: omega-molding
people: [dan-peters]
direction: internal
summary: Identified channel conflict between Scott's custom-work pitch and adoption offer
stage_after: closed_won
next_action: Ask Scott to deconflict; offer free reporting setup to FCFO
next_action_date: 2026-10-24
tags: [channel-conflict, adoption-risk]
---

Narrative body. Full prose, as long as it needs to be. This is what the
CSV cell could not hold.
```

### Field reference

| Field | Required | Notes |
|---|---|---|
| `event_id` | yes | Matches filename without `.md`. Dynamo sort key component |
| `date` | yes | `YYYY-MM-DD`. When the event happened, not when it was written |
| `type` | yes | See enum below |
| `account` | no | Slug → `accounts/<slug>.md`. Omit for non-account events (e.g. marketing) |
| `people` | no | List of slugs → `people/<slug>.md` |
| `direction` | no | `inbound` \| `outbound` \| `internal` |
| `summary` | yes | One line. This is what a status UI renders in a list |
| `stage_after` | no | **Only when the event changes deal stage.** Latest wins on rollup |
| `next_action` | no | Latest non-empty wins on rollup |
| `next_action_date` | no | `YYYY-MM-DD` |
| `tags` | no | Free-form list. Cross-cutting themes |
| `metrics` | no | Nested map for numbers (see marketing example below) |

### `type` enum

`meeting` · `call` · `email` · `linkedin` · `text` · `event` · `demo` · `poc_work` · `payment` · `contract` · `internal_note` · `marketing_post` · `metrics_reading` · `stage_change`

### Deal stages (unchanged from the CSV era)

`exploratory` · `demo_done` · `poc` · `trial` · `proposal` · `security_review` · `closed_won` · `closed_lost` · `dormant`

---

## Entity docs

`accounts/` and `people/` hold **stable facts only** — who someone is, what a company runs. Anything with a date belongs in `events/`.

**Do not keep a `Status:` line in an entity doc.** Status is derived by the rollup. A hand-maintained status line is exactly the drift this structure exists to prevent.

### Account frontmatter

```yaml
---
account_id: omega-molding      # required, matches filename stem
name: Omega Molding            # required
type: customer                 # customer | prospect | closed_lost
deal_type: subscription
arr: 7200
industry: Building materials distribution
erp: IBM Informix
erp_tier: B                    # A | B | C per the reachability tiers
ownership: PE-backed
source: referral
icp_fit: high                  # high | medium | low
---
```

Other fields as useful (contract dates, seats, sites, headcount). Only `account_id` and `name` are required.

### Person frontmatter

```yaml
---
person_id: lauren-leonard-data-analytics   # required, matches filename stem
name: Lauren Leonard                        # required
role: Runs a data analytics practice
company:                                    # blank if independent
account:                                    # slug → accounts/, when they belong to one
linkedin: https://www.linkedin.com/in/...
relationship: friend                        # friend | colleague | networked | cold
category: prospect                          # prospect | advisor | connector | press | investor | friend -- blank if unsure, see Relationship rules
connected: 2011-01-18                       # LinkedIn connection date, if known
---
```

Body sections are freeform prose. The established pattern — history, what they care about, Dashbud angle, open questions, next — works well and should be kept.

---

## Relationship rules

These are the rules that get broken most often, usually by an agent writing a file. They were all learned by getting them wrong.

### Not everyone is a prospect

The default instinct — yours or an agent's — is to treat every new contact as pipeline. Resist it. **If the category is unclear, leave `category:` blank and ask.** A wrong guess of `prospect` quietly converts a relationship into a sales target, and the file then reads as though someone decided to work the account.

| Category | Means | Next actions? |
|---|---|---|
| `prospect` | Could buy Dashbud | Yes |
| `advisor` | Gives guidance on product, GTM, or market | Yes — ask them things |
| `connector` | Can make introductions, or could be a channel | Yes, carefully |
| `press` | Media, coverage angle | Yes, carefully |
| `investor` | Funding or market signal | Informational |
| `friend` | A personal relationship. Their job title is biography | **No** |

### `friend` means pull, not push

A personal relationship is the wrong channel into an organization's vendor process, and the friendship is worth more than the deal. So for anyone marked `friend`:

- **No next actions, no nurture, no sequence.**
- Note plainly in the file that they are not a prospect and why.
- If their organization looks like a fit on paper, say so *and* say that it is not a reason to act.

**The exception is when they raise it themselves.** That is pull, and responding is not a push. Two worked examples:

- [[michael-roberts-metlife]] — friend since 2010, CMO at a huge formal organization, has never expressed interest. **Do nothing.**
- [[patrick-mcgovern]] — friend of twenty years, CEO of a small organization, *said he would like to hear more*. **Respond, on his pace.** Answer what he asks, build no process around him, leave an easy exit.

### Don't create an account doc for a pull-based relationship

An `accounts/` file puts the organization on the status board as something to work. For a relationship that must stay pull-based, that is exactly wrong — the board will keep asking for a next action.

Create the account doc when it actually becomes an account, on their initiative.

### Entity docs hold no dates

Already stated above, worth repeating because it is the most common drift: **no `Status:` line, no dated "Interactions" list inside a person or account file.** Status and history are derived from `events/`. A hand-maintained status line goes stale and then misleads.

---
## Status rollup

Derived, never stored:

- **Current stage** — most recent event with `stage_after`
- **Open next action** — most recent event with `next_action`
- **Last activity** — `date` of most recent event
- **Interaction log** — all events for the account, sorted by date
- **Staleness** — today minus last activity

---

## DynamoDB mapping (for later)

Single-table design. Frontmatter fields become attributes verbatim.

| Access pattern | PK | SK |
|---|---|---|
| All events for an account, in order | `ACCOUNT#<account>` | `EVENT#<date>#<event_id>` |
| Account entity doc | `ACCOUNT#<account>` | `META` |
| Person entity doc | `PERSON#<slug>` | `META` |
| All events touching a person | `PERSON#<slug>` | `EVENT#<date>#<event_id>` (fan-out write) |
| Journal — everything by date | GSI1: `DATE#<YYYY-MM>` | `<date>#<event_id>` |

Body text becomes a `body` string attribute. Nothing else transforms.

**Known weak spot:** cross-account queries ("every account with no event in 60 days", "all events tagged `adoption-risk`") are scans in Dynamo. Fine at 10K documents; the place it would hurt if this grew. In the file world these are just `grep`.

---

## Migration status

- [x] Schema defined
- [x] Omega migrated from `pipeline.csv`
- [x] Remaining 5 deals migrated (6 accounts, 14 events)
- [x] Rollup script: `scripts/crm/rollup.py`
- [ ] `pipeline.csv` retire or freeze — superseded by the rollup; pending Arthur review
- [ ] `sales/activity-log.md` — decide whether it merges into `events/` or stays as a time record
- [ ] Decide whether these records stay file-based long term
