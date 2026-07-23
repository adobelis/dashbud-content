# AI workflows: here to save the day!

At first an AI workflow you built yourself with AI (say Claude Code or ChatGPT) seems like the ultimate solution. 

You *can* build a reporting workflow in Claude or ChatGPT. Get it to write a Python script, hook up a cron job, pipe the output to email. It works! But there are some serious issues to be aware of.

## What happens next?

* Support: who maintains the script, modifies it when it needs updating?
* Scaling and sharing: What happens when you share it, and someone wants a different view of the data? 
* This is the competence penalty — anyone who has created a great spreadsheet knows the perils of becoming the owner of "the spreadsheet." 
* But different and worse: now it's code, and code you didn't write yourself.

**You can build yourself a report. But now you're the data team, the DevOps team, and the support desk — none of which is your actual job.**

## Flexibility, scope, and accuracy

* AI workflows are fine for simple reports: "pull these 6 numbers out of these two SaaS APIs and them to me in a daily email." Complications arise when you make a calculation — even just to combine two numbers. Calculations involve assumptions and need to be audited. 
* Who checks the calculations and confirms the sources and assumptions are correct? AI wrote you a Python script. Can you read it and guarantee it's coded correctly? 
* This is the dueling reports problem: Candace's report says x, Mike's says y. 
* Except worse, because with AI the authors may not understand the code, or worse, the report may be completely prompt-based and ad hoc.

**You can build yourself a report. But even the least complexity requires you to audit and justify the calculations, and AI workflows make this more difficult.**

## Privacy and security

It is possible to build secure data workflows with AI, but giving generalist AI tools access to private and sensitive data is a recipe for disaster.

* General-purpose AI tools (Claude, ChatGPT) require you to upload or provide access to your raw data.
* Your data may be stored, logged, or used for model training — even with opt-outs, the risk is real.
* Regulatory environments (HIPAA, financial compliance) make this a non-starter.
* Building your own security layer around an AI workflow is another job you didn't sign up for.

**AI can power your analytics without seeing your data. That's what Dashbud does.**

# From ad hoc AI to Dashbud

Dashbud replaces your ad hoc, self-supported, and insecure reporting workflows with a stable, auditable, secure solution. 

You can easily reproduce your existing work in Dashbud — even drop the original prompts or the code itself into a Data Explorer conversation. 

The difference is what happens after the first report:

* Your queries are saved as stable SQL — not re-prompted every time.
* Your business rules live in the semantic model — shared, not siloed in one person's script.
* Your team can self-serve dashboards — no one has to ask you for a different view.
* Your data stays private — the AI never sees the raw values.

You keep the intelligence of AI. You lose the maintenance, the fragility, and the risk. That's the upgrade from workflow to platform.