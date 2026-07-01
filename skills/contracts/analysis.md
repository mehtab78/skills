# Extracting and reading contracts

The job is to pull out facts and flag things worth a human's attention, never to
judge whether a clause is fair or advise on signing.

## What to capture in `meta.md`

For every new contract, extract:

```markdown
# Contract: {name}

## Parties
- Party A: {name, role}
- Party B: {name, role}

## Signature status
- Status: draft | pending-them | pending-us | executed
- Sent / signed-them / signed-us / fully-executed: YYYY-MM-DD

## Dates
- Effective: YYYY-MM-DD
- Term: {duration}   Expires: YYYY-MM-DD
- Auto-renews: yes/no; {renewal term}
- Notice period: {days} before expiration

## Value
- Amount: {total or recurring}
- Payment terms: {net 30, milestone, …}
- Late fees: {if any}

## Key clauses
- Termination: {how to exit, penalties}
- Renewal: {automatic/manual, rate changes}
- Liability: {caps, exclusions}
- IP: {who owns what}
- Confidentiality: {NDA terms if any}

## Notes
{observations, flags, context}
```

## Clauses people ask about most

- **Cancellation:** notice period, required method, early-exit fees.
- **Auto-renewal:** renewal length, any price adjustment, the opt-out window.
- **Liability:** cap amount, indemnification scope, insurance requirements.
- **Confidentiality:** duration (often outlives the contract), what's covered,
  permitted disclosures.

## Patterns worth flagging (for review, not judgment)

| Pattern | Example | What to do |
|---------|---------|------------|
| Unlimited liability | "indemnify for all claims" | Flag for review |
| Silent auto-renewal | renews with no reminder | Set an early alert |
| Unilateral changes | "terms may change at any time" | Record the current version |
| Asymmetric termination | they can exit anytime, you can't | Flag it |
| Broad non-compete | restricts unrelated work | Check the scope |
| Mandatory arbitration | no court option | Note the limitation |
| Unclear data retention | what happens to your data? | Flag to clarify |

Flagging means surfacing the clause and suggesting a lawyer look, not saying
whether it's good or bad.

## Queries to handle

Natural-language questions the skill should answer from `meta.md` data:

- "What's my notice period for [contract]?"
- "When does [contract] expire?"
- "Find all contracts expiring in [timeframe]."
- "Who owns the IP in my contract with [party]?"
- "What's my liability cap with [client]?"
- "Show every NDA I've signed."
- "List recurring payments across all contracts."
