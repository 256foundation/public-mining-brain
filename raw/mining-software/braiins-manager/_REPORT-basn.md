# _REPORT-basn — A11 farm-management fetch: braiins-manager / awesome-miner / simplemining / nicehash

> Agent: fetch subagent (phase A11, farm management)
> Collected: 2026-10-10
> Scope: 9 capture files (braiins-manager 3, awesome-miner 2, simplemining 2, nicehash 2). Did not touch wiki/, scripts/, sources/, .agent/, foreman/ or luxor-commander/ dirs. No git commands.

## Files captured (9)

| # | File | Registry | Source URL | Posture | HTTP | Bytes |
|---|------|----------|-----------|---------|------|-------|
| 1 | raw/mining-software/braiins-manager/2026-10-10-braiins-com-manager-landing.md | braiins-manager | https://braiins.com/manager | verbatim (SSR text extract) | 200 | 52,977 |
| 2 | raw/mining-software/braiins-manager/2026-10-10-academy-braiins-manager-overview.md | braiins-manager | https://academy.braiins.com/braiins-manager/overview.md | verbatim (.md) | 200 | 2,494 |
| 3 | raw/mining-software/braiins-manager/2026-10-10-academy-braiins-manager-using-components.md | braiins-manager | https://academy.braiins.com/braiins-manager/using-components.md | verbatim (.md) | 200 | 1,399 |
| 4 | raw/mining-software/awesome-miner/2026-10-10-awesomeminer-home.md | awesome-miner | https://www.awesomeminer.com/ | extract | 200 | 52,099 |
| 5 | raw/mining-software/awesome-miner/2026-10-10-awesomeminer-signup-pricing.md | awesome-miner | https://www.awesomeminer.com/signup | extract | 200 | 44,105 |
| 6 | raw/mining-software/simplemining/2026-10-10-simplemining-home.md | simplemining | https://simplemining.net (→ /mining) | extract | 200 | 76,664 |
| 7 | raw/mining-software/simplemining/2026-10-10-simplemining-features.md | simplemining | https://simplemining.net/mining/features | extract | 200 | 35,468 |
| 8 | raw/mining-software/nicehash/2026-10-10-github-nicehashminer-readme.md | nicehash | https://raw.githubusercontent.com/NiceHash/NiceHashMiner/master/README.md | verbatim | 200 | 6,438 |
| 9 | raw/mining-software/nicehash/2026-10-10-github-nhos-readme.md | nicehash | https://raw.githubusercontent.com/NiceHash/NHOS/main/README.md | verbatim | 200 | 1,080 |

SSR assessment: braiins.com, academy.braiins.com (Rspress: serves /llms.txt + per-page .md), awesomeminer.com, simplemining.net — all fully SSR with content text in HTML. No JS-shell parks among captured sites. www.nicehash.com = JS shell (park, see below).

## Key facts (exact literal quotes → file)

### braiins-manager (Braiins Manager — ASIC farm/site management, SaaS + local Agent)
- Positioning: "Smart Fleet Management Automate. Optimize. Profit." / "Manage miners across every site, and automate fleet operations, power optimization, and energy market participation as conditions change." → file 1
- Scale claim: "Reliably managing 1+ GW across mining sites worldwide" → file 1
- Docs scale claim: "Easily manage thousands of devices with batch management, monitoring, automation, and issue tracking." → file 2
- Core feature set: "It provides **real-time monitoring**, **batch management**, **curtailment solutions**, **automation** of routine tasks, and **energy reporting**" → file 2
- Mixed fleet / pool config at scale: "Monitor and control diverse ASIC models, firmware and pool settings, even beyond bitcoin. Perfect for hosting providers with custom client power rates." → file 1; batch pool change: "Manage multiple miners on the [Workers page], allowing actions like restarting or changing pool settings." → file 3
- Profitability/energy: "Price Adapt … automatically keeps miners running at the most profitable power target based on energy prices" → files 1-3; curtailment + CSP/demand-response integration + strike price per miner model → file 3
- Monitoring cadence: dashboard "Data is refreshed **every 5 minutes**"; "Time-series data has a 20-minute delay for data freshness" (from /braiins-manager/dashboard.md, HTTP 200, 919 B — fetched, quoted in file 3 header note, not stored as separate file to respect the 2-3 file cap) → files 2/3
- Architecture: Agent installed locally ("The Agent collects real-time data from mining hardware and relays it to the Braiins Manager web application"); Agent platforms: "The Agent is compatible with Ubuntu and Debian Linux servers, as well as Windows 11 servers. However, Braiins recommends Ubuntu or Debian Linux for enhanced stability and reliability." → files 1, 2
- OS target: ASIC-centric ("supports altcoin miners, such as Icerivers and altcoin Antminers … its primary focus remains on Bitcoin miners"); hosting-client model (Providers vs Hosting Clients) with per-client power rates, energy reports, sitemap Groups/Racks → files 1, 2
- Pricing model: "Braiins Manager offers a free plan. However, for data centers requiring fast and knowledgeable support, there is a paid premium support plan." (1-month premium trial; pricing on their Pricing Page — not scraped, out of scope) → file 1
- Provenance note: formerly Krater — "I've been using Braiins Manager (formerly Krater) since its inception" (testimonial) → file 1
- Not folded away: product is alive and standalone (its own llms.txt docs tree /braiins-manager/* with ~36 pages incl. public-api.md, agent/*, workers/*); Braiins OS docs separately note batch management "with use of Braiins Toolbox, Braiins Manager, or other market-standard management solutions."

### awesome-miner (Windows central management; ASIC + GPU)
- Scale claim (verbatim): "Scalable up to 200,000 ASIC miners and 25,000 GPU/CPU miners" → file 4
- ASIC support: "A total of more than 200 ASIC miner models are supported." (Bitmain Antminer, Baikal, Canaan Avalon, Goldshell, Innosilicon, Obelisk, Whatsminer); managed "without installing any software on the device" → file 4
- Automation: "More than 30 different trigger conditions and more than 40 different actions are available"; Power Curtailment "based on the current electricity price, a signal from a power management service or a custom set of triggers" → file 4
- Profit switching: "Profit switching based on real time revenue and power consumption"; benchmark measures "hashrate and power usage for each" algorithm/software → file 4
- Firmware: optimized Antminer firmware for "S9, S9i, S9j, T9+, L3+, L3++, S17, S17+, T17, T17+, S19, T19, S21, T21, L7, L9"; "Significant performance increase for Antminer S17, S19 and S21" → file 4
- OS targets: Windows app; GPU miners on "either Windows or Linux" via "Awesome Miner Remote Agent"; built-in web interface; Client-Server multi-user; HTTP API + C# script engine → file 4
- Pricing (file 5): "The subscription price is $2 per miner and month. Save 25% with a Yearly subscription."; tiers: Monthly "$4 for 2 miners per month", Yearly "$36 for 2 miners per year", Antminer Firmware "2.8% mining fee" (L3+, L7, S9, S17, S19, S21, T9+, T17, T19, T21), free "up to 2 miners with limited features"; volume discounts 25+ 10% → 5000+ 75%. Free tier: "Awesome Miner can be used with limited features for up to 2 miners without a subscription."
- Pricing page note: no /pricing URL; tiers live on /signup; /upgrade is only a license-change form (HTTP 200, 32,180 B, captured as observation only). Cloud Services detail: /cloud HTTP 200, 32,669 B — web interface, multi-user, Telegram+SMS notifications, included with subscription (quoted in file 4 footer note).

### simplemining (GPU-miner Linux distro + farm management)
- Positioning: "Easy to use Plug&Play Linux Mining OS Platform for cryptocurrency GPU mining" → file 6
- OS target: GPU only (NVIDIA/AMD), Linux distro flashed to "empty 7+ GB pendrive/hdd/ssd drive"; storage: HDD/SSD/USB → file 6
- Farm management: "Batch management of your rigs. Execute commands on multiple rigs. Assign rigs to overclock and mining groups, set tags, reboot, reload, pause or power off."; alerts (missing GPU, reboots, temperature), Telegram notifications, sleep schedules, 1 year of historical stats, group OC/undervolt → files 6, 7
- Miners: phoenixminer, teamredminer, t-rex, lolminer, nbminer, gminer, nanominer + 11 more listed; "You can prepare any other Linux based miner and use it." → file 6
- Pricing tiers (per rig, billed monthly): "1 - 49 rigs 2.0$ / 50 - 99 rigs 1.8$ / 100 - 249 rigs 1.6$ / 250 - 499 rigs 1.4$ / 500 - 999 rigs 1.2$ / 1000 - 1999 rigs 1.0$ / 2000 - 4999 rigs 0.8$ / 5000+ rigs 0.5$"; free trial: "Test our services for FREE with one rig for 30 days!" → file 6
- Current images: stable SM-i073-6.1.57-3 (u20), NVIDIA-5000 stable SM-i088-6.9.12-6 (u22), beta SM-i090-6.18.20-1 (u22); operator: "Copyright © 2026 SimplePod.ai Sp. z o.o. Sp. k."; API docs: https://api.simplemining.net/docs → file 6

### nicehash (farm-management surfaces only)
- JS-shell park (recorded honestly): www.nicehash.com is a Vue SPA, empty `<div id="app"></div>` on every probed route — /miner (HTTP 200, 965 B), /nicehash-miner (HTTP 200, 964 B), /support/mining-help/nicehash-miner/what-is-nicehash-miner (HTTP 200, 962 B); noscript: "We're sorry but client doesn't work properly without JavaScript enabled." Sitemap (HTTP 200, 126,481 B, 2070 URLs) lists /nicehash-miner, /nhos-mining, /easymining, /firmware and NiceHash Rig Manager support articles (rig-management-card, how-to-manage-groups, what-is-power-mode, quickminer-profit-switching, etc.) — none SSR. Parked; substituted the two canonical GitHub surfaces below (both official NiceHash repos).
- NiceHash Miner (Windows auto-miner, profitability switching): "NiceHash Miner is an advanced auto-miner"; "automatic switching to most profitable cryptocurrency algorithm"; "Integrated support for Simple Multi-Algorithm. Always mine most profitable algorithm."; "Watch-feature - automatically restart miner if crashed or hanged" → file 8
- Profitability-switching config literals: "MinimumProfit | number | … will stop mining if the calculated profit falls below the set amount"; "SwitchProfitabilityThreshold | number | Threshold for algorithm switch. Lower this number is, faster switches will happen."; "KwhPrice | number | Set price for kWh, used for profit calculating."; "RigGroup | text | To identify the group your rig belongs to."; "WorkerName | text | To identify the computer on NiceHash web UI." → file 8
- OS target: "Windows 10 or newer operating system 64-bit" (CPU/GPU rig miner, not ASIC) → file 8
- NiceHash OS: "NiceHash OS is a minimal standalone Linux operating system containing everything you need to start mining crypto-currency efficiently." — README covers flash-drive imaging only (NiceHash Flash Tool / balenaEtcher / dd); rig management UI itself is the JS-only dashboard → file 9

## HTTP / status log
- 200 https://academy.braiins.com/llms.txt (5,686 B, text/plain)
- 200 https://braiins.com/manager (52,977 B, text/html, SSR)
- 200 https://academy.braiins.com/braiins-manager/overview.md (2,494 B, text/markdown)
- 200 https://academy.braiins.com/braiins-manager/using-components.md (1,399 B, text/markdown)
- 200 https://academy.braiins.com/braiins-manager/dashboard.md (919 B, text/markdown — fetched for quotes, not stored as file)
- 200 https://www.awesomeminer.com/ (52,099 B, SSR)
- 200 https://www.awesomeminer.com/upgrade (32,180 B, SSR — form only, no tiers)
- 200 https://www.awesomeminer.com/cloud (32,669 B, SSR)
- 200 https://www.awesomeminer.com/signup (44,105 B, SSR — pricing tiers)
- 200 https://simplemining.net → /mining (76,664 B, SSR)
- 200 https://simplemining.net/mining/features (35,468 B, SSR)
- 200 https://www.nicehash.com/sitemap.xml (126,481 B, 2070 URLs)
- 200 (shell) https://www.nicehash.com/miner 965 B; /nicehash-miner 964 B; /support/.../what-is-nicehash-miner 962 B — Vue SPA JS-shell park
- 404 https://raw.githubusercontent.com/NiceHash/NiceHashMiner/main/README.md (default branch is `master` — retried OK)
- 200 https://raw.githubusercontent.com/NiceHash/NiceHashMiner/master/README.md (6,438 B)
- 200 https://raw.githubusercontent.com/NiceHash/NHOS/main/README.md (1,080 B)

## Parks (honest)
1. nicehash www JS shell (above) — no SSR surfaces found anywhere on www.nicehash.com; exchange/marketplace pages were out of scope anyway. GitHub READMEs used as official product/doc surfaces instead, clearly labeled in file headers.
2. Awesome Miner /upgrade — not a pricing page (form only); pricing tiers taken from /signup instead.
3. Braiins Manager dashboard.md (monitoring detail) fetched + quoted but not stored as a 4th file to respect the 2-3 file cap for this registry.
