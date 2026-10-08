# 256foundation/mujina pull request #76: feat: native Windows support for Bitaxe mining

> Source: https://github.com/256foundation/mujina/pull/76
> Collected: 2026-10-07
> Published: 2026-07-05

- Repository: 256foundation/mujina
- Type: pull request
- Number: 76
- State: open
- Author: IxTechCrypto
- Opened: 2026-07-05
- Closed: n/a
- Labels: none

## Description

Adds native Windows support so Mujina can drive a Bitaxe over USB on Windows, plus two related fixes.

Windows transport: COM-port discovery + interface ordering, a tokio-serial SerialStream mirroring the Unix serial API, cfg wiring, and Ctrl-C shutdown handling.
Chip discovery: wait 500ms after ASIC reset and retry BM1370 discovery up to 5× so a cold board doesn't fail with "no chips discovered".
Frequency telemetry: new frequency_mhz field on BoardTelemetry exposing the 525 MHz clock.
Tested on Windows 11 with a Bitaxe Gamma (BM1370): mines end-to-end at ~1.25 TH/s, submits shares, serves the REST API. cargo fmt --check, cargo clippy --release -- -D warnings, and cargo test pass on each commit. Supersedes the stale #75.

Shoutout to @aadhi1014 for his work on #75 and getting us 80% there

## Comments

### rkuester on 2026-07-06

Hey @IxTechCrypto, this is great! I'll take a look shortly.
