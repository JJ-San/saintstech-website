# Session handoff — saintstech.co.nz website

_Updated 2026-06-16. Current state + what's left. Durable "how to work" rules live in this folder's `CLAUDE.md`; this file is the blueprint for the next session._

## Status: LIVE over HTTPS — https://saintstech.co.nz
- Repo **github.com/JJ-San/saintstech-website** (public) · deploy = commit + `git push` (GitHub Pages, `main`, root).
- **Working tree clean, fully pushed.** Last commit `aed40bc`.
- **Single-page site** (`index.html`) + `about/index.html` kept as a `/about/ → /#about` redirect. **JS is a progressive enhancement** (`js/main.js`: tool rotator, ROI calculator, IntersectionObserver scroll-reveals, sticky mobile CTA); the page must still read without JS.

## Done recently (2026-06-15 / 16)
- **Single-page redesign deployed (v3):** new hero, four-step process, two service cards, "ships with" marquee, ROI calculator, FAQ, dogfood strip, About (folded in), contact. Self-hosted Poppins, real founder photo.
- **Nav:** real STAS logo image (`assets/img/stas-logo.png`) **+** restored "SAINTS TECHNOLOGIES & SERVICES" wordmark beside it. Weight ladder — **SAINTS ExtraBold 800 / nav links SemiBold 600 / "Technologies & Services" Medium 500** at `--body` contrast. `.bl-rest` hides the suffix ≤600px so the nav fits on phones.
- **Fonts:** added **Poppins SemiBold 600 + ExtraBold 800** to the self-hosted set (now 300/400/500/600/700/800). Subset via `scripts\subset-fonts.py`; source TTFs in `../services/assets/fonts/` (OFL, from google/fonts).
- **Hero copy:** H1 "Find where AI **actually pays off** in your business." + one merged subhead with the inline rotator (Xero · MYOB · Microsoft 365 · Google Workspace · HubSpot), reading "…such as [rotator] and the spreadsheets you live in." (no colon, no em-dash).
- **Rotator stays TEXT, not logos** — 2026-06-15 brand-policy research: MYOB and Microsoft 365 logos would be policy violations, Xero a caution. Footer carries a trademark/independence notice. (Rationale recorded in `CLAUDE.md`.)
- **"Book a free talk" CTAs:** nav button fixed to white-on-teal (was navy — a `.nav-links a` specificity collision; scoped to `:not(.btn)`). Hero / calculator / mobile-sticky CTAs are `btn-light` by design.
- **CSS cache-buster:** `styles.css?v=2026-06-15d` (bump the suffix on CSS changes so returning visitors don't get stale CSS).
- **One-pager re-synced + re-rendered:** `../services/services-onepager.html` had **drifted** (old "We put AI to work…" tagline); brought in line with the new hero and the PDF re-rendered (headless Edge — see `../services/README.md`).

## Open / next steps
1. **PRICING DISPLAY — active strategy decision (do this before touching `#services`).** Josiah is reconsidering whether to show prices ($2,500–6,000 / $7,500–15,000) and timelines ("delivered in days" / "2–3 weeks") in the Services section. Competitor revisit doc: **`C:\Users\josia\Documents\STAS-NZ-competitors.md`**. The 2026-06-12 research flagged *published fixed mid-band pricing* as differentiator (gap #3) and recorded "prices unchanged" — now being revisited. Resolve which of three: (a) numbers visible at all, (b) timelines feel boxed-in, (c) prices in services-section specifically vs assessment-gated. **The fix differs per answer.**
2. **Master reconciliation still owed:** `index.html` has sections (FAQ, calculator, restructured copy) not fully back-ported into the `../services/services.md` master. Flagged in the `index.html` header comment. Reconcile so master → render stays one-directional.
3. **DNS cleanup (minor, optional):** `www` is still an **A** record → GitHub flags `InvalidARecordError`. Change `www` from A `185.199.108.153` to **CNAME → jj-san.github.io** in Freeparking so `www.` is also HTTPS-covered. Apex is fully live.
4. **Josiah to review website-only copy** in `../services/services.md` → `## Website-only content` (bio, "how I work", response promise, meta), then re-sync.
5. **Testimonial** — commented-out block in `index.html`; activate only with a real client quote (name + result).
6. **CTAs → Microsoft Bookings:** currently `mailto:`; point at a Bookings page when ready (marked `PRODUCTION` in `index.html`).

## Backlog (not started)
NZBN footer slot (comment already in footer) · analytics (GoatCounter / Cloudflare-free) · Google Business Profile (ops) · `/work` case-study page once one exists · OG card could gain the logo.

## Key context / gotchas
- **Content master** = `../services/services.md` (incl. `## Website-only content`). Site + one-pager are render targets — edit the master then "sync the services sheet"; never edit page copy directly. Flow: `../services/README.md`.
- **Don't add third-party brand logos** (Xero/MYOB/M365/Google/HubSpot) without a policy check — text mentions + footer notice are the cleared path. See `CLAUDE.md`.
- **Assets:** logo `../logo/stas-logo.jpg` → `scripts\prep-images.py` → `assets/img/stas-logo.png` + `josiah.jpg`. Fonts → `scripts\subset-fonts.py` (uses the `.venv`). Logo vertical nudge: `--logo-nudge` on `.brand-mark`.
- **Iterating visuals:** serve locally (`.venv\Scripts\python.exe -m http.server 8080 --directory .`), screenshot at 390/768/1440 (proof rule), deploy. **After each deploy, hard-refresh (Ctrl+Shift+R)** — GitHub CDN + browser cache serve old CSS otherwise.
- **DNS** (Freeparking): apex `@` → four GitHub IPs `185.199.108–111.153`; `www` → `185.199.108.153`. **Never touch MX / SPF / autodiscover / `MS=` TXT — that's the M365 email.**
- **HTTPS** (resolved 2026-06-11): if a cert ever sticks on `null`, toggle the custom domain off/on in Settings → Pages to force re-issue.
