# Who It's For — Page Build Spec

## Overview
The main pitch page. Organized by the prospect's situation rather than by Dashbud's features. The prospect should recognize their company's problem in one of the sections and see a concrete example of how Dashbud solves it.

**URL:** `/who-its-for`
**Nav label:** "Who It's For"
**Content source:** `content/website/pages/who-its-for.md` (source of truth for all copy)

## Page Flow

```
1. Hero
2. How teams use Dashbud (tabbed use cases — 6 sectors)
3. Your answers are bottlenecked (Who)
4. Your sources are scattered (Where)
5. Your reporting is _ad hoc_ (How)
6. Your data is sensitive (What)
7. How Dashbud is different (4 differentiators)
8. CTA
```

---

## Section 1: Hero

**Layout:** Two-column flex (same pattern as Why Dashbud / How It Works hero). Title + subtitle on the left, segment menu on the right. Gradient background `bg-gradient-to-r from-white to-dashbud-teal`.

**Left side:**
- Headline: "Self-service analytics <br> **that works**"
- Body (bulleted):
  * Dashbud gives you access to data and reporting to support every member of your team.
  * Everyone gets the access they need, with an AI analyst that answers their questions in plain English.
  * **See how teams use Dashbud** across industries ↓ (link/scroll to Section 2)

**Right side — Segment menu:**
- Header above the 2x2 grid: **"Use Dashbud if..."**
- Four cards below, each with illustration + title + single one-liner. Lighter than before — cards are scannable, not readable.

| Image | Title | One-liner |
|-------|-------|-----------|
| `wif-images/clipping-locks.png` | Your data is locked up | One person knows the system. Everyone else waits. |
| `wif-images/playing-jacks.png` | Your sources are scattered | Multiple platforms, no single view across them. |
| `wif-images/herding-cats.png` | Your reporting is *ad hoc* | Everyone builds their own, nobody trusts anyone else's. |
| `wif-images/spying-eyes.png` | Your data is sensitive | Most AI tools want to see your raw data. |

**Design notes:**
- Cards should be visually substantial — these are the primary visual element of the hero, not a thin list
- Each card: illustration (small, ~60-80px) left or top, title + description right or below
- Use a 2x2 grid instead of a vertical stack to give the cards more visual weight
- Cards link to `#bottlenecked`, `#scattered`, `#broken`, `#sensitive` anchors
- Hover: subtle shadow or teal border accent
- The illustrations are playful/humorous — let them breathe, don't shrink them to icons

**Image files:** `content/website/pages/wif-images/` — copy to `src/assets/` or `public/` as appropriate for the Astro build.

---

## Section 2: How Teams Use Dashbud (tabbed use cases)

**Layout:** Section heading + intro text + 3-across card grid + expandable content panel.

- **Heading:** "How teams use Dashbud"
- **Intro:** "Dashbud works for teams across industries with different data sources and reporting needs. Here are some examples."
- **Cards:** 6 cards in a 3-across grid (desktop), 2-across or stacked on mobile. Each card shows the sector name (line 1) and the use case title (line 2). Clicking a card reveals the content panel below.
- First card active on page load.

**Tabs and content:**

| Tab label | Use case title | Content |
|-----------|---------------|---------|
| Professional services | Monthly executive report from 3 systems | 

Every month, your agency's operations lead pulls data from your project management tool, your time-tracking system, and your accounting platform to build an executive report. It takes a full day — downloading exports, matching client names across systems, fixing formula errors, and formatting charts. ¶ Dashbud connects to all three sources. Your operations lead defines the relationships: this client ID in your PM tool matches that account in your billing system. She teaches Dashbud what "utilization" means, how overhead is allocated, and which projects count as retainer vs. project-based. ¶ With Dashbud, your exec team gets a live dashboard with billable utilization, revenue by client, and project margin. The report updates every month automatically. Your operations lead spends that day on actual operations. |

| Manufacturing | Self-serve dashboards from your ERP | 

Your ERP has twenty years of sales history, purchase orders, and inventory data. But getting a report means asking the one person who knows the system — and she's busy running operations, not pulling numbers for the sales team. Everyone else either waits or tries to build something in Excel from a CSV export. ¶ Dashbud connects directly to the database behind your ERP. Your operations manager teaches Dashbud the business rules: what "on-time delivery" means, how to calculate cost per unit, which warehouse codes map to which product lines. She sets up filtered views so each team sees only their own data. ¶ With Dashbud, your sales team checks their pipeline dashboard every morning without asking anyone. Finance sees margins by product line. Warehouse ops tracks fulfillment rates. Your operations manager goes back to running operations. |

| E-commerce | Cross-platform customer profitability | 

Your order data lives in Shopify, your ad spend is in Meta and Google, and your returns and shipping costs are in your 3PL's system. Your marketing team knows revenue by channel. Your finance team knows cost of goods. But nobody can answer "which customers are actually profitable after returns, shipping, and acquisition cost?" ¶ Dashbud brings all three sources together under one semantic model. Your analyst defines the relationships — this Shopify order ID ties to that 3PL shipment, this customer's first-touch channel maps to that ad campaign. She defines what "profitable" means: revenue minus COGS, minus shipping, minus returns, minus attributed acquisition cost. ¶ With Dashbud, your team queries across the full picture. Marketing sees which channels bring profitable customers, not just cheap ones. Finance stops arguing with marketing about ROI. The quarterly review uses one set of numbers. |

| Healthcare | Operational analytics without exposing PHI | 

Your practice generates thousands of patient encounters a month. You need operational reporting — revenue by provider, visit volume trends, payer mix, charge analysis — but your EMR locks the data behind strict access controls. Your compliance officer won't let you hand patient data to an external AI tool, and she's right. ¶ Dashbud connects to your reporting database — Clarity, Caboodle, or a flat-file export from your EMR. The AI reads your schema and writes SQL queries, but never sees a single patient record, diagnosis code, or billing amount. Every calculation is auditable SQL you can review. ¶ With Dashbud, your practice administrator gets operational dashboards without a compliance headache. Revenue by specialty updates automatically. Visit trends surface scheduling problems before they hit the bottom line. Your compliance officer sleeps at night. |

| Financial services | Replace your team's Excel reporting pipeline | 

Every month, your head of marketing produces revenue breakdowns, channel performance, and campaign ROI in an executive report built in Excel. It takes his top analyst five hours to update. Your head of strategy produces her own similar report, which sometimes shows different results. Nobody knows whose numbers are right, and the quarterly board meeting starts with twenty minutes of reconciliation. ¶ Dashbud connects to your CRM, your accounting platform, and your marketing tools. Your analyst defines the business rules once — what counts as revenue, how to attribute a lead, which costs roll up into CAC. Those definitions live in the semantic model, not in someone's spreadsheet. ¶ With Dashbud, both teams query the same data with the same rules. Reports have an auditable query trail. Data is live or from shared imported sources, and reports update automatically. Your top analysts are freed to do real analysis, and everyone is singing from the same songbook. |

| PE portfolio companies | Get answers from legacy data exports | 

Your portfolio company is a roll-up of three acquisitions, each running a different system. Getting data out of any of them means scheduled CSV exports, manual downloads, or calling the one person who knows the admin password. Your operating partners need a consolidated view across all three, but standing up a data warehouse will destroy your margins. ¶ Dashbud imports those CSV exports automatically — set up a Google Drive folder, drop the files in, and Dashbud picks them up, cleans the data, and makes it queryable. Your operating team teaches Dashbud the business rules: what the columns mean, how to calculate the KPIs you care about, how to normalize across the three systems. ¶ With Dashbud, your operating partners get consolidated dashboards within days, not months. The approach templates across portfolio companies — same structure, different data. No system replacement, no data engineering hire, no disruption to the business. |

**Design notes:**
- Active tab: teal underline or highlight. Inactive tabs: gray text.
- Tab bar should scroll horizontally on mobile with no wrapping — all six tabs visible via swipe
- Content panel: white or very light background, comfortable reading width (max-w-3xl), subtle border or shadow to frame it
- Use case title appears as a subheading inside the content panel, below the sector name
- Each paragraph is a distinct block — scenario, implementation, result. The "Dashbud..." and "With Dashbud..." paragraph openers create a consistent rhythm
- No images in the content panel — keep it clean text
- No auto-rotate — let the visitor browse at their own pace
- Consider a subtle fade or slide transition between tabs

**Content source:** These use cases should also be added to `content/website/pages/who-its-for.md` as a new section.

---

## Sections 3–6: Four Situation Segments

Each segment follows the same structure: headline → 2–3 paragraphs describing the prospect's situation and how Dashbud addresses it → a bolded example block.

**Layout:** Full-width sections, alternating white and light gray backgrounds. Each section:
- Teal headline (h2)
- Body text at comfortable reading width (max-w-3xl or similar)
- Example block at the bottom: slightly inset, with a subtle left border or background tint to distinguish it from the body copy

| # | Headline | Image | Frame | Key message | Example | Specifics |
|---|----------|-------|-------|-------------|---------|-----------|
| 3 | Your answers are bottlenecked | `clipping-locks.png` | Who | One person can get at the data, everyone else waits. Dashbud connects to underlying DBs + semantic model translates cryptic schemas → self-serve. | ERP not built for reporting, daily CSV exports, dashboards per team, bottleneck person freed up | Legacy ERPs, production databases, locked-down systems, single-person dependencies |
| 4 | Your sources are scattered | `playing-jacks.png` | Where | Data spread across platforms, locations, formats. Semantic model joins them, query as one. | CRM + accounting + inventory, connect all three, query across the full picture | Multi-system, multi-location, mixed cloud/on-prem, databases alongside spreadsheets |
| 5 | Your reporting is ad hoc | `herding-cats.png` | How | DIY culture, dueling reports, tribal knowledge. Define rules once, everyone uses the same definitions. | Head of marketing and head of strategy produce conflicting reports, 5 hours/month, reconciliation at board meetings | Spreadsheet overload, ad hoc AI scripts, competence penalty, dueling reports |
| 6 | Your data is sensitive | `spying-eyes.png` | What | AI never sees raw values — schema only. Query runs against your data, results go to your screen. | Healthcare practice, operational reporting, PHI never exposed to AI | Healthcare/PHI, financial services, legal, HR/payroll, any regulated industry |

**Design notes:**
- Each section should feel like a self-contained story — a prospect could land directly on their section via anchor link and get the full pitch
- The example blocks should stand out visually but not overwhelm. Consider:
  - Light teal-tinted background (`#E0F4F9` or similar) with a left border in teal
  - Bold "Example:" label
  - Or a subtle card treatment
- Each segment can optionally display its illustration as a small visual accent (e.g., floated right or in the section header area). Images are in `content/website/pages/wif-images/`
- Each segment ends with a line of specifics in italics — these are the concrete instances (ERPs, healthcare, spreadsheets) that ground the abstract headline
- The sections are intentionally ordered from broadest/most relatable (bottlenecked) to most differentiated (sensitive data)
- Horizontal rule or generous spacing between sections

---

## Section 7: How Dashbud Is Different

**Layout:** 4 blocks — title left, description right (same grid pattern as "How Dashbud helps" on the Why Dashbud page). Or 2x2 cards on desktop, stacked on mobile.

| Title | Description |
|-------|-------------|
| AI that never sees your data | The AI reads your schema — field names, table structures, business rules — and writes SQL. It never sees a single data value. |
| Shared business rules, not tribal knowledge | Define "profit" once in the semantic model. Every query, every dashboard, every team uses the same definition. |
| Works with your data as it is | Messy CSVs, dates in three formats, dollar signs baked in. Smart data loading cleans and normalizes automatically. |
| Days to deploy, not months | Connect or upload. Model through conversation. Start asking questions. No data warehouse, no ETL, no six-month project. |

**Design notes:**
- Light gray or white background — differentiate from the last segment section
- Teal titles, dark gray descriptions
- This section is a bridge to the CTA — it should feel conclusive, not introductory
- Keep the same visual treatment as the "vs." sections on Why Dashbud for cross-page consistency

---

## Section 8: CTA

**Layout:** Standard full-width CTA bar (reuse the homepage/Why Dashbud CTA component).

**Content:**
- Headline: "See your company here?"
- Sub: "Connect your data and start getting answers."
- Primary: "Try Dashbud" → /signup
- Secondary: "Book a Demo" → bookDemo link

---

## Navigation

- Add "Who It's For" to the site header nav
- Nav should read: **Why Dashbud? | Who It's For | Pricing | Blog**
- URL: `/who-its-for`

## Relationship to other pages

- **Why Dashbud** (`/why-dashbud`) is the comparison/migration page: trade-offs table, vs. cards, switching paths, trust/privacy
- **This page** is the main pitch — "is this for me?" organized by the prospect's situation
- **Why Dashbud** is the deeper analytical page — "how does Dashbud compare to what I'm doing now?"
- **Homepage personas section** ("Built with your data needs in mind" — Operations & Finance, Data-Savvy Teams, Executives) overlaps with this page. Two options:
  1. Keep the homepage section as-is and add a "Learn more →" link to this page
  2. Simplify the homepage section to a single line + link: "See who Dashbud is built for →"
  - Recommend option 1 for now — the homepage personas are brief enough to not feel redundant

## Brand colors
- Teal: #007BA1
- Teal dark: #00546E
- Teal light: #E0F4F9
- Text: #111827
- Gray: #6B7280
- Light gray bg: #F3F4F6

## Content files reference

| File | What it contains | Used for |
|------|-----------------|----------|
| `content/website/pages/who-its-for.md` | Full page copy | All sections |
| `content/website/pages/why-dashbud.md` | Why Dashbud page (companion) | Cross-linking |
| `content/website/pages/why-dashbud-build-spec.md` | Why Dashbud build spec | Design consistency reference |
| `content/website/pages/data-sources-panel-spec.md` | Data sources component | May appear on this page in a compact form |
| `content/website/pages/use-cases.md` | Reference: business types, capabilities, personas | Background content, not directly used |
