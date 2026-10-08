# Open Mining Stack

> Source: https://256foundation.org/projects
> Collected: 2026-10-07
> Published: Unknown

# The Open Mining Stack

Bitcoin mining will be open-source, or Bitcoin stays permissioned

Mining began open: general-purpose CPUs, open operating systems, off-the-shelf chips. It matured into a closed stack a handful of vendors control. These are the four domain-specific building blocks a modern miner is made of, and the open replacement for each.

Every mature industry runs on commoditized, open inputs: recipes anyone can read, use, and improve. Bitcoin mining doesn't, yet. Four layers make a miner and run the network, and each one is undocumented, closed, or concentrated. Open one layer and close another and you have rebuilt the cage, so we open all four, and give the work away.

## Ember One

Open-source Bitcoin mining hash board reference design

A fully open-source hardware reference design for a Bitcoin mining hash board, the foundational blueprint that miners, researchers, and companies can build upon.

The closed problemMining chips ship with no datasheets, no pinouts, no voltages or frequencies, and no way to buy the chips on their own. To build on competitive silicon you buy a full machine, desolder the chips, and reverse-engineer how to talk to them.

The open answerEmber One publishes the whole recipe: open PCB files, bill of materials, and firmware interface spec. It teaches the industry how ASICs chain in series and how a standalone hash board pairs with a separate control board, then lets you scale one design from a bench build to a rack.

Funded by 256 · Core Architect & Lead Maintainer, Skot [@skot9000](https://x.com/skot9000)

Key Specifications

Key Features

- →Bitmain BM1362 ASIC
- →USB-C data interface
- →Integrated temperature sensors
- →Native Libre Board + Mujina compatibility
- →Open PCB design files

## Libre Board

Open-source Bitcoin miner control board

An open-source hardware control board that runs Linux, supporting Mujina natively, plus anything else you need alongside it. Swappable compute scales across system complexity, so one board can run your system with no extra controllers.

The closed problemA control board silently decides what a “miner” is allowed to be. Want your own firmware, a display, Wi-Fi on a remote site, or a flow sensor wired into a heat system? The closed board says no.

The open answerLibre Board exposes every interface a mining system might need and runs full Linux. It teaches builders how to wire anything into a miner, then strip the design down to their own parts list and form factor.

Funded by 256 · Core Architect & Lead Maintainer, Schnitzel [@Schnitzel](https://x.com/Schnitzel)

Key Specifications

Key Features

- →Runs full Linux, not just firmware
- →Bitcoin full node + local Stratum server
- →RPi 40-pin header, GPIO, fan connectors
- →Ethernet, WiFi, HDMI, NVME
- →Native Mujina firmware

## Mujina

The Linux kernel project of Bitcoin mining firmware

Actively maintained open-source mining firmware, a drop-in replacement for proprietary firmware on existing hardware and a standard for new open designs.

The closed problemFirmware is the operating system of a miner. Closed options are un-auditable, unmodifiable and take license fees. You cannot verify they aren't skimming hashrate, phoning home, or holding a remote kill switch.

The open answerMujina is the Linux-kernel project of mining firmware: open, reproducible, and forkable, with per-chip power control and no dev fee. It standardizes the layer everything else depends on, and gives operators source they can actually verify.

Funded by 256 · Core Architect & Lead Maintainer, Ryan Kuester [@ryankuester](https://x.com/ryankuester)

Key Specifications

Key Features

- →No dev fee, no pool lock
- →Per-chip power targeting and watt budgets
- →Stratum V1/V2 with DATUM compatibility
- →Drivers for Antminer, Whatsminer, Avalon
- →Web dashboard, REST API, CLI

## Hydrapool

One-click deployable open-source Bitcoin mining pool

A fully open-source mining pool built as a platform: payout and accounting logic are plug-ins, not hard-coded, and deploy with a single command.

The closed problemThe pool is the server side of mining, and it is concentrated. Pools can filter which transactions get mined, custody your payouts, and hide the accounting, and there’s no permissionless way to aggregate hashrate without trusting an operator.

The open answerLike WordPress for pools: the core is a platform and payouts are plug-ins: solo, PPLNS, and more (Lightning, Ark) on the same core, all non-custodial from the coinbase. A P2Pool V2 path goes further, to pooling with no operator to trust at all.

Funded by 256 · Core Architect & Lead Maintainer, Jungly [@jungly](https://x.com/jungly)

Key Specifications

Key Features

- →One-command Docker deploy
- →Plugin payout logic: solo, PPLNS, more
- →Non-custodial coinbase payouts
- →P2Pool V2 path (pool without an operator)
- →Prometheus + Grafana monitoring
- →Live at pool.256foundation.org:3333

## Together, a Permissionless Development Kit

An open hash board on an open control board running open firmware, mining to an open pool. Four independent projects that combine into one open-source mining development kit, free for anyone to study, fork, manufacture, and build a business on.
