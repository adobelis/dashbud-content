# Why we built Dashbud

Dashbud is an AI-powered analytics platform.

Our founders spent years analyzing data and building custom data solutions, which we love.

What we *didn't* love was rebuilding the same infrastructure for every project and client. Connect to data sources, clean the data, model the business rules. Even building flexible reporting components can lose its luster after a while.

So we built the platform we wished we had: to handle data plumbing, codify business rules, write accurate queries, and leave us more time to focus on analysis and insights.

That product is Dashbud. Dashbud is your AI data engineer and the embedded AI analyst on your team, who knows your data inside and out and can configure dynamic charts, too.

You ask the questions, and Dashbud knows how to get the right answers from your data.

---

## What we believe

### Business data has come a long way, but access is still uneven

Twenty years of investment in data infrastructure has produced significant results. Many organizations have clean shared resources, embedded analysts, and automated pipelines. But for many others, the data landscape is **still bottlenecked.** Getting answers means filing a ticket, getting special access, or spending hours pulling exports and cleaning them in Excel. This friction is a drag on productivity and a cost to data-savvy people, who must either wait or take on data wrangling in addition to the rest of their work.

### Reliable analytics requires a system, not just an agent

**AI to the rescue? Yes, but not on its own.** An AI agent can write a script to pull from an API and answer a question or deliver a report. But for that report to be trusted as a resource, it needs to follow shared business rules, and must be auditable and reproducible. And data access must be managed even more carefully when AI is the client. Managed self-service — centralized data and governance, federated analysis — works. AI makes it affordable for organizations that could never justify the cost before.

### AI should be applied from the bottom up

AI's most reliable role in analytics is encoding data semantics and business rules, then applying that knowledge to answer questions with accurate, sourced analysis. These two levels deliver **immediate, verifiable impact.** Higher levels — synthetic reports, autonomous analysis, decision-making — are real possibilities, but each requires more oversight and carries more risk. It's best to start where the value is certain.

### Privacy must be encoded in architecture, not policy

**Institute privacy by design.** If AI never touches your raw data, you don't need to trust it not to leak or train on it. The agent should serve primarily as a translation layer: business questions in, correct queries out, based on metadata and business rules. Higher-level AI roles that process data directly may be valuable, but they shouldn't be mixed into your core data access infrastructure.

---

## Who we are

**Scott Binger, co-founder.** Scott has been building data management and analytics solutions for over fifteen years. He's designed and deployed custom platforms for clients in healthcare, consumer goods, financial services, and many multi-site operations. This work in data solutions was the impetus for creating Dashbud.

**Arthur Dobelis, co-founder.** Arthur leads product strategy, engineering, and marketing. His background is in mathematics, computer science, and law. He's been the "data wonk" at multiple organizations: the person who ends up pulling exports and building reports because they're the one who can. Dashbud is shaped by that experience.

You can reach us at **hello@getdashbud.com** or [book a conversation](https://calendly.com/arthur-evolytix/dashbud-demo-and-setup).

---

## Build Spec

**URL:** `/about`
**Nav label:** "About"
**Nav position:** after Pricing, before Blog → **Why Dashbud? | Who It's For | Pricing | About | Blog**

**Design:** This is a reading page, not a product page. Different register from the rest of the site.

- No hero section, no gradient background. Title and straight into text.
- Comfortable reading width throughout (max-w-3xl).
- Title: "Why we built Dashbud" as h1 with gradient text on "Dashbud".
- Opening paragraph ("Dashbud is an AI-powered analytics platform.") at text-xl, rest of intro at text-base.
- "What we believe" section: four conviction blocks with teal left border, teal h3 headlines, body in text-base gray. Each has one bold phrase.
- "Who we are" section: founder names bolded in gray-900, bios as inline text.
- Contact line at the bottom: quiet, just links. No CTA banner.

**Content source:** This file (`content/website/pages/about.md`) — everything above this spec section is the page copy. Astro file is the live version and may be slightly ahead.
