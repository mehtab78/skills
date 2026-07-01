#!/usr/bin/env python3
"""
build_catalog.py — turn gig-config.json into a single review-ready HTML catalog.

The output (fiverr-catalog.html) is self-contained: it renders a 1280x769 canvas
thumbnail per gig, shows the copy-paste-ready title / description / tags / pricing,
and provides buttons to copy each field and download each thumbnail as a PNG.

Usage:
    python build_catalog.py                 # reads gig-config.json in the cwd
    python build_catalog.py my-config.json  # custom config path
    python build_catalog.py --no-photo      # skip embedding the seller photo
    python build_catalog.py --out cat.html  # custom output path
"""
import argparse
import base64
import json
import os
import sys


def load_photo(seller, config_dir, skip):
    """Return a data: URI for the seller photo, or '' if none/unavailable."""
    if skip:
        return ""
    rel = seller.get("photo")
    if not rel:
        return ""
    for path in (rel, os.path.join(config_dir, rel)):
        if not os.path.isfile(path):
            continue
        ext = os.path.splitext(path)[1].lower().lstrip(".")
        mime = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg",
                "webp": "image/webp"}.get(ext, "image/png")
        with open(path, "rb") as fh:
            raw = base64.b64encode(fh.read()).decode("ascii")
        print(f"  embedded photo: {path} ({len(raw) // 1024} KB)")
        return f"data:{mime};base64,{raw}"
    print(f"  photo not found at '{rel}' — rendering with a placeholder")
    return ""


def funnel_text(gigs):
    """A plain-text cross-sell map, highest-priced gig at the top."""
    if not gigs:
        return "(no gigs)"
    lines = []
    anchor = max(gigs, key=lambda g: g["pricing"]["premium"]["price"])
    lines.append(f"        [ {anchor['img']['headline']} ]  <- anchor / bundle (gig #{anchor['id']})")
    lines.append("               |")
    for g in gigs:
        if g["id"] == anchor["id"]:
            continue
        lo = g["pricing"]["basic"]["price"]
        hi = g["pricing"]["premium"]["price"]
        lines.append(f"   +-- gig #{g['id']}: {g['img']['headline']}  (${lo}-${hi})")
    return "\n".join(lines)


def action_plan(phase_counts):
    p1, p2, p3 = phase_counts
    steps = [
        "Today — pause or delete any existing gig that dilutes your focus.",
        f"This week — publish your {p1} Phase 1 gig(s): lowest competition, "
        "fastest to a first review.",
        "Weeks 2-3 — win the first 5 reviews on each (launch pricing, buyer "
        "requests), and reply to every message within an hour.",
        "Weeks 3-4 — add a short gig video where you can (more impressions, "
        "more orders).",
    ]
    if p2:
        steps.append(f"Week 6+ — launch your {p2} Phase 2 upsell gig(s) once you "
                     "have 5+ reviews.")
    if p3:
        steps.append(f"After Level 2 — launch your {p3} Phase 3 gig(s), guided by "
                     "what's actually converting.")
    return steps


PAGE_CSS = """
:root{
  --bg:#07070b; --card:#101018; --edge:#20202c; --ink:#e7e7ee; --dim:#8a8a99;
  --p1:#22c55e; --p2:#a855f7; --p3:#3b82f6; --gold:#f5c518;
}
*{margin:0;padding:0;box-sizing:border-box}
body{background:var(--bg);color:var(--ink);
  font-family:'Inter',system-ui,-apple-system,Segoe UI,Roboto,sans-serif;line-height:1.6}
.wrap{max-width:1180px;margin:0 auto;padding:0 20px}
header{padding:52px 0 34px;text-align:center;border-bottom:1px solid var(--edge);
  background:radial-gradient(ellipse at 50% -10%,rgba(168,85,247,.10),transparent 60%)}
.badges{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-bottom:16px}
.chip{font-size:10px;font-weight:700;letter-spacing:.8px;padding:4px 11px;border-radius:20px;
  border:1px solid var(--edge);color:var(--dim);text-transform:uppercase}
h1{font-size:34px;font-weight:800;letter-spacing:-1px}
h1 .a{color:var(--p1)} h1 .b{color:var(--p2)}
.sub{color:var(--dim);max-width:640px;margin:10px auto 0;font-size:14px}
.stats{display:flex;gap:30px;justify-content:center;margin-top:22px;flex-wrap:wrap}
.stat b{display:block;font-size:22px;font-weight:800}
.stat span{font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:1px}
.funnel{margin:26px auto 0;max-width:760px;background:rgba(255,255,255,.02);
  border:1px solid var(--edge);border-radius:12px;padding:16px}
.funnel h3{font-size:11px;letter-spacing:1.5px;text-transform:uppercase;color:var(--p1);
  text-align:center;margin-bottom:10px}
.funnel pre{white-space:pre;font-size:11px;color:#9a9aa8;overflow-x:auto;text-align:center}
.toolbar{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin:22px 0}
.tbtn{border:none;border-radius:8px;padding:9px 16px;font-size:12px;font-weight:700;
  cursor:pointer;color:#04120a;background:var(--p1)}
.tbtn.alt{background:var(--p2);color:#fff} .tbtn.ghost{background:#181822;color:var(--ink)}
.section-title{display:flex;align-items:center;gap:12px;margin:34px 0 18px}
.section-title span{font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;
  white-space:nowrap}
.section-title .ln{flex:1;height:1px;background:var(--edge)}
.card{background:var(--card);border:1px solid var(--edge);border-radius:14px;
  overflow:hidden;margin-bottom:26px}
.card.p1{border-color:rgba(34,197,94,.35)}
.card.p2{border-color:rgba(168,85,247,.32)}
.card.p3{border-color:rgba(59,130,246,.30)}
.thumb{width:100%;display:block;background:#000}
.body{padding:20px 22px}
.cat{font-size:10px;letter-spacing:.6px;text-transform:uppercase;color:var(--p1);font-weight:700}
.title{font-size:17px;font-weight:700;margin:5px 0 2px;color:#fff}
.count{font-size:11px;color:var(--dim);font-weight:400;margin-left:6px}
.meta{font-size:11px;color:var(--dim);margin:6px 0 12px;display:flex;gap:14px;flex-wrap:wrap}
.meta .lo{color:var(--p1)} .meta .md{color:#f59e0b} .meta .hi{color:#ef4444}
.xsell{font-size:11px;color:#9a9aa8;background:rgba(34,197,94,.05);
  border:1px solid rgba(34,197,94,.14);border-radius:8px;padding:9px 12px;margin-bottom:14px}
.flabel{font-size:10px;letter-spacing:1px;text-transform:uppercase;color:var(--dim);
  font-weight:700;margin-bottom:6px}
.tags{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:14px}
.tag{font-size:11px;padding:3px 9px;border-radius:6px;background:rgba(34,197,94,.07);
  border:1px solid rgba(34,197,94,.16);color:#7ee2a8}
.desc{font-size:12.5px;color:#b6b6c2;white-space:pre-wrap;max-height:150px;overflow:hidden;
  transition:max-height .3s;margin-bottom:4px}
.desc.open{max-height:1400px}
.more{font-size:11px;color:var(--p1);cursor:pointer;font-weight:600}
.tiers{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin:14px 0}
.tier{border:1px solid var(--edge);border-radius:9px;padding:13px 11px;text-align:center;position:relative}
.tier.best{border-color:var(--p1);background:rgba(34,197,94,.04)}
.tier.best::after{content:'POPULAR';position:absolute;top:-8px;left:50%;transform:translateX(-50%);
  background:var(--p1);color:#04120a;font-size:7px;font-weight:800;padding:1px 7px;border-radius:4px;
  letter-spacing:.6px}
.tier .tn{font-size:9px;letter-spacing:.6px;text-transform:uppercase;color:var(--dim);font-weight:700}
.tier .tt{font-size:11px;color:#d0d0da;margin:4px 0 6px;min-height:28px;display:flex;
  align-items:center;justify-content:center}
.tier .tp{font-size:23px;font-weight:800;color:var(--p1)}
.tier ul{list-style:none;text-align:left;margin-top:8px}
.tier li{font-size:10px;color:#9a9aa8;padding:1px 0}
.tier li::before{content:'+ ';color:var(--p1)}
.actions{display:flex;gap:7px;flex-wrap:wrap;padding-top:14px;border-top:1px solid var(--edge)}
.act{border:1px solid var(--edge);background:#181822;color:var(--ink);border-radius:7px;
  padding:6px 11px;font-size:10px;font-weight:600;cursor:pointer}
.act.k{color:var(--p1);border-color:rgba(34,197,94,.25);background:rgba(34,197,94,.07)}
.plan{max-width:900px;margin:24px auto 0;background:rgba(255,255,255,.02);
  border:1px solid var(--edge);border-radius:12px;padding:22px}
.plan h3{font-size:12px;letter-spacing:1.5px;text-transform:uppercase;color:#ef4444;margin-bottom:12px}
.plan ol{padding-left:20px;font-size:13px;color:#b6b6c2;line-height:1.9}
footer{text-align:center;padding:30px 0;border-top:1px solid var(--edge);margin-top:40px;
  font-size:11px;color:#4a4a57}
.toast{position:fixed;bottom:22px;right:22px;background:var(--p1);color:#04120a;font-weight:700;
  font-size:12px;padding:9px 15px;border-radius:8px;opacity:0;transform:translateY(8px);
  transition:.25s;pointer-events:none}
.toast.on{opacity:1;transform:translateY(0)}
@media(max-width:720px){.tiers{grid-template-columns:1fr}h1{font-size:26px}}
"""

RENDER_JS = r"""
const GIGS = __GIGS__;
const PHOTO = __PHOTO__;
const MARK = __MARK__;
const PHASE_LABEL = {1:'Phase 1 - Launch now',2:'Phase 2 - After 5 reviews',3:'Phase 3 - After Level 2'};

const portrait = new Image();
if (PHOTO) portrait.src = PHOTO;

function esc(s){const d=document.createElement('div');d.textContent=s==null?'':s;return d.innerHTML;}
function toast(msg){const t=document.getElementById('toast');t.textContent=msg;t.classList.add('on');
  clearTimeout(t._t);t._t=setTimeout(()=>t.classList.remove('on'),1600);}
function copy(text,label){navigator.clipboard.writeText(text).then(()=>toast('Copied '+label));}
function rgba(hex,a){hex=hex.replace('#','');return 'rgba('+parseInt(hex.slice(0,2),16)+','+
  parseInt(hex.slice(2,4),16)+','+parseInt(hex.slice(4,6),16)+','+a+')';}
function roundRect(c,x,y,w,h,r){c.beginPath();c.moveTo(x+r,y);c.arcTo(x+w,y,x+w,y+h,r);
  c.arcTo(x+w,y+h,x,y+h,r);c.arcTo(x,y+h,x,y,r);c.arcTo(x,y,x+w,y,r);c.closePath();}

function paintThumb(canvas, g){
  const im = g.img, ac = im.accent;
  const W = 1280, H = 769, cx = W/2;
  canvas.width = W; canvas.height = H;
  const c = canvas.getContext('2d');

  const grad = c.createLinearGradient(0,0,W,H);
  grad.addColorStop(0, im.bg1); grad.addColorStop(.5, im.bg2); grad.addColorStop(1, im.bg1);
  c.fillStyle = grad; c.fillRect(0,0,W,H);

  c.fillStyle = 'rgba(255,255,255,.02)';
  for(let x=0;x<W;x+=34) for(let y=0;y<H;y+=34){c.beginPath();c.arc(x,y,.8,0,7);c.fill();}

  const glow = c.createRadialGradient(cx,320,0,cx,320,520);
  glow.addColorStop(0, rgba(ac,.16)); glow.addColorStop(1,'transparent');
  c.fillStyle = glow; c.fillRect(0,0,W,H);

  c.strokeStyle = rgba(ac,.30); c.lineWidth = 2;
  roundRect(c,14,14,W-28,H-28,16); c.stroke();

  if(im.badge){
    c.font = '700 13px Inter,sans-serif';
    const bw = c.measureText(im.badge).width + 30;
    roundRect(c, cx-bw/2, 34, bw, 30, 15);
    c.fillStyle = rgba(ac,.13); c.fill();
    c.strokeStyle = rgba(ac,.5); c.lineWidth = 1.5; c.stroke();
    c.fillStyle = ac; c.textAlign='center'; c.textBaseline='middle';
    c.fillText(im.badge, cx, 50);
  }

  const pr = 96, pcy = 196;
  c.save(); c.beginPath(); c.arc(cx,pcy,pr,0,7); c.closePath(); c.clip();
  if(PHOTO && portrait.complete && portrait.naturalWidth){
    const s = Math.max(2*pr/portrait.naturalWidth, 2*pr/portrait.naturalHeight);
    const w = portrait.naturalWidth*s, h = portrait.naturalHeight*s;
    c.drawImage(portrait, cx-w/2, pcy-h/2, w, h);
  } else {
    c.fillStyle = rgba(ac,.18); c.fillRect(cx-pr,pcy-pr,2*pr,2*pr);
  }
  c.restore();
  c.strokeStyle = rgba(ac,.55); c.lineWidth = 3;
  c.beginPath(); c.arc(cx,pcy,pr+4,0,7); c.stroke();

  let fs = im.headline.length > 18 ? 58 : 72;
  c.font = '800 '+fs+'px Inter,sans-serif';
  while(c.measureText(im.headline).width > W-140 && fs > 30){fs-=3;c.font='800 '+fs+'px Inter,sans-serif';}
  c.textAlign='center'; c.textBaseline='top';
  c.save(); c.shadowColor = rgba(ac,.5); c.shadowBlur = 30;
  c.fillStyle = '#fff'; c.fillText(im.headline, cx, 336); c.restore();

  const barY = 336 + fs + 12;
  c.fillStyle = ac; roundRect(c, cx-36, barY, 72, 4, 2); c.fill();

  if(im.sub){
    let sf = 20; c.font = '500 '+sf+'px Inter,sans-serif';
    while(c.measureText(im.sub).width > W-160 && sf > 12){sf-=1;c.font='500 '+sf+'px Inter,sans-serif';}
    c.fillStyle = 'rgba(255,255,255,.55)'; c.fillText(im.sub, cx, barY+18);
  }

  const tools = (im.tools||[]).slice(0,6);
  if(tools.length){
    c.font = '600 12px Inter,sans-serif';
    const pad = 14, gap = 9;
    const widths = tools.map(t => c.measureText(t).width + pad*2);
    let total = widths.reduce((a,b)=>a+b,0) + gap*(tools.length-1);
    let x = cx - total/2; const y = H - 116;
    tools.forEach((t,i)=>{
      roundRect(c, x, y, widths[i], 28, 7);
      c.fillStyle = rgba(ac,.10); c.fill();
      c.strokeStyle = rgba(ac,.30); c.lineWidth = 1; c.stroke();
      c.fillStyle = 'rgba(255,255,255,.7)'; c.textAlign='center'; c.textBaseline='middle';
      c.fillText(t, x+widths[i]/2, y+14);
      x += widths[i] + gap;
    });
  }

  c.font = '700 11px Inter,sans-serif'; c.fillStyle = 'rgba(255,255,255,.10)';
  c.textAlign='center'; c.textBaseline='bottom'; c.fillText(MARK, cx, H-24);
}

function tierHTML(t, best){
  const items = (t.items||[]).map(i=>'<li>'+esc(i)+'</li>').join('');
  return '<div class="tier'+(best?' best':'')+'">'+
    '<div class="tn">'+esc(t.name)+'</div>'+
    '<div class="tt">'+esc(t.title||'')+'</div>'+
    '<div class="tp">$'+t.price+'</div>'+
    '<div style="font-size:10px;color:#8a8a99;margin-top:4px">'+esc(t.del)+' &middot; '+esc(t.rev)+' rev</div>'+
    '<ul>'+items+'</ul></div>';
}

function gigCard(g){
  const el = document.createElement('div');
  el.className = 'card p'+g.phase;
  const tags = g.tags.map(t=>'<span class="tag">'+esc(t)+'</span>').join('');
  el.innerHTML =
    '<canvas class="thumb" id="thumb'+g.id+'"></canvas>'+
    '<div class="body">'+
      '<div class="cat">'+esc(g.cat)+'</div>'+
      '<div class="title">'+esc(g.title)+'<span class="count">'+g.title.length+'/80</span></div>'+
      '<div class="meta"><span>'+esc(PHASE_LABEL[g.phase]||('Phase '+g.phase))+'</span>'+
        '<span class="'+g.compCls+'">Competition: '+esc(g.competition)+'</span></div>'+
      '<div class="xsell">'+esc(g.xsell)+'</div>'+
      '<div class="flabel">Tags '+g.tags.length+'/5</div><div class="tags">'+tags+'</div>'+
      '<div class="flabel">Description '+g.desc.length+'/1200</div>'+
      '<div class="desc" id="desc'+g.id+'">'+esc(g.desc)+'</div>'+
      '<span class="more" data-t="'+g.id+'">Show more</span>'+
      '<div class="tiers">'+tierHTML(g.pricing.basic,false)+tierHTML(g.pricing.standard,true)+
        tierHTML(g.pricing.premium,false)+'</div>'+
      '<div class="actions">'+
        '<button class="act k" data-copy="title" data-id="'+g.id+'">Copy title</button>'+
        '<button class="act k" data-copy="desc" data-id="'+g.id+'">Copy description</button>'+
        '<button class="act k" data-copy="tags" data-id="'+g.id+'">Copy tags</button>'+
        '<button class="act" data-copy="all" data-id="'+g.id+'">Copy all</button>'+
        '<button class="act" data-png="'+g.id+'">Download PNG</button>'+
      '</div>'+
    '</div>';
  return el;
}

function fieldText(g, which){
  if(which==='title') return g.title;
  if(which==='tags') return g.tags.join(', ');
  if(which==='desc') return g.desc;
  return 'TITLE: '+g.title+'\nCATEGORY: '+g.cat+'\nTAGS: '+g.tags.join(', ')+
    '\nCOMPETITION: '+g.competition+'\n\nDESCRIPTION:\n'+g.desc+
    '\n\nPRICING:\n'+['basic','standard','premium'].map(k=>{
      const t=g.pricing[k];return '- '+t.name+' $'+t.price+' ('+t.del+', '+t.rev+' rev): '+(t.items||[]).join(' | ');
    }).join('\n')+'\n\n'+g.xsell;
}

function render(){
  const root = document.getElementById('root');
  let lastPhase = null;
  GIGS.forEach(g=>{
    if(g.phase !== lastPhase){
      lastPhase = g.phase;
      const st = document.createElement('div');
      st.className = 'section-title';
      st.innerHTML = '<span class="ln"></span><span>'+(PHASE_LABEL[g.phase]||('Phase '+g.phase))+
        '</span><span class="ln"></span>';
      root.appendChild(st);
    }
    root.appendChild(gigCard(g));
  });
  GIGS.forEach(g=>{const cv=document.getElementById('thumb'+g.id);if(cv)paintThumb(cv,g);});
}

document.addEventListener('click', e=>{
  const t = e.target;
  if(t.dataset.copy){const g=GIGS.find(x=>x.id==t.dataset.id);copy(fieldText(g,t.dataset.copy),t.dataset.copy);}
  if(t.dataset.png){const cv=document.getElementById('thumb'+t.dataset.png);
    const a=document.createElement('a');a.download='gig-'+t.dataset.png+'-thumbnail.png';
    a.href=cv.toDataURL('image/png');a.click();}
  if(t.dataset.t){const d=document.getElementById('desc'+t.dataset.t);d.classList.toggle('open');
    t.textContent=d.classList.contains('open')?'Show less':'Show more';}
});
document.getElementById('copyAll').onclick=()=>{
  copy(GIGS.map(g=>fieldText(g,'all')).join('\n\n----------\n\n'),'all gigs');
};
document.getElementById('dlAll').onclick=()=>{
  GIGS.forEach((g,i)=>setTimeout(()=>{const cv=document.getElementById('thumb'+g.id);
    const a=document.createElement('a');a.download='gig-'+g.id+'-thumbnail.png';
    a.href=cv.toDataURL('image/png');a.click();}, i*250));
};

if(PHOTO){portrait.onload=render; portrait.onerror=render;} else {render();}
"""


def build_html(config, photo):
    seller = config.get("seller", {})
    strategy = config.get("strategy", {})
    gigs = config.get("gigs", [])

    counts = [sum(1 for g in gigs if g.get("phase") == p) for p in (1, 2, 3)]
    brand = seller.get("brand") or seller.get("name", "")
    website = seller.get("website", "")
    watermark = brand + (f"  |  {website}" if website else "")
    target = strategy.get("monthlyTarget", "")

    chips = "".join(
        f'<span class="chip">Phase {p}: {n} gig(s)</span>'
        for p, n in enumerate(counts, 1) if n
    ) + '<span class="chip">Research-backed</span>'

    stats = f'<div class="stat"><b>{len(gigs)}</b><span>Total gigs</span></div>'
    for p, n in enumerate(counts, 1):
        if n:
            stats += f'<div class="stat"><b>{n}</b><span>Phase {p}</span></div>'
    if target:
        stats += f'<div class="stat"><b>{target}</b><span>Monthly target</span></div>'

    plan_items = "".join(f"<li>{s}</li>" for s in action_plan(counts))

    js = (RENDER_JS
          .replace("__GIGS__", json.dumps(gigs, ensure_ascii=False))
          .replace("__PHOTO__", json.dumps(photo))
          .replace("__MARK__", json.dumps(watermark)))

    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Fiverr Catalog — {brand}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>{PAGE_CSS}</style></head>
<body>
<header><div class="wrap">
  <div class="badges">{chips}</div>
  <h1>Fiverr <span class="a">Gig</span> <span class="b">Catalog</span></h1>
  <p class="sub">Combo-niche gigs on low-competition keywords, rolled out in phases,
     each one cross-selling into the next.</p>
  <div class="stats">{stats}</div>
  <div class="funnel"><h3>Cross-sell funnel</h3><pre>{funnel_text(gigs)}</pre></div>
</div></header>

<div class="wrap">
  <div class="toolbar">
    <button class="tbtn" onclick="window.print()">Print / Save PDF</button>
    <button class="tbtn alt" id="dlAll">Download all thumbnails</button>
    <button class="tbtn ghost" id="copyAll">Copy all gigs</button>
  </div>
  <div id="root"></div>
  <div class="plan"><h3>Immediate action plan</h3><ol>{plan_items}</ol></div>
</div>

<footer>Generated by the fiverr-gig-optimizer skill &middot; {brand}</footer>
<div class="toast" id="toast"></div>
<script>{js}</script>
</body></html>"""


def main():
    ap = argparse.ArgumentParser(description="Build an HTML gig catalog from gig-config.json")
    ap.add_argument("config", nargs="?", default="gig-config.json", help="path to gig-config.json")
    ap.add_argument("--no-photo", action="store_true", help="skip embedding the seller photo")
    ap.add_argument("--out", default=None, help="output HTML path (default: alongside the config)")
    args = ap.parse_args()

    if not os.path.isfile(args.config):
        print(f"ERROR: {args.config} not found.")
        print("Generate it with the fiverr-gig-optimizer skill, or copy "
              "references/config-example.json and edit it.")
        return 1

    with open(args.config, encoding="utf-8") as fh:
        config = json.load(fh)
    if not config.get("gigs"):
        print("ERROR: config has no gigs.")
        return 1

    config_dir = os.path.dirname(os.path.abspath(args.config))
    photo = load_photo(config.get("seller", {}), config_dir, args.no_photo)

    out = args.out or os.path.join(config_dir, "fiverr-catalog.html")
    html = build_html(config, photo)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(html)

    counts = [sum(1 for g in config["gigs"] if g.get("phase") == p) for p in (1, 2, 3)]
    print(f"Wrote {out} ({len(html) // 1024} KB)")
    print(f"  {len(config['gigs'])} gigs — "
          f"{counts[0]} Phase 1, {counts[1]} Phase 2, {counts[2]} Phase 3")
    print("  Open it in a browser to review thumbnails and copy gig fields.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
