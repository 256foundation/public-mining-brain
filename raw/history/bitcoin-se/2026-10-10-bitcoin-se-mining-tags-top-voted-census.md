# Bitcoin Stack Exchange — mining tags, top-voted questions census

> Registry ID: bitcoin-se
> Source: https://api.stackexchange.com/2.3/search/advanced?order=desc&sort=votes&tagged=<TAG>&site=bitcoin&pagesize=50
> Collected: 2026-10-10
> Published: n/d (site content; the 50 census questions were asked 2011–2017)
> Posture: extract
> As-Of: 2026-10-10

CENSUS/extract capture of the top-voted mining questions on bitcoin.stackexchange.com. Method notes (honest park list):

- The HTML tag page (https://bitcoin.stackexchange.com/questions/tagged/mining?tab=Votes&pagesize=50) is Cloudflare-gated for non-browser agents ("Just a moment..." challenge page), so the official Stack Exchange API 2.3 (anonymous, no key) was used instead.
- There is NO plain `mining` tag on bitcoin.stackexchange.com; mining questions carry a mining-* tag family. Swept 15 tags: mining-theory (831 q), mining-pools (827), mining-profitability (453), mining-reward (437), mining-hardware (436), mining-software (141), gpu-mining (134), solo-mining (122), cpu-mining (103), mining-technical-details (95), mining-setup (91), mining-pool-shares (79), merged-mining (44), selfish-mining (35), cloud-mining (34). The first 12 returned 50 items each with has_more=true; merged-mining / selfish-mining / cloud-mining returned 44 / 35 / 34 items (tag exhausted).
- Merge of all tag sweeps: 598 unique questions; this census = top 50 by net vote score. Scores/answers/views are site-wide counts at capture time, not per-tag.
- For the top 10 questions, the top-voted answer was captured as a short verbatim snippet (first ~400 chars, HTML stripped). Snippets truncate mid-thought by design; answers are community content under CC BY-SA 4.0 (per API metadata).

## Top 50 mining-tagged questions by vote score

| # | Score | Answers | Accepted | Views | Asked | Tags | Title |
|---|-------|---------|----------|-------|-------|------|-------|
| 1 | 208 | 9 | yes | 118,377 | 2011-08-30 | mining-reward proof-of-work mining-theory | [What exactly is Mining?](https://bitcoin.stackexchange.com/questions/148) |
| 2 | 163 | 6 | yes | 297,722 | 2013-02-28 | mining-theory hash mining-reward proof-of-work | [What are bitcoin miners really solving?](https://bitcoin.stackexchange.com/questions/8031) |
| 3 | 132 | 9 | yes | 48,496 | 2011-09-11 | transaction-fees mining-reward mining-theory | [How much will transaction fees eventually be?](https://bitcoin.stackexchange.com/questions/876) |
| 4 | 131 | 7 | yes | 55,570 | 2011-08-30 | mining-reward trading buy-bitcoins canonical-question | [How do you obtain bitcoins?](https://bitcoin.stackexchange.com/questions/91) |
| 5 | 124 | 5 | yes | 24,037 | 2011-09-20 | security confirmations mining-theory | [Why is 6 the number of confirms that is considered secure?](https://bitcoin.stackexchange.com/questions/1170) |
| 6 | 116 | 9 | yes | 336,978 | 2011-08-30 | mining-profitability mining-hardware | [How much Bitcoin will I mine right now with hardware X?](https://bitcoin.stackexchange.com/questions/118) |
| 7 | 112 | 4 | yes | 83,713 | 2011-08-31 | hashpower merged-mining | [How does merged mining work?](https://bitcoin.stackexchange.com/questions/273) |
| 8 | 70 | 11 | yes | 11,987 | 2012-03-08 | economic-theory mining-reward reward-schedule future-proof | [Will Bitcoin suffer from a mining Tragedy of the Commons when mining fees drop to zero?](https://bitcoin.stackexchange.com/questions/3111) |
| 9 | 67 | 9 | yes | 94,104 | 2011-08-31 | mining-theory mining-reward economic-theory value key-selling-points | [Where do bitcoins come from and what gives them their value?](https://bitcoin.stackexchange.com/questions/182) |
| 10 | 67 | 3 | yes | 74,476 | 2015-11-07 | mining-profitability asic gpu-mining cpu-mining canonical-question | [In the ASIC-age, is it worth starting mining Bitcoin at home?](https://bitcoin.stackexchange.com/questions/41276) |
| 11 | 62 | 4 | yes | 33,762 | 2011-09-10 | security economic-theory difficulty block-interval mining-theory | [What keeps the average block time at 10 minutes?](https://bitcoin.stackexchange.com/questions/855) |
| 12 | 55 | 5 | yes | 37,711 | 2011-11-03 | security mining-theory block-interval | [Why was the target block time chosen to be 10 minutes?](https://bitcoin.stackexchange.com/questions/1863) |
| 13 | 50 | 2 | yes | 25,539 | 2013-03-06 | mining-theory blockchain-fork consensus best-chain stale-block | [What happens if two miners mine the next block at the same time?](https://bitcoin.stackexchange.com/questions/8172) |
| 14 | 48 | 2 | yes | 14,762 | 2013-05-08 | mining-pools | [What prevents a pool miner from stealing an entire block?](https://bitcoin.stackexchange.com/questions/10687) |
| 15 | 45 | 4 | yes | 8,109 | 2011-10-03 | mining-pools weaknesses block-withholding | [How is block-solution-withholding a threat to mining pools?](https://bitcoin.stackexchange.com/questions/1338) |
| 16 | 43 | 6 | yes | 241,006 | 2011-10-07 | mining-pools mining-pool-shares mining-setup | [What are stale shares and what can I do to avoid them?](https://bitcoin.stackexchange.com/questions/1416) |
| 17 | 43 | 2 | yes | 84,266 | 2011-10-13 | mining-pools solo-mining terminology mining-pool-shares | [What is a share? Can I find it while mining solo, or only when pool mining?](https://bitcoin.stackexchange.com/questions/1505) |
| 18 | 43 | 8 | yes | 38,301 | 2011-08-30 | linux mining-profitability cpu-mining | [Is CPU mining even worth it?](https://bitcoin.stackexchange.com/questions/59) |
| 19 | 42 | 8 | yes | 21,478 | 2017-12-25 | mining-theory difficulty confirmations | [Can bitcoin exist without miners?](https://bitcoin.stackexchange.com/questions/66516) |
| 20 | 41 | 3 | yes | 50,936 | 2013-04-17 | transactions wallet transaction-fees mining-reward | [Who gets Bitcoin transaction fees?](https://bitcoin.stackexchange.com/questions/9895) |
| 21 | 41 | 5 | yes | 27,764 | 2012-11-06 | mining-reward bitcoin-economy reward-schedule | [What will happen to mining after the 20 999 999th Bitcoin?](https://bitcoin.stackexchange.com/questions/5275) |
| 22 | 38 | 2 | yes | 14,262 | 2012-08-27 | protocol mining-reward coinbase-transaction | [What is the coinbase?](https://bitcoin.stackexchange.com/questions/4571) |
| 23 | 37 | 2 | yes | 74,934 | 2015-08-18 | ethereum mining-theory | [What is Gas Limit in Ethereum?](https://bitcoin.stackexchange.com/questions/39132) |
| 24 | 37 | 3 | yes | 54,824 | 2011-10-08 | linux cpu-mining gpu-mining miner-configuration | [How can I start mining Bitcoin?](https://bitcoin.stackexchange.com/questions/1433) |
| 25 | 37 | 4 | yes | 18,876 | 2011-10-01 | mining-profitability | [Is there any point to casual mining?](https://bitcoin.stackexchange.com/questions/1319) |
| 26 | 36 | 1 | yes | 39,183 | 2011-09-01 | mining-pools solo-mining bandwidth | [What are the bandwidth requirements of a mining rig?](https://bitcoin.stackexchange.com/questions/360) |
| 27 | 35 | 5 | yes | 12,530 | 2013-01-23 | asic cryptography mining-hardware | [Bitcoin Mining ASICs used for cryptographic application? Rainbow tables?](https://bitcoin.stackexchange.com/questions/7236) |
| 28 | 34 | 2 | yes | 3,045 | 2011-08-31 | mining-pools security decentralization | [Do mining pools centralize the Bitcoin network and make it less secure?](https://bitcoin.stackexchange.com/questions/312) |
| 29 | 31 | 6 | yes | 123,873 | 2013-04-04 | mining-profitability mining-hardware difficulty asic | [Do these new ASIC miners really pay for themselves in 5 days?](https://bitcoin.stackexchange.com/questions/9148) |
| 30 | 31 | 3 | yes | 45,489 | 2014-01-07 | mining-theory proof-of-work proof-of-stake peercoin | [How does proof-of-stake &quot;mining&quot; work?](https://bitcoin.stackexchange.com/questions/20007) |
| 31 | 30 | 6 | yes | 147,343 | 2013-11-14 | solo-mining mining-profitability hashpower | [Solo mining just for luck, realistic?](https://bitcoin.stackexchange.com/questions/16687) |
| 32 | 30 | 3 | yes | 3,228 | 2011-09-13 | mining-theory asic-resistance | [Are there algorithms that could have been chosen for mining that balance CPU/GPU?](https://bitcoin.stackexchange.com/questions/931) |
| 33 | 29 | 8 | yes | 179,006 | 2012-03-15 | mining-hardware raspberry-pi | [What hash rate can a Raspberry Pi achieve? Can the GPU be used?](https://bitcoin.stackexchange.com/questions/3165) |
| 34 | 29 | 10 | yes | 40,945 | 2011-08-30 | mining-setup miner-configuration mining-software | [What open source miner applications are there?](https://bitcoin.stackexchange.com/questions/1) |
| 35 | 29 | 3 | yes | 9,791 | 2011-12-19 | mining-setup mining-hardware | [Can I use Bitcoin mining as a data furnace to heat my home?](https://bitcoin.stackexchange.com/questions/2283) |
| 36 | 28 | 3 | yes | 48,713 | 2013-04-27 | cpu-mining javascript gpu-mining | [How useful is a JavaScript miner?](https://bitcoin.stackexchange.com/questions/10320) |
| 37 | 28 | 4 | yes | 29,475 | 2012-10-16 | mining-pools mining-profitability pool-payout-methods pool-hopping | [What is pool hopping?](https://bitcoin.stackexchange.com/questions/5072) |
| 38 | 28 | 2 | yes | 18,712 | 2012-11-29 | blockchain mining-theory consensus terminology best-chain | [What does the term &quot;Longest chain&quot; mean?](https://bitcoin.stackexchange.com/questions/5540) |
| 39 | 27 | 5 | yes | 30,888 | 2012-06-24 | asic mining-hardware fpga butterfly-labs | [Is Butterfly Labs reputable / Should I preorder the SC Jalepeno?](https://bitcoin.stackexchange.com/questions/4052) |
| 40 | 27 | 7 | yes | 13,129 | 2017-11-09 | mining-theory decentralization asic-resistance | [Why did Satoshi design Bitcoin to be mineable only on specialized hardware, if the goal was decentralization?](https://bitcoin.stackexchange.com/questions/62336) |
| 41 | 26 | 3 | yes | 83,309 | 2013-08-11 | block proof-of-work algorithms mining-theory block-header | [The bitcoin mining algorithm from a programmer&#39;s viewpoint](https://bitcoin.stackexchange.com/questions/12603) |
| 42 | 26 | 6 | yes | 37,563 | 2013-03-26 | mining-theory network reward-schedule weaknesses | [What happens to the bitcoin network when the miners all stop in the future?](https://bitcoin.stackexchange.com/questions/8743) |
| 43 | 26 | 2 | yes | 8,336 | 2016-04-02 | asic mining-technical-details asicboost | [How does AsicBoost work?](https://bitcoin.stackexchange.com/questions/43579) |
| 44 | 25 | 1 | yes | 30,062 | 2011-09-02 | mining-pools | [How can I start my own mining pool?](https://bitcoin.stackexchange.com/questions/446) |
| 45 | 25 | 1 | yes | 16,535 | 2011-09-28 | block verification nonce mining-theory | [When a block is &quot;discovered&quot; how is the nonce determined?](https://bitcoin.stackexchange.com/questions/1290) |
| 46 | 25 | 3 | yes | 5,970 | 2011-11-19 | mining-reward mining-theory empty-blocks | [What happens if there are no transactions in a block?](https://bitcoin.stackexchange.com/questions/2021) |
| 47 | 24 | 1 | yes | 31,879 | 2011-08-30 | ubuntu mining-setup | [How to mine in Ubuntu?](https://bitcoin.stackexchange.com/questions/123) |
| 48 | 24 | 1 | yes | 5,940 | 2011-09-03 | mining-profitability | [How can I compute mining profitability?](https://bitcoin.stackexchange.com/questions/485) |
| 49 | 23 | 2 | yes | 30,226 | 2014-08-10 | mining-theory altcoin mining-hardware asic asic-resistance | [What does it mean for a cryptocurrency to be ASIC-resistant?](https://bitcoin.stackexchange.com/questions/29975) |
| 50 | 23 | 2 | yes | 29,283 | 2012-10-13 | getwork nonce mining-technical-details | [What is the extraNonce?](https://bitcoin.stackexchange.com/questions/5048) |

## Top-voted answer snippet for the top 10 questions

### Q148 — What exactly is Mining? (question score 208)

[760](https://bitcoin.stackexchange.com/a/760) — score 238, ACCEPTED answer:

> David Schwartz's answer is entirely accurate, but all that "bitspeak" might be a little intimidating to the average user. Let me try and put it into more plain language: The way Bitcoin works is that instead of having one central authority who secures and controls the money supply (like most governments do for their national currencies), this work is spread out all across the network. Most of the…

### Q8031 — What are bitcoin miners really solving? (question score 163)

[8033](https://bitcoin.stackexchange.com/a/8033) — score 162, top-voted answer, not the accepted one:

> Here is an extremely simplified sketch of the problem, but it should give a pretty good idea of what the problem is. The data: This is the hash of the lastest block (shortened to 30 characters): 00000000000001adf44c7d69767585 These are the hashes of a few valid transactions waiting for inclusion (shortened). 5572eca4dd4 db7d0c0b845 And this the hash of one special transaction that you just…

### Q876 — How much will transaction fees eventually be? (question score 132)

[895](https://bitcoin.stackexchange.com/a/895) — score 75, ACCEPTED answer:

> I read that the market will find the equilibrium how much these transaction fees will be. It will not. This is perhaps the biggest flaw in Bitcoin at the moment: once mining rewards end there is no direct linkage between the amount of hashpower needed to secure the network and the incentive to mine. True, there is a limit on the blocksize, so if the transaction volume in a block window…

### Q91 — How do you obtain bitcoins? (question score 131)

[100](https://bitcoin.stackexchange.com/a/100) — score 71, ACCEPTED answer:

> Exchanges These are platforms that match buyers with sellers. They allow you to deposit fiat currency (like USD, EUR, etc.) and use it to buy Bitcoin. There are both centralized platforms and decentralized exchanges (often referred to as DEXs). Brokerage Services Unlike exchanges, where you're trading with other users, brokerage services sell you Bitcoin directly. This method might be more…

### Q1170 — Why is 6 the number of confirms that is considered secure? (question score 124)

[1174](https://bitcoin.stackexchange.com/a/1174) — score 73, top-voted answer, not the accepted one:

> I believe this is addressed in page 8 of Satoshi's Bitcoin paper when showing the probability of an attacker catching up. The wiki states: "Only 6 blocks or 1 hour is enough to make reversal computationally impractical." The key word is "impractical". The important sentence in Satoshi's paper is: "Assuming the honest blocks took the average expected time per block, the attacker's potential…

### Q118 — How much Bitcoin will I mine right now with hardware X? (question score 116)

[2999](https://bitcoin.stackexchange.com/a/2999) — score 60, ACCEPTED answer:

> Go to http://bitminter.com/test and click the "test start" button. If you have Java installed the miner should launch. Click "engine start" on your GPU(s) to start mining and the GUI will show how many bitcoins per day you will make (on average). Note that you are actively mining in a pool without getting paid. This test page launches a version of the miner which is only meant to be used for a…

### Q273 — How does merged mining work? (question score 112)

[275](https://bitcoin.stackexchange.com/a/275) — score 101, ACCEPTED answer:

> Merged mining allows a miner to mine for more than one block chain at the same time. The benefit is that every hash the miner does contributes to the total hash rate of both (all) currencies, and as a result they are all more secure. Starting with a high-level explanation: The miner (or mining controller in the case of pooled mining) actually builds a block for both hash chains in such a way that…

### Q3111 — Will Bitcoin suffer from a mining Tragedy of the Commons when mining fees drop to zero? (question score 70)

[3123](https://bitcoin.stackexchange.com/a/3123) — score 23, top-voted answer, not the accepted one:

> There will definitely be a tragedy of the commons problem if things stand as they are now. This was discussed at some length here and elsewhere. There are some proposed ways to address this and make transaction fees nonzero (block size limit, hardcoded fees, insurance entities, mining cartel, gentleman's agreements which are maintained for fear defection would beget more defection, etc.), but I…

### Q182 — Where do bitcoins come from and what gives them their value? (question score 67)

[185](https://bitcoin.stackexchange.com/a/185) — score 42, ACCEPTED answer:

> Although individual bitcoins enter the Bitcoin economy as miners are rewarded for processing transactions, it's much more helpful to think of all 21 million bitcoins as having been created when Satoshi Nakamoto defined the Bitcoin protocol and launched the Bitcoin network in 2009. The reason for this is that the Bitcoin protocol specifically defines and controls when and how a limited total…

### Q41276 — In the ASIC-age, is it worth starting mining Bitcoin at home? (question score 67)

[41277](https://bitcoin.stackexchange.com/a/41277) — score 63, ACCEPTED answer:

> Generally, it's not worth your time and effort to mine at home! (Some exceptions may apply.) Age of ASIC mining CPU mining has been unprofitable since 2011 , GPU mining just slightly later . Today, ASICs rule mining. The Bitcoin network has more than 1.7 Ehash/s (Oct 2016) now which is 1,700,000,000,000 Mhash/s. Your graphics card will be running full blast to churn out a few hundred Mhash/s,…


---

*Captured via Stack Exchange API 2.3 (anonymous), 2026-10-10. Content license CC BY-SA 4.0. Cloudflare challenge blocks curl on the site's HTML pages; API route used instead.*
