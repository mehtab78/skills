# Fiverr Gig Optimizer — a Claude Code Skill

A [Claude Code](https://claude.com/claude-code) skill that turns a freelancer's
raw list of skills into a research-backed Fiverr gig catalog: low-competition
combo-niches, copy-ready titles/descriptions/tags, three-tier pricing, designed
thumbnails, and a phase-based rollout where every gig cross-sells into the next.

It produces a `gig-config.json`, then renders:

- **`fiverr-catalog.html`** — 1280×769 thumbnails, copy-paste buttons for every
  title/description/tag, a cross-sell funnel map, and an action checklist.
- **`pdfs/*.pdf`** — one editorial A4 PDF per gig (needs Chrome or Edge).

## Install

Clone into your Claude Code skills directory so Claude can discover it:

```bash
git clone https://github.com/mehtab78/gig-optimizer ~/.claude/skills/fiverr-gig-optimizer
```

(Or drop the folder anywhere Claude Code loads skills from — a project's
`.claude/skills/`, or a plugin.)

Then just describe what you want in natural language — e.g. *"help me set up my
Fiverr gigs, I do n8n automation and AI chatbots"* — and the skill triggers.

## How it works

1. **Gather** your name, services, headshot, goals, and experience level.
2. **Research** real Fiverr competition to find combo-niche gaps.
3. **Generate** `gig-config.json` — the full catalog strategy.
4. **Build** the HTML catalog and per-gig PDFs from bundled scripts.
5. **Review** in the browser.
6. **Launch** with step-by-step guidance for uploading to Fiverr.

## Structure

```
fiverr-gig-optimizer/
├── SKILL.md                        # the skill: workflow + strategy
├── references/
│   ├── config-schema.md            # gig-config.json schema + field limits + palette
│   ├── fiverr-playbook.md          # research method, pricing, phases, algorithm notes
│   └── config-example.json         # a filled-in single-gig template
├── scripts/
│   ├── build_catalog.py            # gig-config.json -> fiverr-catalog.html
│   └── build_pdfs.py               # gig-config.json -> pdfs/*.pdf (Chrome/Edge)
└── README.md
```

## Requirements

- Python 3.8+ (standard library only — no pip installs).
- Google Chrome or Microsoft Edge for PDF export (the HTML catalog needs
  neither).

## Credits

Adapted from the original
[fiverr-gig-optimizer](https://github.com/waseemnasir2k26/fiverr-gig-optimizer)
slash-command project, reworked into a self-triggering skill with real
competition research and progressive-disclosure references. MIT licensed.
