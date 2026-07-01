---
name: fiverr
description: >-
  Use for running and scaling a Fiverr selling business day to day, buyer
  communication, replying to messages/inquiries, handling scope creep, seller
  level progression (New → Level 1/2 → Top Rated), protecting response rate and
  order-completion metrics, spotting buyer red flags/scams, and AI-disclosure /
  legal questions. Trigger whenever the user mentions Fiverr buyers, orders,
  reviews, seller levels, "how do I reply to this Fiverr client", off-platform
  requests, or scaling their Fiverr operation. To build or optimize the gigs
  themselves (titles, tags, pricing, thumbnails, catalog), use the
  fiverr-gig-optimizer skill in this collection instead.
license: MIT
---

# Running a Fiverr business

This skill covers everything *after* a gig is live: turning inquiries into
orders, keeping buyers happy, climbing the seller levels, and scaling without
tripping Fiverr's rules. If the user still needs to *build or rework the gigs*
(titles, tags, pricing, thumbnails, the whole catalog), point them to the
**fiverr-gig-optimizer** skill in this collection; it generates all of that.
This one is about operating the business once gigs exist.

## What actually moves the needle

Fiverr rewards sellers who convert fast, deliver reliably, and keep buyers on
the platform. Three metrics gate everything and each is fully in the seller's
control; protect them above short-term convenience:

- **Response rate:** reply to new messages quickly; the badge buyers see and
  the algorithm both track it.
- **Order completion:** don't accept orders you can't finish; a cancellation
  hurts more than a polite decline ever would.
- **On-time delivery:** pad your delivery estimates so revisions don't push you
  past the clock.

Keep all three above ~90% and most other things take care of themselves.

## Handling inquiries

Sort incoming messages by intent and spend your fastest replies where they pay
off:

- **Ready to buy** (names a specific project, mentions budget) → reply within an
  hour; this is where speed converts.
- **Interested, needs info** → reply within a few hours with the one detail that
  unblocks them.
- **Repeat question** → keep a few saved answers, but vary the wording (see
  `scaling.md`; identical text at volume looks automated).
- **Suspicious** → check it against `red-flags.md` before engaging.

**Defending scope:** when a buyer asks for something beyond the order, don't
absorb it silently and don't refuse flatly. Name it as extra and offer a custom
offer: *"That's outside the original order. I can add it for $X as a custom
offer, want me to send it?"*

## Seller levels

Levels unlock visibility and buyer trust. The bars below are approximate, and
Fiverr changes them, so verify the current values:

| Level | Rough requirements | Notable unlock |
|-------|--------------------|----------------|
| New | none | Standard features |
| Level 1 | ~60 days active, ~10 orders, ~4.7 rating | Priority support |
| Level 2 | ~120 days, ~50 orders, ~4.7 rating | Eligible for Promoted Gigs |
| Top Rated | ~180 days, ~100 orders, ~4.7 rating | Faster clearance, VIP support |

## Just starting out

The first handful of orders are the hardest: no reviews means no trust. The
play is: price competitively to win the first orders, over-deliver, collect
reviews, then raise prices in steps. Full zero-to-first-$100 roadmap in
`getting-started.md`.

## Scaling up

Once you're juggling 20+ orders a month, the risk shifts from *finding work* to
*staying reliable and staying compliant*. That means a single view of every open
order, templated replies with real variation, human-realistic timing, and clean
hand-offs if you bring on help. Workflows and the automation-safety guardrails
are in `scaling.md`.

## Legal & AI disclosure

Fiverr permits AI tools across all categories; the obligations are to own the
rights to what you deliver, add genuine human value, and answer honestly if a
buyer asks whether you used AI. Never deny it. EU buyers carry higher
transparency expectations. Details and the Fiverr-vs-Upwork contrast are in
`legal.md`.
