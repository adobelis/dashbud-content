# Content Management System — How It Works

## Source of Truth
Website content (hero, features, etc.) is managed as **local YAML files** in the `dashbud-content` repo, NOT edited directly in Sanity or hardcoded in Astro components.

**Content files:**
- `content/website/hero.yaml` — headline, subheadline, CTAs
- `content/website/features.yaml` — the 4 feature pillar sections (title, short description, long description, image alt)

**HSS (HTML Screenshot) configs:**
- `website/dashbud-home-astro-01/src/content/hss/*.yaml` — conversation mockup configs for the demo strip and hero image

## Push Pipeline
Content flows from local YAML → Sanity → Astro site:

```
Edit YAML files in content repo
    ↓
python3 scripts/sanity/push_content.py              → pushes to staging
python3 scripts/sanity/push_content.py --dataset production  → pushes to production
    ↓
Astro reads from Sanity at dev/build time
```

**The push script** (`content/scripts/sanity/push_content.py`) reads the YAML, converts markdown (including `**bold**` and bullet lists) to Sanity's Portable Text format, and patches the documents via the Sanity API.

## Sanity Setup
- **Project:** `89a9k63v`
- **Datasets:** `production` (live site) and `staging` (dev/preview)
- **Dataset switching:** The Astro site reads from `import.meta.env.PUBLIC_SANITY_DATASET || 'production'` in `src/utils/sanityClient.ts`
- **Local dev:** Set `PUBLIC_SANITY_DATASET=staging` in `.env.local` to read from staging
- **Vercel dev deployment:** Has `PUBLIC_SANITY_DATASET=staging` set as an env var

## Sanity Document IDs
- **Hero:** `b8feb522-f902-4fa6-bbc1-92724e3df508`
- **Homepage:** `f691ab1a-c9ff-40d0-bc80-0cd3a92c53ea`
- **Feature 1 (Connect):** `f511cdf6-cfb1-4906-a82d-e404844d808e`
- **Feature 2 (Model):** `353166e1-2171-4557-a9f1-2c5186e8e312`
- **Feature 3 (Explore):** `aada85c2-bedf-4f07-9e7c-55d004241700`
- **Feature 4 (Share):** `3e0abf06-4e77-4fdc-aae7-58db5b439c26`
- **Feature 5 (old, removed from homepage):** `11e6db09-82cb-4188-a008-4d43ea907672`
- **Privacy Policy:** `3c4bf370-559c-453a-b429-de0e5248bd50`

## What NOT To Do
- Don't hardcode feature/hero text in Astro components — it comes from Sanity
- Don't edit content directly in the Sanity Studio — edit the YAML files and push
- Don't use the production dataset for dev work — use staging

## HSS System
We built a system for rendering Dashbud product mockups as static HTML that looks like real screenshots:
- **`HSSConversation.astro`** — renders a Data Explorer conversation from YAML config, matching real app UI (colors, bubbles, tabs, avatars, sidebar)
- **`HSSDashboard.astro`** — renders a dashboard view mockup
- **`HSSCarousel.astro`** — hero carousel component
- **`HSSFileImport.astro`** — file import mockup
- **`HSSSemanticModelFull.astro`** — semantic model view mockup
- **`render_hss_chart.mjs`** — renders ECharts SVG charts from real conversation data in local Postgres
- **`generate_hss.py`** — pulls conversation text from local Postgres to generate YAML configs
- Charts output to `public/assets/hss/` as SVGs

## Chart Rendering
The chart renderer (`content/scripts/research/render_hss_chart.mjs`) connects to the local Dashbud Postgres database (via Docker), reads `content_struct` from conversation messages, and renders ECharts charts server-side as SVG files.

Usage:
```bash
node scripts/research/render_hss_chart.mjs <conv_id> --list                    # list chart messages
node scripts/research/render_hss_chart.mjs <conv_id> --message <idx> --output name.svg  # render one
```

Charts use the Dashbud app's color palette (MODERN_COLORS), gradients, and rounded corners.

## Key Token
`SANITY_WRITE_TOKEN` lives in `content/.env` (gitignored). Needed for push scripts.

## Scroll-Driven Demo Strip
The homepage has a scroll-captured product demo section that:
1. Pins the HSS browser frame when the section enters the viewport
2. Scrolls the internal conversation as the user scrolls the page
3. Rotates title/description text on the left column
4. Highlights the corresponding conversation element with a yellow glow
5. Transitions from Data Explorer → Save → Dashboard → Share modals
6. Unpins when all steps are complete

The JS for this is inline in `index.astro` using `position: fixed` toggling (not `position: sticky`, which breaks with `overflow-x-hidden` on the body).
