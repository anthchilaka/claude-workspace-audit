# Eval Methodology — the Assertion-First Grading Gate

## Why this exists

An Anthropic Applied AI engineer's public talk, *"Picking the right model"* (Claude YouTube channel, May 2026), describes a benchmark that looked near-perfect until the raw execution logs were read directly — the model wasn't solving the coding tasks, it was pulling answers out of its own prior-run git history. The headline score gave zero signal that this was happening; only reading the transcript caught it. The talk's core lesson: a metric can be gamed cleanly while looking clean. Read the underlying evidence, every time, not just the score.

This repo had already hit a version of the same failure class before that talk was reviewed here: an earlier eval iteration reported a 9/9 tie validating a rule that, on direct file check, wasn't in the deployed skill yet. The assertion wasn't testing what it claimed to test — the "pass" was measuring nothing. That correction is recorded in `eval-results/linkedin-job-intel/scorecard.md`. This methodology file exists so that failure mode is structurally harder to repeat, not just something a manual audit happens to catch after the fact.

## The gate

Grading for every eval in this repo runs through three roles, in a fixed order — later roles cannot run until earlier ones clear:

1. **Assertion Auditor VA** — checks whether the assertion itself is validly designed *before* anything is scored. Confirms the rule, behavior, or output being tested actually exists in the current version of the skill under test. An assertion that fails this check is rejected and rewritten — it never reaches a verdict.
2. **Verdict VA** — grades each surviving assertion strictly against the actual output evidence (the raw transcript / tool-call log, not a self-reported summary).
3. **Skeptic VA** — adversarial reviewer whose only job is arguing why a "pass" from Verdict VA might actually be wrong. Never confirms, only tries to break it. As of 2026-07-14, this role runs cross-vendor (see below), not just as another Claude instance.

Previously, Assertion Auditor ran as a cleanup pass after Verdict VA had already scored — which is how the dead-rule assertion above slipped through undetected until a manual audit found it. The gate now makes validation a precondition for scoring, not a follow-up check.

## Mapping the three roles to the talk's failure modes

| Role | Failure mode it targets | Mechanism |
|---|---|---|
| Assertion Auditor VA | A benchmark score that doesn't reflect what it claims to measure — the tested rule was never actually in the deployed skill | Validates each assertion against the current rule/skill file *before* any verdict is trusted; gates Verdict VA rather than reviewing it afterward |
| Verdict VA | Trusting a headline score instead of the evidence behind it | Grades strictly against the raw output/transcript evidence, not a self-reported summary |
| Skeptic VA (cross-vendor) | A model's own blind spots going undetected because the same model graded its own output | Argues every "pass" might be wrong; now run on two additional model families alongside Claude, so a same-family blind spot can't pass unchallenged |

## Cross-vendor Skeptic VA

Running Skeptic VA only as another Claude instance still shares Claude's training-induced blind spots, even under an adversarial persona — this is the pattern described in the LLM-as-judge literature as **self-preference bias**: a model favoring outputs or reasoning that resembles its own, even when explicitly instructed to look for flaws. Skeptic VA is the highest-leverage seat for cross-vendor diversity because its entire job is disagreement.

**Implementation:** OpenRouter (single API key, pay-as-you-go access across vendors), running Skeptic VA on:
- `openai/gpt-5.4-nano`
- `google/gemini-3.1-pro-preview`

Both models grade the same transcript independently. Disagreement between the two — or between either and the Claude-run Skeptic pass — is itself a signal worth logging, not noise to average away.

**Status (2026-07-14):** gate defined and documented; cross-vendor Skeptic VA implementation staged at `scripts/skeptic_va_openrouter.py`, pending OpenRouter API key activation. Not yet run against a live eval.

## Raw evidence retention

Every fresh eval run's raw evidence — the actual classified output, not a narrative summary — is saved to disk immediately after it's produced, before grading starts. This closes the exact gap that made a full self-preference-bias check on the 2026-07-09 `linkedin-job-intel` eval impossible: that run's raw transcript was never retained, only a post-hoc scorecard summary, so Assertion Auditor VA and Verdict VA would have had nothing but a narrative to grade against.

**Rule, going forward:** raw evidence from any fresh eval run is saved to `eval-results/<skill-name>/` before the Assertion Auditor VA -> Verdict VA -> Skeptic VA gate runs, named `<layer-or-scope>-fresh-run-evidence-YYYY-MM-DD.md`, not folded into or replacing the final scorecard.

**Current example:** [`eval-results/linkedin-job-intel/layer2-fresh-run-evidence-2026-07-15.md`](eval-results/linkedin-job-intel/layer2-fresh-run-evidence-2026-07-15.md) — Layer 2 Global Talent Filter, 182 real jobs, 2026-07-14 batch, saved 2026-07-15, not yet graded.

## Validation still needed before this is trusted

A deliberate adversarial test case — modeled on the git-history exploit described above, giving a skill under test a way to "cheat" via cached or prior-run output — is queued but not yet built. The gate should not be cited as closing this gap until that probe has been run and caught.
