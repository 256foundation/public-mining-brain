# bitaxeorg/ESP-Miner issue #119: Bitaxe Ultra 1366 No mining

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/119
> Collected: 2026-10-07
> Published: 2024-02-28

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 119
- State: closed
- Author: FragOmatig
- Opened: 2024-02-28
- Closed: 2024-03-05
- Labels: none

## Description

hey folks,

my bitaxe wont mining.
i try new power supply, Web flash wantclue, in GUI new download and flash esp-miner.bin and www.bin.
with webflash the firmware are rest, must Wlan new connected und co.  
In GUI only Show "Working" then nothing.
ASIC Dead? i have no ideas more. 
 

## Comments

### FragOmatig on 2024-02-28

₿ (1820767) http_server: Handshake done, the new connection was opened
₿ (1823447) stratum_task: rx: {"id":null,"method":"mining.notify","params":["e8339f","667aae154bd645011e041b56ecd1a80cde9c78840000cf840000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703c5b30c5075626c69632d506f6f6c","ffffffff021ac56228000000001976a91462e907b15cbf27d5425399ebf6f0fb50ebb88f1888ac0000000000000000266a24aa21a9ed0c989e26603d4d003f7365a7c1fc8afe716cc826719b4ee13f006d6b03fa436900000000",["d08613596e1120e7eaa4dbe5e241190d3aa25c822cacb522515c567e5a7f2705","222dc94c5201fbe17ca0ffdcf126fc729fb8a1a353552b51cb4fed92adb1f269","18e011a00cccdc34f94c912ce35e80728dc937b73b8e45b70d41a2688f7b0be4","bcf5fa579842e8bf12efd1b20ffb558136b460a68fd60e76a62d7285b8a624df","b4b68b951918dd6ce3b00d8a78a6657feb1000f73bf716c66153f8677b3c86c6","857d7c177a0c778be5c4a3a203b65a0893c5ac33dc735e4787363ed65928d8d4","d8b77234c4861d70eae85a8d066092d0c580fdeb86bcaae9289a558beffc876b","175ef15b1af6deb086281c9110a89ebd8149f087cad84cc026031e99387d533a","01da0dc20d77075283354243f3dc1b3c63324c19ea348a954968c58fadca56a5","5241c8f7db51e676d2a87824859759324a4dcd4422193263981879901f90a114","4a10283bc9c0e9620f33e2b0954726c1311e2f4d47f2e84d38d40480406940e0","bed5bbd2b163adc3035fc0e6f3407de0dd4ae2b22e0f0a9aa35378075155c7c9"],"20000000","170371b1","65dfab84",false]}
₿ (1825557) create_jobs_task: New Work Dequeued e8339f
₿ (1883557) stratum_task: rx: {"id":null,"method":"mining.notify","params":["e837d0","667aae154bd645011e041b56ecd1a80cde9c78840000cf840000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703c5b30c5075626c69632d506f6f6c","ffffffff021ac56228000000001976a91462e907b15cbf27d5425399ebf6f0fb50ebb88f1888ac0000000000000000266a24aa21a9ed0c989e26603d4d003f7365a7c1fc8afe716cc826719b4ee13f006d6b03fa436900000000",["d08613596e1120e7eaa4dbe5e241190d3aa25c822cacb522515c567e5a7f2705","222dc94c5201fbe17ca0ffdcf126fc729fb8a1a353552b51cb4fed92adb1f269","18e011a00cccdc34f94c912ce35e80728dc937b73b8e45b70d41a2688f7b0be4","bcf5fa579842e8bf12efd1b20ffb558136b460a68fd60e76a62d7285b8a624df","b4b68b951918dd6ce3b00d8a78a6657feb1000f73bf716c66153f8677b3c86c6","857d7c177a0c778be5c4a3a203b65a0893c5ac33dc735e4787363ed65928d8d4","d8b77234c4861d70eae85a8d066092d0c580fdeb86bcaae9289a558beffc876b","175ef15b1af6deb086281c9110a89ebd8149f087cad84cc026031e99387d533a","01da0dc20d77075283354243f3dc1b3c63324c19ea348a954968c58fadca56a5","5241c8f7db51e676d2a87824859759324a4dcd4422193263981879901f90a114","4a10283bc9c0e9620f33e2b0954726c1311e2f4d47f2e84d38d40480406940e0","bed5bbd2b163adc3035fc0e6f3407de0dd4ae2b22e0f0a9aa35378075155c7c9"],"20000000","170371b1","65dfabc0",false]}
₿ (1885197) create_jobs_task: New Work Dequeued e837d0
₿ (1902397) stratum_task: rx: {"id":null,"method":"mining.notify","params":["e83bef","2cfdde02d985440df61fd5d66578c8d87f3201a2000031740000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703c6b30c5075626c69632d506f6f6c","ffffffff02775a3f28000000001976a91462e907b15cbf27d5425399ebf6f0fb50ebb88f1888ac0000000000000000266a24aa21a9ede473866caffa089dcfd3004b1df5e8e25c37240d11de11c3ed1aaf3fac48d7a100000000",["6d2192f587275010c5a39f029fa250589b55b24d683548178c2ce4396ba03874","c3e20a4176c0625fc55dd58d7df23f4a9800b5b8ec41cdc2015481cea6dce2dc","7006ffe73bd5defc9ec090269c045eaa8dc538f0e4ec1d8ad7ea6ddaf86f7357","2840ac0c8a8c90b7c9a202747e785efc7246509df5a80e4ee0af50512bb6e406","c00e531b3720bdbf69a360f4a2d848b63b6e1d3bf310a34a0748ef9deca2f736","676c9f5e4a3c833a771956452b0f17dbf96e7943fced52906931a695434278ef","3156d55402043a1958de0628f6de5df8891ecba16b7f79314767ba73d2662722","ace0f50af8ada7de9c334cab3274a0317032c057031811ce5d86ba09b0db27bb","75ae8ded42ef87984291c6f9615d9a21c7d13a7bd1ff1c4b7cb0d6499060ef56","66e167da4748abc1f54b15b0c2d32b78232dc0de2ca7caf2cf61913f30f3e205","0b6df7a81c2a549bad15e267cdfaf1210fe490719e45e181000b8c6b4b155053","67c4d35f9ce48cb293d1c9872e33b7f65cbed0dc4f96f2da69735f18f61b40df"],"20000000","170371b1","65dfabd1",true]}
₿ (1902507) stratum_task: abandoning work
₿ (1902507) create_jobs_task: New Work Dequeued e83bef
₿ (2003567) stratum_task: rx: {"id":null,"method":"mining.notify","params":["e8402f","2cfdde02d985440df61fd5d66578c8d87f3201a2000031740000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703c6b30c5075626c69632d506f6f6c","ffffffff02775a3f28000000001976a91462e907b15cbf27d5425399ebf6f0fb50ebb88f1888ac0000000000000000266a24aa21a9ede473866caffa089dcfd3004b1df5e8e25c37240d11de11c3ed1aaf3fac48d7a100000000",["6d2192f587275010c5a39f029fa250589b55b24d683548178c2ce4396ba03874","c3e20a4176c0625fc55dd58d7df23f4a9800b5b8ec41cdc2015481cea6dce2dc","7006ffe73bd5defc9ec090269c045eaa8dc538f0e4ec1d8ad7ea6ddaf86f7357","2840ac0c8a8c90b7c9a202747e785efc7246509df5a80e4ee0af50512bb6e406","c00e531b3720bdbf69a360f4a2d848b63b6e1d3bf310a34a0748ef9deca2f736","676c9f5e4a3c833a771956452b0f17dbf96e7943fced52906931a695434278ef","3156d55402043a1958de0628f6de5df8891ecba16b7f79314767ba73d2662722","ace0f50af8ada7de9c334cab3274a0317032c057031811ce5d86ba09b0db27bb","75ae8ded42ef87984291c6f9615d9a21c7d13a7bd1ff1c4b7cb0d6499060ef56","66e167da4748abc1f54b15b0c2d32b78232dc0de2ca7caf2cf61913f30f3e205","0b6df7a81c2a549bad15e267cdfaf1210fe490719e45e181000b8c6b4b155053","67c4d35f9ce48cb293d1c9872e33b7f65cbed0dc4f96f2da69735f18f61b40df"],"20000000","170371b1","65dfac38",false]}
₿ (2004477) create_jobs_task: New Work Dequeued e8402f

### FragOmatig on 2024-02-28

![IMG_3007](https://github.com/skot/ESP-Miner/assets/161623595/94818774-6b61-4441-8dc3-27ca0c3d6916)


### FragOmatig on 2024-02-28

![IMG_3008](https://github.com/skot/ESP-Miner/assets/161623595/e53df4de-6610-4243-b29f-eb18d36596a8)


### FragOmatig on 2024-02-28

![IMG_3009](https://github.com/skot/ESP-Miner/assets/161623595/c4d90805-2dd2-4360-9a3a-80a2f9410c58)


### FragOmatig on 2024-02-28

web flash logs are clear, only in Gui logs

Frequenz and Voltage are stock 485/1200

### FragOmatig on 2024-02-28

ESP update 204 - v2.0.7 Update Failed: Not Enough Space

### MyOwn2C on 2024-02-29

You have a 3-wire fan, yet fan speed is zero.
If it cannot detect your fan, perhaps it is preventing it from mining. 

### skot on 2024-02-29

I think the issue is that your board version is set to 204, but you don't actually have a 204. It's something earlier.

Let me look into how to fix this and get back to you.

### FragOmatig on 2024-02-29

@skot 

Thats my men 🤗 i have no idea whats going on to fix it. 


### xXAsystolieXx on 2024-02-29

@FragOmatig maybe contact the Support from d-central? They should know which board version they sold you

### xXAsystolieXx on 2024-02-29

@FragOmatig Have you ever tried the board version 0.11 when flashing?

### FragOmatig on 2024-02-29

@xXAsystolieXx 

I try to contact the support 👍

nope, i have only update @ web GUI. 
i must google how worx bitaxetool 🫣

Sorry for bad english, iam German 😜

### xXAsystolieXx on 2024-02-29

🤣 dann sag das doch 😜

### xXAsystolieXx on 2024-02-29

@FragOmatig 

### skot on 2024-02-29

This might be a job for @WantClue ! Basically all the German I know I learned from him in the last couple days 😅

### FragOmatig on 2024-02-29

He he genial, warum hände und Füße, wenn es Deutsch gibt😂 

@skot nicht das gelbe vom Ei 😝

Yes back to topic guys 😁  board version where find it? 

### xXAsystolieXx on 2024-02-29

> He he genial, warum hände und Füße, wenn es Deutsch gibt😂
> 
> @skot nicht das gelbe vom Ei 😝
> 
> Yes back to topic guys 😁 board version where find it?

Ja man 🤣 wenn du Hilfe brauchst beim bitaxetool, kann ich gerne versuchen dir zu helfen

### WantClue on 2024-02-29

usually the board version these days no longer means anything to the code basis we have. It should work no matter what board version you flash to your bitaxe. The web flasher I wrote only pushes the 204 version (the most recent one, currently) to it. I'm on a fix on it.

Can you please also provide us a high quality picture of the ASIC? Just so that we verify the soldering but it should be fine...

But I need to admit this is some early version of the bitaxe ultra so we would need to investigate the versioning more. 

Did you already tried to reach out to D-Central cause it appears that they produced it?

### FragOmatig on 2024-02-29

@xXAsystolieXx 

moment der meister hat ne idee. Erstmal abwarten was wantclue hat. Dann wird ubuntu gebootet 👌🏻
@WantClue its a BM1366AL iam looking for the picture. Nope, i try friday after work to write a email to d-centrale



### FragOmatig on 2024-02-29

![IMG_2897](https://github.com/skot/ESP-Miner/assets/161623595/08e0cd1c-f7f2-4ffb-9c1e-63f64edcfcd3)


### FragOmatig on 2024-02-29

The grey mist are thermal compund

### WantClue on 2024-03-01

This seems to be a soldering issue. Had another viewer of mine send me one for repair. After resoldering it works again. 
I'll close this issue in three days unless someone wants to extend this issue.

### FragOmatig on 2024-03-01

How much it cost the resoldering?
