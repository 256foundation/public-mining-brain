# 256 Foundation Forum

> Sources: 256 Foundation forum (Welcome to The 256 Foundation!), 2026-03-18; 256 Foundation forum (Auradine support?), 2026-04-28; 256 Foundation forum (Messing around with FPGA mining), 2026-05-05; 256 Foundation forum (Waterblock stl?), 2026-05-15; 256 Foundation forum (Where is s19jpro support?), 2026-06-27; 256 Foundation forum (New user-facing website, PRs welcome), 2026-07-23
> Raw: [forum: welcome](../../raw/foundation/2026-03-18-forum-welcome-to-the-256-foundation-wave.md); [forum: Auradine support](../../raw/foundation/2026-04-28-forum-auradine-support.md); [forum: FPGA mining](../../raw/foundation/2026-05-05-forum-messing-around-with-fpga-mining.md); [forum: waterblock STL](../../raw/foundation/2026-05-15-forum-waterblock-stl.md); [forum: S19j Pro support](../../raw/foundation/2026-06-27-forum-where-is-s19jpro-support.md); [forum: new website](../../raw/foundation/2026-07-23-forum-new-user-facing-website-prs-welcome.md)
> Updated: 2026-10-07

## Overview

The forum at forum.256foundation.org is where the foundation's projects are discussed in public. Its welcome post calls it the home for developers, contributors, researchers and miners who think Bitcoin mining should be free and open. It is organized by project. This article covers how the forum is laid out and what a handful of early threads established about hardware support.

## How the forum is organized

| Category | What it covers, per the welcome post |
|---|---|
| General | Announcements, ideas and open mining discussion. |
| Ember One Hashboard | The open-source ~100W hashboard: standardized form factor, multi-ASIC, 12–24VDC, USB-C. |
| Mujina Firmware | Open-source firmware written in Rust. Linux-based, with no closed parameters and no dev fees. |
| Libre Control Board | The open control board. Runs a full Bitcoin node, a Stratum server and the hashboards, with swappable compute modules (ARM, RISC-V). |
| Hydrapool | A one-click, self-hostable pool with Solo and PPLNS modes and payouts direct from coinbase. |
| asic-rs | A Rust library for unified ASIC management: one API for Antminer, Whatsminer, Avalon, Bitaxe, Braiins and more. |
| Site Feedback | Questions and issues about the forum itself. |

Each category has a pinned About topic.

## Ways in, according to the welcome post

- Contribute code on GitHub.
- Test the hardware and firmware: build an Ember One, flash Mujina, spin up a Hydrapool instance.
- Join the Telegram group chat for day-to-day discussion.
- Listen to POD256, the weekly podcast.
- Follow on X and Nostr, and subscribe to the newsletter.
- Donate. The post says the foundation is funded entirely by donations.

The house rule: be direct, be constructive, and criticize ideas, not people. Lurking is welcome.

## What early threads established

### Auradine chips are not planned

A member asked on 2026-04-28 whether Auradine ASIC support was coming. Skot answered on 2026-04-30 that he had no immediate plans to build an Auradine Ember One, but that it would be a good project if someone wanted to take it on.

### S19j Pro support was not yet merged in mid-2026

A member noticed on 2026-06-27 that the Mujina README still listed the S19 series under near-term targets and that the main repo had no S19 board module. Ryan confirmed on 2026-06-29 that the S19j Pro work was not merged into the main repo yet and was being cleaned up for merging. He pointed to a prototype version in another forum post and a GitHub discussion.

He also gave a safety warning for anyone experimenting:

- Mujina was not yet completely fail-safe in all cases on S19s.
- It would not necessarily detect and protect against an insufficient power supply.
- Start with only one hashboard connected.

See [Mujina Firmware](../mujina/mujina-firmware.md) for the wider status, and [RY3T Nova](ry3t-nova.md) for S19 hashboards running under Mujina in a demonstration.

### No waterblock files for Ember One yet

A member asked on 2026-05-15 for a waterblock STL file for the Ember One. Tyler explained that the prototypes used at TELEHASH #3 came from CryoByte Labs. Ryan said he did not have the files, and that if the team obtained them and was able to, it should post them on the forum.

### An FPGA miner experiment

On 2026-05-05 Skot shared TangMiner, an FPGA Bitcoin miner project. He was blunt that FPGA mining performance is poor, but said some of the concepts carry over to designing a real ASIC some day. Asked about a Mujina driver, he posted a quick demo branch the next day.

### A user-facing Mujina website

On 2026-07-23 Ryan posted a new user-facing website for Mujina at mujina.org, with a GitHub discussion for feedback. Pull requests are welcome.

## See Also

- [Donate and Get Involved](donate-and-get-involved.md)
- [Events and Calendar](events-and-calendar.md)
- [Mujina Firmware](../mujina/mujina-firmware.md)
- [Ember One](../hardware/ember-one.md)
