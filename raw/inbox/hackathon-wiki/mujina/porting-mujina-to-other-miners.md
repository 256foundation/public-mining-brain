# Porting Mujina to Other Miners

> Sources: 256 Foundation forum (Best Practices for Hacking Mujina onto Other Miners?), 2026-05-18; 256 Foundation forum (Mujina-Antminer), 2026-05-11; 256 Foundation forum (Mujina Dev Call #2), 2026-05-05; Mujina project (mujina.org hardware compatibility, current as of July 2026), collected 2026-10-07
> Raw: [Hacking Mujina onto other miners thread](../../raw/mujina/2026-05-18-forum-best-practices-for-hacking-mujina-onto-other-miners.md); [Mujina-Antminer thread](../../raw/mujina/2026-05-11-forum-mujina-antminer.md); [Dev Call 2](../../raw/mujina/2026-05-05-forum-mujina-dev-call-2.md); [mujina.org hardware compatibility](../../raw/mujina/mujina-org-reference-hardware-compatibility.md)
> Updated: 2026-10-07

## Overview

Community members have got [Mujina](mujina-firmware.md) hashing on Bitmain Antminer S19-family machines, working in personal forks and often with AI coding agents. Two forum threads collect what they learned. The work splits into two separate problems: getting any software of your own to run on the control board, and then adding Mujina support for that hardware. As of the threads there is no image file for easy loading. It takes SSH access and side loading. The project says any porting guide must lead with safety warnings.

## Why Antminers

Skot opened the Mujina-Antminer thread on 2026-05-11. Bitmain Antminer control boards run Linux and can run Mujina. He reported the first proof of concept: Mujina running on an S19j Pro with a stock Amlogic control board. Building and loading it was, in his words, "a very manual process".

## A framework, not one-off ports

Asked whether support would be added case by case or through a framework, Ryan answered that it is both. Mujina is being built as modular components: ASIC chips, power supplies, fan controllers, temperature sensors and so on. A supported miner is a built-in recipe for how one system composes those pieces.

The goal is that supporting a new miner mostly means describing how it wires existing pieces together. When a piece is missing, you add it. A new ASIC gets a chip driver. A new PSU or fan controller gets a peripheral driver. The next person can reuse it.

The mujina.org compatibility page says the same thing from the other side: Mujina is not ported to a board, a driver for the board is added to Mujina.

## Two separate problems

Dev Call #2 agreed the docs should keep these apart:

1. Get arbitrary software running on the control board.
2. Add Mujina support for that board.

Skot asked for a "hacker kit" or getting-started guide that covers the first problem too: removing proprietary firmware, getting around Secure Boot, and loading software onto control boards.

## Getting onto the control board

What the threads report for Amlogic control boards:

- **SSH.** AgentP's answer on whether SSH is required: technically no, practically yes. An agent that can SSH in tests in minutes. Moving a USB stick or SD card by hand takes hours or days.
- **Aftermarket firmware.** AgentP's port relied on LuxOS, which was already installed and handled the secure boot exploit. The agent stopped the LuxOS process and started Mujina.
- **Persistence.** Stock Bitmain firmware has a read-only filesystem, so Mujina does not survive a power cycle unless the filesystem is made writeable. Skot said the easiest way is to install LuxOS or Braiins. He is also working on doing it from scratch with mujina-loader, which works but needs cleanup.
- **Root access is closing.** Skot wrote that the exploit LuxOS uses to get root on stock Bitmain firmware was blocked by a firmware update sometime mid-2025, and that very recent LuxOS turned off root access.
- **Rolling back.** A control board with recent stock firmware needs the "usb burn" method to return to early-2025 stock firmware. Skot had not yet got a Mujina image with a writeable filesystem working with usb burn.

For Xilinx control boards, a different method is documented in [Mujina Xilinx Platform](mujina-xilinx-platform.md).

## AgentP's S19XP port

AgentP reported on 2026-05-30 that Mujina was working on an S19XP.

**Setup:** an S19XP running LuxOS on an Amlogic control board, with a single hashboard, an AC Infinity fan, and an APW12 modded to accept 120V. LuxOS had been set to 110MHz for a low, stable load of about 10TH and 290W. The control board had no control over fan speed, so the hashrate had to stay low.

**Method:** the first prompt gave the agent the Mujina main branch, the test machine's address, Skot's mujina-loader as a starting point, and the esp-miner repo as a reference for driving both chip types. It asked for research and a detailed plan first. AgentP adjusted the plan, then had the agent implement it.

**What went wrong along the way:**

- The first test only tried to read from the chips. It failed because the PSU cut hashboard power when the LuxOS service stopped.
- After that was fixed, hashing worked but every share came back at very low difficulty. The agent found that XP chips return the nonce with different endianness than the jPro. Fixing that gave good shares.
- UART stayed stuck at 115200. Raising it to 3M lost contact with the chips.

**Hindsight:** AgentP wished the agent had also been given Skot's S19j Pro fork, to avoid rebuilding the PSU control logic.

On 2026-06-17 AgentP got a persistent install working on an older LuxOS board and was running an XP board at 10.9V for undervolt testing.

## Working with AI agents

Dev Call #2 described a possible new open-source workflow for 2026: vibe-coded prototypes do the research, then maintainers turn them into production-quality merges. Skot's corollary was to keep Mujina modular, so prototypes can drop in without rewriting the core.

AgentP's practical tips from the thread:

- How much permission to give an agent depends on the model, your risk tolerance, your workflow, and how much you trust the repositories.
- Their agent cannot run sudo and has no GitHub integration. Commits and pushes are done by hand.
- For a repeated sudo action, such as restarting a service, write a script for that one action and allow passwordless sudo on the script only.
- Do not over-specify prompts. Vague is sometimes fine, and agents can find better solutions than the one you had in mind.
- To check for SSH, ask the agent to try, or try `ssh root@` plus the miner's address yourself. Enabling SSH is likely done in the firmware's web UI.
- For deep work, consider instruments the agent can read directly, such as WiFi power meters and voltage sensors.

## Safety

- AgentP told the agent not to run any code on the miner unless they were physically present to pull the plug.
- AgentP watched hashboard bus voltage with a multimeter and wall draw with a power meter.
- Dev Call #2 set an action item for everyone: treat safety warnings as the lede of any porting documentation. The risks named were fire and hardware destruction.
- The same call called Bitaxes the safe starter target for testing.

## State for non-developers

In August 2026 a forum user with a fleet of S19j Pro machines asked for an easy guide. Tyler replied on 2026-08-05 that Schnitzel, Skot and AgentP each have their own Mujina forks for various S19 versions, but there is no image file for easy loading yet. It requires SSH access and side loading the Mujina application.

The mujina.org compatibility page agrees. Running Mujina on an S19 means prototype software and an unsettled install path, not a replacement for stock firmware. See [Mujina Hardware Compatibility](hardware-compatibility.md).

Other efforts mentioned in the threads:

- ixtech.xyz was trying a bare-bones loader app from Bitmain firmware, starting with the jPro (2026-07-13).
- ixtech.xyz also asked for a PSU bypass, so that Loki kits are not needed.

## See Also

- [Mujina Firmware](mujina-firmware.md)
- [Mujina Hardware Compatibility](hardware-compatibility.md)
- [Mujina Xilinx Platform](mujina-xilinx-platform.md)
- [Mujina Dev Calls](mujina-dev-calls.md)
- [Bitaxe and Open Source Miners United](../ecosystem/bitaxe-and-osmu.md)
