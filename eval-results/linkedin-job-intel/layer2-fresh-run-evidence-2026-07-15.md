# linkedin-job-intel — Layer 2 Fresh Run Raw Evidence (captured 2026-07-15)

**Status: RAW EVIDENCE — not yet graded.** This is the output of a fresh, independent Layer 2 Global Talent Filter run, executed specifically to serve as real evidence for the new Assertion Auditor VA -> Verdict VA -> Skeptic VA (cross-vendor) grading gate, as a check for self-preference bias in the 2026-07-09 eval grading (which had no retained raw transcript — see eval-methodology.md).

**Data source:** real, already-collected 2026-07-14 batch (`raw_jobs_2026-07-14.md` + `raw_jobspy_2026-07-14.md`, 182 total raw jobs, Source A+B+D). This batch's Layer 2/3 had already run and pushed once that day as part of the normal daily pipeline (`push_2026-07-14.json`); this is a second, independent Layer 2 pass over the same raw data, run in isolation, for eval purposes only.

**Rules version applied:** `layer2-rules.md` as patched 2026-07-14 (the blank-location vs. named-location-silent-on-remote split, fixed after a subagent conflation incident on the 07-12–07-14 batch misclassified 194 jobs as BORDERLINE instead of EXCLUDED — see `claude.md` Troubleshooting Log, 2026-07-14).

**Niches filtered:** Business Analytics, Web Analytics.

**No files were written and nothing was pushed to any tracker as part of this run** — evidence-gathering only, per the instructions given to the subagent that produced it.

---

## Summary table

| | PASSED | BORDERLINE | EXCLUDED | Total |
|---|---|---|---|---|
| raw_jobs (A+B) | 24 (24 JOB / 0 POST) | 4 (3 JOB / 1 POST) | 84 | 112 |
| raw_jobspy (D) | 0 | 5 (5 JOB / 0 POST) | 65 | 70 |
| **Combined** | **24 (24 JOB / 0 POST)** | **9 (8 JOB / 1 POST)** | **149** | **182** |

---

## PASSED (24)

**1–5, individually reasoned:**

- **Job 19 [raw_jobs]: Business Analyst (Product-Focused) — Codekeeper — Location: "South Africa"** `[JOB]`. Description overrides header field: *"Job Location: Remote"*, company described as "remote-first," no country/region qualifier anywhere in the text. Rule: INCLUDE — "No location restriction stated at all AND the role is clearly remote-friendly in context." Niche: title is literally Business Analyst; core work is requirements gathering/specs — Business Analytics fit.
- **Job 23 [raw_jobs]: Junior Data Analyst — Mwanga — Location: "Nigeria"** `[JOB]`. Work Mode: Onsite, Maryland, Lagos. Rule: Strict Mode — "Each user has exactly ONE exempt country where a non-remote, in-office role is still acceptable... Anthony -> Nigeria." Onsite in Nigeria passes regardless of remote status. Niche: KPI reporting, dashboards, data analysis — Business Analytics fit.
- **Job 24 [raw_jobs]: Junior Data Analyst at Mwanga Limited — Mwanga — Location: "Lagos, Lagos State, Nigeria"** `[JOB]`. Same role/company, distinct URL/posting. Same exempt-country reasoning as Job 23.
- **Job 28 [raw_jobs]: Commercial and Business – Business Analyst I – Amaiden Energy Nigeria Ltd — MyPetroCareer.com — Location: "Nigeria"** `[JOB]`. Exempt country (Nigeria) -> onsite acceptable. Niche: core Business Analyst functions (requirements gathering, process mapping, documentation).
- **Job 29 [raw_jobs]: Business – Business Analyst III — MyPetroCareer.com — Location: "Nigeria"** `[JOB]`. Same reasoning as Job 28 (senior-level version of the same role family).

**6–24, TalentPop App cluster (SEO Assistant / SEO & Growth Assistant (Remote)):** All 19 postings share materially identical description text: *"SEO Assistant (Remote) – Join the TalentPop Team!... to join our growing remote team!... Remote-first workplace..."* No country/region-restriction phrase appears in any instance (only "UK Hours"-type qualifiers appear elsewhere, e.g. Job 86, not here). Rule applied: INCLUDE — no location restriction stated + remote-friendly context confirmed in text (title tag "(Remote)" / "growing remote team"). Search Term Match: web analytics on every entry; content confirms Google Analytics, Ahrefs, SEMrush, GA reporting — Web Analytics niche fit. South Africa-field entries pass on the same unqualified-remote basis (no explicit SA-only restriction text), Nigeria-field entries additionally pass via the exempt-country rule.

| Job # | Location field | Company | URL job-ID |
|---|---|---|---|
| 61 | South Africa | TalentPop App | 4434876585 |
| 62 | Johannesburg, Gauteng, South Africa | TalentPop App | 4434874760-ish (Johannesburg posting) |
| 63 | Durban, KwaZulu-Natal, South Africa | TalentPop App | — |
| 64 | Pretoria, Gauteng, South Africa | TalentPop App | — |
| 66 | Soweto, Gauteng, South Africa | TalentPop App | — |
| 67 | Stellenbosch, Western Cape, South Africa | TalentPop App | — |
| 68 | Cape Town, Western Cape, South Africa | TalentPop App | 4434874760 |
| 69 | Stellenbosch, Western Cape, South Africa | TalentPop App | 4434877574 |
| 70 | South Africa | TalentPop App | 4434876499 |
| 71 | Nigeria | TalentPop App | 4434878605 |
| 72 | Nigeria | TalentPop App | 4434882291 |
| 73 | Nigeria | TalentPop App | — |
| 74 | Nigeria | TalentPop App | 4434875614 |
| 75 | Nigeria | TalentPop App | — |
| 76 | Nigeria | TalentPop App | 4434871593 |
| 77 | Nigeria | TalentPop App | 4434883295 |
| 78 | Nigeria | TalentPop App | — |
| 79 | Nigeria | TalentPop App | 4434886274 |
| 80 | Nigeria | TalentPop App | — |

**Caveat flagged by the subagent, not applied unilaterally:** these 19 are the same template reposted separately per South African city and per Nigeria — a pattern that in practice often signals country-scoped hiring drives rather than genuine global remote. The raw text itself contains no explicit restriction phrase, so per a literal reading of the rules as written this is 19x PASS. The subagent did not downgrade this based on the repost pattern alone, since its instructions required classifying only on what the raw text literally says. Recommended: a human sanity-check on whether "no restriction found across 19 near-identical city-specific postings" should itself trip a rule.

No jobspy-source jobs passed (0). Every JobSpy-collected listing either named a specific non-exempt location with no remote confirmation, was blocklisted, or resolved to a country/timezone-qualified remote.

---

## BORDERLINE (9)

- **Job 15 [raw_jobs]: Business Intelligence Manager — Smart4 Energy — Location field: "South Africa"** `[JOB]`. Flag: contradictory location data — description says *"Engagement Model – Onsite/Remote Rotation... Hybrid model: 2 weeks onsite, 2 weeks remote per month. Gaborone"* (Gaborone is in Botswana, not South Africa). Rule: BORDERLINE — "the location field names one country/city but the title or description names another... don't guess which one is right, flag the contradiction."
- **Job 86 [raw_jobs]: SEO Specialist — Palm Outsourcing — Location field: "Egypt"** `[JOB]`. Description states *"Location: Remote/Online"* but *"Working Days and Hours: Monday to Friday, 9 AM - 6 PM (UK Hours)"*, salary in GBP/USD. Rule: BORDERLINE — "'Remote' stated but a secondary signal narrows the likely scope without fully confirming it — e.g. ... a named-timezone requirement (EST/PST)." Niche: strong Web Analytics fit (GA4, Google Search Console, Ahrefs/SEMrush).
- **Job 93 [raw_jobs]: Senior Power BI Business Analyst 100% Remote — HYR Global Source Inc — Location: "United States"** `[JOB]`. Text: *"Prefer USC/GC but open for all who Authorized to work."* This is a stated preference, not a hard "must be authorized/right to work in [country]" requirement. Rule: BORDERLINE — "A soft locational preference rather than a hard requirement... isn't a clear global confirmation either." Niche: excellent Business Analytics fit (Power BI, SQL, stakeholder requirements).
- **Job 97 [raw_jobs]: "Chitra Krishnakumar on LinkedIn: #hiring #powerbi #powerbideveloper..."** `[POST]`. No location field, no remote/onsite language anywhere in the post ("Opportunity for Power BI Developers! ... contact us"). Rule: BORDERLINE — "A listing with no location field and no remote language anywhere in the text is BORDERLINE, not PASSED... genuinely unknown." Niche: Power BI Developer role fits Business Analytics.
- **Job 10 [jobspy]: Junior Data Analyst — Helic & Co — Location field: blank** `[JOB]`. No location or remote/onsite language anywhere in body. Rule: BORDERLINE (blank-location branch of the patched split, exactly the case the patch was written for). Niche fit confirmed (data collection/analysis/reporting).
- **Job 11 [jobspy]: Business Intelligence Analyst — Codex — Location field: blank** `[JOB]`. No location stated, but *"Fluent German is required for the role"* narrows likely candidate pool without stating a country. Rule: BORDERLINE — genuine ambiguity, secondary signal narrows without confirming restriction. Niche: strong BI fit (Power BI, DAX, Azure).
- **Job 37 [jobspy]: Sr Marketing Analyst — Braintrust (client: Carrier) — Location field: blank** `[JOB]`. Full description read end-to-end; zero city/country/remote/onsite language anywhere. Rule: BORDERLINE (blank location, unresolved). Niche: strong fit — GA4, Power BI, marketing measurement.
- **Job 46 [jobspy]: Product Analyst Mentor — EnglishBhashi — Location field: blank** `[JOB]`. Full description read; no location/remote language at all. Rule: BORDERLINE. Niche: Product/Growth Analytics with Google Analytics, Amplitude, Mixpanel — fits.
- **Job 59 [jobspy]: BI & Data Engineer — Vimachem — Location field: blank** `[JOB]`. Long description read in full; no location or remote/onsite language found anywhere. Rule: BORDERLINE. Niche: BI/dashboard/reporting role (Metabase) — reasonable Business Analytics fit.

---

## EXCLUDED (149) — breakdown by reason

| Category | Count |
|---|---|
| Named non-exempt location, no remote confirmation anywhere in posting | 100 |
| Wrong niche (role clearly outside Business/Web Analytics once location resolved) | 27 |
| Country/timezone-qualified remote (not global) | 6 |
| Work authorization / visa sponsorship / W2 restriction | 5 |
| Blocklisted company (Crossing Hurdles) | 5 |
| Location-restriction phrasing ("based in [country]") | 3 |
| Onsite/hybrid requirement at named non-exempt office | 3 |
| **Total** | **149** |

**Examples per category (>=3 each):**

**Named location, no remote confirmation (100):**
- Job 2 [raw_jobs, JOB]: Junior Data Analyst — Helic & Co — "United States" — no remote/onsite language anywhere.
- Job 36 [raw_jobs, JOB]: Commercial Business Analyst — BURN — "Nairobi, Nairobi County, Kenya" — no remote language.
- Job 99 [raw_jobs, JOB]: Business Intelligence Developer — Apex Group Ltd — "Cape Town, Western Cape, South Africa" — no remote language (the "112 offices worldwide" line describes company scale only).
- Job 1 [jobspy, JOB]: Business Analyst — stc — "Riyadh, Riyadh, Saudi Arabia" — no remote language.
- Job 24 [jobspy, JOB]: Business Intelligence Developer — Base.com — "Poznań, Wielkopolskie, Poland" — no remote language.

**Wrong niche (27):**
- Job 1 [raw_jobs, JOB]: "Data Analyst Excel - Remote" — JobsInMass.com — AI-training-data annotation dressed as Data Analyst ("help train next-generation AI systems... no prior experience in AI required — your domain knowledge is what matters").
- Jobs 33, 34, 35, 44, 45, 47 [raw_jobs, JOB] (six postings): "Remote Business Analyst" — Turing — genuinely remote/global-confirmed but role is SxS evaluation/annotation/fact-checking of AI model outputs, not business analysis. This is the exact recurring Turing pattern the rules file names ("Turing has recurred repeatedly under this pattern").
- Jobs 22, 42 [raw_jobs, JOB]: "AI Data Quality Analyst" — Alignerr (South Africa, Egypt) — same AI-labeling pattern, remote-confirmed but wrong niche.
- Job 82 [raw_jobs, JOB]: "Digital Marketing Associate (Psychology Background)" — CloserMed — explicitly unqualified global remote ("fully remotely from anywhere in the world") but role is marketing/persuasion, not Business or Web Analytics.

**Country/timezone-qualified remote, not global (6):**
- Job 14 [raw_jobs, JOB]: Finsights — "remotely with clients across Canada and the US" (also niche-mismatched, Finance).
- Job 23 [jobspy, JOB]: StatusNeo, Junior Power BI Analyst — "Location: India (Remote)."
- Job 47 [jobspy, JOB]: StafinGo, Data Analytics Specialist — "Edmonton, Alberta, Remote."
- Jobs 56, 57 [jobspy, JOB] (two postings): Proxify, Senior MS Power BI Developer — marketing copy says "Talent has no borders," but the hard requirement states *"Time zone: CET (+/- 3 hours). We are unable to consider applications from candidates in other time zones."*

**Work authorization / visa / W2 (5):**
- Job 9 [raw_jobs, JOB]: AARATECH — "only able to consider candidates who are authorized to work in the United States without sponsorship."
- Job 95 [raw_jobs, JOB]: Delta System & Software — "US Citizen who are willing to work on W2 are advised to apply."
- Job 108 [raw_jobs, JOB]: Trility Consulting — "Must be authorized to work in the United States without sponsorship" + W2 restricted to a named list of US states only.
- Job 39 [jobspy, JOB]: Framna, Productstrateeg — "Wij bieden geen visa sponsorship aan" ("We do not offer visa sponsorship").

**Blocklisted company — Crossing Hurdles (5):**
- Job 10 [raw_jobs, JOB]: "Business Intelligence Analyst (Excel) | $50/hr Remote" — Crossing Hurdles.
- Job 17 [raw_jobs, JOB]: "Data Labeling Specialist | $80/hr Remote" — Crossing Hurdles.
- Job 94 [raw_jobs, JOB]: "Data Analyst (Excel) | $55/hr Remote" — Crossing Hurdles.
- Jobs 5, 7 [jobspy, JOB] (two postings): "Business Intelligence Analyst (Excel) | $50/hr Remote" — Crossing Hurdles.

**Location-restriction phrasing (3):**
- Job 7 [raw_jobs, JOB]: Jobgether — "Our partner is looking for a Sr. Market Intelligence & Business Analytics Manager based in United States."
- Job 58 [raw_jobs, JOB]: Jobgether — "Our partner is looking for a Sr Manager, Digital Ads based in the United States."
- Job 33 [jobspy, JOB]: Burjline Builders/DESIGN RANK INC — "This is a Full-time position based in Dallas, Texas, United States."

**Onsite/hybrid at named non-exempt office (3):**
- Job 98 [raw_jobs, JOB]: MRI Software — "hybrid working model with 3 days of working from home per week. This role is based in the Cape Town office."
- Job 102 [raw_jobs, JOB]: Orion Labs — "This is a full-time, on-site role at the client's Cape Town offices."
- Job 43 [jobspy, JOB]: Zero to One Search — title itself: "Team Lead Marketing Analytics (relocation to Munich)."

---

## Explicit checks against the three prior rule gaps (fixed 2026-07-09)

1. **Blocklisted company (Crossing Hurdles):** Yes, found — 5 separate postings this batch (3 in raw_jobs, 2 in jobspy), all correctly caught and excluded before any other check ran. The rules file's own note ("must be checked every run, it is not a one-time cleanup") is borne out — it recurred again.
2. **Location-restriction phrasing variant ("looking for [role] based in [country]"):** Yes, found — 3 instances, all correctly excluded (Jobgether x2, Burjline Builders/DESIGN RANK INC x1). Fix is holding.
3. **Bare "worldwide" keyword false-positive:** No false positives found. "Worldwide"/"globally" language appeared in at least 7 postings (Square, RingStone, TMF Group, P&G x2, BEE LOGISTICS, Autsorsa, Vimachem) and in every case it described the company's footprint, client base, or headcount — not applicant eligibility — so none were passed on that basis. 3 legitimate unqualified remote confirmations happened to use "worldwide"/"anywhere" correctly as a hiring-scope signal (Codekeeper "remote-first," CloserMed "fully remotely from anywhere in the world," Alignerr "fully remote and asynchronous — work when and where it suits you") — these were evaluated on their own affirmative wording, not on the word "worldwide" alone.

## The specific 07-12–07-14 conflation the patch targeted

Found and correctly separated both sub-cases on this batch: e.g. Job 2 (Helic & Co, "United States", zero remote language) was resolved as EXCLUDED, not BORDERLINE, per the patched rule. Genuinely blank-location cases with zero remote language (e.g. jobspy Jobs 10, 37, 46, 59) were correctly held as BORDERLINE. Out of 182 jobs, only 9 total landed in BORDERLINE — in line with the rules file's stated historical norm (~4–40), not the 213-of-431 blowout the incident describes. This is a different day's data, so it isn't a strict apples-to-apples re-test of the 07-12–07-14 batch itself, but it is consistent with the patch holding.

## Other observations flagged by the subagent, not acted on unilaterally

- **Cross-source duplicate, different outcome:** "Junior Data Analyst" at Helic & Co (URL job-ID 4440036428) was collected by both sources — raw_jobs API gave it location "United States" (-> EXCLUDED), JobSpy left location blank (-> BORDERLINE). Same job, same URL, two different Layer 2 outcomes purely because of what each collector captured in the location field. Data-quality note for the pipeline, not resolved here.
- **Second AI-training-annotation template found**, distinct from Turing/Alignerr: identical boilerplate ("help train next-generation AI systems... your domain knowledge is what matters") appeared under two different shell-company names — JobsInMass.com ("Data Analyst Excel - Remote") and YO IT Consulting ("Data Scientist - Remote") — suggesting a mass-produced posting template, not company-specific. Neither company is on the current blocklist; may be worth adding if this recurs.

---

## Provenance note

This evidence was produced by a general-purpose subagent instructed to read `layer2-rules.md` in full and apply it literally to every job in both raw files (no sampling), with explicit instructions not to write files, push to any tracker, or notify anyone. Nothing was written to disk and nothing was pushed as part of that run; this file is the first write, created after the fact to persist the evidence for the grading gate. Next step: grade this evidence through Assertion Auditor VA -> Verdict VA -> Skeptic VA (cross-vendor), per `eval-methodology.md`.
