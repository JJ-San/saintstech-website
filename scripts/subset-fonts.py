"""Subset the brand-owned Poppins TTFs into WOFF2 for the website.

Source of truth for the font binaries: ../services/assets/fonts/ (brand copy).
Output: assets/fonts/*.woff2.  Run via the project venv:

    .venv\\Scripts\\python.exe scripts\\subset-fonts.py
"""
from pathlib import Path

from fontTools.subset import main as subset_main

ROOT = Path(__file__).resolve().parents[1]            # brand/website
SRC = ROOT.parent / "services" / "assets" / "fonts"   # brand-owned TTFs
OUT = ROOT / "assets" / "fonts"

# Basic Latin + Latin-1 (covers the middot) + general punctuation
# (en/em dashes, curly quotes, bullet, ellipsis) + euro + minus.
UNICODES = "U+0020-007E,U+00A0-00FF,U+2010-2027,U+2030-203A,U+20AC,U+2212"

FACES = ["Poppins-Light", "Poppins-Regular", "Poppins-Medium", "Poppins-Bold"]

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
