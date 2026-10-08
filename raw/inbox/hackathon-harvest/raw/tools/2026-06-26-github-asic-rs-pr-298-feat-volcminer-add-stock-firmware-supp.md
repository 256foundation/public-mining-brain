# 256foundation/asic-rs pull request #298: feat(volcminer): add stock firmware support

> Source: https://github.com/256foundation/asic-rs/pull/298
> Collected: 2026-10-07
> Published: 2026-06-26

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 298
- State: closed
- Author: cfilipescu
- Opened: 2026-06-26
- Closed: 2026-06-29
- Labels: none

## Description

## Summary
- add VolcMiner make metadata and stock firmware backend
- support discovery, status telemetry, pool config read/write, fans, temperatures, hashrate, and runtime pools over the web CGI interface
- add ignored live tests for reading data and writing a three-pool LTC config via MINER_IP / MINER_PASSWORD

## Verification
- cargo test -p asic-rs-firmwares-volcminer -p asic-rs-makes-volcminer
- cargo clippy
- cargo check --all-features
