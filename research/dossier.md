# NICHE DOSSIER — Expat / foreign-account tax compliance (FBAR·FATCA cluster)

Decision date: 2026-09-12 · Method per `../RESEARCH_PLAN.md` · Raw data: `suggestions.json`, `serps_raw.json` (Bing layer discarded — see §3), `scores.json`

## 1. What was measured

| Data layer | Source | Status |
|---|---|---|
| Long-tail demand breadth | Google suggest API (alphabet-soup, 21 suffixes × seeds × 6 niches) | ✅ 1,746 distinct suggestions captured |
| SERP composition | DDG HTML via reader service + Z.ai WebSearch (US) | ✅ 4 expat-tax queries + 1 insurance + 1 retirement sampled in depth |
| SERP composition (2nd source) | Bing HTML via curl | ❌ discarded — serves unrelated cached junk without a session |
| CPC benchmarks | [WordStream 2025](https://www.wordstream.com/blog/2025-google-ads-benchmarks) (avg $5.26; legal ~$6.75), [AdBacklog 2025](https://adbacklog.com/blog/google-ads-benchmarks-per-industry-2025) (finance/insurance $3.50–6.50 search CPC) | ✅ cited |

## 2. Scores (rebuilt from valid layers: suggestions + sampled SERPs + cited CPC bands)

| Niche | Suggestions | SERP page-1 composition (sampled) | CPC band | Winnability verdict |
|---|---|---|---|---|
| **A. Expat/foreign-account tax** | **252** | FBAR queries: mostly **small law/CPA firm blogs** (goldinglawyers.com, vernitaxlaw.com, virginia-tax-lawyer.com, brighttax.com, hntaxlaw.com, taxesforexpats.com) + 1 forum + 1–2 gov/brand | **$8–15** | **WINNER** |
| E. Insurance claims | 318 | "renters insurance water damage" page 1 = NerdWallet, Lemonade, The Zebra, Assurance IQ, Policygenius — wall of national brands | $6–20 | brand-blocked |
| B. Retirement mechanics | 540 | "mega backdoor roth 2026" = Mercer, IRA Financial, SDO CPA, Coldstream, WealthKeel — high-authority financial firms | $4–10 | authority-blocked |
| D. Career licensing | 374 | not sampled in depth | $1–4 | CPC too low vs plan gate |
| F. German finance | 238 | not sampled in depth | €1–4 | CPC too low; language scale-down |
| C. Accounting software | 24 | — | $2–6 | demand breadth below gate (<30) |

## 3. Why expat tax wins

1. **Beatable SERP class**: FBAR/FATCA long-tail is owned by solo-practitioner and small-firm blogs — typically slow sites (heavy WordPress themes, 1–3 MB pages), thin schema, stale dates, weak internal linking. This is precisely the "in-class site" the build spec (§5 of plan) is designed to outperform on Core Web Vitals, structured data, and freshness.
2. **CPC**: expat-tax/legal cluster sits near the legal-services benchmark (~$6.75 avg; FBAR-specific terms commonly cited $8–15) → strong AdSense RPM for informational traffic.
3. **Demand**: 252 distinct long-tail suggestions from 8 seeds (floor estimate — question forms alone are dense: deadline, penalty, joint account, signature authority, reasonable cause, delinquent filing, 8938-vs-FBAR).
4. **Evergreen + recurring**: annual deadline cycle re-triggers demand every Q1–Q2; rules change yearly (limits, inflation adjustments) → freshness moat for a maintained site.
5. **THE content gap (live today)**: **On July 1, 2026 the IRS silently removed the Delinquent FBAR Submission Procedures (DFSP) page** (confirmed by [Fredrikson & Byron](https://www.fredlaw.com/lets-talk-about-tax/irs-just-deleted-the-delinquent-fbar-filing-procedures-now-what), JD Supra, Kaufman Rossin). Most incumbent "how to file FBAR late" pages still describe DFSP as current procedure. A new site that documents the post-DFSP reality (file directly via FinCEN BSA E-Filing; reasonable-cause defense; recall that FBAR always went to FinCEN, not IRS) is *more current than every stale incumbent* — a genuine ranking opening.
6. **AdSense-safe**: informational tax explainers with IRS/FinCEN citations and disclaimers are a standard, approvable content category (YMYL handled with citations per plan §4).

## 4. Verified fact base for content (every load-bearing number checked 2026-09-12)

- FBAR = FinCEN Form 114, filed electronically via **FinCEN BSA E-Filing** (never with IRS, never with Form 1040).
- 2026 deadline (for 2025 accounts): **April 15, 2026**, with **automatic extension to October 15, 2026** — no request needed ([IRS](https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar), FinCEN).
- Filers with **signature authority only** (non-owner): extended deadline **April 15, 2027** ([KPMG](https://kpmg.com/us/en/taxnewsflash/news/2025/12/fbar-filings-extended-deadline-april-2027-individuals-signature-authority.html)).
- Threshold: aggregate value of foreign financial accounts **> $10,000 at any time during the calendar year**.
- 2026 penalty maximums (inflation-adjusted, per practitioner sources incl. [Taxes for Expats](https://www.taxesforexpats.com/articles/fbar-fatca/fbar-penalties.html)): **non-willful up to $16,536 per annual report** (enforcement practice: per form, not per account); **willful: greater of $165,353 or 50% of account balance**, per account per year.
- **DFSP removed July 1, 2026**; FinCEN direct e-filing unchanged; reasonable-cause defense (31 U.S.C. § 5321) and other relief avenues remain.
- Record-keeping: **5 years** from filing date.

## 5. Site plan (hub-and-spoke, 10 pages)

Hub: *FBAR Filing Guide 2026* → spokes: deadline guide · penalties · **filing late after DFSP ended** · FBAR vs 8938 · joint accounts & signature authority · reasonable-cause statement · record-keeping · aggregation rules · FinCEN 114 e-filing walkthrough. Brand: **Expat Tax Desk**. All facts cited to IRS/FinCEN pages; explicit not-advice disclaimer (also required by AdSense policy).
