# Pool Choice for Heat Miners

> Sources: Hashrate Heatpunks Telegram group, 2024-08-02 → 2026-10-08
> Raw: [Hashrate Heatpunks Telegram signal digest](../../raw/economics/2026-10-09-heatpunks-telegram-signal.md)
> Updated: 2026-10-09
> As-Of: 2026-10-09
> Status: Draft

## Overview

A hashrate heater is an unusual pool customer: it hashes when the house needs heat and stops when it doesn't, so its shares arrive in bursts that can last hours (thermostat cycling, on-peak curtailment) or months (heating season). The Hashrate Heatpunks group argued for two years about what that means for pool choice. The FPPS camp (led by Karl) holds that intermittent hashrate looks like pool hopping and is penalized by any share-window scheme, so FPPS pays fairer value for heaters [#946 · 2024-09-04 · Karl] [#6558 · 2025-06-24 · Karl]. The OCEAN/TIDES camp (Cody Harris, Toine, Dane O, Travis, Dylan Seib) reports that TIDES works fine with daily curtailment and values sovereignty: building your own block templates via DATUM, non-custodial coinbase payouts and Lightning payouts with no minimum [#947 · 2024-09-04 · Cody Harris] [#6583 · 2025-06-25 · Dane O] [#6594 · 2025-06-25 · Dylan Seib]. The best field data available is one home S9 run side by side from 2025.06.02. It showed FPPS ahead by a small and shrinking margin, and the experimenter concluded the gap did not justify the effort [#6448 · 2025-06-10 · Heatpunk Forum] [#7080 · 2025-08-14 · Heatpunk Forum]. This article covers that debate, payout mechanics, DATUM setup for home miners, failover for heat-critical installs, share difficulty and solo mining.

## Rules of thumb

- **Match the scheme to your duty cycle.** If the heater runs 24/7 for the whole winter, PPLNS makes a lot of sense [#976 · 2024-09-04 · Karl]. For very intermittent hashrate FPPS is the conservative choice, because it pays the full value of each share when you hash it [#946 · 2024-09-04 · Karl] [#6587 · 2025-06-25 · Karl]. Consistent daily curtailment (on-peak hours, 2x daily) has worked on OCEAN in the field [#6582 · 2025-06-25 · Travis Bitkle] [#6583 · 2025-06-25 · Dane O].
- **Judge a pool over months, not a week.** One miner moved to Ocean at the beginning of February and had two rough weeks, then two good ones [#4485 · 2025-03-12 · Travis Bitkle]. Ocean worked out for a regularly powered-off miner after about 6 weeks [#4505 · 2025-03-13 · Travis Bitkle].
- **Always configure failover, because the heat matters more than the hashrate.** One recommended heater pool order is Pool 1 DATUM, Pool 2 Ocean, Pool 3 drain:// [#4012 · 2025-02-12 · Cody Harris]. Keep OCEAN as the backup behind your own DATUM gateway [#4009 · 2025-02-12 · Dylan Seib].
- **Count firmware dev fees and pool fees together.** Using LuxOS firmware waives the Luxor pool fee [#1088 · 2024-09-07 · Nicolas Drouin-Audet]. Karl's Lincoin setup gets zero pool fees with Vnish, and he notes there is no way to run third-party firmware on Ocean and avoid its fees [#6548 · 2025-06-24 · Karl] [#6549 · 2025-06-24 · Karl]. Vnish autotune saves pool fees even where it doesn't match LuxOS tuning [#4729 · 2025-03-22 · Karl]. Gianluca's tests found Luxor and Braiins similarly profitable at a given frequency (both better than Vnish), with Luxor charging higher fees than Braiins [#8442 · 2025-12-26 · Gianluca L].
- **Every ASIC needs a pool entry**, even when solo mining [#1129 · 2024-09-14 · Jonathan Y].

## FPPS vs PPLNS vs OCEAN TIDES for intermittent hashrate

### How the schemes treat an on/off heater

- TIDES pays for time you were online, even if your miners are offline when a block is found [#945 · 2024-09-04 · Cody Harris]. Cody Harris described it as working much like FPPS except that payout happens when blocks are found, and as "pretty much PPLNS" with a gigantic n that smooths variance [#947 · 2024-09-04 · Cody Harris] [#953 · 2024-09-04 · Cody Harris].
- Karl's counter: PPLNS/TIDES shares get diluted the longer a block takes, and an on/off heater can't accrue shares to make up for it [#946 · 2024-09-04 · Karl] [#954 · 2024-09-04 · Karl]. He says you must be hashing for 8 blocks that Ocean finds to get the full value of your shares [#6569 · 2025-06-25 · Karl]. Dane O's reply is that the 8-block average simply reflects your hashrate over the window, and OCEAN's "estimate earnings for next block" box shows it [#6583 · 2025-06-25 · Dane O] [#6585 · 2025-06-25 · Dane O].
- **Fee volatility.** FPPS is better when fees are volatile: Ocean had a dry spell during the halving fee period, but hashers cannot verify how an FPPS pool distributes fees [#955 · 2024-09-04 · Cody Harris]. Karl says Lincoin users overclocked for higher payouts during the halving period while Ocean users missed the fees, adding "Not all fpps are the same" [#6592 · 2025-06-25 · Karl]. Dylan's view is the opposite for one-off events: FPPS won't pay extra for a single high-fee block, but OCEAN users would see more sats [#6589 · 2025-06-25 · Dylan Seib]. Fee-storm data point: a Lincoin payout went from ~75sat/th/day to over 85sat for ~24hr [#969 · 2024-09-04 · Karl].
- **Trust and decentralization.** FPPS is a centralized layer and is easy to attack with block withholding. It is easier than under PPLNS, where the attacker takes a hit [#964 · 2024-09-04 · Brett Rowan] [#965 · 2024-09-04 · Brett Rowan]. Cody Harris put it this way: "FPPS is the Wallet of Satoshi of mining", meaning it works but isn't very cypherpunk [#961 · 2024-09-04 · Cody Harris].
- **Early-adopter effect.** When more hash joins OCEAN, existing TIDES miners are rewarded, but that holds only while Ocean adoption outpaces difficulty adjustments [#4494 · 2025-03-13 · Toine Heat Reuse] [#4496 · 2025-03-13 · Dylan Seib] [#4498 · 2025-03-13 · Toine Heat Reuse].
- Specs to read: ocean.xyz/docs/tides and the Braiins academy FPPS specification [#952 · 2024-09-04 · Brett Rowan]. See also [Pool Payout Schemes](pool-payout-schemes.md).

> **Status: Disputed**
> Karl: "Pplns is bad for intermittent hashrate especially when there's fee volatility". In his view TIDES and PPLNS are effectively the same against FPPS, and intermittent hashrate is equivalent to pool hopping, which share-window schemes punish [#4497 · 2025-03-13 · Karl] [#4500 · 2025-03-13 · Karl] [#6558 · 2025-06-24 · Karl] [#6565 · 2025-06-25 · Karl]. Toine: pro-rating rewards over 8 blocks helps a ton, and in his comparisons TIDES paid more than the FPPS pools even when mining intermittently [#4499 · 2025-03-13 · Toine Heat Reuse] [#4501 · 2025-03-13 · Toine Heat Reuse]. Operators who curtail on a fixed schedule report payouts as expected [#6582 · 2025-06-25 · Travis Bitkle] [#6583 · 2025-06-25 · Dane O]. Current best assessment (as of October 2026): the controlled home experiment below found FPPS slightly ahead, with a gap smaller than earlier pool-level comparisons. The choice comes down to fee sensitivity versus own-template sovereignty, not a large revenue difference.

### Field data (dated)

**Pool-level comparisons**

- March 2025 (OCEAN vs FPPS): average Ocean payout was 64.5sats/TH/day vs ~56.78sats/TH/day on FPPS. Split by period, 03/1-23 averaged 56.07sats/TH/day and 03/24-31 averaged 88.83sats/TH/day. Dylan attributed the late-March jump to 2EH/s joining continuously on 3/24 plus TIDES ramp-up, and expected it to fall back to FPPS levels [#5314 · 2025-04-05 · Dylan Seib] [#5316 · 2025-04-05 · Dylan Seib]. Ocean also hit a double block around then, reportedly a first for the pool [#5173 · 2025-03-30 · Travis Bitkle].
- Wilson Mining Pool comparison (SBI proxy) as of June 3 2025: Luxor paid out 10.8% less and Ocean 5.2% less than Wilson [#6566 · 2025-06-25 · Karl]. Dylan went through the Wilson Bros' data and found the gap closing from -10% to -5% for OCEAN. He agrees FPPS was paying more at the time [#6594 · 2025-06-25 · Dylan Seib].

**Dylan Seib's home experiment: 1x S9, TIDES vs FPPS**

Setup: one S9 running BraiinsOS, started 2025.06.02 [#6448 · 2025-06-10 · Heatpunk Forum]. OCEAN was mined through a DATUM Gateway at 1% total fee [#6669 · 2025-06-30 · Dylan Seib].

| Checkpoint | Braiins (FPPS) | OCEAN (TIDES) | Note |
|---|---|---|---|
| 2025-06-30 | 5648 sats | 4786 sats | Braiins about 18% higher since 6/2 [#6667 · 2025-06-30 · Dylan Seib] |
| 2025-08-07 (two months) | 12991 sats | 12579 sats | [#6946 · 2025-08-07 · Heatpunk Forum] |
| 2025-08-11 | 13119 sats | 12680 sats | Miner off for travel, shares still in the OCEAN window [#6969 · 2025-08-11 · Heatpunk Forum] |

- While the miner was offline it earned "a whopping 18 sats from OCEAN". At that point FPPS led TIDES by ~3.3% over the whole run since 2025.06.02. Dylan's conclusion: "The juice is not worth the squeeze from a utility bill perspective" [#7080 · 2025-08-14 · Heatpunk Forum].
- This is one machine, one summer and one pair of pools. The gap narrowed from the early-June lead to ~3.3%, which is consistent with TIDES needing time to ramp.

## Payouts: thresholds, lag and Lightning

- **On-chain threshold.** Ocean's minimum on-chain payout threshold is about 1 million sats. A Lightning option exists, but setting it up is technical [#6577 · 2025-06-25 · Jarno].
- **Payout lag.** Ocean payouts can lag. One explanation offered is that only a limited number of on-chain payouts fit in a block's coinbase, depending on the machine that found it (the poster flagged his own example numbers as wrong). Another user saw balances go 20%-25% over the threshold, but never more [#7558 · 2025-11-05 · Dylan Seib] [#7564 · 2025-11-05 · Travis Bitkle].
- **Lightning payouts.** Small Ocean miners commonly take Bolt12 Lightning payouts for better privacy and steady payouts with no minimum [#5323 · 2025-04-06 · Cody Harris]. These payouts are sent through a subsidiary rather than the coinbase, and they take a while [#3817 · 2025-01-31 · Dylan Seib] [#3816 · 2025-01-31 · Cody Harris].
  - Channel strategy: Toine receives Ocean payouts on his Core Lightning node. He started with a 400,000 sat channel to ACINQ, then opened a larger one to the Boltz node because Aqua wallet uses Boltz. His tip is to open a channel to the node your destination wallet uses, which cuts hops and fees [#1895 · 2024-11-07 · Toine Heat Reuse]. Aqua auto-swaps LN to L-BTC and charges "a pretty high fee for it" [#1907 · 2024-11-08 · R D].
  - Gotchas: on Umbrel, Core Lightning reportedly can't connect to Bitcoin Knots, so the Ocean LN payout can't be used there, and DATUM works only with Knots [#1932 · 2024-11-14 · Jim ⚡️]. Bitcoin Mechanic reportedly said LuxOS causes problems with Bolt12 payments while Braiins OS+ does not. This was relayed without technical detail [#1856 · 2024-11-06 · Toine Heat Reuse].
- **FPPS conveniences.** Lincoin offers FPPS, management tools, Paynym and Lightning payouts, and low thresholds. Its "Agent" software is well liked [#958 · 2024-09-04 · Toine Heat Reuse] [#968 · 2024-09-04 · Karl]. The Agent can also send notifications and remote-control miners, which answered a request for over-temperature alerts [#7437 · 2025-10-19 · Shawn Flowers] [#7438 · 2025-10-19 · Karl].
- **Splitting rewards for installers.** A trustless reward split across several addresses, like Braiins offers, isn't available on OCEAN. Per a conversation with Mechanic, it was tried and hit a dead end but may be revisited. This matters for installers managing heaters at client sites [#4218 · 2025-02-24 · Dane O]. The workaround is DATUM-level splits (see below).

## DATUM for home miners

### What it is

- DATUM lets hashers build their own block templates and write their own tags [#1424 · 2024-10-08 · Trevor Bello]. With DATUM, OCEAN supplies the coinbase split information and everything else comes from the miner's own node [#7139 · 2025-08-20 · Dylan Seib]. In September 2024 it was a private beta, available by emailing Ocean [#1231 · 2024-09-29 · Tyler Stevens].
- OCEAN fees: 1% for DATUM users, 2% for default OCEAN users [#4017 · 2025-02-12 · Dylan Seib].
- Dylan Seib: "Hard to put a price on the ability to use your own node for block templates" [#6594 · 2025-06-25 · Dylan Seib]. Building your own template also saves some fees [#4505 · 2025-03-13 · Travis Bitkle]. Tyler Stevens' reasoning: more hashrate heaters means more pool choice, and a heater paired with a full node can run DATUM [#2051 · 2024-11-19 · Tyler Stevens].
- A DATUM gateway can solo mine or mine on Ocean. One "solo mined" block via DATUM was actually pooled on Ocean using the miner's own templates. Full-reward, non-pooled mining is also possible with DATUM [#5799 · 2025-04-25 · Patrick Patel] [#5800 · 2025-04-25 · Patrick Patel] [#5803 · 2025-04-25 · Patrick Patel] [#5804 · 2025-04-25 · Dylan Seib] [#5807 · 2025-04-25 · Dane O].

### Node hardware and setup gotchas

- **Cheap node hardware.** One node is an old Dell Optiplex with $30 worth of new RAM and a $100 SSD, flashed with StartOS. Intel NUCs and small form factors are power-efficient alternatives [#1846 · 2024-11-06 · Tyler Stevens] [#1876 · 2024-11-06 · Dane O]. Another dedicated DATUM server runs on cheap hardware with StartOS [#4378 · 2025-03-03 · Nick]. Start 9 OS with DATUM on a $60 NUC took 12 hrs end to end, about 2 hrs of reading and downloading plus 10hrs of passive syncing [#2056 · 2024-11-20 · Dane O]. Small boxes can overheat: one Start9 node needed a big heat sink or active cooling [#1841 · 2024-11-06 · R D] [#1842 · 2024-11-06 · R D].
- **Knots conversion.** Switching a node from Core to Knots for DATUM required a fresh initial block download in two reports [#1934 · 2024-11-14 · Cody Harris] [#4365 · 2025-02-28 · Cody Harris]. After converting, open the config of every dependent service and click save to refresh its RPC credentials. "Otherwise nothing works" [#1937 · 2024-11-14 · Cody Harris].
- **Same-network gotcha.** A Loki rig on a Vonets Wi-Fi dongle, pointed at the DATUM port, silently defaulted to the OCEAN address. The miner must be on the same network as the DATUM gateway, which you can confirm in the threads/client tab of the DATUM GUI [#7306 · 2025-09-08 · Trevor Bello] [#7311 · 2025-09-08 · Mourad D.].
- **Incident.** One morning DATUM shares were reaching OCEAN, but a normal OCEAN address wasn't getting shares, while OCEAN reported everything normal [#3803 · 2025-01-30 · Cody Harris].
- **Stale templates.** Karl worried that if your node filters sub-1-sat transactions, it might take seconds to verify a new block while you hash a stale template [#7145 · 2025-08-20 · Karl]. Dylan expected the effect to be negligible, since the OCEAN share window is "8x the current difficulty worth of shares" and OCEAN's own templates filter <1sat/vB [#7146 · 2025-08-20 · Dylan Seib]. Mourad D. clarified that stale-template shares are accepted, but "will not count if block has advanced". The real risk is a slow server validating or fetching transactions [#7154 · 2025-08-21 · Mourad D.].

### Splits for installers

- A DATUM fork was in progress to split a percentage of miners' shares to different Ocean addresses, for revenue-share or hashrate-payment programs [#5151 · 2025-03-29 · Patrick Patel] [#5152 · 2025-03-29 · Patrick Patel]. By August 2025 DATUM hashrate splits were working, intended for splitting revenue between hashrate-heating installers and customers. Users of The Space's gateway were unaffected [#6927 · 2025-08-04 · Dylan Seib].
- Split syntax gotchas: % caused URL-encoding issues, so a tilde is used instead. Whatsminer's character limit allowed only 2 splits, maybe 3 depending on address type [#6930 · 2025-08-05 · Patrick Patel].

### Shared gateways: The Space and others

- The Space runs a DATUM gateway that builds block templates on its own node. The node is close to Knots, with datacarrier size raised to allow Whirlpool transactions [#4042 · 2025-02-13 · Dylan Seib]. It was offered at 1% fees at stratum+tcp://datum.denver.space:3333 [#6276 · 2025-05-30 · Travis Bitkle], and its configuration is documented on discourse.denver.space [#6803 · 2025-07-18 · Tyler Stevens]. A heater installer connected two clients to it [#4092 · 2025-02-15 · Toine Heat Reuse].
- Hashrate pointed at The Space's gateway (2025): 16-18 PH/s on 2025-04-10, over 20PH/s by 2025-04-15, 20225.83 TH/s per a reporting bot on 2025-04-17, and a 27PH/s peak on 2025-04-28 [#5417 · 2025-04-10 · Dylan Seib] [#5428 · 2025-04-11 · Dylan Seib] [#5526 · 2025-04-15 · Dylan Seib] [#5596 · 2025-04-17 · Dylan Seib] [#5843 · 2025-04-28 · Dylan Seib].
- For Undermine, a solo-mining "Hashrate Heatpunks" DATUM gateway was set up alongside The Space's pooled gateway [#4085 · 2025-02-15 · Dylan Seib] [#4094 · 2025-02-15 · Dylan Seib].
- Some heatpunks run their own DATUM gateway, and istheserverup.xyz was built to monitor The Space's DATUM [#7986 · 2025-11-26 · Travis Bitkle] [#8304 · 2025-12-16 · Dylan Seib]. When The Space's DATUM had problems in March 2026, Exergy's DATUM on the same network kept working, and stratum+tcp://mine.exergyheat.com:3334 was offered as a backup [#9708 · 2026-03-20 · Dylan Seib] [#9759 · 2026-03-27 · Dylan Seib].
- During the BIP-110 fork in August 2026, BIP-110 hit mandatory signaling at block 961,632. When Ocean mined a non-signaling block, BIP-110 nodes rejected it and forked off. With "less than 3%" miner support, the BIP-110 chain trails with virtually no hashrate [#10435 · 2026-08-08 · Christopher]. One heater owner pointed hashrate at Datum Denver during the fork [#10423 · 2026-08-08 · ₿ Minion].
- Tooling: an Ocean Mining Pool API repo was shared as a starting point for customer monitoring apps [#8509 · 2026-01-03 · Heatpunk Forum] [#8522 · 2026-01-03 · Travis Bitkle]. Exergy's HACS-installable Home Assistant integrations include pool integrations for OCEAN, DATUM and Public Pool [#8896 · 2026-01-27 · Heatpunk Forum]. Thermine, a Raspberry Pi platform, shows Ocean payouts and Lightning payouts [#7750 · 2025-11-14 · Gianluca L] [#8443 · 2025-12-26 · Gianluca L].

## Keeping the heat on when the pool is unreachable

- A heater that loses its pool stops making heat. Setting a last backup pool keeps the miner working (on BOS) during internet outages [#1041 · 2024-09-04 · Jonathan Y] [#1043 · 2024-09-04 · Brett Rowan]. A local node plus a local solo pool only really helps for 10-20 minute outages [#1052 · 2024-09-04 · Brett Rowan].
- The Braiins `drain://` pool URL burns hashrate locally when no pool is reachable, so the miner keeps producing heat [#3216 · 2025-01-08 · Brett Rowan] [#4024 · 2025-02-13 · Cody Harris]. An example entry is `drain://mine.ocean.xyz.3334`. Brett understands that any string works after `drain://` [#3235 · 2025-01-10 · Cody Harris] [#3236 · 2025-01-10 · Brett Rowan]. For installs in non-technical homes, this "limp mode" is the standard approach, and Epic UMC OS and Luxor have similar settings [#7931 · 2025-11-24 · Heatpunk Forum].
- Whatsminers have no drain-like option. A Raspberry Pi proxy acting as a local "drain" turned out harder than expected [#3217 · 2025-01-08 · Patrick Patel] [#4013 · 2025-02-12 · Patrick Patel] [#4020 · 2025-02-12 · Patrick Patel]. Details are in [Heater Firmware and Power Control](../firmware/heater-firmware-and-power-control.md).

> **Status: Disputed**
> In one test Vnish did not keep hashing offline, which suggested the behavior is Braiins-specific [#1073 · 2024-09-06 · Karl]. Others argued that pool handling should be the same across firmware [#1074 · 2024-09-06 · Brett Rowan] [#1094 · 2024-09-07 · Toine Heat Reuse]. Best assessment: test failover on your own firmware before relying on it for heat.

## Share difficulty

- Share difficulty changes how often shares are submitted, not the reward. Tune it to the mine's size so a large mine doesn't flood the pool and a tiny one isn't rarely heard from [#5246 · 2025-04-01 · Tyler Stevens] [#5247 · 2025-04-01 · Tyler Stevens]. Pool shares are like valid blocks at a lower difficulty, mirroring how network difficulty targeting works [#5252 · 2025-04-01 · Brett Rowan].
- In pooled mining a bad share matters less. For solo mining latency matters, which is one reason miners still want wired Ethernet [#3696 · 2025-01-21 · Dane O].

## Solo mining with heater hashrate

- The case for it: "Im already paying for the heat", so pointing hashrate at the "global hashrate lottery" makes sense [#7308 · 2025-09-08 · Trevor Bello].
- **Own-node setups.** Travis runs Public Pool for solo and the DATUM service for pooled mining. Both pull the same block template from his Knots service [#7307 · 2025-09-08 · Travis] [#7310 · 2025-09-08 · Travis].
- **Partial solo.** To send only part of your hashrate to solo, point one board at a different pool or use Braiins Pool Groups (LuxOS is likely similar) [#5459 · 2025-04-12 · Elijah Sanders] [#5462 · 2025-04-12 · Dylan Seib].
- **Testnet.** A Testnet4 solo option is stratum+tcp://solo4.antpoolandfriends.com:34255 with a TN4 address as the username, with "no guarantee it works or will stay up". The stratum-mining/sv2-apps repo has TN4 configs [#8863 · 2026-01-23 · Deleted Account] [#8805 · 2026-01-22 · Deleted Account].

### Hydrapool and Telehash

- Because Hydrapool is open source, the 256 Foundation instance accepts any username, including a nostr address linked to a profile [#8677 · 2026-01-15 · Tyler Stevens]. See [Hydrapool](hydrapool.md).
- Telehash #3, the 256 Foundation fundraiser, aimed to solo mine a block live during an 8 hour livestream starting Wed Jan 21 (2026) [#8675 · 2026-01-15 · Tyler Stevens] [#8767 · 2026-01-21 · Tyler Stevens]. It was extended thanks to donated hashrate from Elektron Energy and "1EH NiceHash" [#8801 · 2026-01-22 · Tyler Stevens].

## See Also

- [Pool Payout Schemes](pool-payout-schemes.md)
- [Hydrapool](hydrapool.md)
- [Decentralized Pool Designs](../protocols/decentralized-pool-designs.md)
- [Heater Firmware and Power Control](../firmware/heater-firmware-and-power-control.md)
- [Home Assistant Heater Control](../mining-software/home-assistant-heater-control.md)
- [Hashrate Heating Economics](../economics/hashrate-heating-economics.md)
- [Air-Cooled Hashrate Heating](../hardware/air-cooled-hashrate-heating.md)
- [Hashrate Heating Products and Installs](../industry/hashrate-heating-products-and-installs.md)
- [Heatpunks Community Timeline](../history/heatpunks-community-timeline.md)
- [Open Mining Economics](../economics/open-mining-economics.md)
