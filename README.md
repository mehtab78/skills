# Skills — for Claude Code

A collection of independent [Claude Code](https://claude.com/claude-code) skills:
a **freelance business pack** (Fiverr, Upwork, contracts, clients, agency) and a
**model-routing expert team** (a router that delegates to specialist subagents on
the cheapest capable model tier). Each skill is self-contained and triggers on
its own — install one, several, or all.

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

### Model routing & expert team

| Skill | What it does | Type |
|-------|--------------|------|
| [`model-router`](skills/model-router/) | Classifies any task, picks the cheapest capable model tier (haiku → sonnet → opus → fable), delegates to the right expert via subagents, validates output, escalates on failure. Fable falls back to opus-with-decomposition when unavailable. | Orchestrator |
| [`expert-web-developer`](skills/expert-web-developer/) | Frontend/backend implementation, refactors, tests. | Specialist |
| [`expert-ai-engineer`](skills/expert-ai-engineer/) | LLM integrations, prompts, RAG pipelines, evals. | Specialist |
| [`expert-devops`](skills/expert-devops/) | CI/CD, containers, migrations, incident strategy. | Specialist |
| [`expert-product-strategist`](skills/expert-product-strategist/) | Scoping, prioritization, roadmaps, metrics. | Specialist |
| [`expert-security-reviewer`](skills/expert-security-reviewer/) | Security reviews, threat models; auto second-pass gate on risky work. | Specialist |
| [`expert-data-analyst`](skills/expert-data-analyst/) | SQL, analysis, metric sanity checks. | Specialist |
| [`expert-technical-writer`](skills/expert-technical-writer/) | READMEs, runbooks, changelogs, guides. | Specialist |

Install `model-router` together with the experts — it delegates by pointing
subagents at their `SKILL.md` files.

## Install

Each top-level folder under `skills/` is a standalone skill. Drop the ones you
want into a place Claude Code loads skills from (`~/.claude/skills/` for global,
or a project's `.claude/skills/`).

Install everything:

```bash
git clone https://github.com/mehtab78/skills /tmp/skills
cp -r /tmp/skills/skills/* ~/.claude/skills/
```

Or just one skill:

```bash
git clone https://github.com/mehtab78/skills /tmp/skills
cp -r /tmp/skills/skills/fiverr-gig-optimizer ~/.claude/skills/
```

Then describe what you need in natural language — e.g. *"help me set up my
Fiverr gigs, I do n8n automation and AI chatbots"* or *"draft an Upwork proposal
for this job post"* — and the matching skill triggers.

### As a Claude Code plugin

```bash
claude  # then inside the session:
/plugin marketplace add mehtab78/skills
/plugin install mehtab-skills@mehtab78-skills
```

## Structure

```
.
├── skills/
│   ├── fiverr-gig-optimizer/   # gig generator (SKILL.md + references/ + scripts/)
│   ├── fiverr/                 # Fiverr selling & scaling (SKILL.md + references/)
│   ├── upwork/                 # Upwork proposals & profile (SKILL.md + references/)
│   ├── freelance/              # cross-platform strategy (SKILL.md + references/)
│   ├── job-search/             # job/contract-role hunting (SKILL.md + references/)
│   ├── negotiate/              # rate & deal negotiation (SKILL.md + references/)
│   ├── clients/                # personal client system (SKILL.md only)
│   ├── contracts/              # contract tracking & alerts (SKILL.md + references/)
│   ├── agency/                 # scaling into an agency (SKILL.md + references/)
│   ├── model-router/           # tier router & orchestrator (SKILL.md + references/)
│   └── expert-*/               # 7 specialist skills (web, ai, devops, product, security, data, writer)
├── .claude-plugin/             # plugin.json + marketplace.json (installable as a Claude Code plugin)
├── LICENSE                     # MIT
└── README.md
```

Every skill keeps its detail in `references/` — `SKILL.md` stays short and
points there for depth. `clients` is the one exception: it's small enough that
everything fits in `SKILL.md` alone.

## Requirements

- Most skills are pure Markdown and need nothing.
- `fiverr-gig-optimizer` uses Python 3.8+ (standard library only) for the build
  scripts, and Google Chrome / Microsoft Edge for the optional PDF export (the
  HTML catalog needs neither).

## License

MIT licensed — see [LICENSE](LICENSE).
