# Product page module: Your AI, your data, with guardrails

**Status:** DRAFT, 2026-10-19. Copy below is Claude's first pass for Arthur to edit. Transcript numbers are illustrative, based on the Forge & Frame mock dataset's planted stories, not captured API output.

**For Cody:** This is a feature module for the revised product page. The centerpiece is a mock chat UI, styled like a generic web AI assistant (not Claude or ChatGPT branding), showing an AI exploring data through the Dashbud API. Tool calls should render as collapsed "Dashbud" cards inside the chat, the way assistants show tool use. Static mock is fine; animate on scroll if cheap. Headline and body sit beside or above the chat.

---

## Headline

Bring your own AI. Keep your guardrails.

## Subhead

Dashbud's API is built for AI agents. Point Claude, ChatGPT, or your own agent at a Dashbud workspace, and it can explore your data, run real analysis, and explain its work. It sees only what the workspace permits: governed query results, with your business rules applied. Never the database. Never anything out of scope.

## Body (three short points beside the chat)

* **Scoped by workspace.** An API key is tied to specific workspaces. The agent can see those sources, those tables, those columns, and nothing else. Exclude a column or filter rows, and the agent never knows it existed.
* **Your rules, every time.** Every question runs through the semantic model. "Margin" means what your team decided it means, whether a person or an agent is asking.
* **Auditable by design.** Every answer comes back with the SQL that produced it. No black box between the question and the number.

---

## Mock chat transcript

> **User**
> Our Q2 2025 gross margin came in low. Can you figure out why?

> **AI**
> I'll check the Forge & Frame sales workspace.
>
> ▸ **Dashbud** · workspace: Forge & Frame Sales · sources: orders, order_items, products, customers
>
> ▸ **Dashbud** · *"Gross margin by quarter, 2024 to 2025"*
> Margin held near 42% through Q1 2025, then dropped to 37% in Q2 2025.
>
> That's a five-point drop in one quarter. Let me see whether it's broad or concentrated.
>
> ▸ **Dashbud** · *"Gross margin by wholesale account, Q1 vs Q2 2025"*
> One account stands out: Metro Restaurant Supply. Volume up about 30%, margin down from 41% to 28%.
>
> The drop traces to Metro Restaurant Supply. Their order volume jumped roughly 30% in Q2, but at a much lower margin, consistent with a negotiated discount starting that quarter. The rest of the book is flat.

> **User**
> Is that a one-off, or do we have a bigger exposure problem?

> **AI**
> ▸ **Dashbud** · *"Wholesale revenue share by account, trailing 12 months"*
> Top 3 accounts: 40% of wholesale revenue. Metro is the largest at 17%.
>
> It's both. The margin hit is one account's discount, but that account is your largest, and three accounts make up 40% of wholesale. A second discount request from any of them would move the whole company's margin. Worth a conversation with sales before the next renewal.

---

## Caption under the chat

Every tool call above is a real API request. The agent asked, Dashbud ran the governed query, and the agent reasoned over the result. What the agent never touched: the database, any column or row the workspace excludes, or any data outside its scope. The guardrails are in the workspace, not in the prompt.

## Link

Read the API docs → *(target: docs page, to be written)*

---

## Notes for Arthur

* Guardrail is told, not shown, per your call: the subhead, the first body bullet, and the caption carry it. If you later want a shown version, add a final exchange where the user asks for a buyer's contact and the agent reports the field is excluded; that needs the demo workspace configured to match.
* "Never the database" is deliberate wording. The API returns query results, so the module can't claim the agent never sees data; it claims the agent never sees anything outside the workspace's scope. Keep it consistent with the Trust section, which is about Dashbud's own agents working from schema.
* The script at scripts/research/dashbud_api_session.py works against workspace 106 if you later want real captured output. Base URL is the app host, not api.getdashbud.com; the API doc's base URL is stale (one for Corey).
