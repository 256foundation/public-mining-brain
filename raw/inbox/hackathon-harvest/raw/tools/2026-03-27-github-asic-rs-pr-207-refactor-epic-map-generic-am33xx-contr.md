# 256foundation/asic-rs pull request #207: refactor(epic): map Generic AM33XX control boards correctly to BeagleBoneBlack

> Source: https://github.com/256foundation/asic-rs/pull/207
> Collected: 2026-10-07
> Published: 2026-03-27

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 207
- State: closed
- Author: cfilipescu
- Opened: 2026-03-27
- Closed: 2026-03-27
- Labels: none

## Description

## Summary
- map `GENERIC AM33XX` board identifiers to `BeagleBoneBlack` in ePIC v1 control board detection.
- prevent these boards from falling back to `EPicUMC` when parsing control board versions.
