---
title: "Trial: OpenAI work-data offering, Google Analytics connector"
project: diy-ai-reporting
type: trial
status: raw
created: 2026-11-11
author: Arthur
annotated_by: Claude
n: 1
outcome: abandoned
visibility: private
---

# Trial: OpenAI work-data offering, GA connector

First-hand. Arthur attempted to connect Google Analytics to OpenAI's work-data
product and abandoned the attempt. Recorded here because it is a trial by
someone at the top of that product's competence range, and it still failed.

## What happened

- Attempted the **Google Analytics connector**.
- Got an **opaque error. Twice.**
- Quit.
- Separately, formed the impression that the product **was looking at his data**,
  and in his words "ran screaming."

Sequence and causation between the error and the privacy impression are not
fully recoverable; see open questions.

## Observations

### 1. It failed at the door, so the actual product was never evaluated

The failure was in connecting a source. No analysis ever ran. Whatever the
product does well or badly with business data is still unknown to him — and
would be unknown to any user who stopped at the same place.

For a competitor this is worth holding loosely: we have evidence about the
onboarding, not about the analysis.

### 2. Two opacities, same shape

- **Opaque about the data**: could not tell what it was doing with what it could reach.
- **Opaque about the failure**: could not tell whether the error was his fault,
  Google's, or OpenAI's.

Both are the user being unable to see inside. The second one is what ended the
trial; the first is what made him unwilling to push through it.

### 3. Trust is a multiplier on patience, not a separate feature

A user who trusts a tool will debug it. A user who is uneasy treats the first
failure as a reason to stop. Two errors is a very low abandonment threshold —
plausibly lower than it would have been without the privacy impression.

This is the same pattern Arthur described about Grokbot and email access
(2026-11-03): the capability was never refused, the **scope** was, and the
refusal ended the evaluation before the capability could be judged.

### 4. The buyer could not make the safety call — and he is the sophisticated case

Arthur builds on these APIs and runs an analytics company. If the product's data
handling was not legible to him in the time he gave it, it is not legible to a
practice administrator or an operations lead. "Is it safe" and "can the buyer
tell it is safe" are different questions and only the second is the vendor's to
lose.

### 5. Invisible to the vendor

From OpenAI's side this looks like a connector error and a drop-off, not a trust
failure. Nothing in the telemetry distinguishes "couldn't" from "wouldn't."

## Open questions

- Which offering exactly (ChatGPT Business/Enterprise, Projects, "company
  knowledge," something else) and roughly what date?
- What did the error actually say?
- Where did the impression that it was reading his data come from — the OAuth
  consent screen and its scopes, something in the UI, or something it said?
- Was any other connector tried, or GA only?

## Caution

n=1, and it is our own founder, who is not a neutral evaluator of a competing
product. Useful as a hypothesis generator and as a concrete anecdote; not
evidence about the product's quality.
