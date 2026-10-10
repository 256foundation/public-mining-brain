# bitaxeorg/ESP-Miner issue #226: Restarting System when WiFi is reconnecting

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/226
> Collected: 2026-10-07
> Published: 2024-06-16

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 226
- State: closed
- Author: mutatrum
- Opened: 2024-06-16
- Closed: 2025-01-27
- Labels: bug

## Description

On regular intervals, a restart is triggered when the wifi received a timeout. It seems the wifi connection is in the process of getting reconnected, but the statum_api gets a 'recv' error and triggers a restart. Expected behaviour for the stratum_api would be to back off for a few seconds and retry a few times, as it seems the connection will be re-established.

The logs show the course of events:
```
I (71887836) stratum_api: tx: {"id": 22237, "method": "mining.submit", "params": ["bc1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq.bitaxe", "6485163800110394", "8b06000000000000", "666ac8cc", "a086343c", "00004000"]}

I (71890086) wifi:bcn_timeout,ap_probe_send_start
I (71891076) bm1368Module: Job ID: 2D
I (71891076) bm1368Module: RX Job ID: 10
I (71891076) asic_result: Nonce difficulty 431.82 of 472.
I (71892356) bm1368Module: Job ID: FA
I (71892356) bm1368Module: RX Job ID: 78
I (71892356) asic_result: Nonce difficulty 279.34 of 472.
I (71892586) wifi:ap_probe_send over, resett wifi status to disassoc
I (71892596) wifi:state: run -> init (0xc800)
I (71892596) wifi:pm stop, total sleep time: 62173215711 us / 71891718423 us

I (71892596) wifi:<ba-del>idx:0, tid:0
I (71892596) wifi:<ba-del>idx:1, tid:6
I (71892606) wifi:new:<2,0>, old:<2,0>, ap:<255,255>, sta:<2,0>, prof:1, snd_ch_cfg:0x0
I (71892886) bm1368Module: Job ID: 13
I (71892886) bm1368Module: RX Job ID: 08
I (71892886) asic_result: Nonce difficulty 389.38 of 472.
I (71895016) bm1368Module: Job ID: 0C
I (71895016) bm1368Module: RX Job ID: 00
I (71895016) asic_result: Nonce difficulty 283.90 of 472.
I (71895116) wifi station: Retrying WiFi connection...
E (71895116) stratum_api: recv
I (71895116) stratum_api: Restarting System because of Error: recv
W (71895116) httpd_txrx: httpd_sock_err: error in recv : 113
I (71895606) wifi:new:<5,0>, old:<2,0>, ap:<255,255>, sta:<5,0>, prof:1, snd_ch_cfg:0x0
I (71895606) wifi:state: init -> auth (0xb0)
I (71895616) wifi:state: auth -> assoc (0x0)
I (71895636) wifi:state: assoc -> run (0x10)
I (71895666) wifi:connected with ####, aid = 19, channel 5, BW20, bssid = ##:##:##:##:##:##
I (71895666) wifi:security: WPA2-PSK, phy: bgn, rssi: -41
I (71895736) wifi:pm start, type: 1

I (71895736) wifi:set rx beacon pti, rx_bcn_pti: 0, bcn_timeout: 25000, mt_pti: 0, mt_time: 10000
I (71895746) wifi:<ba-add>idx:0 (ifx:0, ##:##:##:##:##:##), tid:6, ssn:1, winSize:64
I (71895856) wifi:AP's beacon interval = 102400 us, DTIM period = 1
I (71896116) wifi:state: run -> init (0x0)
I (71896116) wifi:pm stop, total sleep time: 175251 us / 373912 us

I (71896116) wifi:<ba-del>idx:0, tid:6
I (71896116) wifi:new:<5,0>, old:<5,0>, ap:<255,255>, sta:<5,0>, prof:1, snd_ch_cfg:0x0
I (71896186) wifi:flush txq
I (71896186) wifi:stop sw txq
I (71896186) wifi:lmac stop hw txq
```

Grepping the logs, this is occurring regularly, sometimes faster than others, but it looks like this is currently the main (only) restart triggering event:
```
I (71895116) stratum_api: Restarting System because of Error: recv
I (10640356) stratum_api: Restarting System because of Error: recv
I (38600286) stratum_api: Restarting System because of Error: recv
I (74402906) stratum_api: Restarting System because of Error: recv
I (1477196) stratum_api: Restarting System because of Error: recv
I (270716) stratum_api: Restarting System because of Error: recv
I (1688446) stratum_api: Restarting System because of Error: recv
I (25216) stratum_api: Restarting System because of Error: recv
I (153816) stratum_api: Restarting System because of Error: recv
```

From comment https://github.com/skot/ESP-Miner/issues/105#issuecomment-1948939767 this seems to be by design, as that looks like a similar trigger, but it could indeed be handled more elegantly.

BitAxe Supra 400 with firmware 2.1.8 on solo.ckpool.
