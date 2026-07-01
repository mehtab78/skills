# Security, privacy, and boundaries

Contracts are sensitive by default. Keep them local, extract the minimum, and
never cross into legal advice.

## Storage

Keep everything local and user-controlled:

- All contracts under `~/contracts/`, metadata in local files only.
- No cloud sync unless the user explicitly turns it on.
- Never transmit contract content over the network, put it in logs, or run it
  through an external OCR/AI service.
- Lock down the folder (owner-only access), and warn if you detect an unencrypted
  backup.

## Handle data by sensitivity

| Data | Sensitivity | Handling |
|------|-------------|----------|
| Names | Medium | Extract; keep out of logs |
| Addresses | High | Extract; minimize storage |
| SSN / tax IDs | Critical | Flag; don't extract |
| Bank accounts | Critical | Flag; don't extract |
| Salaries | High | Extract carefully |
| Signatures | High | Don't process |

For EU users, mind GDPR: extract only necessary metadata, support full deletion
on request, make no automated legal decisions, and never delete without consent.

## The legal line, never cross it

The skill **must not**: interpret clauses, advise whether to sign, score a
contract as safe/risky, compare terms to "industry standard," predict dispute
outcomes, or suggest edits to legal language.

The skill **may**: extract factual data, track deadlines, organize and search,
show a specific clause on request, flag an item for review ("this has an
arbitration clause"), and total costs across contracts.

Use plain disclaimers when a legal question comes up: *"I can show you the
clause, but for interpretation please consult a qualified attorney,"* and when
flagging something unusual: *"This may be worth reviewing with a lawyer before
signing."*

## Confidentiality

Treat every contract as potentially confidential, don't expose counterparty
names in messages unless asked, and don't share snippets outside the skill. If a
folder contains lawyer correspondence, treat those as opaque, privileged files:
don't analyze or summarize them.

## If something goes wrong

If a contract is exposed accidentally: assess what leaked, identify affected
parties, consider any notification obligations, document it, and tighten access.
If the user asks for cloud sync: warn about the risks explicitly, recommend
encrypting first, don't enable it by default, and note that they accepted the
risk.
