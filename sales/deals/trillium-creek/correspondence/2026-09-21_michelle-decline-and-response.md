# Trillium Creek — Decline and Response

Full email thread, most recent first. Michelle declined on Sep 21; Scott/Arthur responded same day.

---

## 2026-09-21 — Scott to Michelle (response to decline)

**From:** Scott Binger  
**To:** Michelle Maynard  
**CC:** Arthur Dobelis, Aaron Funk

Hi Michelle,

Thank you for the thoughtful note and for being open with us. We completely understand and appreciate the opportunity you gave us to learn more about your business and reporting needs.

I do want to leave you with a few important thoughts, because I think there are meaningful distinctions between using a general-purpose AI tool like ChatGPT for analysis and what we built Dashbud to do, particularly when patient data is involved, but also for data governance and consistency and scaling your reporting.

**PHI: privacy, compliance, and sending data to AI platforms.** We designed Dashbud with PHI and other sensitive data in mind, and it works very differently in this way. Dashbud uses the structure, schema, and business context of the data to generate queries and analysis. The underlying patient level data does not need to be sent to the AI model. This contains compliance risk and potentially catastrophic data leakage; something to consider before you vibe code your own data solution.

**Reporting reliability and accuracy; providing guardrails against hallucinations.** General purpose AI can produce very convincing analysis even when it does not fully understand the business rules or is missing the data it needs. If it generates Python code, calculations, or transformations behind the scenes, someone ultimately needs to be able to validate that logic and confirm that the resulting numbers are correct. We use AI extensively ourselves and have seen firsthand how confidently an AI model can fill in gaps or make assumptions when it does not have the information it needs. That is why Dashbud uses AI within significant guardrails. We intentionally constrain what the AI can do, give it the appropriate schema and business context, and rely on the underlying data platform to execute the actual queries and calculations. The goal is not simply to produce an answer that looks right, but to provide reporting that can be understood, repeated, and validated.

**Providing a smooth, repeatable process and a shared, governed data source.** Dashbud is designed to turn analysis into a repeatable reporting environment. It can apply consistent definitions and business logic, create interactive visualizations, save and reuse reports, and allow multiple users to work from the same governed data source, which happens to be a high-performance database. Uploading a new file is also a managed process that does not make a call to AI that might work as expected or not: as you upload files, Dashbud builds out this shared, governed data source.

**Not a general AI replacement.** Dashbud is not a replacement for ChatGPT -- they solve different problems. ChatGPT is an extremely capable general purpose AI tool. Dashbud was built specifically to provide an AI assisted analytics and reporting layer over an organization's business data, with particular attention to accuracy, consistency, governance, and data privacy. ChatGPT is a Swiss Army knife and it's good at everything, but it isn't really great at keeping data safe, creating shared data resources, and many of the other processes Dashbud has mastered. To be clear, you can do all of that by vibe-coding data app in ChatGPT, but you will spend hundreds of hours to account for the issues that arise. Dashbud assumes that's not your goal, and that you have more relevant ways to spend your time.

**And, you can use both.** Understanding that Dashbud won't solve every workflow need, we have equipped Dashbud with an API that will let your general-purpose GPT workflow leverage Dashbud's conversational data reporting interface, with full protection for PHI. This allows you to leverage Dashbud's strengths as the "data analyst" and/or "data resource" for your AI-based workflows.

Thank you again, and we hope you understand the spirit of these notes. We appreciate your time and respect your decision; we just want to put some of these distinction in mind as you continue evaluating how you want to use AI. If you are open to it, we would love to take 20 or 30 minutes to better understand what you have found works well with ChatGPT and other AI tools, and where Dashbud may not have met your needs. We aren't trying to change your decision -- your feedback is very valuable to us as we continue developing the platform.

Sincerely,
Scott

---

## 2026-09-21 — Michelle to Scott and Arthur (decline)

**From:** Michelle Maynard <mmaynard@tcohio.com>  
**To:** Arthur Dobelis, Scott Binger  
**CC:** Aaron Funk

Hi Scott and Arthur,

I wanted to follow up and be open and honest about where we are with Dashbud.

Since we first met, we have continued diving deeper into AI and exploring what we can accomplish with other AI tools, including ChatGPT. Through that process, we've found that we are able to accomplish the reporting and analysis we were looking for, along with quite a bit more, in a way that we feel is ultimately a better fit for our needs.

Because of that, we've decided that we do not want to move forward with Dashbud at this time.

I do want to sincerely thank both of you for the time and effort you've put into this. We recognize that you spent a considerable amount of time reviewing our data, recreating our reports, and working with us to demonstrate what Dashbud could do, and we truly appreciate it.

This decision is really about finding the solution that makes the most sense for us as we continue exploring how we can incorporate AI into more of our workflows.

Thank you again for all of your help and responsiveness throughout the process. We appreciate your efforts and wish you and the Dashbud team the very best.

Michelle Maynard, MBA, CCS-P
Director of Operations, Trillium Creek Dermatology

---

## 2026-09-17 — Arthur to Michelle (invite link follow-up)

**From:** Arthur Dobelis  
**To:** Michelle Maynard, Scott Binger, Aaron Funk

Just confirming you got the resent link from a few minutes ago.

---

## 2026-09-17 — Arthur to Michelle (resending invite)

**From:** Arthur Dobelis  
**To:** Michelle Maynard, Scott Binger, Aaron Funk

Understood, I'll resend the link to both you and Aaron.

---

## 2026-09-17 — Michelle to Arthur (expired link)

**From:** Michelle Maynard  
**To:** Arthur Dobelis, Scott Binger, Aaron Funk

I found it, it went to junk. I tried and it said the link is expired.

---

## 2026-09-17 — Arthur to Michelle (invite instructions)

**From:** Arthur Dobelis  
**To:** Michelle Maynard, Scott Binger, Aaron Funk

Hi Michelle,

Yes, you and Aaron both should have received a new account invitation on Sept 2. If you didn't see it, it probably went to your Spam/Junk folder. The email is from Dashbud <hello@app.getdashbud.com>, with the subject line "Welcome to Dashbud." It links you to an account creation page.

Let me know if you don't find it, or have any other issues, please let me know. When you are in your account, you will see the new reports.

Arthur

---

## 2026-09-17 — Michelle to Arthur (login question)

**From:** Michelle Maynard  
**To:** Arthur Dobelis, Scott Binger, Aaron Funk

Thank you, we took a look at the attached. As for the dashboard, I received a few emails, and it takes me to a log in page. Do we need to create accounts to view?

---

## 2026-09-16 — Arthur to Michelle (reports delivered)

**From:** Arthur Dobelis  
**To:** Michelle Maynard, Scott Binger, Aaron Funk

Hi Michelle,

We have reproduced your monthly reports in Dashbud using the August data. Here is where things stand with each of the reports:

- **Patients Seen Per Provider/Provider Totals:** reproduced, appointment counts per provider match July patterns.
- **Charges Per Provider/Visit Averages:** reproduced in both DOS (service date) and Posted Date versions. Note: encounter counts use distinct Bill IDs to avoid double-counting charge lines.
- **New Patients Per Location:** reproduced. New patients defined as visits billed with new patient E/M codes (99202-99205).
- **New Patients Per Provider:** reproduced, including per-location breakdown.
- **New Patients Per Brunswick and Strongsville:** covered by the per-location report above (no separate report needed)
- **Cosmetics Per Procedure:** reproduced. August procedures matched to your category names (Botox, Hair Laser, Hydrafacial, etc.). Note: we filter by CPT description, not appointment type.
- **Aesthetic Cosmetic Report:** this is the monthly total from the Cosmetics report, covered above
- **Botox Average Units:** reproduced. Units, encounters, and avg units per provider
- **E/M Codes (Part A + B):** reproduced. Includes both new patient (99202-99205) and established (99211-99215) codes, counted by distinct encounters per provider.
- **RN Appointment Types:** reproduced. Appointment type counts per RN/LPN provider
- **Online Scheduling:** reproduced, with a new breakdown by scheduling source (Klara vs EliseAI)
- **Patient Count by City/Location:** reproduced. Top cities per location. Also added a zip code version
- **Billing Provider Meeting Report:** this is a compilation of the above metrics into a per-provider scorecard. We have a working version that combines patients seen, avg visit charge, avg Botox units, and E/M distribution in Dashbud.

**Gaps:**
- **HH Sales:** this does not appear to be available in the EMA data exports we have. Is this tracked in a separate system?
- **Chart Audit counts:** same, not in the production or appointment data. Where does this come from?
- Some provider initials in the weekly Provider Totals sheet (DPK, MMC, REM, SMD, DLP, FAE, SGM) use a different abbreviation system than the other reports. We mapped the standard initials but couldn't match these. Can you confirm who these are?
- We haven't gone into those marked "questionable" yet. Let's discuss which ones would be valuable and what data sources they rely on.

I've provided a July-August comparison attached as an Excel sheet. I will share the Dashbud composite reports in the form of a composite report/dashboard shortly.

The comparisons look reasonable on their face. One thing that might be helpful is if you could provide the three core EMA data exports (appointments, service by DOS, and service by posted date) for July. We could then run your July numbers in Dashbud and confirm they match your own reports closely.

Let me know if you have any questions, and let's meet to discuss at your convenience.

Arthur

---

## 2026-09-15 — Michelle to Arthur (answers to data questions)

**From:** Michelle Maynard  
**To:** Arthur Dobelis, Scott Binger, Aaron Funk

Thank you for your follow up. See my responses below.

> Confirming: the data you provided are August-only.

Correct

> Confirming: the DOS Production Summary and Posted Date production summary appear to be the same data filtered differently.

Correct

> There isn't a single unique ID provided...

I'm sorry I'm not following the question.

> Some reports are listed as "questionable." Do you want me to reproduce those?

These reports I wasn't sure if it was possible. If it is sure go ahead, if not that's fine too. Just let me know.

---

## 2026-09-15 — Arthur to Michelle (data questions)

**From:** Arthur Dobelis  
**To:** Michelle Maynard, Scott Binger, Aaron Funk

Hi Michelle,

Thanks for these responses. Regarding the unique-id question for the production table, I'll proceed with the data as is. The issue is not a blocker at all. I'll explain further and we can discuss it after I've produced and shared the reports.

Arthur

---

## 2026-09-15 — Arthur to Michelle (initial data review)

**From:** Arthur Dobelis  
**To:** Michelle Maynard, Scott Binger, Aaron Funk

Hi Michelle,

The data looks very good. I'm in the process of reproducing your reports. A few notes:

- Confirming: the data you provided are August-only.
- Confirming: the DOS Production Summary and Posted Date production summary appear to be the same data filtered differently – based on posted date vs. date of service.
- Unique ID question for deduplication and append process.
- Some reports are listed as "questionable" — do you want me to reproduce those?

I aim to share a full set of reports by COB today, tomorrow morning latest.

Arthur

---

## 2026-09-15 — Michelle to Arthur (checking in)

**From:** Michelle Maynard  
**To:** Arthur Dobelis, Scott Binger, Aaron Funk

Good morning, I just wanted to check and see how it is going and whether or not you have any questions.

---

## 2026-09-10 — Arthur to Michelle (acknowledging data)

**From:** Arthur Dobelis  
**To:** Michelle Maynard, Scott Binger, Aaron Funk

Hi Michelle, Excellent. We're looking at this now and will get back to you with any questions we may have.

---

## 2026-09-10 — Michelle to Scott (data and reports shared)

**From:** Michelle Maynard  
**To:** Scott Binger, Aaron Funk  
**CC:** Arthur Dobelis

I have attached a few documents:
- Compiled list of reports with comments
- Cheat sheet of how we run certain reports
- Cosmetic CPT code list used for some reports
- Google Drive link with all sample reports and August data exports

---

## 2026-09-10 — Scott to Michelle (ready for data)

**From:** Scott Binger  
**To:** Michelle Maynard, Aaron Funk  
**CC:** Arthur Dobelis

Thanks so much. Yes, please start sending over data pulls from ModMed.

---

## 2026-09-10 — Michelle to Scott (agreements signed)

**From:** Michelle Maynard  
**To:** Scott Binger, Aaron Funk  
**CC:** Arthur Dobelis

Attached are the countersigned agreements. If you are good, I can start sending you data pulls from ModMed and sample reports.

---

## 2026-09-09 — Scott to Michelle (minor changes to docs)

**From:** Scott Binger  
**To:** Michelle Maynard, Aaron Funk  
**CC:** Arthur Dobelis

We made a few minor changes to the docs. If you're okay with these, we will sign right away and return them.

---

## 2026-09-08 — Michelle to Scott (following up on docs)

**From:** Michelle Maynard  
**To:** Scott Binger, Aaron Funk  
**CC:** Arthur Dobelis

I just wanted to follow up and see where we are with this. We close the month today and would typically start running reports tomorrow.

---

## 2026-09-02 — Michelle to Scott (NDA and BAA sent)

**From:** Michelle Maynard  
**To:** Scott Binger, Aaron Funk  
**CC:** Arthur Dobelis

Please see the attached BAA and NDA for your review and signature. Once I receive the signed agreements, I will provide countersigned copies along with the sample reports.

---

## 2026-09-01 — Scheduling call for file upload walkthrough

Scott proposed 2:30. Michelle offered times Wed/Thu.

---

## 2026-08-31 — Michelle to Scott (file upload instead of API)

**From:** Michelle Maynard  
**To:** Scott Binger, Aaron Funk  
**CC:** Arthur Dobelis

In light of the $25/month/provider fee from ModMed, we were hoping to pause on the integration for now and instead move forward with a trial where I upload the data from ModMed directly. I believe you mentioned this as a possibility during our call.

---

## 2026-08-27 — ModMed API fee

**From:** Scott Binger

They did mention a fee of $25/month/provider.

**From:** Michelle Maynard

Did they happen to say if there is a fee associated with setting this up, or a monthly fee?

---

## 2026-08-26 — Scott to Michelle (ModMed API instructions)

**From:** Scott Binger  
**To:** Michelle Maynard, Aaron Funk  
**CC:** Arthur Dobelis

To proceed with Dashbud, you need to contact the ModMed Practice Solutions team (practicesolutions@modmed.com) and request a form to establish an API connection. They will then provide important API credential information which you should provide to us so that we can establish the connection to your ModMed data.
