# bitaxeorg/ESP-Miner issue #823: NerdAxe Fehler

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/823
> Collected: 2026-10-07
> Published: 2025-04-05

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 823
- State: closed
- Author: Pxxtzi
- Opened: 2025-04-05
- Closed: 2025-04-06
- Labels: none

## Description

on the Nerdaxe under Logs: Realtime logs.

I keep getting these errors: (i have 2 of them, both have these errors)

(901383) create_jobs_task: New Work Dequeued 67f0c3d54cc09503
(902173) esp-tls: couldn't get hostname for :api.coindesk.com: getaddrinfo() returns 202, addrinfo=0x0
(902173) transport_base: Failed to open a new connection: 32769
(902183) HTTP_CLIENT: Connection failed, sock < 0
(902183) HTTP: HTTP GET request failed: ESP_ERR_HTTP_CONNECT
(902513) bm1366Module: Job ID: 18, Core: 41/6, Ver: 0A20C000
(902523) asic_result: Ver: 2A20C000 Nonce 58360152 diff 262.7 of 131072.
(903093) bm1366Module: Job ID: 18, Core: 13/2, Ver: 0F4D4000
(903103) asic_result: Ver: 2F4D4000 Nonce DD59011A diff 1526.1 of 131072.
(903833) bm1366Module: Job ID: 20, Core: 13/3, Ver: 04056000
(903833) asic_result: Ver: 24056000 Nonce 12B0011A diff 559.1 of 131072.
(904333) bm1366Module: Job ID: 20, Core: 99/1, Ver: 08812000
(904333) asic_result: Ver: 28812000 Nonce F72603C6 diff 501.2 of 131072.
(906093) bm1366Module: Job ID: 28, Core: 87/1, Ver: 065A2000
(906093) asic_result: Ver: 265A2000 Nonce 636D03AE diff 366.1 of 131072.
(906763) bm1366Module: Job ID: 28, Core: 9/7, Ver: 0C63E000
(906773) asic_result: Ver: 2C63E000 Nonce C7A00012 diff 761.9 of 131072.
(907253) esp-tls: couldn't get hostname for :api.coindesk.com: getaddrinfo() returns 202, addrinfo=0x0
(907263) transport_base: Failed to open a new connection: 32769
(907263) HTTP_CLIENT: Connection failed, sock < 0
(907273) HTTP: HTTP GET request failed: ESP_ERR_HTTP_CONNECT



## Comments

### mutatrum on 2025-04-06

The NerdAxe is a different device, with a fork of the software. You can open an issue here: https://github.com/BitMaker-hub/NerdAxe
