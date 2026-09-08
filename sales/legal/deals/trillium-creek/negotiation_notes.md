# Trillium Creek — Negotiation Notes

Internal only. Do not share with HMT.

## Document stack

1. **NDA** (HMT's form) + **Addendum** (mutual confidentiality, publicity consent, entity assignment)
2. **Subscription Agreement** (our form, based on Omega precedent)
3. **BAA** (HMT's form) + **Addendum** (liability cap, entity assignment)

Signing order: NDA first → Subscription Agreement → BAA. NDA protects the deal discussion; subscription agreement defines the commercial terms the BAA references.

## Pricing

**Key context:** ModMed's synapSYS API costs $25/provider/month. TC has 14+ providers = $350+/month just for API access to their own data. Dashbud sidesteps this entirely by ingesting exports — that's a significant value add, not a cost center. TC saves $350+/month by using Dashbud instead of paying for the API.

**Demo discussion:** Quoted $40/seat/month annual, $50/seat/month monthly, 2-seat minimum. At 2 seats = $80–$100/month.

**Omega precedent:** $79/seat/month × 5 users ($4,740/year). Omega also uses export ingestion (IBM Informix → CSV → Google Drive).

**Pricing question:** At $80/month for 2 seats, Dashbud costs less than a quarter of what the ModMed API alone would run. That's arguably too cheap given the value delivered — but TC is the second customer and a healthcare reference account. Consider whether per-seat pricing captures enough value here, or whether a practice-level or provider-based component makes sense for healthcare going forward. This is a platform-level question, not just TC.

## Liability structure

**General cap:** 3 months' platform fees (excluding professional services). Matches Omega precedent. Appears in both the subscription agreement §12 and BAA addendum §1(b).

**Elevated cap:** Fixed dollar amount for PHI/privacy/confidentiality breaches. In BAA addendum §1(c) only. Pick a number — $250K–$500K is typical for mid-market SaaS. HMT will likely push higher. This is the main negotiation point.

**Consequential damages waiver:** Mutual, in both subscription agreement §12 and BAA addendum §1(a). If HMT's counsel pushes to carve out PHI breaches from the waiver, resist — consequential damages from a PHI breach are exactly the open-ended exposure that could sink a startup. The elevated cap already covers the real direct costs (notification, investigation, credit monitoring).

**No carve-outs offered.** If HMT's counsel asks for uncapped liability for willful misconduct / intentional unlawful disclosure, that's a reasonable concession — but let them ask. Don't volunteer it.

**Gross negligence:** If they push for gross negligence as a carve-out, resist. Too easy to allege past MTD, which makes the cap meaningless because discovery costs become the leverage. Gross negligence is already covered by the elevated cap.

## Governing law

- NDA/BAA: Ohio (HMT's documents, their jurisdiction — fine)
- Subscription agreement: New York (our standard, matches Omega)
- If HMT pushes for Ohio on the subscription agreement, it's a reasonable concession. BAA addendum already controls for PHI matters.

## Trial-to-paid conversion

The publicity consent in the NDA addendum (§2) triggers on first payment, not trial start. The subscription agreement (§5) explicitly handles trial periods. Keep these aligned.

## Semantic model IP

The subscription agreement §10 keeps it simple: Customer owns their data and model configurations, Provider owns the platform. Dropped the "reuse structural patterns" clause from the earlier draft — not worth the complexity for a first healthcare deal.

## Professional services

Included in subscription agreement §7 but flexible — no Exhibit B or retainer required upfront. Framework is there for when onboarding work needs billing.

## Items to decide before sending

- [ ] Elevated cap dollar amount
- [ ] Pricing — per-seat only, or add a practice/provider component for healthcare?
- [ ] Annual vs monthly billing
- [ ] Whether to include IP indemnification (consider for later, not this deal)
- [ ] TOU (Exhibit A) — needs updating (Evolytix → partnership, AI language, "Payroll Solution" title)
