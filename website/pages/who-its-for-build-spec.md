# Who It's For — Page Build Spec

## Overview
New page showing prospects who Dashbud is built for, organized by their situation rather than by Dashbud's features. The prospect should recognize their company's problem in one of the sections and see a concrete example of how Dashbud solves it.

**URL:** `/who-its-for`
**Nav label:** "Who It's For"
**Content source:** `content/website/pages/who-its-for.md` (source of truth for all copy)

## Page Flow

```
1. Hero / opening hook
2. Companies running on legacy systems
3. Healthcare and regulated industries
4. Teams buried in spreadsheets
5. Businesses with data scattered across platforms
6. How Dashbud is different (4 differentiators)
7. CTA
```

---

## Section 1: Hero / Opening Hook

**Layout:** Centered text, similar to the Why Dashbud page hero. No image.

**Content:**
- Headline: "Who It's For"
- Subheadline hook: "You have the data. You just can't get at it."
- Two short paragraphs establishing the problem landscape (ERP, spreadsheets, SaaS, AI tools)
- Closing line: "Dashbud is built for companies in exactly this position."

**Design notes:**
- Same hero treatment as Why Dashbud for visual consistency across the two pages
- The subheadline hook should be larger/bolder than the paragraphs — it's the core message
- Consider using the gradient text treatment on "get at it" if it fits

---

## Sections 2–5: Four Situation Segments

Each segment follows the same structure: headline → 2–3 paragraphs describing the prospect's situation and how Dashbud addresses it → a bolded example block.

**Layout:** Full-width sections, alternating white and light gray backgrounds. Each section:
- Teal headline (h2)
- Body text at comfortable reading width (max-w-3xl or similar)
- Example block at the bottom: slightly inset, with a subtle left border or background tint to distinguish it from the body copy

| # | Headline | Key message | Example |
|---|----------|-------------|---------|
| 2 | Companies running on legacy systems | Dashbud connects to the databases behind ERPs (SQL Server, Oracle) or imports your existing CSV exports. Semantic model translates cryptic schemas. | $50M manufacturer, 20-year ERP, daily CSV exports, dashboards for finance/sales/ops |
| 3 | Healthcare and regulated industries | AI never sees data values — schema only. Connects to Epic Clarity/Caboodle. | Healthcare practice, thousands of encounters, operational reporting without PHI exposure |
| 4 | Teams buried in spreadsheets | Replace the spreadsheet pipeline. Define business rules once, no more dueling reports. | Services firm, 3 platforms, monthly report: 2 days → 20 minutes |
| 5 | Businesses with data scattered across platforms | Bring multiple sources under one semantic model. Query across them as one system. | E-commerce, 9 tables, analyst sets up in 30 minutes, team self-serves |

**Design notes:**
- Each section should feel like a self-contained story — a prospect could land directly on their section via anchor link and get the full pitch
- The example blocks should stand out visually but not overwhelm. Consider:
  - Light teal-tinted background (`#E0F4F9` or similar) with a left border in teal
  - Bold "Example:" label
  - Or a subtle card treatment
- The sections are intentionally ordered: legacy systems first (PE portfolio companies, our strongest differentiator), healthcare second (regulated = privacy story), spreadsheets third (broadest audience), scattered platforms fourth (most data-mature audience)
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
