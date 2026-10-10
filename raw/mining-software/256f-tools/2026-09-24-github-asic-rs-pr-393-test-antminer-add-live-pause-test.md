# 256foundation/asic-rs pull request #393: test(antminer): add live pause test

> Source: https://github.com/256foundation/asic-rs/pull/393
> Collected: 2026-10-07
> Published: 2026-09-24

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 393
- State: closed
- Author: cfilipescu
- Opened: 2026-09-24
- Closed: 2026-09-24
- Labels: none

## Description

## Summary
- Add an ignored live AntMiner pause test using `MINER_IP` and firmware auto-detection.
- Print pause success, hashrate, mining/operating state, and raw summary hashrate fields after the request.

## Validation
- `git diff --check` passed.
- The live test requires a miner and is ignored by default. A prior run against the stock T21 received an empty response from `set_miner_conf`; it printed the follow-up diagnostics and failed, documenting the current HTTP pause issue.
