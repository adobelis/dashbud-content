Title: Dashbud — One-Pager
Purpose: Landing page for visitors coming from the LinkedIn announcement or other top-of-funnel content. A survey, not a drill-down. Covers why, who, and how in one page. Should be scannable in under 5 minutes.
URL: TBD — `/about-dashbud`, `/learn`, `/overview`?
Audience: Someone who just read the "born free" post, or another general-interest post, and wants to understand what Dashbud is and why it exists. Not shopping for BI tools yet. Curious, not comparing.
--
# Dashbud — One-Pager

## Section 1: The Problem (Why)

**Everyone wants to be data-driven. So why aren't they?**

Your company runs on data — sales figures, operational metrics, customer records, financial reports. But getting answers from that data can be a problem. Every approach solves part of the problem, only to create new ones. 

**Dashboards: prefab silos.** Your SaaS platforms each have their own dashboards. Some are okay, some are terrible. Regardless, they can't talk to each other and they only answer the questions the platform company thought you might ask.

**Spreadsheet: where your precious time goes to die.** You export the data to Excel. You clean it and build a report. A month later it's out of date, so you update it, a fragile process that takes from minutes to hours. If it's good, you share it. Then you leave the company, and who takes it over? 

**BI: tools with a bright future behind them.** Tableau, Power BI, Looker: so much power, so much promise. Then you woke up to discover the true cost: that you need to invest seriously in data analysts and infrastructure to make them work properly. Now you have both a new cost center and a new dependency to worry about. 

**AI workflows: a tantalizing mirage.** LLMs and vibe-coding tools can pull data from APIs and produce very pretty dashboards and reports. But the outputs are opaque and the calculations may shift between runs. Making business decisions based on the outuput of code you don't understand - sure, what could go wrong? Handing your company's or customer's private data to AI without guardrails... ditto.

---

Zoom out: where do these approaches fall down? The process of creating actionable business reporting is as follows:

* Capture and source the data: get it from wherever it lives to somewhere you can use it. 
* Clean it and make it usable: untangle the mess of overlaps, different date, unit, and naming conventions, etc. You'd do this by hand in a spreadsheet. You'd have a data engineer write an ETL pipeline for a large-scale project.
* Put it somewhere people can access it: trivial for an individual, or at least a organized person; big infrastructure project for a company.
* Analyze following shared rules: either grind out a really good spreadsheet

---

## Section 3: Who It's For (Scale)

### From one user to a whole company.

Dashbud works at every scale:

**Individual user.** You have a few spreadsheets or a CSV export from a system that won't give you the reports you need. Upload them, ask questions in plain English, get charts and answers in minutes. No coding, no formulas, no pivot tables.

**Small team.** Your team shares data across a few systems — a CRM, an accounting platform, maybe a Google Sheets tracker. Connect them all, define the relationships once, and give everyone self-serve access to the answers they need. The person who used to pull every report goes back to their actual job.

**Whole company.** Your organization runs on an ERP, an EMR, a data warehouse, or all three. Dashbud connects directly to production databases and reporting layers. Shared business rules mean every department works from the same definitions. Data governance controls — column exclusion, row-level filtering, workspace scoping — mean everyone sees exactly what they should and nothing they shouldn't.

### Data sources Dashbud works with:

| Source type | Examples |
|---|---|
| Direct database | PostgreSQL, MySQL, SQL Server |
| Cloud/SaaS | Google Sheets, APIs |
| File imports | CSV, Excel exports |
| Legacy/ERP | Via export-to-CSV or reporting database (Dynamics GP, Epicor, SAP, Infor, ModMed, Epic Clarity) |

---

## Section 2: The Approach (What Dashbud Does Differently)

### AI-powered analytics where the AI never sees your data.

Dashbud connects to your data — databases, spreadsheets, cloud platforms, file exports — and learns its *structure*: table names, column types, relationships. Then you teach it your *business rules*: what "margin" means, how to calculate utilization, which ad campaigns should be reported together.

When you ask a question, the AI writes a SQL query from the schema and your business rules. The query runs against your data. The results go to your screen. The AI never sees a single data value.

**This is not a limitation — it's the architecture.** It means:

- **Privacy by design.** Sensitive data — patient records, financial details, payroll — never leaves your database or touches an AI model.
- **Auditable answers.** Every number traces back to a query you can read. No black-box calculations. No "the AI said so."
- **Shared definitions.** "Revenue" means the same thing to sales, finance, and the executive team. Define it once, use it everywhere. No more dueling reports.
- **Deterministic results.** The AI writes the query once. After that, it's a traditional report. Same question, same answer, every time.

---

## Section 4: How It Works

### Connect. Model. Explore. Share.

**1. Connect your data.**
Point Dashbud at your database, upload your files, or connect your cloud platforms. Direct database connections are read-only pass-through — your data stays where it is. File imports are encrypted and isolated in managed infrastructure.

**2. Model your business.**
Tell Dashbud what your data means. Rename cryptic field names into business terms. Define calculations, relationships, and rules. This is the semantic model — the shared source of truth for your entire organization. Non-technical users can participate; you don't need a data engineer.

**3. Explore conversationally.**
Ask questions in plain English: "What were our top 10 accounts by revenue last quarter?" Dashbud writes the query, runs it, and returns a chart or table. Drill down, filter, pivot — all through conversation. Every query is visible and auditable.

**4. Share as dashboards.**
Save your answers as reports. Organize them into dashboards. Share with your team. Everyone sees live data governed by the same business rules. Reports update automatically — no manual refresh, no broken formulas.

---

## Section 5: Trust and Security

### Your data. Your rules.

- **AI never sees your raw data.** Schema and business rules only. Row-level data never touches an AI service.
- **No training on your data.** We don't use customer data to train, fine-tune, or improve AI models.
- **Encryption everywhere.** TLS in transit, encryption at rest for all stored data and credentials.
- **Data governance built in.** Column exclusion, row-level filtering, and workspace scoping give administrators fine-grained control.
- **HIPAA-ready.** Dashbud supports HIPAA-covered workflows with a Business Associate Agreement.
- **Self-hosted option.** For organizations that need it, Dashbud can deploy entirely within your own cloud environment. Your data never leaves your infrastructure.

---

## CTAs

**Primary:** Try Dashbud → /signup
**Secondary:** Book a Demo → Calendly
**Tertiary (text links):** Why Dashbud (deep dive) | Who It's For | Privacy Policy
