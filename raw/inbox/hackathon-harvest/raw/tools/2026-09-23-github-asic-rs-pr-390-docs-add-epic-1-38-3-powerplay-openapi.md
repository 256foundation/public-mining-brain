# 256foundation/asic-rs pull request #390: docs: add ePIC 1.38.3 powerplay OpenAPI spec

> Source: https://github.com/256foundation/asic-rs/pull/390
> Collected: 2026-10-07
> Published: 2026-09-23

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 390
- State: closed
- Author: cfilipescu
- Opened: 2026-09-23
- Closed: 2026-09-23
- Labels: none

## Description

## Summary

Add the ePIC 1.38.3 PowerPlay OpenAPI specification, fetched from the live miner and formatted consistently with the existing metadata.

The document includes the released `/uninstall` endpoint and related schemas. The server URL is normalized to the metadata placeholder (`192.168.0.0:4028`).

## Validation

- JSON parses successfully
- 68 paths and 95 schemas
- Existing 1.22.5 and 1.30.0 metadata remain unchanged
