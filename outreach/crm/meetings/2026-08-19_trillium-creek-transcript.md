---
deal_id: D006
company: Trillium Creek Dermatology
contacts: Michelle Maynard, Aaron Funk
date: 2026-08-19
type: demo_transcript
source_file: sales/presentations/2026-08-19-trillium-creek-raw.md
transcription: Google transcription, cleaned (formatting and transcription errors only)
notes: Demo portion only. Postmortem with Scott captured separately in summary.
---

# Trillium Creek Dermatology — Demo Transcript (2026-08-19)

**Arthur:** So, tell me a little about your practice.

**Michelle:** We're a quality practice. We've got several locations — Medina, Wooster, Wadsworth, Brunswick, Strongsville — so we have five locations and a Mohs Surgery Center. Over 14 providers. We have MDs, PAs, RNs. Not sure what else you want to know.

**Arthur:** No, that's about it, I guess. We gathered that from looking at your web presence. But what in particular are you looking for in data analytics?

**Michelle:** I just kind of stumbled across your platform looking on the ModMed synapSYS website. There wasn't obviously a ton of information, but I just wanted to reach out and kind of see what you have to offer. We have been implementing a lot of AI and automation across different parts of the practice. We do run a lot of monthly reports, daily, weekly — so we just kind of wanted to see what you guys have to offer.

**Arthur:** Are you connecting directly to the ModMed API in order to do that?

**Michelle:** I run everything straight out of ModMed directly. I use all of their reporting functionality that they have natively. I don't connect or use anything external right now.

**Arthur:** I was curious what the automation that you're doing — what the data sources are for that, or is the other automation —

**Michelle:** The other automation is typically usually through an API. But not with ModMed data yet. We are — so like, not with reporting, but other parts of the practice we have APIs for. For example, AI voice for scheduling.

**Arthur:** Sure. That is very good to know.

[Aaron joins the call]

**Arthur:** Hi Aaron, welcome. We are Arthur and Scott, and we're the two founders of Dashbud. We're a reporting platform that leverages AI. We're not just an agent — it's really more like a system. It is a system that allows you to pull all of your data into one place and then have a more structured approach to running reporting, rather than let's say vibe-coding reports.

You wouldn't want to sit down and say "hey Claude, here's a whole bunch of medical data, here's access to an API, go ahead and write me a report." You can do that, and you can create your own guardrails and be very careful about it. But where we differ from that kind of approach is that it's really safety first, it's privacy first, and avoiding the issues that can arise from that.

Also, sustainability. If somebody leaves, will somebody else be able to fix the code that they vibe-coded, that they may or may not — I don't know what your level of coding expertise is — but if Claude or whichever agent generated a whole bunch of Python code for you, do you have somebody who fully understands it themselves?

Is Claude running every time you generate a report? Because that's very bad — it's non-deterministic, so you can get a different answer depending on what day you ask, not because the data changed, just because Claude decided to do something different. That's what AI does.

And then finally, if somebody leaves, can somebody else just take over that whole set of automation very easily?

So Dashbud is designed to solve a lot of those problems. I know we're probably running ahead of where you are, but one of the biggest questions we get — and we're very happy with our answer to — is: why not just do it myself using automation tools? Any questions or thoughts about that? I do like to have that conversation up front because it's a good one to have.

**Michelle:** I think I don't have any questions initially. I think we just need to dive a little bit more into what it looks like, how it works. Because right now I'm not really sure what your software does other than help with reports.

**Arthur:** Sure. I guess we'll jump right into a demo.

**Aaron:** Can you integrate with ModMed? Like, you're on their website?

**Arthur:** So, we had a previous version of our product which integrated with ModMed, and we have totally rebuilt our product, but we still have the code to integrate. We just haven't had an actual ModMed customer who needed it.

**Scott:** I have a relationship with Adam Cooperman — do you know Adam?

**Michelle:** That's not someone I think I regularly work with.

**Scott:** Anyway, the short answer is yes. We have a good relationship with ModMed and we could pretty smoothly and easily get the API connectivity back on track with the platform. So that's not a concern.

---

**Arthur:** All right. Well, so this is Dashbud, and this is a typical view that you might use. You can type in analytical questions about your data. It sounds like you're all fairly advanced technically, so I'll take you back to the very beginning.

Data sources — what we did to prepare for this: we created a standard medical practice demo, created a dermatological practice version of it, and loaded that in. That's one way you can access data — if you don't happen to have a connection to certain data sources, you can load them in as imports.

We even have an append feature so that we can append and deduplicate. Let's say you have your latest month of data and you just want to drop that in and have it update your tables. Not like in Excel where you'd have to figure out where your data ends, make sure you don't have duplicative data — we handle all that.

As you can see, this is a multi-table demo dataset. Apologies if it's a little rough — we're just working off of demo data. Obviously we can't work off real medical data.

**Arthur:** This is the view from our agent — what our agent knows about your data. We are absolutely dedicated to not giving raw data to AI agents. We think it's irresponsible. In most cases, 99% of the time, it also would not be HIPAA compliant.

So what we expose to our agents is really just all the information they need in order to understand your data and write accurate queries against it. In this case, we have a patient table, an appointments table — this would represent, for example, an export from ModMed. All of these relationships — patient ID, provider ID — are established within the system, so it can write multi-table queries to pull the right answers out.

You set this once. If you have particular information you need to fill in — here I had some office data, so I actually allowed it to look at just the locations, so it knows the actual names of the offices. It's not guessing when it writes a query for a single office. But again, that's not private patient data — it was only allowed to look at that data in particular.

These are basically tables and columns. And if there's something particularly — like you have different words you use, like "encounters" or "visits" — if it's intuitive, AI is pretty smart and can get it. But sometimes a particular column isn't named very semantically, or you have particular accounting practices. This is where you would inform our agent so that if you're doing accrual-based accounting, it knows that and doesn't provide incorrect answers based on other accounting systems.

This is not a page you'll visit all the time, but for people with a technical background, it's useful just to know this step in the process exists. This is what we're solving for — sustainable reporting for mid-tier businesses.

**Arthur:** Data Explorer is where you ask questions and get answers. "Count diagnoses by type monthly" — we tried to put in some dermatology diagnoses, but again, this is just pulling directly from the dataset we loaded in.

If there were particular categories you wanted to impose — so you didn't want to see the raw diagnosis codes but wanted a higher-level grouping — ICD-10 is pretty well organized that way. You could use a higher-level code and filter on that description. You can educate the semantic model on that, or load in an additional table that it can read.

But you might also just want to ask more utilization questions — how many visits different providers are taking on in any given week.

[Arthur demonstrates a location-specific query, initially uses wrong office name]

**Arthur:** I'd actually changed the office names, so "Ridgewood Office" is the correct naming. Again, it's conversational — I gave it a not-very-good question, and I realized I actually hadn't let it inspect the office names yet. So when I gave it "Ridgewood," it just searched for "Ridgewood." Now that it's allowed to look at — notice it's very restricted what it's allowed to look at — now that it knows the name is "Ridgewood Office," it creates the correct query.

Any questions about that process?

**Michelle:** So basically here you just ask it a question for a report you want, and it pulls the data from ModMed and just spits out the report. Correct? Okay, yeah.

**Arthur:** And then this is a great interface for generating reports. And if you have ad hoc reporting questions — you want to drill down to a particular provider, or a combination of data that wouldn't be so easy to get out of a report or dashboard, or you wouldn't want to go hunting through a report for a provider-specific answer — you can just ask that right here and get that particular answer.

**Michelle:** Okay, I see there's a favorites section. So each month we have a set of, I would say, 10 to 20 reports. We run the same report every month after we close the month. Would that be something we could set up as favorites?

**Arthur:** Exactly. So from here, you would just save — let's say you're creating that favorite, that monthly report. This might not be one of the ones you'd put in there, but this is like "top diagnoses by month." And I put in a lot of monthly queries to show how it graphs time series data. If you have more non-time-series data where you just want last month's information, that works as well.

So now I've added — I'm just adding reports that are already in here — this one was "provider weekly procedures." I've saved these over here. I might have asked a lot of questions, but I'm not interested long-term in all of them. Or maybe the agent didn't do exactly what I wanted — there sometimes is a bit of trial and error. We don't force you to hunt through all of these in the conversational interface. We allow you to save them as long-term assets.

Then if you go into the dashboards and reports section, I already had one report in here. I can edit this and just add "top diagnoses by month." And I can drag and drop it as I will.

**Scott:** You can also, if you want to change the view from a chart display to data display — you can view the data, view the chart, or view the report as data. If you just want to see a table, you can have higher-dimensional data that fits into a table and doesn't really work in a chart. You can also easily add a total line, or if you were comparing Q1 and Q2, you can add a difference line very easily.

**Michelle:** So you just said you can compare, like Q1 versus Q2. Can you compare different things with previous years? So we do a lot of things where we look at this month this year versus this month last year — like provider, how many patients did they see in 2026, 2025, 2024?

**Arthur:** Yes.

[Arthur attempts a year-over-year comparison query. The agent struggles with it.]

**Arthur:** I'm fumbling around a little bit here. Trust me, it's possible. But if you would like to see a more customized demo for the kinds of things that you want to report, I'm happy to spend some time and make sure those reports are fully baked for our agent. Frankly, I haven't worked with this dataset in a while, and I would love to produce exactly the numbers you need to see and then show you that it's generalizable. Because our goal is not to —

**Aaron:** So all the data and everything that we would want to inquire about — everything is basically, you have to type in what it is you're looking for? So we would have to learn and understand what words to be using, what to inquire?

**Arthur:** Yeah, and that sounds like a learning curve, but actually, in the end, it's pretty — I've used Tableau, Power BI, Domo. Compared to the kind of pointing and clicking you have to do in those platforms to get a report right, it's a lot easier once you get the hang of it. It's kind of more like magic words.

**Aaron:** How detailed can this potentially get? If I want to get into a couple different things — like various locations, by diagnosis, what we're collecting on diagnosis, what insurance companies are paying in comparison to each other — is that all capable?

**Arthur:** Absolutely. That is actually — some display things like comparing two months or year-on-year statistics require a lot more nuance. But the basic filtering on multiple dimensions, it does very handily. Filtering and sorting. And one thing we have is parameterization, so it allows you to create a report that can be custom-filtered on demand.

**Aaron:** I don't have any other questions at the moment. I think I personally just need to digest. Probably regroup with Aaron — yeah, same.

**Arthur:** Sure. And we're happy to set up a trial for you if you would like. You can put real data in — and we can't connect directly to the ModMed API right now, but you could certainly put in whatever data you need. Or if you want to sign an NDA and would prefer to see some reporting that comes directly out of the system, completely transparently, I'll show you how I generated all the reports. Or even if you want us to generate a demo set around that, or you have some demo data, if you'd rather not put live or real data in.

**Aaron:** What is the pricing structure for this?

**Arthur:** So for smaller installs, we charge $40 per month for an annual contract or $50 a month if it's monthly, per seat. That is for active users of the platform — people who will need to access the report generation capabilities. We have a two-seat minimum in order to allow you to share reports with users who aren't paid users. So for one seat, you get a system you can use yourself and you can forward a report to somebody. But if you want the full federated distribution of data to all the stakeholders who might want to see it, you get live dashboards and report sending with two seats.

**Aaron:** Okay, so if Michelle and I just want access, we want to be able to generate whatever data we want to generate and print and review, just her and I — is it $100 a month then?

**Arthur:** Yes, for monthly. And then for annual, we discount it somewhat.

**Aaron:** Okay. Well, I appreciate it. Let me chat with Michelle and then we will circle back.

**Arthur:** Great! Thanks!

**Aaron:** Nice meeting you! I appreciate your time.

**Arthur:** Likewise! Thank you!
