# 256foundation/asic-rs pull request #122: Fix MaraFW detection priority + add Pause/Resume support for MaraFW (Kaonsu) and AntMinerV2020

> Source: https://github.com/256foundation/asic-rs/pull/122
> Collected: 2026-10-07
> Published: 2026-01-03

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 122
- State: closed
- Author: glitchpixelz
- Opened: 2026-01-03
- Closed: 2026-01-05
- Labels: none

## Description

## Summary

This PR fixes miner identification when multiple discovery probes succeed (notably MaraFW/Marathon showing a stock-like Web UI), and adds working `pause()` / `resume()` support for:

* **Marathon / MaraFW** (via Kaonsu Web API)
* **AntMinerV2020 stock firmware** (supports both new and old config keys)

The goal is reliable detection + reliable pause/resume behavior across these firmwares.

---

## Problem

### 1) MaraFW sometimes detected as Stock

Discovery runs multiple probes in parallel (HTTP, RPC, etc.). Previously, the factory returned the **first successful** identification result. On MaraFW devices, the HTTP probe can look “stock”, so the code could select the Stock backend before the RPC probe had a chance to report MaraFW.

Result: MaraFW miners were misclassified as Stock, and stock commands were used against a MaraFW device.

### 2) Marathon backend had no Pause/Resume

`MaraV1` previously returned `Unsupported command` for Pause/Resume.

### 3) AntMinerV2020 needed Pause/Resume across firmware variants

Some Bitmain firmwares use `bitmain-work-mode`, while older ones use `miner-mode`.

---

## Changes

### A) Prefer explicit firmware IDs over Stock during discovery

**File:** `src/miners/factory/mod.rs`

* Discovery now keeps the “best” identification result instead of returning the first one.
* Explicit firmware identifications (Marathon/MaraFW, BraiinsOS, LuxOS, etc.) **override** Stock/make-only results.
* Stops early once a high-confidence non-stock firmware is found.

**Why:** MaraFW/Marathon should win even if the HTTP probe returns a stock-like result first.

---

### B) Implement Pause/Resume for MaraFW (Marathon backend) via Kaonsu Web API

**File:** `src/miners/backends/marathon/v1/mod.rs`

Adds helper methods to `MaraV1`:

* `get_work_mode()`

  * `GET /kaonsu/v1/miner_config`
  * reads `/mode/work-mode-selector`

* `set_work_mode(mode)`

  * `GET /kaonsu/v1/miner_config` (full config)
  * updates `mode.work-mode-selector`
  * `POST /kaonsu/v1/miner_config`
  * validates response `{"error":false,"msg":"success"}`

* `last_mode_before_sleep_from_history()`

  * `GET /kaonsu/v1/log?type=miner_config_history`
  * scans newest → oldest for `Mode/WorkModeSelector` transitions where `to == "Sleep"`
  * returns the `"from"` mode (Auto / Fixed / Stock)

#### Behavior

* `pause()`

  * if already `Sleep`, returns `true` (no-op)
  * otherwise sets work mode to `Sleep`

* `resume()`

  * if not currently `Sleep`, returns `true` (no-op)
  * if `Sleep`, restores the last mode before Sleep using history
  * falls back to `Stock` if history has no match

**Why history-based resume:** it restores the correct mode even if Sleep was triggered via the GUI or another tool.

---

### C) Implement Pause/Resume for AntMinerV2020 (stock)

**File:** `src/miners/backends/antminer/v2020/mod.rs`

* Reads current config via `get_miner_conf()`
* If `bitmain-work-mode` exists:

  * pause → `"1"`
  * resume → `"0"`
* Otherwise fallback:

  * pause → `"miner-mode": "Sleep"`
  * resume → `"miner-mode": "Normal"`

---

## Testing / Verification

* `cargo build` (local)
* Manual MaraFW verification:

  * `POST /kaonsu/v1/miner_config` returns `{"error":false,"msg":"success"}`
  * Mode changes reflected in `GET /kaonsu/v1/miner_config`
  * Resume restores the previous non-sleep mode based on `miner_config_history`

---

## Notes

* The discovery priority change is intentionally conservative: Stock/make-only results remain valid fallbacks, but will no longer override explicit firmware IDs.
* MaraFW pause/resume uses the same endpoints the web UI uses (`miner_config` + config history log).
