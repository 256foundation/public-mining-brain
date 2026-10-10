# Assembling Freedom #17: Unpacking POD256 Episode 105 - Chips, Chains, and Hot Tubs in Open Bitcoin Mining

> Source: https://256foundation.substack.com/p/assembling-freedom-17-unpacking-pod256
> Collected: 2026-10-07
> Published: 2026-02-19

*A weekly newsletter by 256 Foundation*

Welcome to this in-depth newsletter edition, tailored for tech enthusiasts passionate about Bitcoin, hardware innovation, and decentralized systems. We’re diving into POD256’s Episode 105, “Chips, Chains, and Hot Tubs: Open Mining Goes Hands-On,” hosted by [@econoalchemist](https://x.com/econoalchemist), [@skot9000](https://x.com/skot9000), and [@tylerkstevens](https://x.com/tylerkstevens). Streamed live from Bitcoin Park, this episode explores the frontiers of open-source Bitcoin mining, blending hands-on hardware demos with discussions on energy efficiency, firmware freedom, and community-driven tech. The hosts are joined by [Dylan](https://x.com/tronsington), the bros geeking out on builder-first topics like ASIC chips, blockchain reliability, and immersion cooling setups that resemble hot tubs. If you’re into tinkering with mining rigs or advocating for developer freedom, this breakdown will equip you with technical insights and actionable ideas.

## Episode Overview

This episode focuses on democratizing Bitcoin mining through open-source tools, addressing barriers like proprietary hardware and inefficient cooling. The hosts emphasize “freedom tech” that empowers individuals to mine at home, repurpose heat, and contribute to the network without relying on big players like Bitmain or Intel’s closed ecosystems. Key themes include fixing real-world hardware bugs, evolving firmware for universal compatibility, and fostering community innovations to make mining more accessible and sustainable.

## Key Takeaways

- **Hardware Breakthroughs:** A voltage domain [bug](https://github.com/256foundation/emberone00-pcb/issues/53) in the Ember One miner was fixed hands-on, boosting performance to \~2 TH/s—highlighting the power of open-source debugging.
- **Chip Design Insights:** Discussions on stacked voltage domains in ASICs reveal challenges in scaling long chains, with calls for open spec sheets to accelerate third-party builds.
- **Firmware Evolution:** Mujina’s open firmware aims for Linux-first universality, supporting devices like Antminers and Ember One boards while navigating auto-detect vs. manual config trade-offs.
- **Cooling Innovations:** Immersion cooling (dubbed “hot tubs”) is positioned as a game-changer for home setups, turning waste heat into practical value like home heating.
- **Community Momentum:** From solo-block wins on the 256F Hydra Pool to prep for the Heat Punk Summit, the episode celebrates grassroots efforts and urges support for developer freedom petitions.
- **Broader Implications:** Open mining reduces centralization risks, but faces hurdles like silicon politics and license restrictions—pushing for a builder-centric future.

### Hardware Updates and Fixes

The episode kicks off with practical demos, like troubleshooting the Ember One miner (an open-source rig with Intel boards and 12 chips targeting 3.6 TH/s).

- **Voltage Bug Fix:** Discovered by Mujina dev Ryan, this IO voltage domain issue was resolved desk-side, achieving \~2 TH/s post-fix. Proper cooling could push it to full spec.
- **Performance Metrics:** Current hashrate emphasizes the need for immersion or advanced air cooling to avoid thermal throttling.
- **Compatibility Notes:** Upcoming support for existing Antminers integrates seamlessly with open firmware.

Hardware ComponentIssueFixPerformance ImpactEmber One (12 chips)IO voltage domain bugHardware patch\~2 TH/s (up from unstable); target 3.6 TH/s with coolingAntminer SeriesLimited open firmwareMujina integrationUniversal Linux-first control, auto-detect featuresIntel BoardsChain reliabilityStacked domains redesignImproved long-chain stability for home rigs

### Chip Design (ASICs) Deep Dive

ASICs are the heart of mining efficiency. The hosts discuss the shift from FPGA teaching rigs to full community-designed chips, critiquing big silicon players like Intel for insider politics.

- **Stacked Voltage Domains:** Essential for power efficiency but prone to bugs in long chains—think cascading failures if one domain spikes.
- **Open vs. Closed Sales:** Advocating for public chip sales and spec sheets to empower builders like Epic Blockchain, reducing dependency on monopolies.
- **Case Studies:** FutureBit’s Apollo 3 (likely using Auradine chips) exemplifies open licenses, contrasting “lawyered” proprietary ones that stifle innovation.
- **Scarcity and Scaling:** As one related [X post](https://x.com/justh0dl/status/1695808493750526339) notes, 5nm chips like BM1366 are scarce, with production limits (e.g., TSMC’s \~150K/month) creating a “glass ceiling” for network difficulty.

### Chains (Blockchain) in Mining Context

While not a deep blockchain primer, the episode ties mining hardware to network health, including community hashing and solo wins.

- **Reliability in Chains:** Long ASIC chains mirror blockchain’s distributed ledger—emphasis on voltage stability to prevent “chain breaks” in hardware.
- **Community Hashing:** The 256F HydroPool enables shared mining, leading to solo-block successes and real-world decentralization.
- **Implications for Bitcoin:** Open tools reduce centralization, but challenges like min\_retweets:N engagement thresholds highlight the need for broader adoption.

### Hot Tubs (Immersion Cooling) Explained

Immersion cooling steals the show as a “hot tub” metaphor for submerging rigs in dielectric fluid, capturing waste heat for home use.

- **Efficiency Gains:** Reduces noise and energy waste; ideal for hashrate-heat products like space heaters.
- **Hands-On Applications:** Tied to Heat Punk Summit prep, where miners repurpose heat for freedom tech (e.g., heating homes while stacking sats).
- **Challenges:** Initial setup costs and fluid management, but ROI shines in cold climates—echoing DIY tutorials for Bitcoin mining heaters.
- **Tech Specs:** Fluids like mineral oil dissipate heat 1,000x better than air, allowing overclocking without fans.

Cooling MethodProsConsUse CaseAir Cooling (Fans)Cheap, easy setupNoisy, less efficientBasic home rigsImmersion (Hot Tub)Silent, heat repurposingHigher upfront costEnergy-efficient mining, home heatingHydro (Water Blocks)High performanceLeak risksIndustrial-scale ops

### Firmware and Software Innovations

Mujina firmware is spotlighted for its open-source push toward universal miner control.

- **Linux-First Approach:** Enables auto-detect for hardware, but real-world configs often win for precision.
- **Monitoring Tools:** Agent/LLM integrations (e.g., cron-jobs with heartbeats and MCP) allow remote tuning, alerts, and AI-assisted optimization.
- **UX for Home Miners:** Focus on simplicity—think plug-and-play for non-experts, with tools for overclocking and pool switching.
- **Open Licenses:** Debates on “open vs. lawyered” highlight risks of proprietary traps, urging community designs from FPGAs to ASICs.

### Community and Future Implications

- **Events and Wins:** HydraPool solo-blocks and Heat Punk Summit prep underscore community power.
- **Call to Action:** Support developer freedom at [https://change.org/billandkeonne](https://change.org/billandkeonne) to combat regulatory hurdles.
- **Challenges:** Silicon politics, bug reliability, and balancing openness with security.
- **Future Outlook:** Momentum from open specs could lead to widespread home mining, decentralizing Bitcoin further—as seen in [stories of basement rigs cracking floors from heat](https://x.com/HotAisle/status/2023286302465282440).

## Related X Discussions

Tech enthusiasts on X are buzzing about open mining. Here’s a curated selection of relevant posts:

- **Home Mining Designs and Physics:** [@BitcoinLibertyL](https://x.com/BitcoinLibertyL) hosted [@hashing2heating](https://x.com/hashing2heating), sharing insights on harnessing energy for Bitcoin home mining, including physics principles and career-learned hacks:

A follow-up live dove deeper into environmental sciences applications:

- **ASIC Scarcity and Open-Source Push:** [@justh0dl](https://x.com/justh0dl) breaks down why 5nm chips like BM1366 are key to decentralization, urging experimentation with open-source efforts from [@skot9000](https://x.com/skot9000) and the Open Source Miners United crew. Chips at $15? Time to solder!

- **DIY Mining Heaters:** [@BTCsessions](https://x.com/BTCsessions) shares a tutorial on building a Bitcoin mining space heater using @BraiinsMining tech—perfect for stacking sats while staying warm. Dedicated to critics like [@SenWarren](https://x.com/SenWarren)!

These posts echo the episode’s hands-on spirit, showing how open mining is gaining traction among builders.

Thanks for reading! If this sparked ideas for your own rig, dive into the full episode on

https://www.pod256.org and Subscribe for more breakdowns at https://news.256foundation.org.

Stay tuned for more tech deep dives—Drop your thoughts below. 🚀
