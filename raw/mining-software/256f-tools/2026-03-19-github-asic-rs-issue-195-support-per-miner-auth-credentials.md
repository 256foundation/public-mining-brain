# 256foundation/asic-rs issue #195: Support per-miner auth credentials in MinerFactory

> Source: https://github.com/256foundation/asic-rs/issues/195
> Collected: 2026-10-07
> Published: 2026-03-19

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 195
- State: closed
- Author: ankitgoswami
- Opened: 2026-03-19
- Closed: 2026-03-31
- Labels: none

## Description

Right now miner auth is hardcoded per backend. This breaks for mixed fleets where miners have different credentials.

Two places need auth before the caller has a miner object:
- Runtime control calls (most authenticated backends)
- Model detection, specifically Antminer, which hits `/cgi-bin/miner_type.cgi` with digest auth during `get_model`

### What we likely need

- A shared `MinerAuth` type with optional username and password
- Factory-level storage: per-IP credentials and a default fallback
- Factory APIs: `with_auth`, `set_auth`, `with_default_auth`, `set_default_auth`
- Auth threaded through `FirmwareEntry::build_miner`, `MinerFirmware::get_model`/`get_version`, and `MinerConstructor::new`
- Python bindings with keyword args (`factory.set_auth("192.168.1.50", username="root", password="x")`)
- Passwords redacted in `Debug` output (hard requirement, not nice-to-have)

### Requested Phasing

**Phase 1:** `MinerAuth` type, factory storage and APIs (Rust + Python), trait changes with default impls, wire up WhatsMiner and VNish. Tests for per-IP override, default fallback, and no-auth-provided paths.

**Phase 2:** Remaining backends: Antminer, Braiins, Marathon, ePIC, LuxMiner.

### Acceptance criteria

- Different credentials for different IPs in the same factory
- `get_miner()` uses provided creds during discovery and build
- Runtime control uses the same creds
- No creds provided = existing behavior, backend defaults kick in
- Python has the same capability
- Passwords never appear in debug output
