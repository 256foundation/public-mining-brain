# 256foundation/asic-rs pull request #301: fix(is-mining): ensure `is_mining` represents a paused state rather than hashrate

> Source: https://github.com/256foundation/asic-rs/pull/301
> Collected: 2026-10-07
> Published: 2026-06-29

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 301
- State: closed
- Author: b-rowan
- Opened: 2026-06-29
- Closed: 2026-06-30
- Labels: none

## Description

`is_mining` should represent whether the miner is paused or not, rather than just checking if hashrate is 0.

A good example of this is for a watchdog, the watchdog should check the hashrate of the miner, and if it is bad, it should restart it, UNLESS the miner is paused by the user.

## Comments

### cfilipescu on 2026-06-29

you forgot epic firmware. it has the same logic
