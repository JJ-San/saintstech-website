# brand/website — saintstech.co.nz

Static two-page site (Home + About) for Saints Technologies & Services. This is **render target #3** of the content master `../services/services.md` — same one-way rule as the one-pager: master → render, never the reverse. Full sync flow: `../services/README.md`.

> **Resuming work?** Read `.claude/sessions/handoff.md` for current status, open items, and next steps.

## Rules

- **NEVER edit page copy in the HTML directly.** Edit `../services/services.md` (including its `Website-only content` section), then sync ("sync the services sheet"). Design/CSS polish directly in the HTML/CSS is fine.
- Brand tokens: Poppins (Light 300 / Regular 400 / Medium 500 / Bold 700) · navy `#2F3B49` · teal `#3E9DAE` · **accent-deep `#2E7785`** (web-only token: brand teal is 3.0:1 on white, so small text/CTAs use accent-deep at ≥4.5:1; bright teal is for borders, bullets, large accents, and accents on navy) · accent-soft `#EAF4F6`.
- **Zero JavaScript.** Scroll reveals are CSS `animation-timeline` behind `@supports`, with a `prefers-reduced-motion` opt-out. Keep it that way unless a recorded decision says otherwise.
- The testimonial section in `index.html` ships **commented out**. Activate only with a real client quote (name + specific result). Never placeholder praise.
- The nav/footer logo and the About portrait are **live**. Never hand-edit the generated `assets/img/stas-logo.png` / `josiah.jpg` — regenerate them with `scripts\prep-images.py` (see Rituals).

## Rituals

- **Fonts**: brand-owned TTFs live in `../services/assets/fonts/`. Re-subset → WOFF2: `.venv\Scripts\python.exe scripts\subset-fonts.py`
- **Logo / photo**: canonical logo at `../logo/stas-logo.jpg`. Re-prep web assets: `.venv\Scripts\python.exe scripts\prep-images.py` → `assets/img/stas-logo.png` (white keyed to transparent) + `assets/img/josiah.jpg` (headshot). Nav logo vertical alignment knob: `--logo-nudge` in `css/styles.css`.
- **og-image / touch icon**: edit `assets/og/og.html` (or `assets/og/icon.html`), then `pwsh scripts\render-og.ps1` (headless Edge screenshots).
- **Proof rule (from cvkit)**: after any visual change, screenshot at 390 / 768 / 1440 and *look at it* — overlap and overflow don't show up in code.

## Deploy

- GitHub Pages, repo **github.com/JJ-San/saintstech-website** (`main`, root). `CNAME` = saintstech.co.nz. **Deploy = commit + `git push`.**
- **After deploy, hard-refresh (Ctrl+Shift+R)** — GitHub's CDN + browser cache serve the old CSS otherwise.
- DNS at Freeparking (`dnspackage.com`): apex `@` → GitHub IPs `185.199.108–111.153`; `www` → `185.199.108.153`.
- **NEVER touch the domain's MX / SPF / autodiscover / `MS=` TXT records** — company email (Microsoft 365) lives on this domain.
- HTTPS / Enforce-HTTPS state and the cert-unstick steps: see `.claude/sessions/handoff.md`.

## Validation

Manual proof rule above · W3C-valid HTML · Lighthouse ≥95 target · contrast: all small text ≥4.5:1.
