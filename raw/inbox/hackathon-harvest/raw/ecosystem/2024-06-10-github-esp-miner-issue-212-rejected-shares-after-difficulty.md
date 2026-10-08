# bitaxeorg/ESP-Miner issue #212: rejected shares after difficulty change on ckpool

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/212
> Collected: 2026-10-07
> Published: 2024-06-10

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 212
- State: closed
- Author: mutatrum
- Opened: 2024-06-10
- Closed: 2025-01-27
- Labels: wontfix

## Description

Running a BitAxe Supra (400), firmware 2.1.8 on solo.ckpool.org.

After startup, initial stratum difficulty is 10000. It takes a fair bit of time to find a handful of shares. After this, the difficulty is adjusted downwards, but this results in a batch of rejected shares, with an error message of 'Above target'.
[bitaxe2.log](https://github.com/user-attachments/files/15775643/bitaxe2.log)

## Comments

### skot on 2024-06-10

rejecting work after _they_ lowered the difficulty really seems like a ckpool bug. The developer has been notified, but we haven't gotten a response, afaik. 

```
I (381191) stratum_task: rx: {"params":[398],"id":null,"method":"mining.set_difficulty"}
I (381191) stratum_task: Set stratum difficulty: 398
I (381201) stratum_task: rx: {"result":true,"error":null,"id":9}
I (381201) stratum_task: message result accepted
I (381291) bm1368Module: Job ID: A3
I (381291) bm1368Module: RX Job ID: 50
I (381291) asic_result: Nonce difficulty 757.35 of 10000.
I (383461) bm1368Module: Job ID: 57
I (383471) bm1368Module: RX Job ID: 28
I (383471) asic_result: Nonce difficulty 506.16 of 10000.
I (393681) stratum_task: rx: {"params":["648516380010e299","90ab7ca18a009bb20b05e8dfa5b5688bf717b076000070410000000000000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff350301ee0c0004ba18676604a1ab11160c","0a636b706f6f6c112f736f6c6f2e636b706f6f6c2e6f72672fffffffff037b11c9140000000016001480bded37e3f86a1a546e099b15e2b02855d3843cdd976c000000000016001451ed61d2f6aa260cc72cdf743e4e436a82c010270000000000000000266a24aa21a9ed509253c2c42d27c26dcbb540cf71f9ca7ff4e1777ed513ccefda80dec886885100000000",["8c299541de94a07e5b27f7c50d4835bf77cf75789042c6ec4c5ae7345e821d31","173abf20a4f11aaa1850679b1117e0b3497bf9e76030cee150fbb8b2f2f1f019","01fe12b0401efa90494beaaece8b387bc89f697dee8104cdafe3c4725bed7bf6","07b4a76b49c36165c9aa3510cd9629a00c6ffbad075b4beeee92b0b12760f763","29a624e985273cb00fea48675be395f5daa0a48ab7b324056a8fbd6e97bde1a6","46979615d1a33db96d76fcbf1d2bd26d660dc940b1b4df4fbb9206c7f4a1de5b","625ae540510a9007be34731c2cc6f4cd98a4cd2b25fab6bf85961b0447ce8964","b367ee622207571ddd708f99bccd06f674f5116618864650c3aa5015a356a67e","a52f313ca0ef691b33be42cf0ce301970f0d062bc05bf6679f3baacc890fea00","e7462bc6a30bec58be50dfdf5c2a973baaed26096ca38c3935f641a7bc10ecf4","f737fc1c2a3ba149adea4da799f0f7b8c37d3ac9da665f7adf340fa619305bcd","fde435cdba35eb4d6017f89d19886200bcff14b4c52ebe26e445abdc0700ccdc"],"20000000","17035cb8","666718ba",false],"id":null,"method":"mining.notify"}
I (393811) create_jobs_task: New Work Dequeued 648516380010e299
I (393831) bm1368Module: Job ID: 92
I (393831) bm1368Module: RX Job ID: 48
I (393831) asic_result: Nonce difficulty 1872.60 of 10000.
I (393941) ASIC_task: New pool difficulty 398
I (397101) bm1368Module: Job ID: EB
I (397101) bm1368Module: RX Job ID: 70
I (397101) asic_result: Nonce difficulty 581.89 of 398.
I (397101) stratum_api: tx: {"id": 10, "method": "mining.submit", "params": ["bc1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq.bitaxe", "648516380010e299", "3b01000000000000", "666718ba", "0c7e4366", "00016000"]}
I (397261) stratum_task: rx: {"reject-reason":"Above target","result":false,"error":null,"id":10}
E (397271) stratum_task: message result rejected
I (397581) bm1368Module: Job ID: 14
I (397591) bm1368Module: RX Job ID: 08
I (397591) asic_result: Nonce difficulty 291.87 of 398.
I (397931) bm1368Module: Job ID: A5
I (397941) bm1368Module: RX Job ID: 50
I (397941) asic_result: Nonce difficulty 611.18 of 398.
I (397941) stratum_api: tx: {"id": 11, "method": "mining.submit", "params": ["bc1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq.bitaxe", "648516380010e299", "8f01000000000000", "666718ba", "f3f92a56", "0000a000"]}
I (398081) stratum_task: rx: {"reject-reason":"Above target","result":false,"error":null,"id":11}
```

### skot on 2024-06-10

I removed some info about another unrelated bug (#199) so we can focus on this ckpool difficulty adjustment issue.

### skot on 2024-06-10

I'm pretty sure I have seen this same issue last year where ckpool lowers the difficulty, and then doesn't start accepting shares with that new lower difficulty until the _next_ mining.notify

I think this is a bug in ckpool, but it's mostly superficial as it doesn't affect your mining in any way.

### kakawlala on 2024-06-10

pool.vkbit.com also has a default difficulty of 10,000.  But currently the hash calculation appears to be local instead of waiting for the pool to feed back.  This is helpful.  I know it's working and the difficulty eases off after a while.  Although I get some rejected parts.  But when connected for a long time, the rejected part is less than 1%

This is the data of supra401 running on pool.vkbit.com for 43 hours（2.1.8.bin）
![Screenshot_20240611-035632_Chrome](https://github.com/skot/ESP-Miner/assets/89348834/3d3565a0-ebe1-490e-93fe-4893a902c06a)


### skot on 2024-06-10

vkbit is a ckpool clone, so I suspect it will have this same issue.

### mutatrum on 2024-06-11

I have it running now for ~18 hours, it looks like ckpool only requests a new difficulty once, a few minutes after start of the BitAxe. The only rejected shares (12 in my case) were from that initial ramp down, after that no rejected shares. So for ckpool the impact is minor indeed.

### skot on 2024-06-11

removed the bug tag. afaik this isn't something we can fix on the esp-miner side.
