# 256foundation/asic-rs pull request #362: fix(core): use algorithm-specific hashrate units

> Source: https://github.com/256foundation/asic-rs/pull/362
> Collected: 2026-10-07
> Published: 2026-09-10

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 362
- State: closed
- Author: cfilipescu
- Opened: 2026-09-10
- Closed: 2026-09-10
- Labels: none

## Description

## Summary

- derive the conventional display unit from `HashRate.algo`
- normalize miner, expected, and hashboard rates through `as_default_unit()` across every backend
- infer the algorithm-specific unit in the Python constructor when no explicit unit is supplied
- expose default-unit lookup and conversion in the Rust and Python APIs

The defaults are:

| Algorithm | Unit |
| --- | --- |
| SHA-256, Blake2S256, Kadena, kHeavyHash, Eaglesong, Handshake, Blake256R14 | TH/s |
| Scrypt, X11 | GH/s |
| EtHash | MH/s |
| Equihash | KH/s |
| Unknown | H/s |

Explicitly supplied units are still preserved, `HashRateUnit::default()` remains TH/s for compatibility, and the serialized `HashRate` shape is unchanged.

## Testing

- `cargo test --workspace --all-targets`
- `cargo clippy --workspace --all-targets --all-features -- -D warnings`
- `cargo fmt --all -- --check`
- Python test suite: 114 passed
- targeted Antminer Scrypt parser tests

Closes #304
