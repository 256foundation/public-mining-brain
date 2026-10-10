# Mining Firmware Security

> Sources: 256 Foundation Red Team (256-RedTeam-Public README and "Build your own red-team cage" guide, written 2026-09-13; captured 2026-10-07); Schnitzel and @256FOUNDATION posts on X, 2026-08 → 2026-09; 256 Foundation newsletter (Substack), 2025-05 → 2026-04; 256foundation.org newsroom and our-work pages (captured 2026-10-07); POD256 episodes 2025-09 → 2026-08; GitHub research snapshot of Canaan, Proto and grants (2026-10-07)
> Raw: [256 Red Team README](../../raw/history/256f-org/github-256foundation-256-redteam-public.md); [Red Team cage guide](../../raw/history/256f-org/github-256-redteam-public-docs-build-your-own-cage.md); [X: Red Team launch thread](../../raw/history/256f-research/2026-10-07-x-notable-open-source-mining.md); [newsletter, May 2025](../../raw/history/256f-newsletter/2025-05-05-bitcoin-mining-will-not-be-decentralized-until-it-is-open-so.md); [Assembling Freedom #12](../../raw/history/256f-newsletter/2025-12-22-assembling-freedom-12.md); [Research: Proto, Canaan, grants](../../raw/history/256f-research/2026-10-07-research-proto-braidpool-canaan-grants.md)
> Updated: 2026-10-09
> As-Of: 2026-10-09
> Status: Draft

## Overview

A bitcoin miner is a networked computer that earns money directly, usually sits on a flat and unmonitored LAN, and runs closed firmware that ships the same defaults across a whole fleet. Schnitzel calls mining firmware "The least-audited, most-exposed devices in Bitcoin" ([X: Red Team launch thread](../../raw/history/256f-research/2026-10-07-x-notable-open-source-mining.md)). The history of incidents supports him. Antbleed in 2017 was a remote kill switch in Antminer firmware that a user found by reading strings, not through an audit. A 2025 Bitmain update reportedly blocked connections to specific pools. Operators once had to exploit vendor tools to get root on their own machines. In August 2026 the 256 Foundation launched the 256 Red Team to audit this firmware systematically. It reported 41 findings. Stock Bitmain firmware had serious hygiene bugs but no skimming or kill switches, while hidden behavior concentrated in third-party "optimized" firmware. This page covers how the Red Team works, what it found, the history of closed-firmware incidents, the slow opening of incumbent firmware, and what operators can do today.

## Threat model: why firmware matters

The 256 Foundation lists four building blocks of a miner: hashboard, control board, firmware and pool. Its description of the firmware layer reads: "Firmware is unauditable, so you cannot verify it is not skimming hashrate or holding a kill switch. Antbleed proved it." ([256F: Our Work](../../raw/history/256f-org/256foundation-org-our-work.md)). The Foundation's list of closed-stack risks includes firmware that keeps an owner from proving their own revenue, checking for kill switches, or seeing "what your machines are sending home" ([Presidio fundraiser post](../../raw/history/256f-org/256foundation-org-newsroom-presidio-bitcoin-fundraiser.md)). HRF's framing reaches past the individual operator. If hardware, firmware and pool software are closed, nobody outside a handful of manufacturers can confirm that settlement and issuance follow Bitcoin's rules ([HRF renewal post](../../raw/history/256f-org/256foundation-org-newsroom-hrf-renews-support.md)).

The RY3T Nova announcement adds a practical complaint. Manufacturer firmware from Bitmain, Whatsminer, Canaan and Bitdeer is closed, and so are the aftermarket alternatives Braiins OS, LuxOS and Vnish. All of them were written for a data center running "at a fixed setpoint". The announcement's conclusion: "You cannot fix closed firmware from outside it. You have to replace it." ([RY3T Nova post](../../raw/history/256f-org/256foundation-org-newsroom-ry3t-nova.md)).

| Threat class | What it looks like | Where it shows up |
|---|---|---|
| Remote control / kill switch | Vendor can shut down or redirect miners | Antbleed (2017) |
| Pool restriction | Firmware refuses certain pools | Bitmain S21+ update, April 2025 |
| Hashrate skimming / hidden fees | Shares or time diverted from the owner's worker | Red Team found it concentrated in third-party "optimized" firmware |
| Management-plane weaknesses | Unauthenticated factory APIs, default credentials, baked-in vendor SSH keys, local root paths | Red Team: present in stock firmware too |
| Unsigned updates | OTA chains that do not verify signatures or pin TLS | Red Team cage guide |
| Stratum hijacking | Plaintext Stratum V1 connections redirected in transit | Braiins estimate of 1% to 2% of hashrate stolen |
| Malicious pool | Pool sends a coinbase that does not pay the miner | Mitigated by AxeOS coinbase verification |

Sources for the table rows are cited in the sections below.

## The 256 Red Team

### What it is

The 256 Red Team is the Foundation's firmware security program. It audits mining firmware and pool infrastructure for hidden fees, backdoors, skimming, anti-tamper mechanisms, and undocumented failure modes ([256 Red Team README](../../raw/history/256f-org/github-256foundation-256-redteam-public.md)). Schnitzel introduced it on 2026-08-12. He described ~90% of ASICs as running one vendor's closed firmware that "Almost nobody has audited" ([X: Red Team launch thread](../../raw/history/256f-research/2026-10-07-x-notable-open-source-mining.md)). The Foundation lists it among its programs as "Reverse engineering closed firmware and other mining software, followed by responsible disclosure" ([256F: Our Work](../../raw/history/256f-org/256foundation-org-our-work.md)). The team credits "powerful open-weight AI tools and decompilers" with making the work feasible ([X archive: 2026](../../raw/history/256f-research/2026-10-07-x-256foundation-2026.md)). POD256 #123 discussed the same AI-assisted reverse-engineering approach as a way to expose dev fees and remote controls ([POD256 #123](../../raw/history/pod256/2026-08-10-pod256-123-coldcard-fallout-mining-firmware-and-the-bip-110.md)).

Ground rules from the public README ([256 Red Team README](../../raw/history/256f-org/github-256foundation-256-redteam-public.md)):

- **Own hardware only.** All live testing happens on lab hardware in an isolated environment. AI agents may analyze offline artifacts but never attack devices without explicit operator authorization.
- **Safety classes.** Every operation is either *always safe* (read-only, unattended) or *attended-only* (anything that can change fans, clocks, voltage, flash or process state). Automation enforces the split.
- **Human-gated disclosure.** Humans verify findings and disclose them to vendors before any public write-up.
- **Evidence labels.** Each claim carries affected versions and hashes, reproduction steps, artifacts, and a confidence label: `confirmed | probable | suspected`.

### Method and bench

The launch thread lists the first bench and methods ([X: Red Team launch thread](../../raw/history/256f-research/2026-10-07-x-notable-open-source-mining.md)):

| Category | Targets |
|---|---|
| Stock Bitmain | S19j Pro and S21 (live units, full flash dumps, Ghidra) |
| Third-party firmware | LuxOS, VNISH, Braiins OS |
| Open baselines | Mujina, AxeOS/Bitaxe |
| Next on the bench | MicroBT Whatsminer; Canaan Avalon; Auradine, Bitdeer (SEALMINER), ePIC |
| Methods | Static reverse engineering, live traffic capture, share-level reconciliation |

The cage guide lists the devices actually under test as of 2026-09-13. There were 3 full S19-class miners (LuxOS, ePIC, and Mujina+Nova) and 5 bare control boards (Mara, ePIC, stock S21, BeagleBone S19j Pro, Braiins BCB100) ([Red Team cage guide](../../raw/history/256f-org/github-256-redteam-public-docs-build-your-own-cage.md)). A donor gave the team a Canaan Avalon Mini 3 on launch day ([X: Red Team launch thread](../../raw/history/256f-research/2026-10-07-x-notable-open-source-mining.md)).

### Findings (as of 2026-10-07)

- **41 findings filed**, each with evidence and a reproduction recipe. The thread calls these "Hygiene bugs everyone has, stock included": unauthenticated factory APIs, local paths to root, fleet-default credentials, vendor SSH keys baked into images, and updates that don't verify what they install ([X: Red Team launch thread](../../raw/history/256f-research/2026-10-07-x-notable-open-source-mining.md)).
- **Stock Bitmain came out cleanest on trust.** A full decompile of both miner daemons plus live connection tables found "no hashrate skimming, no kill switches, no covert beacons" ([X: Red Team launch thread](../../raw/history/256f-research/2026-10-07-x-notable-open-source-mining.md)).
- **Third-party "optimized" firmware was the opposite.** In the thread's words, hidden behavior "an owner can't see from the dashboard (and wouldn't choose) is concentrated there, not in stock" ("Better features, worse trust") ([X: Red Team launch thread](../../raw/history/256f-research/2026-10-07-x-notable-open-source-mining.md)).
- **Update chains.** Several vendor update chains the team tested do not verify signatures or pin TLS ([Red Team cage guide](../../raw/history/256f-org/github-256-redteam-public-docs-build-your-own-cage.md)).
- **Mujina.** No major flaws, "just a couple of small improvements". At the time no flashable Mujina OS images existed for the S19 (Schnitzel, 2026-08-13) ([X: Red Team launch thread](../../raw/history/256f-research/2026-10-07-x-notable-open-source-mining.md)).

The thread does not attribute any specific finding to a named vendor. Treat the summary above as the team's characterization until the sanitized write-ups are published.

### Disclosure status

On launch day, three coordinated disclosures had gone to Vnish, Luxor and Braiins, each with 30 days to respond before the team publishes ([X: Red Team launch thread](../../raw/history/256f-research/2026-10-07-x-notable-open-source-mining.md)). On 2026-09-11 the Foundation said the original window had closed, that "Every impacted party asked for an extension" and was working with the team in good faith, and that findings would publish when the extended windows close ([X archive: 2026](../../raw/history/256f-research/2026-10-07-x-256foundation-2026.md)). As of 2026-10-07 the public repo held the lab guide. Sanitized findings, harnesses and agent playbooks are listed as forthcoming ([256 Red Team README](../../raw/history/256f-org/github-256foundation-256-redteam-public.md)).

## Build your own cage (blueprint)

The Red Team's first public release is a build guide for an isolated, fully observed miner lab, written 2026-09-13 from the team's live deployment. Its core rule is "The miner is the untrusted device." Treat each miner like a malware detonation box: it can do anything except reach the internet unobserved, and you must be able to cut its power without touching it ([Red Team cage guide](../../raw/history/256f-org/github-256-redteam-public-docs-build-your-own-cage.md)).

| Layer | What the team runs | Why |
|---|---|---|
| Cage router | Raspberry Pi CM5 + IO board, Debian 13, second NIC via USB3 GbE; dnsmasq, nftables and Tailscale, managed with Ansible | A Linux box you control at OS level is the choke point and the inline MITM and capture point |
| DNS/DHCP/NTP | dnsmasq with `log-queries` and `log-dhcp`; static reservations per MAC; the router serves NTP | DNS logs are "the cheapest beacon detector there is"; an unexpected time server is itself a finding |
| Egress policy | nftables, default drop, toggled between `allow` and `restricted` per test via one Ansible variable | Lock the cage to DNS plus one pool's ports when needed |
| Power control | Shelly Pro 2PM and 2× Shelly Pro 4PM (local Gen2 HTTP API, per-channel metering) | Remote, metered power cut; the router and AP are also on Shelly-fed outlets, with a manual override |
| Remote access | Tailscale subnet router on the cage router | Reach in without exposing anything |
| Capture | tcpdump ring buffer (~200 × 100 MB), Zeek; 7-day baseline per firmware version | Structured, grep-able logs that agents can use |
| Pool instruments | HashScope (Stratum-logging proxy) plus Hydrapool as pool of record; one test against a real public pool with a sacrificial worker | The "primary anti-skimming instrument": any share not going to your worker is visible |
| Cost | Non-miner infrastructure is well under $1,500 new | A control board or used miner is often the pricier part |

The guide's practical lessons ([Red Team cage guide](../../raw/history/256f-org/github-256-redteam-public-docs-build-your-own-cage.md)):

- **Start with bare control boards.** A board with no hashboards draws a few watts and is safe to leave on unattended. It is enough for firmware image analysis, management-plane testing, OTA and update paths, network behavior, and Stratum handshake fuzzing. Real hashboards are needed only for thermal and fan behavior, hashboard-link reverse engineering, load-only bugs, and measuring fee or skim behavior, because a bare board submits no shares.
- **Thermal guard.** While hashing, abort at ≥ 80 °C or if fans drop below ~3000 RPM. Document the reversion step before each test. Use a smoke detector, a dedicated circuit and an electrical-rated extinguisher.
- **"read-only" is per-endpoint, not per-HTTP-verb.** The team once triggered a config rewrite and reload with a *bodyless GET* on a factory CGI. Check side effects in the decompile before probing.
- **Agent rules.** No live attacks without an operator instruction naming the target IP. No exfiltration of firmware images; hashes only. Disclosure is human-gated, and every unverified claim is tagged `UNVERIFIED`.

## Closed-firmware incidents and history

| When | Incident | Source |
|---|---|---|
| 2017 | **Antbleed.** A remote kill switch in Antminer firmware, found by a user reading strings, not by an audit. The Foundation calls it "the remote shutdown backdoor found hiding in Bitmain firmware in 2017" | [X: Red Team launch thread](../../raw/history/256f-research/2026-10-07-x-notable-open-source-mining.md); [Presidio fundraiser post](../../raw/history/256f-org/256foundation-org-newsroom-presidio-bitcoin-fundraiser.md) |
| Pre-2025 | Other Bitmain controversies listed by the newsletter: covert ASICBoost, the "Fork Wars", mining empty blocks, and removing SD card slots | [newsletter, May 2025](../../raw/history/256f-newsletter/2025-05-05-bitcoin-mining-will-not-be-decentralized-until-it-is-open-so.md) |
| ~2020 | **OEM SSH lockout.** Per Marshall Long, MicroBT withheld SSH access. Operators got root through a SQL injection vulnerability in the Whatsminer tool, then dumped firmware by inserting an SD card during POST. He describes about two years of cat-and-mouse before OEMs became more cooperative | [newsletter, Jun 2025](../../raw/history/256f-newsletter/2025-06-19-you-know-i-m-something-of-a-decentralized-pool-myself.md) |
| April 15, 2025 | **Pool blocking.** A Bitmain S21+ firmware update was reported to block connections to OCEAN and Braiins pools | [newsletter, May 2025](../../raw/history/256f-newsletter/2025-05-05-bitcoin-mining-will-not-be-decentralized-until-it-is-open-so.md) |
| Ongoing | **Coinbase output caps.** Vendor firmware limits how many payout outputs a coinbase can carry. Old stock Antminers will not handle templates with more than "some 16 payout addresses", which constrains non-custodial pools like Hydrapool | [newsletter, Sep 2025](../../raw/history/256f-newsletter/2025-09-25-rig-bitcoin-mining-re-imagined.md); [POD256 #090](../../raw/history/pod256/2025-10-15-pod256-090-make-every-meetup-a-pool-stratum-v2-hole-punching.md) |
| 2026-08 / 2026-09 | **GPL violations in clone firmware.** skot says HammerMiner admitted using Bitaxe's GPL esp-miner code in closed-source firmware (2026-08-27) and that MagicMiner violates the esp-miner GPL (2026-09-02). These are skot's public claims, not adjudicated findings | [X: skot on copyleft](../../raw/history/256f-research/2026-10-07-x-notable-skot-bitaxe.md) |

POD256 has framed closed firmware as antithetical to Bitcoin's trust-minimized ethos, tracing a history of CGMiner GPL violations and secure-boot cat-and-mouse ([POD256 #095](../../raw/history/pod256/2025-11-19-pod256-095-open-source-or-bust-mujina-miner-firmware-wars-an.md)).

> **Status: Disputed**: are third-party firmware dev fees legitimate?
> Supporters see developer fees as monetization for features like auto-tuning and efficiency gains. Critics prefer fee-free open firmware such as Mujina ([POD256 #086](../../raw/history/pod256/2025-09-10-pod256-086-open-source-vs-closed-source-the-future-of-bitcoi.md)). The 256 Foundation's newsletters describe closed-firmware dev fees as "often 2-3%" and as acting like SaaS subscriptions ([Assembling Freedom #14](../../raw/history/256f-newsletter/2026-01-30-assembling-freedom-14.md); [Assembling Freedom #19](../../raw/history/256f-newsletter/2026-03-11-assembling-freedom-19-revolutionizing-bitcoin-mining-hacking.md)). Best assessment: a disclosed dev fee is a business model, not a security issue. The Red Team's concern is behavior an owner "wouldn't choose" and can't see. Whether specific third-party firmware takes more than its advertised fee awaits the published findings.

### Pool-side and protocol incidents

These are not firmware bugs, but they belong to the same trust problem:

- **Duplicate-share exploit.** On April 27, 2025, Public Pool patched a Nerdminer exploit. It had not been checking for duplicate shares, so scam firmware submitted each valid share five times to fake five times the hashrate ([newsletter, May 2025](../../raw/history/256f-newsletter/2025-05-05-bitcoin-mining-will-not-be-decentralized-until-it-is-open-so.md)).
- **Stratum hijacking.** Braiins estimates that 1% to 2% of hashrate is stolen by hijacking unencrypted Stratum connections. Stratum V2's encrypted miner-to-pool connection is the protocol-level fix ([newsletter, Jul 2025](../../raw/history/256f-newsletter/2025-07-15-the-bigger-they-are-the-harder-they-fall.md)).
- **Unsafe clones.** On June 16, 2025, a miner posing as a Bitaxe exploded. The newsletter blames clones that change the bill of materials to cheaper, untested parts ([newsletter, Jul 2025](../../raw/history/256f-newsletter/2025-07-15-the-bigger-they-are-the-harder-they-fall.md)). Separately, NerdQaxe users were told on July 12, 2025 to update to firmware v1.0.31-RC because of a bug that blew a fuse and several diodes ([newsletter, Aug 2025](../../raw/history/256f-newsletter/2025-08-18-is-open-source-communism.md)).

## Incumbents going open source

| Vendor / project | What opened | Notes | Source |
|---|---|---|---|
| Canaan | Avalon firmware source (Avalon_mm repo, created 2025-10-30) under BSD3 | Canaan has open-sourced Avalon software since 2013 (cgminer fork, OpenWrt packages, Avalon-extras), and most of those repos went dormant around 2019. The newsletter notes that BSD3 raises compatibility questions with GPL-V3, and argues that Canaan, a distant third in market share, has only upside from opening up | [Assembling Freedom #12](../../raw/history/256f-newsletter/2025-12-22-assembling-freedom-12.md); [Research: Proto, Canaan, grants](../../raw/history/256f-research/2026-10-07-research-proto-braidpool-canaan-grants.md) |
| Canaan (community port) | Mujina running on a Canaan Nano 3S, reverse-engineered by Aadhi Maalaven (2026-08-12); Mini 3 work followed by 2026-10-03 | Tyler Stevens called it "the unlock" for builders to modify devices | [X: Canaan Mujina port](../../raw/history/256f-research/2026-10-07-x-notable-canaan-mujina-port.md) |
| Braiins | Braiins Control Board open-sourced (2025) | The 256 Foundation chose not to adopt it for Libre Board. A community fork later ran Mujina on the Braiins BCB100 | [newsletter, Jun 2025](../../raw/history/256f-newsletter/2025-06-19-you-know-i-m-something-of-a-decentralized-pool-myself.md); [Assembling Freedom #23](../../raw/history/256f-newsletter/2026-04-11-assembling-freedom-23.md) |
| Proto (Block) | Proto Fleet management software, Apache-2.0 (block/proto-fleet, repo created 2026-03-26) | Announced 2025-08-13 as free, open-source fleet management. No Proto Rig hardware-design repo was found. A Mujina PR to Fleet was opened at Bitcoin 2026 | [Research: Proto, Canaan, grants](../../raw/history/256f-research/2026-10-07-research-proto-braidpool-canaan-grants.md); [X archive: 2026](../../raw/history/256f-research/2026-10-07-x-256foundation-2026.md) |
| Tether | MOS fleet management platform open-sourced (early February 2026) | Fleet layer, not miner firmware | [Assembling Freedom, POD256 #103](../../raw/history/256f-newsletter/2026-02-05-unlocking-decentralized-mining-deep-dive-into-pod256-episode.md) |
| LuxOS | Added an "ignore PSU link" option (April 2026) | Closed firmware that is still useful for custom PSU mods | [Assembling Freedom #25](../../raw/history/256f-newsletter/2026-04-22-assembling-freedom-25.md) |

The open-firmware alternatives are Mujina (GPLv3 Rust on Linux, with no dev fee or pool lock) for full-size miners ([256F: Projects](../../raw/history/256f-org/256foundation-org-projects.md)) and ESP-Miner/AxeOS for Bitaxe-class devices. AxeOS includes coinbase verification to protect miners against malicious pools ([Assembling Freedom #23](../../raw/history/256f-newsletter/2026-04-11-assembling-freedom-23.md)). For ESP-Miner's own security posture and bug history, see [ESP-Miner / AxeOS](../firmware/esp-miner-axeos.md).

## Operator hardening checklist

The Red Team's advice for operators, given at launch ([X: Red Team launch thread](../../raw/history/256f-research/2026-10-07-x-notable-open-source-mining.md)):

1. **Firewall ports 6060, 4028 and 1534** on miners. Do not expose miner management or API ports to untrusted networks.
2. **Rotate default credentials.** Fleet-shared defaults were one of the hygiene findings.
3. **Isolate miners on their own VLANs**, away from laptops, NAS devices and cameras.

Further steps drawn from the cage guide and related sources:

4. **Log DNS for the miner VLAN.** Unexpected domains are the cheapest phone-home signal. Serve NTP locally and watch for unexpected time servers ([Red Team cage guide](../../raw/history/256f-org/github-256-redteam-public-docs-build-your-own-cage.md)).
5. **Default-deny egress.** Allow only your pool's Stratum port, and open more only when needed ([Red Team cage guide](../../raw/history/256f-org/github-256-redteam-public-docs-build-your-own-cage.md)).
6. **Verify shares, not dashboards.** A Stratum-logging proxy such as HashScope shows whether every share goes to your worker ([Red Team cage guide](../../raw/history/256f-org/github-256-redteam-public-docs-build-your-own-cage.md)). Hydrapool lets users download its share accounting through an API so they can audit payouts themselves ([Hydrapool README](../../raw/pools/hydrapool/github-256foundation-hydrapool.md)).
7. **Treat updates as untrusted.** Several vendor update chains do not verify signatures or pin TLS. Fetch firmware from the vendor directly and record hashes ([Red Team cage guide](../../raw/history/256f-org/github-256-redteam-public-docs-build-your-own-cage.md)).
8. **Prefer encrypted or local pool connections** to reduce exposure to Stratum hijacking ([newsletter, Jul 2025](../../raw/history/256f-newsletter/2025-07-15-the-bigger-they-are-the-harder-they-fall.md)).
9. **Buy from license-respecting sellers.** Bitaxe clones with undocumented component and firmware changes cause overheating, WiFi problems and failures that OSMU volunteers cannot reproduce. bitaxe.org/buy lists license-respecting distributors ([newsletter, May 2025](../../raw/history/256f-newsletter/2025-05-05-bitcoin-mining-will-not-be-decentralized-until-it-is-open-so.md)).

## Contradictions & Open Questions

- The Red Team's published claims are summaries. The 41 findings, the affected vendors per finding, and their confidence labels were not public as of 2026-10-07, pending the extended disclosure windows ([X archive: 2026](../../raw/history/256f-research/2026-10-07-x-256foundation-2026.md)).
- The cage guide's DUT list (LuxOS, ePIC, Mujina+Nova full miners) differs from the launch thread's bench (stock S19j Pro and S21, LuxOS, VNISH, Braiins OS). The two describe different points in time, a month apart, and are not necessarily in conflict ([Red Team cage guide](../../raw/history/256f-org/github-256-redteam-public-docs-build-your-own-cage.md); [X: Red Team launch thread](../../raw/history/256f-research/2026-10-07-x-notable-open-source-mining.md)).
- The S21+ pool-blocking report comes from a single linked post cited by the newsletter. No vendor statement was captured ([newsletter, May 2025](../../raw/history/256f-newsletter/2025-05-05-bitcoin-mining-will-not-be-decentralized-until-it-is-open-so.md)).

## See Also

- [The 256 Foundation](../history/256-foundation-organization.md)
- [Mujina](../firmware/mujina.md)
- [ESP-Miner / AxeOS](../firmware/esp-miner-axeos.md)
- [Heater Firmware and Power Control](../firmware/heater-firmware-and-power-control.md)
- [HashScope](../mining-software/hashscope.md)
- [Hydrapool](../pools/hydrapool.md)
- [Stratum in Practice](../protocols/stratum-in-practice.md)
- [Libre Board and Control Boards](../hardware/libre-board-and-control-boards.md)
- [Bitmain ASIC Reference](../hardware/bitmain-asic-reference.md)
- [Repair, Supply and Vendors](repair-supply-and-vendors.md)
- [Pool Centralization and FPPS](../pools/pool-centralization-and-fpps.md)
