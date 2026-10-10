# X archive: notable open-source Bitcoin mining posts (adjacent to 256 / OSMU / Heatpunks)

> Source: X keyword and thread fetch, 2026-10-07. Accounts: @Schnitzel, @skot9000, @Public_Pool_BTC, @tylerkstevens, @wantclue.
> Collected: 2026-10-07
> Published: 2025-06-05 to 2026-10-06

Method: X keyword search (`from:notable` plus date windows and `max_id` paging). This is not an official X archive export. Coverage is incomplete; gaps are listed at the bottom. Original post text is preserved. Engagement counts are as of collection.

Account: Mixed. Selected for reach or load-bearing claims about open-source mining, Bitaxe, Public Pool, Mujina, Hydrapool, Red Team. Japanese 'Mujina' VTuber hits were discarded.
Posts in this file: 24

## 2026-10-03  skot (@skot9000)

- URL: https://x.com/skot9000/status/2106403102631084271
- ID: 2106403102631084271
- Engagement: likes=5 reposts=0 replies=0 quotes=0 bookmarks=0 views=296
- Media: https://pbs.twimg.com/media/HTtyTHJWQAAq7V9.png

When open source hardware work pays well I won't tell, but there will be signs

---

## 2026-09-24  skot (@skot9000)

- URL: https://x.com/skot9000/status/2103256115253563510
- ID: 2103256115253563510
- Engagement: likes=28 reposts=4 replies=3 quotes=0 bookmarks=1 views=2596

Check out these awesome bitaxe enclosure ideas and vote for your favorite!

---

## 2026-09-23  skot (@skot9000)

- URL: https://x.com/skot9000/status/2102782722087498106
- ID: 2102782722087498106
- Engagement: likes=2 reposts=0 replies=0 quotes=0 bookmarks=0 views=83

Hydrapool is open source mining pool software from @jungly and  @256FOUNDATION it provides the basics of a mining pool and is designed for people to develop and add in their own share accounting and payout mechanism… essentially its a platform for exactly what you suggested.

---

## 2026-09-22  skot (@skot9000)

- URL: https://x.com/skot9000/status/2102535857022333149
- ID: 2102535857022333149
- Engagement: likes=13 reposts=0 replies=3 quotes=0 bookmarks=0 views=1651

Excellent to see Chinese hardware manufacturers deploying and supporting open source to make their products better. (👋 @BITMAINtech )

---

## 2026-09-20  skot (@skot9000)

- URL: https://x.com/skot9000/status/2101506775434285532
- ID: 2101506775434285532
- Engagement: likes=0 reposts=0 replies=1 quotes=0 bookmarks=0 views=67

Open source Bitcoin miners aren’t the business of extracting cash from unsuspecting plebs. That’s shitcoinery.

---

## 2026-08-17  Michael Schmid (@Schnitzel)

- URL: https://x.com/Schnitzel/status/2089377710241927389
- ID: 2089377710241927389
- Engagement: likes=104 reposts=12 replies=8 quotes=2 bookmarks=6 views=5735
- Media: https://pbs.twimg.com/media/HP71c2WWwAEoOnm.jpg

A lot of you asked how the @256FOUNDATION Red Team actually tests closed-source mining firmware. The answer is real hardware. You can't audit what you can't run — so we run it. This is our control-board cage: miner brains on the bench, wired into an isolated lab network.

---

## 2026-08-13  Michael Schmid (@Schnitzel)

- URL: https://x.com/Schnitzel/status/2087733119453376754
- ID: 2087733119453376754
- Engagement: likes=1 reposts=0 replies=1 quotes=0 bookmarks=0 views=24

We didn't find any major flaws in Mujina, just a couple of small improvements. However there are no flashable OS Images for Mujina on S19 yet, we're working on this. Give us a couple of weeks.

---

## 2026-08-12  Michael Schmid (@Schnitzel)

- URL: https://x.com/Schnitzel/status/2087619577484046470
- ID: 2087619577484046470
- Engagement: likes=314 reposts=77 replies=19 quotes=16 bookmarks=44 views=64950
- Media: https://pbs.twimg.com/media/HPiz8sfWAAA3GXZ.png

~90% of ASICs run one vendor's closed-source firmware. Almost nobody has audited it.

We at @256FOUNDATION do.

Introducing the 256 Red Team 🧵 — the 256 Foundation's firmware security program. On hardware we own, in an isolated lab, under coordinated disclosure.

---

## 2026-08-12  Michael Schmid (@Schnitzel)

- URL: https://x.com/Schnitzel/status/2087619580785021380
- ID: 2087619580785021380
- Engagement: likes=37 reposts=1 replies=1 quotes=0 bookmarks=0 views=1978

Why mining firmware? The least-audited, most-exposed devices in Bitcoin:

💰 they earn directly (hashrate)
🌐 flat, unmonitored LANs
📦 closed firmware, fleet-shared defaults

Antbleed (2017): a remote kill switch in Antminer firmware, found by a user reading strings — not by an audit.

---

## 2026-08-12  Michael Schmid (@Schnitzel)

- URL: https://x.com/Schnitzel/status/2087619582928273443
- ID: 2087619582928273443
- Engagement: likes=21 reposts=1 replies=1 quotes=0 bookmarks=0 views=1597
- Media: https://pbs.twimg.com/media/HPi0AZaWkAAImCJ.png

What we've put on the bench:

🏭 Stock Bitmain: S19j Pro + S21 (live units, full flash dumps, Ghidra)
🛠 Third-party firmware: LuxOS, VNISH, Braiins OS
🌱 Open baselines: Mujina, AxeOS/Bitaxe

Method: static RE, live traffic capture, share-level reconciliation.

---

## 2026-08-12  Michael Schmid (@Schnitzel)

- URL: https://x.com/Schnitzel/status/2087619586422088007
- ID: 2087619586422088007
- Engagement: likes=16 reposts=2 replies=2 quotes=0 bookmarks=0 views=1347
- Media: https://pbs.twimg.com/media/HPi0CURX0AA-uea.png

41 findings filed, each with evidence + a reproduction recipe.

Hygiene bugs everyone has, stock included:

🚪 unauthenticated factory APIs
🔓 local paths to root
🗝 fleet-default credentials
💂 vendor SSH keys baked into images
📥 updates that don't verify what they install

---

## 2026-08-12  Michael Schmid (@Schnitzel)

- URL: https://x.com/Schnitzel/status/2087619589303574841
- ID: 2087619589303574841
- Engagement: likes=24 reposts=0 replies=2 quotes=0 bookmarks=0 views=1000

Now the counterintuitive part.

On stock Bitmain — a full decompile of both miner daemons + live connection tables — we found no hashrate skimming, no kill switches, no covert beacons.

The firmware everyone knocks on features is the cleanest we've tested on trust 👀

---

## 2026-08-12  Michael Schmid (@Schnitzel)

- URL: https://x.com/Schnitzel/status/2087619590922653700
- ID: 2087619590922653700
- Engagement: likes=20 reposts=0 replies=2 quotes=0 bookmarks=1 views=936
- Media: https://pbs.twimg.com/media/HPi0HVNXEAISsQx.png

Third-party "optimized" firmware is the opposite🔥. The behavior an owner can't see from the dashboard (and wouldn't choose) is concentrated there, not in stock.

Better features, worse trust. That's where our first coordinated disclosures are headed.

---

## 2026-08-12  Michael Schmid (@Schnitzel)

- URL: https://x.com/Schnitzel/status/2087619594064105932
- ID: 2087619594064105932
- Engagement: likes=15 reposts=0 replies=2 quotes=0 bookmarks=0 views=856

Bitmain came first because it's ~90% of the market. It won't be the last.

Next on the bench — the rest of the fleet:
🏭 MicroBT: Whatsminer
🏭 Canaan: Avalon
🏭 emerging: Auradine, Bitdeer (SEALMINER), ePIC

Same method, same rules. No firmware gets a pass.

---

## 2026-08-12  Michael Schmid (@Schnitzel)

- URL: https://x.com/Schnitzel/status/2087619595603509544
- ID: 2087619595603509544
- Engagement: likes=22 reposts=2 replies=2 quotes=0 bookmarks=1 views=987
- Media: https://pbs.twimg.com/media/HPi0JeZWIAAXOl6.jpg

Three responsible disclosures are already submitted: @Vnishfirmware , @luxor  and @Braiins . Each privately reported, 30 days to respond, then the 256 Red Team publishes.

Operators, harden today:
🧱 firewall 6060 / 4028 / 1534
🔄 rotate default creds
🏝 isolate miner VLANs

---

## 2026-08-12  Michael Schmid (@Schnitzel)

- URL: https://x.com/Schnitzel/status/2087619598317134332
- ID: 2087619598317134332
- Engagement: likes=22 reposts=1 replies=4 quotes=1 bookmarks=2 views=2530
- Media: https://pbs.twimg.com/media/HPi2FfiXsAA0aRK.jpg

Support the work:

💸 Donate to the 256 Foundation — a 501(c)(3) nonprofit, tax-deductible:
https://www.256foundation.org/donate

🖥 Donate hardware — reach out to @schnitzel. Testing real firmware takes real machines.

---

## 2026-08-12  Michael Schmid (@Schnitzel)

- URL: https://x.com/Schnitzel/status/2087650910021325238
- ID: 2087650910021325238
- Engagement: likes=14 reposts=1 replies=4 quotes=0 bookmarks=0 views=1547

Someone just donated a "Canaan Avalon Mini 3" for the 256-Red-Team 👀 🎉
Let's see what we can find on it. And of course after we dissect it also run Mujina on it, based on the epic work of @unknown_aadhi

---

## 2026-07-28  Public Pool (@Public_Pool_BTC)

- URL: https://x.com/Public_Pool_BTC/status/2081920674923253822
- ID: 2081920674923253822
- Engagement: likes=20 reposts=0 replies=2 quotes=0 bookmarks=1 views=3496

Actually, ASIC series architecture had been done with the original Bitaxe Hex, years before hammer stole and closed source esp-miner for their products.

---

## 2026-07-22  Tyler Stevens (@tylerkstevens)

- URL: https://x.com/tylerkstevens/status/2079986435126657421
- ID: 2079986435126657421
- Engagement: likes=52 reposts=15 replies=3 quotes=5 bookmarks=3 views=7520

Excited to announce the third Heatpunk Summit!

Feb 26-27 in Denver, CO.

Year 1: The First Gathering
Year 2: Formalizing the Movement
Year 3: The open-source stack is here

No More Barriers. What Will You Build?

Get on the waitlist to secure your spot!
https://www.heatpunks.org/summit

---

## 2026-07-10  Public Pool (@Public_Pool_BTC)

- URL: https://x.com/Public_Pool_BTC/status/2075431013497356538
- ID: 2075431013497356538
- Engagement: likes=420 reposts=86 replies=38 quotes=50 bookmarks=28 views=59319
- Media: https://pbs.twimg.com/media/HM1mUzHXYAADqO4.jpg

🎉 Block #2 on hosted Public-Pool. By a lone Bitaxe. 
https://mempool.space/block/00000000000000000000f4f8c91a6c400c42a40577fafa2ca2231d78f1955424

---

## 2026-06-05  Public Pool (@Public_Pool_BTC)

- URL: https://x.com/Public_Pool_BTC/status/2062950516544372833
- ID: 2062950516544372833
- Engagement: likes=171 reposts=43 replies=24 quotes=6 bookmarks=38 views=18136

🎉 Public-Pool Announcements: 🎉
1⃣ With the release of Stratum V2 support on Bitaxe/ESP-Miner (v2.14.0),
https://web.public-pool.io/ now supports Stratum V2! 
Simply configure your miner for SV2 in advanced pool options and provide the public key 9c4zpyJ2ndm4e8sP2uNc1VNCGxYjqaxWS6wUCjk8zFj6njFquH6
Special thanks to warioishere + https://t.co/t606fgM6gj for the implementation details and respecting the open source license 💪
2⃣ The last several months of improvements have been merged into the main sqlite branch and pushed to @umbrel and @start9labs app stores. Pending their approval, upgrading is recommended for those running public-pool at home!
Hash on.

---

## 2026-05-14  Public Pool (@Public_Pool_BTC)

- URL: https://x.com/Public_Pool_BTC/status/2054996503232475144
- ID: 2054996503232475144
- Engagement: likes=68 reposts=4 replies=5 quotes=0 bookmarks=3 views=2667

I think before Bitaxe the home mining market was stagnant and nearly non existent. Your choices where usb sticks or full sized machines. To suggest that it is somehow holding back innovation is fucking stupid.
"it was about time, someone disrupted that business."

---

## 2025-08-17  Public Pool (@Public_Pool_BTC)

- URL: https://x.com/Public_Pool_BTC/status/1957212121869267255
- ID: 1957212121869267255
- Engagement: likes=135 reposts=22 replies=3 quotes=0 bookmarks=8 views=8975

Since this post, the Bitcoin network hashrate has increased 2X. The hashrate of open-source miners has surged 10X, from the 201 Ultra to the Nerdqaxe++. Production capacity is orders of magnitude higher, prices are lower, and availability is now global.

Sometimes progress seems slow until you reflect on how far we've come. 🔭 There's no time to slow down, though. Today's eight consecutive blocks from @FoundryServices highlight the importance of this work and how much more we have to do.

---

## 2025-06-05  skot (@skot9000)

- URL: https://x.com/skot9000/status/1930622245367410710
- ID: 1930622245367410710
- Engagement: likes=274 reposts=37 replies=32 quotes=7 bookmarks=18 views=28005

If by Bitaxe in every home you mean; an enormous global legion of miners running open source hardware, firmware and software with a wide variety of hashrate in all sorts of decentralized home mining, stranded energy, heat reuse, and innovative new applications we can’t even imagine yet, who are largely immune to regulation, aren’t cucks to FPPS shenanigans, can afford to run through low periods of low fiat profitability, aren’t totally beholden to a single Chinese mega corp’s equipment and aren’t just appeasing investors until they can pivot to high performance computing artificial intelligence whatever… then yes, that fixes Bitcoin mining.

And that’s exactly what we’re going to do. 🔥

---

## Coverage gaps

Not exhaustive. High-reach threads prioritized. Missing: full @skot9000 timeline, @wantclue timeline, @jungly, @unknown_aadhi Canaan port original, @ry3t_official, Bitaxe Gamma Hex Mining Disrupt thread, MolonLabeVC feud thread. Batch 2 will page those.
