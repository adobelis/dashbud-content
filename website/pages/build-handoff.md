# Website Pages Build Handoff

## What's being built
New pages and components to replace/augment the old How It Works, Product, Traditional Workflow, and Foundational Questions pages. The old pages are archived at `website/_archive/pages-july2026/`.

## The pages and components

### Who It's For (`/who-its-for`)
**Purpose:** The main pitch page. Answers "is this for me?" through use case scenarios and four situation segments the prospect recognizes.
**Spec:** `website/pages/who-its-for-build-spec.md`
**Content:** `website/pages/who-its-for.md`
**Images:** `website/pages/wif-images/` (four playful illustrations for segment cards)
**Structure:** Hero with "Self-service analytics that works" + 2x2 segment cards → "How teams use Dashbud" tabbed use cases (6 sectors) → four situation sections (bottlenecked → scattered → ad hoc → sensitive) → differentiators → CTA.

### Why Dashbud (`/why-dashbud`)
**Purpose:** The comparison and migration page. Shows trade-offs of current approaches and how to switch.
**Spec:** `website/pages/why-dashbud-build-spec.md`
**Content:** `website/pages/why-dashbud.md`
**Drilldown content:** `website/pages/ai-workflow-traps.md`
**Structure:** Trade-offs table → AI workflow drilldown accordion → "How Dashbud helps" vs. grid → "Switching is easy" migration paths → Trust & privacy → CTA.

### Data Sources Panel (homepage component)
**Purpose:** Show what Dashbud connects to — databases, cloud sources, and ERP/legacy systems.
**Spec:** `website/pages/data-sources-panel-spec.md`
**Placement:** Homepage, between feature pillars and trust section. Replaces unused `Logos.astro` component.
**Structure:** Logo grid (9 direct connections) + text block (ERP "works with" story).

### Carousel Update (homepage fix)
**Purpose:** Remove fictional company names from hero carousel mockups.
**Spec:** `website/pages/carousel-update-spec.md`

## How they relate to each other
- **Who It's For** is the main pitch — "is this for me?" organized by use cases and the prospect's situation.
- **Why Dashbud** is the deeper comparison — "how does Dashbud compare to what I'm doing now?" and "how hard is it to switch?" For prospects further along in evaluation.
- They're complementary but not sequential — either can be a landing page from search, ads, or the nav.

## How they relate to the homepage
- The **homepage** is the overview: hero, scroll-driven demo, feature pillars, trust, personas, CTA.
- **Who It's For** expands the homepage's personas section into a full page organized by situation and use cases. The homepage personas section could link here.
- **Why Dashbud** goes deeper on the comparison story — trade-offs table, AI workflow drilldown, "vs." cards, migration paths.
- The homepage **scroll-driven demo strip** and **feature pillars** already cover "how it works" — neither new page needs to repeat that.
- The **data sources panel** adds a visual connectivity story to the homepage that doesn't exist today.

## Navigation
Nav: **[Home] [Why Dashbud?] [Who It's For] [Pricing] [Blog] [Signup]**

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
