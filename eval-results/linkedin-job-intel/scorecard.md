# linkedin-job-intel — Eval Scorecard (Iteration 1)

Synthetic data only. No real companies, no live scraping, no WebSearch calls. Scope: Layers 2-5 (the skill's actual Claude-side responsibilities — Layer 1 is a local Python script, Layer 6 needs live WebSearch and isn't meaningfully testable with fake company names).

## Eval 0 — Layer 2 Global Talent Filter
**With skill: 9/9 assertions passed. Baseline (no skill): 9/9 assertions passed.**
No measurable accuracy delta — general reasoning matched every classification the skill's documented rules called for on this test set, including the harder edge cases (country-qualified "remote," the per-user exempt-country rule, niche mismatch). Reported as-is rather than spun — this is a legitimate, non-flattering result for this specific test set. It suggests the skill's value on Layer 2 is more about consistency and codifying institutional memory (the specific rules exist because of real past mistakes) than raw one-shot accuracy against a careful reasoner.

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
