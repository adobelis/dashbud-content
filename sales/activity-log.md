# Activity Log — Late August / November 2026

Working backwards from today. Tracking time, activities, and ticket associations.

---

## 2026-10-31–11-02 (Saturday–Monday)

### Marketing — content strategy
- **MKT-68L ("Downstream" blog series):** 6h of research into AI memory, covering both agent and non-agent approaches. Relates to the memory plane of the series argument and the candidate sixth post, "Memory Is Not a Database Feature."
- **Working docs drafted:** `website/blog/_downstream-series-plan.md` (five posts, arguments, tone guardrails, bench) and `website/blog/_downstream-space-map.md` (the planes, who owns each, plus the in-weights memory addendum).
- **Time:** 2h Sat 10/31, 3h Sun 11/01, 1h Mon 11/02 morning.

---

## 2026-10-21–22 (Wednesday–Thursday)

### Marketing — LinkedIn launch
- **Founder announcement posted** Wed 10/21 2:00pm — "Data is born free" (Rousseau hook). First public association of Arthur with Dashbud. Full stats and running log in `outreach/linkedin-post-tracker.md`.
- **~21h performance:** 965 impressions, 507 members reached, 48% out-of-network, 40 engagements (23 reactions / 13 comments / 2 reposts). ~4.1% engagement rate; comment-to-reaction ratio 0.57, well above typical — the likely driver of the out-of-network reach.
- **Promotion legwork:** ~30 of 50 planned personal outreaches done (text + DM). Escalating to high-value promoters only once the post is ~a day old, so the ask comes with visible traction attached rather than as a cold favor. Post written to be non-time-sensitive for exactly this reason.
- Outcomes (DMs, profile→site traffic, notable commenters) still to be filled in.

---

## 2026-10-08 (Thursday)

### Sales / CRM
- **ADAPT:** Scott sent the Dashbud security overview to Devon this week. Deal is now in security review — most advanced live deal. Still likely implementation by EOY. Note: the $35K Azure deployment figure is a stale bid; Arthur would price higher today, so treat any revival as a rebid.
- **Omega:** Confirmed paid — 7 annual licenses, $7,200/yr, payment received 2026-08-25. Contract effective 2026-05-11, 12-month term, auto-renews unless either party gives 30 days' notice → real decision point ~2027-04-11. No product adoption yet; they consume only reports Arthur built. Re-engagement set for 2026-10-22: offer additional reports plus a recurring cadence, routed through the new Fractional CFO (the real stakeholder; Dan Peters, CTO, remains main contact).
- **Trillium Creek:** Confirmed closed-lost. No response from Michelle or Aaron to the win-back email. Never logged into the app — consumed only Arthur-delivered reports, so never saw the semantic model or governance that make the ChatGPT comparison invalid.

### CRM hygiene
- `outreach/crm/pipeline.csv` brought current: all 6 deals re-staged (Omega closed_won, ADAPT security_review, TC closed_lost, AAH/PCI/PMC dormant), contacts and dates filled in, running history added to notes.
- `outreach/crm/README.md`: documented `pipeline.csv` for the first time (it had no schema entry) and defined a 9-stage deal enum. Added an explicit **POC vs. trial** distinction — POC = we do hands-on work with their data; trial = they have self-serve product access. Marked the empty `deals.csv` as superseded.
- Added `scripts/contacts/validate_pipeline.py` — parses the CSV and flags any stage not in the documented enum.

### Insights captured
- **Adoption pattern is the central GTM problem.** In 4 of 6 deals the product was delivered as a service. A customer who never uses the product has no way to know why ChatGPT isn't equivalent — this is upstream of the ChatGPT objection, not separate from it.
- **POCs still pay for themselves** as reusable technical proof points regardless of deal outcome: Omega proved Informix ingestion at scale; TC proved ModMed EMA tables ingest easily, which de-risks every future ModMed prospect. The risk to manage is the handoff, not the POC.
- **Possible principal-agent dynamic at TC:** champion may have been optimizing for personal skill acquisition (learning to vibe-code) rather than company reporting needs. Worth treating "champion wants to build it themselves" as a qualification signal.

---

## 2026-10-06 (Monday)

### Marketing / Legal
- **MKT-61:** Privacy Policy overhaul — rewrote from scratch to reflect current data architecture (direct DB pass-through vs. file imports), AI separation, data governance, security controls, self-hosted option. Pushed to Sanity.
- **MKT-61:** TOU tweaks — entity description reworded, "accessing Dashbud" (not "website"), free trial clause added. Pushed to Sanity.
- Homepage hero CTAs corrected in Sanity (Try Dashbud → /signup, Book a Demo → Calendly)
- Security overview drafted for ADAPT's Devon (VP of IT) — covers data architecture, encryption, access controls, governance, compliance, self-hosted deployment
- LinkedIn founder announcement draft finalized

### Sales
- **Trillium Creek:** Lost. Michelle declined Sep 21 — chose to "use ChatGPT instead." Win-back email sent (Arthur + Scott) explaining why ChatGPT isn't a substitute. No reply as of Oct 6. Correspondence archived. MKT-60 and MKT-63L updated.
- **ADAPT:** Still interested, likely implementation by EOY. Devon requested security synopsis. Self-hosted Azure deployment quoted at $35K (earlier note said ~$40K; $35K is the figure in the bid, and it is stale — Arthur would price higher today).

---

## 2026-09-17 (Wednesday)

**Time: ~8:00am – present**

### Product engineering
- **DS-433:** Resend invite for expired welcome links + replace alert() with ConfirmModal (TC invites went to Junk) — ~1hr morning
- **DS-429:** Board collection formats — dashboard (tiled), report (linear), tabbed (full screen per asset) — ~1hr previous night (11pm-12am on 9/16)
- **DS-428:** Dashboard board rename UI — click title to edit (owner only) — 9/16 evening

### Customer work (Trillium Creek)
- Recreated ~15 reports from TC's August raw data (appointment + production tables from ModMed EMA) with Watts (Dashbud-user agent)
- Michelle shared Google Drive with ~30 reports and priority listing
- **Time: ~8am–6:30pm with lunch break** (mostly TC data analysis)

---

## 2026-09-16 (Tuesday)

### Product engineering
- **DS-428:** Dashboard board rename UI — evening
- **DS-426:** Semantic table names for FileImportDS — rename, display_sql, hide raw schema
- **DS-426:** Code review — inject sm_model_repo, remove current_app dependency
- **DS-426:** Use repo for workspace links, proper logging for SM updates

---

## 2026-09-15 (Monday)

### Product engineering
- **DS-425:** Fix duplicate CTE alias when LLM reuses table name as CTE alias
- **DS-425:** Code review response — add tests, broaden regex, update local test infra
- **DS-424:** Populate approx_distinct for FileImportDS columns after materialization

---

## 2026-09-12 (Friday)

### Product engineering
- **DS-423:** Add-table preview wizard, graceful timestamp coercion, table name dedup
- **DS-423:** Async background job for add-table route
- **DS-423:** Code review fix — remove hasattr check

---

## 2026-09-08 (Monday)

### Marketing / Legal
- **MKT-60:** Legal docs for TC and others, outreach work (content repo commit)
- **MKT-61:** Update Terms of Use — correct entity, expand privacy and liability (website commits)
- Sanity push script for info pages
- TOU backups created

---

## 2026-08-25–26

### Sales
- **Omega Molding — FIRST REVENUE.** Payment received 8/25: 7 annual licenses, $7,200/yr. Contract effective 2026-05-11. First paying Dashbud customer.

### Product engineering
- **DS-419:** API key authentication and management — multiple commits
- **DS-342:** Remove RDS fallbacks (bundled with DS-419)
- **DS-421:** Protect local Docker volumes from accidental deletion
- CloudFront fix for API 403/404 responses
- Hide API key UI for non-owner/admin users

---

## 2026-08-20–21

### Sales
- TC demo happened 8/19 — transcripts and materials committed
- Sales directory reorganized (playbooks, decks, meetings)

### Product
- Anthropic version fix
- DS-419: Fix params lost on rehydration

---

## 2026-08-13–18

### Marketing / Website
- **MKT-58:** Mobile formatting fixes for small phones + LinkedIn (Aug 13)
- **MKT-59:** Update signup form to new endpoint (Aug 14)
- **MKT-60P:** Collect website feedback from inner circle (Aug 17)
- **MKT-60:** TC sales prep in wiki (Aug 18)
- CRM/outreach infrastructure, first-round feedback committed (Aug 18)

### Outreach
- Active first-round outreach to friends and advisors
- Fernando Pizarro call (GTM advisor, Aug 20 timeframe)
- Website feedback collection from inner circle
- Advisor conversations: Matt Lovett, Matt Rodgers, Alyssa Elser (summaries and transcripts exist)

---

## Sprint s17 (Jul 29 – Aug 12) — needs closing

### Done during sprint window:
- MKT-52: Who It's For page ✓
- MKT-54: Data sources panel ✓  
- MKT-55: About page / mission statement ✓
- MKT-51: ERP research ✓
- MKT-53: Competitor analysis (synthesis complete) ✓

### Continued past sprint window:
- MKT-58L/58: Outreach — ongoing
- MKT-46: Contact list — ongoing
- MKT-43: LPBI review — not started

### Not on sprint but happened:
- MKT-59: Signup form update
- MKT-60: TC sales engagement (demo, legal, data analysis)
- MKT-61: Terms of Use
- DS-419 through DS-433: Product engineering (API keys, table management, board formats, semantic table names, CTE fix, resend invites)
