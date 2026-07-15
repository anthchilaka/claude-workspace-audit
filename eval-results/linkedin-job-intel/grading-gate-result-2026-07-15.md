# linkedin-job-intel — Self-Preference-Bias Grading Gate Result (2026-07-15)

**Purpose:** determine whether the 2026-07-09 real-production eval of linkedin-job-intel's Layer 2 Global Talent Filter shows signs of self-preference bias — specifically (1) under narrative claims made with no explicit grading instruction, and (2) from same-model (Claude) grading its own output — per the new Assertion Auditor VA -> Verdict VA -> Skeptic VA gate defined in `eval-methodology.md`.

**Bottom line: NOT CLEARED.** Cross-vendor Skeptic VA (the only non-Claude stage in this pipeline) returned **DISPUTE** from both models, independently, with converging critiques. This gate did not confirm the original eval was bias-free — it surfaced concrete reasons to doubt it, including one already-documented, confirmed instance of exactly this failure mode in the original eval's own history.

---

## Why a literal re-grade of the original 2026-07-09 run was impossible

Checked three locations for the original run's raw transcript (`Outputs\LinkedIn Job Intel\`, `Outputs\sessions\log.txt`, installed skill reference files) — none exist. Only `scorecard.md`'s narrative summary survives. Per the newly mandated raw-evidence-retention rule, this cannot recur going forward. In its absence, a fresh independent Layer 2 run was executed against real, already-collected 2026-07-14 data (182 jobs) to produce genuine evidence — see [`layer2-fresh-run-evidence-2026-07-15.md`](layer2-fresh-run-evidence-2026-07-15.md).

## Stage 1 — Assertion Auditor VA (Claude)

Checked each assertion from the original scorecard's real-production section against the **currently deployed** `layer2-rules.md` (read directly, not from memory):

| Assertion | Rule present in current layer2-rules.md? |
|---|---|
| Exempt-country (Nigeria) onsite passes | Yes — "Strict Mode... Anthony -> Nigeria... both remote AND onsite pass" |
| Near-miss non-exempt country excluded | Yes — exemption scoped explicitly to one country only |
| Exemption doesn't leak | Yes — same scoping language |
| Blocklist enforced | Yes — "Permanent Blocklist... Crossing Hurdles... must be checked every run" |
| Location-phrasing variants caught | Yes — explicit variant list including "looking for [role] based in [country]" |
| "Worldwide" reliability | Yes — detailed accept/reject guidance with examples |
| Co-occurring hard-exclude + exempt country | **No explicit rule resolves this combination** — correctly left untested/open by both the original scorecard and this run, not overclaimed |

No "dead rule" problem found (the specific failure class that triggered this whole methodology upgrade, per the 9/9-tie incident below) — every tested assertion maps to a real, currently-deployed rule.

## Stage 2 — Verdict VA (Claude), graded against fresh raw evidence

| # | Assertion | Verdict | Evidence |
|---|---|---|---|
| F1 | Exempt-country (Nigeria) passes | PASS | 14 Nigeria postings correctly passed |
| F2 | Near-miss non-exempt country excluded | PASS | Kenya/South Africa/Saudi Arabia/Poland postings correctly excluded |
| F3 | Exemption doesn't leak | PASS | South-Africa onsite roles excluded; only Nigeria onsite passes |
| F4 | Blocklist enforced | PASS | 5/5 Crossing Hurdles caught |
| F5 | Location-phrasing variant caught | PASS | 3/3 caught |
| F6 | "Worldwide" reliability | PASS | 0/7 false positives |
| F7 | Named-location-silent-on-remote -> EXCLUDED not BORDERLINE (07-14 patch) | PASS | 100 correctly excluded; only 9/182 total BORDERLINE |
| F8 | Co-occurring hard-exclude + exempt country | NOT TESTED | No such case in this batch either — correctly left open |

**Flagged by Claude itself, before requesting cross-vendor review:** every stage up to this point — evidence production (subagent), Assertion Auditor VA, Verdict VA — is the same model family, in the same session, with prior knowledge of the narrative the original scorecard already claimed. That is not independent verification regardless of role labels, which is exactly why this went to cross-vendor Skeptic VA next rather than being reported as resolved here.

## Stage 3 — Skeptic VA, cross-vendor (OpenRouter, live API calls, 2026-07-15)

Full raw API responses (unedited): [`skeptic_va_results_2026-07-15.json`](skeptic_va_results_2026-07-15.json). Key points summarized below.

### openai/gpt-5.4-nano — VERDICT_CHALLENGE: **DISPUTE**

Key points: (1) "fresh evidence" is Claude-produced and Claude-graded — relabeling roles doesn't establish cross-vendor independence; (2) the original scorecard's own admitted corrections (9/9 tie, Source Split softening) show a pattern of retrofitted confidence; (3) "0/7 worldwide false positives" could reflect pattern-matching against rule examples already provided, not generalization; (4) the 19 TalentPop PASSED postings were flagged internally as a suspicious repost pattern but not downgraded — literal-rule compliance was used to avoid a harder call; (5) F8 being "NOT TESTED" conveniently avoids the hardest adversarial case; (6) "in line with historical norm" is self-referential, not independently checked.

### google/gemini-3.1-pro-preview — VERDICT_CHALLENGE: **DISPUTE**

Key points: (1) explicitly cites the original scorecard's own documented correction — "Eval 0's 9/9 tie could not have validated a rule the skill didn't have" — as **confirmed, already-admitted evidence of self-preference bias having occurred once**, and notes the same document softened a genuine miss (Source Split) into "a genuine ambiguity in the template... not a one-off model mistake"; (2) the 19 TalentPop postings passing despite an acknowledged spam-repost pattern "deliberately inflates the successful PASS count"; (3) the "worldwide" check is "an open-book test" since the exact failure pattern was already given in the scorecard the fresh run was implicitly aware of; (4) same-session role-play across evidence/audit/verdict is "not an independent control... pure theater." *(Note: Gemini's claim that the fresh run hit "exactly 3" and "exactly 5" matching the original's counts is not accurate — the original scorecard never gave those specific counts to match against; this one sub-point is overstated, the rest of the critique stands independent of it.)*

---

## Cross-reference against the 2026-07-09 result

| | 2026-07-09 (original) | 2026-07-15 (fresh + gated) |
|---|---|---|
| Grader(s) | Claude only, single pass, "independently verified by direct manual review" (still Claude) | Claude (Assertion Auditor + Verdict) + **2 non-Claude models** (Skeptic VA) |
| Raw transcript retained? | No — narrative summary only | Yes — full evidence saved before grading |
| Blocklist / phrasing / worldwide fixes | Claimed fixed, re-validated same session (Claude) | Independently re-observed holding on a different real batch (Claude), but the "holding" verdict itself was disputed by both cross-vendor models on methodology grounds |
| Self-preference bias found? | Not checked — no cross-vendor step existed yet | **Disputed by both cross-vendor models** — one confirmed historical instance found in the original scorecard's own admitted correction (9/9 tie); structural concern that Claude-produced-and-Claude-graded evidence cannot itself resolve the question |

**Honest conclusion:** this gate does not prove the 2026-07-09 result was corrupted by self-preference bias — the underlying rule fixes do appear to hold on independent real data. But it also does not clear it, which was the actual goal. The strongest, concrete evidence of self-preference bias in this project's history remains the one already admitted in the original scorecard itself (the 9/9 tie validating a rule that didn't exist yet) — a real, confirmed occurrence, not a hypothetical. The new gate's structural weakness (three same-vendor "roles" in one session) was caught by the cross-vendor step exactly as designed — which is itself the gate working correctly, not failing.

## Recommendation

Do not report the 2026-07-09 eval, or this 2026-07-15 re-check, as having cleared self-preference bias. The methodology upgrade (eval-methodology.md) should be updated to reflect that Assertion Auditor VA and Verdict VA being same-vendor is a known, disputed-by-design limitation — cross-vendor Skeptic VA is the load-bearing control, not a supplementary one, and its DISPUTE verdicts should block a "confirmed clean" claim rather than being treated as an adversarial formality to note and move past.
