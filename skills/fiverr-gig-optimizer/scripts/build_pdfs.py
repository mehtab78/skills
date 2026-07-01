#!/usr/bin/env python3
"""
build_pdfs.py — render one print-ready PDF per gig from gig-config.json.

For each gig it builds a standalone HTML sheet (a cover page plus a content page
with the title, tags, description, three pricing tiers, and any FAQs) and drives
a headless Chromium browser with --print-to-pdf to produce the PDF.

Requires Google Chrome, Chromium, or Microsoft Edge (auto-detected; override with
--chrome PATH). If no such browser is installed, skip this step — the HTML
catalog from build_catalog.py is the essential artifact.

Usage:
    python build_pdfs.py
    python build_pdfs.py --config gig-config.json --out pdfs
    python build_pdfs.py --chrome "/path/to/chrome" --keep-html
"""
import argparse
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def find_browser():
    """Locate a Chromium-family binary, or return None."""
    for name in ("google-chrome", "google-chrome-stable", "chromium",
                 "chromium-browser", "microsoft-edge", "msedge"):
        found = shutil.which(name)
        if found:
            return found
    guesses = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    ]
    return next((p for p in guesses if os.path.isfile(p)), None)


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-")[:60] or "gig"


def e(text):
    return html.escape(str(text) if text is not None else "")


def desc_to_html(desc):
    """Render the plain-text description as paragraphs, bullet blocks -> <ul>."""
    blocks = []
    for para in [p.strip() for p in (desc or "").split("\n\n") if p.strip()]:
        rows = [r for r in para.split("\n") if r.strip()]
        if rows and all(re.match(r"^[•➔>\-\*]\s+", r) for r in rows):
            items = "".join(f"<li>{e(re.sub(r'^[^ ]+ +', '', r))}</li>" for r in rows)
            blocks.append(f"<ul>{items}</ul>")
        else:
            blocks.append("<p>" + e(para).replace("\n", "<br>") + "</p>")
    return "\n".join(blocks)


SHEET_CSS = """
@page { size: A4; margin: 15mm 15mm 16mm; }
@page :first { margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; background: #faf7f2; }
body { color: #1b1b1f; font-family: 'Inter', system-ui, sans-serif;
       font-size: 10.5pt; line-height: 1.55; }

.cover { page-break-after: always; width: 210mm; height: 297mm; padding: 30mm 24mm;
  color: #fff; display: flex; flex-direction: column; justify-content: space-between;
  background: linear-gradient(140deg, #1c0b28 0%, #35114b 55%, #5a1a74 100%); position: relative; }
.cover::after { content: ""; position: absolute; inset: 0;
  background: radial-gradient(circle at 78% 26%, rgba(232,121,249,.28), transparent 58%); }
.cover > * { position: relative; z-index: 1; }
.c-top { display: flex; justify-content: space-between; align-items: baseline; }
.c-brand { font-weight: 800; font-size: 13pt; color: #e879f9; letter-spacing: .5px; }
.c-kicker { font-size: 8pt; letter-spacing: 2px; text-transform: uppercase; color: rgba(255,255,255,.55); }
.c-no { font-size: 88pt; font-weight: 800; line-height: .8; color: rgba(232,121,249,.20); letter-spacing: -3px; }
.c-pill { display: inline-block; margin: 6mm 0 8mm; padding: 5px 13px; border: 1px solid rgba(232,121,249,.6);
  border-radius: 40px; color: #e879f9; font-size: 8.5pt; font-weight: 700; letter-spacing: 1.4px; text-transform: uppercase; }
.c-title { font-size: 30pt; font-weight: 800; line-height: 1.1; margin: 0 0 8mm; max-width: 150mm; }
.c-rule { width: 56mm; height: 3px; background: #e879f9; margin-bottom: 6mm; }
.c-intro { font-size: 11pt; color: rgba(255,255,255,.8); max-width: 145mm; }
.c-foot { display: flex; justify-content: space-between; align-items: flex-end;
  border-top: 1px solid rgba(255,255,255,.15); padding-top: 8mm; }
.c-author { font-weight: 700; font-size: 12pt; }
.c-author small { display: block; font-weight: 400; font-size: 8.5pt; letter-spacing: 1px;
  text-transform: uppercase; color: rgba(255,255,255,.55); margin-top: 3px; }
.c-url { font-size: 9pt; color: rgba(255,255,255,.6); }

.row { page-break-inside: avoid; margin-bottom: 7mm; }
.lbl { font-weight: 700; color: #6d1f8c; font-size: 8.5pt; letter-spacing: 1.8px; text-transform: uppercase;
  border-bottom: 1px solid rgba(109,31,140,.18); padding-bottom: 2mm; margin-bottom: 3mm; }
.val p { margin: 0 0 2mm; } .val ul { margin: 2mm 0; padding-left: 5mm; } .val li { margin-bottom: 1mm; }
.tags { display: flex; flex-wrap: wrap; gap: 2mm; }
.tag { background: #efe6db; color: #6d1f8c; font-size: 9pt; font-weight: 600; padding: 3px 10px; border-radius: 40px; }

.tiers { display: grid; grid-template-columns: repeat(3, 1fr); gap: 5mm; }
.tier { background: #fff; border: 1px solid rgba(0,0,0,.1); border-radius: 5px; padding: 6mm 5mm; position: relative; }
.tier.mid { background: #1c0b28; color: #fff; }
.tier.mid::before { content: "RECOMMENDED"; position: absolute; top: -8px; left: 50%; transform: translateX(-50%);
  background: #e879f9; color: #fff; font-size: 6.5pt; font-weight: 700; letter-spacing: 1.2px; padding: 3px 9px; border-radius: 40px; }
.t-name { font-size: 8pt; font-weight: 700; letter-spacing: 1.6px; text-transform: uppercase; color: #9a7b52; }
.tier.mid .t-name { color: #e879f9; }
.t-title { font-weight: 700; font-size: 11pt; margin: 2mm 0; }
.t-price { font-size: 18pt; font-weight: 800; color: #6d1f8c; }
.tier.mid .t-price { color: #e879f9; }
.t-meta { font-size: 8.5pt; color: #9a7b52; margin-bottom: 3mm; }
.tier.mid .t-meta { color: rgba(255,255,255,.6); }
.tier ul { margin: 0; padding-left: 4mm; font-size: 9pt; color: #555; }
.tier.mid ul { color: rgba(255,255,255,.8); }

.faq { background: #fff; border-left: 3px solid #e879f9; border-radius: 0 4px 4px 0; padding: 4mm 5mm;
  margin-bottom: 3mm; page-break-inside: avoid; }
.faq-q { font-weight: 700; color: #1c0b28; margin-bottom: 1.5mm; }
.faq-a { font-size: 10pt; color: #3a3a3a; }
.foot-note { margin-top: 10mm; padding-top: 4mm; border-top: 1px solid rgba(0,0,0,.08);
  text-align: center; font-size: 8pt; letter-spacing: 1.5px; text-transform: uppercase; color: #9a7b52; }
"""


def cover_html(gig, seller):
    title = re.sub(r"^\s*i will\s+", "", gig.get("title", ""), flags=re.I).strip()
    title = title[:1].upper() + title[1:] if title else gig.get("title", "")
    intro = (gig.get("img", {}).get("pdfWhat")
             or gig.get("desc", "").split("\n\n")[0]).strip()
    if len(intro) > 280:
        intro = intro[:277].rsplit(" ", 1)[0] + "..."
    phase = gig.get("phase", 1)
    pill = {1: "Phase 1 - Launch now", 2: "Phase 2 - After 5 reviews",
            3: "Phase 3 - After Level 2"}.get(phase, f"Phase {phase}")
    brand = seller.get("brand") or seller.get("name", "")
    return f"""<div class="cover">
  <div class="c-top"><div class="c-brand">{e(brand)}</div>
    <div class="c-kicker">Fiverr Gig Sheet</div></div>
  <div>
    <div class="c-no">#{gig.get('id', 0):02d}</div>
    <div class="c-pill">{e(pill)}</div>
    <h1 class="c-title">{e(title)}</h1>
    <div class="c-rule"></div>
    <p class="c-intro">{e(intro)}</p>
  </div>
  <div class="c-foot">
    <div class="c-author">{e(seller.get('name', ''))}<small>{e(brand)}</small></div>
    <div class="c-url">{e(seller.get('website', ''))}</div>
  </div>
</div>"""


def tiers_html(pricing):
    order = [("basic", "", "Basic"), ("standard", "mid", "Standard"),
             ("premium", "", "Premium")]
    cards = []
    for key, cls, name in order:
        t = pricing.get(key, {})
        items = "".join(f"<li>{e(i)}</li>" for i in t.get("items", []))
        cards.append(
            f'<div class="tier {cls}"><div class="t-name">{name}</div>'
            f'<div class="t-title">{e(t.get("title") or t.get("name", ""))}</div>'
            f'<div class="t-price">${e(t.get("price", ""))}</div>'
            f'<div class="t-meta">{e(t.get("del", ""))} &middot; {e(t.get("rev", ""))} revisions</div>'
            f'<ul>{items}</ul></div>')
    return '<div class="tiers">' + "".join(cards) + "</div>"


def faqs_html(faqs):
    if not faqs:
        return ""
    blocks = "".join(
        f'<div class="faq"><div class="faq-q">{e(f.get("q", ""))}</div>'
        f'<div class="faq-a">{e(f.get("a", ""))}</div></div>'
        for f in faqs)
    return f'<div class="row"><div class="lbl">FAQ</div>{blocks}</div>'


def sheet_html(gig, seller):
    tags = "".join(f'<span class="tag">{e(t)}</span>' for t in gig.get("tags", []))
    footer = " · ".join(x for x in (seller.get("brand"), seller.get("website")) if x)
    return f"""<!doctype html><html><head><meta charset="utf-8">
<title>Gig #{gig.get('id', 0)} — {e(gig.get('title', ''))}</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>{SHEET_CSS}</style></head><body>
{cover_html(gig, seller)}
<div class="row"><div class="lbl">Gig title</div><div class="val"><p>{e(gig.get('title', ''))}</p></div></div>
<div class="row"><div class="lbl">Category</div><div class="val"><p>{e(gig.get('cat', ''))}</p></div></div>
<div class="row"><div class="lbl">Tags ({len(gig.get('tags', []))}/5)</div><div class="val"><div class="tags">{tags}</div></div></div>
<div class="row"><div class="lbl">Description ({len(gig.get('desc', ''))}/1200)</div><div class="val">{desc_to_html(gig.get('desc', ''))}</div></div>
<div class="row"><div class="lbl">Pricing</div>{tiers_html(gig.get('pricing', {}))}</div>
{faqs_html(gig.get('faqs', []))}
<div class="row"><div class="lbl">Cross-sell</div><div class="val"><p>{e(gig.get('xsell', ''))}</p></div></div>
<div class="row"><div class="lbl">Competition</div><div class="val"><p>{e(gig.get('competition', ''))}</p></div></div>
<div class="foot-note">{e(footer)}</div>
</body></html>"""


def render_pdf(browser, html_path, pdf_path, profile_dir):
    cmd = [
        browser, "--headless", "--disable-gpu", "--no-sandbox",
        f"--user-data-dir={profile_dir}",
        "--no-pdf-header-footer",
        "--virtual-time-budget=3000",
        f"--print-to-pdf={pdf_path.resolve()}",
        html_path.resolve().as_uri(),
    ]
    try:
        proc = subprocess.run(cmd, capture_output=True, timeout=90)
    except subprocess.TimeoutExpired:
        print("    timed out")
        return False
    ok = pdf_path.exists() and pdf_path.stat().st_size > 1000
    if not ok:
        err = (proc.stderr or b"").decode("utf-8", "replace")[:400].strip()
        if err:
            print(f"    browser: {err}")
    return ok


def main():
    ap = argparse.ArgumentParser(description="Render per-gig PDFs from gig-config.json")
    ap.add_argument("--config", default="gig-config.json", help="path to gig-config.json")
    ap.add_argument("--out", default="pdfs", help="output directory")
    ap.add_argument("--chrome", default=None, help="path to a Chromium/Edge binary")
    ap.add_argument("--keep-html", action="store_true", help="keep the intermediate HTML")
    args = ap.parse_args()

    cfg_path = Path(args.config)
    if not cfg_path.is_file():
        print(f"ERROR: {cfg_path} not found.")
        print("Generate it with the fiverr-gig-optimizer skill first.")
        return 1

    browser = args.chrome or find_browser()
    if not browser:
        print("ERROR: no Chrome/Chromium/Edge found. Pass --chrome PATH, or skip "
              "PDFs — the HTML catalog is the essential output.")
        return 1
    print(f"Using browser: {browser}")

    config = json.loads(cfg_path.read_text(encoding="utf-8"))
    seller = config.get("seller", {})
    gigs = config.get("gigs", [])
    if not gigs:
        print("ERROR: config has no gigs.")
        return 1

    out_dir = Path(args.out)
    html_dir = out_dir / "_html"
    html_dir.mkdir(parents=True, exist_ok=True)
    profile_dir = Path(tempfile.mkdtemp(prefix="fiverr-pdf-"))

    built = 0
    for gig in gigs:
        gid = gig.get("id", built + 1)
        base = f"gig-{gid:02d}-{slug(gig.get('title', ''))}"
        html_path = html_dir / f"{base}.html"
        pdf_path = out_dir / f"{base}.pdf"
        html_path.write_text(sheet_html(gig, seller), encoding="utf-8")
        if render_pdf(browser, html_path, pdf_path, profile_dir):
            size = pdf_path.stat().st_size // 1024
            print(f"  gig {gid:02d}: OK   {pdf_path.name} ({size} KB)")
            built += 1
        else:
            print(f"  gig {gid:02d}: FAIL {pdf_path.name}")

    shutil.rmtree(profile_dir, ignore_errors=True)
    if not args.keep_html:
        shutil.rmtree(html_dir, ignore_errors=True)

    print(f"\n{built}/{len(gigs)} PDFs written to {out_dir.resolve()}")
    return 0 if built == len(gigs) else 1


if __name__ == "__main__":
    sys.exit(main())
