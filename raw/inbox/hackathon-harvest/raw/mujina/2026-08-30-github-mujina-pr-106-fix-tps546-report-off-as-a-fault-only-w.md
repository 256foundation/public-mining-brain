# 256foundation/mujina pull request #106: fix(tps546): report OFF as a fault only when the output is on

> Source: https://github.com/256foundation/mujina/pull/106
> Collected: 2026-10-07
> Published: 2026-08-30

- Repository: 256foundation/mujina
- Type: pull request
- Number: 106
- State: closed
- Author: rkuester
- Opened: 2026-08-30
- Closed: 2026-08-30
- Labels: none

## Description

The chip sets OFF whenever the output is off, including when commanded off, so the status check logged a critical fault whenever the board monitor polled while the rail was intentionally off. Count OFF as a fault only while OPERATION is on. Verified on a Bitaxe Gamma.
