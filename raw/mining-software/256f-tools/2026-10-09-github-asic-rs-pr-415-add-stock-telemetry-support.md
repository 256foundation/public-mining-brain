# asic-rs PR #415: feat(goldshell): add stock telemetry support

> Source: https://github.com/256foundation/asic-rs/pull/415
> Collected: 2026-10-10
> Published: 2026-10-09
> Registry ID: asic-rs

State: open | Merged: no | Author: dtyg0d | +1336/-1 | Commits: 1

## Body

Adds read-only Goldshell stock discovery and telemetry, with SC5Pro/Blake2b identification and unknown-model handling. Commands and parsing stay in the versioned backend, using explicit trait implementations.

API mappings were adapted from pyasic; regression tests use sanitized SC5Pro and ARI31 captures.

## Files changed

- asic-rs-firmwares/goldshell/Cargo.toml (+24/-0) / src/lib.rs (+2/-0) — new firmware crate `Goldshell Stock`
- asic-rs-firmwares/goldshell/src/firmware.rs (+119/-0) — firmware entry: model/version from web `status`, identification via RPC markers `goldshell`/`kdaminer`/`intchains_qomo` and web markers `goldshell`/`cloud-box`/auth header
- asic-rs-firmwares/goldshell/src/backends/mod.rs (+1/-0)
- asic-rs-firmwares/goldshell/src/backends/v1/mod.rs (+700/-0) — read-only v1 telemetry backend over cgminer-style RPC (`version`, `summary`, `devs`, `stats`, `pools`) + web (`status`, `setting`)
- asic-rs-firmwares/goldshell/src/backends/v1/web.rs (+111/-0) — web API client (read-only command allowlist)
- asic-rs-firmwares/goldshell/tests/fixtures/live_sc5pro_2_2_0.json (+90/-0), live_ari31_2_2_3.json (+90/-0), tests/fixtures/README.md (+6/-0) — sanitized captures
- asic-rs-makes/goldshell/Cargo.toml (+20/-0), make.rs (+28/-0), hardware.rs (+9/-0), models.rs (+65/-0) — `SC5Pro` (Blake2b) identity + `Unknown` fallback; `GoldshellMake`
- asic-rs-core/src/data/device.rs (+5/-0)
- asic-rs-macros/src/lib.rs (+1/-0)
- Cargo.toml (+12/-0) / Cargo.lock (+30/-0) — workspace + feature registration
- docs/supported-devices.md (+5/-0) — `Goldshell Stock` row; Goldshell `SC5PRO` entry
- go/asic_go/enums.go (+2/-1), types_test.go (+1/-0); python/pyasic-rs/Cargo.toml (+2/-0), asic_rs.pyi (+1/-0), test_pydantic_interop.py (+1/-0)
- src/factory.rs (+6/-0) / src/lib.rs (+2/-0) — register goldshell firmware

## Key patch excerpts

Firmware identification (`goldshell/src/firmware.rs`):

```rust
impl DiscoveryCommands for GoldshellFirmware {
    fn get_discovery_commands(&self) -> Vec<DiscoveryCommand> {
        vec![
            HTTP_WEB_ROOT,
            RPC_VERSION,
            DiscoveryCommand::Web { command: "/mcb/status", port: 80 },
        ]
    }
}

// model from web "status" payload: status.get("model") -> GoldshellMake::parse_model
// firmware version: status.get("firmware"), 'v'-prefix stripped -> semver

impl FirmwareIdentification for GoldshellFirmware {
    fn identify_rpc(&self, response: &str) -> bool {
        let response = response.to_ascii_lowercase();
        response.contains("goldshell")
            || response.contains("kdaminer")
            || response.contains("intchains_qomo")
    }
    fn identify_web(&self, response: &WebResponse<'_>) -> bool {
        let body = response.body.to_ascii_lowercase();
        matches!(response.status, 200 | 401 | 403)
            && (body.contains("goldshell")
                || body.contains("cloud-box")
                || response.auth_header.to_ascii_lowercase().contains("goldshell"))
    }
    fn is_stock(&self) -> bool { true }
}
```

Model identity (`asic-rs-makes/goldshell/src/models.rs`) — normalization + unknown-model handling:

```rust
let normalized = raw.to_ascii_uppercase().replace([' ', '-', '_'], "");
let name = normalized.strip_prefix("GOLDSHELL").unwrap_or(&normalized);
serde_json::from_value(serde_json::Value::String(name.to_string()))
    .or_else(|_| Ok(Self::Unknown(raw.to_string())))
// SC5Pro => Blake2b; Unknown(_) => HashAlgorithm::Unknown
```

Telemetry locations (`backends/v1/mod.rs` — API mappings adapted from pyasic):

```text
Mac            <- web "setting"  /name
ApiVersion     <- rpc "version"  /VERSION/0/API
FirmwareVersion<- web "status"   /firmware
Hashrate/IsMining <- rpc "summary" /SUMMARY/0
Uptime         <- rpc "summary"  /SUMMARY/0/Elapsed
Hashboards     <- rpc "devs"     /DEVS   (tag "devices")
Fans           <- rpc "stats"    /STATS
Pools          <- rpc "pools"    /POOLS
```

Web client is read-only: `allows_read` gates commands, control commands and parameters are rejected before network I/O.

SC5Pro fixture shape (`live_sc5pro_2_2_0.json`, firmware 2.2.0): 4 boards × 84 chips (`chips-nr`); per-DEVS keys `MHS 20s` (~2.77–2.89 MH board rate scale), `Status`, `clock`, `fan0..fan3`, `tstemp-0..2`, `voltage`. ARI31 capture (`live_ari31_2_2_3.json`) exercises unknown-model handling (parses as `GoldshellModel::Unknown`, `hash_algorithm` stays `Unknown`).

related: this PR supersedes the Goldshell portion of #413 (same backend/fixture set, revised).
