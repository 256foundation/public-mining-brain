# S19 Loki Space Heat Build Guide by HeatJack

> Source: https://forum.heatpunks.org/t/s19-loki-space-heat-build-guide-by-heatjack/250
> Collected: 2026-10-10
> Published: 2026-02-02
> Registry ID: heatpunks-forum

HeatJack | 2026-02-02 22:06:03 UTC | #1

Finally stepping out of the shadows because I may have gone a little overboard with my latest winter project: turning a Loki miner into a space heater. With the cold settling in and my office already chewing through 900 - 1500W of heat every day, it occurred to me that my ‘dumb heater’ could stand to earn its keep. I found a solid deal on a used S19J Pro and decided to piece together a setup using off the shelf parts from Amazon and other sources online. Turns out, with a little creativity you can turn an ASIC into a surprisingly effective (and not so dumb) space heater.

I’ll admit, this turned into a small research project. Huge thanks to everyone who has posted in this info online! Your info and builds made it much easier to understand what’s possible with these miners and how to repurpose them. I was overwhelmed at first, so I bought a bit of everything: APW3++ PSUs, Loki board kits, 120mm PC fans, 4 AWG wire, WiFi dongles and Resistor packs. Looking back I definitely over complicated things, but the learning process was worth it. In the end, I only ended up needing the core build components I listed below for a S19.

With that said here’s my S19J Pro dual‑hashboard build guide:

**Core Build Components:**

1x S19 ASIC Miner Variant (Can be found used online/marketplace)

1x Pack of 1Ω resistors - [Amazon](https://a.co/d/0Ck8KbJ)

2-4x 120mm Arctic P12 Pro PST fans - [Amazon](https://a.co/d/5YziBsE)
(**Tip:** The 5 pack on [Amazon](https://a.co/d/09U6v9zp) brings the fan cost down, use 4 fans + a spare)

2-3x 60mm PSU fans (Thermalright TL‑B6B) - [Amazon](https://a.co/d/6bmdC6)

1-2x CRJ Mini 2‑Pin → 3/4‑Pin fan adapter cables (2 per pack, 3 are needed if replacing all PSU fans) - [Amazon](https://a.co/d/eq3g3Sz)

1x Vonets WiFi dongle (if using WiFi; otherwise use Ethernet cable) - [Amazon](https://a.co/d/arvl9NV)

1x PSU power cord (seller claims 14 AWG - DYOR) - [eBay](https://www.ebay.com/itm/396075405327)

**Guides & References:**

[Pivotal Pleb’s APW12 120V Unlock Guide](https://cdn.shopify.com/s/files/1/0710/7362/8440/files/APW3_Voltage_Mod_Guide_Revision_3.pdf?v=1691019011)
[Stackin Sats Podcast YouTube Channel](https://youtu.be/OSICDVew1-U) - @[Trevorbello](https://forum.heatpunks.org/u/trevorbello)
@[Josh’s](https://forum.heatpunks.org/u/josh) Loki builds [here](https://forum.heatpunks.org/t/loki-rig-builds/112) – Great examples of Loki Builds!

**Tools & Supplies:**

Soldering iron (70W or higher recommended)
Solder
Reflow station with heat gun or heat source (for removing PCB coating)
Hot glue gun (to secure resistors on the APW12 board)
Flush cutters (to cut off the excess resistor leads)
Screwdriver
X‑Acto knife or small sharp blade

**Optional parts, but helpful if using Home Assistant & sensors:**

1x Sonoff S31 WiFi Smart Plug (Flash with [Tasmota](https://tasmota.github.io/docs/devices/Sonoff-S31/) or [ESP Home](https://roborooter.com/post/flashing-sonoff-s31-with-esphome/)) - [eBay](https://www.ebay.com/itm/406128350648)

1x FTDI USB UART IC FT232RL USB to Serial (**Tip:** Raspberry Pi can be used to flash the S31 smart plug FW) - [Amazon](https://a.co/d/5rZydra)

1x Pack of Test Hook to Female Jumper Wires - [Amazon](https://a.co/d/6hjm1jL)

1x Shelly H&T Smart WiFi Temp Sensor - [Amazon](https://a.co/d/9eUUmQr)

**Build Notes:**

**Stock S19 Miner Fans:** Are very loud and annoying! If you can’t stand that high‑pitched whine swap them out ASAP. The stock PSU fans don’t offer easy speed control unless you add an inline resistor, or you replace the 60mm PSU fans with quieter ones while you already have the PSU open for the resistor mod. If you’re upgrading the 120mm hashtunnel fans, the plastic guide on the fan connector needs to be trimmed so they fit properly into the fan headers on the miner’s control board:

[![120mm Fan Connector Trim](https://forum.heatpunks.org/uploads/default/optimized/1X/ea543325e3466918e238ea080ecd7ace2416c698_2_281x375.jpeg)120mm Fan Connector Trim750×1000 130 KB](https://forum.heatpunks.org/uploads/default/original/1X/ea543325e3466918e238ea080ecd7ace2416c698.jpeg)

PSU Fan Adapters (CRJ Mini 2‑Pin → 3/4‑Pin Fan):

[![PSU Fan Adapters](https://forum.heatpunks.org/uploads/default/optimized/1X/da4db40d4b58470dba0f43dd9e8831ee10961e91_2_328x375.jpeg)PSU Fan Adapters712×811 152 KB](https://forum.heatpunks.org/uploads/default/original/1X/da4db40d4b58470dba0f43dd9e8831ee10961e91.jpeg)

PSU Fan Adapters (CRJ Mini 2‑Pin → 3/4‑Pin Fan) - **Tip:** Route fan cables under each fan for easy cable management. I only swapped out 2 of three fans - YMMV.

[![PSU Fan Adapter Bundle](https://forum.heatpunks.org/uploads/default/optimized/1X/1872d883c964b01c15208957d9e873bf6302afdc_2_377x500.jpeg)PSU Fan Adapter Bundle574×761 144 KB](https://forum.heatpunks.org/uploads/default/original/1X/1872d883c964b01c15208957d9e873bf6302afdc.jpeg)

**PSU Board Coating:** Removing the protective coating on the PSU board can be tedious, so take your time with this step. Gently heating the area with a hot air gun or a small torch held at a safe distance softens the coating and makes it much easier to scrape away. Always do this in a well ventilated space since heating the PCB coating can release harmful fumes. (**Tip:** If you start to see copper, **STOP!** You’ve gone too far, possibly cutting copper traces. Gently cut and pick at the silver area on either side of the 0805 surface mount chip resistors on the PCB):

[![PP - Guide Photos](https://forum.heatpunks.org/uploads/default/optimized/1X/043994c83b7ebbc76edca38719c6f01a6a888077_2_690x212.jpeg)PP - Guide Photos848×261 83.6 KB](https://forum.heatpunks.org/uploads/default/original/1X/043994c83b7ebbc76edca38719c6f01a6a888077.jpeg)

The [Pivotalpleb APW12 120 Volt Unlock Guide](https://cdn.shopify.com/s/files/1/0710/7362/8440/files/APW12_120V_Unlock_Guide_Revision_3.pdf?v=1706840604) covers this topic in depth, so I highly recommend you read through Zack’s guide. #Photo Creds: Zack @ [Pivotalpleb.com](http://Pivotalpleb.com)

**Air Baffle Kits:** I tested my S19 in both single‑board and dual‑board configurations. In the end, I went with the dual‑board setup for the extra hashrate and the added heat output since it warms my office better. The air baffle kits from [structur3.io](http://structur3.io) make a huge difference in airflow, temp control and overall performance. STL files are available [here](https://github.com/SatStackingPleb/S19-Air-Baffle-Kit). (**Tip:** Depending on your specific miner model, you may need to print the “Pro” version of the STL. Each baffle is split into two halves. Print the S19 intake section, then pair it with the exhaust section that matches your miner model. For example: I printed an S19 intake and an S19 Pro exhaust to match my S19 Pro. Once both halves are printed, combine them to complete the baffle. Great work done by: @[Satstackingpleb](https://forum.heatpunks.org/u/satstackingpleb)) - The PSU & hashtunnel fans flow like this:

[![S19 Fan Flow](https://forum.heatpunks.org/uploads/default/optimized/1X/411cf7ecbc03833382e6ca1b809c246cffdb2dbb_2_447x375.jpeg)S19 Fan Flow723×606 75.9 KB](https://forum.heatpunks.org/uploads/default/original/1X/411cf7ecbc03833382e6ca1b809c246cffdb2dbb.jpeg)

**Miner Firmware:** I choose to run [LuxOS](https://luxor.tech/firmware) and have been very satisfied with the results. [Structur3.io](http://Structur3.io) has some great power performance profiles listed at the bottom of this [page](https://structur3.io/products/s19-single-or-dual-board-air-baffle-set). I would use those settings as a starting point, if you opt for a dual hashboard setup the TH/s double and so does the power. To get LuxOS on your miner you must install the [stock Bitmain/Antminer firmware provided by LuxOS](https://docs.luxor.tech/firmware/kb/sdrecovery/JPro/jpro7007) and then use LuxOS commander to install LuxOS. The ATM feature is quite handy in LuxOS to tune your miner. I have the following values set:

Temperature & ATM:

[![Miner ATM Config](https://forum.heatpunks.org/uploads/default/optimized/1X/a40267a5ab1812a8efb88bffe422b4b0bd2e73d8_2_690x319.png)Miner ATM Config1633×755 128 KB](https://forum.heatpunks.org/uploads/default/original/1X/a40267a5ab1812a8efb88bffe422b4b0bd2e73d8.png)

LuxOS ATM Temp Settings:

[![Miner ATM Temps](https://forum.heatpunks.org/uploads/default/optimized/1X/43df3986e2e5fe0d1b72c9a5d5c8859013931b93_2_690x217.png)Miner ATM Temps1608×506 80 KB](https://forum.heatpunks.org/uploads/default/original/1X/43df3986e2e5fe0d1b72c9a5d5c8859013931b93.png)

**WiFi Dongle Power:** Right now I’m powering the Vonets WiFi dongle with a standard USB wall adapter. It works fine, but there are cleaner ways to do it. You can use a dedicated WiFi bridge power splicer from [ixtech.xyz](https://ixtech.xyz/products/12v-to-5v-splicer?variant=44511807865090) - or if you’re comfortable with a bit of tinkering, tap into the control board power cables and build your own power feed.

[![ixtech wifi power dongle](https://forum.heatpunks.org/uploads/default/optimized/1X/9922f65e0f633c9e82665caa9b8b40391bead271_2_288x250.webp)ixtech wifi power dongle832×721 15.7 KB](https://forum.heatpunks.org/uploads/default/original/1X/9922f65e0f633c9e82665caa9b8b40391bead271.webp)

**Home Assistant Integration:** The Exergy Stealthminer integration [GitHub](https://github.com/exergyheat/ha-integration-stealthminer) works right out of the box with Home Assistant. During setup, it will prompt you for the miner’s IP address and port. I initially entered my miner’s IP with port 4028, but kept running into errors. Leaving the port at the default 8080 solved the issue immediately. I use this integration heavily with my power plug and temp sensor. Great work done by: @[tylerkstevens](https://forum.heatpunks.org/u/tylerkstevens) & @[tronsington](https://forum.heatpunks.org/u/tronsington)

**Build Pictures** (Cardboard air baffle setup pictured… because HeatPunk, the cooling results convinced me to 3D print the actual air baffles):

Dual-Board Setup:

[![S19 Hashtunnel 2 Board](https://forum.heatpunks.org/uploads/default/optimized/1X/94d364dace5aa5a3164c4cdf31c6c4d19abe3ac1_2_261x375.jpeg)S19 Hashtunnel 2 Board891×1280 423 KB](https://forum.heatpunks.org/uploads/default/original/1X/94d364dace5aa5a3164c4cdf31c6c4d19abe3ac1.jpeg)

Single-Board Setup:

[![S19 Hashtunnel 1 Board](https://forum.heatpunks.org/uploads/default/optimized/1X/5b19ca6655d5b1b79a7c5e4bcf85cbf9e4171974_2_276x375.jpeg)S19 Hashtunnel 1 Board947×1280 304 KB](https://forum.heatpunks.org/uploads/default/original/1X/5b19ca6655d5b1b79a7c5e4bcf85cbf9e4171974.jpeg)

LuxOS Dashboard Stats:

[![Miner Dashboard - Stats](https://forum.heatpunks.org/uploads/default/optimized/1X/4c8ab652aaa2f2b55917339e5038a3b9f18a87b1_2_690x103.png)Miner Dashboard - Stats1096×165 27.2 KB](https://forum.heatpunks.org/uploads/default/original/1X/4c8ab652aaa2f2b55917339e5038a3b9f18a87b1.png)

[![Miner Hashboard - Stats](https://forum.heatpunks.org/uploads/default/optimized/1X/b1ff5ed036ca44222d9e037e9617c3164938ac7b_2_690x214.png)Miner Hashboard - Stats1058×329 48 KB](https://forum.heatpunks.org/uploads/default/original/1X/b1ff5ed036ca44222d9e037e9617c3164938ac7b.png)

**Custom Home Assistant Dashboards I created** (Thanks to the [xergyheat](https://github.com/exergyheat) HA integration):

Miner stats, BTC network stats w/active “real-time heat rebate” stats that adjust to network, hashrate and power usage:

[![HA Miner Stats](https://forum.heatpunks.org/uploads/default/original/1X/6fa4096966326979fb8f0b686a96d54a130d6e2a.png)HA Miner Stats750×309 33.7 KB](https://forum.heatpunks.org/uploads/default/original/1X/6fa4096966326979fb8f0b686a96d54a130d6e2a.png)

[![HA Miner Stats Summary](https://forum.heatpunks.org/uploads/default/original/1X/4fce4c5bd7a8caa1b800b29607808faa7164c5c5.png)HA Miner Stats Summary308×370 20.1 KB](https://forum.heatpunks.org/uploads/default/original/1X/4fce4c5bd7a8caa1b800b29607808faa7164c5c5.png)

Miner estimate earnings (pool mining), power usage stats and chart for single pane view:

[![HA Miner Power and Earnings](https://forum.heatpunks.org/uploads/default/optimized/1X/50f7dc78dd30c6a2f1a1a771a95152dc735bdb65_2_690x208.png)HA Miner Power and Earnings1202×364 59.7 KB](https://forum.heatpunks.org/uploads/default/original/1X/50f7dc78dd30c6a2f1a1a771a95152dc735bdb65.png)

[![HA Miner Chart](https://forum.heatpunks.org/uploads/default/optimized/1X/2f0289d7384bd694b05bcdba951977a208949fcc_2_690x205.png)HA Miner Chart1602×477 79.9 KB](https://forum.heatpunks.org/uploads/default/original/1X/2f0289d7384bd694b05bcdba951977a208949fcc.png)

Smart plug wall power reporting vs Miner power stats:

[![HA Miner Power Stats](https://forum.heatpunks.org/uploads/default/optimized/1X/57966b2204f1c4a8984dc241b4c9a292b139cf2d_2_690x193.png)HA Miner Power Stats1584×444 88.3 KB](https://forum.heatpunks.org/uploads/default/original/1X/57966b2204f1c4a8984dc241b4c9a292b139cf2d.png)

Over time I plan on updating post this as my heater goes though different configurations. Feel free to ask any questions and I’ll respond when time allows.

****** If you found this guide helpful and plan to share, reference or build upon it please make sure to credit the original creators. Clear and visible attribution not only respects the work that went into it, it strengthens the entire HeatPunk ecosystem by keeping knowledge traceable and collaborative. ******

-HeatJack

-------------------------

tylerkstevens | 2026-02-02 22:16:34 UTC | #2

Dude! This is incredible. Would love to have you join us at the Heatpunk Summit later this month in Denver to share more of your experience. Email me at [admin@heatpunks.org](mailto:admin@heatpunks.org) if you’re interested!

-------------------------

HeatJack | 2026-02-06 16:46:28 UTC | #3

Weekend forecast: 100% chance of reclaimed heat. More updates on my space heater:

I was able to print the new air baffles and install vibration pads.

**Retiring the OG cardboard heat management system…**

[![Baffle_Cardboard](https://forum.heatpunks.org/uploads/default/optimized/1X/495cffe5f9bd3351754106f2e6e1e42446dc2de5_2_255x375.jpeg)Baffle_Cardboard1000×1462 188 KB](https://forum.heatpunks.org/uploads/default/original/1X/495cffe5f9bd3351754106f2e6e1e42446dc2de5.jpeg)

**Hot off the printer (next-gen airflow wrangler):**

[![Baffle_Set](https://forum.heatpunks.org/uploads/default/optimized/1X/ea884f5e4dcef109dd962590a98a3e3fb5a1d0dd_2_517x300.jpeg)Baffle_Set1783×1036 184 KB](https://forum.heatpunks.org/uploads/default/original/1X/ea884f5e4dcef109dd962590a98a3e3fb5a1d0dd.jpeg)
#credit: @Satstackingpleb - [STL files](https://github.com/SatStackingPleb/StealthMiner)

**New air baffles installed:**

[![Baffle_Half_Part1](https://forum.heatpunks.org/uploads/default/optimized/1X/6c57df3789e11f8ab6ffbd1e8c4d573809bd8a56_2_296x375.jpeg)Baffle_Half_Part11013×1280 265 KB](https://forum.heatpunks.org/uploads/default/original/1X/6c57df3789e11f8ab6ffbd1e8c4d573809bd8a56.jpeg)

[![Baffle_Half_Part2](https://forum.heatpunks.org/uploads/default/optimized/1X/de2e7b7e42639f20a5807d3b70454853a514eca7_2_291x375.jpeg)Baffle_Half_Part2981×1262 277 KB](https://forum.heatpunks.org/uploads/default/original/1X/de2e7b7e42639f20a5807d3b70454853a514eca7.jpeg)

**Vibration pads installed to help tame fan harmonics:**

[![Heater_Pads](https://forum.heatpunks.org/uploads/default/optimized/1X/08ca443a8a608dc997d3e4b8512cd789ed2c2f39_2_517x309.jpeg)Heater_Pads1694×1014 242 KB](https://forum.heatpunks.org/uploads/default/original/1X/08ca443a8a608dc997d3e4b8512cd789ed2c2f39.jpeg)
(Furniture pads from [Amazon](https://a.co/d/06n1SVnb))

-------------------------

Plunger | 2026-02-12 01:32:01 UTC | #4

Really nice project. Love the printed baffles. 41% reduction in heating cost is stellar. I have a S19 setup kit from Toine at 256Heat. I have to get that going. Its all put together but haven’t had time to play with it yet. Luxe OS looks really clean too. Nice job.

-------------------------

HeatJack | 2026-02-18 06:11:04 UTC | #5

@Plunger Thanks, this project has paid some dividends! Toine has some nice kits, I hope you get yours running soon. Honestly, LuxOS has been my go‑to miner OS/FW for this setup. Their crew is doing some awesome stuff for us Heatpunks. If you peek at their latest release notes, it kinda feels like they were like, “Bro… what if we just made a whole update about heat reuse?” Here’s the [LuxOS changelog from 2026‑02‑11](https://docs.luxor.tech/firmware/changelog#2026-02-11) if you wanna flip through it with some notes:

- Added option to [bypass](https://docs.luxor.tech/firmware/api/luxminer/psuset) the PSU for custom builds. - PSU models like the APW3 can be used once the voltage is adjusted, making loki boards *optional*. The APW12 still needs a resistor mod to ‘trick’ the brown out detectors, no loki needed.

- Added support for S19k Pro BHB56907.

- Added option to [continue hashing](https://docs.luxor.tech/firmware/api/luxminer/pooloptsset) even when network or pools disconnect. - Avoids those annoying stop‑start cycles where the miner idles, cools off, then ramps back up. That’s inefficient for both heat reuse and hardware stability. Sure, you’re hashing into the void for a bit, but we’re Heatpunks. Half the reward is the heat anyway… right?

- Added option to start machine with quiet [fans](https://docs.luxor.tech/firmware/api/luxminer/fanset). - QOL setting, may interfere with LuxOS curtail settings… TBD.

- Added UI support for bypassing the PSU, hashing on disconnect, and more fan controls. - APIs controlled these settings in the past, now baked right into the dashboard.

- Reduced [minimum fan speed](https://docs.luxor.tech/firmware/api/luxminer/fanset) low threshold from 20 to 10. - I wouldn’t push this setting too low, or you’ll end up cooking your hashboards like a backyard pig roast at the Space.

[![image](https://forum.heatpunks.org/uploads/default/optimized/1X/1ef0a7949d7e55b6196717fc4ec4190d7d6806bb_2_690x497.jpeg)image1078×778 103 KB](https://forum.heatpunks.org/uploads/default/original/1X/1ef0a7949d7e55b6196717fc4ec4190d7d6806bb.jpeg)

[![image](https://forum.heatpunks.org/uploads/default/optimized/1X/110ad9c99b5e5c22c6cee887c19c8cdad97211aa_2_690x439.jpeg)image1198×763 98 KB](https://forum.heatpunks.org/uploads/default/original/1X/110ad9c99b5e5c22c6cee887c19c8cdad97211aa.jpeg)

Photo creds: @altair_tech

-------------------------

HeatJack | 2026-02-22 17:49:36 UTC | #6

Sunday forecast: Some cable management, questionable engineering. More updates on my space heater:

Because the heater refuses to stay in one room, the extra power adapters had to go. I hardwired the VONETS VAP11G‑300 into the control board power port and slipped the cut USB barrel jack through the closest PCB opening. This WIFI dongle can support 5V-15V (Typical 5V/1A, ripple less than 100mV) the average power consumption is less than 2.5W:

[![VAP11G-300_Back](https://forum.heatpunks.org/uploads/default/original/1X/fa140d3edac1a584e24ee000973eba1b8d863adc.jpeg)VAP11G-300_Back373×237 15.6 KB](https://forum.heatpunks.org/uploads/default/original/1X/fa140d3edac1a584e24ee000973eba1b8d863adc.jpeg)

**USB DC barrel jack added to the S19 control board for direct power:**

[![Miner_CB_Bottom](https://forum.heatpunks.org/uploads/default/optimized/1X/6178a7359f3d52b327a56131f3388c52bc9b68a9_2_378x374.jpeg)Miner_CB_Bottom1920×1902 670 KB](https://forum.heatpunks.org/uploads/default/original/1X/6178a7359f3d52b327a56131f3388c52bc9b68a9.jpeg)

**S19 control board top view:**

[![Miner_CB_Top](https://forum.heatpunks.org/uploads/default/optimized/1X/876d3e9b77ec39f072249c6c1c70a1763501b8e4_2_312x375.jpeg)Miner_CB_Top1065×1280 285 KB](https://forum.heatpunks.org/uploads/default/original/1X/876d3e9b77ec39f072249c6c1c70a1763501b8e4.jpeg)

**Pro Tip:** When tearing these boards down, take it slow. Most used miners are on borrowed time and the connectors are crispier than KFC chicken. The small six-pin APW12 board connector nearly crumbled just from breathing on it, disconnect it from the PSU side:

[![Miner_CB_Top_Sixpin](https://forum.heatpunks.org/uploads/default/optimized/1X/9b6b58624ee58b867b760a4f662c12c7a0b5e9b6_2_312x375.jpeg)Miner_CB_Top_Sixpin1065×1280 354 KB](https://forum.heatpunks.org/uploads/default/original/1X/9b6b58624ee58b867b760a4f662c12c7a0b5e9b6.jpeg)

(Credits: Zack @ [Pivotalpleb.com](http://Pivotalpleb.com) for posting this online, circa 2023!)
