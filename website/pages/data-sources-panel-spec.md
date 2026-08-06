# Data Sources Panel — Build Spec

## Overview
A visual component showing all data sources Dashbud connects to. Replaces the unused `Logos.astro` component (imported but not rendered on the homepage; contains stale v1 logos for platforms we don't actually connect to).

**Placement:** Homepage, between the feature pillars and the trust/privacy section. Also reference on the Why Dashbud page.

## Strategy

Dashbud has no unmanaged signup — every new user goes through a gated onboarding. This means we always know what data sources a customer needs before they touch the product. Connectors for ticketed databases (Oracle, Redshift, Snowflake, BigQuery) can be built on demand in <24 hours. We present all of these as direct connections with no caveats.

For ERP/legacy systems, many run on SQL Server or Oracle under the hood — which Dashbud already connects to. The semantic model is the differentiator: it maps cryptic ERP schemas to business terms so non-technical users can query them.

For everything else, Dashbud's file import (CSV, Excel, Google Drive auto-sync) works with any system that exports data — which is how most mid-market companies already operate.

## Panel Design

### Two-column layout (text left, visual right — matching site pattern)

```
┌──────────────────────────┬──────────────────────────┐
│ "Connect to your data"   │                          │
│                          │  [logo cluster —          │
│ Databases, warehouses,   │   11 logos, organic       │
│ cloud sources...         │   layout, no labels]      │
│                          │                          │
│ Business systems like    │                          │
│ Dynamics GP, SAP, Epic...│                          │
│ we connect directly or   │                          │
│ provide import workflows │                          │
│                          │                          │
│ Hundreds of other        │                          │
│ platforms via API,       │                          │
│ database, or file export │                          │
└──────────────────────────┴──────────────────────────┘
```

Stacks on mobile (text first, then logo cluster below).

**Left column: Text**

Headline: **"Connect to your data"**

Body — flowing text, not categorized lists. Covers both data platforms and business systems in a natural way. Something like:

> Dashbud connects directly to databases like PostgreSQL, SQL Server, and Oracle, and to cloud warehouses like Snowflake, BigQuery, and Redshift. Import spreadsheets, connect Google Sheets or Airtable, or upload CSV and Excel files.
>
> For business systems like Dynamics GP, SAP Business One, or Epic — Dashbud connects directly to the underlying database or provides automated import workflows. Plus hundreds of other platforms via API, database, or file export.

Design:
- Teal headline
- Body text in dark gray, comfortable reading width
- Mention a couple of top system names naturally in the text — don't list them all, don't use category headers (ERPs/EMRs/POS)
- Keep it brief and confident, not encyclopedic

**Right column: Logo cluster**

11 logos in a static organic cluster layout. No labels — the logos are recognizable on their own.

Logos:

| Logo | Tooltip | Notes |
|------|---------|-------|
| PostgreSQL | PostgreSQL | Have logo (square icon) |
| MySQL | MySQL | Have logo (need square icon version) |
| SQL Server | Microsoft SQL Server | Have logo (square) |
| Oracle | Oracle | Have logo (need square icon version) |
| Redshift | Amazon Redshift | Need logo |
| Snowflake | Snowflake | Need logo |
| BigQuery | Google BigQuery | Need logo |
| Google Sheets | Google Sheets | Have logo (need square icon version) |
| Airtable | Airtable | Have logo (need square icon version) |
| CSV | CSV file import | Have logo (square) |
| Excel | Excel file import | Have logo (need square icon version) |

Design:
- **Static cluster layout** — logos arranged organically, not a rigid grid. Slight variations in spacing and offset.
- Each logo: icon/glyph version (not wordmarks), roughly square, similar visual weight
- **No labels** — logos speak for themselves. Each logo has a `title` attribute for hover tooltip text (see table above).
- Bigger than current implementation — w-16 h-16 or larger so they read clearly
- **Cloud effect:** A soft, granular haze behind the entire logo group — not a smooth gradient but a dusty/grainy cloud texture. Use an SVG `feTurbulence` filter to generate procedural noise over a blurred teal/gray ellipse. This gives an organic, dusty feel with no image assets. Each individual logo gets a subtle halo/shadow (soft box-shadow or drop-shadow filter) so they feel like they're sitting slightly above the cloud surface.

  Implementation hint for the coding agent:
  ```html
  <svg width="0" height="0">
    <filter id="cloud-noise">
      <feTurbulence type="fractalNoise" baseFrequency="0.65" numOctaves="3" />
      <feColorMatrix type="saturate" values="0" />
      <feBlend in="SourceGraphic" mode="multiply" />
    </filter>
  </svg>
  <div style="filter: url(#cloud-noise); background: radial-gradient(ellipse, rgba(0,123,161,0.08), transparent 70%); ..." />
  ```
  Tune `baseFrequency` for grain size (higher = finer dust, lower = bigger clouds). Start at 0.65 and experiment. The cloud color should be very subtle — barely visible teal/gray, not a prominent shape.
- No hover effects or links — informational, not clickable

Logo format notes:
- **Need square/icon versions** for: Airtable (wide wordmark), MySQL (wide), Google Sheets (tall), Oracle (no viewBox), Excel (wide). Use icon/glyph forms.
- PostgreSQL elephant, SQL Server, CSV are already square.
- New logos needed: Redshift, Snowflake, BigQuery (square icon format).

## Content source

Create a new YAML file for this component:

**`src/content/data-sources.yaml`**

```yaml
headline: "Connect to your data"

body:
  - "Dashbud connects directly to databases like PostgreSQL, SQL Server, and Oracle, and to cloud warehouses like Snowflake, BigQuery, and Redshift. Import spreadsheets, connect Google Sheets or Airtable, or upload CSV and Excel files."
  - "For business systems like Dynamics GP, SAP Business One, or Epic — Dashbud connects directly to the underlying database or provides automated import workflows. Plus hundreds of other platforms via API, database, or file export."

logos:
  - postgresql
  - mysql
  - sql_server
  - oracle
  - redshift
  - snowflake
  - bigquery
  - google_sheets
  - airtable
  - csv
  - excel
```

## Logo files needed

New logos to source (SVG preferred, PNG fallback):

- `redshift.svg` — Amazon Redshift
- `snowflake.svg` — Snowflake
- `bigquery.svg` — Google BigQuery

Note: Airtable logo already exists (`Airtable_Logo.svg`) — keep it, do NOT remove.

Save to `src/assets/api-logos/`. All three are widely available as SVG.

## Logos to remove from `api-logos/`

These are v1 aspirational logos for platforms we don't connect to. Remove or move to an `_unused/` subdirectory:

- `Logo_Google_Analytics.svg.png`
- `Square,_Inc._logo.svg.png`
- `Stripe.svg`
- `WooCommerce.svg`
- `qb-logo-preferred-and-alternate-photo.svg` (QuickBooks)
- `shopify_glyph.svg`

## Component

Replace the existing `Logos.astro` with a new `DataSources.astro` component (or rename in place). The new component reads from `data-sources.yaml`.

## Placement on pages

### Homepage (`index.astro`)
- Insert after the feature pillars section, before the trust/privacy section
- Remove the unused `import Logos` line (or replace with the new component)

### Why Dashbud (`why-dashbud.astro`)
- Consider a compact version (logo grid only, no ERP text block) in the "Switching to Dashbud" section near "Your database / ERP → Connect directly"
- Or just a cross-link: "See all supported data sources →"

## Do NOT change
- The feature pillar "Connect Any Data Source" section — that's about the import workflow UX, not a logo panel
- The carousel data source examples — those are demo content, not a connectivity list
- Any existing page structure or animation

## Research reference
Full connectivity research: `wiki/dashbud/research/erp-connectivity/summary.md`
Product tickets: DS-354 (Oracle), DS-311 (Redshift), DS-309 (Snowflake), DS-310 (BigQuery), DS-407 (gated UI)
