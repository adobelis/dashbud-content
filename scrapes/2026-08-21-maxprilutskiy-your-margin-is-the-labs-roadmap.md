---
title: "Your Margin Is the AI Labs’ Roadmap"
url: https://maxprilutskiy.com/p/your-margin-is-the-ai-labs-roadmap
author: Max Prilutskiy
published: 2026-08-21
fetched: 2026-11-02
method: http
chars: 13019
---

_Why “just a GPT wrapper” is the best way to start a company — and the token reseller test that tells you if yours will survive._
# Your Margin Is the AI Labs’ Roadmap

### Why “just a GPT wrapper” is the best way to start a company — and the token reseller test that tells you if yours will survive.

Max PrilutskiyAug 21, 2026

Jeff Bezos has a famous line: “your margin is my opportunity.” It’s usually quoted as a threat Amazon makes to everyone else. If you’re building an AI startup, you need to hear it the other way around: *you* are the “everyone else.” Every dollar of gross margin you make on top of a foundation model is a line item on someone’s roadmap in San Francisco — and, highly likely, they have more GPUs than you.

Sam Altman said this part out loud. Asked in 2024 which startups OpenAI would run over, he described companies that “assume the model is not going to get better” and build little things on top: “when we just do our fundamental job... we’re going to steamroll you.”Not because we don’t like you. Because we have a mission.

So here’s the standard advice you’ll get: don’t be a wrapper.

The standard advice is wrong. Being a wrapper is the best way to start a company in the history of starting companies. You just have to understand which of the two wrapper species you are — because one of them compounds and the other one is already dead. The debate has heated up this month — VCs are publishing “the wrapper is dead” and “revenge of the wrappers” essays in the same news cycle — and both camps are right about their half of the evidence. The two-species distinction is what reconciles them.

## What is an AI wrapper, really?

An AI wrapper is a product whose core capability comes from someone else’s model, accessed through an API. That’s the definition, and by that definition the insult falls apart immediately, because it describes almost every great software company at founding. Stripe wrapped banking rails. Every SaaS company you admire wraps AWS.

When a VC told Perplexity’s Aravind Srinivas “you’re just a wrapper, so tell us how are you going to build it?”, his answer wasn’t to deny it. It was that “at the end, most successful businesses are wrappers of some form” — Coca-Cola, he pointed out, is a wrapper around refrigeration and distribution. Perplexity is now worth about $20 billion.

The receipts on this are not subtle:

- Cursor was dismissed on Hacker News as “like a wrapper for some APIs” with “no moat”, and at launch as “just a VS Code fork.” It went from ~$100M ARR in January 2025 to $500M by Juneto a $1B run-rate by November — the fastest-growing startup in history. Slack took ~4 years to do what Cursor did in ten months. And this August, SpaceX bought it for $60 billion in stock — the largest startup acquisition of the year, double its last private valuation. That’s not a paper mark; it’s a price someone actually paid. Nobody pays $60B for a markup on tokens.
- Harvey, the “ChatGPT for lawyers” wrapper, passed $350M in annualized revenue and is reportedly raising at a $15.5 billion valuation — up more than 5x in eighteen months.
- Cognition’s Devin went from $1M to $73M ARR in nine months on less than $20M of lifetime burn.
- Lovable crossed $100M ARR eight months after launch.

Stripe’s founders, who see the payments data for the top 100 AI companies, put a number on the pattern: top AI startups reach $5M ARR in 24 months versus 37 for the best SaaS cohort ever, and “some people have called these startups ‘LLM wrappers’; those people are missing the point.”

So no — “wrapper” is not the problem. Here is the problem.

## Why do AI wrapper startups fail?

There is a second kind of company that looks identical on day one: the **token reseller**. Its product is the model’s output plus a markup. Its roadmap is the provider’s roadmap with a delay. Its margin is, in the most literal sense possible, the provider’s opportunity.

You know these companies by their obituaries:

- Jasper wrapped GPT-3 into a copywriting tool, reached $75M+ ARR and a $1.5B valuation — then ChatGPT shipped the same capability for free, and within a year Jasper had cut its ARR forecast by 30%+, laid off staff, and slashed its own internal valuation.
- And Jasper is the famous one, not the rare one. Analysts project roughly 80% of AI wrapper startups fail by end of 2026, and the average wrapper churns 65% of its customers within 90 days — double the SaaS norm. Just this month, Zams shut down after seven years; its founder’s post-mortem: “the application layer went from differentiated, to crowded, to indistinguishable.” So when someone tells you most wrappers die, agree with them. Most wrappers are token resellers. That’s not the counterargument to this essay — it’s the mechanism.
- OpenAI’s November 2023 DevDay added PDF upload to ChatGPT and erased an entire class of PDF-chat wrappers in one keynote. “OpenAI killed my startup” became a meme that week.

And the species is not extinct — it has just raised more money. There are venture-backed companies today, in unglamorous categories, whose entire mechanism is reselling frontier-model API calls at a markup to customers who haven’t yet realized they could go direct. Consultants who audit AI vendor bills report markups of 3x to 50x over raw API cost: “they’re literally just reselling OpenAI with a wrapper.” I’ve watched this up close in my own market. It works — right up until the customer gets educated or the provider ships the feature, whichever comes first. Both are on someone else’s schedule.

Which gives you the **token reseller test**:

> **If tokens were free tomorrow, would your customers still pay you?**

If yes, you’re a company that happens to buy tokens. If no, you’re a distribution arm of a foundation-model lab, and you don’t set your own prices — or your own lifespan.

Field notes from building a YC startup. Subscribe free to get them by email.

The wrapper companies that won all pass the test. Nobody pays Cursor for tokens; they pay for an editing experience wrapped around the models, and switch models underneath without noticing. Nobody pays Harvey for GPT output; a16z’s analysis of why incumbents can’t catch app-layer companies lands on exactly this: “if Harvey deeply understands how a particular law firm structures its work... there is simply no way a new entrant can replicate that overnight.”The model is fungible underneath; the system of work is not. That’s the moat — and it’s why the platform risk everyone warns you about only kills one of the two species.

And what builds that system of work? Not better prompts. Customer conversations. The quality bar in every real domain — what “good” means to a law firm, a dev team, a hospital — isn’t in any training set. You collect it one call at a time, and it compounds into the only asset the model provider’s roadmap can’t ship: knowing exactly what your customer needs the model to do.

## What do falling inference costs mean for your startup?

Here’s where it gets good, because the same force that kills token resellers is the biggest subsidy ever handed to real companies.

The price collapse is not a rumor; it’s the most reliable curve in the industry. a16z measured GPT-3-level capability falling from $60 per million tokens to $0.06 in three years — a 1,000x drop they named “LLMflation.” Stanford’s AI Index clocked GPT-3.5-level inference falling 280-fold in 18 months. Epoch AI, tracking fixed capability milestones, found prices falling 9x to 900x per year depending on the benchmark. This July, OpenAI cut GPT-5.6 Luna’s price by 80%, three weeks after launch, mid-price-war with Google and everyone else’s cheap tier.

But look closely at that July announcement, because it contains the most important pricing fact in this essay: while Luna fell 80%, GPT-5.6 Sol — the frontier model — stayed at $5/$30 per million tokens. The same list price as the frontier model before it, and the one before that.

There are two different prices, and they behave in opposite ways:

1. **The price of a fixed capability** — “a model that clears my quality bar” — falls relentlessly, because every year more suppliers hit that bar with smaller, cheaper models.
2. **The price of the best available model** never really falls, because “the frontier” is a different, always-premium product each year.

If your product requires “the best available model,” forever, you have opted out of the deflation entirely. If you can name the capability you actually need — and test for it — the deflation is yours. But nothing moves your traffic to the cheaper model for you. You have to know your bar, and go collect.

And here’s the catch that makes the whole thing a strategy rather than a coupon: **you only learn your quality bar from customers.** The bar is not a benchmark score. It’s the specific, unglamorous definition of “good enough” in your domain, and the only instrument that measures it is a customer conversation. This is why Srinivas could bet Perplexity’s whole existence on API costs “going down 2X every four months” — riding “a 10 to 100X reduction in cost for the same intelligence” — while the token resellers got no benefit from the exact same curve. The deflation flows to whoever knows precisely what they need. Everyone else pays frontier prices or resells at a doomed markup.

(If you’re wondering whether cheap tokens at least shrink the market: no. Jevons paradox — cheaper intelligence means radically more of it gets consumed. Your bill can still go up while your unit economics improve, because you’ll build things that were unaffordable last year.)

## Should you build on frontier models or cheap models?

Put the pieces together and the strategy for a founder starting today writes itself:

**Phase 1 — frontier to discover.** Start as a thin wrapper on the best available model, and don’t apologize for it. You’re not buying tokens; you’re buying discovery speed. New products become possible only at the capability edge — if your idea works fine on last year’s commodity models, someone built it last year. Pay the frontier premium happily. It’s the cheapest product R&D in history. One caution from the 2026 data: don’t count on open-weight models erasing the frontier for you — Epoch found the gap between open and closed models stopped narrowing this year, and cheap per-token prices routinely lie about the per-task cost once weaker models burn extra turns doing the same work.

One more caution, fresher: the frontier is rented, and the landlord is getting choosier. The Information reported this month that OpenAI and Anthropic may restrict — or silently degrade — API access to their best models, to prevent distillation and to favor their own apps. Canva just cut its revenue growth forecast after users defected to ChatGPT, and is migrating to smaller and open models mid-flight. Phase 1 is a lease with a demolition clause. One more reason not to linger.

**Phase 2 — commodity to deliver.** Every customer conversation converts frontier-dependence into a quality bar you can name. Once you can name it, you can test cheaper models against it, and the 10x-per-year price collapse becomes *your* margin expansion instead of your extinction event. This is the Bezos line running in reverse: now the model provider’s falling prices are **your** opportunity. Sequoia’s David Cahn made the macro version of this point: declining compute prices are good for startups, because value has to land at the layer that delivers it to end users.

The companies that die are the ones that never make the phase transition. The Jaspers stay in phase 1 forever — thin on top of whatever the provider ships, value proposition one keynote away from deletion. The token resellers are worse: they skip discovery entirely, arbitraging the gap between an educated and an uneducated customer. That gap only closes.

The companies that win treat the wrapper as a starting point with a countdown clock attached. A wrapper with deep customer adoption is not just a wrapper anymore — it’s a distribution channel, a data engine, and a product lab that the model provider cannot steamroll, because the thing customers pay for was never the tokens.

## Start as a wrapper, proudly

So when someone sneers that your startup is “just a GPT wrapper,” here’s the honest answer: *yes — for now, and on purpose.*

Ship the thin wrapper this week. It’s the best starting position any founder has ever been handed: frontier intelligence, rented by the token, no infrastructure, no research lab, no permission required. Then get on customer calls and start converting that borrowed capability into the one asset that isn’t on anyone’s roadmap — knowing your customer’s definition of good better than anyone alive.

And every quarter, run the token reseller test: *if tokens were free tomorrow, would customers still pay us?* The day the answer is no, stop building and go find out what they’d pay for. Because your margin is the model provider’s roadmap — right up until the moment you build something that isn’t made of tokens. After that, their roadmap is your margin.

This post is public. Share it if it’s useful.

Share
