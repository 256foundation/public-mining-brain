# 256foundation/asic-rs pull request #165: test: add live auto-detect epic miner parse test

> Source: https://github.com/256foundation/asic-rs/pull/165
> Collected: 2026-10-07
> Published: 2026-03-10

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 165
- State: closed
- Author: cfilipescu
- Opened: 2026-03-10
- Closed: 2026-03-10
- Labels: none

## Description

## Summary
- add an ignored live integration test for the EPic v1 backend that reads `MINER_IP` from the environment
- auto-detect the miner backend/model using `MinerFactory::scan_miner(ip)` instead of hardcoding a model
- pretty-print live `MinerData` while clearing per-hashboard chip arrays to keep test output concise
