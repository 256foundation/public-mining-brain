# bitaxeorg/ESP-Miner issue #1458: Allow to turn off mining via AxeOS

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1458
> Collected: 2026-10-07
> Published: 2025-12-15

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1458
- State: closed
- Author: luisschwab
- Opened: 2025-12-15
- Closed: 2025-12-16
- Labels: none

## Description

It would be nice to be able to turn off mining whilst keeping the BitAxe on.

A button on AxeOS would suffice, along with a REST endpoint for integration with external services.

## Comments

### Painerman on 2025-12-15

I'd add a scheduled on/off feature. This will come in handy when devices become more powerful and energy-intensive. So, I'll mine at night, when it's cheaper, automatically! =)

### mutatrum on 2025-12-15

Duplicate of #734 

As for schedule, this needs to be done externally, as the Bitaxe doesn't know what time it is. For a discussion on why this, see #601
