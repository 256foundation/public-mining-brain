# Bitcoin Mining Will Not Be Decentralized Until It Is Open Sourced

> Source: https://256foundation.substack.com/p/bitcoin-mining-will-not-be-decentralized
> Collected: 2026-10-07
> Published: 2025-05-05

*A monthly newsletter by The 256 Foundation*

May 2025

### **Introduction:**

Welcome to the fifth newsletter produced by The 256 Foundation! April was a jam-packed month for the Foundation with events ranging from launching three grant projects to the first official Ember One release. The 256 Foundation has been laser focused on our mission to dismantle the proprietary mining empire, signing off on a productive month with the one-finger salute to the incumbent mining cartel.

Dive in to catch up on the latest news, mining industry developments, progress updates on grant projects, Actionable Advice on helping test Hydra Pool, and the current state of the Bitcoin network.

Definitions:

DOJ = Department of Justice

SDNY = Southern District of New York

BTC = Bitcoin

SD = Secure Digital

Th/s = Terahash per second

OSMU = Open Source Miners United

tx = transaction

PSBT = Partially Signed Bitcoin Transaction

FIFO = First In First Out

PPLNS = Pay Per Last N Shares

GB = Gigabyte

RAM = Random Access Memory

ASIC = Application Specific Integrated Circuit

Eh/s = Exahash per second

Ph/s = Petahash per second

### **News:**

**April 7**, the first of a few notable news items that relate to the Samourai Wallet case, the US Deputy Attorney General, Todd Blanche, issued a memorandum titled “[Ending Regulation By Prosecution](https://www.defieducationfund.org/_files/ugd/84ba66_4278778963f14119be0ef1c7976bc3b2.pdf)”. The memo makes the DOJ’s position on the matter crystal clear, stating; “Specifically, the Department will no longer target virtual currency exchanges, mixing and tumbling services, and offline wallets for the acts of their end users or unwitting violations of regulations…”. However, despite the clarity from the DOJ, the SDNY (sometimes referred to as the “Sovereign District” for it’s history of acting independently of the DOJ) has yet to budge on dropping the charges against the Samourai Wallet developers. Many are baffled at the SDNY’s continued defiance of the Trump Administration’s directives, especially in light of the recent suspensions and resignations that swept through the SDNY office in the wake of several attorneys refusing to comply with the DOJ’s directive to drop the charges against New York City Mayor, Eric Adams. There is speculation that the missing piece was Trump’s pick to take the helm at the SDNY, [Jay Clayton](https://decrypt.co/315876/jay-clayton-takes-helm-at-sdny-returning-to-government-with-crypto-record-in-tow), who was yet to receive his Senate confirmation and didn’t officially start in his new role until April 22. In light of the Blanche Memo, on April 29, the prosecution and defense [jointly filed a letter](https://cointelegraph.com/news/samourai-wallet-feds-ask-for-time-consider-dropping-crypto-mixer-case) requesting additional time for the prosecution to determine it’s position on the matter and decide if they are going to do the right thing, comply with the DOJ, and drop the charges. Catch up on what’s at stake in this case with an appearance by [Diverter on the Unbounded Podcast](https://x.com/TheUNBOUNDEDPod/status/1915451508717498827) from April 24, the one-year anniversary of the Samourai Wallet developer’s arrest. This is the most important case facing Bitcoiners as the precedence set in this matter will have ripple effects that touch all areas of the ecosystem. The logic used by SDNY prosecutors argues that non-custodial wallet developers transfer money in the same way a frying pan transfers heat but does not “control” the heat. Essentially saying that facilitating the transfer of funds on behalf of the public by any means constitutes money transmission and thus requires a money transmitter license. All non-custodial wallets (software or hardware), node operators, and even miners would fall neatly into these dangerously generalized and vague definitions. If the SDNY wins this case, all Bitcoiners lose. Make a contribution to the defense fund [here](https://p2prights.org/donate.html).

**April 11**, solo miner with \~230Th/s [solves Block #891952](https://x.com/ckpooldev/status/1910809325834236347) on Solo CK Pool, bagging 3.11 BTC in the process. This will never not be exciting to see a regular person with a modest amount of hashrate risk it all and reap all the mining reward. The more solo miners there are out there, the more often this should occur.

**April 15**, [B10C](https://b10c.me/blog/015-bitcoin-mining-centralization/) publishes new article on mining centralization. The article analyzes the hashrate share of the currently five biggest pools and presents a Mining Centralization Index. The results demonstrate that only six pools are mining more than 95% of the blocks on the Bitcoin Network. The article goes on to explain that during the period between 2019 and 2022, the top two pools had \~35% of the network hashrate and the top six pools had \~75%. By December 2023 those numbers grew to the top two pools having 55% of the network hashrate and the top six having \~90%. Currently, the top six pools are mining \~95% of the blocks.

B10C concludes the article with a solution that is worth highlighting: “More individuals home-mining with small miners help too, however, the home-mining hashrate is currently still negligible compared to the industrial hashrate.”

**April 15**, As if miner centralization and proprietary hardware weren’t reason enough to focus on open-source mining solutions, leave it to Bitmain to release an S21+ firmware update that [blocks connections](https://x.com/Singekino_Miner/status/1912154613295313080) to OCEAN and Braiins pools. This is the latest known sketchy development from Bitmain following years of shady behavior like Antbleed where miners would phone home, Covert ASIC Boost where miners could use a cryptographic trick to increase efficiency, the infamous Fork Wars, mining empty blocks, and removing the SD card slots. For a mining business to build it’s entire operation on a fragile foundation like the closed and proprietary Bitmain hardware is asking for trouble. Bitcoin miners need to remain flexible and agile and they need to be able to adapt to changes instantly – the sort of freedoms that only open-source Bitcoin mining solutions are bringing to the table.

### **Free & Open Mining Industry Developments:**

The development will not stop until Bitcoin mining is free and open… and then it will get even better. Innovators did not disappoint in April, here are nine note-worthy events:

**April 5**, 256 Foundation [officially launches](https://x.com/256FOUNDATION/status/1908585602968170598) three more grant projects. These will be covered in detail in the Grant Project Updates section but April 5 was a symbolic day to mark the official start because of the [6102](https://en.wikipedia.org/wiki/Executive_Order_6102) anniversary. A reminder of the asymmetric advantage freedom tech like Bitcoin empowers individuals with to protect their rights and freedoms, with open-source development being central to those ends.

**April 5**, Low profile ICE Tower+ for the Bitaxe Gamma 601 introduced by [@Pleb\_Style](https://x.com/Pleb_Style/status/1908406781526651291) featuring four heat pipes, 2 copper shims, and a 60mm Noctua fan resulting in up to 2Th/s. European customers can pick up the complete upgrade kit from the Pleb Style [online store](https://pleb.style/en-am/products/argon-thrml-60-upgrade-kit-ultimate-cooling-for-maximum-performance-en) for $93.00.

**April 8**, Solo Satoshi spells out issues with Bitaxe knockoffs, like Lucky Miner, in a detailed article titled *[The Hidden Cost of Bitaxe Clones](https://www.solosatoshi.com/the-hidden-cost-of-bitaxe-clones-how-knock-offs-threaten-the-open-source-mining-revolution/)*. This concept can be confusing for some people initially, Bitaxe is open-source, right? So anyone can do whatever they want… right? Based on the specific open-source license of the Bitaxe hardware, [CERN-OHL-S](https://opensource.org/license/cern-ohl-s), and the firmware, [GPLv3](https://www.gnu.org/licenses/gpl-3.0.html), derivative works are supposed to make the source available. Respecting the license creates a feed back loop where those who benefit from the open-source work of those who came before them contribute back their own modifications and source files to the open-source community so that others can benefit from the new developments. Unfortunately, when the license is disrespected what ends up happening is that manufacturers make undocumented changes to the components in the hardware and firmware which yields unexpected results creating a number of issues like the Bitaxe overheating, not connecting to WiFi, or flat out failure. This issue gets further compounded when the people who purchased the knockoffs go to a community support forum, like [OSMU](https://discord.com/invite/osmu), for help. There, a number of people rack their brains and spend their valuable time trying to replicate the issues only to find out that they cannot replicate the issues since the person who purchased the knockoff has something different than the known Bitaxe model and the distributor who sold the knockoff did not document those changes. The open-source licenses are maintaining the end-users’ freedom to do what they want but if the license is disrespected then that freedom vanishes along with details about whatever was changed. There is a list maintained on the Bitaxe website of legitimate distributors who uphold the open-source licenses, if you want to buy a Bitaxe, use [this list](https://bitaxe.org/buy) to ensure the open-source community is being supported instead of leeched off of.

**April 8**, The [Mempool Open Source Project v3.2.0](https://x.com/mempool/status/1909532932211138574) launches with a number of highlights including a new UTXO bubble chart, address poisoning detection, and a tx/PSBT preview feature. The GitHub repo can be found [here](https://github.com/mempool/mempool/releases/tag/v3.2.0) if you want to self-host an instance from your own node or you can access the website [here](https://mempool.space/). The Mempool Open Source Project is a great blockchain explorer with a rich feature set and helpful visualization tools.

**April 8**, [@k1ix](https://x.com/k1ix) publishes bitaxe-raw, a firmware for the ESP32S3 found on Bitaxes which enables the user to send and receive raw bytes over USB serial to and from the Bitaxe. This is a helpful tool for research and development and a tool that is being leveraged at The 256 Foundation for helping with the Mujina miner firmware development. The bitaxe-raw GitHub repo can be found [here](https://github.com/bitaxeorg/bitaxe-raw).

**April 14**, Rev.Hodl [compiles](https://njump.me/nevent1qqsx0llnhlflz8vz9z5djem3jft66szul5u8mgxhvedeexlgu7nqedspz9mhxue69uhkummnw3ezuamfdejj7q3qf5pre6wl6ad87vr4hr5wppqq30sh58m4p33mthnjreh03qadcajsxpqqqqqqzwwc8lt) many of his homestead-meets-mining adaptations including how he cooks meat sous-vide style, heats his tap water to 150°F, runs a hashing space heater, and how he upgraded his clothes dryer to use Bitcoin miners. If you are interested in seeing some creative and resourceful home mining integrations, look no further. The fact that Rev.Hodl was able to do all this with closed-source proprietary Bitcoin mining hardware makes a very bullish case for the innovations coming down the pike once the hardware and firmware are open-source and people can gain full control over their mining appliances.

**April 21**, [Hashpool](https://x.com/btchashpool) explained on [The Home Mining Podcast](https://www.youtube.com/watch?v=1Ueuop27bko), an innovative Bitcoin mining pool development that trades mining shares for ecash tokens. The pool issues an “ehash” token for every submitted share, the pool uses ecash epochs to approximate the age of those shares in a FIFO order as they accrue value, a rotating key set is used to eventually expire them, and finally the pool publishes verification proofs for each epoch and each solved block. The ehash is provably not inflatable and payouts are similar to the PPLNS model. In addition to the maturity window where ehash tokens are accruing value, there is also a redemption window where the ehash tokens can be traded in to the mint for bitcoin. There is also a bitcoin++ [presentation](https://x.com/btcplusplus/status/1882512931595960511) from earlier this year where @vnprc explains the architecture.

**April 26**, [Boerst](https://x.com/boerst/status/1916262402791743688) adds a new page on [stratum.work](https://stratum.work/) for block template details, you can click on any mining pool and see the extended details and visualization of their current block template. Updates happen in real-time. The page displays all available template data including the OP\_RETURN field and if the pool is merge mining, like with RSK, then that will be displayed too. Stratum dot work is a great project that offers helpful mining insights, be sure to book mark it if you haven’t already.

**April 27**, Public Pool patches [Nerdminer exploit](https://findtheblock.com/blog/the-nerdminer-hack-nobodys-talking-about-and-why-you-should-stay-away) that made it possible to create the impression that a user’s Nerdminer was hashing many times more than it actually was. This exploit was used by scammers trying to convince people that they had a special firmware for the Nerminer that would make it hash much better. In actuality, Public Pool just wasn’t checking to see if submitted shares were duplicates or not. The scammers would just tweak the Nerdminer firmware so that valid shares were getting submitted five times, creating the impression that the miner was hashing at five times the actual hashrate. Thankfully this has been uncovered by the open-source community and Public Pool quickly addressed it on their end.

### **Grant Project Updates:**

Three grant projects were [launched](https://x.com/256FOUNDATION/status/1908585602968170598) on April 5, Mujina Mining Firmware, Hydra Pool, and Libre Board. Ember One was the first fully funded grant and launched in November 2024 for a six month duration.

**Ember One:**

[@skot9000](https://x.com/skot9000) is the lead engineer on the Ember One and April 30 marked the conclusion of the first grant cycle after six months of development culminating in a standardized hashboard featuring a \~100W power consumption, 12-24v input voltage range, USB-C data communication, on-board temperature sensors, and a 125mm x 125mm formfactor. There are several Ember One versions on the road map, each with a different kind of ASIC chip but staying true to the standardized features listed above. The first Ember One, the 00 version, was built with the Bitmain BM1362 ASIC chips. The first official release of the Ember One, v3, is available [here](https://github.com/256-Foundation/emberone00-pcb/releases/tag/v3-release). v4 is already being worked on and will incorporate a few circuit safety mechanisms that are pretty exciting, like protecting the ASIC chips in the event of a power supply failure. The firmware for the USB adaptor is available [here](https://github.com/256-Foundation/emberone-usbserial-fw). Initial testing firmware for the Ember One 00 can be found [here](https://github.com/skot/emberone-miner/tree/emberone-BM1362-support) and full firmware support will be coming soon with Mujina. The Ember One does not have an on-board controller so a separate, USB connected, control board is required. Control board support is coming soon with the Libre Board. There is an in-depth schematic review that was recorded with Skot and Ryan, the lead developer for Mujina, you can see that video [here](https://bitcointv.com/w/59cB1SEHPYZCdumE2MFnqF). Timing for starting the second Ember One cycle is to be determined but the next version of the Ember One is planned to have the Intel BZM2 ASICs. Learn more at [emberone.org](https://emberone.org/)

**Mujina Mining Firmware:**

[@ryankuester](https://x.com/ryankuester) is the lead developer for the Mujina firmware project and since the project launched on April 5, he has been working diligently to build this firmware from scratch in Rust. By using the bitaxe-raw firmware mentioned above, over the last month Ryan has been able to use a Bitaxe to simulate an Ember One so that he can start building the necessary interfaces to communicate with the range of sensors, ASICs, work handling, and API requests that will be necessary. For example, using a logic analyzer, this is what the first signs of life look like when communicating with an ASIC chip, the orange trace is a message being sent to the ASIC and the red trace below it is the ASIC responding \[IMG-006\]. The next step is to see if work can be sent to the ASIC and results returned. The GitHub repo for Mujina is currently set to private until a solid foundation has been built. Learn more at [mujina.org](https://mujina.org/)

**Libre Board:**

[@Schnitzel](https://x.com/Schnitzel) is the lead engineer for the Libre Board project and over the last month has been modifying the [Raspberry Pi Compute Module I/O Board](https://www.raspberrypi.com/products/compute-module-4-io-board/) open-source design to fit the requirements for this project. For example, removing one of the two HDMI ports, adding the 40-pin header, and adapting the voltage regulator circuit so that it can accept the same 12-24vdc range as the Ember One hashboards. The GitHub repo can be found [here](https://github.com/256-Foundation/Libre-Board), although there isn’t much to look at yet as the designs are still in the works. If you have feature requests, creating an issue in the GitHub repo would be a good place to start. Learn more at [libreboard.org](https://libreboard.org/)

**Hydra Pool:**

[@jungly](https://x.com/jungly)is the lead developer for Hydra Pool and over the last month he has developed a working early version of Hydra Pool specifically for the upcoming Telehash #2. Forked from CK Pool, this early version has been modified so that the payout goes to the 256 Foundation bitcoin address automatically. This way, users who are supporting the funderaiser with their hashrate do not need to copy/paste in the bitcoin address, they can just use any vanity username they want. Jungly was also able to get a great looking statistics dashboard forked from

[CKstats](https://github.com/mrv777/ckstats)and modify it so that the data is populated from the Hydra Pool server instead of website crawling. After the Telehash, the next steps will be setting up deployment scripts for running Hydra Pool on a cloud server, support for storing shares in a database, and adding PPLNS support. The 256 Foundation is only running a publicly accessible server for the Telehash and the long term goals for Hydra Pool are that the users host their own instance. The 256 Foundation has no plans on becoming a mining pool operator. The following Actionable Advice column shows you how you can help test Hydra Pool. The GitHub repo for Hydra Pool can be found

[here](https://github.com/256-Foundation/Hydra-Pool). Learn more at

[hydrapool.org](https://hydrapool.org/)

### **Actionable Advice:**

The 256 Foundation is looking for testers to help try out Hydra Pool. The current instance is on a hosted bare metal server in Florida and features 64 cores and 128 GB of RAM. One tester in Europe shared that they were only experiencing \~70ms of latency which is good. If you want to help test Hydra Pool out and give any feedback, you can follow the directions below and join The 256 Foundation public forum on Telegram here. The first step is to configure your miner so that it is pointed to the Hydra Pool server. This can look different depending on your specific miner but generally speaking, from the settings page you can add the following URL:

`stratum+tcp://stratum.hydrapool.org:3333`  On some miners, you don’t need the “stratum+tcp://” part or the port, “:3333”, in the URL dialog box and there may be separate dialog boxes for the port. Use any vanity username you want, no need to add a BTC address. The test iteration of Hydra Pool is configured to payout to the 256 Foundation BTC address. If your miner has a password field, you can just put “x” or “1234”, it doesn’t matter and this field is ignored. Then save your changes and restart your miner. Here are two examples of what this can look like using a Futurebit Apollo and a Bitaxe:

Once you get started, be sure to check [stats.hydrapool.org](https://stats.hydrapool.org/) to monitor the solo pool statistics.

At the last Telehash there were over 350 entities pointing as much as 1.12Eh/s at the fundraiser at the peak. At the time [the block](https://mempool.space/block/0000000000000000000269d52c24ea451225613aab095d90d771d4e29aa96cdd) was found there was closer to 800 Ph/s of hashrate. At this next Telehash, The 256 Foundation is looking to beat the previous records across the board. You can find all the Telehash details on the Meetup page [here](https://www.meetup.com/bitcoin-park-austin/events/305924193/).

### **State of the Network:**

Hashrate on the 14-day MA according to [mempool.space](https://mempool.space/graphs/mining/hashrate-difficulty#1y) increased from \~826 Eh/s to a peak of \~907 Eh/s on April 16 before cooling off and finishing the month at \~841 Eh/s, marking \~1.8% growth for the month.

Difficulty was 113.76T at it’s lowest in April and 123.23T at it’s highest, which is a 8.3% increase for the month. But difficulty dropped with Epoch #444 just after the end of the month on May 3 bringing a -3.3% downward adjustment. All together for 2025 up to Epoch #444, difficulty has gone up \~8.5%.

According to the [Hashrate Index](https://data.hashrateindex.com/asic-index-data/price-index), ASIC prices have flat-lined over the last month. The more efficient miners like the \<19 J/Th models are fetching $17.29 per terahash, models between 19J/Th – 25J/Th are selling for $11.05 per terahash, and models >25J/Th are selling for $3.20 per terahash. You can expect to pay roughly $4,000 for a new-gen miner with 230+ Th/s.

Hashvalue over the month of April dropped from \~56,000 sats/Ph per day to \~52,000 sats/Ph per day, according to the new and improved [Braiins Insights](https://insights.braiins.com/en) dashboard \[IMG-012\]. Hashprice started out at $46.00/Ph per day at the beginning of April and climbed to $49.00/Ph per day by the end of the month.

The next halving will occur at block height 1,050,000 which should be in roughly 1,063 days or in other words \~154,650 blocks from time of publishing this newsletter.

### **Conclusion:**

Thank you for reading the fifth 256 Foundation newsletter. Keep an eye out for more newsletters on a monthly basis in your email inbox by subscribing at [256foundation.org](https://256foundation.org/newsletter.html). Or you can download .pdf versions of the newsletters from there as well. You can also find these newsletters published in article form on Nostr.

If you haven’t done so already, be sure to [RSVP](https://www.meetup.com/bitcoin-park-austin/events/305924136/) for the Texas Energy & Mining Summit (“TEMS”) in Austin, Texas on May 6 & 7 for two days of the highest Bitcoin mining and energy signal in the industry, set in the intimate Bitcoin Commons, so you can meet and mingle with the best and brightest movers and shakers in the space.

While you’re at it, extend your stay and spend Cinco De Mayo with The 256 Foundation at our second fundraiser, Telehash #2. Everything is bigger in Texas, so set your expectations high for this one. All of the lead developers from the grant projects will be present to talk first-hand about how to dismantle the proprietary mining empire.

If you are interested in helping The 256 Foundation test Hydra Pool, then hopefully you found all the information you need to configure your miner in this issue.

If you want to continue seeing developers build free and open solutions be sure to support the Samourai Wallet developers by making a tax-deductible contribution to their legal defense fund [here](https://p2prights.org/donate.html). The first step in ensuring a future of free and open Bitcoin development starts with freeing these developers.

Live Free or Die,

-econoalchemist
