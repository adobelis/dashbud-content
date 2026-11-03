---
title: "AkasicMEM: Governed Enterprise Memory for Agents"
author: Jeongmin Bae, Yongjae Kim, Kyoung Hur, Donghyoung Han, Min-Soo Kim
author_slug:
org: arXiv (cs.DB), GraphAI
url: https://arxiv.org/abs/2609.25563v1
published: 2026-09-22
added: 2026-11-03
scrape: scrapes/2026-09-22-arxiv-akasicmem-governed-enterprise-memory.md
series: downstream-02
tags: [downstream, memory, governance, academic, cite]
---

# AkasicMEM: Governed Enterprise Memory for Agents

## Summary (abstract only; PDF not read)

Defines "Governed Enterprise Memory": agent memory where enterprise sources and accumulated memory are used together, shared memory stays subject to organizational policy through its lifecycle, and **authorization continuity** holds, meaning a source's access restrictions keep applying as information is derived into memory and reused by other agents under other principals. The failure they're preventing: information from a restricted source persists in memory and leaks when retrieved by someone who couldn't see the source. Mechanisms: transitive lineage, policy composition at memory formation, policy re-evaluation at retrieval. Built on a combined vector, graph, and relational database.

## Relevance to Downstream

Direct, and it corrects the map. Organizational memory with governance is being worked on, in a database group, with exactly the problem the Downstream map names: who may see what, carried through everything derived from it. The post-2 claim should be "the governance problem in memory is recognized and the work is happening in databases and startups, not in the labs," not "nobody is here."

It's about agent memory under policy, not about agreed business definitions. Still a different thing from the semantic model. But "authorization continuity" is a precise name for something Dashbud's workspace scoping does implicitly: a query result inherits the scope of the workspace it came from. Worth borrowing the term with attribution if post 2 goes technical.

Read the PDF before citing beyond the abstract.
