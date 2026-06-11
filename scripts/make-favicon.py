"""Generate assets/img/favicon.svg.

Navy rounded square with the teal top edge (the service-card motif) and the
real Poppins-Bold 'S' outline extracted as an SVG path — so the favicon is
genuinely set in the brand face, not a lookalike.  Run via the project venv:

    .venv\\Scripts\\python.exe scripts\\make-favicon.py
"""
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT.parent / "services" / "assets" / "fonts" / "Poppins-Bold.ttf"
OUT = ROOT / "assets" / "img" / "favicon.svg"

font = TTFont(str(SRC))
glyph_set = font.getGlyphSet()
glyph_name = font.getBestCmap()[ord("S")]
glyph = glyph_set[glyph_name]
pen = SVGPathPen(glyph_set)
glyph.draw(pen)
path = pen.getCommands()

upm = font["head"].unitsPerEm
cap = getattr(font["OS/2"], "sCapHeight", 0) or int(upm * 0.7)
adv = glyph.width

SIZE = 100
TARGET_CAP = 52                      # cap height in viewBox units
s = TARGET_CAP / cap
tx = (SIZE - adv * s) / 2
ty = (SIZE + TARGET_CAP) / 2         # baseline; scale(s,-s) flips the y-up glyph

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SIZE} {SIZE}">
  <defs><clipPath id="r"><rect width="{SIZE}" height="{SIZE}" rx="20"/></clipPath></defs>
  <g clip-path="url(#r)">
    <rect width="{SIZE}" height="{SIZE}" fill="#2F3B49"/>
    <rect width="{SIZE}" height="7" fill="#3E9DAE"/>
  </g>
  <g transform="translate({tx:.2f},{ty:.2f}) scale({s:.6f},-{s:.6f})">
    <path d="{path}" fill="#F8F9FA"/>
  </g>
</svg>
"""
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(svg, encoding="utf-8")
print(f"wrote {OUT}  (upm={upm}, cap={cap}, adv={adv})")
