# bitaxeorg/ESP-Miner issue #314: Add current pool minimum difficulty to AxeOS dashboard

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/314
> Collected: 2026-10-07
> Published: 2024-08-30

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 314
- State: closed
- Author: skot
- Opened: 2024-08-30
- Closed: 2025-10-21
- Labels: enhancement, help wanted, good first issue

## Description

It would be cool to show the current pool minimum difficulty somewhere on the AxeOS dashboard. Maybe even show the accepted share _rate_ too.

## Comments

### WantClue on 2024-09-02

I'm also add that the pool diff is being used for the asic and not the hard coded one 

### skot on 2024-09-02

We should keep the ASIC difficulty (ticket mask) at a static value, much lower than the pool difficulty.

### remcoros on 2024-10-11

If this gets added to 'api/system/info', May I suggest to use a number and not a string, so it plays nice with prometheus scrapers
