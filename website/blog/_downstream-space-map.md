# Downstream — a map of the space

**Status:** Thinking notes, 2026-11-02. Companion to `_downstream-series-plan.md`. Not copy. The point is to name the planes between the model and business value, say who owns each, and predict which the labs absorb.

## The organizing idea

Every plane below exists because someone has to hold a stake: a liability, an agreement, a trust boundary, a contract. Models don't hold stakes. Organizations do. That is the structural reason this work is downstream, and it is a better foundation than "the labs aren't good at business apps," which is contingent and will age badly.

A second lens: **personal vs. organizational** and **generic vs. specific**.

|  | Generic | Specific |
| --- | --- | --- |
| **Personal** | The labs' home turf: chat, memory, artifacts, personal agents. Fully upstream. | The mirage: personal AI scripts, vibe-coded reports. Works for one person, encodes private assumptions, doesn't survive sharing. |
| **Organizational** | Contested: enterprise admin consoles, org-wide connectors and search. The labs will push here and win the generic parts. | Downstream proper: definitions, scopes, lineage, deployment. Needs proximity to the customer. Independent territory. |

The series argues the bottom-right cell, and warns about the top-right one.

## The planes

Ordered roughly from the model outward. For each: what it is, Dashbud's instance, who owns it, and whether it gets eaten.

### 1. Control plane
What the model is allowed to see and do, and as whom. Identity, scope, permissions, tool allowlists, data boundaries, policy.

- **Dashbud instance:** workspaces; API keys scoped to workspaces; column exclusion and row filters; the agent works from schema and never from values.
- **Who owns it:** the enterprise wants to, and must. Labs offer org admin and SSO, which is the generic layer. They cannot know which columns are PHI or which team may see which region.
- **Eaten?** The generic shell, yes. The specific policy, no. This is the most durable plane because it encodes liability.
- **Inversion worth noting:** with agent APIs, the control plane *becomes the product's surface*. Dashbud's agent API is Dashbud acting as a control plane for whatever model the customer brings. Downstream products should expose themselves to the upstream models, not compete with them for the chat window.

### 2. Memory plane
What persists between interactions. Three kinds, and the series should insist on the distinction because everyone selling "memory" is blurring it:

- **Personal memory:** what the assistant remembers about you. The labs own this and it is thin: per-user memory in chat products, project folders, and in Claude Code literally a markdown file the user curates. No sharing model, no governance. Upstream, but not impressive.
- **Agent memory:** what an agent retains across sessions and tasks: episodic, semantic, procedural. This is the crowded layer. Memory-layer startups (Mem0, Zep, Letta), every database vendor retrofitting vectors and graphs, and the "memory engineering" DIY school (Richmond Alake's content is the best articulation). Mostly storage and retrieval machinery. Being built downstream because the labs structurally don't, which is evidence for the thesis.
- **Organizational memory:** what the company has agreed is true. Definitions, business rules, join logic, what `GL00100` means, which revenue number is the real one. Shared, versioned, governed, written by people after an argument. This is the semantic model. **Nearly empty as a market.** Downstream by nature, because the hard part is the agreement and the authority, not the storage.
- **Artifact memory:** saved queries, reports, dashboards. The compiled outputs. Downstream because they carry an audience and a permission set.

Key lines: personal memory makes the model better *for you*; organizational memory makes it *correct for the company*. A memory layer stores what was observed; a semantic model records what was decided. Retrieval vs. governance.

The agent-memory crowd are allies and integration partners, not targets. A memory layer could point at a semantic model as its source of truth for business terms. Say that in the post.

Possible post from this: "Memory Is Not a Database Feature." The memory-layer market is solving storage and retrieval for a problem that is actually about agreement and authority. Slots between posts 3 and 5, or replaces the bench item "The Semantic Model Is the Product."

Contested ground: labs are shipping enterprise search and connectors and calling it knowledge. Retrieval finds documents; a semantic model encodes decisions. Different things.

### 3. Data plane (grounding)
Connectivity to sources, schema discovery, imports, freshness, versioning, rollback.

- **Dashbud instance:** direct DB connections, Google Sheets, CSV auto-append from Drive, import tracking and rollback, the modeling agent that learns structure.
- **Split:** *transport* (connectors, MCP servers for every SaaS) is being commoditized and will be upstream. *Semantics* (what the source means) and *lifecycle* (what version of the data produced this number, can we roll back) stay downstream.
- **Eaten?** Transport, yes. Lifecycle and meaning, no.

### 4. Execution plane
Where the computation actually runs, and with what guarantees.

- **Dashbud instance:** model authors SQL once; the database runs it; results go to the person. Deterministic thereafter.
- **Principle:** the model is a compiler, not a runtime. Reliability debates mostly dissolve when the model isn't answering live.
- **Eaten?** Generic sandboxes (code interpreter) are upstream already. Execution against *your* systems of record, under *your* guarantees, with auditable artifacts, is downstream.

### 5. Assurance plane
Lineage, reproducibility, audit. "Every number has a source." Cross-cutting rather than a layer, but worth naming because regulated buyers ask for it first.

- **Dashbud instance:** every result carries its SQL; imports are tracked; same question, same answer.
- **Who owns it:** nobody upstream. Labs log the conversation, not the lineage of the number.
- **Eaten?** No. It's the paper trail for the stake-holder.

### 6. Presentation plane (consumption)
How results reach people who never touch a model. Dashboards, scheduled reports, shares, parameterized controls, audiences.

- **Dashbud instance:** saved results, boards, link sharing, interactive controls.
- **Labs' version:** artifacts and canvases, which are personal and ephemeral.
- **Eaten?** Personal presentation, yes. Audience-aware, permissioned, refreshing consumption, no. It inherits from the control plane.

### 7. Deployment plane
Where all of the above runs. Residency, BAA, own-account, air gaps.

- **Dashbud instance:** push-button deploy into the customer's AWS account; Azure scoped.
- **Eaten?** Labs offer regions and enterprise tiers. They do not run inside your account. Quietest moat on the list and the one enterprise buyers ask about after security.

### 8. Agreement plane (not software)
The human process by which organizational memory gets written: who decides what margin means, how a definition changes, who signs off. Mostly workflow and governance.

Named here because it is the plane most products ignore and the one that determines whether the memory plane is trustworthy. Dashbud's answer today is "the semantic model, edited conversationally by people who agree." Thin, and honest to say so.

## What gets eaten, in one list

Upstream-bound, expect to lose it: personal memory, connectors as transport, sandboxes, chat UI, basic agent loops, artifacts for one person, prompt engineering as a discipline, retrieval plumbing.

Durable downstream: scoped control, organizational memory, data lifecycle, execution under guarantees, lineage, permissioned consumption, deployment into the customer's perimeter, and the agreement process behind all of it.

Founder's test, from post 5: would this still matter if the model were ten times smarter? Everything in the durable list passes. Everything in the eaten list fails.

## Where Dashbud sits

A downstream stack for one job, analytics, covering planes 1 through 7 and gesturing at 8. The agent API is the move that makes it a control plane for other people's models rather than a competitor to them. That is the shape the series should recommend to other builders: pick a job, own the organizational and specific planes for it, and present yourself to the upstream models as a governed surface.

## Open questions

- Is "memory plane" the right word for organizational memory, or does it concede too much to the labs' usage? Alternatives: "definition plane," "semantic plane." Memory is the more evocative word and the conflict with personal memory is a feature.
- Does the agreement plane deserve its own post, or is it a paragraph inside post 3? Leaning paragraph for now; a post when Dashbud has more to show there.
- The 2x2 might be the opener's one diagram.

## Addendum, 2026-11-02: in-weights memory

Arthur's read of Google's recent sleep/consolidation work: at least two years from mass-market deployment and architecturally distant from current offerings. Implication for the thesis:

- In-weights memory is the opposite of organizational memory. What consolidates into the model is opaque, unversioned, unauditable. It cannot answer "who decided this, when, and can we roll it back." The better the model remembers, the more a business needs an external, inspectable record to check it against.
- It targets the crowded layer (agent memory: storage and retrieval) rather than the empty one (organizational memory: agreement and authority). Confirms the eaten-vs-durable split from the architecture side.
- Timeline is a floor, not an estimate. Continual learning has consistency and safety problems that get harder at scale. Two to four years before it touches an enterprise deployment; longer before a regulated buyer trusts it.

Line for post 5: the labs' most ambitious answer to memory is to put it in the weights, which is precisely the form of memory a business cannot audit.

## The skipped step (unifying idea, 2026-11-02)

Arthur, on in-weights memory: "Trust the model to know what to keep... generalizes to the whole ballgame. Jumps a step."

The step: someone with a stake deciding what matters. What to remember, which definition is right, who may see what, whether this is the number we report. The model can execute the decision; it cannot make it, because mattering is a property of the stakeholder, not of the content.

The labs jump the step because it is the one thing that doesn't scale: prioritization is local, political, and changes when the CFO changes. Their architectures route around it, so the result is systems superb at the part after the decision and silent on the decision itself.

**Downstream is the step.** Not plumbing around the model; the place where someone with skin in the game says what counts.

Restates the planes:
- Control plane = who decided what the model may see.
- Memory plane (organizational) = who decided what is true.
- Assurance = show me the decision and its history.
- Agreement plane = the process by which the decision gets made. Now clearly central, not an afterthought.

Restates post 5's test: if what you're building *is* the skipped step, it survives. If it's execution, the model gets it eventually.

Candidate opener thesis, replacing or preceding the utility analogy. Working title: "The Skipped Step." Keep "Downstream" as the series name.

## Organizational metaprogramming (optimistic close, 2026-11-02)

Arthur's proposal: give an organization a coding agent that knows how to build personal/organizational memory systems, and the organization works with it to build the priority-based system its use case demands. Not a content focus; an optimistic fallback. "I'm not negative on the whole enterprise."

Why it's consistent with the thesis: the skipped step is still taken by a human. What changes is the cost of taking it. The agent doesn't decide what matters; it makes encoding, testing, and revising the decision cheap. That is the path by which mid-market companies without data teams get organizational memory at all.

Evidence it's more than a fallback:
- Dashbud's modeling agent is this in miniature: it proposes the semantic model from the schema; people confirm and correct conversationally; the governed artifact is the output. Organizational metaprogramming scoped to analytics.
- Arthur's own setup (memory files, CLAUDE.md, SDK runner with hooks, Jira CLI) is a priority system built with a coding agent. Its failure mode is the predicted one: the stale team line persisted ten months because nobody owned curation. Tools lower the cost of the step; they don't supply the authority.

Limit: bespoke systems per org risk the vibe-code problem at company scale unless the builder agent works from shared primitives: versioning, provenance, scoping, review. Those primitives are the downstream planes. The builder is generic and the labs will ship one; what it builds is organizational and specific and stays downstream.

Placement: closing paragraph of post 5. Also where the gratitude lands honestly: the labs' coding agents are the best thing that has happened to downstream builders, because they make the skipped step affordable.
