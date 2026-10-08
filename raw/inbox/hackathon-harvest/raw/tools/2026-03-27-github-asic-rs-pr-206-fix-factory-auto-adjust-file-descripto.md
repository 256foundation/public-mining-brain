# 256foundation/asic-rs pull request #206: fix(factory): auto-adjust file descriptor limits before scans

> Source: https://github.com/256foundation/asic-rs/pull/206
> Collected: 2026-10-07
> Published: 2026-03-27

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 206
- State: closed
- Author: jpcomps
- Opened: 2026-03-27
- Closed: 2026-03-27
- Labels: none

## Description

## Summary
- add configurable nofile limit handling in MinerFactory with a safe default derived from scan concurrency
- raise limits only when current limits are below target, continue scanning on any failure, and use `rlimit::increase_nofile_limit` on Unix so macOS `kern.maxfilesperproc` caps are respected
- add Windows stdio limit support via rlimit and document the new behavior/options in crate docs

## Validation
- cargo check -p asic-rs
- cargo check -p asic-rs --features python

## Comments

### b-rowan on 2026-03-27

Uhhhh.... GitHub?  This is merged already?  What?
