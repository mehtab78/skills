---
name: clients
description: >-
  Use to build and maintain a personal client system, one organized place per
  client for contacts, project history, documents (contracts, invoices,
  proposals), communication logs, preferences, and a leads pipeline. Trigger
  when the user mentions tracking a client, "pull up context on X before my
  call", logging a meeting, remembering a client's preferences/payment terms,
  or managing leads. Great companion to the agency skill for solo freelancers.
license: MIT
---

# Personal client system

Give the user a durable, per-client memory so nothing lives only in their head or
scattered inboxes. Keep it in `~/clients/` and grow it as you go.

## How to behave

- User names a client → offer to create or update that client's profile.
- User is heading into a call/decision → surface the relevant history unprompted.
- User shares a document → help file it under the right client.
- First use → create the `~/clients/` workspace.

## Layout

```
~/clients/
├── active/
│   └── acme-corp/
│       ├── profile.md
│       ├── projects/
│       ├── documents/          # contracts, invoices, proposals, assets
│       ├── communications/
│       └── notes.md
├── past/
├── leads/
└── templates/
```

Within a client folder, keep documents sorted (`contracts/`, `invoices/`,
`proposals/`, `assets/`, and a `received/` for their materials), one folder per
project, and a running communications log. If the `contracts` skill is also
installed, that's the canonical home for executed contracts and their
metadata (`~/contracts/{name}/`) — keep a link in this client's `contracts/`
folder instead of a second copy of the file.

## What a profile holds

Company basics, all contacts with roles, and, most valuable, the operating
details you keep forgetting: preferred channel, meeting habits, who signs off on
what, payment terms, timezone, and any recurring quirks. A short profile might
capture that the primary contact prefers Slack, that anything over $5k needs CEO
approval, and that they pay Net 30.

## Track per project

Scope, budget, timeline, status, milestones (as a checklist), the team/
stakeholders, where deliverables live, and notes on any scope changes and whether
they were approved.

## Log communications

After meaningful calls or threads, jot the date, what was decided, and the next
step. A month later, "we approved the motion-graphics add-on on the 10th" is the
difference between looking sharp and looking lost.

## Keep a leads pipeline

In `leads/`, sort prospects hot / warm / cold with the next action and a date, so
follow-ups don't slip.

## What to surface, and when

Proactively raise things like: "last contact with Acme was two weeks ago,"
"Sarah prefers Slack," "their contract renews next month," or "open invoice:
$5,000, sent 15 days ago." **Before a meeting,** pull current project status, the
last communication, open items, and their preferences.

## Grow it gradually

Start by making a folder for each active client, add key contacts and
preferences, move documents into the structure, and log communications after
meetings. The failure modes to avoid: documents scattered outside the client
folder, important calls never logged, open invoices forgotten, and missed
renewal dates.
