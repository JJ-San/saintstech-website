# Session handoff — saintstech.co.nz website

_Updated 2026-06-16. Durable "how to work" rules live in this folder's `CLAUDE.md`; this file = current state + what's next._

## ✅ Done 2026-06-16 — two sections removed (commit `d9a25f5`, pushed + deployed)

Executed the founder-decided work order to cut two sections from the live single-page site. **Both were web-render-only** — the copy stays in the `../services/services.md` master + one-pager for the leave-behind, so nothing was synced (these are render-layout choices, not master edits).

- **Removed the "We run on what we sell" dogfood strip** (was between FAQ and `#about`). Website-only copy, not in the master — no breadcrumb needed. FAQ (grey) now flows straight into About (white): clean seam, verified.
- **Removed the "Straight answers / The fine print, up front" section** (the two panels **What we don't sell** · **Why fixed prices**, was between the "ships with" `.band` and `#calculator`). These **do** live in the master + one-pager — **left there**; an HTML breadcrumb now sits where the section was so a future "sync the services sheet" won't silently re-add it.
- **Seam fix (the proof-rule watch-out):** removing the light fine-print section put the navy `.band` directly on the navy `#calculator` (two dark blocks). Added a 1px hairline `border-top:1px solid rgba(255,255,255,.10)` on `.calc` so the band→calculator boundary reads clearly. Checked at **390 / 768 / 1440** — the band reads as its own strip and the calculator clearly re-opens below it; not a merged slab.
- **Cleanup:** dropped now-dead `.straight` / `.panel` / `.dogfood` CSS; bumped cache-buster to `styles.css?v=2026-06-16a`.

## ⏸ Strategy context — do NOT act on this yet
- The live strategy thread is the **pricing display** in `#services` (the $ ranges + "delivered in days" / "delivered in 2–3 weeks"). **Undecided** — leave prices/timelines exactly as they are until Josiah calls it. Competitor revisit doc: `C:\Users\josia\Documents\STAS-NZ-competitors.md`.
- FYI only: the "Why fixed prices" panel removed above (the fine-print cut) was the on-page justification for those prices. Its removal is a separate, already-made call and does **not** pre-decide the pricing thread.

## Status (current live site)
- LIVE over HTTPS — https://saintstech.co.nz. Repo **github.com/JJ-San/saintstech-website** (`main`, root). Working tree clean.
- Single-page site; **JS is progressive enhancement** (`js/main.js`: tool rotator, ROI calculator, IntersectionObserver reveals, sticky mobile CTA). `about/index.html` = redirect to `/#about`.
- Nav: logo + "SAINTS TECHNOLOGIES & SERVICES" wordmark; weight ladder **SAINTS 800 / nav links 600 / suffix 500**. Six self-hosted Poppins weights (300/400/500/600/700/800), subset via `scripts\subset-fonts.py` from `../services/assets/fonts/`.
- Hero: "Find where AI **actually pays off** in your business." + one merged subhead with the inline **text** rotator (Xero · MYOB · Microsoft 365 · Google Workspace · HubSpot). **Rotator stays text, not logos** — brand-policy (MYOB / M365 = violation, Xero = caution); footer carries a trademark notice. See `CLAUDE.md`.

## Other open items (not part of the work order above)
- **Master reconciliation owed:** `index.html` carries sections (FAQ, calculator, restructured copy) not back-ported into the `services.md` master — flagged in the `index.html` header comment.
- **DNS:** `www` is still an A record → change to CNAME → jj-san.github.io for www HTTPS coverage. Apex is fully live.
- **Testimonial:** commented-out block in `index.html`; activate only on a real client quote (name + result).
- **CTAs** are `mailto:` → point at a Microsoft Bookings page when ready (marked `PRODUCTION` in `index.html`).

## Gotchas
- **Content master** = `../services/services.md`; site + one-pager are render targets. Edit the master then "sync the services sheet"; never edit page *wording* directly. (Choosing which sections a render *includes* is a layout call — that's what Task 2's breadcrumb documents, so it isn't mistaken for drift.)
- **Don't add third-party brand logos** without a policy check (see `CLAUDE.md`).
- **After every deploy, hard-refresh** — GitHub CDN + browser cache serve old CSS otherwise.
- **DNS** (Freeparking): apex `@` → GitHub IPs `185.199.108–111.153`. **Never touch MX / SPF / autodiscover / `MS=` TXT — that's the M365 email.**
- **Assets:** logo `../logo/stas-logo.jpg` → `scripts\prep-images.py`; fonts → `scripts\subset-fonts.py` (both use the `.venv`).
