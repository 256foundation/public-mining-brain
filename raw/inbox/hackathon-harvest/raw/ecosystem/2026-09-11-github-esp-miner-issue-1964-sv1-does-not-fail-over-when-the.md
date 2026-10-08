# bitaxeorg/ESP-Miner issue #1964: SV1 does not fail over when the primary pool stays connected but stops replying

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1964
> Collected: 2026-10-07
> Published: 2026-09-11

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1964
- State: open
- Author: johnny9
- Opened: 2026-09-11
- Closed: n/a
- Labels: none

## Description

On Gamma-02 running firmware `ede6c13` (PR #1962 CI build), mining remained on primary after it stopped sending Stratum replies and jobs. The fallback pool remained available.

Steps to reproduce:

1. Configure working primary and fallback pools.
2. Confirm accepted shares on primary.
3. Stop primary’s Stratum replies and jobs while keeping its TCP connection open.
4. Leave fallback running.

During 180 seconds, the miner sent 154 unanswered requests. Accepted shares stayed at six, primary remained selected, and fallback received no connection. Normal failover when primary disconnects passes.

`esp_transport_read()` returns `0` on timeout, but `STRATUM_V1_receive_jsonrpc_line()` only exits on negative results. It repeats zero-result reads indefinitely, preventing the retry/failover logic from running. A native reproduction remained in this loop through 20 simulated minutes.

This code is unchanged by #1962 and #1957.

Expected behavior: an overall inactivity deadline should return a connection failure, allowing the existing retry and fallback logic to run. Short gaps between messages should remain valid.
