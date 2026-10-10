# 256foundation/asic-rs pull request #344: fix(factory): bound miner discovery operations

> Source: https://github.com/256foundation/asic-rs/pull/344
> Collected: 2026-10-07
> Published: 2026-08-26

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 344
- State: closed
- Author: DanNicolau
- Opened: 2026-08-26
- Closed: 2026-08-26
- Labels: none

## Description

Added timeouts to discovery ops. The first of a few PRs I'm going to submit for scan improvements. Contributes to #319 
---
This change prevents miner discovery from hanging indefinitely.

  Previously, the identification timeout covered only the firmware-detection commands. Once firmware was identified,
  constructing the miner object could perform additional network requests without being covered by that deadline. HTTP
  connections also lacked an explicit connection timeout in some paths.

  The change:

  - Applies the existing identification timeout to the entire operation:
      - Run firmware-detection commands.
      - Select the detected firmware.
      - Construct the firmware-specific miner object.

  - Adds explicit connection and total-request deadlines to discovery HTTP clients.
  - Treats an expired discovery deadline as “miner not identified” (Ok(None)), allowing the rest of the scan to continue.
  - Adds tests for a stalled HTTP response and stalled miner construction.
  - Updates Rust/Python documentation to clarify the timeout’s end-to-end meaning.

  It deliberately does not change concurrency, retry behavior, port probing, scan staging, or defaults. Consequently, normal
  scans perform essentially the same; the benefit appears when a device or connection stalls.
