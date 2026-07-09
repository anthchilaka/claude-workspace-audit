# linkedin-job-intel — Eval Scorecard

## Update (2026-07-09) — real production validation, not synthetic

Everything below the next horizontal rule is Iteration 1 (synthetic fixtures only, corrected inline where needed). This section is a live production test: the skill's actual daily pipeline run against real collected job data for two active users of the skill, results independently verified by direct manual review of the real output, not agent self-report.

**Scope:** ran Layer 2 (Global Talent Filter) against a combined two-day real batch — 1,000 raw postings collected across both users before deduplication, 839 unique after ID-based dedup. No synthetic fixtures, no fabricated company data — this is the skill doing its actual job.

**What this closed vs. the prior synthetic eval:** the synthetic Eval 0 below could only test the per-user exempt-country rule in isolation, with no competing signals. Three adversarial gaps flagged then as untested were checked against real data this run:

| Adversarial scenario (flagged as untested in the prior synthetic eval) | Result on real data |
|---|---|
| A near-miss non-exempt country still correctly excluded (not over-passed on the exemption alone) | **Closed** — real postings in tracked near-miss countries appeared in both users' batches; none were wrongly auto-passed, ambiguous ones correctly fell to a flagged-for-review state rather than a silent pass |
| The exemption doesn't leak into general onsite-exclusion logic for other countries | **Closed** — non-exempt onsite roles at large, well-known multinational employers were correctly excluded; the exemption applied only to each user's single intended country |
| A competing hard-exclude clause co-occurring with an exempt-country location | **Still open** — no real posting in this batch happened to combine an exempt-country location with a competing restriction clause; inconclusive, not disproven |

**Three additional rule gaps found via manual review — not caught by the written rules or an independent verification script on the first automated pass:**
1. A company on the project's permanent fraud blocklist (added after a confirmed-fraud finding weeks prior) reappeared in both users' real batches. The blocklist had only ever been recorded in an internal log, never actually encoded into the skill's own rule file — nothing in the deployed skill would have caught it without a human cross-referencing that log by hand.
2. A location-restriction phrasing variant ("looking for [role] based in [country]," distinct from the literal "must be based in [country]" the old rule matched) let country-restricted postings through undetected. This exact gap had previously been logged internally as resolved via a script that, on verification, does not exist anywhere reachable — the earlier "resolved" status was not real.
3. A bare "worldwide" keyword, used as a positive signal for global hiring eligibility, was unreliable at volume: 11 of 12 matches across the real batch were generic company-marketing language ("operates in 120 countries worldwide") rather than job-specific hiring-scope language. Only 1 was a genuine global-hiring claim.

**Fix applied to the skill's rule file and re-validated against the same real batch before deployment:** the blocklisted company and the location-restricted postings correctly flipped to excluded; 9 of 11 "worldwide" false positives correctly flipped to excluded, the remaining 2 correctly moved to a flagged-for-review state rather than a false pass; the one genuine "worldwide" case and the original exempt-country passes were unaffected — no regression measured.

**Outcome:** 6 correctly-identified roles pushed to the two users across this batch (one primary user, one mentee account), confirmed received by both.

**Honest limitation:** this is one production batch on one day, not a repeated-trials measurement — it demonstrates the fix holds under real, messy data (which the synthetic eval couldn't), not a statistical reliability rate. The remaining open adversarial scenario (co-occurring hard-exclude + exempt country) needs either a longer observation window or a deliberately constructed test case.

---

# linkedin-job-intel — Eval Scorecard (Iteration 1)

**Correction (2026-07-09), superseding two claims below — read before citing this scorecard anywhere:**
1. Eval 0's claim that the per-user exempt-country rule was among the "harder edge cases" tested is inaccurate. A 2026-07-09 audit confirmed the skill's own `references/layer2-rules.md` did not contain any per-user exempt-country logic at the time this eval ran — that rule was documented in the project's `claude.md` change log (2026-07-03/07-04) but never actually made it into the skill file until 2026-07-09. Eval 0's 9/9 tie could not have validated a rule the skill didn't have; whatever test cases produced that tie were not exercising this rule, regardless of the framing used at the time.
2. Eval 2's known "Source Split" miss was fixed 2026-07-09 (template heading now states its own scope). A follow-up eval attempting to re-validate this specific fix found the re-test itself invalid (test prompt pre-labeled the answer, never exercising the original retrieval-under-load failure mode) — so this fix is applied on sound reasoning but **not yet empirically confirmed**, and should not be cited as resolved without caveat.
3. Aggregate "19/20 (95%)" below should not be cited going forward without this correction attached. A fresh synthetic eval targeting the per-user exempt-country rule specifically (run 2026-07-09, 3 trials) found exempt-country onsite jobs pass 100% with the fix vs. 0% without it on synthetic data — since superseded by the real production validation above, which is the stronger evidence.

Synthetic data only. No real companies, no live scraping, no WebSearch calls. Scope: Layers 2-5 (the skill's actual Claude-side responsibilities — Layer 1 is a local Python script, Layer 6 needs live WebSearch and isn't meaningfully testable with fake company names).

## Eval 0 — Layer 2 Global Talent Filter (see correction above — do not read this section as having validated the per-user exempt-country rule)
**With skill: 9/9 assertions passed. Baseline (no skill): 9/9 assertions passed.**
No measurable accuracy delta on the assertions this eval actually covered — general reasoning matched every classification the skill's documented rules called for on this test set, including country-qualified "remote" and niche mismatch. Reported as-is rather than spun. It suggests the skill's value on Layer 2 is more about consistency and codifying institutional memory (the specific rules exist because of real past mistakes) than raw one-shot accuracy against a careful reasoner.

## Eval 1 — Layer 3 Push File Format
**With skill: 4/4 assertions passed. Baseline (no skill): 1/4 assertions passed.**
The skill produced the exact required contract: flat JSON array, 6 fields (`job_number`, `title`, `company`, `status`, `url`, `match_reason`), no wrapper. The baseline, given the same task with no format spec, wrapped the output in a metadata object (`{"push_request": ..., "jobs": [...]}`) and used different field names (`job_id`, `source_type`). This is the exact failure class documented in the project's real troubleshooting log — a wrapped-object push file previously caused `AttributeError: 'str' object has no attribute 'get'` in production. Strongest, fully-verified result in this batch: reproducible, checkable, not narrative.

## Eval 2 — Layer 4/5 Intake + Tracker Updates
**With skill: 6/7 assertions passed. Baseline (no skill): 5/7 assertions passed.**
Skill correctly followed the required template structure and included the Layer 6 stub (baseline invented its own report format and omitted the stub entirely). Both correctly preserved existing tracker entries and continued sequential numbering. One real miss on the skill side: the required "Source Split" field should reflect the full raw batch (per the template's own reference notes: "tracked separately inside the raw file header"), but the with-skill run reported only the filtered-shortlist split (2/3) instead of the full-batch split (6 JOB/4 POST) — the baseline actually got this specific field right. This points to a genuine ambiguity in `layer4-template.md`'s inline placeholder text, not a one-off model mistake — worth tightening the template itself.

## Aggregate
| | With skill | Baseline |
|---|---|---|
| Eval 0 (Layer 2 filter) | 9/9 | 9/9 |
| Eval 1 (Layer 3 format) | 4/4 | 1/4 |
| Eval 2 (Layer 4/5 template) | 6/7 | 5/7 |
| **Total** | **19/20 (95%)** | **15/20 (75%)** |

## Action item this eval surfaced
`layer4-template.md`'s inline `## Source Split` placeholder doesn't make clear it should reflect the raw batch header, not the filtered shortlist — the clarifying instruction only lives in a separate footnote most implementations won't reliably reach. Recommend tightening the inline placeholder text directly.
