# POD256 Episode 090: Make Every Meetup a Pool: Stratum v2, Hole Punching, and Open Mining

> Sources: POD256 (episode 090 transcript), 2025-10-15
> Raw: [POD256 episode 090 transcript](../../raw/pod256/transcripts/2026-10-07/transcripts/2025/2025-10-15-e090.md)
> Updated: 2026-10-07

## Overview

Episode 090 was published on 2025-10-15 and runs 01:22:16. eco and Tyler carry the first half hour. Skot then joins live from TABConf in Atlanta with a guest, AverageGary, who works on Stratum v2 tooling. The source is the publisher's machine transcript, so names and terms are often misspelled and speakers are not labelled. The first half is the clearest telling on the show of how the Mujina and Hydrapool grants were scoped and how Hydrapool went from a CKPool fork to a fresh Rust stratum server. The second half covers Stratum v2 on Start9, NAT hole punching so any meetup can host a pool, ehash, and a plan for a foundation-run test Hydrapool.

## Topics in order

### TABConf and the talk that did not happen [00:02:41]

Skot is at TABConf. Skot and Ryan had prepared a session on open-source mining, but the proposal went in too late for the schedule, so Ryan did not travel.

### Mujina: design and scope [00:04:22]

eco's account:

- He believes the only open-source mining firmware available now is the ESP-Miner that runs Bitaxes. Mujina is meant to cover a much broader range.
- Ryan comes from a twenty year background in embedded Linux and is building Mujina from the ground up in Rust. It is not a fork.
- The design aims to be modular enough for hot swappable hash boards: the system keeps running, detects the new board and loads the right drivers [00:04:54].
- The firmware broadcasts work and each chip takes its piece by address. Because the nonce space is small, chips also roll bits in fields such as time and version. Some chips cannot. Mujina will work out what each chip can roll and hand out work to match [00:05:27].
- The aim is for Mujina to become its own Linux distribution that loads on any Linux-compatible hardware [00:08:32].

On scope [00:07:29]: eco says nobody at the foundation calls themselves an expert, since open mining is uncharted. Grant proposals were kept to about one page. For Mujina that meant drivers for different chips, a web UI or terminal interface, talking to a pool, and monitoring onboard sensors. Ryan then filled in the detail from experience and wrote the roadmap. Hot swap was found along the way, not planned.

eco says the projects were launched in April with stated deliverables and dates, and that the team is very close. An initial Mujina release should come in tandem with the first production batch of Ember One boards [00:11:20].

### Ember One v5 and scope creep [00:11:55]

The Ember One grant has closed, so the foundation is not paying Skot or eco for it, yet the board is on version five. The team was unhappy with the old voltage regulator's noise and large coils. The new one needs no big coils, talks over I2C so power use can be shown on the dashboard, and frees up board space. eco stresses that all four projects are iterative and will need upkeep.

### First outside Mujina build [00:14:39]

Tyler reports that a friend, a long-time Linux systems architect, was given access to the repo by Ryan and compiled Mujina on a Bitaxe in Colorado in a day. He has already sent a first pull request adding documentation.

### Hydrapool: how it got here [00:18:58]

eco tells the story in order:

1. **Motive.** Earlier in the year he tried to run his own Public Pool instance on a Raspberry Pi 4 and struggled for weeks; the chain sync alone took about sixteen days. He concluded that most people are shut out of running a pool.
2. **Vision.** A one click, self-hosted open pool that friends can join. Long term, many instances should coordinate and share rewards [00:22:16].
3. **Why Jungly.** He has a PhD in distributed systems and had already worked on P2Pool. He is building P2Pool version two, and showed how Hydrapool would complement it.
4. **First version.** An early Hydrapool was a fork of CKPool. Telehash number two, held on Cinco de Mayo in Austin, ran on it [00:24:20].
5. **Restart.** Lessons from that event sent the team back to the drawing board. Jungly started again with a basic stratum server written from scratch in Rust, which is the base of Hydrapool now.

Design choices since then:

- Solo mode and a PPLNS mode for groups [00:25:53].
- The number of coinbase outputs is user configurable. eco objects to Bitmain firmware limits having capped this across the industry. Stock Antminers with incompatible firmware may fail on larger coinbases, and he accepts that.
- Share auditing is done through an API endpoint that anyone can watch in real time, instead of the operator keeping a full share database for download. The reason given is to keep the burden on a novice operator low [00:28:35].

Tyler corrects an earlier episode: Ocean does have a share API. It is not public, but his team asked for it and used it to verify their shares [00:30:17]. He also relays Ocean's explanation of its custody claim: funds go to a wallet Ocean owns, but payout is automatic once the 100 block requirement passes [00:54:07]. Skot and Gary answer that what matters is who holds the keys.

### AverageGary: Stratum v2, Start9 and hole punching [00:33:07]

- Gary packaged Stratum v2 for the new Start9 framework so people can self-host a pool.
- He has a Stratum v2 branch that does NAT hole punching with a library called Iroh, and had it working with other developers at the conference. The goal: install a Stratum v2 pool on a home server and let anyone connect peer to peer [00:34:23].
- The slogan that gives the episode its title: every Bitcoin meetup in the world can have its own mining pool [00:35:33].
- He wants coinbase outputs to stop identifying pools, with a fresh address for each block. He says this is an idea, not yet built [00:37:46].
- He chose Stratum v2 over DATUM because it covers local templates too, because he knows Rust and not C, and because of the Rust tooling around it [00:50:19]. He notes Ocean's server side is not open.
- Stratum v1 has no formal spec and sends plain-text JSON; Stratum v2 is a specified binary protocol with encryption [00:46:43]. Skot mentions a student who said the campus network blocks mining from dorm rooms.

Brett Rowan's asic-rs, the Rust version of pyasic, has been placed in the 256 Foundation GitHub organization and published as a crate [00:51:27].

### Dummy work again [00:43:53]

Gary met a home miner who heats a greenhouse and lost the heat on a winter night when the miner stopped. That became a live feature request for made-up work. Skot explains that firmware has to actively stop the chips, so keeping them on dummy work is the simpler path.

### Payout schemes and ehash [00:55:14]

- Gary describes DMND, which he calls the first public Stratum v2 pool, and its PPLNS variant that weights the fee part of the reward by the fees in each miner's template while splitting the 3.125 Bitcoin subsidy evenly.
- He explains ehash: blinded tokens issued for shares, redeemable after the pool is paid. He says it is still custodial but adds no new trust assumption, and could help small or intermittent miners [00:58:26].
- Skot argues custody is less of a problem when there are many pools to switch between.
- Tyler describes his Home Assistant setup that turns a miner on when solar power makes mining free and off when it does not, with heating demand overriding it [01:02:11].

### Hashers, leaderboard and a test Hydrapool [01:04:30]

After the worker shout-outs:

- The hosts want a leaderboard of hashrate contributors and have enlisted helpers to build one for the upcoming Telehash.
- Gary announces a hashrate fundraiser at the Bitcoin Veterans summit at Bitcoin Park in November [01:09:30]. It will probably not solo mine unless enough hashrate turns up.
- eco will spin up a local test Hydrapool with Jungly, then rent a VPS and make it public. His idea is to move the show's hashrate contributors from other pools onto it [01:11:10]. It will run PPLNS with no hard-coded address, so the coinbase reflects the workers. There is no payout until a block is found.
- Jungly made progress on Hydrapool dashboards with Prometheus and Grafana.
- Parasite Pool has open-sourced its code [01:13:50].
- A NerdQAxe found a block while pool mining on Ocean and received only its normal share payout. Several hosts say this is why they solo mine their small miners [01:14:52].

### Core v30 and faster nodes [01:18:12]

Gary says the multi-process design in Bitcoin Core v30 lets Stratum v2's template provider talk to the node over IPC and receive pushed templates instead of polling. Skot met a developer working on CPU acceleration for signature and hash checks to speed up initial sync, which he hopes leads to smaller, cheaper nodes.

## Notable claims and decisions

- Mujina's first release is tied to the first Ember One production batch.
- Hydrapool dropped its CKPool fork after Telehash number two and was rebuilt in Rust.
- Hydrapool makes the coinbase output count configurable and audits shares through a live API.
- asic-rs now lives in the foundation's GitHub organization.
- A foundation-run public test Hydrapool is planned.

## See Also

- [POD256 Episode Guide: 2025](episode-guide-2025.md)
- [Open-Source Mining Stack Coverage on POD256](open-source-mining-stack-coverage.md)
- [POD256 Guests](guests.md)
- [Mujina Firmware](../mujina/mujina-firmware.md)
- [Hydrapool](../hydrapool/hydrapool.md)
- [Running Your Own Hydrapool](../hydrapool/running-hydrapool.md)
- [Ember One](../hardware/ember-one.md)
- [asic-rs](../tools/asic-rs.md)
- [Telehash](../foundation/telehash.md)
- [Grants and Funding](../foundation/grants-and-funding.md)
- [Public Pool](../ecosystem/public-pool.md)
- [The Nerd Miner Family](../ecosystem/nerd-miner-family.md)
- [Home Mining and Heat Reuse on POD256](home-mining-and-heat-reuse.md)
