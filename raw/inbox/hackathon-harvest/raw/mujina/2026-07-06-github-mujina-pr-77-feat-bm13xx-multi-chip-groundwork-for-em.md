# 256foundation/mujina pull request #77: feat(bm13xx): multi-chip groundwork for EmberOne00 and Bitmain chains

> Source: https://github.com/256foundation/mujina/pull/77
> Collected: 2026-10-07
> Published: 2026-07-06

- Repository: 256foundation/mujina
- Type: pull request
- Number: 77
- State: closed
- Author: rkuester
- Opened: 2026-07-06
- Closed: 2026-07-07
- Labels: none

## Description

### Summary

Restructures the BM13xx ASIC layer from a single-chip implementation shaped around the Bitaxe into a foundation that can drive multi-chip chains. The first target is the EmberOne00 (12x BM1362), with Bitmain machines behind it: the S19j Pro and S19k Pro class today, and newer models as they're understood. The chain and topology model is built for chains of any length, and the protocol work is grounded in captured factory traffic from long-chain Bitmain hardware. No board bring-up is included yet; this is the protocol, register, and driver groundwork the chain work builds on.

### What's here

- The monolithic protocol module is split into focused submodules: commands, responses, registers, and a codec parameterized by chip model.
- Registers get semantic types with named bit fields (misc control, UART relay, analog mux, core mailbox, midstate config, soft reset, hash counting number), replacing raw u32 constants.
- A chain and topology domain model describes chip addressing and how work is partitioned across chains of any length.
- A reader task demultiplexes chip responses from the shared serial bus, and a driver layers request/response register conversations on top of it.
- PLL calculation moves into a ChipConfig, using a new unit-aware Frequency type.
- TPS546 voltage control is decomposed into PMBus primitives, with two fixes (ON_OFF_CONFIG CP bit dropped, family naming in logs and docs).
- PROTOCOL.md grows substantially: register semantics and the version-rolling search-space model, covering how chip address, nonce offset, and the hash counting number distribute work across a chain, with corrections to earlier assumptions.
- Wire-format fixes found along the way: the JobFull length byte now matches factory firmware, and domain-boundary drive strength is corrected.

Frame encoders and decoders are covered by unit tests that check against bytes from captured factory traffic, including S21 Pro and S19j Pro chains. The Bitaxe Gamma path has been exercised on hardware during development.

### Status

Draft: history will still be amended. The final documentation commit is labeled WIP while its search-space rewrite is under review. Queued next on this branch: computing the hash counting number from the achieved PLL dividers instead of the fixed constant now in use, and chain-level configuration for bring-up.
