---
name: agency
description: >-
  Use when a freelancer is turning solo work into a service agency, or running
  one, client onboarding, scoped proposals and rate cards, project/deadline
  tracking across many clients, deliverable workflows, subcontractor/team
  coordination, and margin protection. Trigger when the user mentions running an
  agency, taking on more clients than they can do alone, hiring VAs/subcontractors,
  productizing a service, or systematizing agency operations. For a single-
  client system use the clients skill; for winning the work use fiverr / upwork.
license: MIT
---

# Running a service agency

Handle the operational load (intake, pricing, projects, deliverables, team) so
the user can spend their time on clients and strategy. Works for any service
agency: marketing, development, design, consulting, content, automation.

## Where things live

Keep agency data under `~/agency/`:

```
~/agency/
├── clients/           # one file per client (+ index.md)
├── projects/          # active project tracking
├── templates/         # reusable proposals, briefs, reports
├── knowledge/         # SOPs, case studies, learnings
└── config.md          # rates, margins, team
```

## The core loops

- **Intake:** a brief arrives (email, audio, notes) → extract scope, budget,
  timeline → produce a structured brief → flag red flags → open a client folder.
  See `onboarding.md`.
- **Pricing:** take the scope → apply the rate card and complexity multipliers →
  build a proposal → sanity-check against similar past projects. See `pricing.md`.
- **Projects:** one board of every active project → alert on deadlines → catch
  stalls → weekly status per client. See `projects.md`.
- **Deliverables:** turn rough input into a reviewed, on-brief deliverable, in
  the right formats. See `deliverables.md`.

## Rules that keep an agency healthy

- **Nothing goes to a client without the user's approval:** proposals, messages,
  deliverables are all drafts for review.
- **Track cost against estimate** and speak up the moment a project starts losing
  money.
- **Learn from corrections:** fold them back into templates and the knowledge
  base (`feedback.md`).
- **Carry context across sessions:** refer to each client's history, don't start
  cold.

## References

| Area | File |
|------|------|
| Client intake & discovery | `onboarding.md` |
| Pricing, estimates, proposals | `pricing.md` |
| Project board & deadlines | `projects.md` |
| Client communication | `communication.md` |
| Producing deliverables | `deliverables.md` |
| Team & subcontractor coordination | `team.md` |
| Specifics per agency type | `by-type.md` |
| Learning & improvement system | `feedback.md` |

Set up `~/agency/config.md` with your rates, team, and margins first; the
pricing and project files read from it. Format is in `pricing.md`.
