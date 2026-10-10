# 256foundation/asic-rs pull request #306: Derive EPic coin from model hash algorithm

> Source: https://github.com/256foundation/asic-rs/pull/306
> Collected: 2026-10-07
> Published: 2026-06-30

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 306
- State: closed
- Author: cfilipescu
- Opened: 2026-06-30
- Closed: 2026-06-30
- Labels: none

## Description

## Summary
- add MinerModel::hash_algorithm with SHA256 default
- mark VolcMiner models as Scrypt and detect them in EPic PowerPlay
- derive EPic pool coin from the backend device algorithm
- add ignored live test for EPic pool config writes

## Tests
- cargo test -p asic-rs-firmwares-epic
- cargo test -p asic-rs-makes-volcminer
