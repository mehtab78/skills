# Routing Decision Table (detailed)

Loaded only for ambiguous cases. Format: task pattern → tier + specialist.

| Task pattern | Tier | Specialist | Why |
|---|---|---|---|
| Summarize a file / changelog | haiku | technical-writer | Extraction, no reasoning |
| Write API reference from code | haiku | technical-writer | Mechanical transformation |
| Classify/label a list of items | haiku | data-analyst | Simple classification |
| Rename, reformat, convert data | haiku | (none — router may answer) | Transformation |
| Implement a feature from clear spec | sonnet | web-developer / ai-engineer | Standard engineering |
| Write or fix unit tests | sonnet | web-developer | Standard engineering |
| Refactor a module, same behavior | sonnet | web-developer | Bounded change |
| Build a dashboard query / SQL | sonnet | data-analyst | Structured but routine |
| Write a runbook or onboarding guide | sonnet | technical-writer | Structured writing |
| Set up CI pipeline from template | sonnet | devops | Known patterns |
| Prompt tuning, eval harness | sonnet | ai-engineer | Standard AI work |
| Choose between architectures (Kafka vs SQS) | opus | devops or web-developer | Trade-off reasoning, ADR |
| Debug intermittent cross-service failure | opus | devops | Strategy before action |
| Design auth/permissions model | opus | security-reviewer | High-risk, irreversible |
| Multi-quarter roadmap or scope cut | opus | product-strategist | Deep prioritization |
| Migration plan (DB, framework, cloud) | opus | devops | Multi-step, risky |
| Threat model a new feature | opus | security-reviewer | Adversarial reasoning |

## T4 (fable) — reserve tier

Direct-route to fable only for: greenfield architecture with no industry-standard answer, threat models against sophisticated adversaries, post-incident analysis where opus-level attempts already failed, or the user explicitly asks. Everything else reaches T4 only through escalation.

Fallback when fable is unavailable (spawn error / model not offered): opus with forced decomposition (break into sub-questions → solve → synthesize), then an independent adversarial opus review. On disagreement, surface both to the user. Log in the routing report that T4 was requested but degraded, so the user knows the result came from the fallback path.

## Tie-breakers

- Reads code but changes nothing → one tier lower than the equivalent write task.
- Anything touching secrets, auth, payments, PII → minimum sonnet; design-level → opus; always add a security-reviewer pass.
- User says "quick" or "rough draft" → bias one tier down.
- User says "production", "careful", "this broke before" → bias one tier up.
- Output feeds directly into an irreversible action (deploy, delete, send) → opus validates even if a lower tier drafts.

## Multi-domain splits (examples)

- "Build a signup page and document it" → web-developer (sonnet) + technical-writer (haiku), parallel.
- "Add an LLM feature and make sure it's safe" → ai-engineer (sonnet) → security-reviewer (sonnet) sequential.
- "Why is prod slow and what should we do long-term?" → devops (opus) for strategy, then devops (sonnet) for fixes.
