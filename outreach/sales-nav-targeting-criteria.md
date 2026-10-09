---
title: "Sales Navigator Targeting Criteria — Round 1"
visibility: private
---

# Sales Navigator Targeting Criteria — Round 1

**Created:** 2026-10-08
**Owner:** Arthur
**Status:** Draft for review — vertical choice and filter values need sign-off before list building

This is the written spec behind Track 2 of the GTM plan ("surgical outbound → focused ICP"). It exists so the target list is reproducible: anyone should be able to recreate the same ~200 companies from these filters, and we should be able to tell afterwards which criteria actually predicted interest.

---

## Decision: one vertical, round 1

**Manufacturing & distribution, 10–50 employees, legacy or on-prem ERP, no data team.**

### Why this over healthcare

| | Manufacturing / distribution | Healthcare / specialty practices |
|---|---|---|
| Proof point | **Omega** — paying customer, 30-year-old IBM Informix ERP, 8 warehouses, $50M revenue | Trillium Creek — POC proved ModMed ingestion, but deal lost |
| Advisor endorsement | Lovett, near-verbatim: *"manufacturing teams with custom ERP data, 10 to 50 employees, without their own data team"* | Raised as promising, not specified |
| Blocking dependency | None | ModMed connector / partnership (Scott re-engaging) |
| Per-deal overhead | Normal | BAA, PHI handling, security review |
| Reachability | High — SQL Server is the golden thread (see below) | Mixed — Epic yes, Cerner/athena no |

Healthcare is likely the bigger long-term market, and the privacy story is strongest there. But it is gated on the ModMed connector and carries compliance overhead per deal. Round 1 should be the segment where we already have a paying reference and zero blockers.

**Revisit after round 1.** If manufacturing outbound produces a reply rate below ~5%, re-examine the segment before blaming the messaging.

---

## Firmographic filters (Sales Navigator — Account search)

| Filter | Value | Rationale |
|---|---|---|
| **Industry** | Manufacturing; Wholesale; Wholesale Building Materials; Industrial Machinery; Plastics; Packaging & Containers; Food & Beverage Manufacturing | Omega is building materials distribution. Keep the net at the sector level, narrow via headcount |
| **Company headcount** | 11–50, 51–200 | Lovett said 10–50. Extend to 200 because ADAPT-scale deals pay better and the pain scales with sites |
| **Company type** | Privately Held; Partnership; Self-Owned | Excludes public companies (have BI teams) and most tech startups |
| **Geography** | United States — Midwest and Northeast first (OH, PA, NY, NJ, IN, MI, IL, WI) | Omega and Trillium Creek are both Ohio. Time-zone overlap for demos; regional credibility |
| **Annual revenue** | $10M–$100M | From `offer_framework.md`. Enough to justify $5–50K; too small to have a data team |
| **Headcount growth** | *Do not filter* | Growth signals a scaling company, but legacy-ERP pain is not growth-dependent |

### Exclusions (hard)

- Software, IT services, internet, and tech companies — **they can build their own** (Rodgers and Lovett both explicit)
- Public companies and enterprises >500 employees — established BI teams, Tableau/Looker incumbency
- Single-location businesses under ~$10M — have to sell the concept of analytics itself
- Staffing, consulting, and agencies — different data shape, no ERP anchor

---

## Signal filters — what makes a company *reachable*, not just a fit

This is where the ERP research (`wiki/dashbud/research/erp-connectivity/summary.md`) earns its keep. Fit without connectivity is a wasted conversation.

### Tier A — connect today, zero new development (highest priority)

Companies on these systems can be onboarded with the current product. **SQL Server is the golden thread.**

| ERP | Note |
|---|---|
| Microsoft Dynamics GP | ~68K customers, **end-of-life 2029** — forced-migration urgency is a live hook |
| Microsoft Dynamics NAV / BC on-prem | Same semantic-model story as GP |
| Epicor Kinetic (on-prem) / ERP 10 | No BI tool has Epicor schema intelligence |
| Epicor Prophet 21 | Distribution-specific; even Fivetran's connector is basic |
| Infor SyteLine / CloudSuite Industrial v10+ | **No BI tool has Infor connectors** |
| SAP Business One (SQL Server edition) | Sigma/Zenlytic/Omni have zero SAP connectivity |
| Sage 100 Premium | |
| JD Edwards EnterpriseOne (SQL Server) | |

### Tier B — CSV/file import path (still viable, slightly longer sell)

| ERP | Note |
|---|---|
| IBM Informix | **Omega's exact system** — strongest proof point we have |
| Sage 50 / Sage 100 Standard | No BI tool handles ProvideX or Actian Zen well |
| SAP ECC | Licensing makes direct access risky for everyone, not just us |
| Oracle EBS, JD Edwards World (AS/400) | Nobody connects to AS/400 easily |

### Tier C — deprioritize for round 1

NetSuite, Sage Intacct, Dynamics 365 cloud — need API connectors we have not built. Do not prospect into these yet; log them as demand signal if they surface.

### How to detect ERP in Sales Navigator

Sales Navigator does not expose installed technology directly. Proxies, in order of reliability:

1. **Job titles and descriptions** — search employee titles for "ERP," "Dynamics," "Epicor," "Infor," "SyteLine," "Prophet 21," "Informix," "AS/400." A company with an "ERP Administrator" has an ERP worth connecting to.
2. **Job postings** — hiring for "Dynamics GP Developer" or "Epicor report writer" is a direct signal, and it signals *pain* (they are trying to staff around the reporting gap).
3. **Account keyword search** on company descriptions.
4. **PE ownership** — see below.

Worth considering a supplementary data source (BuiltWith, Apollo, ZoomInfo) for installed-ERP data if Sales Nav proxies prove too thin. Decide after the first 50 accounts.

### PE ownership — a strong accelerant

From `gtm-status`: *"PE-backed ownership transitions: new owners wanting visibility into an opaque business they just bought."* Omega is exactly this pattern — newly PE-owned former family business.

Why it works: new PE ownership creates a **reporting mandate with a deadline and a budget**, and the operators are often inheriting systems they do not understand. Detect via recent "acquired by," new CFO/CEO announcements, or a fractional CFO appearing.

**Omega's own lesson applies here:** the fractional CFO was the real stakeholder, not the CTO who signed. In PE-backed accounts, target the finance stakeholder.

---

## Target buyer titles (Sales Navigator — Lead search)

Per `gtm-status` ICP research and the Omega stakeholder lesson.

### Primary

- Chief Operating Officer / VP Operations / Director of Operations
- Chief Financial Officer / VP Finance / Controller / **Fractional CFO**
- Director / VP of Supply Chain, Logistics, or Distribution
- General Manager (multi-site or plant level)

### Secondary (often the internal champion)

- ERP Administrator / ERP Manager
- Business Analyst / Operations Analyst / Financial Analyst
- IT Director at companies with no separate data function
- "The person who builds the reports" — often an ops or finance analyst by title

### Do not target first

- **CEO** — too strategic at this deal size unless the company is <25 people (then the CEO *is* the ops lead)
- **Pure IT / infrastructure / sysadmin** — too technical, wrong incentive, often threatened by the purchase
- **Data engineers / analytics engineers** — if they exist, the company is out of ICP

---

## Qualification signals to capture during outreach

### Positive

- Describes manual monthly reporting, export-to-Excel, or "one person who knows the system"
- Recently acquired, new ownership, or a new finance leader
- Multiple sites, plants, or warehouses
- Previously shelved a BI tool, or lost the analyst who built everything
- ERP is old, on-prem, or heavily customized

### Disqualifiers

- Has a data team, data engineer, or existing warehouse + BI stack
- Is a software or tech company
- Single location, under $10M revenue
- **Champion wants to build it themselves** — see below

### The build-it-themselves signal

*Derived from the Trillium Creek loss. This is a principal-agent problem, not a feature objection.*

When the champion is personally excited about **building** the solution rather than **having** it, their interest and the company's diverge. The company wants reliable reporting; the person wants the skill, the credit, or the career story. A vendor delivers what the company wants while taking away what the person wants — which is why no amount of product argument wins. Michelle declined Dashbud for ChatGPT and never replied to the win-back; she had never logged into the app.

**Detect it:** enthusiasm about the building rather than the outcome. "I've been playing with ChatGPT on this." "I want to understand how it works under the hood." "I'm teaching myself to build this."

**Countermove:** do not argue with that person. Find the stakeholder who eats the cost when it breaks, or who inherits the mess when the builder leaves — usually the CFO or COO. If that person cannot be reached, deprioritize the account.

---

## Volume and sequencing

| Parameter | Value | Source |
|---|---|---|
| Target accounts | ~200 | Rodgers and Lovett both said ~200 logos |
| Leads per account | 2–3 (one primary, one secondary, one finance) | Multi-threading; Omega's signer ≠ stakeholder |
| Channel | **LinkedIn first, not email** | Lovett: email domain trust is unknown |
| Goal | 5 customers in 2–3 months | Lovett's benchmark |
| Decision gate | Reply rate <5% after 50 accounts → revisit segment or messaging before continuing | |

### Pre-sales rule — the Trillium Creek lesson

POC work is worth doing: each one produces a reusable technical proof point regardless of outcome. But **land the POC inside the product and hand over app access.** Do not deliver finished reports from outside it. A prospect who only ever sees output concludes that output is replaceable by ChatGPT — because from where they are sitting, it is.

Build *with* a named stakeholder, then get them asking their own second question in the app.

---

## What we can honestly claim in outreach

**Available now:**
- Paying customers in manufacturing/distribution
- Ingestion and modeling proven on a 30-year-old IBM Informix ERP (orders + warehouse ops), including per-team walled gardens
- ModMed EMA ingestion proven (healthcare, for later)
- Direct connection today to SQL Server, PostgreSQL, MySQL, Google Sheets, CSV with auto-append
- AI never sees raw data — schema and business rules only
- Self-hosted deployment available

**Not yet:**
- Named logos or customer quotes
- Usage, adoption, time-saved, or ROI figures
- Any claim implying a customer runs self-serve analytics day to day

Keep the distinction. The technical proof points are strong on their own and a legacy-ERP buyer finds them more credible than a logo.

---

## Open questions

1. **Vertical sign-off** — manufacturing/distribution for round 1, or is there a reason to lead with healthcare?
2. **Geography** — is the Midwest/Northeast start right, or should it be national from the outset?
3. **Supplementary data source** — worth paying for installed-ERP data (BuiltWith/Apollo/ZoomInfo), or run on Sales Nav proxies first?
4. **Dynamics GP end-of-life (2029)** — worth building a dedicated campaign around the forced migration? ~68K customers facing a decision is a rare, dated, universal hook.
5. **Sequencing vs. the LinkedIn launch** — does outbound start before, during, or after the founder announcement? Prospects will check Arthur's profile.
