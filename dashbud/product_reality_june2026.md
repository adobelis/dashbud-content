# Dashbud Product Reality — June 2026

## Core Product
The product delivers on the original Connect → Blueprint → Ask → Share vision. 99% of the plan from 2025 is now built and working.

## Two Use Models
1. **Uploads with appends** — flat file uploads (CSV etc.), with ability to append new data over time
2. **Direct DB connection** — connect directly to databases

## Data Sources
### Live now
- File uploads (CSV, etc.)
- Direct database connections (proven with IBM Informix, likely PostgreSQL, MySQL, etc.)

### Coming soon
- Google Sheets connector
- Excel 365 connector
- (Cloud flat file ingestion)

### On roadmap
- Redshift, Snowflake, BigQuery (easily within reach)

### Back burner
- SaaS API connectors

## Key Product Capabilities
- **Semantic Models** (formerly "Blueprints"): Data Source + filtering + context for the AI
  - Tied 1-to-1 with a Workspace
  - Can clone, filter, and share Semantic Models
  - Enables "walled gardens" — e.g., sales teams can't see each other's numbers
- **Data Sources**: Can be shared resources across the org
- **Dashboards**: Can be shared to others
- All three layers (Data Sources, Semantic Models, Dashboards) work together with sharing/permissions

## Terminology Changes from 2025 Materials
- "Blueprint" / "Blueprint Conversation" → **Semantic Model (SM)**
- "Query Conversation" → **Data Explorer**
- New concept: **Workspace (WS)** — conceptually separate from SM, but in practice every WS has its own SM (which can be modified for that WS)

## Product Architecture (how things relate)
- **Data Source (DS)**: foundation — where cleaned data lives (uploads→Postgres or direct DB connection)
- **Workspace (WS)**: has a 1-to-1 Semantic Model; but a DS can feed many Workspaces (one-to-many)
- **Semantic Model (SM)**: data context + rules for the AI, tied to its Workspace
- **Data Explorer**: conversational interface where users query data and produce outputs (formerly "Query Conversation")
- **Dashboard**: composed of saved Data Explorer outputs; viewable, interactive, shareable

Flow: DS (import/clean) → WS/SM (model/contextualize) → Data Explorer (query/author) → Dashboard (compose/share)

## Data Explorer → Dashboard (detailed)

### Data Explorer (conversational query authoring)
- Conversational interface — user describes what they want, AI produces tables and charts
- Outputs: tables, charts (BAN format coming)
- **Smart chart formatting** — the AI understands:
  - What works in bar vs. line charts
  - When there are too many categorical x-values or too many series for a clean legend
  - Time series interpretation: months without years, time-of-day without dates, etc.
  - Max two y-axes per chart
  - All of this is encoded so the ECharts engine produces a good first pass automatically
- **Parametrized queries**: "Give me quarterly sales by product category for the NE region. Parametrize region." → produces interactive charts with controls to modify the parameter
- User can then modify output format:
  - Charts: stack bars, stack areas, pie instead of bar, bar vs. line, etc.
  - Tables: hide rows/cols, add sum row/col, diff row/col, etc. (very easy table format interface)

### Dashboard composition
- Save any Data Explorer output → it becomes an asset available for dashboards
- Compose dashboards from saved assets
- View, interact with (including parametrized controls), and share dashboards

## Data Ingestion (major differentiator)
- CSVs are pulled into a Postgres DB (not just stored as files)
- **Intelligent type casting**: text fields (including messy ones) are automatically cast to date and numeric fields
- Same casting logic used for appends — or alerts you when the cast doesn't work
- Data cleaning UX is genuinely best-in-class — "never worked with a system that has as nice an interface"
- **Full upload/append history**: all ingestions are tracked and can be rolled back
- This solves a real pain point — data cleaning is tedious and error-prone everywhere else

## Semantic Model Clone + Filter + Share
- SM/Workspace is where data modeling + context lives (1-to-1 relationship)
- Home office/IT does the data modeling once on a "base" workspace
- That workspace can be **filtered** (e.g., by region, team) and **shared** to different groups
- Recipients can **clone** their shared workspace to add domain-specific context without polluting the base model
- The AI query agent only sees the context relevant to each workspace — no unnecessary burden

### Omega Molding example (proven in pitch)
- Sales teams get filtered views of shared data — can't see each other's numbers
- Each team's workspace has only the context relevant to them

### PVM Bridge Analysis example (shows full flow)
1. **DS stage**: CEO imports order data, cleans it during ingestion (casts "$2,000.00" → numeric, string dates → dates)
2. **WS/SM stage**: Adds general context about how the order data works to the Semantic Model → shares this base workspace to sales and ops teams
3. **Clone**: For his PVM bridge analysis, he clones the workspace to add PVM-specific rules to that clone's SM
4. PVM rules don't matter for sales/ops — they live in a domain-specific workspace, not the shared one
- Key insight: clone lets you layer specialized analytical context on top of shared foundational data modeling
- Note: the data cleaning happened at DS import — everything downstream benefits from clean data

## Where It's Working
- Orgs with **large, traditional ERP and/or ERM systems**
- That have either **direct DB access** or **flat file downloads**
- Sweet spot: companies with established operational systems but weak/manual reporting

## Proof Points
- **POC: $50M/year framing supply company**
  - Modeled finances and warehouse operations
  - Data from IBM Informix ERP via exports
  - Created walled gardens for sales teams (Semantic Model clone + filter + share)
  - No formal case study yet

## What's Different from 2025 Messaging
- Product is real, not aspirational
- Two clear use models emerged (uploads vs. direct DB)
- Semantic Model sharing/cloning/filtering is a key differentiator (not fully articulated in 2025 materials)
- ERP/ERM + flat file export is the beachhead, not the multi-source SaaS integration story from 2025
- API connectors haven't landed yet — the "connect Google Analytics, Ads, Meta" scenario from the Sarah dental example isn't available today
