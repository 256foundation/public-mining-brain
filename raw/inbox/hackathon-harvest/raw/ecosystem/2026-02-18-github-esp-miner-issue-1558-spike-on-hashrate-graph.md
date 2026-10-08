# bitaxeorg/ESP-Miner issue #1558: Spike on hashrate graph

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1558
> Collected: 2026-10-07
> Published: 2026-02-18

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1558
- State: closed
- Author: mutatrum
- Opened: 2026-02-18
- Closed: 2026-03-13
- Labels: none

## Description

After ~10 hours of uptime, a spike appears:

<img width="724" height="972" alt="Image" src="https://github.com/user-attachments/assets/5b33276c-b4a8-45c3-970d-26a306118127" />

Seen it twice now. It doesn't show in statistics, only in live data so it's a short-lived peak.

## Comments

### mutatrum on 2026-02-19

It was not fixed. After 3h15m:

<img width="1920" height="968" alt="Image" src="https://github.com/user-attachments/assets/d11c1054-3020-4d03-bed1-db00fbc51f50" />

### mutatrum on 2026-02-20

This happened around that time:
```
I (11687381) stratum_api: rx: {"id":null,"method":"mining.notify","params":["..."],"20000000","1701f303","69979af4",false]}
I (11687439) bm1370: Job ID: 30, Asic nr: 0, Core: 108/10, Ver: 048B4000
I (11687501) create_jobs_task: New Work Dequeued 1771543284367818953
I (11687503) stratum_task: Scriptsig: ....i....../m45eu-goPool/JeKM-oKlc
I (11687515) asic_result: ID: 1771543254378683498, ASIC nr: 0, ver: 248B4000 Nonce 4B5B02D8 diff 360.2 of 1217.
I (11687522) stratum_task: Coinbase outputs: 4, total value: 314842805 sats
I (11687540) stratum_task:   Output 0: OP_RETURN: .!.........=.@=F;M9.l..Q8...0w!.o...
I (11687549) stratum_task:   Output 1: bc1q###################################### (308545949 sat) (Your payout address)
I (11687560) stratum_task:   Output 2: 3B86bWqfjdQeLEr8nkeeWU6ygksc2K7MoL (5667170 sat)
I (11687569) stratum_task:   Output 3: bc1qxvdq5fgftkgdxw8f8k4kz8v03s6cf7jhd6rayf (629686 sat)
I (11687580) stratum_api: rx: {"id":null,"method":"client.show_message","params":["Pool restarting; please reconnect."]}
I (11687590) stratum_api: unhandled method in stratum message: {"id":null,"method":"client.show_message","params":["Pool restarting; please reconnect."]}
E (11687606) stratum_api: Error: transport read failed: Connection closed by peer (code: -1)
E (11687614) stratum_task: Failed to receive JSON-RPC line, reconnecting...
E (11687621) stratum_task: Shutting down socket and restarting...
I (11687630) stratum_task: Clean Jobs: clearing queue
I (11688699) stratum_task: Resolved eu.m45core.com:4333 → 188.245.70.49
I (11688700) stratum_task: Connecting to: stratum+tcp://eu.m45core.com:4333 (188.245.70.49)
I (11688705) stratum_api: Using TLS transport
I (11688710) stratum_api: Using default cert bundle
I (11688715) stratum_task: Transport initialized, connecting to eu.m45core.com:4333
E (11688747) esp-tls: [sock=43] delayed connect error: Connection reset by peer
E (11688748) esp-tls: Failed to open new connection
E (11688750) transport_base: Failed to open a new connection
E (11688756) stratum_task: Transport unable to connect to eu.m45core.com:4333 (errno -1). Attempt: 2
I (11689065) bm1370: Job ID: 78, Asic nr: 0, Core: 83/2, Ver: 05D64000
I (11689066) asic_result: ID: 1771543284367818953, ASIC nr: 0, ver: 25D64000 Nonce 4CE801A6 diff 370.9 of 1217.
I (11689073) fan_controller: Temp: 55.4 °C, SetPoint: 60.0 °C, Output: 0.0%
I (11689380) bm1370: Job ID: 10, Asic nr: 0, Core: 10/4, Ver: 038A8000
I (11689380) asic_result: ID: 1771543284367818953, ASIC nr: 0, ver: 238A8000 Nonce 10E50314 diff 367.5 of 1217.
I (11689506) bm1370: Job ID: 10, Asic nr: 0, Core: 82/13, Ver: 0517A000
I (11689507) asic_result: ID: 1771543284367818953, ASIC nr: 0, ver: 2517A000 Nonce 694C00A4 diff 286.2 of 1217.
I (11689815) bm1370: Job ID: 28, Asic nr: 0, Core: 44/10, Ver: 02BB4000
I (11689816) asic_result: ID: 1771543284367818953, ASIC nr: 0, ver: 22BB4000 Nonce 4DDA0258 diff 3022.6 of 1217.
I (11689823) stratum_api: tx: {"id":2577,"method":"mining.submit","params":["bc1q######################################.bitaxe-gamma","1771543284367818953","04000000","69979af4","4dda0258","02bb4000"]}
I (11691068) fan_controller: Temp: 55.1 °C, SetPoint: 60.0 °C, Output: 2.0%
I (11693068) fan_controller: Temp: 55.4 °C, SetPoint: 60.0 °C, Output: 1.8%
I (11693774) stratum_task: Resolved eu.m45core.com:4333 → 188.245.70.49
I (11693774) stratum_task: Connecting to: stratum+tcp://eu.m45core.com:4333 (188.245.70.49)
I (11693780) stratum_api: Using TLS transport
I (11693785) stratum_api: Using default cert bundle
I (11693790) stratum_task: Transport initialized, connecting to eu.m45core.com:4333
I (11694374) esp-x509-crt-bundle: Certificate validated
I (11694561) stratum_task: Resetting stratum uid
I (11694562) stratum_task: Clean Jobs: clearing queue
I (11694562) stratum_api: tx: {"id":1,"method":"mining.configure","params":[["version-rolling"],{"version-rolling.mask":"ffffffff"}]}
I (11694576) stratum_api: tx: {"id":2,"method":"mining.subscribe","params":["bitaxe/BM1370/v2.13.0b8-4-ge44a0f9d-dirty"]}
I (11694587) stratum_api: tx: {"id":3,"method":"mining.authorize","params":["bc1q######################################.bitaxe-gamma","x"]}
I (11694634) stratum_api: rx: {"id":1,"result":{"version-rolling":true,"version-rolling.mask":"1fffe000","version-rolling.min-bit-count":1},"error":null}
I (11694638) stratum_task: Set version mask: 1fffe000
I (11694645) stratum_api: rx: {"id":2,"result":[[["mining.set_difficulty","1"],["mining.notify","1"],["mining.set_extranonce","1"],["mining.set_version_mask","1"]],"00000001",4],"error":null}
I (11694662) stratum_task: Set extranonce: 00000001, extranonce_2_len: 4
I (11694670) stratum_api: rx: {"id":3,"result":true,"error":null}
I (11694676) stratum_task: setup message accepted
I (11694681) stratum_api: tx: {"id":4,"method":"mining.suggest_difficulty","params":[2048]}
I (11694713) stratum_api: rx: {"id":4,"result":true,"error":null}
I (11694714) stratum_task: setup message accepted
I (11694716) stratum_api: rx: {"id":null,"method":"mining.set_difficulty","params":[1448.1546878700492]}
I (11694725) stratum_task: Set pool difficulty: 1448
I (11694734) stratum_api: rx: {"id":null,"method":"mining.notify","params":["..."],"20000000","1701f303","69979af8",true]}
W (11694842) transport_base: Poll timeout or error, errno=Success, fd=-1, timeout_ms=5000
I (11694859) create_jobs_task: New Work Dequeued 1
I (11694860) stratum_task: Scriptsig: ....i....../m45eu-goPool/JeKM-Fjxd
I (11694873) create_jobs_task: New pool difficulty 1448
I (11694886) create_jobs_task: Set chip version rolls 65535
I (11694882) stratum_task: Coinbase outputs: 4, total value: 314842805 sats
I (11694873) bm1370: Job ID: 40, Asic nr: 0, Core: 123/5, Ver: 04C8A000
I (11694903) stratum_api: rx: {"id":null,"method":"mining.notify","params":["..."],"20000000","1701f303","69979af8",true]}
W (11694907) bm1370: Invalid job nonce found, 0x40
I (11695036) create_jobs_task: New Work Dequeued 1
I (11695037) stratum_task: Coinbase outputs: 4, total value: 314842805 sats
I (11695047) bm1370: Job ID: 58, Asic nr: 0, Core: 2/1, Ver: 03C02000
W (11695060) bm1370: Invalid job nonce found, 0x58
I (11695066) bm1370: Job ID: 38, Asic nr: 0, Core: 100/7, Ver: 0554E000
W (11695073) bm1370: Invalid job nonce found, 0x38
I (11695079) bm1370: Job ID: 68, Asic nr: 0, Core: 7/10, Ver: 02674000
W (11695086) bm1370: Invalid job nonce found, 0x68
I (11695091) bm1370: Job ID: 00, Asic nr: 0, Core: 107/15, Ver: 01EFE000
W (11695099) bm1370: Invalid job nonce found, 0x00
I (11695104) fan_controller: Temp: 55.2 °C, SetPoint: 60.0 °C, Output: 0.6%
I (11695509) bm1370: Job ID: 48, Asic nr: 0, Core: 24/10, Ver: 059F4000
I (11695510) asic_result: ID: 1, ASIC nr: 0, ver: 259F4000 Nonce F5350030 diff 291.8 of 1448.
I (11696687) bm1370: Job ID: 10, Asic nr: 0, Core: 80/9, Ver: 019D2000
I (11696688) asic_result: ID: 1, ASIC nr: 0, ver: 219D2000 Nonce 3B9604A0 diff 4836.4 of 1448.
I (11696693) stratum_api: tx: {"id":5,"method":"mining.submit","params":["bc1q######################################.bitaxe-gamma","1","03000000","69979af8","3b9604a0","019d2000"]}
I (11696730) stratum_api: rx: {"id":5,"result":true,"error":null}
I (11696731) stratum_task: message result accepted
I (11696732) stratum_task: Stratum response time: 18.4 ms
```
