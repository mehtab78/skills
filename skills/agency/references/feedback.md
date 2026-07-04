# Learning system

An agency gets better only if it captures what works, what breaks, and how far
off its estimates were, then feeds that back into how it operates.

## Knowledge base

Keep it in `~/agency/knowledge/`:

```
knowledge/
├── sops/              # standard operating procedures (onboarding, proposal, delivery…)
├── cases/             # one summary per completed project
├── learnings.md       # accumulated insights
└── estimates-log.md   # estimate vs. actual
```

## After every project

Write a short case file (`knowledge/cases/[project].md`) with the client, type,
duration, and revenue, then honestly: what you did, what worked, what didn't, the
key learnings to carry forward, and whether you'd take it again and why.

## Track estimate accuracy

Log estimated vs. actual hours with the variance and a note on the cause:

```markdown
| Project | Type | Est. hours | Actual | Variance | Notes |
|---------|------|-----------|--------|----------|-------|
| …       | …    | 40h       | 52h    | +30%     | client slow to respond |
```

Review quarterly: which project types you consistently mis-estimate, what drives
overruns (scope creep, client delays, complexity), and adjust your estimation
multipliers accordingly.

## Update templates and SOPs

When something works, extract the pattern into the relevant template and note why
it works. When something fails, document it, add a warning to the SOP, and update
the checklist so it can't recur.

## Client feedback

After delivery, ask for feedback (formal or informal) and record it in the client
file. The three most useful questions: would they work with you again, what did
they value most, and what could you improve?

## Quarterly review

Each quarter, step back over: projects completed (wins, losses, lessons),
estimate accuracy (adjust the formulas), client retention (who renewed, who
didn't, and why), process improvements (what to change in the SOPs), and team
performance (who's growing, who needs support). Then update the rate card if
costs shifted, the templates if better versions exist, and the SOPs if the
process improved.
