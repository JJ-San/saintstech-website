"""Prepare the web image assets from their canonical sources.

  Logo : ../logo/stas-logo.jpg (brand-owned)         -> assets/img/stas-logo.png
         white background keyed to transparent + trimmed, so it sits cleanly on
         the translucent nav and the white footer with no visible box.
  Photo: applications/cvkit/assets/photo.jpg (the CV headshot) -> assets/img/josiah.jpg
         re-encoded as an optimized, progressive JPEG.

Run via the project venv:  .venv\\Scripts\\python.exe scripts\\prep-images.py
"""
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]    # brand/website
BRAND = ROOT.parent                           # brand
STAS = BRAND.parent                           # repo root
OUT = ROOT / "assets" / "img"
OUT.mkdir(parents=True, exist_ok=True)

LOGO_SRC = BRAND / "logo" / "stas-logo.jpg"
PHOTO_SRC = STAS / "applications" / "cvkit" / "assets" / "photo.jpg"

# ---- Logo -> trimmed, transparent PNG ----------------------------------------
logo = Image.open(LOGO_SRC).convert("RGBA")
w, h = logo.size
# Flood-fill the exterior white from every edge seed (connectivity-bound, so it
# never eats the teal swoosh highlights inside the mark).
for seed in [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1),
             (w // 2, 0), (w // 2, h - 1), (0, h // 2), (w - 1, h // 2)]:
    ImageDraw.floodfill(logo, seed, (0, 0, 0, 0), thresh=80)
# Clear any fully-enclosed pure white (the counter inside the 'A').
px = logo.load()
for y in range(h):
    for x in range(w):
        r, g, b, a = px[x, y]
        if a and r >= 250 and g >= 250 and b >= 250:
            px[x, y] = (0, 0, 0, 0)
logo = logo.crop(logo.getbbox())
target_w = 360
logo = logo.resize((target_w, round(logo.height * target_w / logo.width)), Image.LANCZOS)
logo.save(OUT / "stas-logo.png", optimize=True)
print(f"stas-logo.png: {logo.size}  {(OUT / 'stas-logo.png').stat().st_size // 1024} KB")

# ---- Photo -> optimized web JPEG ---------------------------------------------
photo = Image.open(PHOTO_SRC).convert("RGB")
photo.save(OUT / "josiah.jpg", quality=82, optimize=True, progressive=True)
print(f"josiah.jpg: {photo.size}  {(OUT / 'josiah.jpg').stat().st_size // 1024} KB")
