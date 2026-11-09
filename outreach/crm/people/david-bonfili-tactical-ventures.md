---
person_id: david-bonfili-tactical-ventures
contact_id: 47
name: David Bonfili
role: Managing Partner
company: Tactical Ventures
account:
relationship: inner_circle
category: advisor
era: college
---

# David Bonfili

**Role:** Managing Partner, Tactical Ventures
**Focus:** Defense and dual-use technology
**Relationship:** College friend (Harvard); LinkedIn connection since Dec 2012
**CRM:** contact_id 47 — category `advisor`, proximity `inner_circle`

## Background

- Rhodes Scholar
- Navy ROTC → intelligence
- Operations executive at Two Sigma Investments (quantitative hedge fund)
- Now invests in / works on defense and dual-use technology

## Interactions

- **2026-11-04 — demo + feedback call (~29 min+).** First half was a live demo; the
  recorded portion is the Q&A that followed. See
  [transcript](../../meetings/2026-11-04_david-bonfili_transcript.md).
- Prior CRM state was a standing to-do from 2026-08-12 ("Reconnect and share
  Dashbud") — now closed by the Nov 4 call.

## What he probed on

He asked sharp questions. The two areas he pushed hardest:

1. **Zero data exposure.** How Dashbud achieves it architecturally — the product as a
   passthrough that does its job while never storing customer data. Arthur's framing in
   the call: the agent lives inside a control plane with no ability to see underlying
   data, loosened slightly for semantic modeling, then writing SQL against a metadata
   description only.
2. **"Why Dashbud" vs. raw AI workflows.** If you can just point Claude at an API, what
   is the value add? Most of the call went here, and the answer that carried it was the
   **shared rules and governance layer** delivered through the workspace and semantic
   model — agreed-upon business rules set in advance, reusable and supportable, rather
   than one-off analyses you have to reverse-engineer later.

He also pressed on who the customer is (Arthur conceded the breadth is the weak spot),
the cost model, and whether a business in practice wants *supported data analytics* or
wants someone to come in and plan the agentic transformation of whole functions —
marketing, accounting, analytics — as a menu.

## The specification / generation / validation frame

The most reusable thing to come out of the call. **David's contribution, not ours** —
he was relaying a mental model from **Tymofiy Mylovanov**, president of the Kyiv School
of Economics and former Ukrainian economy minister, who has been working out how to
integrate AI into the curriculum (including a concentrated summer bootcamp) and is using
this frame to do it. David didn't know whether Mylovanov has published it; unverified as
of 2026-11-04.

The frame, in three stages:

> What AI lets you outsource is the **generation** stage — the work you'd previously
> have done manually yourself. It does *not* let you outsource **specification** or
> **validation**. Those become materially *more* important, because if you don't specify
> correctly or validate appropriately, you have a good chance of both getting garbage
> out of generation **and not knowing that you did**.

David's application to Dashbud, close to verbatim: *one way of thinking about what
you're doing is providing pressure around specification and validation, that allows for
more effective use of generation without putting that burden wholly on every individual
user.*

**Why it's better than the governance framing.** "Shared rules and governance" is a
feature argument and invites a feature rebuttal. This is a claim about what AI
categorically cannot do: collapsing the cost of generation *raises* the relative value
of the two stages either side of it. On this framing Dashbud doesn't compete with the
model — it supplies the stages the model can't. The semantic model is specification,
institutionalized. Auditable SQL is validation, institutionalized.

It also answers the breadth problem David pressed on: the qualifier isn't an industry,
it's *organizations where more than one person has to agree what a number means*. And it
bears on pricing — as a reporting convenience you're a $100/mo seat; as the layer that
makes everyone else's generation trustworthy, the unit of value is the organization.

**The thin leg, to avoid overclaiming.** Specification is strong — the semantic model
genuinely is that. Validation is weaker than the framing implies: auditable SQL makes a
number *checkable by a human*, it doesn't check anything itself. Adopting this language
invites "so how do you validate?", and the honest answer today is that we make
validation possible, not automatic. A wrong definition still produces wrong numbers —
but consistently and visibly wrong, which is recoverable, rather than variably and
silently wrong, which isn't. Metric assertions and reconciliation checks are the
roadmap opening here.

**Attribution note for anyone reading the transcript:** the Lovable anecdote at ~18:56
(a company that handed out unlimited Lovable tokens, everyone built their own data apps,
all saying different things, head of CX/analytics going nuts) is **Arthur's**, told just
before. Mylovanov's frame via David lands at ~19:46 as an abstraction *of that example*.
The diarization reverses speakers in this stretch — do not trust the labels, and note
that reversing these two inverts the meaning of the exchange.

A worked example of the frame applied with and without Dashbud (revenue per provider at
a multi-location derm practice) was developed on 2026-11-04 — see conversation notes;
candidate copy line: *AI made the work cheap. It didn't make deciding what's correct any
easier — and that's now the whole job.*

## Why he matters to Dashbud

- **Governance-first buyer instincts, from the defense side.** His defense and dual-use
  work is the through-line here — it shapes both how he reads the product and why the
  zero-exposure question is the one he went at hardest. That market is as
  data-sensitive as they come, so his questions are a good proxy for how a
  security-minded buyer interrogates the claim. Worth reusing his framing when it gets
  written up. (He also spent time as an ops exec at Two Sigma Investments.)
- **Offered intros.** Closed the call saying he'd think about people to get Arthur in
  front of — [[follow-up]] owed.
- Related: the trust/auditability angle in the website positioning work, and the
  "why not just use Claude directly" objection that needs a durable answer.
