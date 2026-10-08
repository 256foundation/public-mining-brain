# Assembling Freedom #25

> Source: https://256foundation.substack.com/p/assembling-freedom-25
> Collected: 2026-10-07
> Published: 2026-04-22

*Touchscreens, Thermostats, and Doom: A Weekend of Open Mining Hacks*

*April 22, 2026 | Hosted by [@econoalchemist](https://x.com/econoalchemist), [@skot9000](https://x.com/skot9000), & [@tylerkstevens](https://x.com/tylerkstevens)*

*Bitcoin mining, freedom tech, and awesome tangents from [POD256 #113](https://www.pod256.org/episodepage/113-touchscreens-thermostats-an-doom-a-weekend-of-open-mining-hacks)*

Tech enthusiasts, this episode is pure weekend-warrior gold for open-source Bitcoin mining hackers. The 256 Foundation crew breaks down a frenzy of community-driven hardware hacks, firmware breakthroughs, and practical integrations that turn miners into smart home devices, retro gaming rigs, and even heating systems. No fluff—just actionable prototypes, real-world limits, and the open hardware momentum making closed-source tricks obsolete.

### 1. Skot’s Touchscreen Miner Retrofit: The Ampminer Prototype on S19j Pro

Skot walks through a clean, Wi-Fi-enabled retrofit on a stock Bitmain Antminer S19j Pro using **Mujina firmware**. Key innovation: tapping the hidden USB port for connectivity without ripping open the case.

**Core Hack Breakdown (Step-by-Step as Discussed):**

- **Firmware**: Flash Mujina directly onto the stock control board (Ethernet/USB method).
- **Connectivity**: Hidden USB port + USB hub → Wi-Fi dongle for wireless operation.
- **Display**: Repurposed open-source touchscreen (sourced from Bitaxe GT Touch ecosystem) wired via USB hub.
- **Dashboard**: Live readouts for hashrate, temperatures, fan speeds, and pool stats—right on the miner itself.
- **Bonus**: Native support for AC Infinity duct fans for quieter, smarter cooling.

This creates a “tidy, Wi-Fi-connected touchscreen miner” that feels like a consumer appliance. AI-assisted CAD and browser automation sped up the prototyping loop dramatically.

**Visual: Bitaxe Touch-style interface concept (the exact screen tech reused here)**

**Related X Post Spotlight**

@skot9000 shared the first working prototype:

“First working prototype of The Ampminer: A stock S19j Pro running Mujina firmware with a touchscreen (from the Bitaxe GT Touch). Full WiFi connection. Native AC Infinity duct fan support.”


**Components Table**

### 2. LibreBoard + Thermostats: Turning Miner Waste Heat into Smart Home Heating

The crew brainstorms (and prototypes) using **LibreBoard** (the 256 Foundation’s open-source mining control board) as a bridge between standard 24V home thermostats and Bitcoin miners.

**Technical Deep Dive:**

- **Bridge Logic**: LibreBoard translates thermostat “heat calls” into miner ramp-up/down commands.

**Control Modes Compared:**

- **Binary Heat Calls**: On/off—simple but inefficient (full power or nothing).
- **Ramp Control**: Gradual frequency scaling for smoother heat output.
- **PID Loops**: Discussed for precise temperature targeting (Proportional-Integral-Derivative control to minimize overshoot).
- **Firmware Limits**: Frequency tuning works differently across Mujina vs. stock vs. LuxOS—real-world testing shows hardware caps on older ASICs.

This is perfect for home miners: excess heat warms your house while the miner earns sats. Community builds already include filament dryers heated by hashrate.

**Visual: Waste-heat reuse in action (3D printer/filament dryer example using miner exhaust)**

Catch the full interview with PizzAndy in [this](https://www.tomshardware.com/tech-industry/cryptomining/3d-printer-that-can-mine-bitcoin-uses-excess-heat-for-temperature-control-throttled-asics-use-printing-bed-as-a-heatsink) Tom’s Hardware article.

**Control Modes Table**

### 3. Schnitzel’s Doom-on-LibreBoard Test (#LibreDOOMAxe)

Pure hacker joy: Schnitzel got **Doom** running on the LibreBoard paired with a Bitaxe hashboard. Mujina firmware treats the Bitaxe like a hashboard via [bitaxe-raw](https://github.com/bitaxeorg/bitaxe-raw), with real-time stats on an OLED display, Qwiic-connected temp sensors, fan RPM control, and even RGB temperature indicators. HDMI output shows the 256 Pool dashboard.

**Why It Matters**: Open firmware (Mujina + LibreBoard) makes proprietary “trick boards” obsolete. The path to full open firmware on WhatsMiners is accelerating—goodbye to vendor lock-in.

**Visual: LibreBoard in action (open hardware control boards)**

**Related X Post Spotlight**

@Schnitzel (LibreBoard lead engineer):

“LibreBoard Revision 1/2 testing continues: I built a LibreBoard-Axe! Mujina running on Libreboard with a Raspberry Pi CM5… And obviously the best: completely open source hardware and software.”


And the Doom tease:

“But can it run Doom? #LibreDOOMAxe” (with follow-up tests including MIPI DSI touch displays and full Raspberry Pi HAT support).


**Visual: Bitaxe open-source miner (the hashboard used in the LibreDOOMAxe build)**

### 4. Firmware, PSU, & Stratum V2 Momentum

- **LuxOS Update**: New “ignore PSU link” option—huge for custom PSU mods (120V hacks discussed in detail).
- **WhatsMiners**: Rapid progress toward open firmware; hardware hacks like trick boards become unnecessary.
- **Stratum V2**: BlitzPool’s solo pool + non-custodial PPLNS roadmap. Vision for a node-native, open block-template app that could unlock true decentralized mining.

**Community Shoutouts**: - OpenSats’ *[Open Hardware Impact Report](https://opensats.org/blog/open-hardware-for-open-money)*highlighting Bitaxe, BitShoka/BitSoka Nini, and the 256 Foundation.

- New features on [hardestblocks.org](http://hardestblocks.org) and the growing [dash.256f.org](http://dash.256f.org) roster.
- Wild builds: BitForge Nano, hashrate-heated filament dryers.

### Key Takeaways for Tech Enthusiasts

- **Open hardware wins**: LibreBoard + Mujina turns expensive ASICs into customizable, Wi-Fi, touchscreen, heating, *and* gaming devices.
- **Rapid iteration**: AI CAD + community testing = prototypes in days.
- **Practical Freedom**: Waste heat reuse, no dev fees, decentralized pools—Bitcoin mining as a true home freedom tech.

Catch the [full episode](https://www.pod256.org/episodepage/113-touchscreens-thermostats-and-doom-a-weekend-of-open-mining-hacks) on your favorite pod app (Fountain, Apple, Podverse, etc.) or watch the live replay. The 256 crew heads to Bitcoin 2026 in Vegas next week for panels on open hardware and human rights.

**Stay mining, stay hacking.**

Support POD256 via [Zaprite](https://pay.zaprite.com/pl_ZRWeSGjRWG) (Bitcoin or fiat). Follow [@256FOUNDATION](https://x.com/256FOUNDATION)and the hosts for prototype drops and next-week live updates.

*Generated from Episode 113 show notes & community context. All projects 100% open source—fork, build, improve.*

*All of our newsletters are published under the CC0 1.0 license.*
