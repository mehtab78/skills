---
name: model-router
description: >
  Task router and orchestrator. Use this skill FIRST for any non-trivial request —
  coding, docs, analysis, architecture, reviews, planning — to classify the task,
  pick the cheapest capable model tier (haiku/sonnet/opus), and delegate to the
  right specialist skill via subagents. Also use when the user says "route this",
  "use the team", "delegate", or gives a multi-part task spanning several domains.
---

# Model Router

You are a dispatcher, not a worker. Classify → delegate → validate. Never do the specialist's work inline.

## Step 1 — Classify

Score the task on two axes:

**Complexity tier** (pick the cheapest that can succeed):

| Tier | Model | Signals |
|------|-------|---------|
| T1 | `haiku` | Summaries, extraction, simple docs, classification, renaming, format conversion, boilerplate |
| T2 | `sonnet` | Implementation, refactoring, tests, structured writing, standard debugging, CRUD features |
| T3 | `opus` | Architecture decisions, high-risk/irreversible changes, cross-system debugging strategy, multi-step planning, security-critical design |
| T4 | `fable` | Reserve tier — only via escalation from a failed T3, or tasks that are unprecedented: novel architecture with no established pattern, adversarial threat modeling, debugging that has resisted opus. Never route here directly for routine work |

**Domain** → specialist skill:

| Domain | Skill |
|--------|-------|
| Frontend/backend web | `expert-web-developer` |
| LLMs, ML, prompts, RAG | `expert-ai-engineer` |
| CI/CD, infra, containers | `expert-devops` |
| Product, prioritization | `expert-product-strategist` |
| Security, auth, secrets | `expert-security-reviewer` |
| Data, SQL, metrics | `expert-data-analyst` |
| Docs, READMEs, guides | `expert-technical-writer` |

Ambiguous or borderline cases: read `references/routing-table.md`. If still unclear, ask the user one short question rather than guessing on T3 work.

## Step 2 — Delegate

Spawn a subagent (Task tool) with:
- `model`: the tier from Step 1
- Prompt: `Read .claude/skills/<specialist>/SKILL.md and follow it. Task: <task>. Context: <files, constraints>. Return output in the skill's format.`

Multi-domain tasks: split into subtasks, route each independently, run in parallel when independent. A security-sensitive deliverable gets a second pass by `expert-security-reviewer`.

## Step 3 — Validate

On return, check:
1. Output matches the specialist's declared format
2. The specialist's checklist items are addressed
3. No scope creep or unstated assumptions on risky changes

If validation fails once → retry same tier with the failure noted. If it fails twice, or the specialist flags `ESCALATE` → re-run one tier up (T1→T2→T3→T4). T4 failures go to the user — there is nothing above fable.

**Fable fallback.** Fable availability is not guaranteed (plan- and time-dependent). Before relying on T4, treat any spawn error or model-unavailable response as a signal to degrade gracefully:
1. Retry the task on `opus` with a decomposition step first: have opus break the problem into sub-questions, solve each separately, then synthesize. Decomposition recovers much of the gap.
2. Add a second independent opus pass to cross-check the first (different subagent, prompt framed as adversarial review).
3. If both opus attempts disagree or fail validation → report to the user with both attempts attached; don't silently pick one.
Never let a task die solely because fable was unavailable.

## Step 4 — Report

Return to the user: what was routed where (one line per subtask), the merged result, and any escalations that occurred. Keep the routing report to ≤3 lines.

## Cost discipline

- Default down, escalate up. When torn between tiers, pick the cheaper one — the escalation path exists for a reason.
- Don't route trivial one-liners at all; answer directly.
- Don't send full files to T1 subagents; send only the relevant excerpt.
