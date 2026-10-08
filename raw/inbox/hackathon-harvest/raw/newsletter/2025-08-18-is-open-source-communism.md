# Is Open Source Communism?

> Source: https://256foundation.substack.com/p/is-open-source-communism
> Collected: 2026-10-07
> Published: 2025-08-18

*A monthly newsletter by 256 Foundation*

August 2025

### **INTRODUCTION:**

Welcome to the eighth newsletter produced by The 256 Foundation and supported by [Proto](https://proto.xyz/)! July was an eventful month for freedom tech; the Samourai Wallet devs took a plea agreement, the Atlanta Bitlabs Hackathon concluded, and there is a new Hydra Pool test server online. Dive into all the interesting things going on in and around the Bitcoin mining industry and catch up on the latest freedom tech news, free & open mining developments, 256 Foundation grant progress updates, Actionable Advice, and the current state of the Bitcoin network. Or are we building the rails needed to abolish private intellectual property? Is open-source in fact communism? Have we got it all wrong? Find out, have fun, and enjoy the read.

### **DEFINITIONS:**

v = version

RSSI = Received Signal Strength Indicator

UI = User Interface

API = Application Programming Interface

JSON = Java Script Object Notation

### **FREEDOM TECH NEWS:**

**July 11**, Skot reignites the [Loriques](https://x.com/skot9000/status/1943859166797606957%0Ahttps://github.com/skot/Loriques) project, a solar powered Meshtastic LoRa gateway. There seems to be renewed interest in mesh networks after Jack Dorsey shared the source files for a Bluetooth mesh chat application he built called [Bitchat](https://x.com/jack/status/1941989435962212728). Mesh communications are a neat concept that can give users a way to send encrypted messages offline. One of the limitations of Bluetooth is the effective range, projects like Lorques are one solution aimed at Long Range (LoRa), low-power communications.

**July 12**, @bc1984adam writes an in-depth [Ashigaru review](https://bc1984.com/ashigaru-terminal-whirlpool-review/) aimed at clearing up criticisms after the developers released their own version of Samourai Wallet’s Whirlpool at the end of June 2025. Some familiar faces in the privacy flame wars came crawling out of the woodwork still clutching to the same FUD they used when Samourai Wallet was active. Unfortunately, it seems as though any developers building on what Samourai Wallet started will need to endure attacks just as vicious as Samourai Wallet did even though they are not associated with Samourai Wallet in any way. The primary criticism raised by [@1440000bytes](https://bitcointalk.org/index.php?topic=5547639.0) was that the Whirlpool coordinator could de-anonymize users and link the inputs and outputs of CoinJoin rounds. The claim assumes that the coordinator is malicious. There is zero evidence that the vulnerability described has ever been executed in the previous Whirlpool coordinator and the Ashigaru devs implemented a fix to the edge-case issue anyways, as described in @bc1984adam’s article. The article goes on to describe the fix may have introduced a separate concern related to a malicious coordinator having the ability to link CoinJoin participants across rounds. Regardless, in my personal opinion, the concerns are blown out of proportion and there is no evidence of compromise. I say, make every spend a CoinJoin and I’m glad there is a Whirlpool coordinator back online.

**July 14**, Roman Storm (Tornado Cash developer) trial starts, marking a new era of significant government overreach where software developers are held liable for the actions of end users. The trial took place in the Southern District of New York (“SDNY”) and prosecutors charged Storm with conspiracy to commit money laundering, conspiracy to violate economic sanctions, and conspiracy to operate an unlicensed money transmitting business. In actuality, Storm did nothing more than build software tools on the Ethereum blockchain that provided basic privacy benefits. In the end, the jury convicted Storm of the conspiracy to operate an unlicensed money transmitting business. The jury was not able to reach a unanimous verdict on the other two charges. There will likely be an appeal following the sentencing hearing. Follow [@theragetech](https://www.therage.co/tornado-cash-trial-intro/) on twitter for detailed coverage of the case.

**July 30**, Samourai Wallet developers reach plea agreement with prosecutors and [plead guilty](https://x.com/zackbshapiro/status/1950573332451016856) to conspiracy to operate an unlicensed money transmitting business. Previously, the developers had plead not guilty to all charges however, the prosecutors presented them with a plea agreement in which if they changed their plea to guilty then the prosecution would drop the conspiracy to commit money laundering charge. The money laundering charge carried a maximum sentence of 20-years and the money transmitting charge carried a maximum sentence of 5-years in prison. The good news in this agreement is that the developers are no longer facing 25-years in prison, hopefully the judge gives them time-served at sentencing for the nearly 500 days they have been under house arrest now. This hardly feels like a win though considering that the developers never once transferred money on behalf of the public, as Samourai Wallet is a non-custodial application, therefore the developers could not have possibly been a money transmitter. The way in which prosecutors twisted the letter of the law to mean that non-custodial wallet developers had to plead guilty to conspiracy to operate a money transmitting business is shocking and should be a wake up call to every one involved in the Bitcoin ecosystem. The language used was so vague that the term “*to facilitate the transfer of funds by any and all means*” could be applied to any non-custodial hardware or software wallet developer, anyone who plugs in a miner, or anyone who operates a node. Basically everyone. As for precedent, none was set in this case because it was resolved in a plea agreement, not that it really matters at the end of the day considering that the charges brought against Samourai Wallet and the ensuing actions against them were completely unprecedented. Demonstrating once again that you can be as nice as you want to the government but they will still lock you in a cage for any reason they want. This marks the end of a courageous fight the developers were embroiled in for 462 days. Currently, sentencing hearings are scheduled for November 6 & 7, 2025 and the developers need to pay a $6m fine by then. In hind-sight of the Roman Storm case, the Samourai Wallet developers made the right decision taking the plea agreement. They would have only incurred more expense taking it to trial, they would have been facing 20 additional years, the fines would have been bigger, the judge would have been harsher in her sentencing, and the jury would have at the very least convicted them on the conspiracy to operate an unlicensed money transmitting business charge anyways if the Roman Storm case is any indicator. There is no reason for the developers to martyr themselves.

### **FREE & OPEN MINING DEVELOPMENTS:**

**July 1**, the latest release of Bitaxe firmware, AxeOS v2.9.0 was released. A few of the many new features include: the addition of a “clear” button and filter for real-time logs so the user can quickly narrow down their search to relevant log entries or clear the entire log to get a clean start; the addition of Stratum response time so the user can see how long it takes the Stratum server to respond to the clients share submission; and the addition of the hostname and WiFi RSSI in the header of the UI so the user can quickly see what their device is named and which WiFi network it is on. There were API improvements as well, like returning a JSON object for unhandled API requests instead of redirecting to the main page. There are several more updates from Stratum improvements to display enhancements to bug fixes. You can read all about them on the [GitHub releases page](https://github.com/bitaxeorg/ESP-Miner/releases). You can also watch a video about the new release [here](https://www.youtube.com/watch?v=oMxUgP9KI08) from [@wantclue](https://x.com/wantclue).

**July 3**, Stratum v2 **[website](https://stratumprotocol.org/pools)** updated to include helpful explanations, differences between v1 & v2, and how you can get started running Stratum v2 in your mining pool.

**July 3**, Solo miner finds block with [Solo CK Pool](https://x.com/ckpooldev/status/1940912861552996502) with 2.3Ph/s. This marks the 301<sup>st</sup> block found by Solo CK Pool and came from the EU server. A miner of this size had roughly a 1 in 2,800 change of solving a block every day on average.

**July 5**, [Tyler Stevens](https://x.com/gladstein/status/1941568193577021743) gives a talk in Alaska about Bitcoin mining heat re-use and the potential it has to triple current network hashrate by capturing only 1% of world-wide comfort heat. The 256 Foundation believes that closed and proprietary mining hardware will not be suitable to realize this type of potential. Open-source hardware and firmware however, will usher in heat re-use developments like a wild fire (pun intended).

**July 8**, the Atlanta Bitlab Mining Hackathon concludes and winners were announced online via a live video feed. There were three categories: software, hardware, and energy. A project called Minor League Miners took the software prize for their cool dashboard that gamifies micro-scale bitcoin mining by putting a competitive twist on variables like best difficulty \[IMG-003\]. For the hardware prize, PC-AXE was the winner with the idea being that PCIe cards equipped with ASICs could produce \~1.2Th/s each \[IMG-004\]. For the energy prize, Rev.Hodl took the prize by using a special type of clay to actually cool down air with a Bitcoin miner \[IMG-005\].

**July 11**, [@Boerst](https://x.com/boerst) has been hard at it refining [stratum.work](https://stratum.work/). This update incorporates a Sankey diagram, which traces how mining pools assemble block templates. Sankey diagrams are a type of data visualization tool that emphasizes flows or change from one state to another. In this case, the mining pools are the flows and the template Merkle branches are the nodes.

**July 12**, [@tendkraft](https://x.com/trendkraft/status/1944076579891470407) recommends updating NerdQaxe firmware to v1.0.31-RC due to an issue that was causing a fuse and several diodes to blow!

**July 22,** [Covert solar-powered Bitaxe](https://x.com/depinnomad/status/1947714601438826725). In the posted video, it appears that @depinnomad has installed a solar panel and weather-proof electrical enclosure on a utility pole. Among the battery and other components in the box, there is a Bitaxe hashing away. This seems to be a Decentralized Physical Infrastructure Network or “DePIN”, which is a new term for me and apparently kind of a rabbit hole. You can learn more about DePINs [here](https://cointelegraph.com/explained/decentralized-physical-infrastructure-network-depin-explained).

**July 26**, a miner with only 49Th/s solves the 303<sup>rd</sup> block for [Solo CK Pool](https://x.com/ckpooldev/status/1949228381054337413), this one again on the EU server!

### **GRANT PROJECT UPDATES:**

The 256 Foundation team has been crushing each project, getting closer to completing the first open-source complete mining stack. The first batch of Ember Ones is taking a little longer than we thought last month but they are well on their way. By the end of October, the first official release of the Libre Board should be out along with the first official release of Hydra Pool. Around this time, there may also be a beta version of Mujina firmware released for the developers and testers working with the newly manufactured Ember One hashboards; the first official release of Mujina firmware is not due until the end of December, maybe January 2026. By all accounts, we are making great progress and we are excited to share the updates with you.

**Ember One**In July, Skot has continued refining the Ember One with upgrades like a reverse polarity protection circuit (contributed by

[@zbomstaz](https://x.com/zbomstaz)) and adding Transient Voltage Suppression diodes to protect connected USB devices. Then he

[hand assembled](https://x.com/skot9000/status/1941233839638184062)some prototypes of the resulting v4 board and began the validation process. Once validated, there will be a small production run of roughly 100 units for testers and developers. Ember One is the hashboard only and does not include the required control board (see Libre Board), cooling fan (a reference fan will be documented), or the heat-sink (there is work being done on designing and producing one which should be available soon).

After battling getting the components hand assembled, Skot was finally able to get the [first signs of life](https://x.com/skot9000/status/1950282184352289068) out of all 12 ASIC chips. The validation process is close to being done and then there will be some units produced. You can learn more at [emberone.org](https://emberone.org/).

**Libre Board**There is not much to report on Libre Board this month, we are currently checking all the traces to ensure the PCB layers are correct before the initial test batch is manufactured, a tedious process. Users will be able to connect up to four Ember One hashboards to each Libre Board controller. Additionally, the NVME port allows users to install an SSD card if they want to run a fully validating Bitcoin node on their Libre Board. The standardized two 100-pin connectors for the compute module gives users the flexibility to choose any Raspberry Pi or other x86 or even RISC-V compute module with various CPU and RAM specifications. There are a number of other features and the form factor of the Libre Board has been designed to match the standardized Ember One form factor so that the control board and hashboards can all fit inside the same enclosure. You can learn more at

[libreboard.org](https://libreboard.org/).

**Mujina Firmware**There also is not much news to report for Mujina this month either, lots of incremental steps. Mujina firmware has the ability to handle hot-swappable hashboard replacement without a system reboot, or any system interruption at all. As the hashboards communicate via USB-C, they are discoverable like any other USB device and can be detected instantly upon connection. The Ember One road map includes future versions with a range of ASIC chips and Mujina handles this with the ability to easily port in drivers for the various types of hashboards. For example, a user will be able to unplug and swap out a hashboard while the system is running and Mujina will detect the new hashboard, determine the necessary driver for it based on the ASICs it is fashioned with, and start communicating with the new hashboard immediately without interruption to the other hashboards. We believe that over time this capability will be a significant mitigating factor against maintenance and repair down time. Other features include the development of a terminal interface in addition to the web UI, for an example of what is possible in the terminal interface check out some of the themes

[here](https://ratatui.rs/showcase/apps/). Currently, the firmware is handling communications to and from the ASIC chip as well as peripheral board components. In the weeks ahead, testing and development will graduate from the Bitaxe Raw interface to running Mujina on one of the Ember One 00 v4 prototypes. You can learn more at

[mujina.org](https://mujina.org/).

**Hydra Pool**In July,

[@jungly](https://x.com/jungly)was able to get the new and improved test server configured on Signet and testing has commenced. See the Actionable Advice column for instructions and join the

[256 Foundation Telegram](https://t.me/the256foundation)channel for community support. Hydra Pool is a one-click deployable pool made to work on Mujina which eventually will become its own Linux distribution. There will be two payout methods available in the first release of Hydra Pool, selectable by the user, solo mining mode and Pay Per Last N Shares (“PPLNS”) mode. With the ability to run a Bitcoin node on the Libre Board, the complete Ember One mining system will be a versatile open-source solution that gives the user the full mining stack in a fully customization package. You can learn more about Hydra Pool

[here](https://hydrapool.org/).

### **ACTIONABLE ADVICE:**

This month we are covering how to help test the latest Hydra Pool software. Our goal is to validate the Hydra Pool Stratum server is working well with various types of Bitcoin mining hardware and firmware. Unfortunately, there is no Stratum v1 standard so it is difficult to know how Stratum v1 clients will communicate with the server. This testing helps us find issues that we can resolve before the first release. Don’t be discouraged if your miner shows up as “Pending” or “Fail” in the dashboard, that is actually helpful for us because it means there is an issue we need to resolve! The logs from the brief connection are saved so that we can study them and find the issues, make corrections where needed, and push the changes into GitHub. The current test server is configured to run on Signet so there is no mining rewards to be had. We will switch it over to Bitcoin Mainnet once we have enough testing done to be assured it could actually submit a valid block in the event one of the testers gets so lucky.

1\) Open your miner’s configuration page and point the device to:

`stratum+tcp://test.hydrapool.org:3333`
For the username, feel free to enter any vanity name you want.

2\) Restart your miner for the changes to take effect.

3\) Navigate to [test.hydrapool.org](https://test.hydrapool.org/) to check the dashboard. After 5-minutes there should be enough information in the logs for the test to be done. You can reset your miner’s configuration at that point. Short & sweet, thanks!

### **STATE OF THE NETWORK:**

Hashrate on the 14-day MA according to [mempool.space](https://mempool.space/graphs/mining/hashrate-difficulty#1y) increased from \~832 Eh/s on the first day of July to 906 Eh/s by the end of the month, marking roughly +8.8% increase for the month and bringing the difficulty right back to where it was before that massive decrease. The year to date hashrate difference is +15.2%.

Difficulty was 127.62T at it’s highest in July and 116.96T at it’s lowest, which marks a \~8.4% increase for the month. All together for 2025 up to Epoch #450, difficulty has gone up \~16.2%.

According to the [Hashrate Index](https://data.hashrateindex.com/asic-index-data/price-index), ASIC prices have increased ever so slightly over the last month. The more efficient miners like the \<19 J/Th models are now fetching $17.94 per terahash, models between 19J/Th – 25J/Th are selling for less than last month, down from $7.52/Th to $6.52/Th, and models >25J/Th are surprisingly higher in price this month over last, fetching $3.04/Th now compared to $2.82/Th last month.

Hashvalue over the month of July plummeted from roughly 54k sats/Ph/day to finish the month out at 49k sats/Ph/day, according to the [Braiins Insights](https://insights.braiins.com/en) dashboard.

### CONCLUSION:

With all that is going on with freedom tech, free and open Bitcoin mining development, and the awesome projects being built at the 256 Foundation and elsewhere, let’s circle back to the opening image, the "Open source is communism for intellectual property" meme. I think the underlying question this poses is: are open-source and private property mutually exclusive? Personally, I’m quite passionate about both, surely I’m not a walking contradiction. I couldn’t help but think about this for a long time, I’ll admit it, the meme had it’s intended affect on me. But I think that for as much as there is to unpack here, it can be organized and broken down plainly.

The assertion that open-source equates to communism for intellectual property and inherently undermines private property rights rests on a misunderstanding of both concepts. This can be broken down into five areas and there is a logical way that open-source and private property can coexist harmoniously.

**1) Open-Source as a Voluntary Choice, Not a State Imposition:**Communism, as historically practiced, involves centralized state control and the abolition of private property through coercion. Open-source, by contrast, is a voluntary model where individuals or entities choose to share their intellectual creations under specific licenses (e.g.,

[MIT](https://opensource.org/license/mit)or

[GPL](http://GPL)). This act of sharing doesn’t negate private property; it’s an exercise of it. Creators retain ownership of their code and grant permissions for others to use, modify, or distribute it; rights explicitly defined by licenses. For example, when a developer releases code under the MIT License, they’re not surrendering ownership but licensing it, much like a landlord rents a property while retaining title. This aligns with libertarian principles of voluntary exchange, not communist expropriation.

**2) Intellectual Property as a Managed Resource, Not Abolished:**The meme implies open-source eliminates intellectual property similar to how communism abolishes private property, but open-source doesn’t eliminate intellectual property in actuality. Open-source operates within the framework of intellectual property law. Licenses like GPL ensure that derivative works remain open, but they still recognize the original creator’s copyright. This is evident in GitHub’s default license options, where projects are explicitly tagged with legal terms (see

[gnu.org](https://www.gnu.org/philosophy/free-sw.html)and

[opensource.org](http://opensource.org)). Far from being "communism," this is a market-driven innovation: companies like Red Hat and Canonical thrive by offering support and services for open-source software, proving that private property in the form of expertise and infrastructure can coexist with shared code. This concept of discovering viable business opportunities built on a foundation of open-source is central to the 256 Foundation’s vision.

**3) Economic Benefits Support Coexistence:**Recent data from the Linux Foundation’s 2025

[report](https://www.linuxfoundation.org/research/measuring-economic-value-of-os)on "Measuring the Economic Value of Open Source" highlights cost savings, faster development, and interoperability as key benefits. These outcomes don’t dismantle private property but enhance it by creating new markets. Take Twitter for example, OpenAI released GPT and its been adopted by Twitter and implemented in their AI servers; this demonstrates how open-source can drive private enterprise. Developers and firms invest in infrastructure and talent (private assets) to leverage open code, turning a shared resource into proprietary value-added services. Think about how MicroSoft supports the Linux Foundation, they know the open-source community is producing the feed stock for their business.

**4) Philosophical Alignment with Property Rights:**Libertarian thinkers like

[Stephan Kinsella](https://en.wikipedia.org/wiki/Stephan_Kinsella), often cited in intellectual property debates, argue against patents and copyrights likening them to state-granted monopolies that distort free markets. Open-source aligns with this critique by rejecting artificial scarcity in ideas, which are “non-rivalrous goods” (in other words, one person's consumption of the good does not diminish its availability for others). Yet, open-source doesn’t abolish property rights; it redefines them. Creators retain moral and legal claims to their work, and the community’s contributions build on that foundation.

**5) Countering the Meme’s Provocation:**The "Change My Mind" format invites challenge, so let’s flip it: Open-source isn’t communism; it’s capitalism’s evolution. It leverages private property to foster competition and innovation, as seen in the rapid adoption of AI, Apache web servers, and even Bitcoin itself. If anything, proprietary software, locked behind paywalls and legal threats, more closely resembles a state-enforced monopoly, the true antithesis of free markets.

Open-source and private property aren’t mutually exclusive; they’re complementary when viewed through a voluntary, market-based lens. The meme’s hyperbolic comparison to communism overlooks the agency of creators, the legal structure of licenses, and the economic reality of thriving private enterprises in the open-source ecosystem. The tech landscape shows this model strengthening, not weakening, property rights. Open-source ensures the users have the freedom to run, copy, distribute, study, change and improve the software. That doesn't sound like socialism or communism to me.

Thank you for reading the eighth 256 Foundation newsletter. Keep an eye out for more newsletters on a monthly basis in your email inbox by subscribing at [256foundation.org](https://256foundation.org/newsletter.html). Or you can download .pdf versions of the newsletters from there as well. You can also find these newsletters published in article form on Nostr.

Live Free or Die,

-econoalchemist
