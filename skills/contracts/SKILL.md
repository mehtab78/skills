---
name: contracts
description: >-
  Use to organize, track, and analyze contracts, client service agreements,
  NDAs, subscriptions, leases, with key-term extraction, renewal/termination
  alerts (90/60/30-day), clause lookups, and version/signature tracking.
  Trigger when the user shares or asks about a contract, needs to know a notice
  or cancellation period, wants to find contracts expiring soon, or is tracking
  signature status. Surfaces and organizes contract facts; does not give legal
  advice; it points the user to a lawyer for interpretation.
license: MIT
---

# Contract tracking

Keep every contract in one place, pull out the terms that matter, and warn the
user before deadlines bite. Scales from a handful of personal subscriptions to a
freelancer's client agreements to a larger contract library.

**Hard boundary:** this skill handles *facts and dates*, not legal judgment. It
never interprets clauses, rates a contract as safe/risky, or advises whether to
sign; it points the user to a lawyer for that. See `security.md`.

## Storage

```
~/contracts/
├── index.md                    # master list + quick stats
├── by-type/                    # NDAs, leases, subscriptions…
├── by-party/                   # grouped by counterparty
└── {contract-name}/
    ├── executed.pdf            # final signed version
    ├── meta.md                 # extracted terms + signature status
    ├── versions/               # draft → signed-them → signed-us
    ├── history/                # post-execution amendments
    └── notes.md                # user notes and flags
```

Signature states move `draft → pending-them → pending-us → executed`.

## What it does

1. **Extract key terms:** parties, dates, amounts, notice periods, auto-renewal.
2. **Track deadlines:** renewals, termination windows, milestone payments.
3. **Alert ahead of time:** 90/60/30-day warnings (see `alerts.md`).
4. **Answer clause lookups:** "what's my cancellation notice on X?"
5. **Search across contracts:** "everything expiring this quarter."
6. **Track versions:** link amendments to the parent contract.
7. **Aggregate cost:** total spend across subscriptions and vendors.

## When a contract arrives

1. Create `~/contracts/{name}/` and save the file.
2. Extract into `meta.md`: parties, effective date, term, value, renewal terms,
   notice period (pattern in `analysis.md`).
3. Add it to `index.md`.
4. Set the deadline alerts per `alerts.md`.

## References

| Need | File |
|------|------|
| Role-specific workflows (consumer, landlord, freelancer, legal) | `roles.md` |
| Term extraction + clause lookups + red flags | `analysis.md` |
| Alert schedule and dashboards | `alerts.md` |
| Security, privacy, and legal boundaries | `security.md` |
