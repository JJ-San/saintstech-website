# brand/website — saintstech.co.nz

Static two-page site (Home + About) for Saints Technologies & Services. This is **render target #3** of the content master `../services/services.md` — same one-way rule as the one-pager: master → render, never the reverse. Full sync flow: `../services/README.md`.

## Rules

- **NEVER edit page copy in the HTML directly.** Edit `../services/services.md` (including its `Website-only content` section), then sync ("sync the services sheet"). Design/CSS polish directly in the HTML/CSS is fine.
- Brand tokens: Poppins (Light 300 / Regular 400 / Medium 500 / Bold 700) · navy `#2F3B49` · teal `#3E9DAE` · **accent-deep `#2E7785`** (web-only token: brand teal is 3.0:1 on white, so small text/CTAs use accent-deep at ≥4.5:1; bright teal is for borders, bullets, large accents, and accents on navy) · accent-soft `#EAF4F6`.
- **Zero JavaScript.** Scroll reveals are CSS `animation-timeline` behind `@supports`, with a `prefers-reduced-motion` opt-out. Keep it that way unless a recorded decision says otherwise.
- The testimonial section in `index.html` ships **commented out**. Activate only with a real client quote (name + specific result). Never placeholder praise.
- The About portrait `<figure>` ships with the `hidden` attribute. Drop the headshot at `assets/img/josiah.jpg`, remove `hidden`.

## Rituals

- **Fonts**: brand-owned TTFs live in `../services/assets/fonts/`. Re-subset → WOFF2: `.venv\Scripts\python.exe scripts\subset-fonts.py`
- **og-image / touch icon**: edit `assets/og/og.html` (or `assets/og/icon.html`), then `pwsh scripts\render-og.ps1` (headless Edge screenshots).
- **Proof rule (from cvkit)**: after any visual change, screenshot at 390 / 768 / 1440 and *look at it* — overlap and overflow don't show up in code.

## Deploy

- GitHub Pages, `main` branch, root. `CNAME` = saintstech.co.nz. **Deploy = commit + `git push`.**
- DNS lives at Freeparking (`dnspackage.com` nameservers): apex A records → GitHub Pages IPs, `www` CNAME → the GitHub account's `*.github.io`.
- **NEVER touch the domain's MX / SPF / `MS=` TXT records** — company email (Microsoft 365) lives on this domain.

## Validation

Manual proof rule above · W3C-valid HTML · Lighthouse ≥95 target · contrast: all small text ≥4.5:1.
