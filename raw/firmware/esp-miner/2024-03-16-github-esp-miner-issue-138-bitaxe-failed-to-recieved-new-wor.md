# bitaxeorg/ESP-Miner issue #138: Bitaxe failed to recieved New-Work after WAN-IP-Change (no WAN-IP for e.g. 120s) - Watchdog? - Bug?

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/138
> Collected: 2026-10-07
> Published: 2024-03-16

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 138
- State: closed
- Author: seepv
- Opened: 2024-03-16
- Closed: 2024-04-05
- Labels: bug, enhancement

## Description

If the router get's a new IP from a Internet-Provider the Bitaxe failed to reconect for new work.

The same ocured after an OpenWRT-Router-Restart.

Is this a AxeOS or a Firmware Bug?

Is there e.g. a watchdog somewere (in AxeOS or Firmware) that resets the Bitaxe if recieving or submitting found Blocks failed for a certain time?

Bitaxe 204; AxeOS v2.1.1

## Comments

### seepv on 2024-03-17

@skot - If for e.g. the WAN-IP changes, the mining subscribtion expires and
without a new mining subscribtion, the Bitaxe keeps 'hashing' in a loop with old data.
That's what's going on - or am I wrong?

### skot on 2024-03-17

The firmware can generate a lot of work by rolling extranonce. But we should notice the server is no longer connected pretty soon when attempting to submit a share.
