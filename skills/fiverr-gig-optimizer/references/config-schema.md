# `gig-config.json` schema

The build scripts read this file from the project root. Write it there once the
strategy is decided. `references/config-example.json` is a filled-in template
for a single gig, copy its shape.

## Top-level structure

```json
{
  "seller":   { ... },      // branding for thumbnails + watermark
  "strategy": { ... },      // catalog-level summary (shown in the catalog hero)
  "gigs":     [ { ... } ]   // one object per gig, in launch order
}
```

### `seller`

| field     | required | notes                                              |
|-----------|----------|----------------------------------------------------|
| `name`    | yes      | Used on thumbnails and as watermark fallback.      |
| `brand`   | no       | Watermark text. Falls back to `name`.              |
| `website` | no       | Appended to the watermark.                         |
| `photo`   | no       | Path to headshot (PNG/JPG/WebP). Missing = clean placeholder. A `.txt`/`.b64` file containing base64 is also accepted. |

### `strategy`

| field             | notes                                             |
|-------------------|---------------------------------------------------|
| `totalGigs`       | Total gig count.                                  |
| `phase1Count` / `phase2Count` / `phase3Count` | Gigs per phase.       |
| `monthlyTarget`   | Display string, e.g. `"$8,000"`.                  |
| `primaryCategory` | The Fiverr category the catalog concentrates in.  |

### `gigs[]`, one per gig

| field         | notes |
|---------------|-------|
| `id`          | Integer, 1-based, in launch order. |
| `phase`       | `1`, `2`, or `3` (see the playbook's phase model). |
| `title`       | **Must start with "I will"** and be **≤ 80 characters:** Fiverr enforces both. |
| `cat`         | `"Category > Subcategory"`, e.g. `"Programming & Tech > AI Coding"`. |
| `tags`        | **Exactly 5** search tags. Fewer weakens SEO; more is rejected. |
| `desc`        | Gig description, **≤ 1200 characters**. Use `\n` for line breaks and `•` / `➔` bullets. This is sales copy. |
| `competition` | Human-readable estimate, e.g. `"~24 gigs (LOW)"`. Only cite a number you actually verified. |
| `compCls`     | Color class for the badge: `"lo"` (green), `"md"` (orange), `"hi"` (red). |
| `xsell`       | Cross-sell line, e.g. `"CROSS-SELLS TO: Gig #2 (AI Chatbot) • Gig #5 (AI Bundle)"`. |
| `pricing`     | `basic` / `standard` / `premium` objects (below). |
| `img`         | Thumbnail + PDF-summary fields (below). |

### `pricing.{basic|standard|premium}`

| field   | notes |
|---------|-------|
| `name`  | Tier name, e.g. `"Starter"` / `"Business"` / `"Enterprise"`. |
| `title` | One-line package title. |
| `price` | Integer dollars. |
| `del`   | Delivery time, e.g. `"3 days"`. |
| `rev`   | Revisions, e.g. `"2"`. |
| `items` | Array of deliverable strings. Standard usually gets one more than Basic; Premium one more than Standard. |

The catalog marks **Standard** as "POPULAR". Price it as the one you actually
want them to buy (see pricing strategy in the playbook).

### `img`

| field      | notes |
|------------|-------|
| `bg1`      | Darker background hex (gradient stop 1 & 3). |
| `bg2`      | Slightly lighter background hex (gradient middle). |
| `accent`   | Bright highlight hex: unique per gig. |
| `headline` | 2-4 words, ALL CAPS. Auto-shrinks to fit. |
| `sub`      | One-line subtitle under the headline. |
| `badge`    | Short credibility badge, e.g. `"50+ SYSTEMS BUILT"`. |
| `tools`    | Up to ~6 short tool/tech pills. |
| `pdfWhat`  | One-line "what this gig offers" summary for the PDF cover. |

## Thumbnail color palette

Give each gig a distinct accent so the catalog reads as a set. Pair each accent
with its two backgrounds:

| accent | hex       | bg1       | bg2       |
|--------|-----------|-----------|-----------|
| Cyan   | `#06b6d4` | `#030a0a` | `#061818` |
| Purple | `#a855f7` | `#08050e` | `#18082a` |
| Blue   | `#3b82f6` | `#060a14` | `#0e1a30` |
| Red    | `#ef4444` | `#100505` | `#250a0a` |
| Gold   | `#FFD700` | `#0a0a03` | `#1a1500` |
| Orange | `#f97316` | `#100a03` | `#281a06` |
| Green  | `#1DBF73` | `#030a05` | `#061a0e` |
| Lime   | `#84cc16` | `#050a03` | `#101a06` |

## Handling limits gracefully

Rather than silently truncating, help the user stay within Fiverr's rules:

- Title > 80 chars → tighten the wording with them; don't just cut mid-word.
- Description > 1200 chars → trim to the strongest benefits, keep the CTA and the
  cross-sell lines.
- Fewer than 5 tags → ask for more keywords; the combo-niche research usually
  surfaces them.
- Missing headshot → proceed with the placeholder and mention that a real face
  typically lifts CTR, so it's worth adding later.
