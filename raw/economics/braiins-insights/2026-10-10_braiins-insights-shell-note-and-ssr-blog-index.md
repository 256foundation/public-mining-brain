# Braiins Insights — Dashboard/Blog Shell Note + SSR Blog Discovery & Index

> Registry ID: braiins-insights
> Source: https://insights.braiins.com (+ https://learn.braiins.com/blog, + discovered SSR blog https://braiins.com/blog)
> Collected: 2026-10-10
> Published: n/d (index + shell note)
> Posture: extract
> As-Of: 2026-10-10

## SHELL NOTE (dashboard + blog host are JS-only)

- `https://insights.braiins.com/blog` → 301/redirect → `https://learn.braiins.com/blog`, HTTP 200, **1,613 bytes**, React SPA shell: `<div id="app"></div>` with `app.8da3b47fd6f46d10.js`; build meta `hash="8da3b47fd6f46d10" date="2026-06-01_13:59:15"`. Zero SSR article content. `<title>Bitcoin Mining Dashboard | Braiins</title>`.
- `https://learn.braiins.com/sitemap.xml` and `https://insights.braiins.com/sitemap.xml` both return the same SPA shell (SPA fallback), so no server-side URL discovery possible there.
- Dashboard itself NOT rendered per instructions (JS shell).

## Discovery: SSR mining blog lives at braiins.com/blog

`https://braiins.com/blog` → HTTP 200, 39,472 B, fully server-rendered (WordPress-style). Nav confirms the product tie-in: "Bitcoin Mining Dashboard — Live and historical bitcoin mining data", "Bitcoin Charts — Track hashrate, hashprice, difficulty & more", "Bitcoin Profitability Calculator — Forecast margins and cash flow with precision".

**Hashprice widget gap:** Braiins SSR header carries a hashprice stat labeled `USD/TH/Day` (data-stats="target" with arrow-up/arrow-down icons), but its numeric value is JS-populated — only a `1.53%` change string appears in static HTML. Value not capturable via curl; recorded as n/d.

## Blog index (SSR slugs captured 2026-10-10, most relevant to mining economics)

- /blog/firmware-optimization-gda-40mw-case-study — "40% Higher Hashrate on Identical Hardware: Firmware Optimization at 40MW Scale with GDA" (Published 3.3.2026 = 2026-03-03)
- /blog/tuv-sud-testing-how-braiins-os-delivers-more-efficient-bitcoin-mining — "TÜV SÜD Testing: How Braiins OS Delivers More Efficient Bitcoin Mining" (Published 1.4.2025 = 2025-04-01)
- /blog/maximizing-btc-mining-profitability-with-strike-price-curtailment-in-braiins-manager-cloud-platform
- /blog/braiins-manager-price-adapt-automated-bitcoin-mining-profitability-optimization — "Price Adapt: Automated Bitcoin Mining Profitability Optimization with Braiins Manager"
- /blog/smarter-clock-speed-management-for-bitcoin-miners-maximize-roi-minimize-waste
- /blog/braiins-enel-partnership-introducing-mining-energy-intelligence — "Enel Partnership: Introducing Energy Intelligence - Make Your Flexible Bitcoin Mining Load Pay"
- /blog/how-to-prepare-bitcoin-miners-for-hot-weather · /blog/local-vs-cloud-mining-tools · /blog/braiins-deck-the-bitcoin-clock-for-traders-and-miners

Extracts of the two highest-signal posts (GDA 40MW case study; TÜV SÜD efficiency) in companion files. The blog index page itself does not render dates per item in SSR; dates taken from each post's "Published" line and metadata.
