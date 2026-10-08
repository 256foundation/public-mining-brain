# bitaxeorg/ESP-Miner issue #219: Shares accepted stops updating after ~32k shares

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/219
> Collected: 2026-10-07
> Published: 2024-06-12

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 219
- State: closed
- Author: mutatrum
- Opened: 2024-06-12
- Closed: 2024-06-25
- Labels: bug

## Description

Number of shares is stale, but work is submitted to pool. Both the display on the device as well as the dashboard are not updating the number of shares, after ~30 hours. When checking the statistics from the pool, shares are accepted.

It stays stuck at 32733 shares. When trying to pinpoint this in the logs, I don't see any specific error, but I do see something that happened after result id 32768 (power of 2 alert!):

```I (120841736) asic_result: Nonce difficulty 662.33 of 538.
I (120841736) stratum_api: tx: {"id": 32767, "method": "mining.submit", "params": ["bc1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq.bitaxe", "648516380010f352", "9907000000000000", "6668f8eb", "b9120e84", "0001a000"]}

I (120841886) stratum_task: rx: {"result":true,"error":null,"id":32767}
I (120841886) stratum_task: message result accepted
I (120842366) bm1368Module: Job ID: 94
I (120842376) bm1368Module: RX Job ID: 48
I (120842376) asic_result: Nonce difficulty 308.15 of 538.
I (120843406) bm1368Module: Job ID: 14
I (120843406) bm1368Module: RX Job ID: 08
I (120843406) asic_result: Nonce difficulty 511.33 of 538.
I (120846436) bm1368Module: Job ID: E9
I (120846436) bm1368Module: RX Job ID: 70
I (120846436) asic_result: Nonce difficulty 1842.28 of 538.
I (120846436) stratum_api: tx: {"id": 32768, "method": "mining.submit", "params": ["bc1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq.bitaxe", "648516380010f352", "6f09000000000000", "6668f8eb", "11d60d3c", "00012000"]}

I (120846596) stratum_task: rx: {"result":true,"error":null,"id":32768}
I (120846596) stratum_task: setup message accepted
I (120848746) bm1368Module: Job ID: 3C
I (120848746) bm1368Module: RX Job ID: 18
I (120848746) asic_result: Nonce difficulty 1797.40 of 538.
I (120848756) stratum_api: tx: {"id": 32769, "method": "mining.submit", "params": ["bc1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq.bitaxe", "648516380010f352", "560a000000000000", "6668f8eb", "02ab1872", "00018000"]}

I (120848956) stratum_task: rx: {"result":true,"error":null,"id":32769}
I (120848956) stratum_task: setup message accepted
I (120851066) bm1368Module: Job ID: BB
I (120851066) bm1368Module: RX Job ID: 58
I (120851066) asic_result: Nonce difficulty 22913.00 of 538.
I (120851066) stratum_api: tx: {"id": 32770, "method": "mining.submit", "params": ["bc1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq.bitaxe", "648516380010f352", "3e0b000000000000", "6668f8eb", "fa7f0122", "00016000"]}
```

Instead of 'message result accepted' it now says 'setup message accepted'. After this point, it never logs 'message result accepted' again. When cross-checking with the API data, I can see that this was the point where it stops updating the shares accepted (all other fields cut):
```
{"sharesAccepted":32728, "uptimeSeconds":120823}
{"sharesAccepted":32733, "uptimeSeconds":120883}
```

Running BitAxe Supra 400 with firmware 2.1.8 on ckpool.

## Comments

### skot on 2024-06-12

Nice catch. You're right this definitely seems like a signed 16 bit int rolling over. I'll check it out asap. Thanks!

### kakawlala on 2024-06-16

After observing that the device counter reached 327XX, it got stuck. However, after a day, some devices restored the counter and reached 4XXXX without rebooting.

![Screenshot_20240617-004947_Chrome_1](https://github.com/skot/ESP-Miner/assets/89348834/ee1e12e7-e7a1-4cad-81fb-cc1417c71371)



### mutatrum on 2024-06-17

I can confirm, after another 32k shares, it continues counting up. It got stuck at 32730 accepted shares, with an uptimeSeconds of 107412 and it continued counting on uptimeSeconds 209531, so approx. 2x the uptime. It didn't go to 64k, it continued where it left of, basically not showing the 32k not updated shares.

### kakawlala on 2024-06-17

Yes, I observe that if they stop at 327XX, they will continue to accumulate after a period of time until 655XX stops again. I will continue to observe whether 655XX continues to accumulate after a period of time.

![Screenshot_20240618-200330_Chrome](https://github.com/skot/ESP-Miner/assets/89348834/f375baf2-b4fb-4760-95d6-0c5fa953124c)


### mutatrum on 2024-06-20

Ok, that didn't go as I expected. It sat at 65470 for the same period, then continued going up for a few minutes and wrapped around to 0:
```
 {"sharesAccepted":65470, "date":"2024-06-19T21:04:01Z"},
 {"sharesAccepted":65470, "date":"2024-06-19T21:05:02Z"},
 {"sharesAccepted":65470, "date":"2024-06-19T21:06:01Z"},
 {"sharesAccepted":65470, "date":"2024-06-19T21:07:01Z"},
 {"sharesAccepted":65470, "date":"2024-06-19T21:08:02Z"},
 {"sharesAccepted":65470, "date":"2024-06-19T21:09:01Z"},
 {"sharesAccepted":65488, "date":"2024-06-19T21:10:01Z"},
 {"sharesAccepted":65504, "date":"2024-06-19T21:11:02Z"},
 {"sharesAccepted":65524, "date":"2024-06-19T21:12:01Z"},
 {"sharesAccepted":9, "date":"2024-06-19T21:13:01Z",
 {"sharesAccepted":19, "date":"2024-06-19T21:14:02Z",
 {"sharesAccepted":34, "date":"2024-06-19T21:15:01Z",
 {"sharesAccepted":53, "date":"2024-06-19T21:16:01Z"},
```
Maybe there's a second overflow bug somewhere?

This is the highest uptime I have ever seen btw, 5d 9h and counting!

### mutatrum on 2024-06-25

Running above PR. Now we wait.

### WantClue on 2024-06-25

65535 should be the highest 16bit number and is a good catch. I'll merge that change to a 64bit
