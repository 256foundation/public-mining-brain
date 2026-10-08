# 256foundation/asic-rs pull request #205: fix(factory): include all IPv4 subnet addresses during discovery

> Source: https://github.com/256foundation/asic-rs/pull/205
> Collected: 2026-10-07
> Published: 2026-03-26

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 205
- State: closed
- Author: cfilipescu
- Opened: 2026-03-26
- Closed: 2026-03-26
- Labels: none

## Description

## Summary
- Update IPv4 subnet host expansion in `MinerFactory::hosts_from_subnet` to include every address in the subnet range, including network and broadcast addresses.
- Keep IPv6 behavior unchanged by continuing to use iterator-based host expansion.
- Add regression tests for `/32`, `/31`, and `/30` to verify all IPv4 addresses are returned.

## Testing
- cargo test subnet_hosts_include_all_ipv4_addresses
