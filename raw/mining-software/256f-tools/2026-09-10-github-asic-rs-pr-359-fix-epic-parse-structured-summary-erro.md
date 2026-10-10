# 256foundation/asic-rs pull request #359: fix(epic): parse structured summary errors

> Source: https://github.com/256foundation/asic-rs/pull/359
> Collected: 2026-10-07
> Published: 2026-09-10

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 359
- State: closed
- Author: cfilipescu
- Opened: 2026-09-10
- Closed: 2026-09-10
- Labels: none

## Description

## Summary

- parse object-shaped Status.Last Error values returned by PowerPlay into miner messages
- preserve support for legacy plain-string and JSON-encoded errors
- ignore null and empty last-error values
- add regression coverage for each response shape

## Root cause

PowerPlay v1.24 returns Last Error as an externally tagged JSON object, for example {"NoHashboardsEnabled":"no hashboards enabled"}. The existing parser called Value::as_str, which discarded object-shaped errors and left messages empty.

## Testing

- cargo test -p asic-rs-firmwares-epic
- cargo clippy -p asic-rs-firmwares-epic --all-targets -- -D warnings
- MINER_IP=<miner-ip> cargo test parse_data_live_test_auto_detect -p asic-rs-firmwares-epic -- --ignored --nocapture (live PowerPlay v1.24 miner; message populated as "no hashboards enabled")
