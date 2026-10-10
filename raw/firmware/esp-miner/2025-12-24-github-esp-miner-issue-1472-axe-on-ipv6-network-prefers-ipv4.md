# bitaxeorg/ESP-Miner issue #1472: Axe on IPv6 network prefers ipv4

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1472
> Collected: 2026-10-07
> Published: 2025-12-24

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1472
- State: open
- Author: 0xf0xx0
- Opened: 2025-12-24
- Closed: n/a
- Labels: question

## Description

**Describe the bug**
An axe running on an ipv6 enabled network should prefer ipv6 when resolving hosts, but instead prefers ipv4. this can be seen with ckpool and atlaspool.

**To Reproduce**
Steps to reproduce the behavior:
1. configure an ipv6-enabled pool
2. open the logs 
3. restart your axe
4. when it resolves the domain, itll be the ipv4

**Expected behavior**
ipv6 should be preferred when available.


**Hardware:**
 - ESP-Miner FW version: master
 - Pool URL, Port: solo.atlaspool.io:4333

**Additional context**

```
I (18525) stratum_task: Resolved solo.atlaspool.io:4333 → 166.117.239.148
I (18526) stratum_task: Connecting to: stratum+tcp://solo.atlaspool.io:4333 (166.117.239.148)
```

## Comments

### mutatrum on 2025-12-27

I'm not sure if expected behavior is what we want. Maybe it should be a use choice?

### 0xf0xx0 on 2025-12-27

maybe default ipv6-preferred with an option to prefer ipv4? the expectation on ipv6 enabled networks is everything that supports ipv6 will use it, and ipv4 is the fallback.

### WantClue on 2025-12-28

This would be accaptable I guess. We always should preffer ipv4 imo for the sake of a clean process. But indeed if the bitaxe itself can optain an ipv6 address this should be proof that the network utilizes ipv6 and then we can prefer ipv6

### WantClue on 2026-03-31

The issue here is that IPv6 is required on the entire chain from the bitaxe to the pool. If anything in between does not meet it it will prefer ipv4. Also for the testing of ipv6 i used solo6.ckpool becuase this is a straight ipv6 DNS record and I don't know if this is the case for atlaspool with one record for everything so ipv4 will very likely be used there.

### WantClue on 2026-03-31

A potential solution would be to let the user decide what should be preferred but TBH i don't wanna write that :D 

### ffrediani on 2026-08-03

The user should not need to choose this and IPv6 should always be the preffered option when available.
This is the defaut behavior for any modern Operating System.

There is no harm at all to be like that and avoids that communication to go via IPv4 which sometimes have to pass via more than one NAT (in the user's router and sometimes in the CGNAT in the ISP). This is unecessary and users should always have their devices communicating via IPv6 whenever it is available.

IPv6 is the default internet protocol and IPv4 is legacy.
