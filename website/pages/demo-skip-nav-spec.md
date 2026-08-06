# Demo Skip Navigation — Build Spec

## Problem
On mobile, the homepage demo strip requires a long scroll before the visitor reaches any business/descriptive content. Users who aren't ready for a product demo feel boxed in — they can't easily get to "why should I care?" or "is this for me?" content without scrolling through the entire demo.

This is less of an issue on desktop where the demo strip is shorter relative to viewport height, but still worth addressing.

## Solution
A lightweight navigation element that appears when the user scrolls past the hero and into the demo strip area. Provides links to the two main content pages as an alternative to the demo.

## Behavior

1. **Hidden by default** — not visible when the page loads or while the hero is in view
2. **Appears on scroll** — fades in when the user scrolls past the hero section (i.e., when the demo strip begins)
3. **Stays visible** — remains fixed while the user is in the demo strip area
4. **Hides on scroll-up** — tucks away if the user scrolls back up into the hero
5. **Hides after demo** — disappears once the user scrolls past the demo strip into the feature pillars (at that point they've committed to scrolling the page)

## Design

**Option A: Thin bar below the header**
A slim bar (height ~36-40px) that slides down from beneath the fixed header. Contains two links and a brief prompt.

```
┌──────────────────────────────────────────────┐
│  Header (logo, nav, CTAs)                    │
├──────────────────────────────────────────────┤
│  Skip the demo?  Why Dashbud? · Who It's For │  ← this bar
└──────────────────────────────────────────────┘
```

- Light background (white or `#f9fafb`) with subtle bottom border
- Text: small, gray prompt ("Skip the demo?") + teal links
- Smooth slide-down / slide-up animation (200-300ms)
- On mobile: same layout, text slightly smaller, links still tappable

**Option B: Pill/badge floating below header**
A floating rounded pill centered below the header, less bar-like, more tooltip-like.

```
         ┌─────────────────────────────────┐
         │ Why Dashbud? · Who It's For     │
         └─────────────────────────────────┘
```

- Rounded corners, subtle shadow
- Appears with a fade + slight upward slide
- Less formal than a full-width bar
- Could include a small "×" to dismiss

**Recommendation:** Option A on mobile (full-width is easier to tap), Option B on desktop (lighter footprint). Or just Option A everywhere for simplicity.

## Technical notes

- Trigger: use IntersectionObserver on the demo strip wrapper (the 600vh section), or check scroll position against the hero section's bottom edge
- The header is already `position: fixed` — this bar sits directly below it (`top: 80px` or whatever the header height is)
- Links: standard `<a>` tags to `/why-dashbud` and `/who-its-for`
- Z-index: same as or just below the header
- Should not interfere with the demo strip's scroll-driven animation
- Consider adding `aria-label="Skip to content pages"` for accessibility

## Do NOT change
- The demo strip itself — no shortening, no restructuring
- The header nav — these links supplement the header, not replace the nav items
- The scroll-driven animation behavior
