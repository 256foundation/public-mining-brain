# A9 Firmware fetch report — vnish-site, cgminer-repo, bfgminer-repo

> Collected: 2026-10-10 by fetch subagent (phase A9). All captures under `raw/firmware/vnish-hashcore/` (Registry ID: `vnish-site`) and `raw/firmware/legacy-miners/` (`cgminer-repo`, `bfgminer-repo`). Every capture file carries the standard header block.

## Files captured (13)

Under `raw/firmware/vnish-hashcore/` — all Registry ID **vnish-site**:

| File | Source (HTTP status) | What it is |
|---|---|---|
| `vnish-com-home.md` | https://vnish.com/ (200) | Full SSR text of vnish.com — still VNISH-branded; changelog block names "Hashcore Toolkit v1.7.5"; devices counter (JS) = 1.5 Million |
| `hashcore-com-home.md` | https://hashcore.com/ (200) | Full SSR text + exact i18n stat values (600,000+ Devices on HashCore; evolution timeline Q4 2017→Q4 2025) |
| `hashcore-com-firmware.md` | https://hashcore.com/firmware (200) | Firmware product page — "developed by HashCore FZ-LLC, widely recognized in the market under various brands"; 400,000+ Devices Worldwide |
| `hashcore-com-news.md` | https://hashcore.com/news (200) | News index: Toolkit 1.6.0→1.7.5 + Pulse alphas release notes; "alongside firmware 1.3.7" |
| `docs-hashcore-llms.txt` | https://docs.hashcore.com/llms.txt (200) | Full docs catalog, verbatim (Mintlify llms.txt path worked first try) |
| `docs-firmware-description.md` | docs.hashcore.com/raw/en/firmware/about/opisanie.md (200) | "Vnish by Hashcore — an alternative firmware with an Auto-tune function…" |
| `docs-firmware-key-features.md` | docs.hashcore.com/raw/en/firmware/about/key-features.md (200) | Key features incl. Power Management bullet |
| `docs-firmware-miner-support.md` | docs.hashcore.com/raw/en/firmware/about/miner-support.md (200) | Miner-support page (model list is a JS component; see Parks) |
| `docs-firmware-mining-tuning.md` | docs.hashcore.com/raw/en/firmware/obzor-veb-interfeysa/mining.md (200) | Web-UI Mining page: Pools, Cooling (Auto/Manual/Immersion), Performance presets, Auto-tune — the tuning/power-management page |
| `docs-rebrand-evidence.md` | multiple | Curated VERBATIM rebrand evidence chain (redirects, brand statements, device-count claim text, versions) |
| `_REPORT.md` | — | This report |

Under `raw/firmware/legacy-miners/`:

| File | Source (HTTP status) | Registry ID |
|---|---|---|
| `cgminer-readme.md` | raw.githubusercontent.com/ckolivas/cgminer/master/README (200, 63,501 B) + GitHub API metadata | cgminer-repo |
| `bfgminer-readme.md` | raw.githubusercontent.com/luke-jr/bfgminer/master/README (200, 45,797 B) + GitHub API metadata | bfgminer-repo |

## Rebrand evidence chain (all verbatim quotes in `docs-rebrand-evidence.md`)

1. **Redirects:** vnish.com does **NOT** redirect to hashcore.com. `curl -sIL`: vnish.com → HTTP/2 200 (nginx/1.31.6, last-modified 2026-10-01); http→https and www→apex only; hashcore.com → 200 (Cloudflare, last-modified 2026-10-03); docs.hashcore.com → /en/ (200). Both sites run in parallel; vnish.com canonical stays `https://vnish.com/`, footer "© Vnish 2026".
2. **HashCore brand statements:** hashcore.com homepage — "Behind HashCore is a team of experts with over 7 years of experience…", "We created ASIC Custom Firmware — one of the most popular firmwares in the industry…"; evolution timeline "Q1 2019 ASIC Custom Firmware → Q4 2025 HashCore Ecosystem (Firmware, Toolkit, Proxy, Pulse, Board)"; /firmware — "professional custom firmware for ASIC miners, developed by HashCore FZ-LLC, **widely recognized in the market under various brands**"; homepage — "The legendary firmware for Bitmain ASIC miners, **widely known under various brands** and also through partner networks…".
3. **Rebrand named explicitly** in docs release notes: Pulse `0.8.0-alpha` — "**Firmware Provider** — developer name Vnish has been universally replaced with "HashCore". The version name (e.g., Vnish 1.3.7) remains unchanged."; Pulse `0.7.0-alpha` — "Provider "Vnish" renamed to HashCore"; FAQ/support — "HashCore firmware (**formerly Vnish**)"; docs self-ID — "**Vnish by Hashcore** — an alternative firmware with an Auto-tune function…"; Toolkit docs keep dual naming ("Cloning Devices (Hashcore/Vnish)").
4. **No rebrand announcement blog post exists** — vnish.com/blog and hashcore.com/blog both 404; hashcore.com/news contains only product release notes.

## Device-count claim — VERBATIM AT CAPTURE

The handoff phrase "1.5M+ devices" does **not** appear verbatim anywhere on either site. Actual claim text, copied at capture:

- **vnish.com hero stat** → renders **"1.5 Million Devices"** (label "Million Devices" + JS-animated value ending at "1.5"; hardcoded in `/_nuxt/o5l9FJTb.js`: `case"devices":c($,["0.0","0.1",…,"1.5"],Q*1.1)`; SSR shows placeholder 0.0). No sentence form exists — it's a stat tile, next to "10 Years of Experience" and "Trusted 26,4% of mining market" / "300 Professional Miners". Awards block: "#1 Firmware Provider – 26.4% Global Market Share — Cambridge Research 2025. Independent analysis confirms VNISH as the most widely used third-party ASIC firmware worldwide."
- **hashcore.com** → hero tile **"600,000+ Devices on HashCore"** (i18n `en.hero.blocks[0].upper = "600,000+"`); firmware page **"400,000+ Devices Worldwide"**; Toolkit page "50,000+ Managed devices / 150+ Supported models"; Pulse "monitor and manage up to 1 million devices from any browser, free during Alpha" and "1M + Global Scale".

## Versions found (2026-10-10)

- **Firmware: 1.3.7** (current) — vnish.com changelog "Firmware Update v1.3.7 - Changelog" (Z15 Pro Equihash support, manual frequency/voltage control, CVitek auto-start; Z15 Pro autotune promised in v1.3.8); news: "HashCore Toolkit 1.7.5 introduces support for Antminer Z15 Pro (Equihash / ZEC) **alongside firmware 1.3.7**". Handoff's "v1.2.7" is stale — 1.2.7 survives in docs only as an install-method threshold ("Main Board Types and Firmware Installation Methods starting from version 1.2.7").
- **Toolkit: v1.7.5** (3 Oct 2026; "HashCore Toolkit v1.7.5 Required" banner on vnish.com). 1.7.0 = 13 Apr 2026 (iOS). Handoff's "toolkit 1.7.0" is stale.
- **Proxy v1.0.0; Pulse v1.0.0-alpha3** (header chips on every hashcore.com page).

## Supported-miner coverage

- vnish.com FAQ: "supported model list… currently includes 23 Antminer x19 series modifications"; devfee "2–2.8%" (homepage: "Firmware Vnish for Bitmain with a 2.8% devfee"); new: Antminer Z15 Pro (Equihash/ZEC) + CVitek control boards auto-start.
- hashcore.com/firmware: "100+ Models ASICs Supported"; docs Pulse supported-vendors table: Bitmain (Antminer S/T/L/D/Z), MicroBT (Whatsminer M-series), Canaan (Avalon), Innosilicon (T/A), plus "devices running HashCore firmware (formerly Vnish)"; Pulse also claims Whatsminer control. Toolkit: "150+ Supported models", Windows/Mac/Linux/Android.
- Docs miner-support page body is a JS component (`<miner-models-showcase>`) — the model table itself did not render in the raw markdown (see Parks).

## cgminer / bfgminer activity status

- **cgminer (ckolivas/cgminer): ARCHIVED / DORMANT.** Repo archived on GitHub; last master commit `b8491c6` 2018-12-06; pushed_at 2020-05-27; no GitHub Releases (latest tag v4.11.1); description "ASIC and FPGA miner in c for bitcoin". The "legacy/active-again" framing in the handoff is outdated — it is now an archived legacy reference.
- **bfgminer (luke-jr/bfgminer): DORMANT, not archived.** Default branch is `bfgminer` (no `master` branch in API; raw /master/README still resolves); last default-branch commit `866fd36` 2021-10-26; pushed_at 2023-06-18; no GitHub Releases; 209 tags, highest `bfgminer-5.5.0`.

## HTTP status log (browser UA "Chrome/126.0", --compressed)

200: vnish.com (HEAD+GET), hashcore.com, /firmware, /toolkit, /pulse, /news, docs.hashcore.com/llms.txt, /llms-full.txt, all 6 `/raw/en/...md` pages, hashcore.com `/_i18n/e5a19679/en/messages.json` (200 on retry — first attempt + first browser fetch hit Cloudflare 429/challenge), raw READMEs (both). 404: cgminer README.txt/.rdoc, bfgminer README.rst/.txt, GitHub releases/latest (both repos), /blog on both sites. VNISH redirect chain: no hashcore redirect (www→apex only).

## Parks / gaps

1. **docs `/raw/` behind Cloudflare intermittently** — first `/_i18n/...` curl got a challenge page; succeeded on retry with Referer. If re-crawling docs.hashcore.com programmatically, add backoff.
2. **Miner-support model table** renders via JS component; raw markdown has an empty `<miner-models-showcase>`. Full supported-miner matrix would need the rendered docs page (browser) or the llms-full.txt section (searchable, 2.2 MB, not captured whole to respect file cap).
3. **llms-full.txt (2.2 MB) not captured whole** — catalog + 6 key pages captured instead.
4. **"1.5M+" claim**: not present verbatim on any captured page; nearest verbatim claims recorded above ("1.5 Million Devices" tile / "600,000+ Devices on HashCore"). If the wiki needs a sentence-form claim, none exists at capture time.
5. Toolkit/Pulse full product pages (`/toolkit`, `/pulse`) fetched and skimmed but not saved as files (file cap); key stats are in `hashcore-com-home.md` capture notes.
