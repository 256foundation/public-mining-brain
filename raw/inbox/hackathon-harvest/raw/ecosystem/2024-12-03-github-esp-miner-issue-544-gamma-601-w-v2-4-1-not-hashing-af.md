# bitaxeorg/ESP-Miner issue #544: Gamma 601 w/ v2.4.1 - Not hashing after warm boot

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/544
> Collected: 2026-10-07
> Published: 2024-12-03

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 544
- State: closed
- Author: MyOwn2C
- Opened: 2024-12-03
- Closed: 2025-10-21
- Labels: none

## Description

**Describe the bug**
Gamma 601 w/ v2.4.1 cannot start hashing after warm boot (just pressing restart, with power still on)
Sometimes it can hash again after cold boot (power off, then power on again)

**To Reproduce**
Steps to reproduce the behavior:
1. Set clock + freq (625 / 1200 used)
2. Press Restart
3. Hashing does not start. Power is stuck at 5W. See below log.

**Expected behavior**
Hashing should start after rebooting

**Hardware (please complete the following information):**
 - Bitaxe HW version: 6.1
 - Bitaxe HW vendor: D Central
 - ESP-Miner FW version: 2.4.1
 - Hash Frequency: 625
 - Voltage: 1200
 - Pool URL, Port, User: ch.viabtc.com:3333

**Symptom**
Hashing cannot start. See below log.

AxeOS
Overview
Model:	BM1370
Uptime:	38 seconds
WiFi Status:	Connected!
MAC Address:	F0:9E:9E:0D:21:98
Free Heap Memory:	142532
Version:	v2.4.1
Board Version:	601
Realtime Logs 
₿ (10042) bm1370Module: Setting Frequency to 312.50MHz (312.50)
₿ (10142) bm1370Module: Setting Frequency to 318.75MHz (318.75)
₿ (10242) bm1370Module: Setting Frequency to 325.00MHz (325.00)
₿ (10342) bm1370Module: Setting Frequency to 331.25MHz (331.25)
₿ (10442) bm1370Module: Setting Frequency to 337.50MHz (337.50)
₿ (10542) bm1370Module: Setting Frequency to 343.75MHz (343.75)
₿ (10642) bm1370Module: Setting Frequency to 350.00MHz (350.00)
₿ (10742) bm1370Module: Setting Frequency to 356.25MHz (356.25)
₿ (10842) bm1370Module: Setting Frequency to 362.50MHz (362.50)
₿ (10942) bm1370Module: Setting Frequency to 368.75MHz (368.75)
₿ (11042) bm1370Module: Setting Frequency to 375.00MHz (375.00)
₿ (11142) bm1370Module: Setting Frequency to 381.25MHz (381.25)
₿ (11242) bm1370Module: Setting Frequency to 387.50MHz (387.50)
₿ (11342) bm1370Module: Setting Frequency to 393.75MHz (393.75)
₿ (11442) bm1370Module: Setting Frequency to 400.00MHz (400.00)
₿ (11542) bm1370Module: Setting Frequency to 406.25MHz (406.25)
₿ (11642) bm1370Module: Setting Frequency to 412.50MHz (412.50)
₿ (11742) bm1370Module: Setting Frequency to 418.75MHz (418.75)
₿ (11842) bm1370Module: Setting Frequency to 425.00MHz (425.00)
₿ (11942) bm1370Module: Setting Frequency to 431.25MHz (431.25)
₿ (12042) bm1370Module: Setting Frequency to 437.50MHz (437.50)
₿ (12142) bm1370Module: Setting Frequency to 443.75MHz (443.75)
₿ (12242) bm1370Module: Setting Frequency to 450.00MHz (450.00)
₿ (12342) bm1370Module: Setting Frequency to 456.25MHz (456.25)
₿ (12442) bm1370Module: Setting Frequency to 462.50MHz (462.50)
₿ (12542) bm1370Module: Setting Frequency to 468.75MHz (468.75)
₿ (12642) bm1370Module: Setting Frequency to 475.00MHz (475.00)
₿ (12742) bm1370Module: Setting Frequency to 481.25MHz (481.25)
₿ (12842) bm1370Module: Setting Frequency to 487.50MHz (487.50)
₿ (12942) bm1370Module: Setting Frequency to 493.75MHz (493.75)
₿ (13042) bm1370Module: Setting Frequency to 500.00MHz (500.00)
₿ (13142) bm1370Module: Setting Frequency to 506.25MHz (506.25)
₿ (13242) bm1370Module: Setting Frequency to 512.50MHz (512.50)
₿ (13342) bm1370Module: Setting Frequency to 518.75MHz (518.75)
₿ (13442) bm1370Module: Setting Frequency to 525.00MHz (525.00)
₿ (13542) bm1370Module: Setting Frequency to 531.25MHz (531.25)
₿ (13642) bm1370Module: Setting Frequency to 537.50MHz (537.50)
₿ (13742) bm1370Module: Setting Frequency to 543.75MHz (543.75)
₿ (13842) bm1370Module: Setting Frequency to 550.00MHz (550.00)
₿ (13942) bm1370Module: Setting Frequency to 556.25MHz (556.25)
₿ (14042) bm1370Module: Setting Frequency to 562.50MHz (562.50)
₿ (14142) bm1370Module: Setting Frequency to 568.75MHz (568.75)
₿ (14242) bm1370Module: Setting Frequency to 575.00MHz (575.00)
₿ (14342) bm1370Module: Setting Frequency to 581.25MHz (581.25)
₿ (14442) bm1370Module: Setting Frequency to 587.50MHz (587.50)
₿ (14542) bm1370Module: Setting Frequency to 593.75MHz (593.75)
₿ (14642) bm1370Module: Setting Frequency to 600.00MHz (600.00)
₿ (14742) bm1370Module: Setting Frequency to 606.25MHz (606.25)
₿ (14842) bm1370Module: Setting Frequency to 612.50MHz (612.50)
₿ (14942) bm1370Module: Setting Frequency to 618.75MHz (618.75)
₿ (15042) bm1370Module: Setting Frequency to 625.00MHz (625.00)
₿ (15142) bm1370Module: Setting max baud of 1000000
₿ (15142) serial: Changing UART baud to 1000000
₿ (15142) ASIC_task: ASIC Job Interval: 500.00 ms
₿ (15142) stratum_task: Starting heartbeat thread for primary endpoint: bch.viabtc.io
₿ (15142) stratum_task: Trying to get IP for URL: bch.viabtc.io
₿ (15162) ASIC_task: ASIC Ready!
₿ (15152) main_task: Returned from app_main()
₿ (15172) stratum_task: Connecting to: stratum+tcp://bch.viabtc.io:3333 (172.65.47.162)
₿ (15182) stratum_task: Socket created, connecting to 172.65.47.162:3333
₿ (15192) stratum_api: Resetting stratum uid
₿ (15192) stratum_task: Clean Jobs: clearing queue
₿ (15202) stratum_api: tx: {"id": 1, "method": "mining.configure", "params": [["version-rolling"], {"version-rolling.mask": "ffffffff"}]}
₿ (15212) stratum_api: tx: {"id": 2, "method": "mining.subscribe", "params": ["bitaxe/BM1370/v2.4.1"]}
₿ (15222) stratum_api: tx: {"id": 3, "method": "mining.authorize", "params": ["s10sia.Gamma1", "123"]}
₿ (15232) stratum_api: tx: {"id": 4, "method": "mining.suggest_difficulty", "params": [1000]}
₿ (15252) stratum_task: rx: {"id": 1, "result": {"version-rolling": true, "version-rolling.mask": "1fffe000"}, "error": null}
₿ (15252) stratum_api: Set version mask: 1fffe000
₿ (15262) stratum_task: Set version mask: 1fffe000
₿ (15262) stratum_task: rx: {"id": null, "method": "mining.set_version_mask", "params": ["1fffe000"], "error": null}
₿ (15282) stratum_task: Set version mask: 1fffe000
₿ (15282) stratum_task: rx: {"id": 2, "result": [[["mining.set_difficulty", "171bd4e409b3410a"], ["mining.notify", "171bd4e409b3410a"]], "29d41bde", 4], "error": null}
₿ (15302) stratum_api: extranonce_str: 29d41bde
₿ (15302) stratum_api: extranonce_2_len: 4
₿ (15312) stratum_task: rx: {"id": 3, "result": true, "error": null}
₿ (15312) stratum_task: setup message accepted
₿ (15322) stratum_task: rx: {"id": null, "method": "mining.set_difficulty", "params": [4096]}
₿ (15332) stratum_task: Set stratum difficulty: 4096
₿ (15342) stratum_task: rx: {"id": null, "method": "mining.notify", "params": ["c28c", "a7e1a86329a8438e078458a0bf4f9a0b74c6699e011aa88d0000000000000000", "01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff6003c7590d1d2f5669614254432f4243484e2f4d696e6564206279207331307369612f2cfabe6d6d35057a90da59772bf2194dd669ee200cf51aeeb9aa67370b21456dd7ab12cc5d1000000000000000108cc2800c484ee0c5", "ffffffff02a6f6a112000000001976a914f1c075a01882ae0972f95d3a4177c86c852b7d9188ac00000000000000002b6a2952534b424c4f434b3a4102ff19057784762fef1c23aa2b0b7fd172727fd4d26ac04c20430d006a70c500000000", ["7aca8f6e9672b28cd57ef7f5d39df3568a107726b11168643734b061bd151d00", "b22d7125c92fcd79115167ec22fa5d6185314c64e78be0ab4b7ff65219ea8b7f", "f5eaf2f8e931b8d45fbaf200fccb8a45d5385771eccf651de32bd31bdbf8c656", "3e6e664324b79feaac63ef579026ba2811caada103dc693ee25817de9744cdc8", "1b5064bf857a062e8285c74442deb7a5a715d17b53b17245cc5215ac5a907208"], "20000000", "1801f25d", "674e9224", true]}
₿ (15422) SystemModule: Syncing clock
₿ (15432) stratum_task: rx: {"id": 4, "error": null, "result": true}
₿ (15432) create_jobs_task: Set chip version rolls 65535
₿ (15442) stratum_task: setup message accepted
₿ (15452) stratum_task: rx: {"id": null, "method": "mining.set_difficulty", "params": [1000]}
₿ (15452) create_jobs_task: New Work Dequeued c28c
₿ (15462) stratum_task: Set stratum difficulty: 1000
₿ (15462) ASIC_task: New pool difficulty 4096
₿ (15462) create_jobs_task: Job processed and queued: c28c
₿ (35812) stratum_task: rx: {"id": null, "method": "mining.notify", "params": ["c28d", "a7e1a86329a8438e078458a0bf4f9a0b74c6699e011aa88d0000000000000000", "01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff6003c7590d1d2f5669614254432f4243484e2f4d696e6564206279207331307369612f2cfabe6d6d35057a90da59772bf2194dd669ee200cf51aeeb9aa67370b21456dd7ab12cc5d1000000000000000108dc2800c484ee0c5", "ffffffff0240faa112000000001976a914f1c075a01882ae0972f95d3a4177c86c852b7d9188ac00000000000000002b6a2952534b424c4f434b3ac62e9abf4156a33f67a1932544820383d7ba61e3d4d26ac04c20430f006a70c600000000", ["7aca8f6e9672b28cd57ef7f5d39df3568a107726b11168643734b061bd151d00", "b22d7125c92fcd79115167ec22fa5d6185314c64e78be0ab4b7ff65219ea8b7f", "f5eaf2f8e931b8d45fbaf200fccb8a45d5385771eccf651de32bd31bdbf8c656", "fd54004c042f7df3de1b77e1f1127de25b31c3f9b8a8c31203e6561acd3b7a29", "87af2fb9418b673923ea9be28013df84dce436f196099d52cd6afc59183f4514", "b3c0dab58f451382496440bd2196390d618be00b05adeb72243fdea3179e9671"], "20000000", "1801f25d", "674e9242", false]}
₿ (35992) create_jobs_task: New Work Dequeued c28d
₿ (35992) create_jobs_task: Job processed and queued: c28d


## Comments

### MyOwn2C on 2024-12-03

Here is the log when it hash after cold boot for reference. 
Otherwise same conditions as above. 
Everything here works normally.

AxeOS
Overview
Model:	BM1370
Uptime:	Just now
WiFi Status:	Connected!
MAC Address:	F0:9E:9E:0D:21:98
Free Heap Memory:	140824
Version:	v2.4.1
Board Version:	601
Realtime Logs 
₿ (15518) bm1370Module: Setting Frequency to 318.75MHz (318.75)
₿ (15618) bm1370Module: Setting Frequency to 325.00MHz (325.00)
₿ (15718) bm1370Module: Setting Frequency to 331.25MHz (331.25)
₿ (15818) bm1370Module: Setting Frequency to 337.50MHz (337.50)
₿ (15918) bm1370Module: Setting Frequency to 343.75MHz (343.75)
₿ (16018) bm1370Module: Setting Frequency to 350.00MHz (350.00)
₿ (16118) bm1370Module: Setting Frequency to 356.25MHz (356.25)
₿ (16218) bm1370Module: Setting Frequency to 362.50MHz (362.50)
₿ (16318) bm1370Module: Setting Frequency to 368.75MHz (368.75)
₿ (16418) bm1370Module: Setting Frequency to 375.00MHz (375.00)
₿ (16518) bm1370Module: Setting Frequency to 381.25MHz (381.25)
₿ (16618) bm1370Module: Setting Frequency to 387.50MHz (387.50)
₿ (16718) bm1370Module: Setting Frequency to 393.75MHz (393.75)
₿ (16818) bm1370Module: Setting Frequency to 400.00MHz (400.00)
₿ (16918) bm1370Module: Setting Frequency to 406.25MHz (406.25)
₿ (17018) bm1370Module: Setting Frequency to 412.50MHz (412.50)
₿ (17118) bm1370Module: Setting Frequency to 418.75MHz (418.75)
₿ (17218) bm1370Module: Setting Frequency to 425.00MHz (425.00)
₿ (17318) bm1370Module: Setting Frequency to 431.25MHz (431.25)
₿ (17418) bm1370Module: Setting Frequency to 437.50MHz (437.50)
₿ (17518) bm1370Module: Setting Frequency to 443.75MHz (443.75)
₿ (17618) bm1370Module: Setting Frequency to 450.00MHz (450.00)
₿ (17718) bm1370Module: Setting Frequency to 456.25MHz (456.25)
₿ (17818) bm1370Module: Setting Frequency to 462.50MHz (462.50)
₿ (17918) bm1370Module: Setting Frequency to 468.75MHz (468.75)
₿ (18018) bm1370Module: Setting Frequency to 475.00MHz (475.00)
₿ (18118) bm1370Module: Setting Frequency to 481.25MHz (481.25)
₿ (18218) bm1370Module: Setting Frequency to 487.50MHz (487.50)
₿ (18318) bm1370Module: Setting Frequency to 493.75MHz (493.75)
₿ (18418) bm1370Module: Setting Frequency to 500.00MHz (500.00)
₿ (18518) bm1370Module: Setting Frequency to 506.25MHz (506.25)
₿ (18618) bm1370Module: Setting Frequency to 512.50MHz (512.50)
₿ (18718) bm1370Module: Setting Frequency to 518.75MHz (518.75)
₿ (18818) bm1370Module: Setting Frequency to 525.00MHz (525.00)
₿ (18918) bm1370Module: Setting Frequency to 531.25MHz (531.25)
₿ (19018) bm1370Module: Setting Frequency to 537.50MHz (537.50)
₿ (19118) bm1370Module: Setting Frequency to 543.75MHz (543.75)
₿ (19218) bm1370Module: Setting Frequency to 550.00MHz (550.00)
₿ (19318) bm1370Module: Setting Frequency to 556.25MHz (556.25)
₿ (19418) bm1370Module: Setting Frequency to 562.50MHz (562.50)
₿ (19518) bm1370Module: Setting Frequency to 568.75MHz (568.75)
₿ (19618) bm1370Module: Setting Frequency to 575.00MHz (575.00)
₿ (19718) bm1370Module: Setting Frequency to 581.25MHz (581.25)
₿ (19818) bm1370Module: Setting Frequency to 587.50MHz (587.50)
₿ (19918) bm1370Module: Setting Frequency to 593.75MHz (593.75)
₿ (20018) bm1370Module: Setting Frequency to 600.00MHz (600.00)
₿ (20118) bm1370Module: Setting Frequency to 606.25MHz (606.25)
₿ (20218) bm1370Module: Setting Frequency to 612.50MHz (612.50)
₿ (20318) bm1370Module: Setting Frequency to 618.75MHz (618.75)
₿ (20418) bm1370Module: Setting Frequency to 625.00MHz (625.00)
₿ (20518) bm1370Module: Setting max baud of 1000000
₿ (20518) serial: Changing UART baud to 1000000
₿ (20518) stratum_task: Starting heartbeat thread for primary endpoint: bch.viabtc.io
₿ (20528) ASIC_task: ASIC Job Interval: 500.00 ms
₿ (20518) stratum_task: Trying to get IP for URL: bch.viabtc.io
₿ (20538) ASIC_task: ASIC Ready!
₿ (20528) main_task: Returned from app_main()
₿ (20548) stratum_task: Connecting to: stratum+tcp://bch.viabtc.io:3333 (172.65.47.162)
₿ (20558) stratum_task: Socket created, connecting to 172.65.47.162:3333
₿ (20598) stratum_api: Resetting stratum uid
₿ (20598) stratum_task: Clean Jobs: clearing queue
₿ (20598) stratum_api: tx: {"id": 1, "method": "mining.configure", "params": [["version-rolling"], {"version-rolling.mask": "ffffffff"}]}
₿ (20608) stratum_api: tx: {"id": 2, "method": "mining.subscribe", "params": ["bitaxe/BM1370/v2.4.1"]}
₿ (20618) stratum_api: tx: {"id": 3, "method": "mining.authorize", "params": ["s10sia.Gamma1", "123"]}
₿ (20628) stratum_api: tx: {"id": 4, "method": "mining.suggest_difficulty", "params": [1000]}
₿ (20678) stratum_task: rx: {"id": 1, "result": {"version-rolling": true, "version-rolling.mask": "1fffe000"}, "error": null}
₿ (20678) stratum_api: Set version mask: 1fffe000
₿ (20678) stratum_task: Set version mask: 1fffe000
₿ (20688) stratum_task: rx: {"id": null, "method": "mining.set_version_mask", "params": ["1fffe000"], "error": null}
₿ (20698) stratum_task: Set version mask: 1fffe000
₿ (20708) stratum_task: rx: {"id": 2, "result": [[["mining.set_difficulty", "171bd4e409b34113"], ["mining.notify", "171bd4e409b34113"]], "29d41be7", 4], "error": null}
₿ (20718) stratum_api: extranonce_str: 29d41be7
₿ (20728) stratum_api: extranonce_2_len: 4
₿ (20728) stratum_task: rx: {"id": 3, "result": true, "error": null}
₿ (20738) stratum_task: setup message accepted
₿ (20738) stratum_task: rx: {"id": null, "method": "mining.set_difficulty", "params": [4096]}
₿ (20748) stratum_task: Set stratum difficulty: 4096
₿ (20758) stratum_task: rx: {"id": null, "method": "mining.notify", "params": ["c28f", "3212429ee18910a1698e048cfd4cda1d3bc62b4b014dad470000000000000000", "01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff6003c8590d1d2f5669614254432f4243484e2f4d696e6564206279207331307369612f2cfabe6d6d35057a90da59772bf2194dd669ee200cf51aeeb9aa67370b21456dd7ab12cc5d1000000000000000108fc2800c484ee0c5", "ffffffff02e574a012000000001976a914f1c075a01882ae0972f95d3a4177c86c852b7d9188ac00000000000000002b6a2952534b424c4f434b3a8b9d2a5d96893c2b123413aa22bb580f6343b269d4d26ac04c20430f006a70c600000000", ["4105292d67536aaca088165a0b3c53149bf22c5693706aeb19e9b03039212710", "d63491c8610d5faa9dab5663696e26c7d564119e86d844983bd4016a086129b0", "cd79e9e920ce1214676aa38864bea116aa2a3c94d7208fd121a1f89edbf0ab5b", "3266d18a72f9b0f8072bc869705ac59683679eafeee5ed8dededd3ee97e741a3"], "20000000", "1801f156", "674e9260", true]}
₿ (20838) SystemModule: Syncing clock
₿ (20848) stratum_task: rx: {"id": 4, "error": null, "result": true}
₿ (20848) create_jobs_task: Set chip version rolls 65535
₿ (20848) stratum_task: setup message accepted
₿ (20868) create_jobs_task: New Work Dequeued c28f
₿ (20868) stratum_task: rx: {"id": null, "method": "mining.set_difficulty", "params": [1000]}
₿ (20868) create_jobs_task: Job processed and queued: c28f
₿ (20868) ASIC_task: New pool difficulty 4096
₿ (20878) stratum_task: Set stratum difficulty: 1000
₿ (21688) bm1370Module: Job ID: 30, Core: 116/12, Ver: 03B58000
₿ (21688) asic_result: Ver: 23B58000 Nonce 714103E8 diff 4977.3 of 4096.
₿ (21698) stratum_api: tx: {"id": 5, "method": "mining.submit", "params": ["s10sia.Gamma1", "c28f", "01000000", "674e9260", "714103e8", "03b58000"]}
₿ (21738) stratum_task: rx: {"id": 5, "error": null, "result": true}
₿ (21738) stratum_task: message result accepted
₿ (21768) bm1370Module: Job ID: 30, Core: 1/4, Ver: 04B68000
₿ (21768) asic_result: Ver: 24B68000 Nonce 179F0102 diff 374.9 of 4096.
₿ (24658) bm1370Module: Job ID: 40, Core: 38/14, Ver: 0357C000
₿ (24658) asic_result: Ver: 2357C000 Nonce C816034C diff 275.7 of 4096.
₿ (26408) bm1370Module: Job ID: 20, Core: 54/5, Ver: 0052A000
₿ (26408) asic_result: Ver: 2052A000 Nonce E77D036C diff 1079.4 of 4096.
₿ (26798) bm1370Module: Job ID: 20, Core: 119/6, Ver: 050CC000
₿ (26798) asic_result: Ver: 250CC000 Nonce E36E04EE diff 430.3 of 4096.
₿ (27778) bm1370Module: Job ID: 50, Core: 21/5, Ver: 04C0A000
₿ (27778) asic_result: Ver: 24C0A000 Nonce 85FA012A diff 717.3 of 4096.
₿ (27778) stratum_task: rx: {"id": null, "method": "mining.notify", "params": ["c290", "63928059e456726555fe199bb7e5da5f7d4fad4101d5c1a60000000000000000", "01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff6003c9590d1d2f5669614254432f4243484e2f4d696e6564206279207331307369612f2cfabe6d6d35057a90da59772bf2194dd669ee200cf51aeeb9aa67370b21456dd7ab12cc5d10000000000000001090c2800c484ee0c5", "ffffffff02847ca012000000001976a914f1c075a01882ae0972f95d3a4177c86c852b7d9188ac00000000000000002b6a2952534b424c4f434b3a702aaceebc8a00a865b0d1ab22260fbb3749bb2cd4d26ac04c20430e006a70c700000000", ["39ff360beb012cd67fdb820d75ee27240925cb0b28e2e4cab8e88c9a59da5008", "47d14d1b2f66e6f88c43292a9ee2da5d6ab2c7e95494402890ffbea8a70b22c1", "62c767849ae7796aa3e6730bf9179d051f11afb9e609204467fc60a6e98f9588"], "20000000", "1801f037", "674e9272", true]}
₿ (27858) stratum_task: Clean Jobs: clearing queue
₿ (27898) create_jobs_task: New Work Dequeued c290
₿ (27898) ASIC_task: New pool difficulty 1000
₿ (27898) create_jobs_task: Job processed and queued: c290
₿ (28248) bm1370Module: Job ID: 00, Core: 77/10, Ver: 04374000
₿ (28248) asic_result: Ver: 24374000 Nonce EB18049A diff 5331.9 of 1000.
₿ (28248) stratum_api: tx: {"id": 6, "method": "mining.submit", "params": ["s10sia.Gamma1", "c290", "18000000", "674e9272", "eb18049a", "04374000"]}
₿ (28318) stratum_task: rx: {"id": 6, "error": null, "result": true}
₿ (28328) stratum_task: message result accepted
₿ (28478) bm1370Module: Job ID: 18, Core: 35/3, Ver: 01086000
₿ (28478) asic_result: Ver: 21086000 Nonce AF510246 diff 266.1 of 1000.
₿ (28598) bm1370Module: Job ID: 18, Core: 44/4, Ver: 02788000
₿ (28598) asic_result: Ver: 22788000 Nonce 28140658 diff 297.7 of 1000.
₿ (29138) bm1370Module: Job ID: 30, Core: 35/8, Ver: 02EB0000
₿ (29138) asic_result: Ver: 22EB0000 Nonce 8DED0046 diff 282.4 of 1000.
₿ (29448) bm1370Module: Job ID: 48, Core: 76/10, Ver: 00A54000
₿ (29448) asic_result: Ver: 20A54000 Nonce 8DB70598 diff 3971.7 of 1000.
₿ (29448) stratum_api: tx: {"id": 7, "method": "mining.submit", "params": ["s10sia.Gamma1", "c290", "1b000000", "674e9272", "8db70598", "00a54000"]}
₿ (29498) stratum_task: rx: {"id": 7, "error": null, "result": true}
₿ (29498) stratum_task: message result accepted
₿ (29788) bm1370Module: Job ID: 48, Core: 5/6, Ver: 04C8C000
₿ (29788) asic_result: Ver: 24C8C000 Nonce 4D0D010A diff 370.6 of 1000.
₿ (30118) bm1370Module: Job ID: 60, Core: 44/15, Ver: 02B5E000
₿ (30118) asic_result: Ver: 22B5E000 Nonce A2230558 diff 1688.1 of 1000.
₿ (30118) stratum_api: tx: {"id": 8, "method": "mining.submit", "params": ["s10sia.Gamma1", "c290", "1c000000", "674e9272", "a2230558", "02b5e000"]}
₿ (30168) stratum_task: rx: {"id": 8, "error": null, "result": true}
₿ (30168) stratum_task: message result accepted
₿ (30298) bm1370Module: Job ID: 60, Core: 120/15, Ver: 04E5E000
₿ (30298) asic_result: Ver: 24E5E000 Nonce 1F6904F0 diff 1367.6 of 1000.
₿ (30298) stratum_api: tx: {"id": 9, "method": "mining.submit", "params": ["s10sia.Gamma1", "c290", "1c000000", "674e9272", "1f6904f0", "04e5e000"]}
₿ (30358) stratum_task: rx: {"id": 9, "error": null, "result": true}
₿ (30368) stratum_task: message result accepted
₿ (31168) bm1370Module: Job ID: 10, Core: 43/2, Ver: 03484000
₿ (31168) asic_result: Ver: 23484000 Nonce C5450456 diff 280.6 of 1000.
₿ (31808) bm1370Module: Job ID: 28, Core: 8/13, Ver: 051BA000
₿ (31818) asic_result: Ver: 251BA000 Nonce D7A80210 diff 2696.1 of 1000.
₿ (31818) stratum_api: tx: {"id": 10, "method": "mining.submit", "params": ["s10sia.Gamma1", "c290", "1f000000", "674e9272", "d7a80210", "051ba000"]}
₿ (31848) stratum_task: rx: {"id": 10, "error": null, "result": true}
₿ (31848) stratum_task: message result accepted

### MadNBG on 2024-12-05

I've got same problem with 2.4.0. 
I thought, it's a PSU-problem and so I did no further checks..also, because my Axe is on 698 1150
