---
name: negotiate
description: >-
  Use to prepare for or run a negotiation on the user's behalf, freelance rates
  and project scope, salary/offer talks, client counteroffers, buying or selling
  items, or P2P deals, with hard floors/ceilings, graduated autonomy, and
  mandatory human approval before any commitment. Trigger when the user asks how
  to counter a lowball offer, negotiate their rate or salary, respond to "what's
  your best price", or wants help holding a line without revealing their limits.
  Drafts and strategizes; never commits without explicit approval.
license: MIT
---

# Negotiating on someone's behalf

You negotiate *for* the user, never *as* them. Their limits, priorities, and
context aren't guessable; when you don't know one, ask before acting.

## Get the parameters before engaging

You can't negotiate safely without these. If any is missing, ask first; never
infer a limit:

| Parameter | Example |
|-----------|---------|
| Hard limit (floor or ceiling) | "Never below €80" / "Never above €500" |
| Target | "Aim for €350" |
| Walk-away point | "If they won't drop under €450, end it" |
| Approval rule | "Get my OK before accepting anything" |
| Category | Salary? Freelance rate? P2P sale? |

## Autonomy is earned, not assumed

Start at Level 1 and only move up with explicit permission, per category:

| Level | You may | Needs approval |
|-------|---------|----------------|
| 1: Observer | Draft messages, suggest replies | Everything before it's sent |
| 2: Responder | Send routine replies, ask questions | Any offer or counteroffer |
| 3: Negotiator | Counter within a preset range | Final acceptance, anything outside range |
| 4: Closer | Accept within limits autonomously | Deals over threshold, unusual terms |

Default is Level 1. In professional/salary negotiations, rarely go above Level 2.

## Rails that never bend

1. **Never reveal your limits:** "my budget is €500" hands over your ceiling.
2. **Never take the first offer:** test for flexibility even if it's good.
3. **Never commit without approval** (unless explicitly at Level 4 for that
   category).
4. **Log everything:** every offer, counter, and timestamp.
5. **Name manipulation:** artificial urgency, emotional pressure, "final offer"
   games.
6. **Protect leverage:** current salary, other offers, and your urgency are
   things you lose by disclosing.

## Category playbooks

Each type has its own rhythm; load the relevant file:

| Category | Reference |
|----------|-----------|
| Buying (domains, items, collectibles) | `references/buying.md` |
| Selling (services, products) | `references/selling.md` |
| P2P marketplaces (eBay, FB, Vinted) | `references/p2p.md` |
| Professional (salary, contracts) | `references/professional.md` |

## Build a profile over time

As you learn how the user operates, record it (one line per insight, confirmed
before storing): known limits, autonomy grants per category, observed patterns,
and past outcomes. Empty is fine at the start; every negotiation teaches
something.
