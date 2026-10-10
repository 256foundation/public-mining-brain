# 256foundation/asic-rs pull request #343: fix(antminer): update stock firmware bundles

> Source: https://github.com/256foundation/asic-rs/pull/343
> Collected: 2026-10-07
> Published: 2026-08-26

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 343
- State: closed
- Author: cfilipescu
- Opened: 2026-08-26
- Closed: 2026-08-26
- Labels: none

## Description

## Summary

- fetch a Digest challenge before starting an Antminer firmware upload
- authorize the streaming multipart request directly instead of passing it through the diqwest clone-based challenge flow
- allow an exact control-board subtype match when older stock firmware reports a generic miner model
- cover both v2020 and v2023_07 Antminer backends
- add regression coverage for upload authorization and generic-model BMU selection

## Root causes

Reqwest represents multipart bodies as streams, so their request builders are not cloneable. send_digest_auth clones the request builder before sending its initial request, causing every firmware upload to fail before any bytes reach the miner.

Some older stock firmware reports a generic miner_type such as Antminer BHB42XXX while its official BMU bundle identifies the product as Antminer S19j Pro. The resolver previously rejected the bundle before considering the exact AMLCtrl_BHB42XXX subtype match.

## Validation

- cargo +1.95.0 test --package asic-rs-firmwares-antminer --lib
- cargo +1.95.0 clippy --package asic-rs-firmwares-antminer --all-targets -- -D warnings
