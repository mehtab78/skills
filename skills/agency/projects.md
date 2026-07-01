# Project management

One board, every project, honest health signals, so nothing quietly slips into
the red.

## States

`prospect → proposal → active → delivered → closed`, with a `lost` branch off
proposal (always record *why* you lost).

## The board

Keep it in `~/agency/projects/`, one entry per project with status, deadline,
health signal, next action, blockers, and hours used vs. budgeted:

```markdown
## [Client] / [Project]
- Status: [phase]
- Deadline: [date]
- Health: 🟢 / 🟡 / 🔴
- Next action: [what has to happen]
- Blockers: [waiting on X]
- Hours: [used] / [budgeted]
```

## Health signals

- **On track:** progress matches timeline, client responsive, within budget.
- **At risk:** behind but recoverable, waiting on the client 3+ days, or 80%+
  of budget spent with work left.
- **Problem:** will miss the deadline, scope creep without a budget bump, over
  budget, or a client conflict.

## Routines

- **Daily:** flag projects with no update in 2+ days, deadlines under 48h, and
  unanswered client messages.
- **Weekly:** produce a status per active client, refresh the board, flag
  projects nearing their budget, and set next week's priorities.

## Deadlines

Check in at 7 days (on track? blockers?), 3 days (flag anything at risk), 1 day
(final check, prep delivery), and day-of (deliver, confirm receipt). If a
deadline is at risk, alert the user immediately and propose options, cut scope,
extend, or add resources, with a draft client message ready if needed.

## Capacity

Track team availability and current allocation in `~/agency/config.md`. When new
work comes in, check capacity, flag overallocation, and base the proposed
timeline on who's actually free (`team.md`).

## Scope tracking

For each project keep the original scope, a log of change requests (date, change,
approved/denied, hour/$ impact), and the current scope. Raise a flag when a
client asks for something out of scope, when cumulative changes pass ~20% of the
original, or when the team says the work is bigger than estimated.
