# Website Pages Build Handoff

## What's being built
New pages and components to replace/augment the old How It Works, Product, Traditional Workflow, and Foundational Questions pages. The old pages are archived at `website/_archive/pages-july2026/`.

## The pages and components

### Why Dashbud (`/why-dashbud`)
**Purpose:** The sales argument. Answers "why should I care?"
**Spec:** `website/pages/why-dashbud-build-spec.md`
**Content:** `website/pages/why-dashbud.md`
**Drilldown content:** `website/pages/ai-workflow-traps.md`

### Who It's For (`/who-its-for`)
**Purpose:** The identification page. Answers "is this for me?"
**Spec:** `website/pages/who-its-for-build-spec.md`
**Content:** `website/pages/who-its-for.md`
**Structure:** Four situation segments (bottlenecked → scattered → broken → sensitive), each with a who/where/how/what frame, concrete example, and specifics line. Plus a differentiators section and CTA.

### Data Sources Panel (homepage component)
**Purpose:** Show what Dashbud connects to — databases, cloud sources, and ERP/legacy systems.
**Spec:** `website/pages/data-sources-panel-spec.md`
**Placement:** Homepage, between feature pillars and trust section. Replaces unused `Logos.astro` component.
**Structure:** Logo grid (9 direct connections) + text block (ERP "works with" story).

### Carousel Update (homepage fix)
**Purpose:** Remove fictional company names from hero carousel mockups.
**Spec:** `website/pages/carousel-update-spec.md`

## How they relate to each other
- **Why Dashbud** is about the problem and the solution. It's persuasion.
- **Who It's For** is about the audience. The visitor recognizes their situation and sees a concrete example. It's identification.
- They're complementary but not sequential — either can be a landing page from search, ads, or the nav.
- They don't need to link to each other explicitly, though they can. The nav provides the connection.

## How they relate to the homepage
- The **homepage** is the overview: hero, scroll-driven demo, feature pillars, trust, personas, CTA.
- **Why Dashbud** goes deeper on the problem/solution story that the homepage only hints at. The homepage doesn't have the trade-offs table, the AI workflow drilldown, or the "vs." comparisons.
- **Who It's For** expands the homepage's 3-card personas section into a full page organized by situation. The homepage personas section could link here, or be kept as a brief summary.
- The homepage **scroll-driven demo strip** and **feature pillars** already cover "how it works" — neither new page needs to repeat that.
- The **data sources panel** adds a visual connectivity story to the homepage that doesn't exist today.

## Navigation
Current nav: [Home] [Why Dashbud?] [Pricing] [Blog] [Signup]

Proposed nav: [Home] [Why Dashbud?] [Who It's For] [Pricing] [Blog] [Signup]

## Design consistency
All pages and components should share these patterns:
- **Title/text grid** for comparison content (used in "vs." section and differentiators)
- **Cards** for categorized items (segments, personas, scenarios)
- **Teal accent color** (#007BA1) for section titles, links, highlights
- **CTASection component** from the homepage for closing CTAs
- **Light gray backgrounds** (#F3F4F6) for alternating sections
- **Two-column hero** with title/subtitle left and visual element right, gradient background

The homepage is visual-heavy (HSS mockups, scroll-driven animations). The new pages are **text-forward with strategic visual elements** (tables, cards, example blocks). They should feel clean and readable, not demo-y.

## Content management
The copy for pages lives in markdown files in the content repo (`content/website/pages/`). These are the source of truth. The Astro pages can either:
1. Read the markdown at build time (like the homepage reads YAML)
2. Hardcode the content initially and migrate to file-based later

The content is NOT in Sanity. If it moves to Sanity later, the push script (`scripts/sanity/push_content.py`) can be extended. See `website/CONTENT_MANAGEMENT.md` for the full content pipeline documentation.

## Files reference

```
content/website/pages/
├── who-its-for.md              ← page copy (NEW)
├── who-its-for-build-spec.md   ← build spec (NEW)
├── why-dashbud.md              ← page copy
├── why-dashbud-build-spec.md   ← build spec
├── ai-workflow-traps.md        ← accordion/drilldown content
├── data-sources-panel-spec.md  ← component spec (NEW)
├── carousel-update-spec.md     ← carousel fix spec (NEW)
├── use-cases.md                ← reference content (not a page for now)
├── use-cases-build-spec.md     ← reference spec (not a page for now)
├── how-it-works.md             ← product flow (separate, not on either page)
└── build-handoff.md            ← this file
```
