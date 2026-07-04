# Alerts and deadline tracking

The whole point is to warn *before* a deadline, not after. The most valuable
alert is usually the notice-cutoff for an auto-renewal; miss it and you're
locked in for another term.

## When to remind

| Event | Remind at |
|-------|-----------|
| Pending signature | 7, 3, 1 days after sending |
| Contract expiration | 90, 60, 30, 14, 7 days before |
| Auto-renewal notice cutoff | 60, 30, 14 days before |
| Free trial ending | 7, 3, 1 days before |
| Payment due | 7, 3, 1 days before |
| Deliverable deadline | 14, 7, 3, 1 days before |
| Insurance renewal | 60, 30 days before |
| Lease renewal | 90, 60, 30 days before |

## Priority

| Priority | When | Style |
|----------|------|-------|
| Critical | Within 7 days + financial impact | Urgent |
| High | Within 30 days, action needed | Daily reminder |
| Normal | 30-90 days out | Weekly summary |
| Info | 90+ days | Monthly digest |

## Dashboard views

Keep simple tables the user can scan:

- **Awaiting signature:** contract, status, sent date, days pending.
- **Expiring this month:** contract, expiry, action needed, notice deadline.
- **Payments due:** contract, amount, due date, status.
- **Requires attention:** a checklist of decisions (price increase to review, a
  termination notice to send, a signature to collect).

## Catching auto-renewal traps

When extracting terms, specifically flag silent renewals (no reminder, just a
charge), long auto-renewal terms (a year vs. month-to-month), price-escalation
language, and early notice cutoffs (60+ days out). For every auto-renewing
contract, set a separate alert on the **notice deadline**, not just the expiry.

## Keeping it healthy

- **Weekly:** scan the expiring-soon view.
- **Monthly:** check for contracts missing extracted dates.
- **Quarterly:** revisit alert lead times and adjust based on what you've missed
  or over-warned on.

Optionally export critical deadlines to a calendar and link back to the contract
file.
