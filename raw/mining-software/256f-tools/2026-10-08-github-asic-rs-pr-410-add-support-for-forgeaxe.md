# asic-rs PR #410: feat: add support for forgeaxe

> Source: https://github.com/256foundation/asic-rs/pull/410
> Collected: 2026-10-10
> Published: 2026-10-08
> Registry ID: asic-rs

State: open | Merged: no | Author: b-rowan | +1495/-1 | Commits: 2

## Body

(No PR body provided upstream — scope is described by the file set: a new `forgeaxe` firmware crate, `forgeaxe` make crate, factory registration, and supported-devices docs entry.)

## Files changed

- Cargo.toml (+12/-0) — add `asic-rs-firmwares-forgeaxe` / `asic-rs-makes-forgeaxe` to workspace + `forgeaxe` feature
- Cargo.lock (+32/-0) — lock entries for new crates
- asic-rs-firmwares/forgeaxe/Cargo.toml (+26/-0) — new firmware crate manifest
- asic-rs-firmwares/forgeaxe/src/lib.rs (+2/-0)
- asic-rs-firmwares/forgeaxe/src/firmware.rs (+142/-0) — "ForgeOS Stock" firmware entry: model/version from `/api/system/info`, web-root identification on "ForgeOS"
- asic-rs-firmwares/forgeaxe/src/backends/mod.rs (+22/-0) — backend module wiring
- asic-rs-firmwares/forgeaxe/src/backends/v1_1_0/mod.rs (+786/-0) — v1.1.0 read-only telemetry backend over `/api/system/info`
- asic-rs-firmwares/forgeaxe/src/backends/v1_1_0/web.rs (+212/-0) — web API client
- asic-rs-firmwares/forgeaxe/src/test/json/v1_1_0/system_info.json (+31/-0) — captured fixture
- asic-rs-makes/forgeaxe/Cargo.toml (+23/-0) — new make crate manifest
- asic-rs-makes/forgeaxe/src/lib.rs (+3/-0)
- asic-rs-makes/forgeaxe/src/make.rs (+22/-0) — `ForgeaxeMake` parse passthrough
- asic-rs-makes/forgeaxe/src/models.rs (+69/-0) — `BitForgeNano` identity (SHA256) + `Unknown` fallback
- asic-rs-makes/forgeaxe/src/hardware.rs (+79/-0) — BitForgeNano = 1 fan / 1 board / 2 chips; `B800` control board parse
- docs/supported-devices.md (+5/-0) — "ForgeOS Stock" row; `BITFORGE_NANO` (also `BM1370`)
- python/pyasic-rs/Cargo.toml (+2/-0)
- python/pyasic-rs/pyasic_rs/asic_rs.pyi (+1/-1) — regenerated stub
- src/factory.rs (+24/-0) — register `forgeaxe` feature in default firmware registry + ForgeOS discovery test
- src/lib.rs (+2/-0)

## Key patch excerpts

Model identity (`asic-rs-makes/forgeaxe/src/models.rs`) — the BitForge Nano is detected from the ASIC model string; config uses `BITFORGE_NANO`, system info reports ASIC `BM1370`:

```rust
pub enum ForgeaxeModel {
    // config-Nano.cvs uses BITFORGE_NANO; system/info identifies its ASIC as BM1370.
    #[serde(alias = "BITFORGE_NANO", alias = "BM1370")]
    #[algorithm(HashAlgorithm::SHA256)]
    BitForgeNano,
    #[strum(to_string = "{0}")]
    #[algorithm(HashAlgorithm::Unknown)]
    Unknown(String),
}
```

Firmware detection + model/version fetch (`asic-rs-firmwares/forgeaxe/src/firmware.rs`):

```rust
impl Display for ForgeaxeFirmware {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "ForgeOS Stock")
    }
}

// version parse: ForgeOS release tags omit the patch component (e.g. v1.1) -> X.Y.0
fn parse_version(version: &str) -> Option<Version> {
    let version = version.trim().trim_start_matches('v');
    Version::parse(version).ok().or_else(|| {
        let (major, minor) = version.split_once('.')?;
        Some(Version::new(major.parse().ok()?, minor.parse().ok()?, 0))
    })
}

async fn get_model(ip: IpAddr) -> Result<Self::Model, ModelSelectionError> {
    let response = util::send_web_command(&ip, "/api/system/info").await;
    // ... model = json_data["ASICModel"].as_str() -> ForgeaxeMake::parse_model(model.to_uppercase())
}

impl FirmwareIdentification for ForgeaxeFirmware {
    fn identify_web(&self, response: &WebResponse<'_>) -> bool {
        response.body.contains("ForgeOS")
    }
    fn is_stock(&self) -> bool { true }
}
```

Telemetry JSON keys — all read from `/api/system/info` (`backends/v1_1_0/mod.rs`): `miningPaused` (operating state), `macAddr`, `hostname`, `version` (firmware + API version), `boardVersion` (control board), `hashRate`, `fanrpm`, `temp`, `power` (wattage), `uptimeSeconds`, `bestDiff` / `bestSessionDiff`, plus board-level `smallCoreCount`, `asicCount`, `voltage`, `frequency`, `vrTemp`, `overheat_mode`.

Hardware constants (`asic-rs-makes/forgeaxe/src/hardware.rs`) — grounded in ForgeOS source:

```rust
// ForgeOS defines BITFORGE_NANO_ASIC_COUNT as 2, including in v1.1:
// https://github.com/WantClue/forge-os/blob/v1.1/components/asic/include/asic.h
ForgeaxeModel::BitForgeNano => Self {
    fans: Some(1),
    boards: Some(vec![Some(2)]),
},
```

```rust
pub enum ForgeaxeControlBoard {
    #[serde(rename = "B800")]
    B800,
}
// parse: "800" (trimmed, spaces stripped, uppercased) => B800; anything else (e.g. "601") => None
```

Registration order note (`src/factory.rs`): `forgeaxe` is inserted alphabetically after `bitaxe` and before `braiins`; discovery test asserts web root `<title>ForgeOS</title>` maps to firmware display name `"ForgeOS Stock"` with `is_stock() == true` (explicitly not AxeOS/NerdAxe).
