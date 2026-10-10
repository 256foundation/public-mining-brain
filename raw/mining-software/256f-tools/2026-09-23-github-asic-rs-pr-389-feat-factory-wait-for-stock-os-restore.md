# 256foundation/asic-rs pull request #389: feat(factory): wait for stock OS restore

> Source: https://github.com/256foundation/asic-rs/pull/389
> Collected: 2026-10-07
> Published: 2026-09-23

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 389
- State: closed
- Author: Erisli
- Opened: 2026-09-23
- Closed: 2026-09-24
- Labels: none

## Description

right now the restore_stock_os doesn't verify whether stock comes back online. Added a new command 

## Summary
- Add MinerFactory::get_stock_miner(ip) to identify only stock firmware at a specific IP.
- Add restore_stock_os_and_wait(miner, timeout_secs, rescan_interval_secs).
- After the restore request is accepted, poll only the original IP until stock firmware is identifiable.
- Return a clear timeout error when stock firmware does not return at that IP, including the possibility that the IP changed.

## Comments

### Erisli on 2026-09-24

decided to close this pr as I was looking through the architecture, and feel like the feature of ```waiting for stock to come back online``` shouldn't be in here. 

Miner trait doesnt have knownldge to MinerFactory, nor it should. If we leave the ```restore_stock_os_and_wait``` in Miners, that means we would need to create a new Miner instance in order to constrain it to stock, and in order to detect whether its a stock miner.

```waiting for stock to come back online``` should be handled by external callsites as its more flexible and concepturally more correct.
