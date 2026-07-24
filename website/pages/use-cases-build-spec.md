# Use Cases — Page Build Spec

## Overview
New page showing who Dashbud is for, what it enables, and how different roles use it. This is the "see yourself in the product" page — prospects should recognize their business type, their analyses, and their role.

**URL:** `/use-cases`
**Content source:** `content/website/pages/use-cases.md` (source of truth for all copy)

## Page Flow

```
1. Who is Dashbud for? (business types)
2. What Dashbud enables (capabilities)
3. How teams use Dashbud (personas)
4. Examples (scenarios)
5. CTA
```

---

## Section 1: Who is Dashbud for?

**Layout:** 4 cards in a row (2x2 on tablet, stacked on mobile).

**Content:** 4 business types, each with a bold title, subtitle (industry examples), and one line listing specific analyses.

| Card | Title | Subtitle | Analyses |
|---|---|---|---|
| 1 | Product-based businesses | retail, e-commerce, manufacturing, distribution | Sales trends by channel, inventory tracking, customer purchasing behavior, sales rep performance |
| 2 | Service-based businesses | agencies, consultancies, professional services | Profitability by client, utilization, marketing ROI, monthly stakeholder reports |
| 3 | SaaS and subscription businesses | software, media, membership | Churn analysis, cohort metrics, revenue recognition, usage patterns |
| 4 | Healthcare and regulated industries | medical practices, financial services, legal | Operational reports from EMR data without exposing sensitive data to AI platforms |

**Design notes:**
- Each card: white background, subtle border/shadow, teal title, gray subtitle, normal-weight analysis text
- The analysis line is the key — it's what makes the prospect say "that's me"
- Cards should be equal height
- Consider a subtle icon per card but not required — the text does the work
- No header needed beyond "Who is Dashbud for?" — keep it clean

---

## Section 2: What Dashbud enables

**Layout:** 4 rows, title left / description right (same grid pattern as the "vs." section on the Why Dashbud page). OR 4 cards. Either works.

**Content:** 4 capability blocks from the "What Dashbud enables" section.

| Title | Description |
|---|---|
| Calculated KPIs across data sources | Sales velocity, margin analysis, utilization rates, rep performance — not just raw numbers, but real calculations grounded in your data. |
| Shared business rules | "Profit" means different things to different people. Teach Dashbud your conventions once, share them across your organization. Everyone works from the same definitions. |
| Clean data from messy sources | Legacy ERPs, complex exports, dirty spreadsheets. Dashbud imports and cleans automatically. Lightning-fast queries on millions of rows. |
| Privacy-safe analysis | Your data stays yours. The AI never sees raw values. Sensitive data — medical, financial, legal — stays in your database or in secure managed storage. |

**Design notes:**
- Light background to differentiate from section 1
- Teal titles, gray descriptions
- These are differentiators that cut across business types — the layout should feel authoritative, not listy
- If using the title/text grid, keep the same proportions as the Why Dashbud "vs." section (~30% title, ~70% description) for visual consistency across pages

---

## Section 3: How Teams Use Dashbud

**Layout:** 4 cards or a 2x2 grid. Each card represents a persona.

**Content:** 4 personas from the "How teams use Dashbud" section.

| Persona | Description |
|---|---|
| The analyst | Connects data sources, builds semantic models, runs complex queries across multiple tables. Spends time on insight, not on data plumbing. Shares workspaces with the team so they can self-serve. |
| The ops leader | Checks the dashboard every morning. Filters by region, by team, by time period. Gets the numbers without asking anyone. Spots the problem before the meeting, not during it. |
| The executive | Sees the dashboards that matter. Doesn't touch a query. Trusts the numbers because they come from the same governed data model the whole organization uses. |
| The data-savvy non-technical user | Knows the business inside and out. Asks questions in plain English: "What were our top accounts last quarter?" Gets a real answer with a real chart. Saves it, shares it, moves on. |

**Design notes:**
- White cards on light gray background
- Bold persona title (teal or dark), description in gray
- The tone shifts here from "what" to "who" — these should feel human, not feature-y
- The inline quote in the last persona ("What were our top accounts last quarter?") should be styled distinctly — italic or a subtle callout
- Consider small avatar-style icons per persona (gear for analyst, chart for ops, briefcase for exec, chat bubble for non-technical) but keep them simple

---

## Section 4: Examples

**Layout:** 4 scenario cards, stacked vertically (full-width). Each is a mini case study.

**Content:** 4 examples from the "Examples" section.

| Example | Key details |
|---|---|
| A mid-market manufacturer | 20-year-old ERP, daily CSV exports, Google Drive, auto-append, filtered dashboards per team |
| An e-commerce company | 9 tables, gift sets, margin calculation, analyst loaded it, team self-serves in 30 min |
| A healthcare practice | EMR data, thousands of encounters, operational reports, schema-only = no patient data exposure |
| A service firm | 3 platforms, billable hours, client profitability, no data warehouse, monthly report: 2 days → 20 min |

**Design notes:**
- Each scenario: bold title, followed by a narrative paragraph (not bullets)
- These read like short stories, not feature lists — the layout should support reading, not scanning
- Consider a subtle left border or accent color per card
- Alternating white/light gray backgrounds
- These are not named customers (yet) — the phrasing ("A mid-market manufacturer") is intentionally generic. When we have real case studies, these become named and linked.
- The quantified outcomes ("30 minutes," "2 days → 20 minutes") should stand out — consider bolding them

---

## Section 5: CTA

**Layout:** Standard full-width CTA bar (reuse the homepage CTASection component).

**Content:**
- Headline: "See yourself in these use cases?"
- Sub: "Try Dashbud with your own data."
- Primary: "Try Dashbud free"
- Secondary: "Book a demo"

---

## Technical Notes

- **Content loading:** Read from `content/website/pages/use-cases.md` or hardcode initially.
- **Navigation:** Add "Use Cases" to the site header nav, after "Why Dashbud" and before "Pricing."
- **Relationship to homepage:** The homepage has a "personas" section (Operations & Finance, Data-Savvy Teams, Executives). This page expands on that. The homepage personas could link to this page, or the homepage section could be simplified to just link here.
- **Relationship to Why Dashbud:** "Why Dashbud" answers "why should I care?" This page answers "is this for me?" They're complementary but not sequential — either can be a landing page.
- **Brand colors:**
  - Teal: #007BA1
  - Teal dark: #00546E
  - Teal light: #E0F4F9
  - Text: #111827
  - Gray: #6B7280
  - Light gray bg: #F3F4F6

## Content Files Reference

| File | What it contains | Used for |
|---|---|---|
| `content/website/pages/use-cases.md` | Full page copy | All sections |
| `content/website/pages/why-dashbud.md` | Why Dashbud page (companion page) | Cross-linking |
| `content/website/pages/why-dashbud-build-spec.md` | Build spec for Why Dashbud | Reference for design consistency |
