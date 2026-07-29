# Hero Carousel Update — Remove Company Names

## Problem
The carousel currently shows three different fictional company names (Ridgeline Gear, Primrose Home, and an ERP example) across the three slides. This is confusing — it's unclear whether the slides show one company's journey or three different companies. 

## Change
Remove all fictional company names from the carousel mockups. The slides should show the data source type and the Dashbud workflow, not a branded scenario. The audience should map it to their own situation.

## What to change

### Slide 1: Spreadsheets
- Remove "Ridgeline Gear" workspace name from the DE mockup header
- Replace with generic label or just "Data Explorer" / "Sales Data"
- The pipeline velocity table content can stay — it's generic enough without the company name

### Slide 2: Databases & Data Lakes  
- Remove "Primrose Home" from the workspace/header
- Replace with generic label or just the page context ("Schema View", "Semantic Model", etc.)

### Slide 3: Mission-Critical Platforms
- Remove any company name from the ERP/import mockups
- Keep the data generic — "purchase orders", "orders import", etc. are fine without a brand

### Carousel top-level titles
- Keep as-is: "Spreadsheets", "Databases & Data Lakes", "Mission-Critical Platforms"
- Keep the narrative descriptions as-is

### Workspace name convention
- Replace all company names in the carousel with a simple context label
- Use the pattern: **"[Function] / [View]"** — e.g. "Sales / Pipeline", "Sales / Semantic Model", "Operations / Import"
- This applies to the browser chrome header bar, sidebar workspace label, and any other place a company name appears
- Don't use "Your Company" or "Acme Corp" — keep it functional, not fictional
- Rep names (Anna L., Sarah T., etc.) and data values are fine as-is — they're generic enough without a company brand
- Rename `primrose_home_orders_2024.csv` (or similar branded filenames) to `orders_2024.csv`

## Files affected
- `src/components/HSSCarousel.astro` — the inline mockup content
- `src/content/hss/hero-carousel.yaml` — if workspace names are referenced there
- Any sub-components rendered inside the carousel (check for hardcoded workspace names)

## Do NOT change
- The carousel structure, animation, or layout
- The slide titles and narrative text
- The actual data content (tables, charts, column names) — just the company branding
