# Vnish → HashCore rebrand — verbatim evidence chain

> Registry ID: vnish-site
> Source: multiple (per-quote Source lines inside)
> Collected: 2026-10-10
> Published: n/d
> Posture: verbatim
> As-Of: 2026-10-10


All quotes copied exactly from linked sources on 2026-10-10.

---

## 1. Redirect chain (curl -sIL, 2026-10-10)

```
https://vnish.com      → HTTP/2 200 (nginx/1.31.6, content-length 139010, last-modified 2026-10-01) — NO redirect to hashcore.com
http://vnish.com       → http://vnish.com/ [200] (no scheme redirect beyond trailing slash)
https://www.vnish.com  → https://vnish.com/ [200] (apex canonicalization only)
https://hashcore.com   → HTTP/2 200 (cloudflare, last-modified 2026-10-03)
https://docs.hashcore.com → https://docs.hashcore.com/en/ [200]
```

Key fact: **vnish.com does not redirect to hashcore.com.** Both sites operate in parallel — vnish.com remains fully VNISH-branded (canonical `<link rel="canonical" href="https://vnish.com/">`, title "VNISH Official Firmware Developer for Antminer ASICs", footer "© Vnish 2026 - All rights reserved", support@vnish.com), while hashcore.com presents the same products under the HashCore brand ("© 2024-2026 HashCore FZ-LLC").

## 2. Brand-lineage statements on hashcore.com (verbatim)

Homepage "Mining Technology Leaders" section:

> "Behind HashCore is a team of experts with over 7 years of experience creating leading mining technologies"
> "We created ASIC Custom Firmware — one of the most popular firmwares in the industry, and continue setting new standards through the HashCore ecosystem."

Homepage "HashCore Evolution" timeline (i18n `en.about.evolution`, rendered on the homepage):

> Q4 2017 — Anthill Monitoring — Mining farm monitoring system
> Q1 2019 — ASIC Custom Firmware — Breakthrough firmware for ASIC miners
> Q3 2022 — Expansion — Global expansion across 5 continents
> Q4 2025 — HashCore Ecosystem — Firmware, Toolkit, Proxy, Pulse, Board

hashcore.com/firmware:

> "HashCore Firmware is a professional custom firmware for ASIC miners, developed by HashCore FZ-LLC, widely recognized in the market under various brands."

Homepage firmware section (i18n `en.firmware.desc`, with "various brands" highlighted in the rendered page):

> "The legendary firmware for Bitmain ASIC miners, widely known under various brands and also through partner networks, has rightfully become a leader in mining. It is the result of seven years of continuous development and improvement by the HashCore team."

Header product descriptions (every page): "HashCore Firmware — Legendary firmware for Bitmain ASIC miners", "HashCore Pulse — Enterprise solution for managing up to one million miners".

## 3. Rebrand named explicitly in docs.hashcore.com release notes (verbatim, from llms-full.txt)

Pulse release notes `0.8.0-alpha` (https://docs.hashcore.com/raw/en/pulse/whats-new/release-notes.md):

> "**Firmware Provider** — developer name Vnish has been universally replaced with "HashCore". The version name (e.g., Vnish 1.3.7) remains unchanged. Developer filter updated."

Pulse release notes `0.7.0-alpha`:

> "Provider "Vnish" renamed to HashCore, color coding corrected."

Pulse FAQ (https://docs.hashcore.com/raw/en/pulse/troubleshooting/faq.md):

> "Bitmain (Antminer), MicroBT (Whatsminer), Canaan (Avalon), Innosilicon devices, and devices running HashCore firmware (formerly Vnish) are supported."

Pulse "Supported Devices" table (llms-full.txt line ~4267):

> "| HashCore Firmware | Devices running HashCore firmware (formerly Vnish) |"

Firmware docs self-identification (https://docs.hashcore.com/raw/en/firmware/about/opisanie.md):

> "Vnish by Hashcore — an alternative firmware with an Auto-tune function, designed to optimize the performance of Bitmain Antminer ASIC miners."

Toolkit docs keep the dual name: "Cloning Devices (Hashcore/Vnish)", "Installing Vnish Firmware … install and update firmware (including Vnish)".

## 4. Device-count claim text — VERBATIM AT CAPTURE (2026-10-10)

The handoff phrase "1.5M+ devices" does **not** appear verbatim on either site. The actual claim text at capture:

vnish.com homepage hero stat (label + JS-animated value; final value 1.5 hardcoded in the site JS `/_nuxt/o5l9FJTb.js`: `case"devices":c($,["0.0","0.1",…,"1.5"],Q*1.1)`; SSR renders `data-metric="devices">0.0<` before hydration):

> "1.5 Million Devices"  — rendered as value **1.5** + label **Million Devices** (adjacent stat: "10 Years of Experience")

Accompanying vnish.com hero claims (verbatim): "The World's Leading Firmware for ASIC Miners" / "Trusted 26,4% of mining market" / "300 Professional Miners"; awards section: "#1 Firmware Provider – 26.4% Global Market Share — Cambridge Research 2025. Independent analysis confirms VNISH as the most widely used third-party ASIC firmware worldwide".

hashcore.com homepage hero stat (i18n `en.hero.blocks[0]`):

> "600,000+ Devices on HashCore - Scalability -"

hashcore.com/firmware hero (i18n `en.firmware-page.hero.blocks`):

> "Up to +50% Hashrate Increase" / "7+ Years of Development Experience" / "100+ Models ASICs Supported" / "400,000+ Devices Worldwide"

HashCore Toolkit page (i18n `en.toolkit-page`): "50,000+ Managed devices", "150+ Supported models"; toolkit-page.pulse-promo.desc verbatim: "Toolkit handles local farm operations. HashCore Pulse extends that control to the cloud: monitor and manage up to 1 million devices from any browser, free during Alpha."

HashCore Pulse: homepage header chip "Enterprise solution for managing up to one million miners"; homepage Pulse unit "1M + Global Scale — Monitoring millions of devices via a single panel".

Interpretation note for the wiki: "1.5M+ devices" is the vnish.com lifetime-deployment claim ("1.5 Million Devices", animated counter, no source sentence); hashcore.com's own counter claims "600,000+ Devices on HashCore" and the firmware product page "400,000+ Devices Worldwide". No sentence containing "1.5M" exists on the captured pages.

## 5. Versions found at capture (2026-10-10)

- Vnish/HashCore Firmware: **1.3.7** current (vnish.com changelog "Firmware Update v1.3.7 - Changelog"; news: "HashCore Toolkit 1.7.5 introduces support for Antminer Z15 Pro (Equihash / ZEC) alongside firmware 1.3.7"; docs example "Vnish 1.3.7"). v1.3.8 announced (Z15 Pro autotune). The handoff's "v1.2.7" is stale — 1.2.7 appears in docs only as an installation-method threshold ("Main Board Types and Firmware Installation Methods starting from version 1.2.7").
- HashCore Toolkit: **v1.7.5** (released 3 Oct 2026; "HashCore Toolkit v1.7.5 Required" banner on vnish.com). 1.7.0 was 13 Apr 2026 (iOS release).
- HashCore Proxy: **v1.0.0**. HashCore Pulse: **v1.0.0-alpha3** (10 Aug 2026).
