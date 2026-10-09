# Outreach CRM

Local CSV-based CRM for tracking Dashbud outreach. Google Sheets are the source of truth (see `outreach/README.md` for file IDs). CSVs here are backups and the working format for scripts.

## Tables

### prospects.csv
Active outreach targets. Seeded from todo_outreach.md, advance_local_outreach.md, personal_contacts.md, and nyu_law_evc_2026.md.

| Column | Type | Description |
|--------|------|-------------|
| prospect_id | PK | P001, P002, ... |
| first_name | text | |
| last_name | text | |
| company | text | |
| title | text | |
| email | text | |
| linkedin_url | text | Links to contacts.csv when contact originated there |
| source | enum | How they entered the CRM: advance_local, college, nyu_attendee_list, pe_network, linkedin_import, referral, inbound |
| era | tag | Networking era (see definitions below) |
| proximity | enum | Relationship proximity (see definitions below) |
| category | enum | prospect, advisor, connector |
| stage | enum | not_started, contacted, replied, meeting_scheduled, meeting_done, active_deal, closed |
| priority | int | 1 = highest |
| context | text | How Arthur knows them — the human story that makes outreach warm |
| notes | text | Outreach strategy and Dashbud-specific angles |

### interactions.csv
Log of every touchpoint with a prospect.

| Column | Type | Description |
|--------|------|-------------|
| interaction_id | PK | I001, I002, ... |
| prospect_id | FK | References prospects.prospect_id |
| date | date | YYYY-MM-DD |
| channel | enum | linkedin, email, phone, in_person, text |
| direction | enum | outbound, inbound |
| type | enum | initial_outreach, follow_up, reply, meeting, intro |
| summary | text | What happened |
| next_action | text | What to do next |
| next_action_date | date | When to do it |

### pipeline.csv
**The live deal pipeline.** This is the file in active use.

| Column | Type | Description |
|--------|------|-------------|
| deal_id | PK | D001, D002, ... |
| company | text | |
| stage | enum | See deal stages below |
| deal_type | text | subscription, subscription + deployment |
| arr | number/range | Annual recurring revenue. Ranges allowed for unsigned deals |
| one_time_revenue | number | Deployment or services revenue |
| primary_contact | text | |
| contact_role | text | |
| source | enum | referral, scott_client, scott_referral, inbound_or_referral |
| started | date | YYYY-MM-DD, when the deal opened |
| last_activity | date | YYYY-MM-DD, most recent meaningful touch |
| next_action | text | |
| next_action_date | date | |
| notes | text | Running history. Prefix status changes in CAPS with the date |

#### Deal stages

| Stage | Meaning |
|-------|---------|
| `exploratory` | Interest established, no formal proposal or evaluation yet |
| `demo_done` | Demo delivered, awaiting next step |
| `poc` | **We** do hands-on work with their real data to prove it works. Costly to us — Arthur builds reports/models directly. Not self-serve |
| `trial` | **They** have product access and are evaluating it themselves. The advertised free trial |
| `proposal` | Pricing and scope submitted |
| `security_review` | In procurement, security, or legal diligence |
| `closed_won` | Signed and paid |
| `closed_lost` | Declined, or went dark after a decision point |
| `dormant` | No activity and no decision. Revisit deliberately rather than letting it drift |

**POC vs. trial matters.** Hands-on POCs are deliberate at this stage: every one produces a reusable technical proof point whether or not the deal closes. Omega proved ingestion and modeling on a large IBM Informix ERP dataset (orders + warehouse). Trillium Creek proved the two ModMed EMA tables driving a derm practice's monthly reporting ingest easily — which de-risks every future ModMed prospect even though the deal was lost. Log these in the success-story portfolio regardless of outcome.

The risk to manage is not the POC itself but the **handoff**: if the prospect never gets into the app, they only ever see output, and output alone looks replaceable by ChatGPT. They never encounter the semantic model, governance, or shared definitions that make the comparison invalid. Aim to land the POC *inside* the product and hand over access, rather than delivering finished reports from outside it.

### deals.csv
**Unused — empty except for the header.** Superseded by `pipeline.csv`. Either populate it or delete it; do not treat it as live.

| Column | Type | Description |
|--------|------|-------------|
| deal_id | PK | D001, D002, ... |
| prospect_id | FK | References prospects.prospect_id |
| stage | enum | Legacy enum; use the `pipeline.csv` stages above instead |
| date_entered_stage | date | YYYY-MM-DD |
| notes | text | |

---

## Proximity tiers

How close Arthur is to someone. Determines outreach tone, message framing, and whether a warm intro is needed.

| Tier | Code | Description | Outreach tone |
|------|------|-------------|---------------|
| Inner circle | `inner_circle` | Actual friend. Would text them, sees them socially. | "Hey, I want to show you something I'm building" |
| Warm | `warm` | Real relationship with shared history, stayed in touch. Natural to catch up. | "It's been a while — here's what I've been up to" |
| Collegial 1 | `collegial_1` | Worked together substantially, mutual respect, ally-like relationship. Not personal but real rapport. | "Hey, thinking of you — I wanted to share something" |
| Collegial 2 | `collegial_2` | Same workplace, school, or organization. Know each other by name and role but didn't work closely together. | "We overlapped at X — I wanted to reach out about something I'm working on" |
| Networked | `networked` | Met at events, had a conversation, connected on LinkedIn with some context. | "We met at X / connected through Y — I wanted to share..." |
| Second order | `second_order` | Haven't met, but someone in Arthur's network knows them well, or Arthur has their info from an attendee list / shared community. | Needs a warm intro or a strong shared-affiliation hook |

## Networking eras

Mapped from Arthur's career timeline. When mining contacts.csv, era is inferred from LinkedIn connection date. Boundaries are approximate — someone from college may have connected years later.

| Era | Code | Years | Context |
|-----|------|-------|---------|
| College | `college` | pre-1997 | Undergraduate |
| PFM | `pfm` | 1997-2000 | Public Finance Management — deals and modeling |
| Empirix | `empirix` | 2000-2002 | Empirix, Cambridge MA |
| NYU Law | `nyu_law` | 2002-2005 | NYU School of Law, class of '05 |
| Cahill Gordon | `cahill_gordon` | 2005-2009 | Cahill Gordon & Reindel (biglaw) |
| Startup era | `startup_era` | 2009-2013 | Evivio and other startup activities. Heaviest networking period — 800+ LinkedIn connections. Some became lasting personal relationships, most didn't. |
| Advance Local | `advance_local` | 2014-2022 | Advance Local — deep working relationships with senior tech/data leaders |
| Gale | `gale` | 2022-2023 | Gale |
| NYC social | `nyc_friends` | 2005+ | Friends made through social life in NYC, not tied to a specific job or institution |
| Dashbud | `dashbud` | 2024+ | Dashbud / current era |

Note: `pe_network` and `nyu_attendee_list` are used as source values but aren't eras — PE contacts and NYU event attendees come from various eras.

---

## Relationship to contacts.csv
`contacts.csv` (parent directory) is the raw LinkedIn export — ~1,500 connections with light categorization. Prospects are mined from contacts using `scripts/contacts/mine_prospects.py`. The `linkedin_url` field is the natural join key between the two.

## Mining new prospects
```bash
# Era summary — see contacts by networking period
.venv/bin/python scripts/contacts/mine_prospects.py --era-summary

# Startup-era founders/C-suite not already in CRM
.venv/bin/python scripts/contacts/mine_prospects.py --era startup_era --seniority c_suite,founder --not-in-crm

# Search by keyword across company, position, notes, category
.venv/bin/python scripts/contacts/mine_prospects.py --keyword "data"

# Filter by seniority level
.venv/bin/python scripts/contacts/mine_prospects.py --seniority c_suite,vp,director

# Advance-era contacts with high Dashbud relevance
.venv/bin/python scripts/contacts/mine_prospects.py --era advance_local --relevance high

# Show only contacts not already in the CRM
.venv/bin/python scripts/contacts/mine_prospects.py --keyword "analytics" --not-in-crm
```
