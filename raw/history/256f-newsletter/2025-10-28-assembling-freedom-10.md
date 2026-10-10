# Assembling Freedom #10

> Source: https://256foundation.substack.com/p/assembling-freedom-10
> Collected: 2026-10-07
> Published: 2025-10-28

*A monthly newsletter by 256 Foundation*

October 2025

**INTRODUCTION:**

Welcome to the tenth newsletter produced by The 256 Foundation and supported by [Proto](https://proto.xyz/)! You’ll notice a few changes in this edition: First, we have a new name for the newsletter, we are calling it “Assembling Freedom” as a nod to the God-given right of individuals to peaceably assemble and collectively express, promote, pursue, and defend their ideas. Also, the focus of this newsletter is to educate people on freedom tech and how to make and assemble tools they can use to defend their freedoms. Also, this one is shorter than you may be used to, we want to dial in the focus so the signal doesn’t get lost among too much information. September was a bit slower than recent months for freedom tech; note worthy events none the less include the ImagineIF summit, Tom’s Hardware featured the 256 Foundation, and our open-source projects are nearing completion. Dive into all the interesting things going on in and around the Bitcoin mining industry and catch up on the latest freedom tech news, free & open mining developments, 256 Foundation grant progress updates, and the current state of the Bitcoin network.

**FREEDOM TECH NEWS:**

**September 7**, a miner with 200Th/s solves block with [Solo CK Pool](https://x.com/ckpooldev/status/1964805627819204764). This was the 307<sup>th</sup> block find for Solo CK Pool and a miner with 200Th/s has approximately a 1 in 36,000 chance per day of solving a block. Interestingly, the miner seems to have added a few more miners to their operation after the block find, with the [SoloStats Page](https://solostats.ckpool.org/users/bc1qtfrexlhl2099rkqdcr56hjt6ukyhqylvdajr38) showing a total of 19 workers in the historical records with 10 of those currently running for a total of 646Th/s. The worker named “Blockbuster” appears to be the one responsible for the block find judging by the highest reported difficulty of 187.32T and this worker is only a \~38Th/s unit. Proving once again that anyone can acquire Bitcoin permissionlessly through mining.

**September 20**, the inaugural ImagineIF Summit took place in Nashville bringing together investors, engineers, policymakers, and entrepreneurs for two days to talk about the intersection of Bitcoin, AI, energy, and freedom tech. econoalchemist presented “*[Freedom Tech is Fundamental to a Free Society](https://x.com/bitcoinpark_/status/1969447429759254614)*” in closing out the second day’s event (presentation starts at the 12:20 mark). This brief presentation highlights how all governments trend toward totalitarianism and the role freedom tech plays in defending your God-given rights. For example, the right to free speech, the right to own property, the right to privacy, and the right to transact; tools like Bitcoin, Tor, and GrapheneOS are becoming more important to understand in an increasingly digital world where the technological conveniences that facilitate faster transactions and instant communication have been turned into surveillance apparatuses used against us. Supporting open-source developers is crucial as there is no freedom tech without them and without freedom tech there is no free society.

**FREE & OPEN MINING DEVELOPMENTS:**

**September 2**, [256 Foundation](https://x.com/256FOUNDATION/status/1962964157793206578) takes possession of the 256,000 Intel BZM2 ASIC chips donated by Proto Mining. These chips were originally produced roughly 3-years ago and have approximately the same efficiency as the chips found in Antminer S19j Pro miners. These chips give developers an opportunity to make new Bitcoin mining-related projects a reality. For example, [@Real\_PizzAndy](https://x.com/Real_PizzAndy/status/1965478792002175309) was one of the recipients and he is planning on building a 3D printer that mines Bitcoin to generate the heat needed in the printer bed. To date all of the donated chips have been disbursed. Unfortunately, technical documentation for the chips could not be included in the donation however, there is an Intel BZM2-based Bitaxe in the works as well as the next Ember One which will also feature the BZM2 chips and once those projects are released, they will include the accompanying relevant documentation. Additionally, there is a group of individuals separate from the 256 Foundation who are working on creating a sub-set of the complete Intel BZM2 documentation that can be released open-source. We do anticipate receiving more Intel BZM2 chips in the future and look forward to not having to un-solder ASIC chips from existing hashboards in order to harvest the chips for new open-source designs. Tom’s Hardware published an article covering the news of the donation [here](https://www.tomshardware.com/tech-industry/semiconductors/intel-bzm2-block-sale-chips-return-from-dead).

**September 29**, Tyler Stevens has been making progress this month using an Avalon Mini 3 and an Avalon Q to heat The Space Denver’s facility. You can see how it started earlier this month with an external radio frequency temperature sensor talking to Home Assistant integration [here](https://x.com/tylerkstevens/status/1962892047322698200); and you can see how the progress is going [here](https://x.com/tylerkstevens/status/1972663945614807499). Tyler is able to automatically maintain a comfortable 77°F (+/- 1°F) by pre-heating the first-floor furnace intake air with an Avalon Q while the furnace runs in circulate mode to keep the warm air cycling through the vents. On the second floor, there is a HoneyWell smart thermostat which communicates with Home Assistant to let it know when the miners are not keeping up with the demand for the current temperature setting, at which point the furnace will supplement the needed heat with the standard natural gas. Saving the Space on utility bills and mining Bitcoin at the same time. If you are interested in learning more about using Bitcoin miners to heat your space, check out the resources available at [heatpunks.org](https://heatpunks.org/t/canaan-avalon-home-miner-apis/168).

**GRANT PROJECT UPDATES:**

**Ember One**Ember One 00 (with the Bitmain BM1362 ASICs) is now on v5, which is available on GitHub as a release candidate

[here](https://github.com/256-Foundation/emberone00-pcb/tree/v5). This version includes an upgraded voltage regulator that enables live monitoring of power metrics and cleans up the real estate on the board with the removal of the large inductors. The biggest trade off is that the input voltage range has been narrowed from 12-24vdc down to 12-17vdc. The latest version still needs to be prototyped and validated before it is officially released. The validation process will include testing the over-voltage protection circuit, which could potentially sacrifice one of the prototype boards. Materials have been ordered to build 5 prototypes, which should be finished before the end of October. After the prototyping phase, so long as everything passes the validation, then there will be a small batch of \~100 units produced specifically for testers and developers to tinker with and help us figure out the best reference power supplies, fans, and heatsinks to use. You can learn more about Ember One

[here](https://emberone.org/).

**Libre Board**We recorded a nearly 2-hour schematic review of the Libre Board, you can find it

[here](https://x.com/bitcoinpark_/status/1970898158965358809)or

[here](https://bitcointv.com/w/k7gpGT44UJ9uroY7D88UcR). Joining the conversation was Schnitzel, Skot, Ryan, and econoalchemist. The conversation revolves around the final review of the Libre Board, focusing on critical aspects such as ground vias, voltage regulators, thermal management, USB-C power negotiation, LED indicators, and I2C connections. The team discusses the importance of documentation for users transitioning from Raspberry Pi, the need for effective thermal management, and the implications of design decisions on user experience. Collaboration and communication are emphasized as essential elements in the hardware development process. This conversation delves into the intricacies of Raspberry Pi connectivity, focusing on the challenges and solutions related to I2C bus management, GPIO pin multifunctionality, and the integration of QUIC connectors. The discussion also covers fan control, LED timing requirements, and the importance of effective communication in collaborative design processes, culminating in considerations for prototyping and PCB design. Currently, prototype materials for the Libre Board are on order and we should be able to start the validation process within roughly a month depending on when the materials arrive. You can learn more about Libre Board

[here](https://libreboard.org/).

**Mujina Firmware**Ryan has been chipping away on Munija Firmware utilizing an Ember One 00 v4.1 prototype board. Mujina is built for flexibility and modularity. For example, if a user wants to run a hashboard with Bitmain chips along side a hashboard with Intel chips, then Mujina will be able to automatically detect that and adjust workloads accordingly so that the available bits to roll in various fields such as nonce, time, version, etc. are made available to each chip depending on it’s capabilities. We are anticipating to have an initial Mujina release ready by the time the first production batch of Ember Ones rolls out. The Mujina repository will also be made publicly available at that time. You can learn more about Mujina

[here](https://mujina.org/).

**Hydra Pool**Jungly makes an appearance on the

[Stephan Livera podcast](https://x.com/stephanlivera/status/1964571871355023461)to talk about decentralizing Bitcoin mining with P2Pool v2, which ties in nicely with the work done on Hydra Pool in that eventually, multiple Hydra Pool instances will be able to combine work for shared rewards. Jungly discusses his work on P2Pool v2, a decentralized mining pool aimed at improving upon the limitations of the original P2Pool. He emphasizes the importance of decentralization in Bitcoin mining and explains the technical innovations that P2Pool v2 introduces, such as sharechains and atomic swaps for non-custodial payouts. Jungly also highlights the need for community involvement and developer engagement to ensure the project’s success, and he shares his vision for a more accessible and efficient mining ecosystem. Going back to Hydra Pool specifically, the Stratum sever component is finished, including the details that make it work such as defining how the PPLNS calculations are made, how the validated shares will be exposed for end-users to verify the pool operator is being honest, and defining how the difficulty is calculated and returned to the miners. We are currently cleaning up the code to make it more presentable and developer friendly, then we are ready to make the initial release and spin up a test server for people to try out and help us test the system on Bitcoin mainnet. We will also update the website with detailed installation instructions for those who want to try operating their own Hydra Pool instance. You can learn more

[here](https://hydrapool.org/).

**STATE OF THE NETWORK:**

Hashrate on the 7-day MA according to [mempool.space](https://mempool.space/graphs/mining/hashrate-difficulty#1y) increased from \~969 Eh/s on the first day of September to \~1,060 Eh/s (1.06 Zh/s) by the end of the month, marking roughly +9.4% increase for the month. The year to date hashrate difference is +34.8% using the 7-day MA up until the last day of September.

Difficulty only went up in September, starting the month at 129.7T and finishing at 142.3T, marking a 9.7% increase for the month. All together for 2025 up to Epoch #455, difficulty has gone up \~29.6%.

According to the [Hashrate Index](https://data.hashrateindex.com/asic-index-data/price-index), new-gen ASIC prices have increased slightly over the last month. The more efficient miners like the \<19 J/Th models are now fetching $14.11/Th, up from $13.96/Th last month. Models between 19J/Th – 25J/Th are selling for $4.75/Th, way down from $8.57/Th at the beginning of the month. Models >25J/Th are stable in price, hovering around $3.52/Th now compared to $3.92/Th last month.

Hashvalue over the month of September dropped from \~48k sats/Ph/day down to \~44.5k sats/Ph/day by the end of the month, according to the [Braiins Insights](https://insights.braiins.com/en) dashboard.

The next halving will occur at block height 1,050,000 which should be around March 29, 2028 in roughly 895 days or in other words \~130,600 blocks from the the time this newsletter is published.

CONCLUSION: Thank you for reading the tenth 256 Foundation newsletter. Keep an eye out for more newsletters on a monthly basis in your email inbox by subscribing at [256foundation.org](https://256foundation.org). Or you can download .pdf versions of the newsletters from there as well. You can also find these newsletters published in article form on Nostr.

Live Free or Die,

-econoalchemist
