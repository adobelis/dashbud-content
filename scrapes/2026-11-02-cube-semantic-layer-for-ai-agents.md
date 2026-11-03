---
title: "Semantic Layer for AI Agents (2026) | Cube"
url: https://cube.dev/articles/semantic-layer-for-ai-agents-2026
author: 
published: 2026-11-02
fetched: 2026-11-02
method: http
chars: 20432
---

_Why AI agents need a semantic layer, not raw text-to-SQL — governed metrics, compile-time governance, and MCP — and how to give an agent one in 2026._
Articles

To stop an AI agent from hallucinating metrics, do not ask the model to decide what a metric means. Give it certified metrics, known join paths, enforced permissions, traceable query results, and evals against known answers. A semantic layer supplies that governed business context. It prevents the agent from redefining revenue on every prompt; it does not make a language model incapable of misreading a result or inventing an unsupported explanation, so the answer still needs evidence and validation.

This is a concept-forward guide for data and platform engineers: why raw text-to-SQL falls short for agents, what a semantic layer actually changes, and how to give an agent one. If you are still deciding whether the layer is necessary at all, use the checklist for whether generative AI needs a semantic layer.

The churn analysis use case applies this pattern to a customer churn review, with metric definitions, a worked example, and MCP and CLI connection steps. For retention at equal customer tenure, see the AI cohort analysis use case.

## How to stop AI agents from hallucinating metrics

“Metric hallucination” usually combines two different failure modes.

The first is **metric-definition drift**. The agent guesses what revenue means, chooses the wrong join, ignores the reporting time zone, or changes the calculation between prompts. The SQL may be valid while the number is wrong. A semantic layer directly constrains this failure because the data team defines the metric, grain, join path, and time behavior before the agent asks a question.

The second is a **language-model error after the query**. The agent may misread a returned value, overstate what the data proves, or add a plausible explanation that the result does not support. A semantic layer makes this error easier to detect because the answer can carry named definitions, filters, lineage, and the generated query, but the model output still needs validation.

Use six controls together:

1. **Define metrics outside the prompt.** Put measures, dimensions, joins, grains, and time behavior in a versioned semantic model owned by the data team. Prompt examples are hints, not definitions.
2. **Make the agent select certified objects.** Let it discover approved metrics and dimensions by name instead of generating free-form SQL against every warehouse table.
3. **Compile permissions into every query.** Apply tenant, row-, column-, and role-level policies below the model so a correct answer cannot include data the asker is not allowed to see.
4. **Return evidence with the result.** Preserve the metric definition, filters, dimensions, time range, model version, and query identifier so a person or another agent can reconstruct the answer.
5. **Run known-answer evals.** Test representative business questions against values verified by the data team, including ambiguous wording, subtle joins, empty results, and denied-access cases.
6. **Require support for narrative claims.** If the agent explains *why* a metric moved, make it query the relevant dimensions or label the explanation as a hypothesis rather than presenting a fluent guess as evidence.

The practical goal is not a promise that the model will never make a mistake. It is to prevent the model from inventing the business logic, constrain what it may query, and make every numerical claim traceable enough to test.

## What teams get wrong about agents and SQL

The first instinct when wiring an LLM to a warehouse is to give it the database and a good prompt: here's the schema, here are a few example queries, now answer the user's question. It demos beautifully. Then it meets production.

The failure mode isn't that the model can't write SQL. Modern models write syntactically perfect SQL all day. The failure mode is that SQL is the *wrong abstraction* to hand an agent, for three reasons:

- **Semantics aren't in the schema.** A table named orders doesn't tell the model whether "revenue" is gross or net, includes tax, excludes refunds, or is recognized at order time or ship time. The model guesses — plausibly, and differently each time.
- **The join graph is a minefield.** Real warehouses have fan-out joins, slowly-changing dimensions, and three tables that all look like they could be "the customer table." Get the grain wrong and the number is silently double-counted. The model has no way to know it was wrong.
- **There's no access control in a SELECT.** A correct query and a query that exposes another tenant's data look identical to the model. If permissions live downstream — or nowhere — the agent is one clever prompt away from a data-leak incident.

So the same prompt ("what was revenue last quarter?") can return three different numbers across three sessions, and any of them might quietly include rows the user shouldn't see. That's not a prompt-engineering problem you can fix with one more example in the context window. It's a missing layer.

## Access vs. understanding

It's worth naming the distinction precisely, because most "AI on your data" pitches blur it.

**Text-to-SQL is an access mechanism.** It translates English into a query against whatever tables exist. It's genuinely useful, and you still want it — query-time flexibility, ad-hoc filters, novel groupings. But access without an agreed model of the business means every answer is re-derived from first principles, and "first principles" for an LLM means "a confident guess."

**A semantic layer is a layer of understanding.** It encodes, once, what the business actually means: metrics (revenue, active users, churn) with their exact definitions, dimensions and the entities they belong to, the join paths between them, and the access policies that govern them. The agent doesn't author that logic — it *selects from* it. "Revenue by region for the last 4 quarters" becomes a request for the revenue measure grouped by the region dimension over a time range, not a freshly invented 40-line query.

This is the part worth internalizing: the semantic layer doesn't make the model dumber or the analysis more rigid. It moves the hard, error-prone work — joins, grain, metric math — out of the prompt and into a definition the data team owns and tests once. The agent is still free to slice, filter, and combine those metrics at query time. It just can't redefine what "revenue" means on a whim, which is exactly the freedom you didn't want it to have.

## Governance has to happen before the SQL, not after

Here's the idea that separates a real agent platform from a clever demo: **compile-time governance.**

The naive approach is to let the agent generate a query and then check it — scan the SQL for forbidden tables, or filter the result set afterward. This is brittle. SQL has too many ways to reach the same data (subqueries, CTEs, views, joins) for a post-hoc check to be reliable, and an agent will eventually find a path your linter didn't anticipate.

The right approach is to evaluate access rules *when the query is generated*. The user's context — tenant, role, region, team — is part of the semantic layer's compilation step, so the SQL it emits already contains the right WHERE clauses and column restrictions. Row-level and role-based rules become a property of how every query is built, not a gate you hope runs afterward. An agent acting for a single-tenant user cannot construct a query that returns another tenant's rows, because the layer never compiles one. The model never even sees the forbidden data exist.

This is what makes governed agents safe enough to put in front of customers. The security boundary isn't the prompt (jailbreakable) or a post-filter (bypassable) — it's the query compiler, which the agent doesn't control. You get to reason about access the same way you do for a well-built embedded analytics product, because under the hood it's the same mechanism.

That security boundary is the core of governed AI data access: the agent can ask analytical questions, but tenant, role, row-level, and column-level rules are already part of the compiled query before data leaves the warehouse.

## How the agent talks to the layer: MCP

For the agent to *use* governed metrics, it has to discover them and request them. In 2026 the common interface for this is the **Model Context Protocol (MCP)** — an open standard for connecting LLMs to external tools and data.

A semantic layer that ships an MCP server exposes its model as something the agent can introspect and call — this is what serving it as an AI context layer means in practice. The flow looks like this:

1. **Discover.** The agent asks the MCP server what's available and gets back the catalog of governed measures and dimensions — revenue, active_users, region, plan_tier — with their descriptions, not raw table DDL.
2. **Select.** Instead of writing SQL, the agent forms a structured request: these measures, by these dimensions, with these filters, over this time range.
3. **Execute under governance.** The semantic layer compiles that request to SQL *with the user's access rules applied*, runs it (hitting a pre-aggregation cache when one exists), and returns governed results.

The agent is choosing from a menu it can read, not improvising a query against a schema it half understands. MCP is what makes "the agent selects from governed definitions" a concrete protocol rather than an aspiration. Claude, Codex, ChatGPT, and in-house agents can receive the same governed business context that Cube uses across Analytics Chat, workbooks, dashboards, and embedded analytics. SQL, REST, and GraphQL expose the model where those interfaces fit better than MCP.

If you are evaluating the implementation pattern directly, the analytics MCP server guide breaks down what the server should expose, how it should apply permissions, and how to test whether the agent's answer is grounded.

## Raw text-to-SQL vs. a semantic-layer-grounded agent

The difference is easiest to see side by side.

Dimension
Raw text-to-SQL against tables
Semantic-layer-grounded agent
Consistency
The model re-derives joins, grain, and metric logic each time; the same question can return different numbers
Metrics are defined once; the agent selects them, so the same question returns the same number
Governance
Access control lives downstream or not at all; a correct query and a leaking query look identical
Row-level and role-based rules applied at query-compile time; the agent can't query data the user can't see
Explainability
Answer is a wall of generated SQL; hard to trust or audit
Answer maps to named, documented metrics and dimensions; you can see exactly what was asked
Maintenance
Business logic is re-encoded in prompts and examples, and drifts across teams and apps
Logic lives in one governed model the data team owns and tests; change it once, every agent inherits it
Ad-hoc flexibility
High, but ungoverned — freedom to be wrong
High and governed — slice/filter/combine certified metrics at query time
Safe to expose to customers
Risky without a separate isolation layer
Yes — same multi-tenant boundary as governed embedded analytics

Raw text-to-SQL is fine for a single analyst exploring a sandbox they fully control. The moment an agent answers on behalf of *other* people — colleagues, or your customers — the semantic layer stops being optional.

## How to give an agent a semantic layer

Concretely, the path looks like this:

1. **Model your metrics and dimensions** in a semantic layer — the definitions of revenue, users, and the rest, with their join paths. If you already model transformations in dbt, that's a partner, not a competitor: dbt shapes the data; the semantic layer governs the metrics on top.
2. **Encode access policies as part of the model** — row-level rules keyed to the user's tenant and role — so they compile into every query rather than being checked afterward.
3. **Expose the model to the agent over MCP** (and SQL/REST/GraphQL for other clients), so the agent discovers governed metrics and requests them by name.
4. **Add caching** — pre-aggregations — so agent queries return fast and the warehouse bill stays sane when an agent fans out into many follow-up questions.
5. **Keep it SQL-first and extensible at query time**, so the agent can build ad-hoc calculations on top of governed definitions without forking them.

### Where Cube fits

Cube is the agentic analytics platform built on a semantic layer, and this is the wedge it was built for. Its open-source foundation, **Cube Core** (Apache 2.0), *is* the semantic layer: you model metrics, dimensions, joins, and access rules once. The Cube platform exposes that governed model to agents over an **MCP server** and over SQL (Postgres-compatible), REST, and GraphQL. Row-level, multi-tenant security is applied at compile time, and pre-aggregation caching keeps agent queries fast. The agent selects from certified definitions and **never writes raw SQL against tables.**

This is why Brex evaluated Cube against the dbt Semantic Layer and LookML and chose Cube — and then built Brex Spaces, an embedded AI financial analyst, on it. In their words, *the semantic layer is what makes the AI useful.* The same governed model that powers their internal BI grounds the agent; the open-source core means the layer the agent depends on isn't a black box. 400+ companies build on Cube across internal BI and embedded analytics.

### On the dbt Semantic Layer

If you want a pure semantic layer and dbt is the center of your stack, the **dbt Semantic Layer** (powered by MetricFlow) is a reasonable grounding source: it defines metrics inside your dbt project and serves them through dbt's Semantic Layer APIs. It's a fair alternative to Cube Core — the open-source semantic layer — rather than to the Cube platform, since it's metric-definition-focused and leans on the warehouse for execution (no built-in pre-aggregation cache) and on the dbt Cloud platform for the hosted layer. Many teams do both: model in dbt, then govern and serve metrics to agents and embedded apps through Cube. (For a fuller side-by-side, see the best semantic layer for AI and BI and the dbt Semantic Layer alternatives.)

## How to choose

- **You're putting an agent in front of colleagues or customers:** ground it in a decoupled semantic layer with compile-time row-level security and an MCP interface — that's Cube.
- **dbt is the center of your stack and you want a pure layer:** start with the dbt Semantic Layer; add a serving layer when you need caching, multi-tenant security, embedded delivery, or an MCP endpoint.
- **Everything lives in one warehouse and the agent never leaves it:** a warehouse-native semantic model (Snowflake, Databricks) can ground that platform's own AI; reach for a decoupled layer when the agent's reach exceeds one platform.
- **You're tempted to skip the layer and just prompt-engineer the schema:** that scales to a demo, not to production. The first inconsistent number — or the first cross-tenant leak — is the layer you didn't build.

## Methodology

This guide is based on how analytics agents are built and governed as of 2026, weighted toward the properties that matter when an agent answers on behalf of other people: metric consistency, access control enforced before query execution, explainability, maintenance, and the interfaces (notably MCP) an agent uses to reach governed data. Protocols and product capabilities are moving quickly — MCP support in particular is evolving across the ecosystem — so confirm specifics against current documentation. As the publisher, Cube has an obvious interest here; we've tried to describe the alternatives fairly and to be explicit about when a different approach is the better fit.

## Frequently asked questions

Why do AI agents need a semantic layer?An LLM can write SQL, but it doesn't know your join paths, metric definitions, or access rules. Pointed at raw tables it re-derives all of that on every prompt, so answers are inconsistent and can leak data. A semantic layer constrains the agent to certified metrics and dimensions and applies governance before any SQL runs, which makes answers consistent, safe, and explainable.How do you stop AI agents from hallucinating metrics?Do not let the model define metrics from table names or prompt examples. Give it certified measures, dimensions, joins, and time behavior from a semantic layer; enforce the user's permissions when the query is compiled; return the metric definition, filters, time range, and query lineage with each result; and run evals against known answers and denied-access cases. This prevents metric-definition drift and makes errors visible, but it does not eliminate every language-model mistake, so unsupported narrative claims still need validation.Isn't text-to-SQL enough for an analytics agent?Text-to-SQL is necessary but not sufficient. It gives the agent access to the database; it doesn't give it an agreed definition of 'revenue' or 'active user', the correct join paths, or the user's permissions. Without a governed layer to select from, two phrasings of the same question can produce two different numbers, and nothing stops the model from querying tables a user shouldn't see.What is compile-time governance?Compile-time governance means row-level and role-based access rules are evaluated when the query is generated, not checked afterward. The user's context (tenant, role, region) is baked into the SQL the semantic layer emits, so an agent cannot construct a query that returns forbidden rows. Governance becomes a property of query generation rather than a filter you hope was applied.How does MCP fit in?The Model Context Protocol (MCP) is an open standard for connecting LLMs to tools and data. A semantic layer with an MCP server exposes its governed metrics and dimensions as something the agent can discover and call: the agent lists what's available, then requests measures and dimensions by name. It asks for governed definitions instead of writing SQL against tables.Does a semantic layer stop the agent from doing ad-hoc analysis?No. A good semantic layer is SQL-first and extensible at query time: the governed definitions stay intact while the agent builds ad-hoc calculations, filters, and groupings on top of them. The constraint is on what counts as 'revenue', not on what questions you can ask of it.How does a semantic layer improve text-to-SQL accuracy?Instead of inferring table structure and business logic, the model picks from pre-defined metrics and dimensions and the semantic layer generates the SQL. The hard, error-prone parts — joins, grain, filters, metric math — are solved once by the data team rather than re-guessed by the model on every query, so results are consistent and governed.Is the dbt Semantic Layer an option for grounding agents?Yes. The dbt Semantic Layer (powered by MetricFlow) is a pure semantic layer that defines metrics inside your dbt project, and it's a reasonable grounding source if dbt is the center of your stack. It competes with Cube Core, the open-source semantic layer, rather than with the Cube platform. dbt itself is a partner: many teams model in dbt and serve metrics to agents through Cube.Can I just put the table schema in the system prompt instead?Pasting schema (or a few example queries) helps a little, but it doesn't scale or govern. The model still authors SQL, still has to be right about joins and grain every time, and still has no enforced access control. A semantic layer turns 'here's the schema, good luck' into 'here are the certified metrics you may use', which is both more accurate and safe.Do I need a separate semantic layer if my warehouse has one?Warehouse-native semantic models (Snowflake, Databricks) are convenient inside a single platform and can ground that platform's own AI. If your agents span multiple warehouses, power embedded analytics, or need multi-tenant row-level security, a decoupled semantic layer is a better fit. Match the layer's reach to the agent's reach.What does Cube provide for AI agents specifically?Cube is the agentic analytics platform built on a semantic layer. Agents reach governed metrics over an MCP server and SQL/REST/GraphQL interfaces, with row-level multi-tenant security applied at compile time and pre-aggregation caching for fast responses. The agent selects from certified definitions and never writes raw SQL against tables.

## Get started with Cube

Get startedRequest a demo
