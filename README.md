# PCX website — design handoff

Thirteen finished pages, the assets they use, and the script that turns them
into a deployable site. This is the visual and structural source of truth for
the PCX web build.

Everything here runs as plain HTML. There is no framework, no build step for
the pages themselves, and no dependencies to install.

    python3 dev-server.py        # serves site/ at http://localhost:8734

---

## What is here

    site/
      homepage-v2.html           →  /
      accounts-v2.html           →  /accounts
      accounts-standard.html     →  /accounts/standard
      accounts-ecn.html          →  /accounts/ecn
      accounts-demo.html         →  /accounts/demo
      accounts-metals.html       →  /accounts/precious-metals
      why-abook-v2.html          →  /why-a-book
      legal-*.html               →  /legal/*
      _shell.html                   the shared navbar + footer (not a page)
      assets/                       56 images, all referenced
      docs/                         signed legal PDFs
    build-dist.py                   pages → dist/ with clean URLs
    dev-server.py                   local preview
    netlify.toml                    build command and headers

`build-dist.py` maps each page to its clean URL, strips the preview hooks,
rewrites asset paths to root-absolute, and copies only referenced assets.

    python3 build-dist.py           # → dist/

---

## Rules that are not negotiable

**The copy is locked.** Every sentence was written and signed off by the
business team, and several are regulatory. Layout, hierarchy, motion and
markup are all yours to rebuild. The words are not. If a line looks wrong,
raise it — do not edit it.

**Numbers must stay in sync across pages.** The same figures appear on the
homepage lineup, the comparison table, each account page and the closing
tiles. Today they agree. A change in one place is a change in four:

| | Standard | ECN | Precious Metals | Demo |
|---|---|---|---|---|
| Spread from | 1.0 pips | 0.0 pips | raw gold spread | mirrors the live account |
| Commission | $0 | $7 per lot | $7 per lot | none, virtual |
| Min deposit | $10 | $100 | $5,000 | $0 |
| Max leverage | 1:500 | 1:500 | 1:10 | mirrors |

**Navbar and footer are one component.** They are copy-pasted into all
thirteen pages here because these are static files. In the real build they
must become a single component — the only per-page difference is
`class="is-active"` on the current nav link.

---

## Things that are prototype, not product

**`?dev=<section-id>` hooks.** Each page carries a small script that jumps to
a section on load, for reviewing. `build-dist.py` strips it. Do not ship it.

**The homepage price panel.** It reads FX levels from a public keyless
endpoint and derives bid/ask from PCX's published spread, held in the page.
That is a stand-in. In production it must read PCX's own MT5 feed — spreads
are broker-specific and cannot come from a third party. XAUUSD has no free
source and currently moves on a simulated walk.

**Motion.** Every looping animation pauses when its section leaves the
viewport, and all of it respects `prefers-reduced-motion`. Keep both.

**Cache.** `dev-server.py` sends `no-store` on purpose: a plain static server
lets browsers hold stale images for hours, which repeatedly made finished work
look unchanged during review.

---

## How the pages are built

Each account page follows the same shape: hero → who it is for → three doubts
→ three answers → the numbers → specifications → other accounts → the honest
caveat → FAQ → invitation.

Illustrations are **named diagrams, not metaphors**. A picture that has to be
decoded was rejected every time it was tried. What survived is a labelled
relationship — `YOUR ORDER → PCX → LIQUIDITY PROVIDERS` — with the providers
stacked so that "many" reads at a glance. The same object always means the
same thing across pages: navy is the market's side, gold is our fee.

## Palette and type

    ivory   #FAF6EF      navy   #0A0A3C / #2C2C54
    gold    #D4AF37 / #B8942C        white  #FFFFFF

Inter for headings and UI, Space Grotesk for body, never below 15px.
**Gold is never used for body text** — it fails contrast on ivory.
