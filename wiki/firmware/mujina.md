# Mujina

> Sources: 256 Foundation Telegram group (t.me/the256foundation), 2024-02-24 → 2026-10-07
> Raw: [256F Telegram signal digest](../../raw/history/2026-10-08-256f-telegram-signal.md)
> Updated: 2026-10-08
> As-Of: 2026-10-08
> Status: Draft

## Overview

Mujina is the 256 Foundation's open-source mining firmware, written in Rust. It exists because every proprietary miner firmware targets grid-connected industrial mining — home heat reuse, grid-stabilization and similar alternative uses end up fighting the firmware instead of being served by it [#309 · 2024-03-03 · Skot Bitaxe] [#319 · 2024-03-03 · Skot Bitaxe] [#320 · 2024-03-03 · Michael Schmid @Schnitzel]. It runs as a single `mujina-miner` program on nearly any Linux machine, with a whole-OS image (MujinaOS) as the longer-term goal, and by 2026 it runs on everything from a Bitaxe Gamma to a stock Bitmain S19j Pro control board.

## Architecture & goals

- Supported-hardware reality (February 2026): only the Bitaxe Gamma (+ CPU miner) is mainline; EmberOne and S19j Pro support in the works [#4378 · 2026-02-02 · Ryan]
- Architecture goal: many hashboards of many types per Mujina instance, hotpluggable while Mujina runs [#4376 · 2026-02-02 · Ryan]
- MujinaOS concept (November 2025): today Mujina is a single `mujina-miner` program you install on any Linux; the bigger goal is MujinaOS — a whole-Linux image for LibreBoard (and later other control boards) with kernel mods, DTs and modules integrated, and a platform for app-specific components (sensors/actuators driving a hot tub, etc.) [#3485 · 2025-11-20 · Ryan] [#3487 · 2025-11-20 · Dan Sokil]
- MineralOS referenced as a project to study for OS structure [#3500 · 2025-11-21 · Dan Sokil]
- Host requirements are modest: it runs on any Linux [#3472 · 2025-11-20 · Ryan]
- Deliberately modular and hashboard-agnostic; priorities are emberOne/Libre/derivatives, with big-vendor board support tracked where feasible [#2182 · 2025-05-16 · Ryan] [#2268 · 2025-05-22 · Ryan]

### Power policy design

- Power-target design (January 2026): (A) user sets a system-wide power target and Mujina optimizes efficiency across boards, or (B) per-board/per-group constraints (different cooling loops); a 'scheduler' sits between hashboards, pools and the user API applying policies as boards come and go [#4175 · 2026-01-07 · Ryan] [#4180 · 2026-01-07 · Ryan]; Home-Assistant sketch: each EmberOne adds 100 W to a controllable budget, split across boards [#4182 · 2026-01-07 · Dylan Seib]
- Layered power-policy proposal (golana): policy layers split by time scale — an economic layer coordinating a whole site passes slower goals down to faster local controllers that enforce constraints (slew limits, valid V/f); his power-aware source (solar MPPT + wall power) would tell Mujina '1000 W solar, 1400 W wall'; example policy 'please break even' [#5138 · 2026-07-22 · golana]; Ryan's response: distill concrete use cases into low-level primitives (per-board power/efficiency curves); grid-price subscription might belong in a second daemon next to the mining daemon [#5139 · 2026-07-22 · Ryan]
- Roadmap ask: thermostat-like control of chip voltage/speed as the feature that makes bitcoin-as-space-heater take off; Aadhi picked it up [#4673 · 2026-04-18 · Collin] [#4674 · 2026-04-18 · Aadhi M]

## Hardware ports (As-Of 2026-10-08)

- Bitaxe Gamma: mainline [#4378 · 2026-02-02 · Ryan]
- S19j Pro stock Bitmain control board: 'very rough version of Mujina compiled and working' (2026-03-09, single hashboard) [#4553 · 2026-03-09 · Skot Bitaxe]; proof-of-concept announced on the forum (2026-05-11): 'Bitmain Antminer controlboards run linux and are perfectly capable of running Mujina firmware' [#4787 · 2026-05-11 · 256F Forum] — this unlocks the entire installed Antminer fleet
- Amlogic control boards: stop LuxOS, compile Mujina for ARM, copy it over; notes in github.com/skot/amlogic-cb-tools; network install over anything is the goal, USB burn works even on bricked boards; Bitmain's signed bootloader/boot partitions required [#4734 · 2026-05-01 · Skot Bitaxe] [#4736 · 2026-05-01 · Skot Bitaxe] [#4737 · 2026-05-01 · Skot Bitaxe] [#4741 · 2026-05-01 · Skot Bitaxe] [#4755 · 2026-05-03 · Skot Bitaxe]
- mujina-loader repo for getting Mujina onto an Amlogic board, plus Skot's mujina fork with Antminer-specific bits (PSU communications) [#4942 · 2026-06-12 · Aadhi M] [#4944 · 2026-06-12 · AgentP]
- Braiins BCB100 control board running Debian: BCB100_Mujina port (github.com/aadhi1014/BCB100_Mujina), Loki-rig testing planned [#4655 · 2026-04-09 · Aadhi M]
- Xilinx Zynq control boards: mujina-xilinx-platform package boots to a mujina shell on the Zynq (ARMv7) — first Zynq execution [#3499 · 2025-11-21 · Dan Sokil] [#3509 · 2025-11-21 · Ryan]
- Windows native (no WSL/docker): community port via Claude assistance; uses tokio-serial with VID:PID auto-discovery [#4090 · 2026-01-05 · Aadhi M] [#4094 · 2026-01-05 · Aadhi M]
- Canaan: A3197 protocol reverse engineered; BMM101 running Mujina + Doom [#5081 · 2026-07-22 · Aadhi M]
- Intel RDS with 300× BZM2 (September 2026): community bring-up attempt on the Intel controller — would be the highest-hashrate Mujina system so far [#5482 · 2026-09-14 · Reckless Apotheosis] [#5489 · 2026-09-14 · Reckless Apotheosis]

## Internals

- Custom serial layer: tokio-serial was dropped because it couldn't handle baud-rate changes after the tx/rx streams were split (ownership issues); the replacement is POSIX/Linux-specific — possibly why WSL misbehaves [#4116 · 2026-01-05 · Ryan] [#4118 · 2026-01-05 · Ryan]; background in mujina discussion #10 [#4117 · 2026-01-05 · Ryan]
- All SHA256 Mujina does outside the ASICs goes through the rust-bitcoin crate [#3514 · 2025-11-21 · Ryan]; rust-bitcoin PR #5493 (SHA intrinsics, due in bitcoin_hashes 0.20.0) worth watching — Bitcoin Core already uses the ARM intrinsics [#4563 · 2026-03-11 · Johnny] [#4564 · 2026-03-11 · Skot Bitaxe]; 'Mujina uses rust bitcoin_hashes' [#4571 · 2026-03-11 · Johnny]
- CI parity: `just ci` runs exactly what the GitHub workflow runs, in the same container image (plain `just checks` runs in the local shell) [#5315 · 2026-08-05 · Ryan] [#5316 · 2026-08-05 · Ryan]
- Self-hosted ARM runners: deploy runners on the expected arm targets (Gamma, emberOne, bm13xx hashboards, mixes), label by target/ASIC, keep hardware checks advisory so they don't block merges; prior art: johnny9's esp-miner-e2e master-controller with a container per USB-connected Bitaxe [#4584 · 2026-03-11 · Johnny] [#4587 · 2026-03-11 · Ryan] [#4590 · 2026-03-11 · Johnny] [#4595 · 2026-03-11 · Johnny]
- SNMP directly on miners: impossible with Bitmain/MicroBT's closed firmware, but 100% possible with Mujina — e.g. a daemon hitting Mujina's API and throwing SNMP traps, on or off the Libre Board; an open MIB would let enterprise tools (openNMS, Nagios) manage miner fleets like switches and PDUs; Wade already graphs drycooler fan/pump speed, PDU power and coolant temps via openNMS [#2618 · 2025-07-02 · Wade Bowlin] [#2620 · 2025-07-02 · Michael Schmid @Schnitzel] [#2621 · 2025-07-02 · Ryan] [#2637 · 2025-07-02 · Reckless Apotheosis] [#2638 · 2025-07-02 · Reckless Apotheosis] [#2639 · 2025-07-02 · Wade Bowlin] [#2641 · 2025-07-02 · Wade Bowlin] [#2642 · 2025-07-02 · Wade Bowlin]

## Sensor debate (resolved January 2026)

> **Status: Disputed** — resolved
> Field report: Gamma hitting 87C in 2 minutes with fan '92 rpm' under Mujina [#4095 · 2026-01-05 · Aadhi M]; Ryan: 'Mujina definitely reports the wrong RPM' — the temp and fan duty cycles were correct [#4114 · 2026-01-05 · Ryan] [#4115 · 2026-01-05 · Ryan]. Cross-firmware check closed it: Mujina and esp-miner agree on the same temperatures with the same Gamma, at identical clock/voltage (525 MHz, 1.146V — noting 1.15V is identical to esp-miner's default); the earlier readings were a reporting bug, not silicon reality [#4173 · 2026-01-07 · Ryan] [#4207 · 2026-01-11 · Ryan].

## Stock-firmware interplay

- Bitmain ASICs default to 115200 baud; most miners increase it after init [#4096 · 2026-01-05 · Skot Bitaxe]
- BraiinsOS+ and stock firmware disagree on S9 temperature readings; Braiins' numbers considered the more trustworthy [#559 · 2024-03-23 · Brett Rowan]
- esp-miner goes through undocumented-diode setup (ideality/gain parameters) for the EMC2101 on Bitmain ASICs; Mujina users were told to check the same values [#4148 · 2026-01-06 · Skot Bitaxe] [#4151 · 2026-01-06 · Skot Bitaxe]

## Docs governance

- Chip documentation doesn't belong in the Mujina repo — Reckless Apotheosis already maintained the bzm2-hwref repo for exactly that purpose; PRs reworked so only function-relevant docs stay with the code [#5110 · 2026-07-22 · Ryan] [#5112 · 2026-07-22 · Reckless Apotheosis] [#5114 · 2026-07-22 · Reckless Apotheosis] [#5118 · 2026-07-22 · Reckless Apotheosis]

## See Also

- [Ember One & the BZM2 Hardware Stack](../hardware/ember-one-bzm2.md)
- [asic-rs and the Fleet-Tooling Stack](../mining-software/asic-rs.md)
- [Decentralized Pool Designs](../protocols/decentralized-pool-designs.md)
- Same topic: [Heater Firmware & Power Control](heater-firmware-and-power-control.md)
