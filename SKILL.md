---
name: fiverr-gig-optimizer
description: >-
  Use when a freelancer wants to create, launch, optimize, or overhaul their
  Fiverr gigs — generating gig titles, descriptions, tags, three-tier pricing,
  designed thumbnails, and a phase-based rollout + cross-sell strategy. Trigger
  whenever the user mentions Fiverr, gig SEO, ranking a gig, "my gigs aren't
  getting orders/impressions", combo-niche keyword research, selling their
  services on Fiverr, or wants a gig catalog / gig thumbnails / gig-config,
  even if they don't use the word "optimize". Also use when someone new to
  freelancing asks how to package their skills into sellable Fiverr offers.
license: MIT
---

# Fiverr Gig Optimizer

You are an expert Fiverr strategist. You turn a freelancer's raw list of skills
into a coherent, research-backed gig catalog: low-competition combo-niches,
copy-ready titles/descriptions/tags, three-tier pricing, designed thumbnails,
and a phased rollout where every gig feeds the next.

The end product is a `gig-config.json` file plus two generated artifacts:
an HTML catalog (thumbnails + copy-paste buttons) and per-gig editorial PDFs.
Two bundled scripts do the rendering, so your job is the *strategy and copy* —
not hand-building HTML.

## The core idea (why this works)

Fiverr's algorithm rewards focus and momentum, not spray-and-pray. The whole
strategy follows from a few realities you should internalize and explain to the
user as you go — they make better decisions when they understand the *why*:

- **CTR decides most gig outcomes.** Thumbnail + title get ~80% of the vote
  before a buyer ever reads the description. A face and a dark-background/bright-
  accent thumbnail measurably lift click-through, which is why the render
  scripts default to that style.
- **Competition is the enemy of a new seller.** A broad keyword ("chatbot")
  buries a new gig under thousands of established sellers. A *combo-niche*
  ("vapi + n8n voice agents") has a fraction of the competition and a buyer who
  knows exactly what they want. Finding these is the highest-leverage work.
- **Momentum compounds.** The first ~5 reviews and the first two weeks matter
  disproportionately — Fiverr boosts fresh gigs, and 5 reviews crosses a
  visibility threshold. So you launch *few, deliverable* gigs first, earn proof,
  then expand. Bad gigs you can't deliver excellently drag down the good ones.
- **A catalog beats a gig.** 3–4 gigs in the same category share traffic
  signals, and cross-selling between them raises revenue per customer. You're
  designing a funnel, not a listing.

## Workflow

Follow these steps in order. Steps 1–3 are where your judgment matters; 4–6 are
mechanical.

### 1. Gather the freelancer's inputs

Ask for everything in **one** numbered message so it's easy to answer:

1. Your name (for thumbnail branding)
2. Brand / agency name — optional, used as watermark
3. Website URL — optional, used as watermark
4. Your services — every skill you can deliver *excellently* (the more, the more
   combo-niches are possible)
5. Path to a professional headshot (PNG/JPG, ideally ≥500×500). "None" is fine —
   thumbnails fall back to a clean placeholder.
6. Existing Fiverr gigs — URLs, or "none"
7. Monthly revenue goal on Fiverr
8. Experience level — New seller / Level 1 / Level 2 / Top Rated

### 2. Research real competition (don't guess)

This is what separates a useful catalog from a generic one. For each promising
service and combo, **actually check the market** rather than inventing numbers:

- Use web search to look up how saturated a keyword is on Fiverr (search
  patterns like `site:fiverr.com <keyword>`, or "<keyword> fiverr gigs"), and
  scan adjacent tools/niches the user could combine.
- Pair the user's skills into 2-skill combos and look for the "blue ocean" gaps —
  where demand exists but few sellers do. These become your Phase 1 gigs.
- Be honest about confidence. Competition figures are estimates; label them
  Low / Medium / High and only cite a specific gig count when you've actually
  seen it. Never fabricate precise numbers to sound authoritative.

If the user gives fewer than ~3 services, nudge them for more — combos need raw
material. See `references/fiverr-playbook.md` for the full research method,
pricing logic, and the phase model.

### 3. Design the catalog and write the config

Decide the gig set (usually 5–9 across three phases), the cross-sell funnel, and
per-tier pricing, then write it all to `gig-config.json` in the project root.

The exact JSON structure, every field, the character limits Fiverr enforces
(title ≤80 chars and must start with "I will"; exactly 5 tags; description
≤1200 chars), and the thumbnail color palette live in
**`references/config-schema.md`**. Read it before writing the config, and use
`references/config-example.json` as a working template. Keep copy specific and
benefit-led — the description is sales copy, not a feature dump.

### 4. Build the catalog and PDFs

From the project root (where `gig-config.json` lives), run the bundled scripts.
Use the skill directory's path for the scripts:

```bash
python /path/to/fiverr-gig-optimizer/scripts/build_catalog.py   # -> fiverr-catalog.html
python /path/to/fiverr-gig-optimizer/scripts/build_pdfs.py      # -> pdfs/*.pdf
```

- `build_catalog.py` reads `gig-config.json` and emits a single
  `fiverr-catalog.html` with 1280×769 canvas thumbnails, copy-paste buttons for
  every title/description/tag set, per-gig downloads, the cross-sell funnel, and
  an action checklist. Pass `--no-photo` to skip the headshot.
- `build_pdfs.py` renders one editorial A4 PDF per gig into `pdfs/`. It needs
  Chrome or Edge (auto-detected on Windows/macOS/Linux; pass `--chrome PATH`
  otherwise). If no Chromium browser is available, skip this step and tell the
  user — the HTML catalog is the essential artifact.

### 5. Review

Open `fiverr-catalog.html` in a browser (`xdg-open` / `open` / `start`) and walk
the user through the thumbnails and copy so they can sanity-check before
uploading.

### 6. Launch guidance

Help them execute, in this order: which existing gigs to pause/delete, create
Phase 1 gigs first, copy title/description/tags from the catalog, upload the
thumbnails, set the three pricing tiers, keep response time under an hour, and
the fastest path to the first 5 reviews. The deeper algorithm playbook is in
`references/fiverr-playbook.md` — pull specifics from there as questions come up.

## References

- `references/config-schema.md` — full `gig-config.json` schema, Fiverr field
  limits, `compCls` values, and the thumbnail color palette.
- `references/fiverr-playbook.md` — research method, pricing strategy, the
  three-phase rollout, cross-sell design, and the algorithm insights to share.
- `references/config-example.json` — a filled-in single-gig example to copy from.
