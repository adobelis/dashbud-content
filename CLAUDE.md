# Dashbud Content Repo

## What is Dashbud
Dashbud is an AI-powered business intelligence platform built for mid-market companies. Users connect data sources, define business rules in a semantic model, then explore data via natural language conversations and share results as dashboards. The core flow is: Connect (data sources) → Model (semantic model) → Explore (Data Explorer chat) → Share (dashboards).

Parent company: Evolytix. Team: Scott (CEO), Arthur (product/marketing/biz dev), Dylan and Nick (engineering).

## Current data source support
- **Direct database connections:** PostgreSQL, MySQL, SQL Server
- **Cloud sources:** Google Sheets
- **File import:** CSV upload, including auto-append from Google Drive
- Legacy/ERP systems currently handled via export-to-CSV (e.g., Omega Molding exports from IBM Informix to Google Drive)

## This repo
Marketing content, website copy, sales materials, scripts, outreach, and wiki for Dashbud's 2026 marketing relaunch.

### Directory structure
- `website/` — website copy source of truth (hero, features, pages, blog)
  - `hero.yaml`, `features/*.md` — pushed to Sanity CMS via scripts
  - `pages/` — page copy and build specs for the Astro site
  - `CONTENT_MANAGEMENT.md` — full pipeline documentation
- `scripts/` — all scripts live here, organized by purpose
  - `sanity/` — push scripts for Sanity CMS
  - `research/` — data gathering, chart rendering, analysis
  - `contacts/` — outreach list management
- `sales/presentations/` — slide decks, outlines, playbooks
- `outreach/` — contact lists and outreach tracking
- `wiki/` — Starlight-based internal wiki (separate git repo)
- `conversations/` — archived Claude conversation exports

### Related repos (relative to this repo, i.e. under `/Users/arthur/www/dashbud/`)
- **Website (Astro):** `../website/dashbud-home-astro-01/` — the actual site code
- **App code:** `../app_code/Dashbud/` — the Dashbud application codebase
- **Jira CLI:** `../app_code/Dashbud/.jira/jira_cli/` — local-first ticket management
- **Marketing tickets:** `../app_code/Dashbud/.jira/jira_cli/workspace/tickets/marketing/`

## Rules

### Git: Arthur controls all git operations
Never run git add, commit, push, merge, checkout, or branch creation. Arthur reviews and commits himself. Read-only git commands (log, diff, status) are fine for investigation. If work is done, mention what changed and let Arthur handle git.

### Scripts: save to files, never inline
Always save scripts to the `scripts/` directory as files before running. Never run raw python one-liners or inline scripts via the command line. Write the file first, then run it.

### Python: always use venv
Never install packages into bare/system Python. The venv is at `.venv/`. Always activate it first: `source .venv/bin/activate && pip install ...` or use `.venv/bin/python`.

### Content accuracy
Always read actual files before claiming what's in them. Do not work from memory or assumptions about file contents. This is critically important — content has been revised many times.

### Research output
Save research output as markdown files in a logical location within this repo. For website-related research, `website/` or `website/pages/` is appropriate. For general research, `scripts/research/` for scripts and data, and a summary doc in the relevant topical directory.

### Web scraping with Zyte API
The Zyte API is available for web research and scraping. API key is in `.env` at the content repo root (`ZYTE_API_KEY`). See `scripts/research/scrape_comparators.py` for a working example of the pattern: Zyte API for HTTP fetching + BeautifulSoup for parsing. Requires `zyte-api` and `beautifulsoup4` packages (in the venv).

## Current marketing context (July 2026)
- Product exists and has been pitched with some traction
- Website is mid-relaunch: new Why Dashbud and Use Cases pages in development
- Build specs ready for coding agent at `website/pages/*-build-spec.md`
- Hero carousel being updated (remove fictional company names — see `website/pages/carousel-update-spec.md`)
- Key positioning: "Stop wrangling data. Start getting answers." / "AI-powered analytics for all your data"
- Target market: mid-market companies, especially PE portfolio companies with legacy systems
- Competitive landscape: ThoughtSpot, Sigma, Zenlytic, Omni, Power BI + Copilot
- Key differentiator: AI never sees raw data (privacy), semantic model as shared business rules, works with legacy/messy data sources

## Wiki
The internal wiki lives at `wiki/` (Starlight-based, separate git repo). Content source files are in `wiki/dashbud/` organized by topic (background, research, comparators, sales, website, etc.).

### Visibility convention
- **Default is public** — files with no `visibility` field are published to the wiki
- Add `visibility: private` to frontmatter to keep a file out of the published wiki
- The build script (`wiki/build-docs.sh`) skips files with `visibility: private`
- Use this for draft/working research that isn't ready to share

### Writing wiki content
- Save markdown files directly in the appropriate `wiki/dashbud/` subdirectory
- Files can have frontmatter (with `title:`, `visibility:`, etc.) or be plain markdown (title extracted from first H1)
- Subdirectories are supported and mirrored in the published site structure

## Jira tickets
Marketing tickets use the MKT project prefix. New tickets are created locally with a provisional "L" suffix (e.g., MKT-53L). Arthur periodically pushes tickets to Jira for visibility, which assigns a real ticket number — it may be the same number without the L, or a different number entirely. Before referencing a ticket ID in content, check the ticket directory for the current filename. Ticket files are in the Jira CLI workspace at the path listed above. The AI should never run Jira write commands.
