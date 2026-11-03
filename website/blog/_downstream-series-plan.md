# "Downstream" — blog series plan

**Status:** Working plan, revised 2026-11-03. Five posts to start. Arthur writes; this is the argument map, not copy. Ticket: MKT-68L (will renumber on push).
**Section:** New blog section, slug `downstream`, alongside Data Analytics. Needs a Sanity section entry.
**Companion:** `_downstream-space-map.md` for the layers between the model and business value.

Convention in this doc: blockquotes are Arthur's words, verbatim, from the ticket and the Nov 2–3 conversation. Unquoted text is Claude's elaboration and can be cut.

---

## Origin

> At dashbud, we are somewhat critical of the big labs' efforts to create business applications. Fundamentally -- not their strong suit. I don't want to piss anyone off, but I think we can talk about the opportunities downstream of model development as a place (where we live, and) that is ripe for independent development.

> Yes, let's do just five to start. Please feel free to cogitate on this as much as you need to. It's a complex space to feel out.

> And don't feel like you need to flesh the posts out. Focus on feeling out the space: control plane, memory plane, etc.

## The frame (ticket summary, Arthur's text)

> New blog section and theme exploring the proposition that the value of AI in business is downstream of the model: in the control plane and other aspects of the execution harness. Critical of the labs' business-application efforts on structural grounds -- avoid criticizing them on competence. Highlight the value of independent developers in the ecosystem -- i.e., where Dashbud lives.
>
> Unifying idea: **the skipped step.** The "let the model handle it" framework skips an important step: asking the model to handle the entire vertical process cuts out an important step: where someone with a stake decides what matters.
>
> We distilled this position by exploring recent developments in model memory. Google's "Sleep" framework and other labs' efforts to enhance medium-term model memory are interesting and may be promising long-term, but they not only lack 1. a grounded, near-term deployment approach, but also, 2. attention to the subtleties of relevance.

How the skipped step surfaced, in the conversation:

> That prioritization argument is absolutely spot-on. Trust the model to know what to keep... yeah. Generalizes to the whole ballgame. Jumps a step. Exactly.

Claude's gloss: the model can execute the decision; it cannot make it, because mattering is a property of the stakeholder, not of the content. The labs skip the step because it is the one thing that doesn't scale. Downstream is the step.

## Tone guardrails (ticket, Arthur's text)

> - Structure, not competence. Never "they can't."
> - No lab's name in a headline.
> - Credit upstream in every post.
> - Argue from design principles with at least one non-Dashbud example each.

Added from the conversation:
- Plain words. Say what happens before naming it. No infrastructure vocabulary (Arthur on "execution guarantees" and "lineage": "a very opaque way of describing things").
- Humility where earned. Arthur, on AI-native UX: "not something the labs have any track record on. In fairness, very few people do."

Note on the word: in ML, "downstream tasks" are what a model is adapted to after pretraining. The overlap is deliberate. Define it in one paragraph in the opener.

---

## The five posts (titles verbatim from the ticket)

### 1. Downstream / The Skipped Step (opener)

Defines the term and the position. The skipped step is the argument; see the frame above for Arthur's statement of it.

Open decision (ticket): "Opener thesis: utility analogy as hook with the skipped step as the argument, or skipped step alone." The utility analogy: the model as electricity; the money and meaning end up in what's built on it.

Claude's note: the post most likely to read as sour. Lead with gratitude, say once that this is where Dashbud lives, end with "weigh it accordingly."

### 2. Model memory and data access require custom work because of the diversity of data environments and hierarchy of relevance.

Arthur, on the state of the memory plane:

> I really don't know what the labs are doing on the memory plane. It seems like... nothing? But I use claude code/cli exclusively, though I've built on it via the SDK. I see Oracle (Richmond Alake) and probably others are building in this direction. Love RA's content, but he is 50% selling oracle enterprise services. The other half of his content is DiY memory layer development, which seems more promising as a market direction.

> BTW I just read Google's Sleep article and it seems at least 2 years away from global deployment. Architecturally very distant from SOTA mass-market offering.

> And who knows whether thats' really the best approach. Yes, HOPE+1. Continuous incorporation of context as a medium-term memory via special fine-tuning is... not close.

Ticket log: "2026-10-31–11-02: 6h research into AI memory, agent and non-agent approaches (2h Sat, 3h Sun, 1h Mon am). Informs the memory plane and the candidate sixth post."

Claude's elaboration: "hierarchy of relevance" is the skipped step applied to data: someone has to decide what the model may see, what the fields mean, and which number is the real one. Memory splits three ways: personal (the labs own it, and it's thin: in Claude Code, a markdown file the user curates), agent memory (crowded: memory-layer startups and database vendors, mostly storage and retrieval), organizational (nearly empty: what the company has agreed is true, written by people after an argument). A memory layer stores what was observed; a semantic model records what was decided. In-weights memory is the form of memory a business can least audit: it cannot answer who decided this, when, and can we roll it back.

Dashbud example: the AI writes the query from schema and business rules and never sees a row. Non-Dashbud example: any team can build that pattern; the model authors, the database runs.

### 3. Orchestration: many gardens and many flowers blooming

Arthur:

> I think you got the orchestration one -- the first framing, but I believe it could also apply to agent coordination... the point is that each agent or tool has a specific surface with its own agreed-upon role and governance. So Dashbud's workspace API as a governance layer: a way agents can either build their own reports or use ones built by humans -- based on shared definitions and governed access.

The first framing, for reference: the downstream world will be plural, many domain-specific gardens that agents visit, rather than one orchestration layer that wins. Both readings hold at once: one principle at two scales.

On the title:

> I didn't know the flowers got hosed in the end, so maybe we have to change that wording.

The Hundred Flowers campaign (1956) invited open criticism and purged the people who offered it within a year. Candidate: "many gardens, many gates." Gardens have walls and gates, which is the point.

Claude's elaboration: an agent arriving at the workspace gate can consume reports humans built, or author its own inside the same definitions and scope. Either way it is a colleague with the same permissions as a person in that role, which is the first time "agent" has meant something a compliance officer could sign.

### 4. AI UX and UX for AI: supporting human users and networked integrations

Arthur:

> But don't undersell the value of AI-native UX. It's a moving target, and again, many of the questions involve governance: do I trust Grokbot to read all my emails? I don't, and right now that is preventing me from using it. But also redefining the UX around AI capabilities is just new, and again, not something the labs have any track record on. In fairness, very few people do.

Claude's elaboration: the two halves meet at consent granularity. The refusal isn't of the capability; it's of the scope, because "all" is the only scope on offer. The UX that unlocks it is a scoping UX: these senders, this label, this date range, read but never send. The labs ship all-or-nothing consent because granular consent doesn't scale and because they'd rather have the data. The UX innovation that matters most is the scope dialog, not the chat box. A Dashbud workspace is a scope dialog turned into a product object.

Open UX questions worth naming: when the model should ask vs. act; how to show where a number came from without leaving the page; whether the artifact or the conversation is the unit of work; how a person corrects what the model believes. Dashbud has opinions on a couple and no track record on the rest.

Home for "same question, same answer": the first promise an interface for AI has to make. Use the model to author the query once; run it conventionally. The model is a compiler, not a runtime.

### 5. The future model capability path

Arthur, on the earlier framing ("What the Model Will Eat, and What It Won't"):

> Ok, good theme. I'll reframe it. Thanks.

Arthur, on the optimistic close:

> Sorry to go way out there but I was just thinking... a possible solution is a kind of organziational metaprogramming. If I give you a coding agent that knows how to build a personal/organizational memory system, then you work with it to develop the priority-based system that your use-case demands. That's not a content focus for us, but it might be a kind of optimistic fallback. I'm not negative on the whole enterprise. Hell if I was we wouldn't be talking about this now.

Claude's elaboration: much of today's downstream work will be absorbed upstream (connectors, prompt tricks, retrieval plumbing, chat interfaces), and the labs will be right to do it. What won't be absorbed is anything that encodes a decision by someone with a stake. Practical close: would this still matter if the model were ten times smarter? If yes, build it. If no, the model will have it next year.

On in-weights memory: every proposal for memory inside the model has to answer who curates it, who can see it, and who can undo it. None do yet; those questions are the organizational layer restated.

On metaprogramming: the coding agent doesn't decide what matters; it makes it cheap for the person who does to encode, test, and revise it. Dashbud's modeling agent is this in miniature. Arthur's own setup (memory files, CLAUDE.md, SDK runner, Jira CLI) is a priority system built with a coding agent, and its failure mode is the predicted one: a stale team line persisted ten months because nobody owned curation. Tools lower the cost of the step; they don't supply the authority. The labs' coding agents are the best thing that has happened to downstream builders. Admit that some of what Dashbud has built will be eaten too.

---

## Recurring case

Michelle Maynard, Trillium Creek Dermatology. Arthur:

> She's the one we wrote the send-off letter to, explaining gently why Dashbud may do some things she needs, even if she doesn't know it now.

Primary report runner at a five-location practice; declined Dashbud for ChatGPT having never logged in. A competent personal solution the organization doesn't own. Pre-fork customer: no dueling report, PHI scare, or broken export yet, so no stakes for a downstream product to hold. The model wins the pre-fork market, and that's fine. Use anonymized. The send-off letter is at `sales/deals/trillium-creek/correspondence/2026-09-21_michelle-decline-and-response.md`.

## Order and cadence

1 → 5 as written. Every other week at most; quality over quantity. Each post gets LinkedIn and X cuts at publish time, with the canonical version on the blog and the LinkedIn post standing alone without a link.

## Open decisions (ticket, Arthur's text)

> - Opener thesis: utility analogy as hook with the skipped step as the argument, or skipped step alone.
> - Integrating "The Vibe-Code Mirage" (existing draft) is a companion to post 3 or stands alone.
> - Candidate sixth post, "Memory Is Not a Database Feature," vs. bench item "The Semantic Model Is the Product."

## Bench (not in the first five)

- The Vibe-Code Mirage (existing draft)
- Memory Is Not a Database Feature: the memory-layer market is solving storage for a problem that is about agreement and authority
- The Semantic Model Is the Product
- Your Cloud, Not Theirs: deployment as the quietest moat
- Build for the Agents: an API that models can call is the right shape for a downstream product

## Relation to existing content

"The Lost Promise of Business Intelligence" is about why BI didn't deliver. Downstream is about why AI won't deliver it either unless someone does the specific work. The opener should link back to it as the prequel. All posts link to /why-dashbud (see MKT-67).
