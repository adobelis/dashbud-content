# Data Sources Panel — Build Spec

## Overview
A visual component showing all data sources Dashbud connects to. Replaces the unused `Logos.astro` component (imported but not rendered on the homepage; contains stale v1 logos for platforms we don't actually connect to).

**Placement:** Homepage, between the feature pillars and the trust/privacy section. Also reference on the Why Dashbud page.

## Strategy

Dashbud has no unmanaged signup — every new user goes through a gated onboarding. This means we always know what data sources a customer needs before they touch the product. Connectors for ticketed databases (Oracle, Redshift, Snowflake, BigQuery) can be built on demand in <24 hours. We present all of these as direct connections with no caveats.

For ERP/legacy systems, many run on SQL Server or Oracle under the hood — which Dashbud already connects to. The semantic model is the differentiator: it maps cryptic ERP schemas to business terms so non-technical users can query them.

For everything else, Dashbud's file import (CSV, Excel, Google Drive auto-sync) works with any system that exports data — which is how most mid-market companies already operate.

## Panel Design

### Two-part layout

**Part 1: Logo grid — "Connect directly"**

A clean grid of logos for databases and platforms Dashbud connects to. No tiers, no asterisks, no "coming soon." One flat grid.

Logos (in this order):

| Logo | Label | Notes |
|------|-------|-------|
| PostgreSQL | PostgreSQL | Have logo |
| MySQL | MySQL | Have logo |
| SQL Server | Microsoft SQL Server | Have logo |
| Oracle | Oracle | Have logo |
| Redshift | Amazon Redshift | Need logo |
| Snowflake | Snowflake | Need logo |
| BigQuery | Google BigQuery | Need logo |
| Google Sheets | Google Sheets | Have logo |
| Airtable | Airtable | Have logo |

Design:
- Grid: 4 columns on desktop, 3 on tablet, 2 on mobile
- Each cell: logo centered, label below in small gray text
- White background, subtle shadow or border per cell
- No hover effects or links — these are informational, not clickable
- All logos should be similar visual weight (use scale factors like the existing Logos.astro)

**Part 2: Text block — "Works with your business systems"**

Below the logo grid, a text section explaining the ERP/legacy story. This is the business content that makes Dashbud's positioning unique — competitors can show a logo grid too, but none of them can make this claim.

Headline: **"Works with your business systems"**

Body (two columns on desktop, stacked on mobile):

**Column 1: Direct connection via SQL Server or Oracle**
> If your ERP runs on SQL Server or Oracle — and many do — Dashbud connects directly to the underlying database. Our semantic model maps your system's schema to plain business language, so your team asks questions without knowing table names.
>
> Systems that work today: Microsoft Dynamics GP, Dynamics NAV, SAP Business One, Epicor Kinetic, Epicor Prophet 21, Infor SyteLine, Oracle E-Business Suite, JD Edwards, Epic Clarity, and more.

**Column 2: File import for everything else**
> For systems that don't expose a database — or when your team prefers their existing export workflows — Dashbud imports CSV and Excel files with automatic type detection, cleaning, and versioning. Set up auto-sync from Google Drive and your reports update themselves.
>
> No data warehouse required. No ETL pipeline. Just your data, however it comes out.

Design:
- Light gray background to differentiate from the logo grid
- Teal headline
- Body text in dark gray, comfortable reading width
- The ERP system names should be slightly emphasized (semibold or a subtle highlight) but not a bulleted list — keep it flowing
- No logos for individual ERP systems (we don't have permission to use SAP/Epicor/etc. logos, and listing them as text is more honest about the relationship)

### Section wrapper

Heading above the whole section: **"Connect to the data you already have"**
Subheading: **"Databases, spreadsheets, cloud platforms, or legacy business systems — Dashbud works with all of them."**

## Content source

Create a new YAML file for this component:

**`src/content/data-sources.yaml`**

```yaml
section_title: "Connect to the data you already have"
section_subtitle: "Databases, spreadsheets, cloud platforms, or legacy business systems — Dashbud works with all of them."

direct_connections:
  - name: PostgreSQL
    logo: postgresql
  - name: MySQL
    logo: mysql
  - name: Microsoft SQL Server
    logo: sql_server
  - name: Oracle
    logo: oracle
  - name: Amazon Redshift
    logo: redshift
  - name: Snowflake
    logo: snowflake
  - name: Google BigQuery
    logo: bigquery
  - name: Google Sheets
    logo: google_sheets
  - name: Airtable
    logo: airtable

erp_headline: "Works with your business systems"

erp_direct:
  headline: "Direct connection via SQL Server or Oracle"
  body: "If your ERP runs on SQL Server or Oracle — and many do — Dashbud connects directly to the underlying database. Our semantic model maps your system's schema to plain business language, so your team asks questions without knowing table names."
  systems:
    - Microsoft Dynamics GP
    - Microsoft Dynamics NAV
    - SAP Business One
    - Epicor Kinetic
    - Epicor Prophet 21
    - Infor SyteLine
    - Oracle E-Business Suite
    - JD Edwards
    - Epic Clarity

erp_import:
  headline: "File import for everything else"
  body: "For systems that don't expose a database — or when your team prefers their existing export workflows — Dashbud imports CSV and Excel files with automatic type detection, cleaning, and versioning. Set up auto-sync from Google Drive and your reports update themselves."
  tagline: "No data warehouse required. No ETL pipeline. Just your data, however it comes out."
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
