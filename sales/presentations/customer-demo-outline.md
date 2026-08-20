---
title: Dashbud Customer Demo — Model Presentation Outline
type: sales_playbook
created: 2026-08-19
based_on: Trillium Creek dry run and demo (2026-08-19), TC demo learnings
---

# Dashbud Customer Demo — Model Outline

## 1. Introduction (~2 min)

**Scott:** "Hi, thanks so much for joining us. I'm Scott Binger, and joining me is my partner Arthur Dobelis. We're really excited to show you Dashbud today.

"Dashbud is an analytics platform that lets you create all the reporting you need using plain language. We use AI to do that, but we're not just an AI agent — we're a whole system. Everything from connecting your data sources to building reports to sharing dashboards with your team fits together in one place. The goal is to get you from having a bunch of data scattered across systems to having effective, sustainable reporting — without needing a data team or learning a complicated tool."

**Key framing:**
- Dashbud is **an analytics platform** that allows you to create all the reporting you need
- We use AI to do that, but **we're not just an agent — we're a whole system**
- A **conversational interface** where you use **plain language** to create exactly the reporting you need
- Avoid: "have a conversation with your data" — too vague, doesn't convey the system, the sustainability, or the outcomes. It can be used casually but shouldn't be the lead.

## 2. Discovery (~5 min)

**Arthur:** "Before we jump in, we'd love to learn a little about you so we can tailor this to what matters most."

- "Tell us about your practice — how many locations, how many providers, that kind of thing."
- "What reporting are you running today? What's the most painful part of that process?"
- "What systems are you using — your EMR, billing, HR, marketing? Is everything in one place or spread across a few tools?"
- "Who on your team needs to see this data? Is it mainly you, or is leadership asking for visibility too?"
- "What brought you to look at something like Dashbud right now?"

**Listen for:** multi-site complexity, legacy/opaque systems, manual exports to Excel, reports that someone rebuilds every month, leadership wanting visibility they don't have.

## 3. Why not just use AI? (~3 min)

Address this proactively — it's the question everyone has or will have.

**Arthur:** "Before I show you the product, I want to address something that comes up a lot, which is: why not just use Claude or ChatGPT for this?

"It's a fair question. You can absolutely sit down with Claude, give it access to an API or a data export, and have it write you a report. And if you're technically comfortable, that can work for a one-off question.

"But there are three problems with that approach as your ongoing reporting solution.

"First is **sustainability**. If somebody builds a set of reports by asking Claude to write Python code, and that person leaves — can the next person maintain it? Do they even know what prompts were used? You're one departure away from rebuilding everything from scratch.

"Second is **consistency**. AI is non-deterministic. You can ask the same question two days in a row and get a slightly different answer — not because the data changed, but because the AI decided to approach it differently. That's fine for brainstorming. It's not fine for a monthly financial report that your leadership relies on.

"Third is **privacy**. If you're feeding raw patient data, or really any sensitive business data, directly into Claude — you're in a gray area at best. For healthcare, you're probably non-compliant with HIPAA.

"Dashbud solves all three. Our AI never sees your raw data — by default, it only sees the structure: what tables you have, what columns are in them, how they relate to each other. You teach it your business context once — your terminology, your coding systems, your accounting practices — and from that point on, every report is generated from the same shared understanding. If someone leaves, the model stays. If you run a report today and again next month, you get the same query, the same logic. It's locked down and reproducible."

**The vibe-coding problem (talking points if needed):**
- If you ask Claude to write reports against your API or your data exports, you get code. If somebody leaves, can the next person maintain that code?
- AI is non-deterministic — you can get a different answer on different days, not because the data changed but because the AI decided to do something different
- There's no shared understanding of your business rules — every person who asks gets their own version of the truth (the Lovable anti-pattern)
- Privacy/HIPAA: if you're feeding raw patient data into Claude, you're probably non-compliant

**What Dashbud does differently (talking points if needed):**
- It's a dedicated analytics system, not a one-shot AI interaction
- Privacy first: by default, Dashbud does not expose your data to AI. The AI only sees the schema — the shape of your data, not the rows
- Sustainability: you set up the semantic model once. Reports are locked down and reproducible. The AI isn't re-inventing the query every time.
- Shared business rules: everyone works from the same definitions (what "revenue" means, what "active patient" means, how accounting works)

## 4. How it works — the 4 steps (~2 min, with visual)

Use the step-by-step slide from the deck:

**Arthur:** "Let me give you a quick overview of how the system works before we dive into the live product. There are really four steps."

**[Show step-by-step slide]**

1. **Connect your data** — import files (CSV/Excel), connect APIs, or connect directly to databases. Multiple data sources can be combined. "If your EMR data lives in one system and your HR or billing data lives somewhere else, you can bring them together."

2. **Model your data** — the semantic modeling agent learns the shape of your data. You educate it about your business context (coding systems, accounting practices, terminology). It doesn't need to see any private data. "Things like: we use ICD-10 codes, our fiscal year starts in July, 'encounter' and 'visit' mean the same thing. This is a set-it-and-forget-it step."

3. **Explore your data** — conversational reporting interface. Ask questions in plain language, get charts and tables. Save the ones you want to keep. "You type a question — 'how many visits did we have last month by location' — and you get a chart or a table."

4. **Share your data** — saved reports roll up into dashboards. Share with stakeholders who don't need full access. Schedule email delivery daily/weekly/monthly. "They don't need a Dashbud account to see them."

**Key phrase:** "Set it and forget it." Once the semantic model is configured, you shouldn't have to go back to it.

## 5. Live demo (~10-15 min)

### Data sources view

**Arthur:** "So here's Dashbud. Let me start at the beginning — data sources. What we did to prepare for today: we created a demo dataset modeled on a multi-location dermatology practice. We loaded it in as CSV imports, which is one way data gets into the system.

"You can see we have several tables — patients, appointments, encounters, diagnoses, procedures, charges, locations. In your case, this would represent what comes out of ModMed. And if you have other data you want to bring in — HR data, marketing data, inventory — you can add additional data sources and combine them.

"We also have an append feature, so you don't have to reload everything every time. If you have a fresh month of data, you just drop it in and we handle deduplication and updating automatically."

- Show the uploaded tables (or connected data source)
- Emphasize: you can load multiple data sources — EMR data, HR data, billing data, marketing data — and combine them
- Show the append/deduplicate feature for ongoing imports

### Semantic model view

**Arthur:** "This is the semantic model — what our AI actually knows about your data. You can see it's all structure: tables, columns, relationships. Patient ID connects patients to encounters. Provider ID connects encounters to providers. Location ID ties everything to a specific office.

"Notice what's not here: no patient names, no diagnoses, no billing amounts. The AI doesn't need any of that to understand how to write a correct query. It just needs to know the shape.

"If there's something specific to your practice — you use a particular procedure coding system, or you categorize diagnoses into groups, or you have specific terminology — you educate the model here. This is the page that makes reporting sustainable and accurate. But once it's set up, you probably won't come back to it often."

- Show what the AI knows: tables, columns, relationships
- Emphasize: this is ALL the AI sees. No row-level data. No patient records. Just the structure.
- Point out that you can add business context (terminology, coding systems, categories)
- **"This is what makes it sustainable and accurate"**

### Data Explorer (the core demo)

**Arthur:** "This is where you spend your time. Data Explorer — you ask questions, you get answers."

Run 3-5 prepared queries that are relevant to the prospect's use case. For healthcare:
1. "Count diagnoses by type, monthly" — time series, shows chart/table toggle
2. "Monthly visits by location for the last two years" — multi-site visibility they can't get from their EMR
3. "Which provider has the highest no-show rate?" — actionable ops insight
4. "What are our top diagnoses by volume?" — clinical mix overview
5. A filtering/drill-down query (by location + diagnosis + payer) — shows multi-dimensional capability

**Show the flow:** ask question → get chart → switch to table view → switch chart types (line, bar, area, stacked area) → save as favorite

"Now, all of this is conversational. There's sometimes a bit of trial and error with how you phrase things — but once you get a report right, you save it, and it's locked down. The AI isn't involved anymore after that. It runs the exact same query every time."

### Favorites and dashboards

**Arthur:** "So I've been asking a lot of questions, but I only want to keep a few of them long-term. That's what favorites are for. I save the ones I care about — like 'top diagnoses by month' and 'provider weekly procedures.'

"Then in dashboards and reports, I can pull those saved reports into a dashboard. Drag and drop, arrange them however I want. Toggle between chart and table view. Add a totals row. If you're comparing Q1 to Q2, you can add a difference line.

"This is what you'd share with your leadership, your office managers, whoever needs to see the numbers. They don't need to use the Explorer — they just see the dashboard. And you can schedule it to go out by email so it lands in their inbox every Monday morning or the first of every month."

- Show a pre-built dashboard with 2-3 saved reports
- Add a new report from favorites (drag and drop)
- Show chart vs. data toggle
- Show parameterized filtering (if working)
- Emphasize: these are shareable. Leadership can see updated dashboards without needing to use the Explorer.

**Anticipated question:** *"So each month, we run 10 to 20 reports after we close the month. Could we set those up as favorites?"*

**Arthur:** "Exactly. You'd build each one once in the Explorer, save it as a favorite, and then assemble them into a monthly close dashboard. Every month you just open it and see the latest numbers. No rebuilding, no re-exporting."

### If things go wrong
- If a query doesn't produce the right result, acknowledge it: "There's sometimes a bit of trial and error, but once a report is right, it's locked down and reproducible."
- Offer to produce a customized demo with their specific report needs

## 6. Pricing (~2 min)

*Wait for them to ask, or transition naturally after the demo.*

**Arthur:** "For pricing — we have a straightforward per-seat model. $40 per seat per month on an annual contract, or $50 monthly. There's a two-seat minimum to unlock the full sharing and distribution features — live dashboards, emailing reports to stakeholders who don't have their own accounts.

"So if two people on your team want full access to build and manage reports, you're looking at $80 a month annually. Everyone else in your organization can view the dashboards and receive reports without needing a paid seat."

*If they react to the price:* "We're priced to be accessible. We want you to be able to get started and see value before making a bigger commitment."

- **Starter:** $40/seat/month (annual) or $50/seat/month (monthly)
- **2-seat minimum** for full sharing/distribution capabilities
- 1 seat = personal use + forwarding reports. 2 seats = live dashboards + report distribution to non-paying stakeholders.
- Priced for accessibility — we want you to get started, not to commit to an enterprise contract

Don't oversell pricing. State it simply. If they ask, that's a buying signal.

## 7. Getting started / next steps (~2 min)

**Arthur:** "If you're interested in taking this further, there are a couple of paths.

"The fastest way to get started: we create an account for you, you export your data from [their system] as CSVs, upload it to Dashbud, and we build the semantic model together. You could be querying your real data the same day.

"The refresh cycle with imports is manual — every time you want fresh data, you'd re-export and re-upload. That's fine for a trial and for getting a feel for the system. Longer term, an API connection automates that entirely.

"If you'd prefer, we can also put together a customized demo using your specific reports — the exact questions you ask every month — so you can see exactly how Dashbud handles them. And if you want to use real data, we're happy to sign an NDA.

"Either way, we'll follow up with an email today with next steps. What sounds most useful to you?"

**Day 1 path (no engineering):**
- We create their account
- They export from their system as CSVs
- Upload to Dashbud, build semantic model
- Start querying their real data

**If they want a deeper evaluation:**
- Offer a customized demo with their specific reports
- Offer an NDA if they want to use real data
- Offer a 30-day trial

**If an API connector is needed:**
- Acknowledge the gap, describe the path, give a timeline
- Don't make promises about specific connectors without checking feasibility

## Notes

### Tone
- This is a demo, not a pitch. Let the product speak. If they say "I just want to see it," skip straight to section 5.
- Be honest about limitations. "We don't have that connector right now, but here's how we'd get there."
- Don't oversell. These are mid-market ops people — they want to see that it works, not hear about AI magic.
- If cameras are off and answers are short, don't push for engagement. Just demo well and let them digest.

### Common questions

**"Are you HIPAA compliant?"**
"We follow HIPAA rules and guidelines. By default, Dashbud does not expose your data to AI. We're happy to walk through our specific practices and execute a BAA if needed."

**"Can we compare year-over-year?"**
"Yes — you can ask for any time comparison. 'Show me January 2026 vs January 2025 by provider,' that kind of thing." *(Make sure this works in the demo data before the call.)*

**"Can we set up recurring monthly reports?"**
"Yes. Save them as favorites, build them into a dashboard, and schedule delivery. Your month-end reporting becomes opening a dashboard, not rebuilding 15 spreadsheets."

**"What if someone leaves?"**
"The semantic model and all saved reports persist. Nothing is tied to one person's session or their code. A new person can pick it up and understand exactly how everything works."

**"How is this different from Tableau / Power BI / Domo?"**
"Those are expert tools built for data analysts. You need training, you need someone who knows how to configure dimensions and measures and build visualizations. Dashbud is built for the people who need answers — ops leads, practice managers, executives. You ask a question in plain language, you get a report. No learning curve beyond learning how to ask good questions."

**"Why should we use this instead of [EMR]'s built-in analytics?"**
"[EMR]'s analytics are fine for basic pre-built reports. But they typically have limited data history, limited customization, and they can't combine data from other systems. If you want to see your EMR data alongside your billing data, your HR data, your marketing data — or if you want reports that [EMR] doesn't offer out of the box — that's where Dashbud comes in."
