# Assembling Freedom #23

> Source: https://256foundation.substack.com/p/assembling-freedom-23
> Collected: 2026-10-07
> Published: 2026-04-11

*From POD256 ep111: Open-Source Overdrive: Mujina Breakthroughs, Public Pool’s First Block, and LibreBoard v3*

*April 8, 2026 | Hosted by [@econoalchemist](https://x.com/econoalchemist), [@skot9000](https://x.com/skot9000), and [@tylerkstevens](https://x.com/tylerkstevens)*

Tech enthusiasts, this episode is pure open-source Bitcoin mining catnip. The crew dives headfirst into the “nerd-sniped” joy of rapid hardware iteration, celebrates a massive week for solo miners (4 blocks in a week!), and drops roadmaps for Mujina firmware, HydraPool, and LibreBoard v3. Everything is GPL/CERN-OHL licensed, community-driven, and aimed at making mining more hackable, transparent, and fun. No proprietary black boxes here—just Rust-powered firmware, custom PCBs, and real blocks hitting public pools.

### 1. Hardware Hacks: From $20 USB Miner Concepts to Fan Control Boards

The episode opens with the classic open-source trap: one idea leads to another. Hosts sketch the **Bitaxe Latte**—a jokey but plausible ultra-low-cost USB Bitcoin miner concept (\~$20 BOM) that could democratize entry-level solo mining even further. They also unveil a tiny custom adapter board for **AC Infinity** duct fans, letting miners control high-CFM, low-noise fans via standard 4-pin PWM headers on hashboards.

**Key Technical Breakdown:**

- **Bitaxe Latte concept**: Builds on existing Bitaxe ecosystem (BM1366/BM1370 chips). Focus on minimalism: USB-powered, open KiCad files, plug-and-play for hobbyists.
- **AC Infinity adapter**: Solves noisy stock fans. Uses 4-pin header for PWM speed control + RPM feedback. Pairs perfectly with Ember One or similar open boards.
- **Why it matters**: Open hardware accelerates iteration—community forks and PRs ship faster than closed-source vendors.

*(Bitaxe hardware examples—imagine the Latte as an even smaller USB variant.)*

*(Mining setups with AC Infinity-style fan integration and adapter examples.)*

### 2. Firmware Deep Dive: Mujina Breakthroughs & Open Collaboration

Mujina (Rust-based, async mining software from 256 Foundation) steals the show. It’s a modern, multi-chip driver firmware running on Debian-based OS, targeting Bitmain, Whatsminer, Avalon, and more. Recent wins include PWM frequency tweaks for better fan control and RPM reporting workarounds.

**In-Depth Bullet Breakdown:**

- **PWM frequency tweaks**: Higher/lower frequencies reduce coil whine or improve fan response on hashboards.
- **RPM reporting hack**: Custom logic in Mujina bridges missing sensor data—critical for monitoring and auto-tuning.
- **Universal Bitmain-chip driver roadmap (April)**: One driver to rule them all. Community forks already appearing (e.g., BCB100 support).
- **AxeOS protections**: Coinbase verification prevents pool attacks; GPL alignment ensures transparency.
- **Collaboration superpowers**: Open-source stack (firmware + hardware + pool) means PRs ship in days, not quarters.

**Mujina vs. Closed Firmware Comparison Table:**

*(Firmware dashboard example—visualizing real-time tuning, hashrate, and temps like Mujina/PrismOS-style interfaces.)*

### 3. Solo Mining Explosion: Public Pool’s First Block + 4 Blocks in Days

A banner week for the little guy. Solo miners (using open pools and hardware) found **4 blocks** recently—proof that probability + open tools = life-changing wins without KYC or custodial drama.

**Blocks Breakdown (as of episode):**

- CKPool ×2 (old Antminers, <sub>230 TH/s and</sub> 70 TH/s)
- **Public Pool’s first hosted-instance block** (\~18.5 TH/s NerdQaxe)
- Node Runners pool (\~4.8 TH/s NerdQaxe++)

**Pool Mechanics Spotlight:**

- Public Pool: Fully open-source, no fees, stratum+tcp://[public-pool.io](http://public-pool.io):21496 (username = BTC [address.worker](http://address.worker)).
- Coinbase verification in AxeOS/Mujina protects against malicious pools.
- Odds example: One 18.5 TH/s miner beat 1-in-28,000 daily odds for a full block.

**Solo Mining Wins Table:**

*(Public Pool branding and live dashboard—transparent, open-source solo mining.)*

*(Block-found celebration visuals—pure open-source mining joy.)*

### 4. April Roadmaps & LibreBoard v3 Power Design

- **HydraPool**: Password-field difficulty/hashrate hints + improved logging for better UX.
- **Mujina**: Push to universal Bitmain driver.
- **LibreBoard v3**: Power delivery upgrades for Ember One hashboards (\~100W, 2-4 TH/s per board). Fully open CERN-OHL-S, versatile I/O, compute module options.

*(Ember One / LibreBoard-style open hashboards and control boards.)*

Additional shop talk: Stencil printer & solder paste tips, Ember One v6.1 reliability, ASIC RS community growth, Telehash/Austin plans, and upcoming events (Vegas + Bitcoin Park Nashville).

### 5. Related X Buzz from the Community

The open-source mining wave is real—here’s what’s lighting up X right now:

- **@skot9000** (Bitaxe instigator): “Make no mistake, what you are looking at here is the future of Bitcoin mining firmware; Mujina. Versatile, customizable, open source freedom.” (quoting a BCB100 Mujina fork).

- **@econoalchemist**: Highlighted the same Mujina fork: “Someone forked Mujina & got it to work on the BCB100. Open-source Bitcoin mining firmware FTW.”

- **@mining\_central**: “This week #Bitcoin paid out 4 times to solo miners! … Public Pool - (\~18.5 TH/s, NerdQaxe) … The network doesn’t care how big you are.”

- **@solo\_mining**: Celebrated “The first Public Pool Bitcoin Block was (finally) found. 🥳 Congrats … Open Source wins!”

### Final Call to Action

Tune in at [pod256.org](http://pod256.org). Dive into the repos: [Mujina on GitHub](https://github.com/256foundation/mujina), [LibreBoard](https://libreboard.org/), Public Pool docs. Build, fork, mine—Bitcoin’s hashrate gets freer one open PR at a time.

Stay hashin’! ⛏️

*Generated from POD256 Episode 111 for tech enthusiasts.*

*This work published under the CC0 1.0 license*
