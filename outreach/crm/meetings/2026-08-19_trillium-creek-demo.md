---
deal_id: D006
company: Trillium Creek Dermatology
contacts: Michelle Maynard (mmaynard@tcohio.com), Aaron Funk
date: 2026-08-19
time: 1:00 PM
type: demo
status: scheduled
source: inbound (website/Calendly) — possible ModMed CEO connection via Scott
---

# Trillium Creek Dermatology — Demo Prep

## Company profile
- **Website:** tcohio.com
- **Business:** Dermatology practice, Northeast Ohio (Medina area)
- **Locations:** 5 clinical offices (Medina, Brunswick, Strongsville, Wadsworth, Wooster) + HH Science locations (their skincare product line)
- **Providers:** 7 MDs (Helen Torok, Leonard J. Torok, Wyatt Andrasik, Bryan Baillis, Selena Pasadyn, Matthew Reedy, Joshua Weaver), 7 PAs, 4 RNs — roughly 18 clinical staff
- **Founded by:** The Toroks (Helen and Leonard) — founder-led, possibly family practice
- **Services:** General dermatology, cosmetic (Botox, fillers, lasers, body shaping), Mohs surgery, pediatric. Broad service mix.
- **EMR:** ModMed EMA (specialty derm EMR)
- **Other systems:** Patient portal, HH Science (own skincare product line), Trizetto (had a data breach — noted on their site)
- **Phone:** 330.725.0569

## What they told us
Michelle's Calendly message: "We have ModMed and are interested in learning about potential report automations/dashboards"

## What they likely struggle with (from ModMed research)
- ModMed's built-in analytics are basic — limited customization, pre-built reports only
- 2-year historical data cap on analytics
- No "connect your BI tool" experience — data is locked in
- Manual CSV exports to Excel when built-in reports don't answer the question
- Multi-location cross-comparisons that ModMed doesn't do well

## Demo dataset
Six tables uploaded as CSVs — modeled on what a ModMed API connector would produce:

| Table | Rows | What it shows |
|-------|------|---------------|
| patients | 3,500 | Demographics, payer mix, Ohio cities |
| encounters | 10,248 | Visits by provider, location, visit type |
| diagnoses | 13,812 | ICD-10 derm diagnoses (acne, BCC, psoriasis, etc.) |
| procedures | 10,788 | CPT codes (office visits, biopsies, Mohs, destruction) |
| appointments | 11,065 | Scheduling with no-shows and cancellations |
| charges | 10,788 | Billing with payer mix, denials, charge amounts |

## Suggested demo prompts
1. "How many encounters did we have last month by location?" — shows multi-location view they don't have
2. "Show me monthly encounter volume by visit type" — New Patient and Telehealth growing
3. "Which provider has the highest no-show rate?" — actionable ops insight
4. "What are our top diagnoses by volume?" — clinical mix overview
5. "Show me the top 20 highest charges with their procedure type" — billing anomalies visible (office visits billed at 3-4x normal)
6. "How is Wadsworth growing compared to other locations?" — growth story for their newer location

## Key questions to explore
- **What reports are they running today?** Are they pulling from ModMed manually? Exports to Excel?
- **Do they use ModMed Analytics or Premium Analytics?** (Premium has more but still limited)
- **Who needs the data?** Michelle/Aaron doing ops reporting? The Toroks wanting practice-level financials? Individual providers wanting their own metrics?
- **Multi-site complexity:** Do they need to compare performance across sites? Aggregate vs. per-location views?
- **What are they measuring?** Likely: patient volume by location/provider, revenue by service line (derm vs cosmetic vs Mohs), appointment utilization, cosmetic product sales (HH Science), no-show rates, new vs returning patients
- **Are they part of a PE rollup?** Common for derm groups — if so, cross-practice reporting is a killer use case
- **What other systems do they use alongside ModMed?** Billing clearinghouse, inventory, marketing — Dashbud unifies these
- **Why now?** Growth? New location? Frustration with ModMed's built-in reporting?

## Dashbud angles
- **Multi-site practice:** 5 locations = can't be hands-on everywhere. Need aggregated visibility. This is the ICP Lovett and Rodgers both identified.
- **ModMed connection:** Scott knows the ModMed CEO. If this works, it could become a channel play — Dashbud as the analytics layer for ModMed practices.
- **Privacy:** Healthcare = HIPAA. Our "AI never sees raw data" story is directly relevant. They've had a Trizetto data breach — security/privacy will be on their mind.
- **Self-serve:** They asked about "report automations/dashboards" — they want answers themselves, not wait on someone.
- **Mixed service lines:** Derm + cosmetic + surgery + products = complex data that doesn't live in one place. Classic Dashbud use case.
- **Only competitor with a ModMed connector:** Domo is the only BI tool with a ModMed connector today. We'd be the second, and the first on the synapSYS Marketplace.

## Getting TC live (if they want to start)

**Day 1 (no engineering):**
- Create their account
- They export from ModMed Analytics as CSVs
- Upload to Dashbud, build semantic model
- Start querying their real data
- **Refresh problem:** Every update requires re-export and re-upload. Fine for a trial.

**The API path (longer term):**
- ModMed has two API tiers — FHIR (public, limited) and proprietary synapSYS (gated, full data)
- FHIR alone is not enough — it lacks encounters, appointments, and billing
- Proprietary API requires partner approval (~2 weeks sandbox provisioning + proficiency demo)
- Scott's connection to ModMed leadership could accelerate this
- Building a ModMed connector makes Dashbud the second BI tool (after Domo) with ModMed integration

## Pricing
- Multi-location practice with ~18 providers — probably Scale ($79/mo) or Enterprise
- If they want the API connector built, that's additional work — could be a paid deployment similar to the ADAPT Azure proposal

## Risk / watch-outs
- "Report automations" might mean scheduled/emailed reports, which we may not have yet
- They may be comparing us to ModMed's built-in analytics (Analytics or Premium Analytics) or Domo
- ModMed data connectivity via API requires partner approval — not instant
- Cosmetic side may have different systems (POS, loyalty program) not covered by ModMed

## Background: ModMed
ModMed (Modernizing Medicine) is a major healthcare IT company — EHR/EMR for specialty practices (dermatology is one of their core verticals). Scott knows their CEO. If Dashbud works well for a ModMed customer, the partnership angle is: ModMed recommends Dashbud for analytics on top of their platform. Large potential TAM — thousands of specialty practices using ModMed.
