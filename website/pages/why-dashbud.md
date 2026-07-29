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
* Flexible
* Existing expertise

**Negatives:**
* Fragile, time-consuming to update
* Hard to share, competence penalty

### AI Workflows (Claude, ChatGPT)
**Positives:**
* Fast for one-off analysis and periodic reports
* Surprisingly capable

**Negatives:**
* Calculations opaque, difficult to audit (see more)
* Doesn't scale (see more) 
* The vibe-coding problem (tech debt)
* Serious privacy and security concerns

##  AI workflows: here to save the day!

At first an AI workflow you built yourself with AI (say Claude Code or ChatGPT) seems like the ultimate solution. 

You can build a reporting workflow in Claude or ChatGPT. Get it to write a Python script, hook up a cron job, pipe the output to email. It works!

### Question 1: what happens next?

Who maintains the script, modifies it when it needs updating?
What happens when you share it, and someone wants a different view of the data, e.g. filtered? 
This is the competence penalty – anyone who has created a great spreadsheet knows the perils of becoming the owner of "the spreadsheet." 
But different and worse: now it's code, and code you didn't write yourself.

**You can build yourself a report. But now you're the data team, the DevOps team, and the support desk — none of which is your actual job.**

### Question 2: flexibility, scope, and accuracy

* AI workflows are fine for simple reports: "pull these 6 numbers out of these two SaaS APIs and them to me in a daily email." Complications arise when you make a calculation — even just to combine two numbers. Calculations involve assumptions and need to be audited. 
* Who checks the calculations and confirms the sources and assumptions are correct? AI wrote you a Python script. Can you read it and guarantee it's coded correctly? 
* This is the dueling reports problem: Candace's report says x, Mike's says y. 
* Except worse, because AI makes the reports more opaque and difficult to audit.

**You can build yourself a report. But even the least complexity requires you to audit and justify the calculations, and AI workflows make this more difficult.**

### Question 3: privacy and security

It is possible to build secure data workflows with AI, but giving generalist AI tools such as GPT or Claude Code access to private and/or sensitive data is a recipe for disaster.

* Generalist AI tools such as Claude Code aren't private or secure by default. When you invite them to look at your data, they will inspect sensitive data and may train on it.
* You can build a workflow that is secure, but it requires knowledge, discipline, and auditing.
* For any regulated industry, such as finance or healthcare, allowing your team to use generalist AI tools with your data is a terrible idea and may in fact be illegal.

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

## Switching to Dashbud is easy

### Your spreadsheets →
Upload them. Ask questions in plain English. Replace complex, fragile tables with stable reports.

### Your SaaS platforms →
Connect via API. See all your data in one place. Stop switching between dashboards.

### Your database / ERP →
Connect directly. No exports, no ETL. Reports update live.

### Your AI workflow →
Keep the intelligence. Lose the maintenance. Share the results with your whole team.

## Designed for privacy, security, and trust

**AI never sees your raw data.** The AI only sees field names and schema — never the actual values in your database.

**Deterministic reports.** The AI writes a SQL query once. After that, it's a traditional report. Same question, same answer, every time.

**Full audit trail.** Every data import is tracked and can be rolled back. Your data stays in your database or in Dashbud's managed infrastructure.

**No third-party sharing.** We don't share your data with third parties. We don't use it for AI training.
