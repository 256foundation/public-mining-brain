# 256foundation/asic-rs pull request #212: fix(whatsminer): surface actual error when V2 privileged RPC returns unencrypted response

> Source: https://github.com/256foundation/asic-rs/pull/212
> Collected: 2026-10-07
> Published: 2026-04-02

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 212
- State: closed
- Author: ankitgoswami
- Opened: 2026-04-02
- Closed: 2026-04-02
- Labels: none

## Description

When a WhatsMiner V2 miner returns a plain error (e.g. permission denied) instead of an encrypted response, fall back to parsing it as a normal RPC result instead of failing with "Missing 'enc' field".
