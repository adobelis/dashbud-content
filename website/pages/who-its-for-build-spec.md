# Who It's For — Page Build Spec

## Overview
New page showing prospects who Dashbud is built for, organized by their situation rather than by Dashbud's features. The prospect should recognize their company's problem in one of the sections and see a concrete example of how Dashbud solves it.

**URL:** `/who-its-for`
**Nav label:** "Who It's For"
**Content source:** `content/website/pages/who-its-for.md` (source of truth for all copy)

## Page Flow

```
1. Hero
2. Your answers are bottlenecked (Who)
3. Your sources are scattered (Where)
4. Your reporting is _ad hoc_ (How)
5. Your data is sensitive (What)
6. How Dashbud is different (4 differentiators)
7. CTA
```

---

## Section 1: Hero

**Layout:** Two-column flex (same pattern as Why Dashbud / How It Works hero). Title + subtitle on the left, segment menu on the right. Gradient background `bg-gradient-to-r from-white to-dashbud-teal`.

**Left side:**
- Headline: "Self-service analytics that works"
- Body: "Dashbud gives you access to data and reporting to support every member of your team. Everyone gets the access they need, with an AI analyst that answers their questions in plain English. Dashbud's targeted features overcome the many challenges teams face: from bottlenecked data sources to privacy and security concerns."

**Right side — Segment menu cards:**
Four cards, each linking to the corresponding anchor below. Each card has an illustration, title, and short description.

Image | Title 
Description 

`wif-images/clipping-locks.png` | Your answers are bottlenecked 
* One person or team knows each system. Everyone else waits for the export, the report, or the analysis. 
* Dashbud connects to or imports all your sources, giving everyone the access they need. 

`wif-images/playing-jacks.png` | Your sources are scattered 
* You have multiple critical platforms: CRM, accounting, inventory, POS — each has a piece of the picture. 
* Dashbud brings them together into a single environment so you can create reports from multiple sources. 

`wif-images/herding-cats.png` | Your reporting is _ad hoc_ 
* Everyone builds their own reports and analyses with their own assumptions. 
* Dashbud internalizes the business rules — every report uses the same definitions. 

`wif-images/spying-eyes.png` | Your data is sensitive 
* Most AI tools want access to your raw data. 
* Dashbud writes accurate, auditable queries and calculations based on your schema and provides governed access to data.

**Design notes:**
- Cards should be visually substantial — these are the primary visual element of the hero, not a thin list
- Each card: illustration (small, ~60-80px) left or top, title + description right or below
- Use a 2x2 grid instead of a vertical stack to give the cards more visual weight
- Cards link to `#bottlenecked`, `#scattered`, `#broken`, `#sensitive` anchors
- Hover: subtle shadow or teal border accent
- The illustrations are playful/humorous — let them breathe, don't shrink them to icons

**Image files:** `content/website/pages/wif-images/` — copy to `src/assets/` or `public/` as appropriate for the Astro build.

---

## Sections 2–5: Four Situation Segments

Each segment follows the same structure: headline → 2–3 paragraphs describing the prospect's situation and how Dashbud addresses it → a bolded example block.

**Layout:** Full-width sections, alternating white and light gray backgrounds. Each section:
- Teal headline (h2)
- Body text at comfortable reading width (max-w-3xl or similar)
- Example block at the bottom: slightly inset, with a subtle left border or background tint to distinguish it from the body copy

| # | Headline | Image | Frame | Key message | Example | Specifics |
|---|----------|-------|-------|-------------|---------|-----------|
| 2 | Your answers are bottlenecked | `clipping-locks.png` | Who | One person can get at the data, everyone else waits. Dashbud connects to underlying DBs + semantic model translates cryptic schemas → self-serve. | $80M/yr manufacturer, 20-year ERP, daily CSV exports, dashboards per team, bottleneck person freed up | Legacy ERPs, production databases, locked-down systems, single-person dependencies |
| 3 | Your sources are scattered | `playing-jacks.png` | Where | Data spread across platforms, locations, formats. Semantic model joins them, query as one. | E-commerce, 9 tables, analyst sets up in 30 min, team self-serves across full picture | Multi-system, multi-location, mixed cloud/on-prem, databases alongside spreadsheets |
| 4 | Your reporting is broken | `herding-cats.png` | How | DIY culture, dueling reports, tribal knowledge. Define rules once, everyone uses the same definitions. | Services firm, 3 platforms, monthly report: 2 days → 20 minutes, consistent numbers | Spreadsheet overload, ad hoc AI scripts, competence penalty, dueling reports |
| 5 | Your data is sensitive | `spying-eyes.png` | What | AI never sees raw values — schema only. Query runs against your data, results go to your screen. | Healthcare practice, thousands of encounters, operational reporting without PHI exposure | Healthcare/PHI, financial services, legal, HR/payroll, any regulated industry |

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

## Section 6: How Dashbud Is Different

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

## Section 7: CTA

**Layout:** Standard full-width CTA bar (reuse the homepage/Why Dashbud CTA component).

**Content:**
- Headline: "See your company here?"
- Sub: "Connect your data and start getting answers."
- Primary: "Try Dashbud" → /signup
- Secondary: "Book a Demo" → bookDemo link

---

## Navigation

- Add "Who It's For" to the site header nav
- Position: after "Why Dashbud?", before "Pricing"
- The nav should now read: **Why Dashbud? | Who It's For | Pricing | Blog**

## Relationship to other pages

- **Why Dashbud** answers "why should I care?" — this page answers "is this for me?" They're complementary. Either can be a landing page.
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
