# 256foundation/asic-rs pull request #184: fix(antminer): recognize BBCTRL control board alias

> Source: https://github.com/256foundation/asic-rs/pull/184
> Collected: 2026-10-07
> Published: 2026-03-17

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 184
- State: closed
- Author: cfilipescu
- Opened: 2026-03-17
- Closed: 2026-03-17
- Labels: none

## Description

## Summary
- add `BBCTRL` as an accepted alias when parsing Antminer control board model names.
- map this alias to `BeagleBoneBlack` to improve control board detection compatibility.
