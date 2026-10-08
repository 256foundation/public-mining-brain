# BTC Toolkit

> Sources: 256 Foundation (btc-toolkit README), collected 2026-10-07
> Raw: [btc-toolkit README](../../raw/tools/github-256foundation-btc-toolkit.md)
> Updated: 2026-10-07

## Overview

BTC Toolkit is a desktop GUI for managing Bitcoin ASIC mining farms. It scans networks, discovers miners, and shows device details. It is a thin application on top of [asic-rs](asic-rs.md), which does the discovery and data collection.

## What it does

- Scans a network for miners.
- Discovers the miners it finds.
- Shows details for each device.

The README lists nothing beyond these three functions.

## How it is built

- The interface uses the iced.rs GUI library, v0.14.
- Miner discovery and data come from [asic-rs](asic-rs.md). The devices it can see are therefore the ones in [asic-rs Supported Devices](asic-rs-supported-devices.md).

## Running it

It needs the stable Rust toolchain. There is no packaged download mentioned in the README. Run it from source:

- `cargo run` for a debug build.
- `cargo build --release` for a release build.

## See Also

- [asic-rs](asic-rs.md)
- [asic-rs Supported Devices](asic-rs-supported-devices.md)
