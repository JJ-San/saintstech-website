# Session handoff — saintstech.co.nz website

_Updated 2026-06-16. Durable "how to work" rules live in this folder's `CLAUDE.md`; this file = current state + what's next._

## ✅ Done 2026-06-16 — two sections removed (commit `d9a25f5`, pushed + deployed)

Executed the founder-decided work order to cut two sections from the live single-page site. **Both were web-render-only** — the copy stays in the `../services/services.md` master + one-pager for the leave-behind, so nothing was synced (these are render-layout choices, not master edits).

- **Removed the "We run on what we sell" dogfood strip** (was between FAQ and `#about`). Website-only copy, not in the master — no breadcrumb needed. FAQ (grey) now flows straight into About (white): clean seam, verified.
- **Removed the "Straight answers / The fine print, up front" section** (the two panels **What we don't sell** · **Why fixed prices**, was between the "ships with" `.band` and `#calculator`). These **do** live in the master + one-pager — **left there**; an HTML breadcrumb now sits where the section was so a future "sync the services sheet" won't silently re-add it.
- **Seam fix (the proof-rule watch-out):** removing the light fine-print section put the navy `.band` directly on the navy `#calculator` (two dark blocks). Added a 1px hairline `border-top:1px solid rgba(255,255,255,.10)` on `.calc` so the band→calculator boundary reads clearly. Checked at **390 / 768 / 1440** — the band reads as its own strip and the calculator clearly re-opens below it; not a merged slab.
- **Cleanup:** dropped now-dead `.straight` / `.panel` / `.dogfood` CSS; bumped cache-buster to `styles.css?v=2026-06-16a`.

## ▶ Pricing work order — approved 2026-06-16 (sync the services sheet)

Decided in a root strategy session, grounded in the consulting-pricing wiki (Enns *Pricing Creativity*, Weiss *Value-Based Fees*). This is a **master edit → render both** ("sync the services sheet"): change `../services/services.md`, then re-render the website (`#services` cards) **and** the one-pager PDF. Do **not** edit the website wording in isolation.

**Changes:**
1. **Drop the word "fixed" from the on-page ranges.** Doctrine: publish *typical ranges*, not fixed numbers — the **fixed quote comes from the paid Assessment** (Step 2 already says so; make it explicit near the cards if needed). Reframe both tiers as "typically $X–$Y, depending on scope."
2. **BUILD ceiling $15k → $25k.** New BUILD range **$7,500 – $25,000** (resolves the parked "BUILD ceiling" question). The top is the *high anchor*, not a "max scope."
3. **Timeframes:**
   - ENABLE: "delivered in days" → **"days to a couple of weeks"** ⚠ *CONFIRM exact wording with Josiah — his phrasing ("in days because it could be a few weeks") was ambiguous; keep it clearly shorter than BUILD's range.*
   - BUILD: "2–3 weeks" → **"2–8 weeks"** (was over-specified, and tighter than the master's own "a few weeks").
4. ENABLE price **unchanged** ($2,500–$6,000).

**Exact master lines to change in `../services/services.md`:**
- ENABLE: `**$2,500 – $6,000 fixed · delivered in days**` → `**$2,500 – $6,000 · delivered in days to a couple of weeks**`
- BUILD: `**Typically $7,500 – $15,000 fixed · delivered in a few weeks**` → `**Typically $7,500 – $25,000 · delivered in 2–8 weeks**`
- Mirror in the website `#services` card `.price` lines and the one-pager `.price` lines.

Then: deploy the website (commit + push, hard-refresh, screenshot 390/768/1440) and re-render the one-pager PDF (headless Edge — see `../services/README.md`).

**Parked (separate, bigger thread — NOT this work order):** make the per-job quote a **3-option good-better-best proposal** out of the Assessment (Enns Rule #2 / Weiss "choice of yeses"). That's a sales-motion change, tracked at root — don't build it into the website.

Competitor revisit doc (context): `C:\Users\josia\Documents\STAS-NZ-competitors.md`.

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
