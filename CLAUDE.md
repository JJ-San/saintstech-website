# brand/website — saintstech.co.nz

Single-page site for Saints Technologies & Services. This is **render target #3** of the content master `../services/services.md` — same one-way rule as the one-pager: master → render, never the reverse. Full sync flow: `../services/README.md`.

The redesign collapsed the old two-page layout (Home + About) into one document at `/`. `about/index.html` is retained as a redirect (`/about/` → `/#about`) so inbound links and indexed URLs keep working.

> **Resuming work?** Read `.claude/sessions/handoff.md` for current status, open items, and next steps.

## Rules

- **NEVER edit page copy in the HTML directly.** Edit `../services/services.md` (including its `Website-only content` section), then sync ("sync the services sheet"). Design/CSS polish directly in the HTML/CSS is fine.
- Brand tokens — **type:** **Newsreader** (variable serif) for **headlines** (`.display` H1 + `h2`, plus the calculator verdict title; opsz baked to display, weight 400–700; self-hosted single WOFF2); **Source Sans 3** (variable humanist sans, self-hosted single WOFF2, weight 300–800) for **everything else** — body, eyebrows, buttons, nav, `h3`/`h4`, SVG labels (600 nav links, 800 nav wordmark). Pairs with Newsreader as a family (chosen 2026-06-16 over Poppins for cohesion + legibility). Poppins is **retired** from the live pages — kept only because `assets/og/` generators reference its WOFF2. Body type scale bumped for an older audience. **colour:** navy `#2F3B49` · teal `#3E9DAE` · **accent-deep `#2E7785`** (web-only token: brand teal is 3.0:1 on white, so small text/CTAs use accent-deep at ≥4.5:1; bright teal is for borders, bullets, large accents, and accents on navy) · accent-soft `#EAF4F6` · **paper-cream `#F7F2E7`** (the calculator "worksheet" surface).
- **JavaScript is a progressive enhancement, not a requirement.** `js/main.js` handles scroll reveals (IntersectionObserver), the hero tool rotator, the ROI calculator, and the sticky mobile CTA. The page must still read sensibly without JS (calculator has a `<noscript>` fallback; rotator falls back to a comma-separated list under `prefers-reduced-motion`). Hero load-in is plain CSS keyframes (`.lift` + `liftIn`) so it works on every browser including Safari/iOS.
- The testimonial section in `index.html` ships **commented out**. Activate only with a real client quote (name + specific result). Never placeholder praise.
- The nav brand mark and the About portrait are **live**. Never hand-edit `assets/img/stas-logo.png` / `josiah.jpg` — regenerate them with `scripts\prep-images.py` (see Rituals).
- **Don't add third-party brand logos** (Xero, MYOB, Microsoft 365, etc.) to the site without a policy check. 2026-06-15 research: Xero restricts logos to certified partners; MYOB explicitly forbids non-Developer-Partner use; Microsoft requires an express licence for logos but explicitly permits text wordmarks. Text mentions + the footer trademark notice are the cleared path. Revisit only if STAS joins the relevant partner program.

## Rituals

- **Fonts**: brand-owned TTFs live in `../services/assets/fonts/`. Re-subset → WOFF2: `.venv\Scripts\python.exe scripts\subset-fonts.py`
- **Logo / photo**: canonical logo at `../logo/stas-logo.jpg`. Re-prep web assets: `.venv\Scripts\python.exe scripts\prep-images.py` → `assets/img/stas-logo.png` (white keyed to transparent) + `assets/img/josiah.jpg` (headshot). Nav logo vertical alignment knob: `--logo-nudge` on `.brand-mark` in `css/styles.css`.
- **og-image / touch icon**: edit `assets/og/og.html` (or `assets/og/icon.html`), then `pwsh scripts\render-og.ps1` (headless Edge screenshots).
- **Hero tool rotator**: text items inside `<span class="rotator" id="ww-rotator">` in `index.html`, cross-faded by `js/main.js`. The JS auto-sizes the slot to the widest item's text (`textContent.length`). To change the rotated tools, edit the `<span class="rot-item">` children — the sizer rebuilds itself. Reduced-motion users see a comma-separated list (CSS in `prefers-reduced-motion` block).
- **Proof rule (from cvkit)**: after any visual change, screenshot at 390 / 768 / 1440 and *look at it* — overlap and overflow don't show up in code.

## Deploy

- GitHub Pages, repo **github.com/JJ-San/saintstech-website** (`main`, root). `CNAME` = saintstech.co.nz. **Deploy = commit + `git push`.**
- **After deploy, hard-refresh (Ctrl+Shift+R)** — GitHub's CDN + browser cache serve the old CSS otherwise.
- DNS at Freeparking (`dnspackage.com`): apex `@` → GitHub IPs `185.199.108–111.153`; `www` → `185.199.108.153`.
- **NEVER touch the domain's MX / SPF / autodiscover / `MS=` TXT records** — company email (Microsoft 365) lives on this domain.
- HTTPS / Enforce-HTTPS state and the cert-unstick steps: see `.claude/sessions/handoff.md`.

## Validation

Manual proof rule above · W3C-valid HTML · Lighthouse ≥95 target · contrast: all small text ≥4.5:1 · with-JS and no-JS both render readable copy.
