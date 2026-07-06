---
name: brand-naming
description: >
  Brand name generator for startups, products, and apps. Uses naming patterns
  from iconic OSS projects (Kubernetes, Vite, Docker, Svelte) and startup
  playbooks. Invoke for any naming request: "name my startup", "what should I
  call this", "brand name ideas", "domain name ideas". If someone needs to name
  anything commercial, use this skill.
---

# Brand Naming

Generate names with domain hints and brandability rationale. Names the user
would actually want on a business card, not a wall of filler.

---

## Step 1 — Gather context (if not already provided)

Three things before generating:

1. **What it is:** industry, what problem it solves, what it feels like to use
2. **Brand attributes:** 2-4 adjectives (e.g. "bold, technical, international")
3. **Constraints:** length cap, preferred TLD, words to avoid, or "none"

If the user gave all three, skip ahead. If any are missing, ask all at once.
If they wave context away, infer from industry and use mixed strategy.

---

## Step 2 — Generate 20 names across multiple strategies

Pull from the pools below. Use at least 5 strategies across the 20 names.
Strong names often combine two pools (a foreign word that is also a compound,
a Greek root that happens to be a perfect misspelling candidate).

---

### Pool A — The OSS playbook
*Patterns proven by Kubernetes, Vite, Docker, Svelte, Redis, Bun, Deno, Vue*

| Strategy | How | Famous example | Domain outlook |
|---|---|---|---|
| **Foreign word that means the product** | Pick a language (French, Japanese, German, Greek, Swahili...) and find a word that translates to the product's core feeling | Vite = French "fast" / Vue = French "view" / Svelte = French-Italian "slender" / Zustand = German "state" / Jotai = Japanese "state" / Hono = Japanese "flame" | 🟢 usually clear |
| **Greek or Latin root** | Mine mythology, nautical terms, classical science. The well is deeper than it looks | Kubernetes = Greek "helmsman" / Electron = physics / Prometheus = Greek titan / Axios = Greek "worthy" | 🟢 usually clear |
| **Acronym-as-name** | Make a meaningful acronym where the letters spell a real-sounding word | Redis = **Re**mote **Di**ctionary **S**erver / GNU = GNU's Not Unix / Nginx = Engine-X | 🟡 depends |
| **Anagram** | Rearrange letters of a relevant word | Deno = anagram of Node | 🟢 if coined |
| **Unexpected short real word** | Borrow a common noun that *feels* like the product but is not a literal description. Unforgettable, domain-hard | Bun / Rust / Go / Yarn / Babel / Parcel / Rails | 🔴 .com likely gone, plan for .io/.dev |
| **Metaphor from the product's feeling** | Not what it does, what it is *like*. Docker workers load containers; Tailwind is the wind behind you | Docker / Tailwind / Ember / Phoenix | 🟡 varies |
| **Functional compound** | Two relevant words fused into one | Webpack (web+pack) / Supabase (supra+base) / GitHub (git+hub) / Rollup | 🟡 |
| **Portmanteau + meaning** | Blend a domain word with a quality word | Debian (Deb+Ian, creator names) / Fedora | 🟢 |

---

### Pool B — Startup naming classics

| Strategy | How | Domain outlook |
|---|---|---|
| **Invented word** | Coin a new word: distinct syllables, pronounceable anywhere | Spotify / Kodak / Xerox | 🟢 |
| **Creative misspelling** | Drop a vowel or swap a letter from a real word | Lyft / Flickr / Fiverr / Tumblr | 🟢 |
| **Suffix pattern** | Attach -ify, -ly, -io, -hub, -able, -ment | Shopify / Grammarly / Calendly | 🟡 crowded |
| **Abstract / aspirational** | Borrow from nature, science, emotion | Amazon / Apple / Uber / Stripe | 🟡-🔴 |

---

### Pool C — Cross-cultural check

Before recommending any name, run it through:
- Does it sound rude, funny, or mean something else in Spanish, French, German, Japanese, Mandarin, Arabic?
- Can someone whose first language is not English pronounce it without coaching?
- Does it transliterate to something search-engine-unfriendly?

Flag names that fail rather than silently dropping them. Sometimes a problematic name is still the right pick once the user knows the tradeoff.

---

### Pool D — Domain availability heuristics

No actual lookup, just pattern signals:

| Signal | Hint |
|---|---|
| Invented word, 8+ chars, unusual combo | 🟢 Likely available |
| Semi-common compound, moderate length, suffix patterns | 🟡 Maybe available |
| Real English word, short/common, popular prefixes (get-, my-, go-) | 🔴 Likely taken |

Include the .com signal. If 🔴, suggest .io / .dev / .app as fallback and say so explicitly.

---

## Step 3 — Format the output

Table first, 20 rows:

```
| # | Name | Strategy | Vibe | .com |
|---|------|----------|------|------|
| 1 | Vaultry | Invented | Secure, premium | 🟢 |
```

Brandability scores for top candidates only, not all 20. Rate on: memorability,
pronounceability (works in non-English mouths), spellability when heard,
uniqueness. One score out of 10, one line of rationale.

Top 3-5 picks: one sentence each on why it fits this specific brand.

Three wildcards: bolder, riskier, higher upside. At least one from Pool A.
Label them: *"These are bolder bets, not universally appropriate."*

---

## Step 4 — Iteration

If the user says "I like X but not Y" or "more like X":
- Generate 10 focused variants, not another full 20
- Narrow to the strategies that resonated
- Try to surface *why* they liked what they liked so each round gets sharper

---

## What makes a name work

The best names do at least one of these things well:

1. **Mean the product in another language.** Vite, Vue, and Svelte all do this. You discover what the word means and the name earns its keep.

2. **Borrow from a deep well.** Greek, Latin, mythology: Kubernetes means "helmsman," Electron is a physics particle, Prometheus is the titan who stole fire. These give a name weight without sounding corporate.

3. **Create a metaphor that fits the feeling, not the function.** Docker was named for dock workers who load and unload containers. Tailwind is the wind at your back. You do not need to have used these tools to feel what they do.

4. **Own their search term completely.** Invented and misspelled names have no competitors. Spotify owns "Spotify." Lyft owns "Lyft." Worth the up-front weirdness.

5. **Be deceptively simple.** Bun, Rust, Go, Yarn: short real words applied sideways. These are unforgettable but nearly impossible to get as a .com. Plan the TLD strategy before falling in love.

Names that describe the product literally are almost always weaker than names that say what it feels like to use it. "InvoiceTracker" tells you what exists. "Ledgr" tells you what kind of thing you are dealing with.
