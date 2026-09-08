# Trillium Creek (HMT) — NDA & BAA Review Notes

Reviewed 2026-09-08. Documents provided by HMT Dermatology Associates for Dashbud to sign.

## NDA

### One-way structure
Dashbud is "Recipient" throughout — HMT discloses, Dashbud protects. Nothing covers information Dashbud shares with HMT (pricing, architecture, roadmap). **Consider requesting mutual NDA or adding a reciprocal clause.**

### AI/model training (§4)
Prohibits using HMT data to train any AI model. Dashbud's architecture shares schema and (with user confirmation) low-cardinality column values with the LLM — never row-level data. Compliant by design. Confirm: no HMT data in error logs or telemetry beyond what's in the confirmed LLM context.

### 24-hour incident notice (§7)
Tight timeline. Need an operational process: who monitors, who contacts HMT, how.

### No publicity (§11)
Cannot reference HMT/Trillium Creek in marketing, case studies, demos, customer lists, or social without prior written consent. Applies to pitch decks too.

### 5-year survival (§13)
Obligations persist 5 years after relationship ends.

### Ohio law/venue (§15)
Litigation in Ohio courts.

## BAA

### No AI/model training (§3)
Same prohibition, specific to PHI. Dashbud's architecture:
- **Schema** (table/column names, types, relationships) → always shared with LLM
- **Low-cardinality column values** → shared with LLM only after explicit user confirmation
- **Row-level / high-cardinality data** → never transits LLM API
- **Query results** → returned directly to user's browser, never sent to LLM

For HMT, low-cardinality values (procedure codes, statuses, payer names, locations) are unlikely to be PHI on their own. But the user confirmation step is the key control: HMT's own users decide what gets shared, and the system prompts before it happens. This is a defensible "minimum necessary" implementation under the BAA.

**Position for HMT:** "Row-level data never touches the LLM. Low-cardinality reference values are only shared with explicit user confirmation." More accurate and auditable than claiming PHI never touches the LLM at all.

### Safeguards (§4)
Specific requirements:
- [x] Encryption in transit (TLS)
- [x] Encryption at rest
- [x] Audit logging — can generate on demand
- [ ] Documented risk analysis (see action items)
- [ ] Workforce training (HIPAA training for team)
- [ ] Access controls based on job responsibilities
- [ ] Vulnerability/patch management documentation

### 24-hour breach notification (§5)
Same tight window as NDA.

### Subcontractors (§6)
All subcontractors will sign our BAA and NDA. Need to execute with:
- [ ] Cloud hosting provider (AWS/GCP/etc.) — standard BAA available
- [ ] Database hosting
- [ ] LLM provider — only if PHI transits their API (low-cardinality values with user confirmation; likely needed)
- [ ] Any other service that could touch HMT data

Must notify HMT before adding a new subcontractor or changing PHI hosting location.

### Individual rights (§7)
Must support: data export on request, record amendment, accounting of disclosures. 10 business day response window, 3 business days to forward individual requests.

### Data portability (§10)
Must provide complete, usable export on request or at termination. Cannot withhold data over payment dispute.

**Dashbud's position is strong here:** Dashbud connects to the customer's own data sources and generates reports live — it does not store their source data. At termination, the deliverable is their semantic model configuration and any imported files (e.g., CSVs). Their source data never left their systems. No need to volunteer this architecture detail proactively, but if asked: "We can export your configuration and any imported data. Your source data never leaves your systems."

### Uncapped breach liability (§13)
If a breach is Dashbud's fault, Dashbud pays all costs — investigation, notification, credit monitoring, regulatory response. **No cap. Consider negotiating a liability cap.**

## Entity structure

Dashbud is currently a general partnership (Arthur & Scott, d/b/a Dashbud). No corporate entity yet. Both documents need:
- Signature block filled as general partnership trading as Dashbud
- Addendum pre-authorizing assignment to a successor corporate entity upon formation, with written assumption of all obligations and prompt notice to HMT
- Addendum should explicitly supersede the assignment restrictions in NDA §16 and BAA §15 for this specific purpose

**Note:** Until incorporation, Arthur and Scott are personally liable under both agreements — including the uncapped breach liability in BAA §13. Reason to incorporate sooner and to push for a cap.

## Operational readiness: monitoring & incident response

### Uptime monitoring (not required by BAA, but operationally useful)
- Set up a heartbeat monitor (Betterstack, Uptime Robot, or cron + curl) against app health endpoint
- Alert via SMS/email if stack is down
- ~20 minutes to set up

### Breach/incident detection (supports BAA §5 and NDA §7)
The 24-hour clock runs from "discovery or reasonable suspicion." For a two-person team, realistic detection surface is:
1. **Cloud provider security alerts** — enable and route to a monitored inbox (unauthorized API calls, IAM changes, unusual access patterns)
2. **Database access alerts** — failed auth attempts, connections from unexpected IPs
3. **Application audit logs** — already available on demand; look for anomalous query patterns or access from deactivated users
4. **Dependency monitoring** — Dependabot or equivalent for known vulnerabilities

### Incident response process
Doesn't need to be elaborate. Needs to exist and be documented:
- Either Arthur or Scott can trigger the process
- Step 1: flag it, preserve evidence
- Step 2: notify HMT within 24 hours (even on suspicion — supplement later as info becomes available)
- Step 3: investigate, mitigate, document
- BAA §5 specifies: do NOT notify individuals/regulators/media on HMT's behalf unless directed

## Action items

1. **Decide:** request mutual NDA or accept one-way?
2. **Negotiate:** liability cap in BAA §13?
3. **Draft:** entity assignment addendum for both documents
4. **Document architecture:** schema + confirmed low-cardinality values only; row-level data never transits LLM
5. **Operational readiness:**
   - [x] Audit logging — on demand
   - [x] Encryption in transit and at rest
   - [ ] Breach notification process — document the 3-step process above
   - [ ] Cloud provider security alerts — enable and route to monitored inbox
   - [ ] Uptime monitor — set up heartbeat ping
   - [ ] Documented risk analysis — HIPAA Security Rule (45 CFR § 164.308(a)(1)). Written doc: what PHI you handle, threats, current safeguards, residual risk. A few pages given Dashbud's minimal-PHI architecture. HHS has a free Security Risk Assessment tool, or write it up as a structured doc. Point is it exists.
   - [ ] HIPAA training
   - [ ] Dependency monitoring (Dependabot or equivalent)
6. **Subcontractor BAAs/NDAs:** inventory services, execute with all subs
7. **Data export:** ✓ can export config + imported data; source data never leaves customer's systems
8. **No publicity:** get separate written consent if we want to reference TC in marketing
9. **Incorporate:** form corporate entity, execute assignment
