# Freelance Skills — for Claude Code

A collection of independent [Claude Code](https://claude.com/claude-code) skills
for freelancers who sell on marketplaces like **Fiverr** and **Upwork**. Each
skill is self-contained and triggers on its own — install one, several, or all.

The collection spans the whole freelancing loop: **finding work** (`job-search`),
**choosing a platform and pricing** (`freelance`), **building and optimizing your
Fiverr gigs** (`fiverr-gig-optimizer`), **running and scaling a Fiverr sales
operation** (`fiverr`), **winning work on Upwork** (`upwork`), **negotiating
rates and deals** (`negotiate`), and **operating the back office** — clients,
contracts, and agency growth.

## Skills

### Sell & win work

| Skill | What it does | Type |
|-------|--------------|------|
| [`fiverr-gig-optimizer`](skills/fiverr-gig-optimizer/) | Generates a full Fiverr gig catalog from your services: combo-niche research, titles/tags/pricing, designed thumbnails, HTML catalog, and per-gig PDFs. | Generator (bundled scripts) |
| [`fiverr`](skills/fiverr/) | Runs the Fiverr business *after* gigs are live: buyer communication, scope-creep defense, seller-level progression, metrics, red flags, scaling. | Advisory |
| [`upwork`](skills/upwork/) | Wins Upwork work: personalized proposals, profile optimization, client messaging/negotiation, JSS, and scam detection. Drafts only — you send. | Advisory |
| [`freelance`](skills/freelance/) | Cross-platform decisions: which marketplace to use, rate-setting, proposal frameworks, client vetting, AI-disclosure basics. | Advisory |
| [`job-search`](skills/job-search/) | Job hunting and contract-role search: application tracking, company research, tailored CV/cover-letter materials, and interview prep. | Advisory |
| [`negotiate`](skills/negotiate/) | Prepares and runs negotiations on your behalf — rates, scope, salary, buying/selling — with hard limits and mandatory approval before any commitment. | Advisory |

### Run the back office

| Skill | What it does | Type |
|-------|--------------|------|
| [`clients`](skills/clients/) | A personal client system: one place per client for contacts, project history, documents, comms logs, preferences, and a leads pipeline. | Advisory |
| [`contracts`](skills/contracts/) | Organizes and tracks contracts: key-term extraction, renewal/termination alerts, clause lookups, and signature/version tracking. Not legal advice. | Advisory |
| [`agency`](skills/agency/) | Turns solo work into an agency: onboarding, scoped proposals/rate cards, multi-client project tracking, deliverable workflows, and team coordination. | Advisory |

`fiverr-gig-optimizer` and `fiverr` are complements: one *builds* the gigs, the
other helps you *sell and scale* them. `clients`, `contracts`, and `agency`
cover everything after the sale.

## Install

Each top-level folder under `skills/` is a standalone skill. Drop the ones you
want into a place Claude Code loads skills from (`~/.claude/skills/` for global,
or a project's `.claude/skills/`).

Install everything:

```bash
git clone https://github.com/mehtab78/freelance-skills /tmp/freelance-skills
cp -r /tmp/freelance-skills/skills/* ~/.claude/skills/
```

Or just one skill:

```bash
git clone https://github.com/mehtab78/freelance-skills /tmp/freelance-skills
cp -r /tmp/freelance-skills/skills/fiverr-gig-optimizer ~/.claude/skills/
```

Then describe what you need in natural language — e.g. *"help me set up my
Fiverr gigs, I do n8n automation and AI chatbots"* or *"draft an Upwork proposal
for this job post"* — and the matching skill triggers.

## Structure

```
.
├── skills/
│   ├── fiverr-gig-optimizer/   # gig generator (SKILL.md + references/ + scripts/)
│   ├── fiverr/                 # Fiverr selling & scaling (advisory)
│   ├── upwork/                 # Upwork proposals & profile (advisory)
│   ├── freelance/              # cross-platform strategy (advisory)
│   ├── job-search/             # job/contract-role hunting (advisory)
│   ├── negotiate/              # rate & deal negotiation (advisory)
│   ├── clients/                # personal client system (advisory)
│   ├── contracts/              # contract tracking & alerts (advisory)
│   └── agency/                 # scaling into an agency (advisory)
├── LICENSE                     # MIT
└── README.md
```

## Requirements

- Most skills are pure Markdown and need nothing.
- `fiverr-gig-optimizer` uses Python 3.8+ (standard library only) for the build
  scripts, and Google Chrome / Microsoft Edge for the optional PDF export (the
  HTML catalog needs neither).

## License

MIT licensed — see [LICENSE](LICENSE).
