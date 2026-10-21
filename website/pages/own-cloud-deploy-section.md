# Why Dashbud section: Deploy in your own cloud

**Status:** DRAFT, 2026-10-20. Claude's first pass for Arthur to edit. Facts are limited to what Arthur has confirmed; gaps are marked.

**Placement:** Why Dashbud, immediately after Trust & Privacy, as its own section with `id="your-cloud"` and `scroll-mt-24`. Same reading-width layout as Trust & Privacy.

**Link targets to point here:**
- `/enlightened`: the "Deploy Dashbud in your own cloud for compliance" line under Enterprise → `/why-dashbud#your-cloud`
- `/pricing`: new Enterprise bullet → `/why-dashbud#your-cloud`
- Trust & Privacy "Full audit trail" item: add "or in your own cloud" as a link to the anchor

---

## Heading

Deploy Dashbud in your own cloud

## Lead

For organizations where data can't leave the building, even a managed one, Dashbud runs entirely inside your cloud account. Same product, same AI agents, same governance. The infrastructure is yours.

## Body

* **Your account, your perimeter.** The full Dashbud stack deploys into an AWS account you control. Your data, your queries, and your semantic model never leave it.
* **Push-button deployment.** Deployment is automated end to end. A new environment is a pipeline run, not a professional-services engagement. [GAP: typical time from go-ahead to running environment, e.g. "under a day".]
* **Same guardrails.** AI agents still work from schema and business rules, not raw values. Workspace scoping, audit trails, and deterministic reports all apply, now inside your own boundary.
* **Updates and support.** [GAP: who runs updates after deployment, Dashbud or the customer? Is there a support or maintenance agreement? One sentence.]

## Availability

AWS today. Azure deployment has been scoped and is available on request as a paid implementation. [GAP: confirm you want Azure stated this plainly on the page, and whether GCP gets a mention.]

## Closing line and CTA

Talk to us about an own-cloud deployment → *(link: contact or book-demo)*

---

## Notes for Arthur

* I kept "AWS today" explicit rather than "any cloud." You said you'd be forthright about Azure timing in conversation; stating it on the page avoids the question being a surprise.
* "Same guardrails" is the bullet that ties this back to the Trust section above it. If it feels redundant on the page, cut it; the lead already says "same governance."
* The two GAPs on deployment time and post-deploy operations are the questions an enterprise buyer asks first. Worth filling before this goes live.
