# Who It's For

## You have the data. You just can't get at it.

Your ERP has ten years of sales history. Your spreadsheets track everything from inventory to payroll. Your SaaS platforms generate reports you never read because they can't talk to each other.

The data is there. Getting answers out of it is the problem.

You've looked at Power BI and Tableau — too complex, too expensive, need a dedicated person. You've tried exporting to Excel — fragile, manual, breaks every month. Maybe you've experimented with AI tools — impressive for one-off questions, terrifying for anything that matters.

Dashbud is built for companies in exactly this position.

---

## Your answers are bottlenecked

Access to the system is limited to one or a few people. Everyone else waits — for the export, for the report, or for the whole analysis. The data is there, but access runs through a single point of failure.

Dashbud gives everyone access to the data they need and the ability to report from those sources themselves. 
* **Enabling access**: Dashbud connects directly to databases (such as PostgreSQL, SQL Server), data warehouses/lakes (such as BigQuery, Snowflake), and APIs (such as Google Sheets, Excel, QuickBooks), and file uploads. 
* **Governing access**: Dashbud allows you to give access to each platform's data to exactly the people to need it, and allows exclusion of sensitive columns and row-based filtering, if user X should not see user Y's data.
* **Semantic modeling and business rules**: Dashbud learns both where your data is and what it means. No one needs to know that `GL00100` is the general ledger accounts table — they just ask "what were our operating expenses last quarter?" and get an answer. Dashbud learns how you work, translating your system's internal language into business terms your team actually uses. 
* **Meets your data where it is.** Dashbud connects directly to your databases, including those powering systems like Dynamics GP, Epicor, SAP Business One, and Infor. But we also realize some systems don't support direct connection or API-based access, so Dashbud also provides automated workflows for legacy platforms, as well as personal data file uploads for one-off analysis.

With Dashbud, anyone on your team can self-serve. The bottleneck is gone.

**Example:** Your team runs on an ERP that wasn't built for reporting. You export daily CSVs to Google Drive. Dashbud auto-imports, cleans the data, and gives finance, sales, and ops their own dashboards — each team sees only their numbers. The person who used to pull every report goes back to their actual job.

*Legacy ERPs, production databases, locked-down systems, single-person dependencies*

---

## Your sources are scattered

Your CRM knows your customers. Your accounting system knows your revenue. Your inventory system knows your stock levels. Your POS knows what sold today. But no single tool can answer "which customers are most profitable after accounting for returns and shipping costs?"

Dashbud brings multiple sources together under one semantic model. Define the relationships once — this customer ID matches that account number, this product SKU maps to that inventory code — and then query across all of them as if they were one system. Databases, spreadsheets, cloud platforms, CSV exports — all in one place.

**Example:** You run a CRM, an accounting platform, and an inventory system. Each has part of the picture but none can answer questions across all three. You connect them all to Dashbud, define the relationships once, and your team queries across the full picture — customers, revenue, and stock in one place.

*Multi-system businesses, multi-location operations, mixed cloud and on-prem, databases alongside spreadsheets*

---

## Your reporting is *ad hoc*

The monthly report takes two days. Half that time is pulling data from three different systems and pasting it into a master workbook. The other half is updating formulas, fixing broken references, and praying nothing shifted by a row. And when someone asks for a different cut of the numbers, the whole process starts over.

This isn't a tool problem — it's a trust problem. Everyone builds their own reports, with their own assumptions, in their own spreadsheets. "Profit" means one thing to finance and another to sales. Nobody trusts anyone else's numbers.

Dashbud replaces the ad hoc reporting cycle. Define your business rules once — what "margin" means, how to calculate utilization, which accounts roll up into overhead. Every query, every dashboard, every team uses the same definitions. When the definition changes, it changes everywhere. No more dueling reports. No more "Candace's numbers say X but Mike's say Y."

**Example:** Your head of marketing produces revenue breakdowns, channel performance, and campaign ROI to create a monthly executive report in Excel. It takes his top analyst five hours to update it every month. Your head of strategy produces her own similar report, which sometimes produces different results. With Dashbud, everyone uses the same data and business rules. Reports have an easy-to-audit query trail. Data is live or from shared imported sources, and reports update automatically. Top analysts are freed to do real work, and everyone is singing from the same songbook.

*Spreadsheet overload, ad hoc AI scripts, tribal knowledge, the competence penalty*

---

## Your data is sensitive

You need analytics — revenue by specialty, margin by client, utilization by team — but your data lives in systems with strict access controls and compliance requirements. Most AI tools want to see your data. That's not an option.

Dashbud's AI never sees a single data value. It reads your schema — field names, table structures, business rules — and writes a SQL query. The query runs against your data, and the results go to your screen. Every number has a source. Every calculation is auditable SQL. No patient record, no financial detail, no sensitive value ever touches an AI model.

For Epic users, Dashbud connects to Clarity or Caboodle — the reporting databases your system already maintains. For other systems, CSV or flat-file exports work just as well.

**Example:** You need operational analytics — revenue by provider, visit trends, payer mix — but you can't expose patient data to external platforms. You connect Dashbud to your reporting database. The AI writes queries from your schema without ever seeing a record. You get the analytics without the compliance risk.

*Healthcare and PHI, financial services, legal, HR and payroll, any regulated industry*

---

## How Dashbud is different

### AI that never sees your data
The AI reads your schema — field names, table structures, business rules — and writes SQL. It never sees a single data value. Your query runs against your data directly, and the results go to your screen. If you don't know where a number came from, you won't trust it. In Dashbud, every answer traces back to an auditable query.

### Shared business rules, not tribal knowledge
"Profit" means different things to different people. In Dashbud, you define it once in the semantic model — the people who know the business define the rules, not a data engineering team. Every query, every dashboard, every team uses the same definition. When the definition changes, it changes everywhere.

### Works with your data as it is
Messy CSVs from a legacy export? Dates in three different formats? Currency columns with dollar signs baked in? Dashbud's smart data loading cleans and normalizes automatically. You don't need to fix your data before you can use it. You don't need a data warehouse. You don't need an ETL pipeline.

### Days to deploy, not months
Connect or upload. Model the data through conversation. Start asking questions. Most teams are running real queries within a day. No data warehouse to build, no pipeline to maintain, no six-month implementation project.
