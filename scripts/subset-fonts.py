"""Subset the brand fonts into WOFF2 for the website.

Source of truth for the font binaries: ../services/assets/fonts/ (brand copy).
Output: assets/fonts/*.woff2.  Run via the project venv:

    .venv\\Scripts\\python.exe scripts\\subset-fonts.py

Fonts:
  - Source Sans 3 (body / UI / SVG) — ONE variable WOFF2, wght axis limited to
    300-800. Humanist sans that pairs with the Newsreader serif. Source:
    github.com/google/fonts (OFL).
  - Newsreader (headlines H1/H2 only) — ONE variable WOFF2 keeping the wght
    axis, opsz pinned to display. Source: github.com/google/fonts (OFL).
  - Atkinson Hyperlegible (body READING text only — paragraphs/prose) — two static
    WOFF2 (400 + 700; Braille Institute, OFL). Max-legibility face for the older
    audience; UI / labels / headings stay Source Sans 3 / Newsreader.
  - Poppins — retired from the live pages; still subset here ONLY because the
    og-image / touch-icon generators in assets/og/ reference the WOFF2.
"""
from pathlib import Path

from fontTools.subset import main as subset_main

ROOT = Path(__file__).resolve().parents[1]            # brand/website
SRC = ROOT.parent / "services" / "assets" / "fonts"   # brand-owned TTFs
OUT = ROOT / "assets" / "fonts"

# Basic Latin + Latin-1 (covers the middot) + general punctuation
# (en/em dashes, curly quotes, bullet, ellipsis) + euro + minus.
UNICODES = "U+0020-007E,U+00A0-00FF,U+2010-2027,U+2030-203A,U+20AC,U+2212"

# Static faces, subset 1:1 (no axis instancing). Poppins is retired (kept only for the
# assets/og/ generators). Atkinson Hyperlegible (400/700) is the body READING face —
# a max-legibility sans for the older audience, scoped to prose in css/styles.css.
FACES = ["Poppins-Light", "Poppins-Regular", "Poppins-Medium", "Poppins-SemiBold", "Poppins-Bold", "Poppins-ExtraBold",
         "AtkinsonHyperlegible-Regular", "AtkinsonHyperlegible-Bold"]

OUT.mkdir(parents=True, exist_ok=True)
for face in FACES:
    src = SRC / f"{face}.ttf"
    out = OUT / f"{face}.woff2"
    subset_main([
        str(src),
        f"--output-file={out}",
        "--flavor=woff2",
        f"--unicodes={UNICODES}",
        "--layout-features=kern,liga",
        "--no-hinting",
    ])
    print(f"{out.name}: {src.stat().st_size // 1024} KB -> {out.stat().st_size // 1024} KB")

# Newsreader — variable serif for headlines (H1/H2). Pin opsz to the display
# optical size (72) and limit wght to the headline range (400-700); one WOFF2
# then covers every headline weight we use, with no opsz axis to set in CSS.
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

nsrc = SRC / "Newsreader[opsz,wght].ttf"
ntmp = OUT / "_newsreader_inst.ttf"
nout = OUT / "Newsreader.woff2"
_nf = TTFont(str(nsrc))
instantiateVariableFont(_nf, {"opsz": 72, "wght": (400, 700)}, inplace=True)
_nf.save(str(ntmp))
subset_main([
    str(ntmp),
    f"--output-file={nout}",
    "--flavor=woff2",
    f"--unicodes={UNICODES}",
    "--layout-features=kern,liga",
    "--no-hinting",
])
ntmp.unlink()
print(f"{nout.name}: {nsrc.stat().st_size // 1024} KB -> {nout.stat().st_size // 1024} KB")

# Source Sans 3 — variable humanist sans for body/UI. Limit wght to 300-800.
ssrc = SRC / "SourceSans3[wght].ttf"
stmp = OUT / "_sourcesans_inst.ttf"
sout = OUT / "SourceSans3.woff2"
_sf = TTFont(str(ssrc))
instantiateVariableFont(_sf, {"wght": (300, 800)}, inplace=True)
_sf.save(str(stmp))
subset_main([
    str(stmp),
    f"--output-file={sout}",
    "--flavor=woff2",
    f"--unicodes={UNICODES}",
    "--layout-features=kern,liga",
    "--no-hinting",
])
stmp.unlink()
print(f"{sout.name}: {ssrc.stat().st_size // 1024} KB -> {sout.stat().st_size // 1024} KB")
