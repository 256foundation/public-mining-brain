# asic-rs

> Sources: 256 Foundation (asic-rs README), collected 2026-10-07; 256 Foundation (asic-rs documentation, Home), collected 2026-10-07; 256 Foundation (asic-rs documentation, Getting Started), collected 2026-10-07; 256 Foundation (asic-rs documentation, API Guide), collected 2026-10-07; 256 Foundation (asic-rs documentation, Documentation Workflow), collected 2026-10-07
> Raw: [asic-rs README](../../raw/tools/github-256foundation-asic-rs.md); [asic-rs docs home](../../raw/tools/docs-asic-rs.md); [asic-rs getting started](../../raw/tools/docs-asic-rs-getting-started.md); [asic-rs API guide](../../raw/tools/docs-asic-rs-api.md); [asic-rs documentation workflow](../../raw/tools/docs-asic-rs-development-documentation.md)
> Updated: 2026-10-07

## Overview

asic-rs is an async library for managing and controlling ASIC miners. It finds miners on a network, reads their telemetry in one standard shape, and runs the controls each miner supports. The core is a Rust crate. Python and Go bindings share the same names and behaviour, so the same ideas carry across all three languages. It is licensed Apache-2.0.

## Three packages, one design

| Language | Package | How it is built |
|----------|---------|-----------------|
| Rust | the `asic-rs` crate | Native |
| Python | `pyasic_rs` | PyO3 classes with Pydantic-compatible data models |
| Go | `github.com/256foundation/asic-rs/go/asic_go` | Lives in-tree and wraps a small C ABI, `asic-rs-ffi`, through cgo |

The docs stress that the bindings are not a separate design. Each language keeps its own habits:

- **Rust.** Network calls are async. Methods generally return `Result<T>`, and `Option<T>` when a miner does not expose a value.
- **Python.** Methods are awaitable. `None` stands for missing or unsupported values.
- **Go.** Methods are synchronous and return `error`. A missing miner is `asic_go.ErrNotFound`. Factory and miner handles must be closed. Streaming scans and `MinerListener` are not wrapped yet.

## The common workflow

1. Build a `MinerFactory`.
2. Identify one miner by IP, or scan a range.
3. Read telemetry with `get_data()` or a focused `get_*` call.
4. Check `supports_*` before any optional control.
5. Apply the control or configuration change.

## Discovery

`MinerFactory` owns the scan range and the tuning of the scan.

- **One known IP.** The factory identifies the firmware and builds the matching miner implementation.
- **A range.** Give it a subnet, octet selectors, or a range string. Large scans use bounded concurrency.
- **Streaming.** `scan_stream()` hands back miners as they are found. `scan_stream_with_ip()` reports every address, so unsupported or offline ones can be tracked too.

Tuning knobs:

- **Concurrency limit.** It bounds the total number of active TCP probes, retries included.
- **Connectivity retries.** Extra attempts after the first probe, with bounded exponential backoff. The default is three. Zero still does one probe.
- **Identification timeout.** One end-to-end deadline for discovery commands and for building the firmware-specific miner.

Common miner ports are probed at the same time. The probe returns after the first success.

## Reading data

`get_data()` returns `MinerData`, a full standard telemetry snapshot. Expensive fields, such as hashboards and chips, can be left out of a snapshot.

Focused getters cover: MAC address, serial number, hostname, firmware version, hashboards, hashrate, fans, wattage, best share difficulty, session best share difficulty, messages, pools and mining state.

Identity is known as soon as the miner handle exists: IP address, make, model, firmware, algorithm and hardware shape.

Two fields the README explains at length:

- **operating_state.** An optional detailed runtime state, for firmware that reports one. It separates mining from startup, tuning, pause, cooldown, errors and more. `Mining` alone does not promise tuning is done. `Stable` is used only when the firmware says so. Unrecognized labels are kept as raw values. The older `is_mining` flag is unchanged and is not derived from it.
- **devfee_connected.** Whether the developer-fee connection is healthy, when the firmware exposes that.

## Controls

Not every miner supports every control. Each control has a matching capability check.

| Control | What it does |
|---------|--------------|
| `restart()` | Restart the miner |
| `pause()`, `resume()` | Stop and start mining |
| `set_fault_light(...)` | Switch the fault light |
| `set_power_limit(...)` | Set a power limit |
| `change_password(...)` | Change the password |
| `read_logs()` | Read logs |
| `factory_reset()` | Restore settings to factory defaults. It does not replace the operating system |
| `restore_stock_os()` | Uninstall an aftermarket OS and restore the maker's stock OS. Disruptive. A successful request may reboot the miner and does not mean the restore is finished |
| `prepare_firmware(...)` | Read-only. Validates a firmware file and returns the image an upgrade would use. Never starts an upload |
| `upgrade_firmware(...)` | Upgrade the firmware |

Every handle also has `revalidate()`. It re-runs discovery against the same IP and reports whether the device still matches the handle.

## Configuration

Four kinds of configuration can be read and written, each behind its own support check: pools, fans, tuning and scaling.

- Pool settings are groups of pools, each with a URL, username and password.
- Fan settings can be manual.
- Tuning targets can be a power figure, a hashrate, a mining mode, a preset, or manual values.

Backends use built-in default credentials unless the caller sets others. Set them before starting concurrent operations on that handle.

## Where the languages differ on the wire

Some long-standing Python representations differ from the Rust schema. The C bridge and Go JSON output keep the Rust schema.

| Value | Rust, C and Go JSON output | Python |
|-------|----------------------------|--------|
| Hashrate unit | `"TeraHash"` | `"TH/s"` |
| Pool scheme | `"StratumV1"` | `"stratum+tcp"` |
| Pool URL | An object with scheme, host, port and pubkey | A URL string |
| Fan mode | `"Auto"` / `"Manual"` | `"auto"` / `"manual"` |

Go accepts the Python input forms and then emits the Rust form. Invalid hash units and algorithms return errors.

## Getting started

Import the factory in your language:

- Rust: `use asic_rs::MinerFactory;`
- Python: `from pyasic_rs import MinerFactory`
- Go: `import "github.com/256foundation/asic-rs/go/asic_go"`

Then ask the factory for a miner by IP, or scan a subnet. For Go, build the native library with `make -C go ffi` before `go test` or `go build`.

## How the project documents itself

There are three documentation targets, fed from shared sources:

- A Zensical site, built from the `docs/` pages.
- The Rust crate docs and the root README, both from `docs-shared/guide.md`.
- The Python package README, from the same guide.

The root README is generated from the crate docs. That step needs the nightly Rust toolchain.

## See Also

- [asic-rs Supported Devices](asic-rs-supported-devices.md)
- [BTC Toolkit](btc-toolkit.md)
- [HashScope](hashscope.md)
