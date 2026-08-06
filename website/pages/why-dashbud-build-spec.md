# Why Dashbud — Page Build Spec

## Overview
The comparison and migration page. Shows the trade-offs of current approaches (SaaS dashboards, BI tools, spreadsheets, AI workflows), how Dashbud compares to each, and how easy switching is. Text-forward with strategic visual elements, not as component-heavy as the homepage.

**URL:** `/why-dashbud`
**Nav label:** "Why Dashbud?"
**Content source:** `content/website/pages/why-dashbud.md` (source of truth for all copy)
**AI drilldown source:** `content/website/pages/ai-workflow-traps.md` (for the accordion content)

## Page Flow

```
1. The landscape (intro)
2. Trade-offs table (with AI drilldown accordions)
3. How Dashbud helps ("vs." grid)
4. Switching to Dashbud is easy (cards)
5. Trust/privacy
6. CTA
```

---

## Section 1: The Landscape

**Layout:** Centered text block, max-width ~800px. Clean typography.

**Content:** Short intro paragraph + bullet list of data sources. Ends with an italicized question.

**Design notes:**
- Subtle background (white or very light gray)
- No visual elements — just well-set text
- The italicized question should feel like a natural lead-in to the next section

---

## Section 2: Trade-offs Table

**Layout:** Full-width table, 3 columns (Approach | Positives | Negatives). 4 rows + header.

**Content:** From the "Every approach has trade-offs" section of why-dashbud.md.

**Design notes:**
- Real HTML table, not a grid of cards
- Alternating row backgrounds (white / light gray)
- Header row in Dashbud teal (#007BA1) with white text
- Approach column: bold name + parenthetical examples in lighter text
- Positives column: green-ish or neutral
- Negatives column: each point as a bullet
- **AI Workflows row is special:** the negatives column should have a "Learn more →" link or indicator that triggers the accordion below
- Table should be responsive — on mobile, consider a stacked card layout per row

### AI Workflow Drilldown (accordion)

**Layout:** 3 expandable accordion sections that appear below the table (or below the AI Workflows row). Collapsed by default.

**Content:** From ai-workflow-traps.md, split into three sections:
- **Question 1: what happens next?** (maintenance/competence penalty)
- **Question 2: flexibility, scope, and accuracy** (calculations/auditing/dueling reports)
- **Question 3: privacy and security** (data exposure/regulatory risk)

**Design notes:**
- Accordion headers should be clickable, showing Q1/Q2/Q3 titles
- Each expanded section has bullets + a bold closing statement (styled as a callout box or highlighted block)
- The bold closing lines are key — they should stand out visually (e.g., teal left border, light teal background)
- Don't use the full intro paragraph ("You can absolutely build a reporting workflow...") in each accordion — it's repeated 3x in the slide deck for context but should only appear once on the web page, above the accordions

---

## Section 3: How Dashbud Helps

**Layout:** Title/text grid — bold teal title on the left, bullet descriptions on the right. 4 rows. Similar to the slide deck layout.

**Content:** The "How Dashbud helps" section with 4 "vs." blocks.

**Design notes:**
- Full-width section with light background
- Left column (~30%): bold teal titles ("vs. SaaS dashboards", "vs. BI tools", etc.)
- Right column (~70%): bullet points in gray
- Visual separation between rows (subtle border or spacing)
- This section mirrors the trade-offs table — same categories, now showing solutions. The visual parallel should be clear.

---

## Section 4: Switching to Dashbud is Easy

**Layout:** 4 cards in a row (2x2 on mobile).

**Content:** The "Switching to Dashbud is easy" section — 4 "Your X →" blocks.

**Design notes:**
- Each card has a bold teal title ("Your spreadsheets →") and 2-3 lines of description
- Cards should have a subtle border or shadow, white background
- The arrow (→) in each title provides visual momentum
- Consider a subtle icon per card (spreadsheet, cloud, database, AI) but not required
- This section should feel lightweight and reassuring — "this isn't hard"

---

## Section 5: Trust / Privacy

**Layout:** Centered text block, max-width ~800px. 4 items, each with bold title + description.

**Content:** The "Designed for privacy, security, and trust" section.

**Design notes:**
- Each item: emoji or icon + bold title on one line, description text below
- Existing icons from the homepage (🔒 📐 📋 🚫) work fine
- Clean, simple — this is a closing reassurance, not a feature showcase
- Alternatively, reuse the homepage trust section component if it exists

---

## Section 6: CTA

**Layout:** Standard full-width CTA bar (reuse the homepage CTASection component).

**Content:**
- Headline: "Get started today" or "Ready to see your data in a new light?"
- Sub: "Connect your data and start building reports in minutes."
- Primary: "Try Dashbud free"
- Secondary: "Book a demo"

---

## Technical Notes

- **Content loading:** The page copy lives in `content/website/pages/why-dashbud.md`. The Astro page should read this file and render it, OR the content can be hardcoded in the Astro component initially and migrated to a content file later. Up to the implementer.
- **AI drilldown content:** Lives in `content/website/pages/ai-workflow-traps.md`. The accordion sections correspond to the three "Question" headings in that file.
- **Accordion component:** Astro doesn't have a built-in accordion. Options: (a) use a simple `<details>/<summary>` HTML element (works without JS), (b) build a lightweight toggle with Alpine.js or vanilla JS, (c) use the existing `animate-on-scroll` pattern. `<details>` is simplest and accessible.
- **Table responsiveness:** On mobile (<768px), consider converting the table to stacked cards — one card per approach with Positives/Negatives as labeled sections.
- **Navigation:** Add "Why Dashbud" to the site header nav. It should sit between the homepage link and Pricing.
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
| `content/website/pages/why-dashbud.md` | Full page copy | All sections |
| `content/website/pages/ai-workflow-traps.md` | AI drilldown standalone piece | Accordion content |
| `content/website/pages/use-cases.md` | Use cases page (separate build) | Not this page |
| `content/website/pages/how-it-works.md` | Product flow steps (may link from here later) | Not this page |



## Trade-off table mobile text:

SaaS Dashboards
QuickBooks, Google Analytics, etc.
+ Built in, no setup	
- Clunky interfaces, can't mix data sources

BI Tools
Power BI, Tableau
+ Powerful, enterprise-grade	
- Hard to learn, expensive, require a data team

Spreadsheets
Excel, Google Sheets
+ Flexible, existing expertise
- Fragile, hard to update/share, competence tax

AI Workflows
Claude, ChatGPT
+ Fast and surprisingly capable
- Calculations opaque, privacy/security concerns
- Doesn't scale, vibe-coding problem [link?]