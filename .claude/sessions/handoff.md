# Session handoff — saintstech.co.nz website

_Updated 2026-06-19. Durable "how to work" rules live in this folder's `CLAUDE.md`; this file = current state + what's next. **Live & deployed.** This session: body reading text → **Atkinson Hyperlegible** + process-steps polish (`18abb98`), calculator "a typical build" (`08c39e1`), one-pager font syncs (Newsreader+SourceSans3 then Atkinson body), DNS verified live. Serena `project_overview` refreshed._

## ✅ Done 2026-06-19 — body reading text → Atkinson Hyperlegible + process-steps polish (commit `18abb98`, deployed)

Founder chose **Atkinson Hyperlegible** (Braille Institute, OFL — built for low-vision/older readers) for the **body reading text**, after a side-by-side mockup (Source Sans 3 / Inter / IBM Plex / Atkinson). **Scope = prose only**, applied to both renders:
- **Website (`css/styles.css`):** Atkinson on the prose selectors — `.lead, .sect-head p:not(.eyebrow), .step p, .card > p, .card li, .card .fit, .how p, .bio p, .faq .a, .calc-note, .field .hint, .verdict p`. UI chrome (nav, eyebrows, tags, buttons, `h3`/`h4`, SVG) **stays Source Sans 3**; headlines **stay Newsreader**. Atkinson ships only **400/700**, so it can't carry the 500/600/800 weight ladder — hence prose-only. **In-prose bold bumped 500→700** (`.step p b`, `.card li b`, `.bio p b`, `.faq .a b`) or it silently falls back to regular (CSS maps 500→400 when only 400/700 exist). New static WOFF2 subset (~9 KB each) via `subset-fonts.py` (added to `FACES`); source TTFs downloaded to `../services/assets/fonts/`. Preloaded; cache-buster → `2026-06-19a`.
- **One-pager (`../services/services-onepager.html` → PDF):** same treatment — Atkinson on `.head .sub, .step p, .card p, .card ul li, .card .fit, .honest p` (its prose bolds are 600/700 → map cleanly to Atkinson 700). PDF re-rendered (headless Edge); proofed at A4, one page. (Not git-tracked — saved to disk only.)
- **Future:** a wholesale single-sans switch (chrome included) would need **"Atkinson Hyperlegible Next"** (variable, 200–800).

**Process steps (`.steps`, desktop ≥901px only):** the connector that was fused with the per-step header lines is now **lifted into a gap** (`--conn-top:-1.5rem`) above the numbers, **ends in an arrowhead** (`.steps::before`, left→right flow), and the **draw is slowed 1.2s→2.4s** (arrowhead delay → 1.9s). Both hidden ≤900px. Verified via Playwright (computed fonts, reduced-motion safe, console clean).

## ✅ Done 2026-06-18 — one-pager synced to the website font system

The one-pager (`../services/services-onepager.html` → `.pdf`) now matches the website: **Newsreader serif** on the hero tagline (`.head .tag` — opsz 72, wght 470, bold span 640; mirrors the site's `.display`/`.display b`), **Source Sans 3** everywhere else (wordmark, section labels, cards, body, footer). Dropped all 4 Poppins TTFs → self-hosted the two variable TTFs already in `assets/fonts/` (`SourceSans3[wght].ttf`, `Newsreader[opsz,wght].ttf`).
- **Also carried the website's 300→400 body-weight fix** — Source Sans 3 Light (300) reads too thin, same lesson the site already learned. If a strict family-only swap is ever preferred, revert the body `font-weight:400` spots back to 300.
- PDF re-rendered via headless Edge (54 KB → 334 KB, variable TTFs embedded); proofed at A4 — one page, footer intact (`website/proofs/onepager-fonts.png`, gitignored).
- `../services/` is **not a git repo** → saved to disk only, no deploy (this is the print leave-behind, not the website). Tuning knob: serif headline weight is `font-weight:470` on line 32 (site runs ~430).

## ✅ Done 2026-06-16 — body font → Source Sans 3 + calculator "paper" (commit `26aaba2`, deployed)

Completed the font system and restyled the calculator. **CSS/JS/font only — no copy changes.** Verified 390/768/1440, no console errors. Cache-buster → `2026-06-16d`.
- **Body/UI/SVG: Poppins → Source Sans 3** — a humanist sans that shares Newsreader's old-style skeleton, so heading + body finally read as one family (Poppins was geometric, slightly cool against the serif). Self-hosted variable WOFF2 (wght 300–800, ~21 KB) via `subset-fonts.py` (source `SourceSans3[wght].ttf` in `../services/assets/fonts/`, OFL). **Poppins retired** from live pages (404 + index now Source Sans 3 + Newsreader); Poppins WOFF2 kept ONLY because `assets/og/` generators reference them — if those get re-rendered, update them too.
  - **Body reading text is weight 400, not 300** (commit `1aa94e2`): Source Sans 3 Light (300) read too thin where Poppins Light hadn't. Don't drop body copy back to 300. Step/card-bullet/how text is 17px (was 16px, below the 17–19px body). Hero H1 has no bold emphasis span — one uniform Newsreader weight.
  - **Mobile nav stacks the wordmark** (commit `a1e67f4`): ≤600px the lockup goes two-line — "SAINTS" over title-case "Technologies & Services" (`.bl-rest`, .72rem) beside the logo, instead of hiding the suffix. Desktop stays single-line (the inter-word space is now a `.bl-rest` margin, not `&nbsp;`). ≤430px trims the nav CTA padding so it clears down to 360px.
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
1. ✅ **RESOLVED 2026-06-18** (commit `08c39e1`, deployed) — chose **"reword to a typical build"**: the verdict copy (`js/main.js:111`) no longer prints a hard $7,500–$15,000, so it stops clashing with the BUILD card's $7,500–$25,000; `BUILD_HI=15000` left untouched so the default slider verdict stays "Borderline" (raising it would've flipped the default to "Honestly, no"). Cache-buster added to the `main.js` tag. _Original framing, for the record:_ ROI calculator quoted $7,500–$15,000 in `js/main.js` copy + `BUILD_HI = 15000` payback math. **Was deliberately left.** Raising `BUILD_HI` to 25000 lengthens high-end payback enough to flip the *default* slider verdict (6 hrs × $45) from "Borderline" to **"Honestly, no"** — clearly not intended. The $25k is a high anchor, not the *typical* build the calculator models, so $7,500–$15,000 is arguably still the right illustration. **Decision:** leave as-is / reword copy to "a typical build" without a hard ceiling / accept the more-pessimistic math. (Calculator is website-only, part of the standing "master reconciliation owed".)
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
- **DNS: ✅ complete (verified live 2026-06-18).** The earlier "www is still an A record" note was **stale** — in the Freeparking panel `www` is already a **CNAME → jj-san.github.io**. Verified: `https://www.saintstech.co.nz` serves over HTTPS (cert provisioned) and `301`-redirects to the apex; apex = 4 A records (`185.199.108–111.153`), HTTPS `200`. Email records confirmed intact and left untouched: `autodiscover` CNAME, `MX → …mail.protection.outlook.com`, `MS=ms20121589` TXT, SPF `v=spf1 …outlook.com -all`. Nothing owed here.
- **Testimonial:** commented-out block in `index.html`; activate only on a real client quote (name + result).
- **CTAs** are `mailto:` → point at a Microsoft Bookings page when ready (marked `PRODUCTION` in `index.html`).

## Gotchas
- **Content master** = `../services/services.md`; site + one-pager are render targets. Edit the master then "sync the services sheet"; never edit page *wording* directly. (Choosing which sections a render *includes* is a layout call — that's what Task 2's breadcrumb documents, so it isn't mistaken for drift.)
- **Don't add third-party brand logos** without a policy check (see `CLAUDE.md`).
- **After every deploy, hard-refresh** — GitHub CDN + browser cache serve old CSS otherwise.
- **DNS** (Freeparking): apex `@` → GitHub IPs `185.199.108–111.153`. **Never touch MX / SPF / autodiscover / `MS=` TXT — that's the M365 email.**
- **Assets:** logo `../logo/stas-logo.jpg` → `scripts\prep-images.py`; fonts → `scripts\subset-fonts.py` (both use the `.venv`).
