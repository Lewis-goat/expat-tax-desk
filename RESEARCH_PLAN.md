# RESEARCH PLAN — AdSense niche site that outperforms its SERP class on SEO

Date: 2026-09-12 · Workspace: `adsense-site/` · Status: plan approved for execution this session

## 1. Objective

Pick one content niche in which a solo, zero-budget, static-HTML website can (a) monetize
via Google AdSense display advertising, and (b) outrank the current page-1 incumbents
("in-class sites") on structural SEO and content quality — then build and deploy that site.

**Hard constraints (environment reality, stated up front):**
- No paid SEO tools (no Ahrefs/Semrush API). Research uses free sources only.
- No payment rails on this machine → no domain purchase, no AdSense account creation
  (requires the user's Google login). Deliver: deployed site + AdSense-ready integration
  (ads.txt, ad slots, policy pages) + an approval checklist. These two steps need the user.
- AdSense approval itself takes days–weeks after submission; rankings take weeks–months.
  "Outperform" at delivery time = measurably superior on the SEO audit (§6), verified, not
  yet proven by live rankings.

## 2. Candidate generation (Phase A — breadth)

Enumerate niche candidates from a pre-registered hypothesis list biased toward high
AdSense RPM verticals, then expand each into a long-tail query cluster:

| # | Candidate cluster (hypothesis) | RPM prior | Beatability prior |
|---|---|---|---|
| A | Foreign-account tax compliance (FBAR/FATCA/8938 explainers) | $8–15 CPC | info long-tail winnable vs CPA lead-gen sites |
| B | US retirement account mechanics (backdoor Roth, rollover rules) | $4–10 | winnable vs huge finance brands on long-tail |
| C | Accounting-software error/how-to long-tail ("QuickBooks error 6xxx") | $2–6 | error-farm SERPs are thin |
| D | State-specific trades/career licensing paths | $1–4 | fragmented, weak incumbents |
| E | Renters/umbrella insurance claim explainers | $6–20 | YMYL, brand-heavy but long-tail thin |
| F | German-language personal-finance explainers | €1–4 | user German-capable; weaker SERP hygiene in DE |

Long-tail expansion via alphabet-soup: Google/DuckDuckGo suggest APIs
(`suggestqueries.google.com/complete/search?client=firefox&q=…`, `duckduckgo.com/ac/?q=…`)
over seeds × {a–z, how, why, best, can, does, is, vs, without, deadline, penalty, calculator}.

## 3. Data collection (Phase B — evidence per candidate query)

For each candidate niche, sample 8–15 representative long-tail queries and record:
1. **SERP composition** — page-1 results scraped from DuckDuckGo HTML (`html.duckduckgo.com`,
   Bing-backed proxy for Google). Classify each result:
   `forum` (reddit/quora/SE), `brand` (major finance/media domain list), `thin-niche`,
   `gov/edu`, `other`. Record top-10 domain + title.
2. **Ad pressure (CPC proxy)** — (a) public industry CPC benchmark tables (WordStream or
   equivalent) fetched and cited; (b) ad density on Bing HTML SERP if scrapeable, else (a) alone.
3. **Demand proxy** — breadth of suggestion space (count of distinct long-tails found per
   seed), question-form share. Honest label: no free volume data; breadth is a floor signal.
4. **Incumbent quality audit** — for the top 2–3 ranking non-brand pages per niche: fetch page,
   record word count, freshness signals, schema.org presence, title/meta quality.

## 4. Scoring & selection gate (Phase C)

Per niche: `score = 0.35·winnability + 0.30·cpc_band + 0.15·demand_breadth + 0.10·evergreen + 0.10·(1 − ymyl_risk)`
- **winnability** = share of page-1 results that are forums/thin/non-brand (median across sampled queries)
- **Gate to build**: winnability ≥ 0.5 on ≥ 70% of sampled queries, CPC band ≥ $2,
  suggestion breadth ≥ 30 distinct long-tails, AdSense-policy-safe topics only (no medical dosage/
  legal-advice claims; informational, well-sourced YMYL handled with citations).

Deliverable: `research/dossier.md` + `research/scores.json` in `goal-evidence/`.

## 5. Build spec (Phase D — the "outperform in-class sites" part)

Static HTML/CSS, zero JS, zero external requests except AdSense (once approved):
- One hand-written long-form article (1.2–2.5k words, original, cited) per target long-tail,
  8–12 articles at launch, all inter-linked in a hub-spoke pattern.
- Per page: unique `<title>` (≤60 chars, keyword-front-loaded), meta description (≤155),
  canonical, OG/Twitter cards, one `h1`, semantic `article/section/nav`, FAQ section with
  `FAQPage` JSON-LD + `Article` JSON-LD with dates, descriptive alt on every image.
- Site: `sitemap.xml`, `robots.txt`, 404, `about`, `contact`, `privacy.html` (AdSense/Cookie
  disclosure — required for approval), `ads.txt` placeholder, `GA4` slot optional off-by-default.
- Performance: inline critical CSS, system fonts, no framework, total page weight < 60 KB →
  Core Web Vitals comfortably green (in-class incumbents typically 300 KB–3 MB with ad-tech).
- Optional experiment (AlphaEvolve-style, per standing instruction): run OpenEvolve locally
  to evolve `<title>`/meta-description variants against a heuristic scorer (keyword placement,
  length bands, specificity). Adopted only if it beats the hand-written control on the scorer
  and reads naturally; otherwise documented as tried-and-rejected. Rationale: no live-ranking
  ground truth exists at build time, so evolution optimizes a proxy, not true SEO fitness.

## 6. Verification gate (Phase E)

Programmatic audit of every page + site-level checks (asserts, not vibes):
titles/desc lengths, canonicals present, JSON-LD parses, sitemap URLs resolve 200,
internal-link graph connected, page weights, images have alt, no broken hrefs, robots/sitemap
correct, privacy+about+contact+ads.txt present. Visual check of homepage + one article via
browser. Deployment: public GitHub repo under **Lewis-goat** + GitHub Pages enabled, URL live.

## 7. Handoff (what only the user can do)

1. Buy a domain (~$10/yr) → point at Pages (CNAME) — github.io subdomains are routinely
   rejected by AdSense. 2. Create AdSense account, submit site, paste publisher ID into the
   prepared slots, upload real `ads.txt`. Checklist ships in the repo README.

## 8. Success criteria for this goal

- [x] Plan document (this file)
- [ ] Research evidence: ≥5 niches scored with SERP composition data (`research/scores.json`)
- [ ] Niche selected + dossier with incumbent audit
- [ ] Website built: ≥8 articles, full SEO stack, AdSense integration points
- [ ] Deployed to a live URL (GitHub Pages) and verified reachable
- [ ] SEO audit passes on all pages; visual check done
- [ ] AdSense approval checklist for the user
