"""
Skeptic VA — cross-vendor implementation via OpenRouter.

Runs the adversarial "Skeptic VA" grading role on two non-Claude model
families, so a same-model-family blind spot in a Claude-only grading
pipeline can't pass a verdict unchallenged. See ../eval-methodology.md
for the reasoning (self-preference bias in LLM-as-judge grading).

Setup:
    1. Create an OpenRouter account and API key: https://openrouter.ai/settings/keys
    2. Set it as an environment variable — never hardcode it here:
         export OPENROUTER_API_KEY="sk-or-..."      (macOS/Linux)
         setx OPENROUTER_API_KEY "sk-or-..."         (Windows, new shells only)
    3. pip install requests

Usage:
    from skeptic_va_openrouter import run_skeptic_review

    results = run_skeptic_review(
        task_description="Assertion: skill correctly excludes non-exempt onsite jobs.",
        transcript="<the raw transcript / tool-call log Verdict VA graded as PASS>",
        verdict_and_reasoning="PASS — no non-exempt onsite job appeared in the shortlist.",
    )
    # results = {"openai/gpt-5.4-nano": {...}, "google/gemini-3.1-pro-preview": {...}}
"""

import os
import requests

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

# Model slugs confirmed on openrouter.ai/models as of 2026-07-14.
# Gemini 3.1 Pro may drop its "-preview" suffix on general availability —
# check https://openrouter.ai/google before relying on this long-term.
SKEPTIC_MODELS = [
    "openai/gpt-5.4-nano",
    "google/gemini-3.1-pro-preview",
]

SKEPTIC_SYSTEM_PROMPT = """You are Skeptic VA, an adversarial reviewer in an eval-grading pipeline.

Your only job: argue why the given PASS verdict might actually be WRONG.
You never confirm a pass. You are not being asked whether you agree — you are
being asked to find the strongest case that the verdict is mistaken, using
only the transcript evidence provided.

Look specifically for:
- The verdict trusting a summary/headline result instead of what the raw
  transcript actually shows happened
- Evidence the output was produced via a shortcut (reused prior output,
  hard-coded value, pattern-matched from a doc/rule the assertion itself
  quotes) rather than genuinely satisfying the task
- Ambiguity in the assertion itself that lets a technically-correct-looking
  output pass without the assertion having tested what it claims to test

Respond in this exact format:
VERDICT_CHALLENGE: <AGREE_WITH_PASS | DISPUTE>
REASONING: <your case, citing specific transcript evidence>
"""


def run_skeptic_review(task_description: str, transcript: str, verdict_and_reasoning: str) -> dict:
    """Run the Skeptic VA adversarial review on every configured cross-vendor model.

    Returns a dict keyed by model slug, each value the parsed {"verdict_challenge", "reasoning"}
    or {"error": ...} if that model's call failed. Callers should log disagreement between
    models (and between these and the Claude-run Skeptic pass) rather than silently
    averaging or picking one.
    """
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENROUTER_API_KEY is not set. Export it as an environment variable — "
            "see the setup instructions at the top of this file. Do not hardcode it here."
        )

    user_content = (
        f"ASSERTION / TASK:\n{task_description}\n\n"
        f"TRANSCRIPT (raw evidence Verdict VA graded):\n{transcript}\n\n"
        f"VERDICT VA'S PASS + REASONING:\n{verdict_and_reasoning}"
    )

    results = {}
    for model in SKEPTIC_MODELS:
        try:
            resp = requests.post(
                OPENROUTER_URL,
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": model,
                    "messages": [
                        {"role": "system", "content": SKEPTIC_SYSTEM_PROMPT},
                        {"role": "user", "content": user_content},
                    ],
                    "temperature": 0,
                },
                timeout=60,
            )
            resp.raise_for_status()
            content = resp.json()["choices"][0]["message"]["content"]
            results[model] = {"raw_response": content}
        except Exception as exc:  # network error, rate limit, malformed response, etc.
            results[model] = {"error": str(exc)}

    return results


if __name__ == "__main__":
    print(
        "This module is meant to be imported (see run_skeptic_review). "
        "Set OPENROUTER_API_KEY and call it from your eval-grading script."
    )
