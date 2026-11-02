---
account_id: omega-molding
name: Omega Molding
type: customer
deal_type: subscription
arr: 7200
seats: 7
industry: Building materials distribution (framing supply)
revenue: ~$50M
employees: ~50
sites: 8 warehouses
erp: IBM Informix (~30 years old)
erp_tier: B
ownership: PE-backed (formerly family-owned)
source: referral
contract_effective: 2026-05-11
contract_term_months: 12
renewal_type: auto
renewal_notice_days: 30
decision_point: 2027-04-11
icp_fit: high
---

# Omega Molding

**First paying Dashbud customer.** 7 annual licenses, $7,200/yr.

## Why they matter beyond the revenue

The prototype ICP account: mid-market distributor, legacy ERP, no data team, newly PE-owned. Everything in the Sales Navigator targeting criteria is modeled on this company.

## Contract

Effective 2026-05-11, 12-month initial term ending ~2027-05-11. Auto-renews for successive one-year terms unless either party gives written notice at least 30 days prior — so **the real decision point is ~2027-04-11**.

Includes a monthly-retainer provision for professional services, a possible vehicle for a recurring reporting cadence.

*Note: the Effective Date is bracketed in the subscription agreement (`sales/legal/deals/omega-moulding/subscription-agreement.md`), which may mean it was a template placeholder. Worth verifying.*

## People

| Person | Role | Notes |
|---|---|---|
| Dan Peters | CTO | Signed the contract. Main contact. Referred Scott to Dashbud (not an Evolytix client) |
| Robert | CEO | |
| *(name unknown)* | Fractional CFO | **The real stakeholder.** Needs this reporting most; would be the actual user |

## Technical proof points (reusable)

POC proved ingestion and modeling on a large IBM Informix ERP dataset — orders plus warehouse ops — including walled gardens so each sales team sees only its own data. This is reusable evidence for any manufacturing/distribution prospect, independent of how this account develops.

## Standing risk: adoption

They pay and nobody logs in. Value has been delivered as a service (Arthur-built reports) rather than through the product. Consequences:

- No usage-and-outcomes case study available — only capability and traction claims
- A zero-usage customer going into the April decision point is exactly who sends a non-renewal notice
- Auto-renewal favors us via inertia, but that is a thin thread

**Why it happened:** newly PE-owned former family business still getting organized. Organizational churn, not disinterest — a better prognosis than Trillium Creek, where the champion actively chose an alternative.

**The play:** make the fractional CFO the adoption beachhead. Build reports *with* them, not *for* them, and use a cadence to get them asking their own follow-up questions in the app.
