# bitaxeorg/ESP-Miner issue #190: Pool difficulty is not respected

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/190
> Collected: 2026-10-07
> Published: 2024-05-29

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 190
- State: closed
- Author: djkazic
- Opened: 2024-05-29
- Closed: 2024-05-31
- Labels: none

## Description

**Describe the bug**
I see logs that would indicate the miner is not respecting pool diffs.

I was mining to ocean pool (ocean.xyz) which has a minimum of 16384 diff.

Logs:
```
₿ (473198) asic_result: Nonce difficulty 16000.40 of 8192.
₿ (473198) stratum_api: tx: {"id": 6, "method": "mining.submit", "params": ["[redacted].bitaxe", "17169890446666395", "7709000000000000", "66572c74", "1199c280", "00006000"]}
₿ (473258) stratum_task: rx: {"error": [23, "high-hash", null], "id": 6, "result": null}
```

Why is it 8192?

https://github.com/skot/ESP-Miner/blob/00d5a7386f259967c6fdccfcd0cb432d2008e756/main/tasks/asic_result_task.c#L42C120-L42C129

Suggests that the job's `pool_diff` member is being printed.

**To Reproduce**
Steps to reproduce the behavior:
1. Setup bitaxe
2. Mine to ocean.xyz
3. Watch logs

**Expected behavior**
The diff should be 16834.

**Hardware (please complete the following information):**
 - Bitaxe HW version: 2.2
 - Bitaxe HW vendor: self built
 - ESP-Miner FW version: v2.1.6
 - Hash Frequency: 500mhz
 - Voltage: 1.4
 - Pool URL, Port, User: ocean.xyz


## Comments

### djkazic on 2024-05-29

I did contact Ocean mining support, they stated that the first message should be a difficulty setting stratum message.

However, when I do a reboot and watch the websocket, I see that we parse a `mining.notify` only. Perhaps there's an issue with parsing the first message over stratum or something to that effect?

### djkazic on 2024-05-29

OK yeah I think that's the issue!

I wrote a script to simulate the stratum connection and the set difficulty message is there:
```
> $ python3 fakeasic.py
Connecting to mine.ocean.xyz:3334
Sending: {"id": 1, "method": "mining.subscribe", "params": []}
Sending: {"id": 2, "method": "mining.authorize", "params": ["[redacted].mock", "password"]}
Received: {"error": null, "id": 1, "result": [[["mining.notify", "c60000001"], ["mining.set_difficulty", "c60000002"]], "c6000000", 8]}
Received: {"id": null, "method": "mining.set_difficulty", "params": [16383.75]}
```

### djkazic on 2024-05-29

I think this is a side-effect of https://github.com/skot/ESP-Miner/commit/5a94acff09da7592d638b0e4db3cba084769f157

Since the authorize response is the set difficulty message

### skot on 2024-05-29

```
I (9641) stratum_api: tx: {"id": 1, "method": "mining.subscribe", "params": ["bitaxe/BM1368"]}

I (9791) stratum_api: Received result {"error": null, "id": 1, "result": [[["mining.notify", "1e0a00001"], ["mining.set_difficulty", "1e0a00002"]], "1e0a0000", 8]}
I (9791) stratum_api: tx: {"id": 2, "method": "mining.configure", "params": [["version-rolling"], {"version-rolling.mask": "ffffffff"}]}

I (9811) stratum_api: Received result {"id": null, "method": "mining.set_difficulty", "params": [16383.75]}
configure_version result null
I (9821) stratum_api: tx: {"id": 3, "method": "mining.suggest_difficulty", "params": [1000]}

I (9831) stratum_api: tx: {"id": 4, "method": "mining.authorize", "params": ["bc1--.bitaxe", "x"]}

I (9841) stratum_task: rx: {"id": null, "method": "mining.notify", "params": ["17170203186668293", "50ab58bdbc3c0f3de5c0e13720ba0e2121c9517800008de00000000000000000", "01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff3c0383e70c37003c204f4345414e2e58595a203e00203c4c6966652c2074686520756e6976657273652c20616e642065766572797468696e673e200028ffffffff13cb6d1400000000001600140cda9ff511c2341765bf7d39ff01201d6809a633a9eee005000000001976a914a934526de2e6bb9896fcb2af195412912da49b1088ac0000000000000000106a0e9382", "afad0e020000000017a914fd9215bf9b92955ae18d706c517f147b9b7772f7872ca8d3010000000017a9142495bed0e6bfba73df0568789bf245f9aa38504d87423391010000000017a9149bf0b4c2d18e606a982acc58df71507edcf9e25487828d88010000000017a914dc20b1a068e738428e948ea4ddb1b8efb99998a3879a9b63010000000017a914e9a11b4472a03cc49cf601d2ff58148c2bcb967987f06035010000000017a914bdaa3cc9e7beefac517006efaf8e71bf1fcc45ae8746d403010000000017a914bf71b01e2efc5b3c9b60a2d1d364a08959e7e330873ace6600000000001600140345e587cb42c201c30e505ea9f6f5fb935876acf9ad61000000000017a914b17f72181722af2aadba8692ead96c7855716b16876003350000000000160014d39f3d6e580534bad136f43ecc81cf9be10f27f094a53400000000001600146d814d7ebda9d66f893846a1c40ebaaeb999ceba2b83340000000000160014bbec25a5e13a1d0ed32c13be6bff844f9f38a32efcf32300000000001976a914e334c08591b05f1602518c4a10c4d258a894b97588ac0000000000000000166a144f4342318df3c095060000000f00220003d27d718054b3020000000017a914413b5901fe4e591c95405fd446b5b002da575bf0870000000000000000266a24aa21a9ed051435521e7c48289df3e452a69c17c045ecfc3e7d43a134b3b52189b3de88fc00000000", ["2551545e0cb9b85fdc4654abf5fc8b0c01278ec1aa076867e7f67738f0ed012b", "bed3d49f36770258c815ec64a287ae11ed7f7a4aad1c095dfb7e5def660ec40c", "5834c5899573663b2919b920f66f3dd5dfed6c55bb70b6032817ec84cf255553", "14ee2dafd1bb2e0431ecf74bcf37cc937c0453d0095b6896b6b864df726270ec", "599ea79000f9bdceadb5cf3fc92578fac02a9c5d60ffea20861b0e22276e4de6", "3acea17d3e8950af59400931e7fb1ad7a62f17366af9d16d22e7f20c26b7ba3b", "c408967ecbc6aa78386971d7c854484199199141f5fcc340e8c860081f7b472a", "cddbfa77160cfb248a0c3a61023aab08c667c6f3b6f03859c7ba2d8c8b2219f8", "eb12a3efd8dda64ded77163d4119e4e3f9fa92d7abae0d2b92dab7848727a1ca", "03ae307b44e0130c7355308097c1ebd7344d5a9a7edd3c3cc04376c8edc40ebd", "2dd3991720bd9daf4bf77094662bb6da600f9f39ca2eca8dd2dd2495dff525bc", "e7612db8afa1594f816263896f29f207f004f31cb96adf3dfa3a17660b291f7b"], "20000000", "170355f0", "6657a69e", true]}
I (10061) SystemModule: Syncing clock
I (10061) create_jobs_task: New Work Dequeued 17170203186668293
I (10061) stratum_task: rx: {"error": null, "id": 2, "result": {"version-rolling": true, "version-rolling.mask": "1fffe000"}}
I (10081) stratum_task: Set version mask: 1fffe000
I (10131) stratum_task: rx: {"error": [-3, "Method 'mining.suggest_difficulty' not found", null], "id": 3, "result": null}
E (10131) stratum_task: message result rejected
I (10141) stratum_task: rx: {"error": null, "id": 4, "result": true}
I (10141) stratum_task: message result accepted
I (10911) stratum_task: rx: {"id": null, "method": "mining.set_version_mask", "params": ["1fffe000"]}
I (10911) stratum_task: Set version mask: 1fffe000
I (12561) bm1368Module: Job ID: BD
I (12561) bm1368Module: RX Job ID: 58
I (12561) asic_result: Nonce difficulty 259.79 of 8192.
I (15301) bm1368Module: Job ID: 4E
I (15301) bm1368Module: RX Job ID: 20
I (15301) asic_result: Nonce difficulty 280.52 of 8192.
I (15311) bm1368Module: Job ID: 7B
I (15311) bm1368Module: RX Job ID: 38
I (15321) asic_result: Nonce difficulty 270.20 of 8192.
I (15421) bm1368Module: Job ID: 88
I (15421) bm1368Module: RX Job ID: 40
I (15421) asic_result: Nonce difficulty 261.44 of 8192.
I (18421) bm1368Module: Job ID: C6
I (18421) bm1368Module: RX Job ID: 60
I (18421) asic_result: Nonce difficulty 267.49 of 8192.
I (20491) bm1368Module: Job ID: 95
I (20491) bm1368Module: RX Job ID: 48
I (20491) asic_result: Nonce difficulty 2515.32 of 8192.
I (22061) bm1368Module: Job ID: 0B
I (22061) bm1368Module: RX Job ID: 00
I (22061) asic_result: Nonce difficulty 583.83 of 8192.
I (23701) bm1368Module: Job ID: C1
I (23701) bm1368Module: RX Job ID: 60
I (23701) asic_result: Nonce difficulty 1305.78 of 8192.
I (27051) bm1368Module: Job ID: 97
I (27051) bm1368Module: RX Job ID: 48
I (27051) asic_result: Nonce difficulty 883.40 of 8192.
I (27521) bm1368Module: Job ID: 6A
I (27521) bm1368Module: RX Job ID: 30
I (27521) asic_result: Nonce difficulty 595.72 of 8192.
I (27901) bm1368Module: Job ID: 85
I (27901) bm1368Module: RX Job ID: 40
I (27901) asic_result: Nonce difficulty 736.96 of 8192.
I (28201) bm1368Module: Job ID: F1
I (28201) bm1368Module: RX Job ID: 78
I (28201) asic_result: Nonce difficulty 2397.81 of 8192.
I (28371) bm1368Module: Job ID: 25
I (28371) bm1368Module: RX Job ID: 10
I (28371) asic_result: Nonce difficulty 4373.78 of 8192.
I (28841) bm1368Module: Job ID: 25
I (28841) bm1368Module: RX Job ID: 10
I (28841) asic_result: Nonce difficulty 14672.88 of 8192.
I (28851) stratum_api: tx: {"id": 5, "method": "mining.submit", "params": ["bc1--.bitaxe", "17170203186668293", "5507000000000000", "6657a69e", "c8212878", "0000a000"]}

I (28921) stratum_task: rx: {"error": [23, "high-hash", null], "id": 5, "result": null}
E (28921) stratum_task: message result rejected
```

### djkazic on 2024-05-29

I see the `mining.set_difficulty` now but I guess it doesn't set the difficulty properly?

Still saying 8192 in those logs

### skot on 2024-05-29

The difference is that OCEAN is making `mining.set_difficulty` a subscription, whereas public-pool (and others) seem to have `mining.set_difficulty` as a response to a method call. I guess all's fair in this wild world. I'll get esp-miner updated to handle this

```
---Public Pool---
I (9991) stratum_api: tx: {"id": 1, "method": "mining.subscribe", "params": ["bitaxe/BM1368"]}

I (10191) stratum_api: Received result {"id":1,"error":null,"result":[[["mining.notify","168e39c1"]],"168e39c1",4]}
I (10191) stratum_api: tx: {"id": 2, "method": "mining.configure", "params": [["version-rolling"], {"version-rolling.mask": "ffffffff"}]}

I (10291) stratum_api: Received result {"id":2,"error":null,"result":{"version-rolling":true,"version-rolling.mask":"1fffe000"}}
I (10291) stratum_api: Set version mask: 1fffe000
I (10301) stratum_api: tx: {"id": 3, "method": "mining.suggest_difficulty", "params": [1000]}

I (10311) stratum_api: tx: {"id": 4, "method": "mining.authorize", "params": ["bc1--.bitaxe", "x"]}

I (10501) stratum_task: rx: {"id":null,"method":"mining.set_difficulty","params":[1000]}
I (10501) stratum_task: Set stratum difficulty: 1000
I (10601) stratum_task: rx: {"id":4,"error":null,"result":true}
I (10601) stratum_task: message result accepted


---OCEAN---
I (9641) stratum_api: tx: {"id": 1, "method": "mining.subscribe", "params": ["bitaxe/BM1368"]}

I (9791) stratum_api: Received result {"error": null, "id": 1, "result": [[["mining.notify", "1e0a00001"], ["mining.set_difficulty", "1e0a00002"]], "1e0a0000", 8]}
I (9791) stratum_api: tx: {"id": 2, "method": "mining.configure", "params": [["version-rolling"], {"version-rolling.mask": "ffffffff"}]}

I (9811) stratum_api: Received result {"id": null, "method": "mining.set_difficulty", "params": [16383.75]}
configure_version result null
I (9821) stratum_api: tx: {"id": 3, "method": "mining.suggest_difficulty", "params": [1000]}

I (9831) stratum_api: tx: {"id": 4, "method": "mining.authorize", "params": ["bc1--.bitaxe", "x"]}

I (9841) stratum_task: rx: {"id": null, "method": "mining.notify", "params": ["17170203186668293", "50ab58bdbc3c0f3de5c0e13720ba0e2121c9517800008de00000000000000000", "01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff3c0383e70c37003c204f4345414e2e58595a203e00203c4c6966652c2074686520756e6976657273652c20616e642065766572797468696e673e200028ffffffff13cb6d1400000000001600140cda9ff511c2341765bf7d39ff01201d6809a633a9eee005000000001976a914a934526de2e6bb9896fcb2af195412912da49b1088ac0000000000000000106a0e9382", "afad0e020000000017a914fd9215bf9b92955ae18d706c517f147b9b7772f7872ca8d3010000000017a9142495bed0e6bfba73df0568789bf245f9aa38504d87423391010000000017a9149bf0b4c2d18e606a982acc58df71507edcf9e25487828d88010000000017a914dc20b1a068e738428e948ea4ddb1b8efb99998a3879a9b63010000000017a914e9a11b4472a03cc49cf601d2ff58148c2bcb967987f06035010000000017a914bdaa3cc9e7beefac517006efaf8e71bf1fcc45ae8746d403010000000017a914bf71b01e2efc5b3c9b60a2d1d364a08959e7e330873ace6600000000001600140345e587cb42c201c30e505ea9f6f5fb935876acf9ad61000000000017a914b17f72181722af2aadba8692ead96c7855716b16876003350000000000160014d39f3d6e580534bad136f43ecc81cf9be10f27f094a53400000000001600146d814d7ebda9d66f893846a1c40ebaaeb999ceba2b83340000000000160014bbec25a5e13a1d0ed32c13be6bff844f9f38a32efcf32300000000001976a914e334c08591b05f1602518c4a10c4d258a894b97588ac0000000000000000166a144f4342318df3c095060000000f00220003d27d718054b3020000000017a914413b5901fe4e591c95405fd446b5b002da575bf0870000000000000000266a24aa21a9ed051435521e7c48289df3e452a69c17c045ecfc3e7d43a134b3b52189b3de88fc00000000", ["2551545e0cb9b85fdc4654abf5fc8b0c01278ec1aa076867e7f67738f0ed012b", "bed3d49f36770258c815ec64a287ae11ed7f7a4aad1c095dfb7e5def660ec40c", "5834c5899573663b2919b920f66f3dd5dfed6c55bb70b6032817ec84cf255553", "14ee2dafd1bb2e0431ecf74bcf37cc937c0453d0095b6896b6b864df726270ec", "599ea79000f9bdceadb5cf3fc92578fac02a9c5d60ffea20861b0e22276e4de6", "3acea17d3e8950af59400931e7fb1ad7a62f17366af9d16d22e7f20c26b7ba3b", "c408967ecbc6aa78386971d7c854484199199141f5fcc340e8c860081f7b472a", "cddbfa77160cfb248a0c3a61023aab08c667c6f3b6f03859c7ba2d8c8b2219f8", "eb12a3efd8dda64ded77163d4119e4e3f9fa92d7abae0d2b92dab7848727a1ca", "03ae307b44e0130c7355308097c1ebd7344d5a9a7edd3c3cc04376c8edc40ebd", "2dd3991720bd9daf4bf77094662bb6da600f9f39ca2eca8dd2dd2495dff525bc", "e7612db8afa1594f816263896f29f207f004f31cb96adf3dfa3a17660b291f7b"], "20000000", "170355f0", "6657a69e", true]}

I (10061) stratum_task: rx: {"error": null, "id": 2, "result": {"version-rolling": true, "version-rolling.mask": "1fffe000"}}
I (10081) stratum_task: Set version mask: 1fffe000
I (10131) stratum_task: rx: {"error": [-3, "Method 'mining.suggest_difficulty' not found", null], "id": 3, "result": null}
E (10131) stratum_task: message result rejected
I (10141) stratum_task: rx: {"error": null, "id": 4, "result": true}
I (10141) stratum_task: message result accepted
I (10911) stratum_task: rx: {"id": null, "method": "mining.set_version_mask", "params": ["1fffe000"]}
I (10911) stratum_task: Set version mask: 1fffe000
```

### skot on 2024-05-29

plot thickens. I tried a dozen different pools and most all of them have `mining.set_difficulty` as a subscription with the actual difficulty coming as an unsolicited message. In some cases esp-miner works, in others it doesn't.

### skot on 2024-05-30

ok I've got it.

the issue is OCEAN sends the `set_difficulty` message before the response to our `mining.configure` that we were expecting. This causes esp-miner to ignore the `set_difficulty`

Out of the pools I tested, OCEAN, Luxor, Braiins and CKPool do it this way... so we need a fix.

The solution is not to hardcode _any_ order for responses, just deal with them whenever they come.

### djkazic on 2024-05-30

Makes sense, yeah the current ordering requirements feel a bit fragile.

### skot on 2024-05-31

I added my initial strategy for this fix in 61e1486 on the ocean_stratum_fix branch. Still needs testing

### djkazic on 2024-05-31

I flashed the CI bin from that branch. I can see the diff being set in the logs.

### djkazic on 2024-05-31

Hmm. Some weird wifi networking issues crop up when I flash the new firmware. Going back to the latest bin fixes it.

### djkazic on 2024-05-31

It seems like `startup_done` isn't being set to true, as it keeps switching between the stats page and the "Connecting to SSID:" page.

### djkazic on 2024-05-31

Hacked around and made my own build with default 16384 diff for the time being. That works and has no networking issues.

### skot on 2024-05-31

ah! thanks, I'll check it

### djkazic on 2024-05-31

Installed from master and it appears to be fixed.

### skot on 2024-06-03

this is going to be released in v2.1.7 https://github.com/skot/ESP-Miner/releases/tag/v2.1.7
