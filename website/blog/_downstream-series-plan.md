# "Downstream" — blog series plan

**Status:** Proposal, 2026-11-02. Five posts to start. Arthur writes; this is the argument map, not copy.
**Section:** New blog section, slug `downstream`, alongside Data Analytics. Needs a Sanity section entry.

## The frame

The frontier labs' incentive is generality. A model that serves everyone has to be agnostic about any one business's schema, definitions, and trust boundary. Business applications are the opposite problem: they are made of the specific stuff. Nobody at a lab is wrong about this; it just isn't where their gradient points.

So the thesis: **the model is upstream; the value is downstream.** Most of what makes AI useful inside a business happens after the token comes out: grounding, governance, determinism, agreement on definitions, deployment. That work needs proximity to the customer, not scale, which makes it independent-developer territory. It is also where Dashbud lives, and the series should say so once, plainly, and then not pitch.

Tone guardrails, every post:
- Structure, not competence. Never "they can't."
- No lab's name in a headline. Products named only as examples, never as targets.
- Credit upstream. The models made this possible, and each post should carry a sentence that says so without flinching.
- Argue from design decisions, not from the product. Each post generalizes one principle that Dashbud happens to embody, with at least one example that isn't Dashbud.

Note on the word: in ML, "downstream tasks" are what a model is adapted to after pretraining. The overlap is deliberate and practitioners will hear it. Define it in one paragraph in the opener.

## The five posts

### 1. Downstream
*Series opener. Defines the term and the position.*

**Argument:** The frontier model is becoming a utility, and the history of utilities is that the money and the meaning end up in what is built on them. Electricity didn't make GE the only company; it made appliances an industry. The important AI businesses of the next decade will be built by people closer to the customer than to the model.

**What it draws on:** the one-pager's "promise vs. reality" framing, now applied to AI itself. The LinkedIn post's AI paragraph (opaque workflow, vibe code) as the symptom.

**Tone risk:** this is the post most likely to read as sour. Lead with gratitude and the utility analogy, which is flattering to the labs. End with "this is where we live, so weigh it accordingly."

### 2. The Model Shouldn't See Your Data
*First design principle.*

**Argument:** The most consequential decision in a business AI system is not which model you use. It is what the model is allowed to see. A model that works from schema, names, and rules, and never from values, can be trusted with regulated data; one that reads the rows cannot, however good it is. This is a trust-boundary decision, and a trust boundary is the one thing a general-purpose vendor cannot draw for you.

**What it draws on:** Trust & Privacy on Why Dashbud; the healthcare example from Who It's For. Generalize: the pattern is "model authors the query, database runs it, results go to the person." Any team can build that way.

**Tone risk:** sounds like a pitch. Keep Dashbud to one paragraph; spend the rest on the pattern and on what you give up (the model can't eyeball the data for anomalies, so you need other tools for that).

### 3. A Smarter Model Won't Settle What "Margin" Means
*Second design principle: agreement is not a model capability.*

**Argument:** The hard problem in business data isn't answering the question; it's agreeing on what the question means. Finance and sales define margin differently, and both are right. No amount of intelligence resolves a definitional dispute, because it is organizational, not analytical. It has to be settled by people and written down somewhere the model reads from. That artifact, the semantic layer, is downstream work by definition: no lab can ship your company's definitions.

**What it draws on:** "Herd the cats" on Who It's For; dueling reports; the vibe-code problem (every personal AI script encodes its author's private assumptions). The "Vibe-Code Mirage" piece already on Arthur's list fits here as a companion or a follow-up.

**Tone risk:** low. This one is almost universally agreed with; the risk is being boring. Lead with a concrete dueling-reports story.

### 4. Same Question, Same Answer
*Third design principle: the model is a compiler, not a runtime.*

**Argument:** Businesses run on numbers that are the same every time they're pulled. Language models are probabilistic by construction. The downstream move is not to make the model more reliable; it's to take it out of the runtime loop. Use it to author the deterministic artifact once (the query, the report definition), then run that artifact conventionally. Reliability debates about models mostly dissolve once the model isn't answering the question live.

**What it draws on:** "Deterministic reports" on Why Dashbud; the LinkedIn post's "answers your question differently today than last week." Generalize: code generation, infrastructure-as-code, and compilers all work this way already.

**Tone risk:** low. This is the most technical post and the one most likely to be shared by engineers. Keep one diagram: question → model → artifact → runtime.

### 5. What the Model Will Eat, and What It Won't
*The map. Keeps the series honest.*

**Argument:** A lot of today's downstream work will be absorbed upstream: prompt engineering, retrieval plumbing, tool wrappers, the connector of the month. Builders who stand there will be run over, and the labs will be right to do it. What won't be absorbed is anything that encodes a trust boundary, an organizational agreement, a liability, or a deployment constraint. A test for founders: would this still matter if the model were ten times smarter? If yes, it's durable downstream territory. If no, it's a feature the model will have next year.

**What it draws on:** posts 2 through 4 as the three worked examples of "still matters." The own-cloud deployment option as a fourth. Dashbud's agent API as an example of building *for* the upstream models rather than against them.

**Tone risk:** prophecy. Frame as a heuristic, give examples of things you expect to be eaten (including some Dashbud has built), and say so. That admission is what earns the rest of the series its credibility.

## Order and cadence

1 → 2 → 3 → 4 → 5 as a series arc: position, three principles, map. At the every-other-week cadence that's ten weeks, which is fine; each post stands alone and the opener can be published before the rest are written. Post 5 could move to second if the framework is wanted early, but ending on it is stronger.

## Bench (not in the first five)

- The Vibe-Code Mirage (Arthur's existing draft; companion to post 3)
- Your Cloud, Not Theirs: deployment as the quietest moat
- The Semantic Model Is the Product
- Build for the Agents: why an API that models can call is the right shape for a downstream product (the agent API module, generalized)
- Generality Is Their Business Model. Specificity Is Yours.

## Relation to existing content

"The Lost Promise of Business Intelligence" is about why BI didn't deliver. Downstream is about why AI won't deliver it either unless someone does the specific work. The opener should link back to it as the prequel.

## Arthur's reframe (2026-11-03, from the ticket)

The five posts as Arthur rewrote them. Supersedes the list above, which stays for reference. The shift: from five principles Dashbud embodies to a survey of the downstream landscape. Less exposed to the "vendor defending its niche" reading; room for things Dashbud doesn't do.

1. **Downstream / The Skipped Step** (opener)
2. **Model memory and data access require custom work** because of the diversity of data environments and the hierarchy of relevance. ("Hierarchy of relevance" = the skipped step applied to data, in plain words.)
3. **Orchestration: many gardens, many gates.** Both readings at once: ecosystem pluralism (domain gardens that agents visit, not one orchestration layer that wins) and agent coordination within a workflow. One principle at two scales: each agent or tool has a specific surface with an agreed role and its own governance. Dashbud's workspace API as a gate: an arriving agent can consume reports humans built, or author its own inside the same definitions and scope. Either way, a colleague with the same permissions as a person in that role. *Wording note: avoid "many flowers blooming"; the Hundred Flowers campaign ended with the flowers purged.*
4. **AI UX and UX for AI: humans and networked integrations.** Don't undersell. AI-native UX is a moving target and few have a track record, labs included. The two halves meet at consent granularity: Arthur won't let Grokbot read all his email because "all" is the only scope offered, so the capability goes unused. The UX that matters most is the scope dialog, not the chat box; a Dashbud workspace is a scope dialog turned into a product object. Open UX questions worth naming: ask vs. act; provenance inline (number → SQL); artifact vs. conversation as the unit of work; how a person corrects what the model believes. Dashbud has opinions on some, no track record on the rest; say so. Home for "same question, same answer" (model as compiler, not runtime) as the first promise an AI-facing interface must make.
5. **The future model capability path.** Softer than "what the model will eat." Home for the ten-times-smarter test as the practical close, and for the in-weights-memory point (the most ambitious memory is the least auditable).

Michelle Maynard (Trillium Creek) as the recurring case: a competent personal solution the organization doesn't own; pre-fork customer; the model wins the pre-fork market and that's fine.
