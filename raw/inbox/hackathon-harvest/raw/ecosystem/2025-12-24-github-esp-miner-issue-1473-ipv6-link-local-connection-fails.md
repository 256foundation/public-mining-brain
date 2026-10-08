# bitaxeorg/ESP-Miner issue #1473: Ipv6 link-local connection fails

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1473
> Collected: 2026-10-07
> Published: 2025-12-24

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1473
- State: open
- Author: 0xf0xx0
- Opened: 2025-12-24
- Closed: n/a
- Labels: none

## Description

**Describe the bug**
Link-local ips resolve correctly, but fail when trying to open the connection.

**To Reproduce**
Steps to reproduce the behavior:
1. Configure a pool to listen on a link local address (unsure about others, pogolo will do it)
2. configure your axe to connect to it
3. watch logs
4. See error

**Expected behavior**
the connection should succeed.

**Hardware:**
 - ESP-Miner FW version: master
 - Pool URL, Port: `fe80::9a48:27ff:fe60:d3a1`, `5662`

**Additional context**

```
I (15441) stratum_task: Opening connection to pool: fe80::9a48:27ff:fe60:d3a1:5661
I (15441) stratum_task: Starting heartbeat thread for primary pool: fe80::9a48:27ff:fe60:d3a1:5661
I (15456) create_jobs_task: ASIC Job Interval: 500 ms
I (15465) create_jobs_task: ASIC Ready!
W (15466) stratum_task: Link-local IPv6 address without scope ID - attempting to set from WiFi STA interface
I (15474) statistics_task: Starting
I (15480) stratum_task: Set IPv6 scope_id to interface index: 2
I (15491) stratum_task: Resolved fe80::9a48:27ff:fe60:d3a1:5661 → FE80::9A48:27FF:FE60:D3A1%2
I (15474) main_task: Returned from app_main()
I (15500) stratum_task: Connecting to: stratum+tcp://fe80::9a48:27ff:fe60:d3a1:5661 (FE80::9A48:27FF:FE60:D3A1%2)
I (15516) stratum_api: TLS disabled, Using TCP transport
I (15522) stratum_task: Transport initialized, connecting to fe80::9a48:27ff:fe60:d3a1:5661
E (15544) esp-tls: [sock=42] connect() error: Host is unreachable
E (15545) transport_base: Failed to open a new connection: 32772
E (15547) stratum_task: Transport unable to connect to fe80::9a48:27ff:fe60:d3a1:5661 (errno -1). Attempt: 1
```
