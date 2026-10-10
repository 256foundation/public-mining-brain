# bitaxeorg/ESP-Miner issue #696: Can't connect to pool with just IP address

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/696
> Collected: 2026-10-07
> Published: 2025-02-10

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 696
- State: closed
- Author: Sjors
- Opened: 2025-02-10
- Closed: 2025-02-10
- Labels: bug, accepted

## Description

I'm sometimes testing (SRI) pool stuff locally, and prefer to use the IP address over a hostname.

This fails and falls back to the backup pool. Probably because it insists on resolving via DNS:

```
₿ (18021) stratum_task: Trying to get IP for URL: 192.168.x.x
```

If I use the `blah.localhost` hostname instead it works fine.


Running AxeOS v2.5.1


## Comments

### skot on 2025-02-10

oh wow, this definitely _used_ to work. I'll check it out!

### eandersson on 2025-02-10

I still use IP and it works fine for me on 2.5.1.

```
₿ (24211) stratum_task: Trying to get IP for URL: 10.0.1.100
₿ (24221) ASIC_task: ASIC Ready!
₿ (24231) stratum_task: Connecting to: stratum+tcp://10.0.1.100:3334 (10.0.1.100)
₿ (24211) main_task: Returned from app_main()
₿ (24241) stratum_task: Socket created, connecting to 10.0.1.100:3334
```

We would need additional log lines to better understand the issue.

For reference we just resolve the host you provide using `gethostbyname` which should have no problem supporting an IP address.

### skot on 2025-02-10

IP directly worked for me on v2.5.1 and v2.6.0b1
```
₿ (13463) stratum_task: Trying to get IP for URL: 192.168.1.113
₿ (13473) ASIC_task: ASIC Job Interval: 2000.00 ms
₿ (13473) stratum_task: Connecting to: stratum+tcp://192.168.1.113:3333 (192.168.1.113)
₿ (13473) ASIC_task: ASIC Ready!
₿ (13463) stratum_task: Starting heartbeat thread for primary endpoint: 192.168.1.113
₿ (13493) stratum_task: Socket created, connecting to 192.168.1.113:3333
₿ (13473) main_task: Returned from app_main()
```

### Sjors on 2025-02-10

Never mind, I can't reproduce this anymore - indeed connecting to the same IP works fine now. Maybe something else was going wrong in parallel.

### eandersson on 2025-02-10

I opened a PR to clean up that log message a bit as it is very confusing.
https://github.com/skot/ESP-Miner/pull/697/files
