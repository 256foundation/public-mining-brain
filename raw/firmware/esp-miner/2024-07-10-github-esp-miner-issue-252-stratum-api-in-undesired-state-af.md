# bitaxeorg/ESP-Miner issue #252: stratum_api in undesired state after wifi timeout

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/252
> Collected: 2026-10-07
> Published: 2024-07-10

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 252
- State: closed
- Author: mutatrum
- Opened: 2024-07-10
- Closed: 2024-12-01
- Labels: bug

## Description

When the wifi haa a timeout `wifi:bcn_timeout,ap_probe_send_start`, it tries to restart the socket and stratum connection, but some bits are left in a wrong state resulting in the device hashing but almost no shares accepted. There are several issues hiding that prevent a proper reconnection.

It starts with:

```
I (118764501) bm1368Module: Job ID: 08, Core: 77/6, Ver: 0146C000
I (118764501) asic_result: Ver: 2146C000 Nonce D317009A diff 794.2 of 502.
I (118764511) stratum_api: tx: {"id": 32242, "method": "mining.submit", "params": ["bc1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq.bitaxe", "64851638001239e9", "0800000000000000", "668d76e2", "d317009a", "0146c000"]}
I (118766321) bm1368Module: Job ID: 50, Core: 0/4, Ver: 06C08000
I (118766321) asic_result: Ver: 26C08000 Nonce A48C0000 diff 391.6 of 502.
I (118766661) bm1368Module: Job ID: 68, Core: 6/15, Ver: 03F7E000
I (118766661) asic_result: Ver: 23F7E000 Nonce 4CA5000C diff 378.1 of 502.
I (118766731) bm1368Module: Job ID: 68, Core: 72/15, Ver: 0549E000
I (118766741) asic_result: Ver: 2549E000 Nonce 9EC90290 diff 497.3 of 502.
I (118768811) bm1368Module: Job ID: 48, Core: 38/10, Ver: 06A34000
I (118768811) asic_result: Ver: 26A34000 Nonce B50E034C diff 465.9 of 502.
I (118770191) wifi:bcn_timeout,ap_probe_send_start
I (118771741) bm1368Module: Job ID: 58, Core: 49/2, Ver: 05604000
I (118771741) asic_result: Ver: 25604000 Nonce 3F3F0062 diff 339.7 of 502.
I (118772581) bm1368Module: Job ID: 08, Core: 35/0, Ver: 02A60000
I (118772581) asic_result: Ver: 22A60000 Nonce C8CC0146 diff 270.4 of 502.
I (118772701) wifi:ap_probe_send over, resett wifi status to disassoc
I (118772701) wifi:state: run -> init (0xc800)
I (118772701) wifi:pm stop, total sleep time: 103045108713 us / 118771732338 us

I (118772701) wifi:<ba-del>idx:0, tid:0
I (118772711) wifi:<ba-del>idx:1, tid:6
I (118772711) wifi:new:<1,0>, old:<1,1>, ap:<255,255>, sta:<1,0>, prof:1, snd_ch_cfg:0x0
I (118773431) bm1368Module: Job ID: 38, Core: 18/13, Ver: 0007A000
I (118773431) asic_result: Ver: 2007A000 Nonce 3C330024 diff 353.1 of 502.
I (118775031) bm1368Module: Job ID: 00, Core: 28/9, Ver: 01BD2000
I (118775031) asic_result: Ver: 21BD2000 Nonce A5B90138 diff 385.0 of 502.
I (118775221) wifi station: Retrying WiFi connection...
I (118775221) stratum_api: Error: recv
E (118775221) stratum_task: Failed to receive JSON-RPC line, reconnecting...
W (118775221) httpd_txrx: httpd_sock_err: error in recv : 113
I (118776071) wifi:new:<8,0>, old:<1,0>, ap:<255,255>, sta:<8,0>, prof:1, snd_ch_cfg:0x0
I (118776071) wifi:state: init -> auth (0xb0)
I (118776081) wifi:state: auth -> assoc (0x0)
I (118776091) wifi:state: assoc -> run (0x10)
I (118776101) bm1368Module: Job ID: 30, Core: 21/9, Ver: 03012000
I (118776101) asic_result: Ver: 23012000 Nonce 82A4012A diff 1848.1 of 502.
I (118776111) stratum_api: tx: {"id": 32243, "method": "mining.submit", "params": ["bc1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq.bitaxe", "64851638001239e9", "1f00000000000000", "668d76e2", "82a4012a", "03012000"]}
I (118776121) wifi:connected with WIFISSID, aid = 31, channel 8, BW20, bssid = ##:##:##:##:##:##
I (118776131) wifi:security: WPA2-PSK, phy: bgn, rssi: -47
I (118776161) wifi:pm start, type: 1

I (118776161) wifi:set rx beacon pti, rx_bcn_pti: 0, bcn_timeout: 25000, mt_pti: 0, mt_time: 10000
I (118776171) wifi:<ba-add>idx:0 (ifx:0, ##:##:##:##:##:##), tid:6, ssn:1, winSize:64
I (118776181) wifi:AP's beacon interval = 102400 us, DTIM period = 1
E (118776221) stratum_task: Shutting down socket and restarting...
I (118776221) stratum_task: Socket created, connecting to 51.81.56.15:3333
E (118776221) stratum_task: Socket unable to connect to solo.ckpool.org:3333 (errno 118)
I (118777161) wifi station: Bitaxe ip:192.168.1.153
I (118777161) esp_netif_handlers: sta ip: 192.168.1.153, mask: 255.255.255.0, gw: 192.168.1.1
I (118777321) bm1368Module: Job ID: 60, Core: 43/8, Ver: 06D30000
I (118777321) asic_result: Ver: 26D30000 Nonce 1BFC0056 diff 1830.1 of 502.
I (118777331) stratum_api: tx: {"id": 32244, "method": "mining.submit", "params": ["bc1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq.bitaxe", "64851638001239e9", "2100000000000000", "668d76e2", "1bfc0056", "06d30000"]}
I (118778261) bm1368Module: Job ID: 10, Core: 68/2, Ver: 05BC4000
I (118778261) asic_result: Ver: 25BC4000 Nonce 71B00088 diff 607.1 of 502.
I (118778261) stratum_api: tx: {"id": 32245, "method": "mining.submit", "params": ["bc1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq.bitaxe", "64851638001239e9", "2300000000000000", "668d76e2", "71b00088", "05bc4000"]}
I (118780101) bm1368Module: Job ID: 70, Core: 69/0, Ver: 02F80000
I (118780101) asic_result: Ver: 22F80000 Nonce 4931028A diff 2153.2 of 502.
I (118780101) stratum_api: tx: {"id": 32246, "method": "mining.submit", "params": ["bc1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq.bitaxe", "64851638001239e9", "2700000000000000", "668d76e2", "4931028a", "02f80000"]}
I (118780461) bm1368Module: Job ID: 08, Core: 66/12, Ver: 00898000
I (118780461) asic_result: Ver: 20898000 Nonce 21F50284 diff 621.2 of 502.
I (118780461) stratum_api: tx: {"id": 32247, "method": "mining.submit", "params": ["bc1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq.bitaxe", "64851638001239e9", "2800000000000000", "668d76e2", "21f50284", "00898000"]}
I (118780791) wifi:<ba-add>idx:1 (ifx:0, ##:##:##:##:##:##), tid:0, ssn:1, winSize:64
I (118781081) bm1368Module: Job ID: 20, Core: 20/14, Ver: 0299C000
I (118781081) asic_result: Ver: 2299C000 Nonce 1E650128 diff 4802.2 of 502.
I (118781081) stratum_api: tx: {"id": 32248, "method": "mining.submit", "params": ["bc1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq.bitaxe", "64851638001239e9", "2900000000000000", "668d76e2", "1e650128", "0299c000"]}
I (118781231) stratum_task: Socket created, connecting to 51.81.56.15:3333
I (118781401) stratum_api: tx: {"id": 32249, "method": "mining.subscribe", "params": ["bitaxe/BM1368 (v2.1.9-8-g04c8b80-dirty)"]}
I (118781411) stratum_api: tx: {"id": 32250, "method": "mining.configure", "params": [["version-rolling"], {"version-rolling.mask": "ffffffff"}]}
I (118781421) stratum_api: tx: {"id": 32251, "method": "mining.suggest_difficulty", "params": [1000]}
I (118781431) stratum_api: tx: {"id": 32252, "method": "mining.authorize", "params": ["bc1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq.bitaxe", "x"]}
I (118781611) stratum_task: rx: {"result":[[["mining.notify","761aae13"]],"d1e54072",8],"id":32249,"error":null}
I (118781611) stratum_api: unhandled result in stratum message: {"result":[[["mining.notify","761aae13"]],"d1e54072",8],"id":32249,"error":null}
I (118781631) stratum_task: rx: {"params":[10000],"id":null,"method":"mining.set_difficulty"}
I (118781641) stratum_task: Set stratum difficulty: 10000
I (118781811) stratum_task: rx: {"result":{"version-rolling":true,"version-rolling.mask":"1fffe000"},"id":32250,"error":null}
I (118781811) stratum_api: unhandled result in stratum message: {"result":{"version-rolling":true,"version-rolling.mask":"1fffe000"},"id":32250,"error":null}
I (118781831) stratum_task: rx: {"params":["64851638001239e9","6bd30b3f0f6389e1074adc7ea14a1d500e0a32360001838b0000000000000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff3503f5fd0c0004e2768d66046b7cfb080c","0a636b706f6f6c112f736f6c6f2e636b706f6f6c2e6f72672fffffffff03e501fc120000000016001480bded37e3f86a1a546e099b15e2b02855d3843c0f2f63000000000016001451ed61d2f6aa260cc72cdf743e4e436a82c010270000000000000000266a24aa21a9ed1857afd3a1f7a45000ffac26c582d2ae74d4194c07afee5086d272d0a909453600000000",["3f2d2340cc79279d6487b660fda157a888cadcde9e3724c7a3f02fc80c1610ea","e6409546c590bf39418eee8f90d2bac9843077c800f276c760b70b787befcb03","bd6c80dfbd529f2ad4c93d79d5702263d1361670051899d91163f802b595a9e5","c26a908877170bfebce8ea0a359345c2771ac95216c44d00d3c5cbec4c6622e9","d870b61fda0db00c5725d88ffbe388a7c6bb89fde0bcc19946253eaf73f94c5e","9cccbbc08318fb3023c93f158a8d5c63a566eff15de0e7a5a1f00bedc27e363b","cd13f3b265ff56af49dfa257b2f13a139ac3f951466a5f4ea70f3eafe26e92bb","c861949e4035080ef907e21d040a1f97c710213326611c139e7f7c31817525fa","3f8b7bce446134687a8a630f107aa5c530751763843cf1fdb2ff758689ced10f","23078b63787805970ccfd474bcd843608eb16f8b824b9a14182e02ed09ad6749","e58b75b09117232e9eb53f8bb191d124e401e7174acd4648da6aada2ff6c56f4","412ed970f32f3ef85c67d2805203795a8a6e5b042a2b5cf18bbd72884f4d08df"],"20000000","17038a6d","668d76e2",true],"id":null,"method":"mining.notify"}
I (118781951) stratum_task: Clean Jobs: clearing queue
I (118781961) create_jobs_task: New Work Dequeued 64851638001239e9
I (118781961) stratum_task: rx: {"params":[10000],"id":null,"method":"mining.set_difficulty"}
I (118781971) ASIC_task: New pool difficulty 10000
I (118781981) stratum_task: rx: {"result":true,"error":null,"id":32252}
I (118781991) stratum_task: message result accepted
```
Some things that caught my eye:
- The `mining.notify` and `version-rolling` responses are unhandled.
- It continues to send `mining.submit` messages, even though the socket is not alive. 
- The id of the last `rx` in this log seems like a continuation of the ids from before. It looks like this is relevant, although I'm not sure who is driving this sequence, is that the pool or the miner, or both?

It looks like it reconnected correctly, and starts mining with the ckpool default 10000 difficulty. A while later, when a share has been found it's rejected with `Above target`:
```
I (118958661) bm1368Module: Job ID: 00, Core: 76/7, Ver: 0318E000
I (118958661) asic_result: Ver: 2318E000 Nonce 49830298 diff 18515.9 of 10000.
I (118958661) stratum_api: tx: {"id": 32253, "method": "mining.submit", "params": ["bc1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq.bitaxe", "64851638001239ef", "2300000000000000", "668d7796", "49830298", "0318e000"]}
I (118958681) bm1368Module: Job ID: 00, Core: 28/13, Ver: 037BA000
I (118958691) asic_result: Ver: 237BA000 Nonce 81B20138 diff 523.1 of 10000.
I (118958861) stratum_task: rx: {"reject-reason":"Above target","result":false,"error":null,"id":32253}
```
This looks like #212 and it might be a red herring. However, on the next `mining.submit` tx:
```
I (119133941) bm1368Module: Job ID: 50, Core: 32/1, Ver: 08002000
I (119133941) asic_result: Ver: 28002000 Nonce C8740040 diff 10944.3 of 10000.
I (119133951) stratum_api: tx: {"id": 32254, "method": "mining.submit", "params": ["bc1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq.bitaxe", "64851638001239f5", "1a00000000000000", "668d784a", "c8740040", "08002000"]}
I (119134061) stratum_task: rx: {"id":null,"method":"client.reconnect","params":[]}
I (119134071) stratum_api: unhandled method in stratum message: {"id":null,"method":"client.reconnect","params":[]}
I (119134071) stratum_task: rx: {"reject-reason":"Above target","result":false,"error":null,"id":32254}
E (119134081) stratum_task: message result rejected
```
The pool requests a `client.reconnect`, as I assume they see something out of sync as well. Not sure what, maybe because of the still increasing ids?

And finally, a little while later it seems the parser is in a proper error state and requests a socker restart:
```
I (119182231) bm1368Module: Job ID: 68, Core: 45/5, Ver: 06AAA000
I (119182241) asic_result: Ver: 26AAA000 Nonce 7A2F005A diff 19254.4 of 10000.
I (119182241) stratum_api: tx: {"id": 32256, "method": "mining.submit", "params": ["bc1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq.bitaxe", "64851638001239f8", "1600000000000000", "668d787c", "7a2f005a", "06aaa000"]}
I (119182401) stratum_api: Error: recv
E (119182401) stratum_task: Failed to receive JSON-RPC line, reconnecting...
E (119183401) stratum_task: Shutting down socket and restarting...
```
This dance will continue forever, restarting the socket every few minutes.

BitAxe 400, latest master  [04c8b80](https://github.com/skot/ESP-Miner/commit/04c8b8028776aaeafd8d4ac2277b6bf1a09aaaee).

## Comments

### mutatrum on 2024-07-10

I'm adding support for `client.reconnect` and see if resetting `send_uid` on a socket restart fixes this.

### mseilnacht on 2024-07-11

In the file component/stratum/stratum_api.c file , it does not look like the “STRATUM_V1_receive_jsonrpc_line” and “STRATUM_V1_submit_share” functions will properly detect an orderly socket close by the server.  The recv call would return ‘0’ in this case and the check against -1 would miss the event,  and loop forever in the read.  The writes don’t check for ECONNRESET either, so they will also fail to recognize the error.

Depending on the compiler optimization and ESP32 behavior , it may also be necessary to declare GLOBAL_STATE->sock as volatile to ensure that it is pulled from the heap and not cached register values.

### mseilnacht on 2024-07-11

According to lwIP recv() docs, the API is not like POSIX, and rather than return -1, it returns the actual errcode.

### seepv on 2024-07-17

After replacing an Half-Defective-Chinese-Fan (The Fan-Sound has Changed and the Airflow was massively reduced) with an Noctua-Fan (NF-A4x20) the
Error:
```
stratum_api: Error: recv
stratum_api: Restarting System because of Error: recv
```
is gone and
the Bitaxe is running like a charm again (many hours not just minutes).

I assume some interference is causing the bitaxe to restart.
What do you think is it possible that the Bitaxe restarts caused by electric or/and magnetic interference?

```
"version":	"v2.1.8", "boardVersion":	"204",
"temp":	48 (Half-Defective-Chinese-Fan)
"temp":	58 (Noctua-Fan)
```

### skot on 2024-10-10

@mutatrum is this still happening? We've had a lot of changes around handling network failures

### mutatrum on 2024-10-12

The timeout still happens, but the device recovered by shutting down the socket and reconnecting to the pool after the wifi is back up and running. On my my Supra 400, both in 2.1.10 as well in 2.2.2 were good, both versions had 30+ days uptime with probably a few `bcn_timeout` event per day.

Logs:
```
I (67497825) bm1368Module: Job ID: 48, Core: 1/9, Ver: 06E92000
I (67497825) asic_result: Ver: 26E92000 Nonce 0EAD0002 diff 331.7 of 639.
I (67498785) wifi:bcn_timeout,ap_probe_send_start
I (67499185) bm1368Module: Job ID: 10, Core: 29/2, Ver: 047C4000
I (67499185) asic_result: Ver: 247C4000 Nonce 6FB0023A diff 494.8 of 639.
I (67499825) bm1368Module: Job ID: 28, Core: 32/14, Ver: 06FE4000
I (67499825) asic_result: Ver: 26FE4000 Nonce 0DE90040 diff 421.1 of 639.
I (67501285) wifi:ap_probe_send over, resett wifi status to disassoc
I (67501285) wifi:state: run -> init (0xc800)
I (67501295) wifi:pm stop, total sleep time: 1897374459 us / 2147338912 us

I (67501295) wifi:<ba-del>idx:1, tid:0
I (67501295) wifi:<ba-del>idx:0, tid:6
I (67501305) wifi:new:<5,0>, old:<5,0>, ap:<255,255>, sta:<5,0>, prof:1, snd_ch_cfg:0x0
I (67503015) bm1368Module: Job ID: 50, Core: 37/4, Ver: 01908000
I (67503015) asic_result: Ver: 21908000 Nonce B5AD014A diff 5515.0 of 639.
I (67503015) stratum_api: tx: {"id": 430, "method": "mining.submit", "params": ["bc1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq.bitaxe", "648516380015fdc3", "910a020000000000", "66f8fc0b", "b5ad014a", "01908000"]}
I (67503815) wifi station: Retrying WiFi connection...
I (67503815) stratum_api: Error: recv
E (67503815) stratum_task: Failed to receive JSON-RPC line, reconnecting...
I (67504085) wifi:new:<2,0>, old:<5,0>, ap:<255,255>, sta:<2,0>, prof:1, snd_ch_cfg:0x0
I (67504085) wifi:state: init -> auth (0xb0)
I (67504105) wifi:state: auth -> assoc (0x0)
I (67504105) wifi:state: assoc -> run (0x10)
I (67504135) wifi:connected with <######>, aid = 35, channel 2, BW20, bssid = ##:##:##:##:##:##
I (67504135) wifi:security: WPA2-PSK, phy: bgn, rssi: -38
I (67504155) wifi:pm start, type: 1

I (67504155) wifi:set rx beacon pti, rx_bcn_pti: 0, bcn_timeout: 25000, mt_pti: 0, mt_time: 10000
I (67504155) wifi:AP's beacon interval = 102400 us, DTIM period = 1
I (67504175) wifi:<ba-add>idx:0 (ifx:0, ##:##:##:##:##:##), tid:6, ssn:1, winSize:64
E (67504815) stratum_task: Shutting down socket and restarting...
I (67504815) stratum_task: Socket created, connecting to 51.81.56.15:3333
E (67504815) stratum_task: Socket unable to connect to solo.ckpool.org:3333 (errno 118)
I (67505155) wifi station: Bitaxe ip:192.168.1.153
I (67505155) esp_netif_handlers: sta ip: 192.168.1.153, mask: 255.255.255.0, gw: 192.168.1.1
I (67505695) bm1368Module: Job ID: 48, Core: 50/1, Ver: 04B42000
I (67505695) asic_result: Ver: 24B42000 Nonce E90B0164 diff 876.2 of 639.
I (67505705) stratum_api: tx: {"id": 431, "method": "mining.submit", "params": ["bc1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq.bitaxe", "648516380015fdc3", "960a020000000000", "66f8fc0b", "e90b0164", "04b42000"]}
I (67505795) wifi:<ba-add>idx:1 (ifx:0, ##:##:##:##:##:##), tid:0, ssn:1, winSize:64
I (67509825) stratum_task: Socket created, connecting to 51.81.56.15:3333
I (67509995) stratum_api: Resetting stratum uid
I (67509995) stratum_task: Clean Jobs: clearing queue
I (67509995) stratum_api: tx: {"id": 1, "method": "mining.subscribe", "params": ["bitaxe/BM1368/v2.2.2"]}
I (67510005) stratum_api: tx: {"id": 2, "method": "mining.configure", "params": [["version-rolling"], {"version-rolling.mask": "ffffffff"}]}
I (67510025) stratum_api: tx: {"id": 3, "method": "mining.suggest_difficulty", "params": [1000]}
I (67510035) stratum_api: tx: {"id": 4, "method": "mining.authorize", "params": ["bc1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq.bitaxe", "x"]}
I (67510195) stratum_task: rx: {"result":[[["mining.notify","7be71efd"]],"fb8c1b77",8],"id":1,"error":null}
I (67510205) stratum_api: extranonce_str: fb8c1b77
I (67510205) stratum_api: extranonce_2_len: 8
I (67510215) stratum_task: rx: {"params":[10000],"id":null,"method":"mining.set_difficulty"}
I (67510215) stratum_task: Set stratum difficulty: 10000
I (67510405) stratum_task: rx: {"result":{"version-rolling":true,"version-rolling.mask":"1fffe000"},"id":2,"error":null}
I (67510405) stratum_api: Set version mask: 1fffe000
I (67510405) stratum_task: Set version mask: 1fffe000
I (67510415) stratum_task: rx: {"params":["648516380015fdc4","12e729fb4b524609d61ac813d2de87f02ecdf84800000eee0000000000000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff35035e2c0d000429fcf86604198e230d0c","0a636b706f6f6c112f736f6c6f2e636b706f6f6c2e6f72672fffffffff033e5c63120000000016001480bded37e3f86a1a546e099b15e2b02855d3843c8e1160000000000016001451ed61d2f6aa260cc72cdf743e4e436a82c010270000000000000000266a24aa21a9eddec62caf232c233d817ab6384423006a3d80617a806bbc5a071530014cc9d57e00000000",["6a39c5891f9472dcb3e672904ddb116f449f200ed218830b14110dae0a439a45","2768792df31799aa80353cff6a2fc3cea0bf4f0be8df72c1c7be6ab6df96cd43","226962dfb377092a0e4cfbbdd3cb104646572e37a072a5a80dabd539c31ad7ad","2e23a0dca06999f7eeeaa596ec5e585af61ce7be2e5d38eb5709c361f9c60832","89e888f493f891d963312399446457f2c38e261836442d8e74b8387c6e92bd22","e9dfa5ea69c64b3193a7ed556bb17d4251c6b5a00f61e1cc9b631d3de571695e","6956ef269bdc64e7dc8c014c4beb6f5f5c1cbd9588d69910c7213f40c55a6b6d","1218611bd9e5780bef4019396b592637a04887e43e7e0538286d8e361034977b","dec9d88b21bbdc4eb24f71c47a804a051f964afc20407019f885b119586f529d","420228b32dc69ff58b9762cf36389e0cab7633d7b5e31d64c8d653d3902c866b","fa0452327f68a1f4cd6991a5ffff2ad01b1a9300d099baee1cc23befc94cc675","9b5dac11f351f0c44d7bce53b4fc02b54e8f576943805f2d7752fbd412c05db0"],"20000000","17032f14","66f8fc29",true],"id":null,"method":"mining.notify"}
I (67510545) create_jobs_task: New Work Dequeued 648516380015fdc4
I (67510545) stratum_task: rx: {"params":[10000],"id":null,"method":"mining.set_difficulty"}
I (67510545) create_jobs_task: Job processed and queued: 648516380015fdc4
I (67510545) ASIC_task: New pool difficulty 10000
I (67510565) stratum_task: rx: {"result":true,"error":null,"id":4}
```

The only nit-pick I think could be improved is that `stratum_api` shouldn't try to send any more mining.submits if the socket is dead.

### WantClue on 2024-12-01

Should be fixed with the backup pool option and the check on pool health (connection)
