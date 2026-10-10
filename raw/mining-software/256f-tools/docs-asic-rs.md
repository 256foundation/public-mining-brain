# Home - asic-rs

> Source: https://256foundation.github.io/asic-rs/
> Collected: 2026-10-07
> Published: Unknown

# asic-rs[¶](https://256foundation.github.io#asic-rs)

asic-rs is an async miner management and control library for ASIC miners. It keeps the Rust crate, Python bindings, and Go bindings aligned around the same concepts: discover miners, gather standardized telemetry, and run supported controls.

```
use asic_rs::MinerFactory;
```
Use the `asic-rs` crate when building native Rust services, daemons, and
tooling.

```
from pyasic_rs import MinerFactory
```
Use `pyasic_rs` when integrating miner management into Python automation,
data pipelines, or API services.

```
import "github.com/256foundation/asic-rs/go/asic_go"
```
Use the in-tree Go module when integrating miner management into Go
services. See `go/README.md` for cgo packaging.

## One API Shape[¶](https://256foundation.github.io#one-api-shape)

| Concept | Rust | Python | Go | 
|---|---|---|---|
| Discovery | `MinerFactory` | `MinerFactory` | `asic_go.MinerFactory` | 
| Miner handle | `Box<dyn Miner>` | `Miner` | `asic_go.Miner` | 
| Full telemetry | `MinerData` | `pyasic_rs.data.MinerData` | `asic_go.MinerData` | 
| Pool config | `PoolGroupConfig`, `PoolConfig` | `PoolGroup`, `Pool` | `PoolGroupConfig`, `PoolConfig` | 
| Fan config | `FanConfig` | `FanConfig` | `FanConfig` | 
| Tuning config | `TuningConfig` | `TuningConfig` | `TuningConfig` | 

The bindings are not a separate design. Python methods mirror the Rust surface,
with Python-native conventions where appropriate: awaitables for async work,
`None` for missing optional values, and Pydantic-compatible model helpers for
data/config objects. Go methods are synchronous and return `error`; a missing
miner is `asic_go.ErrNotFound`.

## Common Workflow[¶](https://256foundation.github.io#common-workflow)

1. Build a `MinerFactory`.
2. Identify one miner by IP or scan a range.
3. Read telemetry with `get_data()` or focused `get_*` calls.
4. Check `supports_*` before optional controls.
5. Apply supported control or configuration changes.

Continue with [Getting started](https://256foundation.github.io/getting-started/) for paired Rust, Python, and
Go examples.
