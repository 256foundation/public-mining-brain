# asic-rs PR #413: feat(telemetry): expand read-only miner support and correct stock readings

> Source: https://github.com/256foundation/asic-rs/pull/413
> Collected: 2026-10-10
> Published: 2026-10-08
> Registry ID: asic-rs

State: closed | Merged: no | Author: dtyg0d | +8999/-978 | Commits: 3

## Body

Added monitoring support for the verified miner models and firmware variants using the existing workspace structure.

- Added KS7 and S19NoPIC/S19x88 identities, plus Hiveon, Mara/KaonSu, IceRiver AL3 and Goldshell SC5 Pro telemetry.
- Updated stock Antminer parsing for the captured legacy, modern, hydro and Z15 responses.
- Included the required measurement fields, Python/Go bindings, protocol regressions and generated supported-device docs.

New firmware backends are read-only. Unknown model identities and unavailable measurements remain unknown.

## Files changed

- Cargo.toml (+32/-1) / Cargo.lock (+98/-0) — new workspace crates: goldshell, iceriver, kaonsu firmwares + makes
- asic-rs-core/src/data/board.rs (+55/-0)
- asic-rs-core/src/data/deserialize.rs (+15/-0)
- asic-rs-core/src/data/device.rs (+39/-4) — add `HashAlgorithm::Blake2b` (Sia) and `Blake3` (Alephium), both TeraHash unit; `total_chips` now returns None if any board count unknown
- asic-rs-core/src/data/device.rs tests — unknown board counts poison total chip count
- asic-rs-core/src/data/miner.rs (+27/-1)
- asic-rs-core/src/traits/miner.rs (+99/-13)
- asic-rs-macros/src/lib.rs (+2/-0)
- asic-rs-makes/antminer/src/models.rs (+10/-2) — add `KS7` (KHeavyHash); `S19NoPIC` (aliases `ANTMINER S19NOPIC`, `ANTMINER S19X88`, `ANTMINER S19X88 HIVEON`); Hiveon aliases on `S19` / `S19jPro`
- asic-rs-makes/antminer/src/hardware.rs (+8/-0)
- asic-rs-makes/goldshell/* (+126) — `SC5Pro` (Blake2b) identity, normalized parse (strips "GOLDSHELL"/spaces/dashes; SC5, SC5ProX, ARI31 stay Unknown)
- asic-rs-makes/iceriver/* (+113) — `AL3` (Blake3; aliases `ICERIVER AL3`, `10306`) + Unknown fallback
- asic-rs-firmwares/antminer/src/backends/telemetry.rs (+915/-0) — shared stock Antminer stats/summary parsing (rate units, legacy-Z15 contract, hydro, power-source attribution)
- asic-rs-firmwares/antminer/src/backends/telemetry_tests.rs (+838/-0)
- asic-rs-firmwares/antminer/src/backends/rpc_response.rs (+106/-0)
- asic-rs-firmwares/antminer/src/backends/v2020/mod.rs (+116/-415) and v2023_07/mod.rs (+119/-418) — parsing moved into shared telemetry module; rpc.rs slimmed (-29 each)
- asic-rs-firmwares/antminer/src/hiveon.rs (+452/-0) — new Hiveon firmware: identify via "HIVEON" marker in RPC/web responses
- asic-rs-firmwares/antminer/src/test/json/v2023_07/* (+~1200) — captured fixtures: hiveon_s19x88_stats, ks7_modern_stats, s21_hydro/s21_plus_hydro/s21_xp_hydro (web+rpc), s21proplus_modern_stats, s23_hydro, z15 legacy/modern/pro stats + summary, z15_malformed_stats
- asic-rs-firmwares/goldshell/* (+~1150) — stock Goldshell v1 backend (RPC devs/stats/summary/pools + web status/setting), SC5Pro + ARI31 fixtures
- asic-rs-firmwares/iceriver/* (+~1250) — stock IceRiver v1 backend: `/user/userpanel?post=4` read, `/user/loginpost?post=6&user=&pwd=` login with session-cookie reuse, AL3 fixtures
- asic-rs-firmwares/kaonsu/* (+~1800) — Marathon "KaonSu" firmware (Antminer-based): `/kaonsu/v1/brief` API, marafw/mara fw/kaonsu markers, rel314 fixtures
- asic-rs-firmwares/proto/src/backends/v1/mod.rs (+1/-1)
- asic-rs-firmwares/sealminer/src/backends/v2025/mod.rs (+2/-0)
- docs/supported-devices.md (+19/-4) — add Goldshell Stock, Hiveon, IceRiver Stock, KaonSu rows; AntMiner 61→63 models; Goldshell SC5Pro + IceRiver AL3 entries
- go/asic_go/{enums,models,types,types_test}.go (+129/-36) — Go bindings incl. Blake2b/Blake3
- python/pyasic-rs/* (+~150) — stubs + telemetry metadata / pydantic interop tests
- scripts/docs/gen_supported_devices.py (+42/-21)
- src/factory.rs (+19/-0) / src/lib.rs (+6/-0) — register goldshell/iceriver/kaonsu

(Note: per the no-massive-data rule the full ~9000-line diff is not reproduced; see upstream.)

## Key patch excerpts

New Antminer model identities (`asic-rs-makes/antminer/src/models.rs`):

```rust
#[serde(alias = "ANTMINER KS7")]
#[algorithm(HashAlgorithm::KHeavyHash)]
KS7,
// ...
#[serde(alias = "ANTMINER S19", alias = "ANTMINER S19 HIVEON")]
#[algorithm(HashAlgorithm::SHA256)]
S19,
#[serde(alias = "ANTMINER S19NOPIC")]
#[serde(alias = "ANTMINER S19X88")]
#[serde(alias = "ANTMINER S19X88 HIVEON")]
#[algorithm(HashAlgorithm::SHA256)]
S19NoPIC,
// S19jPro gains alias "ANTMINER S19JPRO HIVEON"
```

Stock Antminer rate-unit handling (`telemetry.rs`) — unit strings and defaults:

```rust
let solution_unit = match raw.as_str() {
    "S/S" | "SOL/S" | "SOLS/S" => Some(HashRateUnit::Hash),
    "KS/S" | "KSOL/S" | "KSOLS/S" => Some(HashRateUnit::KiloHash),
    "MS/S" | "MSOL/S" | "MSOLS/S" => Some(HashRateUnit::MegaHash),
    "GS/S" | "GSOL/S" | "GSOLS/S" => Some(HashRateUnit::GigaHash),
    _ => None,
};
// solution units only valid for Equihash; SHA256/KHeavyHash default to GigaHash when unit absent
```

Legacy Z15 response contract (exact strings; gates parsing of the 2020-07-03 Z15 firmware):

```rust
fn legacy_z15_contract(value: &Value, model: Option<&str>) -> bool {
    let Some(header) = value.get("legacy_header") else { return false; };
    model.is_some_and(|model| compact_model(model) == "Z15")
        && header.get("Type").and_then(Value::as_str).is_some_and(|model| compact_model(model) == "Z15")
        && header.get("CGMiner").and_then(Value::as_str) == Some("4.9.0")
        && header.get("Miner").and_then(Value::as_str) == Some("9.0.0.5")
        && header.get("CompileTime").and_then(Value::as_str) == Some("Fri Jul  3 11:39:06 CST 2020")
}
```

Stock wattage: accepted JSON keys + source attribution (keys tried: `chain_power` (string with `W` suffix), `total_power`, `power`, `Power`, `watt`; all candidates must agree within ~1%+1W; source string like `antminer.rpc.stats(new_api=true):total_power`):

```rust
let (row, route) = [
    (value.get("modern"), "antminer.rpc.stats(new_api=true)"),
    (value.get("web"), "antminer.cgi.stats"),
    (value.get("legacy"), "antminer.rpc.stats"),
    (Some(value), "antminer.stats"),
] // ... find row containing any of ["chain_power", "total_power", "power", "Power", "watt"]
```

Hydro model matching (`is_s21_hydro`, compacted model names): `S21HYD | S21HYDRO | S21XPHYD | S21XPHYDRO | S21JXPHYD | S21JXPHYDRO | S21EXPHYD | S21EXPHYDRO | S21+HYD | ...` — drives coolant/fluid-temperature fields (fixtures: s21_hydro_coolant, s21_plus_hydro, s21_xp_hydro web/rpc, s21j_xp_hydro web+rpc, s23_hydro).

Hiveon firmware identification (`hiveon.rs`): RPC or web body containing `HIVEON` (case-insensitive) → Hiveon firmware; model from `version` RPC `/VERSION/0/Type`; firmware version from `/VERSION/0/CompileTime`.

KaonSu (Marathon FW on Antminer hardware) identification (`kaonsu/src/firmware.rs`): discovery commands `rpc version`, web root, and `GET /kaonsu/v1/brief`; marker = body/auth-header contains `marafw`, `mara fw`, or `kaonsu`; model from overview payload keys `model_extended` / `model` (exact base identity preferred over capacity-labeled extended).

KaonSu telemetry mapping (`kaonsu/src/backends/v1/mod.rs`): one `brief` location serves hashrate/expected-hashrate/wattage/uptime/is-mining/operating-state; `hashboards` from brief, `chips` from hashboards, `fans` from fans, `messages` from messages; firmware/control-board version from version payload; power has a `power_indicator` sub-check.

IceRiver AL3 stock (`iceriver/src/backends/v1/`): authenticated web session — `POST /user/loginpost?post=6&user=&pwd=` then `GET /user/userpanel?post=4` with session cookie preserved; response payload at `userpanel/data` (or top level); all read-only (light flashing, pools, boards, fans, uptime, hashrate read from panel JSON).

Goldshell stock v1 (`goldshell/src/backends/v1/mod.rs`) — RPC/Web locations:

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

SC5Pro fixture shape (goldshell tests/fixtures): 4 DEVS entries per board with keys `MHS 20s`, `Status`, `clock`, `fan0..fan3`, `tstemp-0..2`, `voltage`; 4 boards × 84 chips.

Core data model: `MinerHardware.boards` entries may be `None` (unknown chip count; `Some(0)` = confirmed empty slot) and `total_chips` is now `None` unless every board count is known (checked add); new `HashAlgorithm::Blake2b` (Sia) and `Blake3` (Alephium), both mapping to TeraHash units.

supported-devices.md deltas: new firmware rows `Goldshell Stock`, `Hiveon`, `IceRiver Stock`, `KaonSu` (all telemetry-capable cells marked per legend); AntMiner 61→63 models across 24→25 families (KS7 family added; `ANTMINER S19NOPIC` also `S19X88`, `S19X88 HIVEON`).
