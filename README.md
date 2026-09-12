# Expat Tax Desk

A zero-JS, AdSense-ready content site in the expat/foreign-account tax niche (FBAR · FATCA ·
FinCEN Form 114), built to outperform the current in-class SERP on structural SEO: 4.5–23 KB
pages, inline CSS, semantic HTML, Article + FAQPage + Breadcrumb JSON-LD, canonical URLs,
sitemap, and 2026-current content — including the post-DFSP reality that most incumbents
still get wrong.

- Live: https://lewis-goat.github.io/expat-tax-desk/
- Source + research: `adsense-site/` in the local workspace (plan, dossier, SERP data, scorer)

## Rebuild locally

```bash
python3 build.py   # markdown in content/ -> dist/
python3 audit.py   # SEO gate: exits 1 on any failure
```

## What only the site owner can do (AdSense checklist)

1. **Domain**: register a domain (~$10/yr) and point it at this site
   (GitHub Pages → custom domain, or any static host). AdSense routinely rejects
   `github.io` subdomains; a real domain is effectively required.
2. **AdSense account**: [google.com/adsense](https://www.google.com/adsense) → add the
   domain → submit for review. Site already has the prerequisites: original content
   (10 articles), about/contact/privacy pages, privacy policy with the required
   Google advertising-cookie disclosures.
3. **After approval**: uncomment the `<head>` script in `build.py` (`AD_HEAD`), replace
   `ca-pub-0000000000000000` with the real publisher ID, replace the two ad-slot comment
   markers per article with responsive `<ins class="adsbygoogle">` units, rebuild,
   and replace `dist/ads.txt` with the real line:
   `google.com, pub-XXXXXXXXXXXXXXXX, DIRECT, f08c47fec0942fa0`
4. **Search Console**: verify the domain, submit `sitemap.xml`, request indexing on the
   hub page. Rankings take weeks–months; the audit gate (`audit.py`) is the build-time proxy.

## Content maintenance (the moat)

- Every January: check the new-year FBAR figures (IRS inflation adjustments) and update
  the penalty/deadline pages — this is the freshness edge over stale incumbents.
- The `content/*.md` files are the source of truth; never edit `dist/` by hand.
