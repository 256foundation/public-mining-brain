# Mining hardware comparison — Bitcoin Wiki (wikitext)

> Registry ID: bitcoin-wiki
> Source: https://en.bitcoin.it/wiki/Mining_hardware_comparison (captured via ?action=raw)
> Collected: 2026-10-10
> Published: 2023-03-28T08:21:56Z (last revision)
> Posture: verbatim (MediaWiki wikitext source)
> As-Of: 2026-10-10

{{seealso|Non-specialized hardware comparison}}
Below are statistics about the Bitcoin [[Mining]] performance of [[ASIC]] hardware and '''only includes specialized equipment that has been shipped.'''

GPUs, CPUs and other hardware not specifically designed for Bitcoin mining can be found in the [[Non-specialized_hardware_comparison]].

'''Notes:''' 
* Mhash/s = millions [[hash per second|hashes per second]] ([[Protocol_specification#Hashes|double sha256]] raw speed performance; may not be very energy efficient with some models)
* Mhash/J = millions hashes per joule (energy efficiency; 1 joule of energy is 1 watt during 1 second: 1 J = 1 W*s)
* W = watt (maximum power consumption, i.e. energy per unit of time: 1 W = 1 J/s)

== ASIC ==

'''Be sure to research any of these vendors and machines intensely before spending any money.'''

{| class="wikitable sortable"
|+ Bitcoin [[Protocol_specification#Hashes|double SHA256]] ASIC mining hardware
! data-sort-type="text" | Product !! data-sort-type="number" | Advertised Mhash/s !! data-sort-type="number" | Mhash/J !! data-sort-type="number" | Mhash/s/$ !! data-sort-type="number" | Watts !! data-sort-type="currency" | Price (USD) !! data-sort-type="date" | Currently shipping !! class="unsortable" | Comm ports !! class="unsortable" | Dev-friendly	
|-	
! [[AntMiner]] S1 <ref name="AntMinerS1">[https://web.archive.org/web/20140210130418/https://www.bitmaintech.com/productDetail.htm?pid=00020140107162747992Ce5uBuxW06D6] Retrieved 2014-02-01</ref>
| 180,000 || 500 || 602|| 360 || 299<ref name="nopsu">Power supply not included</ref> || {{No|Discontinued}} || Ethernet || {{No|GPL infringement}}
|-
! [[AntMiner]] S2 <ref name="AntMinerS2">[https://web.archive.org/web/20140701203234/https://www.bitmaintech.com/productDetail.htm?pid=00020140429083756017VwGm90Xx06B5] Retrieved 2014-07-01</ref>
| 1,000,000 || 900|| 442|| 1100|| 2259|| {{No|Discontinued}} || Ethernet || {{No|GPL infringement}}
|-
! [[AntMiner]] S3 <ref name="AntMinerS3">[https://web.archive.org/web/20141011063608/https://bitmaintech.com/productDetail.htm?pid=00020140917060843699l3bEXYxL06C0 Ant Miner S3 product page] Retrieved 2014-08-06</ref>
| 441,000 || 1300|| 1154|| 340|| 382<ref name="nopsu"/> || {{No|Discontinued}} || Ethernet || {{No|GPL infringement}}
|-
! [[AntMiner]] S3+ <ref name="AntMinerS3+">[https://web.archive.org/web/20141011063608/https://bitmaintech.com/productDetail.htm?pid=00020140917060843699l3bEXYxL06C0 Ant Miner S3+ product page] Retrieved 2014-10-11</ref>
| 453,000 || 1282|| 1198|| 355|| 363<ref name="nopsu"/> || {{No|Discontinued}} || Ethernet || {{No|GPL infringement}}
|-
! [[AntMiner]] S4 <ref name="AntMinerS4">[https://web.archive.org/web/20141009041433/https://www.bitmaintech.com/productDetail.htm?pid=00020140926075515819D846Og240603 Ant Miner S4 product page] Retrieved 2014-10-01</ref>
| 2,000,000 || 1429|| 1429 || 1400 || 1400 || {{No|Discontinued}} || Ethernet || {{No|GPL infringement}}
|-
! [[AntMiner]] S5 <ref name="AntMinerS5">[https://web.archive.org/web/20160322181226/https://bitmaintech.com/productdetail.htm?pid=000201412231604153619o9x1obn0693 Ant Miner S5 product page] Retrieved 2015-02-04</ref>
| 1,155,000 || 1957 || 3121 || 590 || 370 || {{No|Discontinued}} || Ethernet || {{No|GPL infringement}}
|-
! [[AntMiner]] S5+ <ref name="AntMinerS5Plus">[https://web.archive.org/web/20160330065342/https://www.bitmaintech.com/productDetail.htm?pid=0002015081407532655504JMKzsM067B Ant Miner S5+ product page] Retrieved 2015-09-16</ref>
| 7,722,000 || {{#expr:1/0.445 * 1000 round 0}} || {{#expr:7722000 / 2307 round 0}} || 3,436 || 2,307 || {{No}} || Ethernet || {{No|GPL infringement}}
|-
! [[AntMiner]] S7 <ref name="AntMinerS7">[https://web.archive.org/web/20160330113135/https://www.bitmaintech.com/productDetail.htm?pid=00020150827084021471OHYdwd9D06A0 Ant Miner S7 product page] Retrieved 2015-09-16</ref>
| 4,860,000 || {{#expr:1/0.25 * 1000 round 0}} || {{#expr:4860000 / 1823 round 0}} || 1,210 || 1,823|| {{No}} || Ethernet || {{No|GPL infringement}}
|-
! [[AntMiner]] S9 <ref name="AntMinerS9">[https://web.archive.org/web/20160708221612/https://www.bitmaintech.com/productDetail.htm?pid=0002016052907243375530DcJIoK0654 Ant Miner S9 product page] Retrieved 2016-07-02</ref>
| 14,000,000 || 10182 || 5833 || 1,375 || 2,400 || {{Yes}} || Ethernet || {{No|GPL infringement}}
|-
! [[AntMiner]] U1 <ref name="AntMinerU1"/>
| 1,600 || 800 || 55 || 2 || 29 || {{No|Discontinued}} || USB || {{Yes|code, samples}}
|-
! [[AntMiner]] U2+ <ref name="AntMinerU2"/>
| 2,000 || 1,000 || 115 || 2 || 17 || {{No|Discontinued}} || USB || {{No|code}}
|-
! [[AntMiner]] U3 <ref name="AntMinerU3">[https://www.bitmaintech.com/productDetail.htm?pid=00020150109104550452NTD3NdYY0669 Antminer U3 product page] Retrieved 2015-02-06</ref>
| 63,000 || 1,000 || 1658 || 63 || 38 || {{Yes}} || USB || {{No|code}}
|-
! [[ASICMiner]] BE Blade
| 10,752 || 129 || 28<ref name="bcprice"/> || 83 || 350<ref name="nopsu"/><ref name="bcprice"/> || {{No|Discontinued}} || Ethernet || {{Patch|samples}}
|-
! [[ASICMiner]] BE Cube
| 30,000 || 150 || 55 || 200 || 550<ref name="nopsu"/><ref name="bcprice"/> || {{No|Discontinued}} || Ethernet || {{Patch|samples}}
|-
! [[ASICMiner]] BE Sapphire
| 336 || 130 || 17<ref name="bcprice"/> || 2.55 || 20<ref name="bcprice">Actual price is in bitcoins. USD value estimated.</ref> || {{No|Discontinued}} || USB || {{Yes|samples}}
|-
! [[ASICMiner]] BE Tube <ref name="AM tube">[https://bitcointalk.org/index.php?topic=735728.0 ASICMiner Tube Sales Thread]</ref>
| 800,000 || 888 || 2500 || 900 || 320<ref name="nopsu"/> || {{No|Discontinued}} || Proprietary || {{Patch|samples}}
|-
! [[ASICMiner]] BE Prisma <ref name="AM prisma">[https://bitcointalk.org/index.php?topic=791827.0 ASICMiner Prisma Sales Thread]</ref>
| 1,400,000 || 1333 || 2333 || 1100 || 600<ref name="nopsu"/> || {{No|Discontinued}} || Proprietary || {{No}}
|-
! [[Avalon]] Batch 1
| 66,300 <ref name="AvalonPowerUsage"/> || 107 || 52.34 || 620<ref name="AvalonPowerUsage"/> || 1299<ref name="avalon"/> || {{No|Discontinued}} || Ethernet, Wifi || {{No|code}}
|-
! [[Avalon]] Batch 2
| 82,000<ref name="avalon" /> || 117 || 54.70 || 700 || 1499<ref name="avalon" /> || {{No|Discontinued}} || Ethernet, Wifi || {{No|code}}
|-
! [[Avalon]] Batch 3
| 82,000<ref name="avalon" /> || 117 || 54.70 || 700 || 1499<ref name="avalon" /> || {{No|Discontinued}} || Ethernet, Wifi || {{No|code}}
|-
! [[Avalon2]]
| 300,000 || {{Patch|}} || {{Patch|}} || {{Patch|}} || 3075 || {{No|Discontinued}} || USB or Ethernet || {{Yes|code, docs, samples}}
|-
! [[Avalon3]]
| 800,000 || {{Patch|}} || {{Patch|}} || {{Patch|}} || {{Patch|}} || {{No|Discontinued}} || USB or Ethernet || {{Yes|code, docs, samples}}
|-
! [[Avalon6]]
| 3,500,000 || {{Patch|}} || {{Patch|}} || 1080 || {{Patch|}} || {{No|Discontinued}} || Ethernet || {{Patch|?}}
|-
! [[Avalon721]]
| 6,000,000 || 6000 || {{Patch|}} || 1000 || {{Patch|}} || {{No}} || Ethernet || {{Patch|?}}
|-
! Avalon741
| 7,300,000 || 6350 || 5035 || 1150 || 1450 || {{Yes}} || Ethernet || {{Patch|?}} <!-- 88 x A3212 16nm ASIC -->
|-
! Avalon761
| 8,800,000 || 6670 || 4730 || 1320 || 1860 || {{Yes}} || Ethernet || {{Patch|?}} <!-- 104 x A3212 16nm ASIC -->
|-
! Avalon821
| 11,000,000 || 9170 || 3800 || 1200 || 2900 || {{Yes|Bulk only}} || Ethernet || {{Patch|?}} <!-- 104 x A3210 16nm ASIC -->
|-
! bi*fury
| 5,000 || 1,176 || 24 || 4.25 || 209 || {{No|Discontinued}} || USB || {{Yes|docs, samples}}
|-
! BFL SC 5Gh/s
| 5,000 || 166 || 18.24 || 30 || 274 || {{No|Discontinued}} || USB || {{Yes|docs, samples}}
|-
! BFL SC 10 Gh/s
| 10,000 || {{Patch|}} || 200 || {{Patch|}} || 50 || {{No|Discontinued}} || USB || {{Yes|docs, samples}}
|-
! BFL SC 25 Gh/s
| 25,000 || 166 || 20.00 || 150 || 1249 || {{No|Discontinued}} || USB || {{Yes|docs, samples}}
|-
! BFL Little Single
| 30,000 || {{Patch|}} || 46.22 || {{Patch|}} || 649 || {{No|Discontinued}} || USB || {{Yes|docs, samples}}
|-
! BFL SC 50 Gh/s
| 50,000 || 166 || 50 || 300|| 984 || {{No|Discontinued}} || USB || {{Yes|docs, samples}}
|-
! BFL Single 'SC'
| 60,000 || 250 || 46.18 || 240 || 1299 || {{No|Discontinued}} || USB || {{Yes|docs, samples}}
|-
! BFL 230 GH/s Rack Mount<ref name="bf250">[https://products.butterflylabs.com/homepage-new-products/250-gh-s-rack-mount-bitcoin-miner.html "250 GH/s Rack Mount Bitcoin Miner"]. Butterfly Labs. Retrieved September 2, 2014.</ref>
| 230,000 || {{Patch|}} || 500|| {{Patch|}} || 399 (used) || {{No|Discontinued}} || USB || {{Patch|docs}}
|-
! BFL 500 GH/s Mini Rig SC
| 500,000 || 185 || {{Patch|}} || 2700 || 22484 || {{No|Discontinued}} || Wifi || {{Yes|docs, samples}}
|-
! BFL Monarch 700GH/s<ref name="bflmonarch">[https://products.butterflylabs.com/homepage-new-products/700-gh-bitcoin-mining-card.html "700GH/s Bitcoin Mining Card"]. Butterfly Labs. Retrieved September 25, 2014.</ref>
| 700,000 || 1428 || 508 || 490 || 1379 || {{No|Discontinued}} || PCIe, USB || {{Yes|docs, samples}}
|- 
! BitFury S.B.
| {{Patch|}} || {{Patch|}} || {{Patch|}} || {{Patch|}} || {{Patch|}} || {{No|Discontinued}} || RPi GPIO || {{No}}
|-
! Bitmine.ch Avalon Clone 85GH
| 85,000 || {{Patch|}} || 13 || 650 || 6489<ref>Depends on user configuration available from http://www.bitmine.ch</ref> || {{No|Discontinued}} || Ethernet, Wifi, USB || {{No|code}}
|-
! Black Arrow Prospero X-1
| 100,000 || 1000 || 270 || 100 || 370 || {{No|Discontinued}} || Ethernet || {{Patch|docs, samples}}
|-
! Black Arrow Prospero X-3
| 2,000,000 || 1000 || 333 || 2000 || 6000 || {{No|Discontinued}} || Ethernet || {{Patch|?}}
|-
! Blue Fury
| 2,500 || 1000 || 17.8 || 2.5 || 140 || {{No|Discontinued}} || USB || {{Yes|code, samples}}
|-
! BTC Garden AM-V1 310 GH/s<ref name="btcgarden">[https://bitcointalk.org/index.php?topic=622439.0 "BTCGarden Sales Thread"]</ref>
| 310,000 || 954 || 1003 || 324 || 309<ref name="nopsu"/> || {{No|Discontinued}} || RPi GPIO || {{No}}
|-
! BTC Garden AM-V1 616 GH/s<ref name="btcgarden" />
| 616,000 || 951 || 1760 || 648 || 350<ref name="nopsu"/> || {{No|Discontinued}} || RPi GPIO || {{No}}
|-
! [[CoinTerra]] TerraMiner IV
| 1,600,000 || {{Patch|}} || 1066.67 || 2100 || 1500 || {{No|Discontinued}} || Ethernet || {{Yes|docs, code, samples}}	
|-
! Drillbit
| {{Patch|}} || {{Patch|}} || {{Patch|}} || {{Patch|}} || {{Patch|}} || {{No|Discontinued}} || USB || {{Yes|code, samples}}
|-
! [[Ebit]] E9 <ref name="EbitE9">[http://miner.ebang.com.cn/ Company home page] Retrieved 2018-01-22</ref>
| 6,300,000 || 7140 || 4468 || 882 || 1410 || {{No}} || Ethernet || {{No}} <!--96 x DW1227-->
|-
! [[Ebit]] E9+ <ref name="EbitE9+">[http://miner.ebang.com.cn/goods-5.htm Product page] Retrieved 2018-01-22</ref>
| 9,000,000 || 6900 || 6428 || 1300 || 1400 || {{Yes}} || Ethernet || {{No}} <!--132 x DW1227-->
|-
! [[Ebit]] E9++ <ref name="EbitE9++">[http://news.8btc.com/ebang-releasee10-miner-with-samsung-10nm-chips Anouncement] Retrieved 2018-01-22</ref>
| 14,000,000 || 10500 || 3600 || 1330 || 3880 || {{Yes}} || Ethernet || {{No}} <!--48 x DW1228-->
|-
! [[Ebit]] E10 <ref name="EbitE10">[http://miner.ebang.com.cn/goods-2.htm Product page] Retrieved 2018-01-22</ref>
| 18,000,000 || 11100 || 3440 || 1620 || 5230 || {{Yes}} || Ethernet || {{No}} <!--70 x DW1228-->
|-
! HashBuster Micro
| 20,000 || 869 || 29 || 23 || 688 || {{No|Discontinued}} || USB || {{Yes|docs, samples}}
|-
! HashBuster Nano
| {{Patch|}} || {{Patch|}} || {{Patch|}} || {{Patch|}} || {{Patch|}} || {{No|Discontinued}} || USB || {{Yes|docs, samples}}
|-
! [[HashCoins]] Apollo v3
| 1100,000<ref name="HCA">[https://www.hashcoins.com/buy-asic-miners/buy-apollo/ "HashCoins Apollo v3"]. HashCoins.</ref> || xxxx || {{Patch|}} || 1000<ref name="HCA"/> || 599<ref name="HCA"/> || {{No|Discontinued}} || USB || {{No}}
|-
! [[HashCoins]] Zeus v3
| 4,500,000<ref name="HCZ">[https://www.hashcoins.com/buy-asic-miners/buy-zeus/ "HashCoins Zeus v3"]. HashCoins.</ref> || xxxx || {{Patch|}} || 3000<ref name="HCZ"/> || 2299<ref name="HCZ"/> || {{No|Discontinued}} || USB || {{No}}
|-
! HashFast Baby Jet
| 400,000 || 909 || 71 || 440 || 5600 || {{No|Discontinued}} || Ethernet, USB || {{Patch|docs}}
|-
! HashFast Sierra
| 1,200,000 || 909 || 169 || 1320 || 7080 || {{No|Discontinued}} || USB || {{Yes|docs, samples}}
|-
! HashFast Sierra Evo 3
| 2,000,000 || 909 || 294 || 2200 || 6800 || {{No|Discontinued}} || USB || {{Patch|docs}}
|-
! Klondike
| 5,200 || 160 || 260 || 32 || 20 || {{No|Discontinued}} || USB || {{Patch|samples}}
|-
! [[KnCMiner]] Mercury
| 100,000 || {{Patch|}} || 50.04 || 250 || 1995 || {{No|Discontinued}} || Ethernet || {{Yes|code, samples}}
|-
! KnC Saturn 
| 250,000 || 400|| 66 || 300<ref name="nopsu"/> || 2995 || {{No|Discontinued}} || Ethernet || {{Yes|code, samples}}
|-
! KnC Jupiter 
| 500,000 || 400|| 80 || 600<ref name="nopsu"/> || 4995 || {{No|Discontinued}} || Ethernet || {{Yes|code, samples}}
|-
! KnC Neptune <ref name="KnC Neptune">[https://www.kncminer.com/categories/miners "KnC Neptunes 3TH first ever 20nm Chip"] KNC Miner</ref>
| 3,000,000 || 1429 || 231 || 2100 || 12995 <ref name="KnC Neptune">[https://www.kncminer.com/products/neptune "Neptune Online Store"] KnC Miner</ref>|| {{No|Discontinued}} || Ethernet || {{Yes|code, samples}}
|-
! LittleFury
| {{Patch|}} || {{Patch|}} || {{Patch|}} || {{Patch|}} || {{Patch|}} || {{No|Discontinued}} || USB || {{Yes|docs, samples}}
|-
! Metabank
| 120,000 || 705 || 56 || 170 || 2160<ref>Actual costs higher outside Russia</ref> || {{No}} || {{Patch|}} || {{Yes|code, samples}}
|-
! NanoFury / IceFury
| 2,000 || 800 || {{Patch|}} || 2.5 || {{Patch|}} || {{No|Discontinued}} || USB || {{Yes|code, docs, samples}}
|-
! NanoFury NF2
| 3,700 || 740 || 74 || 5 || 50 || {{No|Discontinued}} || USB || {{Yes|code, docs, samples}}
|-
! Red/BlueFury
| 2,600 || 1040 || 4 || 2.5 || 640 || {{No|Discontinued}} || USB || {{Yes|code, samples}}
|-
! ROCKMINER R3-BOX<ref name="rockminer">[http://shop.rockminer.com/ "Rockminer Store"]</ref>
| 450,000 || 1000 || 2250 || 450 || 200<ref name="nopsu"/> || {{No|Discontinued}} || USB || {{Yes|code, samples}}
|-
! ROCKMINER R4-BOX<ref name="rockminer" />
| 470,000 || 1000 || 2238 || 470 || 210<ref name="nopsu"/> || {{No|Discontinued}} || USB || {{Yes|code, samples}}
|-
! ROCKMINER Rocket BOX <ref name="rockminer" />
| 450,000 || 937|| 750 || 480 || 599<ref name="nopsu"/> || {{No|Discontinued}} || RPi GPIO || {{Patch|}}
|-
! ROCKMINER R-BOX<ref name="rockminer" />
| 32,000 || 711 || 500 || 45 || 65<ref name="nopsu"/> || {{No|Discontinued}} || USB || {{Yes|code, samples}}
|-
! ROCKMINER R-BOX 110G<ref name="rockminer" />
| 110,000 || 917 || 1250 || 120 || 88<ref name="nopsu"/> || {{No|Discontinued}} || USB || {{Yes|code, samples}}
|-
! ROCKMINER T1 800G<ref name="rockminer" />
| 800,000 || 800 || 2462 || 1000 || 325<ref name="nopsu"/> || {{No|Discontinued}} || USB || {{Yes|code, samples}}
|-
! Spondooliestech SP10 Dawson<ref name="SP10">[http://www.spondoolies-tech.com/products/sp10-dawson-mid-june-batch "SP10 Dawson June Batch"].</ref>
| 1,400,000 || 1120 || 492 || 1250 || 2845 || {{No|Discontinued}} || Ethernet || {{Yes|code, samples}}
|-
! Spondooliestech SP20 Jackson<ref name="SP20">[http://www.spondoolies-tech.com/products/holiday-special-sp20-jackson-shipping-from-stock "SP20 Jackson"]  Retrieved 2015-02-06</ref>
| 1,700,000 || 1545 || 1299 || 1100 || 1309<ref name="nopsu"/> || {{No|Discontinued}}  || Ethernet || {{Yes|code, samples}}
|-
! Spondooliestech SP30 Yukon<ref name="SP30 Yukon">[http://www.spondoolies-tech.com/products/sp30-yukon-september-batch-1 "SP30 Yukon September Batch 1"].</ref>
| 4,500,000 || 1500 || 1068 || 3000 || 4121 || {{No|Discontinued}} || Ethernet || {{Yes|code, samples}}
|-
! Spondooliestech SP31 Yukon<ref name="SP31 Yukon">[http://www.spondoolies-tech.com/products/sp31-yukon-shipping-from-stock "SP31 Yukon"]  Retrieved 2015-02-06</ref>
| 4,900,000 || 1633 || 2361 || 3000 || 2075 || {{No|Discontinued}} || Ethernet || {{Patch|code}}
|-
! Spondooliestech SP35 Yukon<ref name="SP35 Yukon">[http://www.spondoolies-tech.com/products/sp35-yukon-power-shipping-from-stock "SP35 Yukon"]  Retrieved 2015-02-06</ref>
| 5,500,000 || 1506 || 2460 || 3650 || 2235 || {{No|Discontinued}} || Ethernet || {{Patch|code}}
|-
! TerraHash Klondike 16 <ref name="Klondike16">[https://terrahash.com/product/4-5-ghsec-module/ "4.5 GH/sec Modular Board (Klondike 16)"].</ref>
| 4,500 || 140 || 18 || 32|| 250 || {{No}} || USB || {{Patch|samples}}
|-
! TerraHash Klondike 64 <ref name="Klondike64">[https://terrahash.com/product/18-ghsec-modular-board/ "18 GH/sec Modular board (Klondike 64)"].</ref>
| 18,000 || 140 || 20 || 127 || 900 || {{No}} || USB || {{Patch|samples}}
|-
! TerraHash DX Mini (full)
| 90,000 || 140 || 15 || 640 || 6000 || {{No}} || USB || {{Patch|}}
|-
! TerraHash DX Large (full)
| 180,000 || 140 || 17.14 || 1,280 || 10500 || {{No}} || USB || {{Patch|}}
|-
! Twinfury
| 4,500 || 1174 || 20 || 3.83 || 216 || {{No|Discontinued}} || USB || {{Yes|code, samples}}
|-
! WhatsMiner M1
| {{Patch|}} || {{Patch|}} || {{Patch|}} || {{Patch|}} || {{Patch|}} || {{No|Discontinued}} || Ethernet || {{Patch|}}
|-
! WhatsMiner M2
| 9,200,000 || {{Patch|}} || {{Patch|}} || 2046 || {{Patch|}} || {{No|Discontinued}} || Ethernet || {{Patch|}}
|-
! WhatsMiner M3
| 11,500,000 || {{Patch|}} || {{Patch|}} || 1785  || {{Patch|}} || {{Yes}} || Ethernet || {{Patch|}}
|-	

|}
<references>
<ref name="AntMinerU1">[https://www.bitmaintech.com/productDetail.htm?pid=000201401071629535717ycyGoWo06FE Ant Miner U1 Product page] Retrieved 2014-03-11</ref>
<ref name="AntMinerU2">[https://www.bitmaintech.com/productDetail.htm?pid=00020140227111546291QgbvQbVr06FB Ant Miner U2+ Product page] Retrieved 2014-03-11</ref>
<ref name="AvalonPowerUsage">http://garzikrants.blogspot.com/2013/02/avalon-miner-power-usage.html</ref>
<ref name="avalon">[http://avalon-asics.com/ "Avalon ASIC"]. Avalon. Retrieved January 30, 2013.</ref>
</references>

== FPGA ==

{| class="wikitable sortable" style="text-align:center"
|-
! Product !! Hash rate<br />[Mhash/s] !! Efficiency<br />[Mhash/J] !! Efficiency<br />[Mhash/s/$] !! Power<br />[W] !! Price<br />[$]
|-
! Avnet Spartan-6 LX150T Development Kit
| 100<ref>Fpgaminer (May 19, 2011). [https://bitcointalk.org/index.php?topic=9047.0 "Official Open Source FPGA Bitcoin Miner"]. Bitcointalk.org. Retrieved February 7, 2013.</ref> ||  || 0.10 ||  || 995<ref>[http://avnetexpress.avnet.com/store/em/EMController?action=products&catalogId=500201&storeId=500201&N=0&langId=-1&slnk=b&term=AES-S6DEV-LX150T-G&hrf=http%3A%2F%2Fwww.em.avnet.com%2Fen-us%2Fdesign%2Fdrc%2FPages%2FXilinx-Spartan-6-FPGA-LX150T-Development-Kit.aspx&intcmp=EMA-BUY-AES-S6DEV-LX150T-G "AES-S6DEV-LX150T-G Parts"]. Avnet Express. Retrieved February 7, 2013.</ref>
|-
! Bitcoin Dominator X5000
| 100<ref name="bd" /> || 14.7 || 0.22 || 6.8<ref name="bd" /> || 440<ref name="bd">NewMeat1 (August 18, 2011). [https://bitcointalk.org/index.php?topic=37904.0 "Custom FPGA Board for Sale!"]. Bitcointalk.org. Retrieved January 30, 2013.</ref>
|-
! BitForce SHA256 Single
| 832<ref name="single">[http://www.butterflylabs.com/product-details/ "BitForce SHA256 Single – Technical Specifications"]. Butterfly Labs. Retrieved January 30, 2013.</ref> || 10.4 || 1.38 || 80<ref name="single" /> || 599<ref name="single" />
|-
! Butterflylabs Mini Rig
| 25,200<ref name="mini">[http://web.archive.org/web/20120514032732/http://www.butterflylabs.com/products "Products"]. Butterfly Labs. Archived from the original on May 14, 2012. Retrieved February 7, 2013.</ref> || 20.16 || 1.64 || 1,250<ref name="mini" /> || 15,295<ref name="mini2">[http://www.butterflylabs.com/order-form-bitforce-sha256-mini-rig/ "Order Form – BitForce SHA256 – Mini Rig"]. Butterfly Labs. Retrieved January 30, 2013.</ref>
|-
! Digilent Nexys 2 500K
| 5<ref>The Seven (June 3, 2011). [https://bitcointalk.org/index.php?topic=9047.msg164438#msg164438 "Re: Official Open Source FPGA Bitcoin Miner (Smaller Devices Now Supported!)"]. Bitcointalk.org. Retrieved February 7, 2013.</ref> ||  || 0.03 ||  || 149<ref name="dig">[http://www.digilentinc.com/Products/Detail.cfm?Prod=NEXYS2 "Nexys™2 Spartan-3E FPGA Board"]. Digilent. Retrieved January 30, 2013.</ref>
|-
! Icarus
| 380<ref name="ica">Nzghang (November 9, 2011). [https://bitcointalk.org/index.php?topic=51371.0 "FPGA development board 'Icarus' – DisContinued/ important announcement"]. Bitcointalk.org. Retrieved January 30, 2013.</ref> || 19.79 || 0.66 || 19.2<ref name="ica" /> || 569<ref name="ica" />
|-
! KnCMiner Mars
| 6,000 || ??? || 2.15 || ??? || 2,795
|-
! Lancelot<ref name="lan">Nzghang (May 6, 2012). [https://bitcointalk.org/index.php?topic=79835.0 "FPGA development board "Lancelot" - accept bitsteam developer's orders."]. Bitcointalk.org. Retrieved January 30, 2013.</ref>
| 400<ref name="lan1">Black Arrow (Jun 11, 2013). [https://www.cardreaderfactory.com/shop/lancelot.html "Lancelot - Heavy Duty Dual Spartan6 Bitcoin Mining Device"]. cardreaderfactory.com. Retrieved Jun 11, 2013.</ref> || ||  || 26 || 350<ref name="lan1">Black Arrow (Jun 11, 2013). [https://www.cardreaderfactory.com/shop/lancelot.html "Lancelot - Heavy Duty Dual Spartan6 Bitcoin Mining Device"]. cardreaderfactory.com. Retrieved Jun 11, 2013.</ref>
|-
! ModMiner Quad 
| 800<ref name="mmq">[http://www.btcfpga.com/index.php?route=product/product&product_id=50 "ModMiner Quad"]. BTCFPGA. Retrieved January 30, 2013.</ref> || 20 || 0.75 || 40<ref name="mmq" /> || 1,069<ref name="mmq" />
|-
! Terasic DE2-115
| 80<ref>Fpgaminer (May 4, 2011). [https://bitcointalk.org/index.php?topic=5379.msg105544#msg105544 "Re: FPGA mining"]. Bitcointalk.org. Retrieved February 7, 2013.</ref> ||  || 0.13 ||  || 595<ref name="de2">[http://www.terasic.com.tw/cgi-bin/page/archive.pl?No=502 "Altera DE2-115 Development and Education Board"]. Terasic. Retrieved January 30, 2013.</ref>
|-
! X6500 FPGA Miner 
| 400<ref name="x6500data" /> || 23.25 || 0.72 || 17.2<ref name="x6500data">[http://fpgamining.com/documentation/hardware/power-measurements.html "FPGA Mining Power Measurements"]. FPGA Mining Power Measurements.</ref> || 550<ref name="x65">[http://store.fpgamining.com/ "FPGA Mining Store"]. FPGA Mining. Retrieved January 30, 2013.</ref>
|-
! ZTEX USB-FPGA Module 1.15b
| 90<ref name="miner" /> || || 0.27 ||  || 325<ref>http://shop.ztex.de/product_info.php?cPath=21&products_id=62</ref>
|-
! ZTEX USB-FPGA Module 1.15x
| 215<ref name="miner" /> || || 0.52 ||  || 406<ref>http://shop.ztex.de/product_info.php?cPath=21&products_id=66</ref>
|-
! ZTEX USB-FPGA Module 1.15y
| 860<ref name="miner">http://www.ztex.de/btcminer/</ref> || || 0.65 || || 1,304<ref name="1.15y">http://shop.ztex.de/product_info.php?cPath=21&products_id=74</ref>
|}
<references/>

* [https://www.weusecoins.com/en/mining-guide/ Getting Started With Bitcoin Mining]
* [https://www.bitcoinmining.com/ Bitcoin Mining]
* [https://www.bitcoinmining.com/bitcoin-mining-hardware/ Bitcoin mining hardware]
* [https://www.hobbymining.com/mining-hardware/ Guide on Bitcoin mining hardware]
* [https://99bitcoins.com/best-bitcoin-miners-2016-hardware-reviews/ Bitcoin mining hardware comparison for 2016]