# Why Dashbud

## The landscape

Every business runs on data. You already have it -- probably more than you want to think about right now:

* spreadsheets and other local and cloud-hosted data files
* myriad business platforms: CRM, POS, ERP, marketing, advertising, etc., etc.
* dedicated data resources such as DBs and data lakes. 

So how do you *use* that data? How do you *grab the data you need* and turn it into *information you can act on*?

## Every approach has trade-offs

### SaaS Dashboards (QuickBooks, Google Analytics, etc.)
**Positives:**
* Built in, no setup

**Negatives:**
* Clunky interfaces
* Siloed: can't mix data sources

### BI Tools (Power BI, Tableau)
**Positives:**
* Powerful, enterprise-grade

**Negatives:**
* Finicky, hard to learn, expensive
* Often: need a data team or dedicated resource

### Spreadsheets (Excel, Google Sheets)
**Positives:**
* Flexible, you control it

**Negatives:**
* Fragile, time-consuming to update
* Hard to share, competence penalty

### AI Workflows (Claude, ChatGPT)
**Positives:**
* Fast for one-off analysis and periodic reports
* Surprisingly capable

**Negatives:**
* Doesn't scale - multiple one-offs
* You become the infrastructure
* Calculations → COMPLICATIONS (who audits?)
* The vibe-coding problem (tech debt)

##  AI workflows: here to save the day!

At first an AI workflow you built yourself with AI (say Claude Code or ChatGPT) seems like the ultimate solution. 

You can build a reporting workflow in Claude or ChatGPT. Get it to write a Python script, hook up a cron job, pipe the output to email. It works!

### What happens next?

Who maintains the script, modifies it when it needs updating?
What happens when you share it, and someone wants a different view of the data? 
This is the competence penalty — anyone who has created a great spreadsheet knows the perils of becoming the owner of "the spreadsheet." 
But different and worse: now it's code, and code you didn't write yourself.

**You can build yourself a report. But now you're the data team, the DevOps team, and the support desk — none of which is your actual job.**

### Flexibility, scope, and accuracy

* AI workflows are fine for simple reports: "pull these 6 numbers out of these two SaaS APIs and them to me in a daily email." Complications arise when you make a calculation — even just to combine two numbers. Calculations involve assumptions and need to be audited. 
* Who checks the calculations and confirms the sources and assumptions are correct? AI wrote you a Python script. Can you read it and guarantee it's coded correctly? 
* This is the dueling reports problem: Candace's report says x, Mike's says y. 
* Except worse, because AI makes the reports more opaque and difficult to audit.

**You can build yourself a report. But even the least complexity requires you to audit and justify the calculations, and AI workflows make this more difficult.**

### Privacy and security

It is possible to build secure data workflows with AI, but giving generalist AI tools access to private and sensitive data is a recipe for disaster.

* General-purpose AI tools (Claude, ChatGPT) require you to upload or provide access to your raw data.
* Your data may be stored, logged, or used for model training — even with opt-outs, the risk is real.
* Regulatory environments (HIPAA, financial compliance) make this a non-starter.
* Building your own security layer around an AI workflow is another job you didn't sign up for.

**AI can power your analytics without seeing your data. That's what Dashbud does.**

## How Dashbud helps

### vs. SaaS dashboards
* Well-designed conversational interface – not an afterthought.
* Works across multiple data sources — not siloed.

### vs. BI tools
* Same analytical power and polished display formatting.
* Interactive charts and dashboards out of the box.
* Weeks of platform training not required.

### vs. spreadsheets
* Flexible reporting without the fragility.
* Built-in data updates, versioning, rollback.

### vs. AI workflows
* Same AI-powered outputs — but the infrastructure is built for you.
* Calculations are auditable SQL.
* Business rules and assumptions are shared: decided by agreement, not an AI script.

## Switching is easy

### Your spreadsheets →
Upload them. Ask questions in plain English. Replace complex, fragile tables with stable reports.

### Your SaaS platforms →
Connect via API. See all your data in one place. Stop switching between dashboards.

### Your database / ERP →
Connect directly. No exports, no ETL. Reports update live.

### Your AI workflow →
Keep the intelligence. Lose the maintenance. Share the results with your whole team.

## How it works

### 1. Connect your data
Upload spreadsheets, connect directly to databases, or sync from cloud sources. Smart data loading cleans messy formats automatically.

### 2. Model through conversation
Tell Dashbud what your data means — in plain language. The AI asks questions, you answer. No code, no config files.

### 3. Ask questions, get answers
Type questions in the Data Explorer. Refine through conversation. Dashbud produces the KPIs, tables, and charts you need. Smart formatting. Parametrized controls. Same answer every time.

### 4. Create reports and share
Output anything from individual KPIs to sophisticated charts and tables. Drag and drop outputs into dashboards. Share self-service interactive dashboards; email one-off and periodic reports.

## Designed for privacy, security, and trust

**AI never sees your raw data.** The AI only sees field names and schema — never the actual values in your database.

**Deterministic reports.** The AI writes a SQL query once. After that, it's a traditional report. Same question, same answer, every time.

**Full audit trail.** Every data import is tracked and can be rolled back. Your data stays in your database or in Dashbud's managed infrastructure.

**No third-party sharing.** We don't share your data with third parties. We don't use it for AI training.
