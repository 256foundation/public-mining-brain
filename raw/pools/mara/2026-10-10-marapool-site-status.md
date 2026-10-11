# MARA Pool — marapool.com site status (pool site down; redirects to corporate home)

> Source: http://marapool.com (→ https://www.mara.com/), https://www.mara.com/, https://www.mara.com/sitemap.xml
> Collected: 2026-10-10
> Published: Unknown
> Registry ID: mara-pool

---

MARA Pool is the in-house mining pool of MARA Holdings, Inc. (NASDAQ: MARA; formerly Marathon Digital Holdings). This capture documents the state of the pool's dedicated web presence on 2026-10-10.

## marapool.com is currently broken / decommissioned as a pool site

- `https://marapool.com` and `https://www.marapool.com` resolve (AWS Global Accelerator addresses, e.g. 3.33.152.147 / 15.197.142.173 / 3.33.251.168) but the **TLS handshake fails** on 443: LibreSSL reports `tlsv1 alert internal error` from the server (reproduced repeatedly on collection day).
- Plain `http://marapool.com` answers **301 → https://www.mara.com/** — i.e. the former pool domain now forwards to the corporate marketing site.
- The corporate site `www.mara.com` ("MARA Holdings Inc. — Advancing the world's energy systems… energy, compute, and digital capital") carries **no pool product page**: the sitemap.xml lists marafw (firmware) pages, about-us, operations, insights, posts, etc. — **zero URLs containing "pool"**.
- Historical note: the 2021 launch press release directed prospective members to "visit marapool.com" to apply — that funnel no longer exists at this domain.

## What the corporate home does say (2026-10-10)

- Positioning: "MARA operates at the intersection of three of the fastest-growing industries on Earth: energy, compute, and digital capital." (Company emphasis has shifted to energy/compute/AI — e.g. EXAION majority-stake coverage on the home page.)
- MARA's investor-relations site (ir.mara.com) remains the live first-party source on the pool — see the companion capture of MARA's own MaraPool statements.

## Fee / payout / custody / SV2 disclosure status

- **Fee %:** not disclosed anywhere reachable (dedicated pool site is down; corporate site has no pool page; checked 2026-10-10).
- **Payout scheme / threshold / cadence:** not disclosed on any reachable MARA-controlled page.
- **Custody / who can join:** see companion capture — 2021–2025 press statements describe an application-based pool for North American miners with NYDIG member services; current join path is not published.
- **SV2/DATUM:** not mentioned on any reachable page.
- **Status/incident page:** none found.
