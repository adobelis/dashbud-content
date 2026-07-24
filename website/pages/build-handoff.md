# Website Pages Build Handoff

## What's being built
Two new pages to replace the old How It Works, Product, Traditional Workflow, and Foundational Questions pages. The old pages are archived at `website/_archive/pages-july2026/`.

## The pages

### Why Dashbud (`/why-dashbud`)
**Purpose:** The sales argument. Answers "why should I care?"
**Spec:** `website/pages/why-dashbud-build-spec.md`
**Content:** `website/pages/why-dashbud.md`
**Drilldown content:** `website/pages/ai-workflow-traps.md`

### Use Cases (`/use-cases`)
**Purpose:** The identification page. Answers "is this for me?"
**Spec:** `website/pages/use-cases-build-spec.md`
**Content:** `website/pages/use-cases.md`

## How they relate to each other
- **Why Dashbud** is about the problem and the solution. It's persuasion.
- **Use Cases** is about the audience and the capabilities. It's identification.
- They're complementary but not sequential — either can be a landing page from search, ads, or the nav.
- They don't need to link to each other explicitly, though they can. The nav provides the connection.

## How they relate to the homepage
- The **homepage** is the overview: hero, scroll-driven demo, feature pillars, trust, personas, CTA.
- **Why Dashbud** goes deeper on the problem/solution story that the homepage only hints at. The homepage doesn't have the trade-offs table, the AI workflow drilldown, or the "vs." comparisons.
- **Use Cases** expands the homepage's 3-card personas section into a full page with business types, capabilities, team roles, and example scenarios. The homepage personas section could be simplified to just link here, or kept as a summary.
- The homepage **scroll-driven demo strip** and **feature pillars** already cover "how it works" — neither new page needs to repeat that. Why Dashbud originally had a "how it works" section that was removed for this reason.

## Navigation
Current nav: [Home] [Product] [How It Works] [Pricing] [Blog] [Signup]

Proposed nav: [Home] [Why Dashbud] [Use Cases] [Pricing] [Blog] [Signup]

- "Product" is removed (redundant with homepage features)
- "How It Works" is replaced by "Why Dashbud"
- "Use Cases" is new

## Design consistency
Both pages should share these patterns:
- **Title/text grid** for comparison content (used in "vs." section and "What Dashbud enables")
- **Cards** for categorized items (business types, personas, scenarios)
- **Teal accent color** (#007BA1) for section titles, links, highlights
- **CTASection component** from the homepage for the closing CTA
- **Light gray backgrounds** (#F3F4F6) for alternating sections

The homepage is visual-heavy (HSS mockups, scroll-driven animations). These pages are **text-forward with strategic visual elements** (the trade-offs table, the accordion, cards). They should feel clean and readable, not demo-y.

## Content management
The copy for both pages lives in markdown files in the content repo (`content/website/pages/`). These are the source of truth. For now, the Astro pages can either:
1. Read the markdown at build time (like the homepage reads YAML)
2. Hardcode the content initially and migrate to file-based later

The content is NOT in Sanity. If it moves to Sanity later, the push script (`scripts/sanity/push_content.py`) can be extended. See `website/CONTENT_MANAGEMENT.md` for the full content pipeline documentation.

## Files reference

```
content/website/pages/
├── why-dashbud.md              ← page copy
├── why-dashbud-build-spec.md   ← build spec
├── ai-workflow-traps.md        ← accordion/drilldown content
├── use-cases.md                ← page copy
├── use-cases-build-spec.md     ← build spec
├── how-it-works.md             ← product flow (separate, not on either page for now)
└── build-handoff.md            ← this file

content/website/_archive/pages-july2026/
├── how-it-works.astro          ← old page (archived)
├── how-it-works.yaml           ← old content (archived)
├── product.astro               ← old page (archived)
├── foundational-questions.astro← old page (archived)
└── traditional-workflow.astro  ← old page (archived)
```
