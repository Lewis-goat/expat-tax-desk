#!/usr/bin/env python3
"""Phase A+B+C niche research: suggestion harvest -> SERP composition -> scoring.
Outputs research/suggestions.json and research/scores.json. Free sources only:
Google suggest API + Bing HTML SERP. No keys, no paid tools."""
import json, re, time, random, base64, urllib.parse, urllib.request, pathlib

HERE = pathlib.Path(__file__).parent
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"}

NICHES = {
    "A_expat_tax": {
        "seeds": ["fbar filing", "fbar penalty", "fatca reporting", "form 8938", "foreign tax credit",
                   "fbar extension", "reporting foreign bank account", "fbar married filing jointly"],
        "cpc_band": 9.0, "evergreen": 0.9, "ymyl": 0.5,
    },
    "B_retirement_mechanics": {
        "seeds": ["backdoor roth", "mega backdoor roth", "401k rollover rules", "roth ira withdrawal rules",
                   "solo 401k", "roth conversion taxes", "401k early withdrawal penalty", "required minimum distribution"],
        "cpc_band": 6.0, "evergreen": 0.85, "ymyl": 0.7,
    },
    "C_accounting_software": {
        "seeds": ["quickbooks error 6000", "quickbooks won't open", "quickbooks payroll update error",
                   "quickbooks error ps033", "quickbooks error 3371", "quickbooks multi user mode not working"],
        "cpc_band": 3.0, "evergreen": 0.6, "ymyl": 0.1,
    },
    "D_career_licensing": {
        "seeds": ["how to become a notary in", "electrician license requirements", "hvac certification cost",
                   "how long to become a plumber", "cna certification requirements", "real estate license cost"],
        "cpc_band": 2.5, "evergreen": 0.8, "ymyl": 0.2,
    },
    "E_insurance_claims": {
        "seeds": ["does renters insurance cover", "does homeowners insurance cover mold",
                   "umbrella insurance cost", "water damage claim denied", "insurance claim adjuster secrets",
                   "does car insurance cover"],
        "cpc_band": 12.0, "evergreen": 0.85, "ymyl": 0.8,
    },
    "F_german_finance": {
        "seeds": ["tagesgeld vergleich", "etf sparplan einsteiger", "depot eröffnen vergleich",
                   "krankenversicherung vergleich", "altersvorsorge", "steuererklärung kapitalerträge"],
        "cpc_band": 2.0, "evergreen": 0.8, "ymyl": 0.6, "hl": "de", "gl": "de",
    },
}

FORUMS = ("reddit.com", "quora.com", "stackexchange.com", "stackexchange", "bogleheads.org",
          "community.intuit.com", "superuser.com", "money.stackexchange", "gutefrage.net")
BRANDS = ("irs.gov", "intuit.com", "turbotax", "investopedia.com", "nerdwallet.com", "bankrate.com",
          "fool.com", "forbes.com", "cnbc.com", "smartasset.com", "thebalancemoney.com", "kiplinger.com",
          "schwab.com", "fidelity.com", "vanguard.com", "freetaxusa", "hrblock", "jacksonhewitt",
          "nytimes.com", "marketwatch.com", "businessinsider.com", "yahoo.com", "aol.com", "msn.com",
          "geico.com", "statefarm.com", "allstate.com", "progressive.com", "policygenius.com",
          "thezebra.com", "insurance.com", "nerdwallet", "bankofamerica.com", "chase.com", "wellsfargo",
          "indeed.com", "zippia.com", "coursera.org", "udemy.com", "monster.com", "ziprecruiter.com",
          "bls.gov", "sba.gov", "usa.gov", "sparkrental", "fitsmallbusiness.com", "quickbooks.intuit",
          "finanztip.de", "check24.de", "verivox.de", "focus.de", "chip.de", "stiftung-warentest.de",
          "handelsblatt.com", "sueddeutsche.de", "zeit.de", "spiegel.de", "comdirect.de", "ing.de",
          "consorsbank", "traderepublic", "scalable.capital", "justtrade", "getquin", "financefwd",
          "deutsche-bank", "sparkasse", "volksbank", "commerzbank", "taxfix.de", "wundertax.de",
          "smartbroker", "onvista-bank", "onvista.de", "finanzen.net", "boerse-online.de", "deraktionaer.de",
          "wallstreet-online.de", "börse", "aktiencheck", "comparecamp", "merchantmaverick",
          "softwareadvice.com", "g2.com", "capterra.com", "pcmag.com", "techradar.com", "zapier.com")

def get(url, timeout=15):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "ignore")

def suggestions(seed, hl="en", gl="US"):
    out = set()
    for suffix in ["", " a", " b", " c", " d", " e", " f", " g", " h", " how", " why", " best",
                   " can", " does", " is", " vs", " without", " deadline", " penalty", " calculator", " 2026"]:
        q = f"{seed}{suffix}".strip()
        url = ("https://suggestqueries.google.com/complete/search?client=firefox&hl={hl}&gl={gl}&q="
               + urllib.parse.quote(q))
        try:
            data = json.loads(get(url))
            for s in data[1]:
                if isinstance(s, str): out.add(s)
        except Exception:
            pass
        time.sleep(0.15 + random.random() * 0.2)
    return sorted(out)

def bserp(query):
    url = "https://www.bing.com/search?q=" + urllib.parse.quote(query) + "&count=15&mkt=en-US"
    html = get(url)
    results = []
    for block in re.findall(r'<li class="b_algo".*?</li>', html, re.S):
        m = re.search(r'<h2[^>]*><a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', block, re.S)
        if not m: continue
        href, title = m.group(1), re.sub(r"<[^>]+>", "", m.group(2)).strip()
        real = href
        mu = re.search(r'[?&]u=a1([A-Za-z0-9+/=]+)', href)
        if mu:
            try:
                real = base64.b64decode(mu.group(1) + "=" * (-len(mu.group(1)) % 4)).decode("utf-8", "ignore")
            except Exception: real = href
        dom = urllib.parse.urlparse(real).netloc.replace("www.", "")
        results.append({"title": title, "url": real, "domain": dom})
    time.sleep(1.2 + random.random() * 0.8)
    return results

def classify(dom):
    d = dom.lower()
    if d.endswith(".gov") or d.endswith(".edu"): return "gov"
    if any(f in d for f in FORUMS): return "forum"
    if any(b in d for b in BRANDS): return "brand"
    return "niche"

def main():
    suggestions_out, serp_out = {}, {}
    for nid, cfg in NICHES.items():
        hl, gl = cfg.get("hl", "en"), cfg.get("gl", "US")
        pool = set()
        for seed in cfg["seeds"]:
            pool.update(suggestions(seed, hl, gl))
        pool = {p for p in pool if len(p) > len(seed)}  # drop pure echoes
        suggestions_out[nid] = sorted(pool)
        # pick representative sample: seed heads + question forms + newest-year forms
        sample = list(cfg["seeds"])
        qs = sorted((s for s in pool if s.lower().startswith(("how", "why", "can", "does", "is", "what"))),
                    key=lambda s: -len(s))[:3]
        yr = sorted((s for s in pool if "2026" in s or "2025" in s))[:2]
        long = sorted((s for s in pool if 4 <= len(s.split()) <= 9), key=lambda s: -len(s))[:3]
        sample += qs + yr + long
        sample = list(dict.fromkeys(sample))[:11]
        serp_out[nid] = {}
        for q in sample:
            try:
                res = bserp(q)
            except Exception as e:
                res = []
            for r in res: r["class"] = classify(r["domain"])
            serp_out[nid][q] = res
            print(f"{nid} | {q[:60]:<60} -> {len(res)} results", flush=True)
        (HERE / "suggestions.json").write_text(json.dumps(suggestions_out, indent=1, ensure_ascii=False))
        (HERE / "serps_raw.json").write_text(json.dumps(serp_out, indent=1, ensure_ascii=False))

    scores = {}
    for nid, queries in serp_out.items():
        per_q_win, comp = [], {"gov": 0, "forum": 0, "brand": 0, "niche": 0}
        n_res = 0
        for q, res in queries.items():
            if not res: continue
            n_res += len(res)
            for r in res: comp[r["class"]] += 1
            unbeatable = sum(1 for r in res if r["class"] in ("brand", "gov"))
            per_q_win.append(1 - unbeatable / len(res))
        share = {k: v / n_res if n_res else 0 for k, v in comp.items()}
        win = sum(per_q_win) / len(per_q_win) if per_q_win else 0
        cfg = NICHES[nid]
        demand = min(len(suggestions_out[nid]) / 60, 1.0)
        score = round(100 * (0.35 * win + 0.30 * min(cfg["cpc_band"] / 15, 1.0)
                             + 0.15 * demand + 0.10 * cfg["evergreen"] + 0.10 * (1 - cfg["ymyl"])), 1)
        scores[nid] = {"score": score, "winnability": round(win, 3),
                       "queries_above_gate": sum(1 for w in per_q_win if w >= 0.5),
                       "n_queries": len(per_q_win), "composition_share": {k: round(v, 2) for k, v in share.items()},
                       "n_suggestions": len(suggestions_out[nid]), "cpc_band": cfg["cpc_band"],
                       "evergreen": cfg["evergreen"], "ymyl_risk": cfg["ymyl"]}
    (HERE / "scores.json").write_text(json.dumps(scores, indent=1))
    print(json.dumps(scores, indent=1))

if __name__ == "__main__":
    main()
