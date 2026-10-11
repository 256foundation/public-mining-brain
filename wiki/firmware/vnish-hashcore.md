# Vnish → HashCore (the rebrand)

> Sources: vnish.com + hashcore.com + docs.hashcore.com (all SSR/llms routes, captured 2026-10-10); Cambridge DMIR 2025 for installed-base share
> Raw: [vnish.com home](../../raw/firmware/vnish-hashcore/vnish-com-home.md); [hashcore.com home](../../raw/firmware/vnish-hashcore/hashcore-com-home.md); [hashcore.com/firmware](../../raw/firmware/vnish-hashcore/hashcore-com-firmware.md); [hashcore.com/news](../../raw/firmware/vnish-hashcore/hashcore-com-news.md); [docs catalog (llms.txt)](../../raw/firmware/vnish-hashcore/docs-hashcore-llms.txt); [Firmware description](../../raw/firmware/vnish-hashcore/docs-firmware-description.md); [Key features](../../raw/firmware/vnish-hashcore/docs-firmware-key-features.md); [Miner support](../../raw/firmware/vnish-hashcore/docs-firmware-miner-support.md); [Web-UI mining/tuning](../../raw/firmware/vnish-hashcore/docs-firmware-mining-tuning.md); [Rebrand evidence chain](../../raw/firmware/vnish-hashcore/docs-rebrand-evidence.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

## What actually happened: an umbrella rebrand, not a migration

Vnish did **not** move domains. Both sites run in parallel: vnish.com (HTTP 200, nginx, still fully VNISH-branded, footer "© Vnish 2026") and hashcore.com (HTTP 200, Cloudflare). There is no redirect from one to the other, and **no rebrand announcement blog post exists** — `/blog` 404s on both sites; hashcore.com/news holds only product release notes.

The rename is documented in the product's own release notes (Pulse `0.8.0-alpha`):

> Firmware Provider — "developer name Vnish has been universally replaced with "HashCore""; "The version name (e.g., Vnish 1.3.7) remains unchanged."

Supporting verbatim evidence, all in the [rebrand evidence chain](../../raw/firmware/vnish-hashcore/docs-rebrand-evidence.md):

- Pulse `0.7.0-alpha` note: "Provider "Vnish" renamed to HashCore".
- FAQ/support copy: "HashCore firmware (formerly Vnish)".
- Docs self-identification: "Vnish by Hashcore — an alternative firmware with an Auto-tune function".
- hashcore.com marketing keeps the multi-brand history in view: "legendary firmware for Bitmain ASIC miners, widely known under various brands and also through partner networks"; /firmware — "developed by HashCore FZ-LLC, widely recognized in the market under various brands".
- Toolkit docs keep dual naming ("Cloning Devices (Hashcore/Vnish)").
- Corporate identity: HashCore FZ-LLC; site evolution timeline running "Q1 2019 — ASIC Custom Firmware" to "Q4 2025 — HashCore Ecosystem — Firmware, Toolkit, Proxy, Pulse, Board"; "Behind HashCore is a team of experts with over 7 years of experience creating leading mining technologies".

Practical consequence for the wiki and for tooling: the **firmware is still Vnish** — same product, version line unchanged — while the vendor brand is HashCore. Community references to "Vnish" (e.g., the field notes in [Heater Firmware & Power Control](heater-firmware-and-power-control.md)) remain accurate for behavior; vendor-facing references should say HashCore.

## The device-count claims, verified at capture

The "1.5M+ devices" shorthand does **not** appear verbatim anywhere. The actual claim text, copied at capture:

- **vnish.com hero stat tile: "1.5 Million Devices"** — a JS-animated counter hardcoded to end at "1.5" (in `/_nuxt/o5l9FJTb.js`; SSR shows placeholder 0.0). It sits next to "10 Years of Experience" and "Trusted 26,4% of mining market" / "300 Professional Miners", with an awards block: "#1 Firmware Provider – 26.4% Global Market Share — Cambridge Research 2025. Independent analysis confirms VNISH as the most widely used third-party ASIC firmware worldwide" — no sentence-form device claim on the page.
- **hashcore.com hero tile: "600,000+ Devices on HashCore"** (i18n `en.hero.blocks[0].upper = "600,000+"`).
- **hashcore.com/firmware: "400,000+ Devices Worldwide"**.
- Pulse marketing: "monitor and manage up to 1 million devices from any browser, free during Alpha" / "1M + Global Scale".
- Toolkit page: "50,000+ Managed devices" and "150+ Supported models".

> **Status: Disputed** — device counts, vendor self-claims (unreconciled)
> "1.5 Million Devices" (vnish.com tile) vs "600,000+ Devices on HashCore" vs "400,000+ Devices Worldwide" (firmware page). The three numbers describe overlapping-but-undefined populations (all-time firmware installs vs current HashCore-managed vs firmware-page metric) and are not reconciled anywhere on the vendor's own properties. The handoff's "1.5M+ devices" phrasing does not exist at capture time — nearest verbatim is the "1.5 Million Devices" tile. Cite the specific tile, never the shorthand.
> Corroboration: Cambridge DMIR 2025 puts Vnish at 26.4% of surveyed fleet firmware ([DMIR extract](../../raw/economics/cambridge-report/dmir-2025-extract.md), p.53) — consistent in spirit with the "26.4% Global Market Share" claim both sides make, but a survey figure, not a device count.

## Versions (2026-10-10)

- **Firmware 1.3.7** is current — vnish.com changelog "Firmware Update v1.3.7 - Changelog" (Z15 Pro Equihash support, manual frequency/voltage control, CVitek auto-start; Z15 Pro autotune promised in v1.3.8); hashcore news: "HashCore Toolkit 1.7.5 introduces support for Antminer Z15 Pro (Equihash / ZEC) alongside firmware 1.3.7".
- The handoff's "firmware v1.2.7" is stale — 1.2.7 survives in docs only as an install-method threshold ("Main Board Types and Firmware Installation Methods starting from version 1.2.7").
- **Toolkit v1.7.5** (3 Oct 2026, "HashCore Toolkit v1.7.5 Required" banner on vnish.com); 1.7.0 was April 2026 — the handoff's "toolkit 1.7.0" is stale.
- **Proxy v1.0.0; Pulse v1.0.0-alpha3** (header chips on every hashcore.com page).

## Coverage and fees

- vnish.com FAQ: "supported model list, which currently includes 23 Antminer x19 series modifications"; devfee "2–2.8%" (homepage: "Firmware Vnish for Bitmain with a 2.8% devfee"); new in 1.3.7: Antminer Z15 Pro (Equihash/ZEC) + CVitek control boards auto-start.
- hashcore.com/firmware claims "100+ Models ASICs Supported"; docs Pulse vendor table: Bitmain (Antminer S/T/L/D/Z), MicroBT (Whatsminer M-series), Canaan (Avalon), Innosilicon (T/A), plus "devices running HashCore firmware (formerly Vnish)"; Toolkit claims "150+ Supported models" on Windows/Mac/Linux/Android.
- Gap: the docs miner-support page's model table is a JS component (`<miner-models-showcase>`) — empty in raw markdown (recorded in the capture).
- Docs posture: docs.hashcore.com is Mintlify with a working `llms.txt`; key pages captured via `/raw/en/...md` routes (intermittent Cloudflare 429 — retry with Referer; logged in the report).

## Dev-fee server dependence (security context)

The Vnish dev-fee/license server outage that throttled miners (documented from POD256 e083/e107/e124) predates the rebrand; the HashCore rename does not change the dependency — see [Mining Firmware Security](../industry/mining-firmware-security.md). Braiins' equivalent mechanics are on [Braiins OS](braiins-os.md) (hourly license renewal, 95% hash-rate penalty on failed verification).

## See Also

- [Braiins OS](braiins-os.md) and [LuxOS](luxos.md) — the other closed aftermarket firmwares
- [Heater Firmware & Power Control](heater-firmware-and-power-control.md) — Vnish field section (thermal modes, toolbox, lookalike-site caution)
- [Mining Firmware Security](../industry/mining-firmware-security.md) — dev-fee server outage history
