# Session handoff — saintstech.co.nz website

_Updated 2026-06-16. Durable "how to work" rules live in this folder's `CLAUDE.md`; this file = current state + what's next. **The top block is a ready-to-execute work order handed down from a root strategy session — start there.**_

## ▶ Ready to execute — two section removals (founder-decided 2026-06-16)

A root strategy session decided to cut two sections from the live single-page site. **Both are web-render-only** — do **not** touch the `../services/services.md` master or the one-pager PDF; the relevant copy stays there for the leave-behind. Working tree is clean; deploy = commit + `git push`.

### Task 1 — remove the "We run on what we sell" strip
- In `index.html`, delete the whole `<section class="dogfood" aria-label="We run on what we sell">…</section>` block (it sits between the FAQ section and `#about`).
- This is website-only copy — **confirmed not in the master**, so nothing to sync and no breadcrumb needed.

### Task 2 — remove the "The fine print, up front" section
- In `index.html`, delete the whole `<section class="section" aria-labelledby="straight-t">…</section>` block — i.e. the heading "The fine print, up front." plus its two panels, **"What we don't sell"** and **"Why fixed prices"** (it sits between the "ships with" `.band` and `#calculator`).
- These two panels **do** live in the `services.md` master and the one-pager — **leave them there.** Drop a breadcrumb where the section was so a future "sync the services sheet" doesn't silently re-add it:
  ```html
  <!-- Web render intentionally omits "Straight answers / fine print" (what we don't sell · why fixed prices) — founder call 2026-06-16. Still in services.md master + one-pager; don't re-add on sync. -->
  ```

### ⚠ Proof-rule watch-out (the reason this needs eyes, not just a delete)
Removing the fine-print section makes the **navy `.band` ("ships with") land directly on the navy `#calculator`** — two dark blocks with no light section between them. **Screenshot the band→calculator seam** after the edit. If it reads as one merged slab, add separation (a divider, extra spacing, or give one section a contrasting background) and say what you did. (The faq→about seam is fine — light grey to white.)

### Cleanup + ship
- `.straight` and `.panel` rules in `css/styles.css` become unused after Task 2 — optional to delete. **If you touch CSS, bump the `styles.css?v=` cache-buster** in `index.html`.
- Commit + push (deploy), hard-refresh (Ctrl+Shift+R), screenshot at **390 / 768 / 1440** and look.

## ⏸ Strategy context — do NOT act on this yet
- The live strategy thread is the **pricing display** in `#services` (the $ ranges + "delivered in days" / "delivered in 2–3 weeks"). **Undecided** — leave prices/timelines exactly as they are until Josiah calls it. Competitor revisit doc: `C:\Users\josia\Documents\STAS-NZ-competitors.md`.
- FYI only: the "Why fixed prices" panel removed in Task 2 was the on-page justification for those prices. Its removal is a separate, already-made call and does **not** pre-decide the pricing thread.

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
