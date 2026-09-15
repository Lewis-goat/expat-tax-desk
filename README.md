# Expat Tax Desk

A zero-JS, AdSense-ready content site in the expat/foreign-account tax niche (FBAR · FATCA ·
FinCEN Form 114), built to outperform the current in-class SERP on structural SEO: 4.5–23 KB
pages, inline CSS, semantic HTML, Article + FAQPage + Breadcrumb JSON-LD, canonical URLs,
sitemap, and 2026-current content — including the post-DFSP reality that most incumbents
still get wrong.

- Live: **https://expattaxdesk.com** (Cloudflare-registered domain on GitHub Pages, HTTPS enforced)
- Source + research: `adsense-site/` in the local workspace (plan, dossier, SERP data, scorer)

## Rebuild locally

```bash
python3 build.py   # markdown in content/ -> dist/
python3 audit.py   # SEO gate: exits 1 on any failure
```

## AdSense status

- Custom domain live with HTTPS, ads.txt + publisher script deployed
- Google CMP consent message live; Auto ads enabled
- Site review requested; static pages carry the required Google advertising-cookie disclosures
