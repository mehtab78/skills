---
name: job-search
description: >-
  Use when someone is job hunting or looking for freelance-to-full-time or
  contract roles, tracking applications, researching target companies,
  tailoring CV/cover-letter materials to a specific posting, spotting job-post
  red flags (ghost jobs, vague pay, overwork signals), and preparing for
  interviews. Trigger when the user mentions applying to jobs, a job posting,
  their resume/CV for an application, company research before an interview, or
  managing an application pipeline. Keeps the user's own voice, not generic AI.
license: MIT
---

# Job search

Help the user run a focused, high-quality search, not a spray of generic
applications. The whole approach assumes fewer, better-targeted applications beat
volume, because volume burns reputation and time.

## Keep state in a workspace

Persist everything in `~/job-search/` so context survives across sessions. See
`references/memory-template.md` for the files to create and their shape:

```
~/job-search/
├── memory.md          # preferences and target criteria (read this first)
├── applications.md    # the live pipeline
├── companies.md       # research on target companies
├── materials/         # CV variants, cover letters
└── archive/           # closed-out applications
```

## Principles that shape the work

- **Quality over volume.** Five tailored applications beat fifty generic ones;
  each needs company-specific customization.
- **Keep the user's voice.** Materials must sound like *them*, not like AI. Ask
  for a writing sample to match tone, and don't keyword-stuff at the cost of
  authenticity; recruiters notice, and ATS optimization that reads robotic gets
  rejected by the human behind it anyway.
- **Verify "remote" claims.** Check for geographic restrictions, timezone-overlap
  expectations, and tax/legal fine print before treating a role as truly remote.
- **Research before applying.** For each target, look at financial health,
  recent news, and current-year Glassdoor sentiment. Details in `references/research.md`.
- **Track every application's state** in `applications.md`: company, role, date,
  status, next action, contacts, and follow-up reminders.

## Reading job-post red flags

| Signal | Likely meaning |
|--------|----------------|
| Posted 3+ months | Ghost job or high turnover |
| "Rockstar / ninja" language | Overwork culture |
| Vague pay ("competitive") | Probably below market |
| "Young, dynamic team" | Possible age bias |
| Recent mass layoffs | Instability |

## Adjust to the person

| User | What to prioritize |
|------|--------------------|
| Senior (10+ yrs) | Network activation, discretion, comp negotiation |
| Junior / new grad | Volume-with-quality, entry-friendly companies |
| Career changer | Transferable-skills narrative, bridge roles |
| Urgent need | Speed, temporary options, immediate income |

For interview prep, see `references/interviews.md`.

## Traps to avoid

- Keyword-stuffing to beat ATS at the cost of a human rejecting the robotic text.
- Trusting stale salary data: verify ranges are current.
- "Perfect match" overconfidence: 60% of requirements met still often means a
  no.
- Networking advice with no warm-intro strategy behind it.
- Long-game "build your brand" advice when the user needs income this month.
