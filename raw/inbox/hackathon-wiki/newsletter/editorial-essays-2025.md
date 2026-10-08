# Editorial Essays and Arguments, 2025

> Sources: 256 Foundation (newsletter #5, May 2025), 2025-05-05; 256 Foundation (newsletter #6, June 2025), 2025-06-19; 256 Foundation (newsletter #7, July 2025), 2025-07-15; 256 Foundation (newsletter #8, August 2025), 2025-08-18; 256 Foundation (newsletter #9, September 2025), 2025-09-25; 256 Foundation (Assembling Freedom #10), 2025-10-28; 256 Foundation (Assembling Freedom #11), 2025-11-24; 256 Foundation (Assembling Freedom #12), 2025-12-22
> Raw: [Newsletter May 2025](../../raw/newsletter/2025-05-05-bitcoin-mining-will-not-be-decentralized-until-it-is-open-so.md); [Newsletter June 2025](../../raw/newsletter/2025-06-19-you-know-i-m-something-of-a-decentralized-pool-myself.md); [Newsletter July 2025](../../raw/newsletter/2025-07-15-the-bigger-they-are-the-harder-they-fall.md); [Newsletter August 2025](../../raw/newsletter/2025-08-18-is-open-source-communism.md); [Newsletter September 2025](../../raw/newsletter/2025-09-25-rig-bitcoin-mining-re-imagined.md); [Assembling Freedom #10](../../raw/newsletter/2025-10-28-assembling-freedom-10.md); [Assembling Freedom #11](../../raw/newsletter/2025-11-24-assembling-freedom-11.md); [Assembling Freedom #12](../../raw/newsletter/2025-12-22-assembling-freedom-12.md)
> Updated: 2026-10-07

## Overview

The 2025 newsletters were written in the first person by econoalchemist and carried opinions as well as news. Four issues were titled as essays: *Bitcoin Mining Will Not Be Decentralized Until It Is Open Sourced* (May), *You know, I'm Something of a Decentralized Pool Myself* (June), *The Bigger They Are, The Harder They Fall* (July) and *Is Open Source Communism?* (August). This page sets out the arguments they make. The common thread is that closed, proprietary mining systems are fragile and that open hardware, firmware and pools are the only real path to decentralized mining. These are the author's views. They are recorded here as arguments, not as settled facts.

## Mining needs open source to decentralize (May)

The May issue argues from two events in April.

- **Pool concentration.** Researcher B10C published an analysis showing that only six pools mine more than 95% of blocks. From 2019 to 2022 the top two pools held about 35% of hashrate and the top six about 75%. By December 2023 that had grown to 55% and about 90%. B10C noted that home mining helps but is still negligible next to industrial hashrate.
- **Vendor control.** Bitmain released an S21+ firmware update that blocks connections to the OCEAN and Braiins pools. The newsletter places this in a longer list of Bitmain behavior: Antbleed, Covert ASIC Boost, the Fork Wars, mining empty blocks and removing SD card slots.

The conclusion drawn: a mining business built on closed Bitmain hardware sits on a fragile base. Miners need to adapt instantly, and only open-source mining gives them that freedom. The issue also sees promise in what people already do with closed hardware. Rev.Hodl's home heating builds are offered as a sign of what will come once hardware and firmware are open.

## Centralized pools will not decentralize mining (June)

The June issue responds to Antpool, Bitmain's pool, announcing that it would let miners build their own block templates while keeping FPPS payouts. The newsletter is blunt: "centralized pools will never decentralize Bitcoin mining".

The reasoning runs in steps.

1. FPPS pays miners steadily even though block finds are irregular. A pool needs very large bitcoin reserves to cover runs of bad luck.
2. Pool operators that cannot afford those reserves ask Antpool to bankroll them and become proxy pools. The newsletter lists pools it says Antpool absorbed this way, including Poolin, Braiins, Binance Pool, Luxor and CloverPool.
3. FPPS creates two problems: custody and templates. Both raise the risk of censorship. A custodian can pressure pool operators, and a pool operator decides which transactions go in the template.
4. Letting miners build templates is a good step. But a central pool still counts the shares and coordinates the payouts. It can refuse shares built on a template it dislikes, or exclude a payout address.

The issue points out that Bitmain warned that 58% of hashrate is controlled by two pools without mentioning that Antpool and its proxies make up roughly 40% of the network. It adds that DATUM and Stratum v2 are good steps, but that OCEAN's marketing has overstated their effect.

The July issue repeats the point when noting that Spiral was hiring a senior engineer for Stratum v2. It credits Stratum v2 with encrypted connections, lower bandwidth and miner-built templates. It then adds the caveat that decentralization is overstated while central pools still handle share accounting and coinbase payouts. It says Spiral and the Stratum v2 team have been more straightforward in their marketing than OCEAN. More detail on pools is in [Open Mining Ecosystem News, 2025 to 2026](open-mining-ecosystem-news.md).

## Closed systems are the empire's weak point (July)

The July issue's theme is that systems built to block access to freedom tech are the proprietary mining industry's greatest weakness. Several pieces support it.

- **Luxor and AntPool.** On June 5 researcher boerst showed that Luxor briefly sent miners a block template tagged "Mined by AntPool" in place of "Powered by Luxor Tech". His shares on that template were still accepted. The newsletter takes this as confirmation that Luxor is an AntPool proxy, and asks how pool tags can be trusted at all.
- **Words matter.** A Secret Service post treated CoinJoin as a kind of mixer. The newsletter insists on the difference. In a mixer, users send coins to a custodian. A CoinJoin is a collaborative transaction where nobody else ever takes custody. The author argues that blurred terms are how prosecutors stretch laws to cover developers. See [Samourai Wallet Case and Developer Liability](samourai-wallet-case.md).
- **Skepticism about legislation.** The author doubts that folding the Blockchain Regulatory Certainty Act into the CLARITY Act, as Section 110, changes anything for developers already charged. FinCEN's 2019 guidance already said developers need no money transmitter license, and prosecutors argued that FinCEN's opinion did not matter.
- **Knock-offs and liability.** After a miner posing as a Bitaxe exploded on June 16, the issue warns that clones swap in cheaper, untested parts. It then turns the question around. If a genuine Bitaxe ever caused damage, distributors and manufacturers would be on the line. The author expects pressure for UL or CPSC testing and for product liability insurance, and thinks the project will have to face this sooner rather than later.

## Open-source licenses only work when respected (May, July, November)

The May issue summarizes a Solo Satoshi article on Bitaxe clones. Bitaxe hardware is licensed CERN-OHL-S and its firmware GPLv3. Both require derivative works to publish their source. When a maker ignores that, buyers get undocumented changes, such as overheating or Wi-Fi faults, and community volunteers waste time trying to reproduce problems on hardware nobody can identify. The newsletter's line is that the licenses protect the user's freedom, and that freedom disappears when the license is ignored. It points buyers to the list of legitimate sellers on the Bitaxe website.

The November issue, summarizing POD256, returns to licensing. It contrasts permissive MIT licenses with copyleft licenses (GPL and OHL), argues for sharing editable CAD files such as KiCad instead of PDFs or Gerbers, and rejects the idea that open source must mean non-profit. It also reports that two Chinese entities were trying to register the Bitaxe trademark in the US, which Skot was formally opposing. Background on the project is in [Bitaxe and Open Source Miners United](../ecosystem/bitaxe-and-osmu.md).

## Is open source communism? (August)

The August issue answers a meme that says "Open source is communism for intellectual property". The author takes the real question to be whether open source and private property exclude each other, and answers in five parts.

1. **Voluntary, not imposed.** Communism as practiced meant state control and abolishing private property by force. Open source is a choice. A developer who releases code under a license such as MIT keeps ownership and grants permissions, much as a landlord rents out a property and keeps the title.
2. **Intellectual property is managed, not abolished.** Open source works inside intellectual property law. The GPL keeps derivative works open but still recognizes the creator's copyright. Companies such as Red Hat and Canonical make money from support and services around open code. The newsletter says finding business opportunities on an open base is central to the foundation's vision.
3. **Economic benefits.** A 2025 Linux Foundation report on the economic value of open source cites cost savings, faster development and interoperability. Firms invest private money in infrastructure and talent to build on shared code.
4. **Fit with property rights.** Libertarian writers such as Stephan Kinsella argue that patents and copyrights are state-granted monopolies. Ideas are non-rivalrous: one person using them does not leave less for others. Open source rejects artificial scarcity in ideas without abolishing property rights.
5. **Flipping the meme.** The author's reply: "Open-source isn’t communism; it’s capitalism’s evolution." Proprietary software, held behind paywalls and legal threats, is described as closer to a state-enforced monopoly.

The essay ends by listing the freedoms open source gives users: to run, copy, distribute, study, change and improve the software.

## Platform control (September)

The September issue criticizes two Google moves from August. First, a Google Play policy appeared to require licenses from wallet developers. Google later clarified that non-custodial wallets were out of scope. Second, Google outlined an Android developer verification process that requires government identity documents and would stop Android devices that use Google services from running side-loaded apps by default. The newsletter sums it up as your device but their rules, and notes that developers could no longer publish under a pseudonym through the Play Store. It adds that people who flash an alternative system such as GrapheneOS can still install apps from anywhere.

## Freedom tech as a foundation of a free society (October to December)

- The October issue explains the new name, Assembling Freedom. It refers to the right of individuals to peaceably assemble, and to the newsletter's aim of teaching people to make and assemble tools that defend their freedoms.
- At the ImagineIF Summit econoalchemist gave a talk titled "Freedom Tech is Fundamental to a Free Society". Its argument: all governments trend toward totalitarianism, digital conveniences have been turned into surveillance tools, and tools like Bitcoin, Tor and GrapheneOS protect speech, property, privacy and the right to transact. Without open-source developers there is no freedom tech.
- The December issue closes the year on the Samourai Wallet case and the line "code does not equal crime". It holds that tool makers should not be liable for what end users do.

## See Also

- [Foundation Progress Timeline, 2025](foundation-progress-2025.md)
- [Samourai Wallet Case and Developer Liability](samourai-wallet-case.md)
- [Open Mining Ecosystem News, 2025 to 2026](open-mining-ecosystem-news.md)
- [256 Foundation: Mission and Organization](../foundation/mission-and-organization.md)
- [Bitaxe and Open Source Miners United](../ecosystem/bitaxe-and-osmu.md)
