# Session handoff — saintstech.co.nz website

_Updated 2026-06-11. Blueprint for the next session. Durable "how to work" rules live in this folder's `CLAUDE.md`; this file is current state + what's left._

## Status: LIVE over HTTPS — https://saintstech.co.nz
- Repo **github.com/JJ-San/saintstech-website** (public) · deploy = commit + `git push` (GitHub Pages, `main`, root).
- Two pages: `index.html` (Home) + `about/index.html` (About). Hand-coded HTML/CSS, **zero JS**.

## Done this session
- Built Home + About from the content master; brand design system (Poppins WOFF2 subset, navy/teal, a11y `--accent-deep`, CSS scroll-reveals).
- Logo + motto + founder photo added. Nav = logo + **SAINTS TECHNOLOGIES & SERVICES** lockup (full caps, optical lift `--logo-nudge: -10%`), shown ≥1025px, mark-only below.
- Deployed to GitHub Pages; DNS cut over at Freeparking with **email left intact**.
- **HTTPS resolved (2026-06-11):** cert sat stuck `null` for hours; a custom-domain off/on toggle (Settings → Pages) unstuck it → cert **approved**, **Enforce HTTPS enabled**, `http→https` 301 verified.

## Open / next steps
1. **DNS cleanup (minor, optional).** `www` is still an **A** record → GitHub flags `InvalidARecordError`. In the Freeparking panel, change `www` from A `185.199.108.153` to a **CNAME → jj-san.github.io** so `www.saintstech.co.nz` is also covered by HTTPS. The apex (canonical) is fully live over HTTPS — this only affects the `www.` variant.
2. **Josiah to review website-only copy** in `../services/services.md` → `## Website-only content` (bio, "how I work", response-time promise, meta). Drafted, awaiting his edits → then re-sync.
3. **Motto capitalisation** — kept verbatim ("Increasing Business Productivity through intelligent automation"). Confirm or switch to sentence/Title case.
4. **Testimonial** — commented-out block in `index.html`; activate when a real client quote (name + result) lands.

## Backlog (not started)
NZBN in footer (comment slot already in footer HTML) · analytics (GoatCounter / Cloudflare-free) · Google Business Profile (ops) · `/work` case-study page once one exists · feature the motto more prominently if wanted · OG card could gain the logo.

## Key context / gotchas
- **Content master** = `../services/services.md` (incl. `## Website-only content`). Site is render target #3 — edit master then "sync the services sheet"; never edit page copy directly. Sync flow: `../services/README.md`.
- **DNS** (Freeparking): apex `@` → four GitHub IPs `185.199.108–111.153`; `www` → `185.199.108.153`. **Never touch MX / SPF / autodiscover / `MS=` TXT — that's the M365 email.**
- **Assets**: canonical logo `../logo/stas-logo.jpg` → `scripts\prep-images.py` → `assets/img/stas-logo.png` (white keyed transparent) + `assets/img/josiah.jpg` (headshot, sourced from `applications/cvkit/assets/photo.jpg`). Fonts: `scripts\subset-fonts.py`.
- **Iterating visuals**: serve locally (`.venv\Scripts\python.exe -m http.server 8080 --directory .`), screenshot via Playwright (proof rule), deploy. **After each deploy, hard-refresh (Ctrl+Shift+R)** — GitHub's CDN + browser cache serve old CSS otherwise.
