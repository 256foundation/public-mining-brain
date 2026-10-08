# bitaxeorg/bitaxe-raw pull request #18: Update BitaxeBonanza raw for Bridge protocol 1

> Source: https://github.com/bitaxeorg/bitaxe-raw/pull/18
> Collected: 2026-10-07
> Published: 2026-07-25

- Repository: bitaxeorg/bitaxe-raw
- Type: pull request
- Number: 18
- State: closed
- Author: johnny9
- Opened: 2026-07-25
- Closed: 2026-07-25
- Labels: none

## Description

## Summary

- Identify the USB product as `BitaxeBonanza` and expose the Bonanza VR enable and power-good GPIO controls from #13.
- Support Bonanza Bridge protocol 1 with hardened request/response framing and read-only firmware, RX-statistics, and safety diagnostics.
- Let the raw firmware own the Bridge safety lease. Existing clients can continue using the legacy GPIO interface while the firmware handles compatibility checks, arming, heartbeats, recoverable fault clearing, and fail-safe shutdown.
- Keep the physical ESP-to-Bridge data UART at the required 2 Mbaud while accepting clients that configure the USB CDC port for a legacy baud rate.
- Treat repeated unsafe GPIO writes as idempotent when the requested level is already active.

## Why

The latest Bonanza Bridge firmware requires an explicit safety lease before enabling 5 V, releasing ASIC reset, or reducing the fan from 100%. The raw firmware is the trusted Bridge client, so it owns and renews that lease internally without adding lease-management requirements to BIRDS or other developer clients.

Closing the control port or encountering a Bridge error asserts ASIC reset, disables 5 V, forces the fan to 100%, and disarms the lease.

This supersedes #13.

## Validation

- All 8 Bridge protocol unit tests pass.
- The locked ESP32-S3 release build succeeds.
- Flashed and tested on an attached BitaxeBonanza with Bridge protocol 1.0 and firmware `0.0.1+g4fea080`.
- The unchanged local BIRDS `bzmd` client detected all four ASICs, reported all engines working, and completed system power-on in 4 seconds.
- A client-selected 5 Mbaud USB CDC setting successfully communicated with the ASIC over the fixed 2 Mbaud physical Bridge link.
- Repeated legacy 5 V enable passed while the safety lease remained healthy.
- Bridge FIFO and ring overflow counters remained zero.
- Client disconnect returned the board to safe-off with 5 V disabled, ASIC reset asserted, fan at 100%, no active lease, and no fault.
