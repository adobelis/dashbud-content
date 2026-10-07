# Activity Log — Late August / September 2026

Working backwards from today. Tracking time, activities, and ticket associations.

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
