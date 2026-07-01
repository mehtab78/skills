# Fiverr playbook, research, pricing, phases, algorithm

Background for the strategy work in steps 2-3 and the launch guidance in step 6.
Pull specifics from here; share the reasoning with the user so they can make
their own calls, not just follow orders.

## Competition research method

The goal is to find **combo-niches**: two of the user's skills combined into an
offer that has real demand but far fewer sellers than either skill alone.

1. List every service the user can deliver excellently.
2. Generate 2-skill combinations (e.g. `n8n` + `AI` → "n8n AI automation";
   `vapi` + `n8n` → "voice AI agents wired into automations").
3. For each candidate, gauge saturation with real web search, don't invent
   counts. Useful queries:
   - `site:fiverr.com <keyword>`
   - `<keyword> fiverr` (skim how many established sellers appear)
   - Look for whether buyers are actively searching (blog posts, Reddit,
     tool communities asking "who can build X").
4. Rank candidates: **high demand + low competition = Phase 1 material.** Broad,
   saturated keywords are traps for a new seller even if the user is skilled.
5. Label each `Low` / `Medium` / `High` and set `compCls` accordingly. Cite a
   specific gig count only when you actually saw it.

Rule of thumb from the field: broad terms like "chatbot" can have 10,000+ gigs,
while a specific combo like "vapi + n8n" might have a couple dozen. The buyer who
searches the specific term also converts better because they know what they want.

## Category strategy

- **Concentrate.** 3-4 gigs in the *same* Fiverr category share traffic and
  ranking signals, the algorithm reads you as a specialist.
- **Only list what you can nail.** A gig you deliver poorly earns bad reviews
  that drag down every other gig on the account. Fewer excellent gigs beat many
  mediocre ones.
- **5 reviews is the visibility threshold**, and **response time under 1 hour**
  is a strong ranking signal. Both are within the seller's control from day one.

## Pricing strategy

Three tiers, each with a job:

- **Basic:** the entry point that wins the click. Low friction. ($47-$197)
- **Standard:** where the money is; mark it POPULAR and design it as the
  obvious best value. ($197-$597)
- **Premium:** an anchor that makes Standard look reasonable. Some buyers take
  it; its main job is comparison. ($497-$997+)

Phase-adjust: **Phase 1 gigs price lower** to win the first reviews fast. Once
there's social proof, **Phase 2+ gigs price higher**. Each tier should add one
concrete deliverable over the one below it so the upgrade feels earned.

## The three-phase rollout

- **Phase 1: Launch now (3-4 gigs).** Lowest-competition combo-niches you can
  deliver excellently. Priced to earn the first 5 reviews quickly.
- **Phase 2: After 5+ reviews (2-3 gigs).** Premium upsells that lean on the
  social proof you just built. Higher prices.
- **Phase 3: After Level 2 (1-2 gigs).** Strategic expansion into whatever is
  actually converting. Data-driven, not guessed.

## Cross-sell funnel

Every gig should reference 2-3 related gigs in its description (the `xsell`
field). Map the funnel so Phase 1 gigs feed into Phase 2 premium/bundle gigs.
This raises revenue per customer without new traffic, the buyer is already
sold on you.

## Algorithm insights to share

- **CTR is king:** thumbnail + title drive ~80% of gig success.
- **A face in the thumbnail** lifts CTR meaningfully (commonly cited ~25-40%).
- **Dark background + one bright accent** is the highest-performing thumbnail
  style (what the render script produces by default).
- **The first two weeks** matter most: Fiverr boosts new gigs; use the window.
- **Combo keywords** face 10-100× less competition than broad terms.
- **Same-category gigs** reinforce each other's ranking.
- **Bad gigs hurt good gigs:** pause or delete underperformers.
- **Buyer request responses** are often the fastest route to a first order.
- **A gig video** tends to add impressions and orders, worth adding after
  launch.
- **An FAQ section** on every gig converts better and cuts pre-order messages.

## Launch checklist (step 6)

1. Pause/delete existing gigs that dilute the new focus.
2. Create Phase 1 gigs first, in `id` order.
3. Copy title, description, and tags straight from the catalog buttons.
4. Download each thumbnail PNG and upload it.
5. Set the three pricing tiers exactly as configured.
6. Keep response time under an hour, it's a ranking signal from day one.
7. Line up the first 5 reviews (launch pricing, buyer requests, existing
   network) as the top priority.
