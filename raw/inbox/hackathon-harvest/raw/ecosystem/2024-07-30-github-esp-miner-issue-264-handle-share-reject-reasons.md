# bitaxeorg/ESP-Miner issue #264: Handle share reject reasons

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/264
> Collected: 2026-10-07
> Published: 2024-07-30

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 264
- State: closed
- Author: mutatrum
- Opened: 2024-07-30
- Closed: 2025-03-08
- Labels: enhancement, good first issue

## Description

It seems there is some confusion on the rejected shares. One way of making the user more informed would be to gather statistics on the reject reasons. F.e. number of stale shares, etc.

Unfortunately, error response is outside of the stratum api spec AFAIK, so there's no standard for a reject reason field. But with only limited pool implementations, a best effort implementation could capture more cases.

I've seen two formats:

ckpool:
```
{"reject-reason":"Stale","result":false,"error":null,"id":5333}
{"reject-reason":"Above target","result":false,"error":null,"id":8}
```

public pool:
```
{"id":120,"result":null,"error":[21,"Job not found",""]}
{"id":3423,"result":null,"error":[23,"Difficulty too low",""]}
```

Maybe there are other implementations, but these are the pools I've tested with so far.

These are also the different errors I encountered, so a small map with reason and counter would be sufficient.

## Comments

### Ondalf on 2024-08-07

https://github.com/tpfuemp/yiimp/blob/dev/stratum/client_core.cpp#L73
Yiimp pools replies as well with
```
{"id":integer,"result":false,"error":[integer,"string",null]}
error field being [error code, "error text", null]
```
"result":false comes from ckpool implementation. And this yiimp pools implementation goes back about 10 years.
But when presenting or collecting these errors, there was no documents for stratum-v1 to handle errors, which are caused by asicboost, so pools are reusing existing numbers but with different strings or adding more.
Theoretically, collecting strings would do alone as well just fine.
```
> {"method": "mining.submit", "params": ["donate", "cc", "00000000", "66b3e54a", "7f2f70a0"], "id":4}
< {"id":4,"result":false,"error":[26,"Low difficulty share",null]}
and valid share
> {"method": "mining.submit", "params": ["donate", "cd", "00000000", "66b3e588", "27b36bb0"], "id":4}
< {"id":4,"result":true,"error":null}
```
PS. Do not add "if too many rejects, force reboot" sort of implementation, since autoexchange pools WILL introduce job_id errors (stale shares) with even 1ms RTT, because how it works. When job_clear is set to true, miners should obey it, and not submit the stale to begin with. There are only handful of miners which actually checks, if new work was detected before sending result out... There are already plenty of miners, which doesn't obey job clear, and thus workarounds are introduced to stratums -.- (Basically sending "all good" towards miner even if it was stale to prevent reboot loop)
