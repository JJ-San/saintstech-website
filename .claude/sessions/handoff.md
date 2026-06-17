# Session handoff — saintstech.co.nz website

_Updated 2026-06-16. Durable "how to work" rules live in this folder's `CLAUDE.md`; this file = current state + what's next._

## ▶ Owed: sync the one-pager to the new web font system

The website now uses **Newsreader headlines + Source Sans 3 body**; the one-pager (`../services/services-onepager.html` → PDF) is still **all Poppins**. Josiah said this is minor and to bring the one-pager in line with the website later. When picked up: add Newsreader (headings) + Source Sans 3 (body) to the one-pager's `@font-face` (TTFs are in `../services/assets/fonts/`), re-render the PDF (headless Edge — `../services/README.md`). Not urgent.

## ✅ Done 2026-06-16 — body font → Source Sans 3 + calculator "paper" (commit `26aaba2`, deployed)

Completed the font system and restyled the calculator. **CSS/JS/font only — no copy changes.** Verified 390/768/1440, no console errors. Cache-buster → `2026-06-16d`.
- **Body/UI/SVG: Poppins → Source Sans 3** — a humanist sans that shares Newsreader's old-style skeleton, so heading + body finally read as one family (Poppins was geometric, slightly cool against the serif). Self-hosted variable WOFF2 (wght 300–800, ~21 KB) via `subset-fonts.py` (source `SourceSans3[wght].ttf` in `../services/assets/fonts/`, OFL). **Poppins retired** from live pages (404 + index now Source Sans 3 + Newsreader); Poppins WOFF2 kept ONLY because `assets/og/` generators reference them — if those get re-rendered, update them too.
- **Calculator → cream "worksheet" on a dark "desk":** the `#calculator` section stays dark (preserves the page's dark beat) but the calculating surface is now a cream paper sheet (`.calc-sheet` wrapper) — cream stock, faint ledger ruling, grain as paper tooth, soft drop-shadow. `.calc` is no longer `.on-dark`; all inputs/results/verdict re-inked for the light surface; slider fill recoloured (CSS + the JS `paint()`); verdict CTA → `btn-solid`; verdict title set in Newsreader. New tokens: `--paper-cream`, `--paper-line`, `--ink-warm`, `--ink-warm-soft`.

## ✅ Done 2026-06-16 — typography: Newsreader serif headlines + larger scale (commit `1c5e65b`, deployed)

Headline face decided. Mocked up Poppins / Fraunces / Newsreader / Bricolage side-by-side; Josiah liked Fraunces but found it hard to read (audience skews **older**), so chose **Newsreader** + a size bump.
- **Headlines only** (`.display` H1 + all `h2`) → **Newsreader** (variable serif, designed for reading). Everything else stays Poppins (body, eyebrows, buttons, nav, `h3`/`h4`).
- **Self-hosted** like Poppins: one WOFF2 (~35 KB), opsz pinned to display 72, wght 400–700. Source TTF `Newsreader[opsz,wght].ttf` lives in `../services/assets/fonts/` (google/fonts, OFL); subset via the existing `scripts\subset-fonts.py` (now also does Newsreader). Preloaded in `<head>`.
- **Type scale up for readability:** body 16–17px → 17–19px; `.lead`, H1/H2, and main reading paragraphs (`.step p`, `.card li`, `.how p`, FAQ summary) all larger. Verified 390/768/1440, no overflow.
- Brand-token line in `CLAUDE.md` updated. Headline weights (`.display` 430/640, `h2` 520) are tunable in `css/styles.css` if Josiah wants lighter/heavier.

## ✅ Done 2026-06-16 — design pass: contrast rhythm + cohesion + motion (commit `cdfe682`, deployed)

Restored the section-contrast rhythm that flattened when the dogfood + fine-print sections were removed, plus cohesion/motion polish. **CSS/JS only — no copy or master changes.** Verified at 390/768/1440, no console errors. Cache-buster → `2026-06-16b`.
- **Rhythm:** "ships with" band re-toned to a **light teal-soft strip** (kills the band→calculator dark-on-dark slab — now a clean light→dark beat — and restores a teal accent; the calc hairline band-aid is gone). **About → teal-soft** accent (breaks the FAQ→About→How-I-work light run); **FAQ → white**; **`--paper-2` deepened** (`#F6F9FB`→`#EDF1F4`) so white/grey actually reads as alternation. New cadence: dark · white · grey · teal-band · **DARK calc** · white · **teal About** · grey · **DARK contact**.
- **Dark-section cohesion:** hero dot-grid + a subtle film-grain (`--grain` token) now also on the calculator and contact.
- **Distinctive touches (all reduced-motion safe):** process steps gain a teal **connector that draws on reveal** (4-col desktop only; hidden ≤900px); About portrait floats **centered against the bio** (editorial asymmetry, desktop only); calculator **verdict badge pulses** on state change; nav **teal scroll-progress** fill (`--scroll`) + nav-link **teal underline-wipe**.
- New CSS hooks: `.tint` (teal-soft section), `--grain`, `--scroll`, `.steps.is-drawn`, `.verdict.pulse`.

## ✅ Done 2026-06-16 — two sections removed (commit `d9a25f5`, pushed + deployed)

Executed the founder-decided work order to cut two sections from the live single-page site. **Both were web-render-only** — the copy stays in the `../services/services.md` master + one-pager for the leave-behind, so nothing was synced (these are render-layout choices, not master edits).

- **Removed the "We run on what we sell" dogfood strip** (was between FAQ and `#about`). Website-only copy, not in the master — no breadcrumb needed. FAQ (grey) now flows straight into About (white): clean seam, verified.
- **Removed the "Straight answers / The fine print, up front" section** (the two panels **What we don't sell** · **Why fixed prices**, was between the "ships with" `.band` and `#calculator`). These **do** live in the master + one-pager — **left there**; an HTML breadcrumb now sits where the section was so a future "sync the services sheet" won't silently re-add it.
- **Seam fix (the proof-rule watch-out):** removing the light fine-print section put the navy `.band` directly on the navy `#calculator` (two dark blocks). Added a 1px hairline `border-top:1px solid rgba(255,255,255,.10)` on `.calc` so the band→calculator boundary reads clearly. Checked at **390 / 768 / 1440** — the band reads as its own strip and the calculator clearly re-opens below it; not a merged slab.
- **Cleanup:** dropped now-dead `.straight` / `.panel` / `.dogfood` CSS; bumped cache-buster to `styles.css?v=2026-06-16a`.

## ✅ Done 2026-06-16 — pricing sync (commit `b14b593`, pushed + deployed)

Executed the approved root pricing work order (Enns *Pricing Creativity* / Weiss *Value-Based Fees*). Master `../services/services.md` edited, then mirrored into **both** renders (website `#services` cards + one-pager → PDF re-rendered via headless Edge). Proofed at 390/768/1440 on both renders.

- **Dropped "fixed"** from both card ranges — published ranges are now *indicative*; the fixed quote still comes from the paid Assessment (Step 2 + the `$1,500–2,500 fixed` Assessment tag left unchanged, which reinforces the doctrine).
- **ENABLE:** `$2,500 – $6,000 · delivered in days to weeks, depending on scope` — timeframe wording confirmed by Josiah.
- **BUILD:** `Typically $7,500 – $25,000 · delivered in 2–8 weeks, depending on scope` — ceiling 15k→25k as the high anchor (resolves the parked "BUILD ceiling" question); was "2–3 weeks".
- **Range format:** cost ranges use the **en-dash** (`$X – $Y`) and both cards carry **"depending on scope"** (Josiah, 2026-06-16 — briefly tried "$X to $Y", reverted to en-dash). The "days to weeks" timeframe phrase keeps the word "to".
- **JSON-LD `priceRange`** bumped NZ$15,000 → NZ$25,000 to match.
- Render note: the **website** drops the literal "·" between price and timeframe (the narrow cards wrap, so the flex gap + size/weight/colour hierarchy separates them); the **master + one-pager** keep the "·" (renders inline on the wide print card). Content is identical; only the separator glyph differs per render — a layout call.

### ⚠ Follow-ups this opened (NOT done — need a call)
1. **ROI calculator still quotes $7,500–$15,000** (`js/main.js`: line 98 copy + `BUILD_HI = 15000` in the payback math). **Deliberately left.** Raising `BUILD_HI` to 25000 lengthens high-end payback enough to flip the *default* slider verdict (6 hrs × $45) from "Borderline" to **"Honestly, no"** — clearly not intended. The $25k is a high anchor, not the *typical* build the calculator models, so $7,500–$15,000 is arguably still the right illustration. **Decision:** leave as-is / reword copy to "a typical build" without a hard ceiling / accept the more-pessimistic math. (Calculator is website-only, part of the standing "master reconciliation owed".)
2. **Brain decision record missing:** `brain/wiki/.../service-architecture-three-layer.md` doesn't exist (brain is empty by design). Per `../services/README.md`, price changes should flow into that decision page + log. Capture this decision (drop "fixed" / $25k ceiling / Enns-Weiss rationale) at **root** when the brain wiki is next touched.

**Parked (separate, bigger thread — root):** make the per-job quote a **3-option good-better-best proposal** out of the Assessment (Enns Rule #2 / Weiss "choice of yeses"). Sales-motion change, not a website change.

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
