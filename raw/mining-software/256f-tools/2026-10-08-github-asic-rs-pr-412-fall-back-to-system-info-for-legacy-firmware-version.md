# asic-rs PR #412: fix(antminer): fall back to system info for legacy firmware version

> Source: https://github.com/256foundation/asic-rs/pull/412
> Collected: 2026-10-10
> Published: 2026-10-08
> Registry ID: asic-rs

State: closed | Merged: 2026-10-08 | Author: cfilipescu | +41/-12 | Commits: 2

## Body

## Summary

Follow-up to #411. On older Z15 stock firmware, both `miner_type.cgi` and `summary.cgi` return 404. The missing `summary.cgi` version makes `AntMiner::new` select the v2023.07 backend by default, so the v2020 Xilinx kernel fallback added in #411 is never used.

When the `summary.cgi` compile date is unavailable, read `system_filesystem_version` from `get_system_info.cgi` and use its build date to select the backend. The `summary.cgi` version remains preferred when available.

## Validation

- Read-only probe on a stock Antminer Z15 with `system_filesystem_version` of `Fri Jul 3 11:39:06 CST 2020` now reports version `2020.7.3` and control board `Xilinx`.
- `cargo test -p asic-rs-firmwares-antminer --locked` (39 passed, 3 ignored)
- `cargo fmt --all --check`
- `git diff --check`

## Files changed

- asic-rs-firmwares/antminer/src/firmware.rs (+41/-12) — date parsing extracted to `parse_version_date`; `get_version_with_auth` now falls back from `summary.cgi` `INFO.CompileTime` to `get_system_info.cgi` `system_filesystem_version`; legacy-backend regression test added

## Key patch excerpts

Fallback logic (discovery version fetch under digest auth):

```rust
fn parse_version_date(fw_version: &str) -> Option<semver::Version> { /* date -> semver, e.g. "Fri Jul 3 11:39:06 CST 2020" -> 2020.7.3 */ }

async fn get_version_with_auth(ip: IpAddr, auth: &MinerAuth) -> Option<semver::Version> {
    let client = build_discovery_client().ok()?;
    if let Ok(response) = client
        .get(format!("http://{ip}/cgi-bin/summary.cgi"))
        .send_digest_auth((auth.username(), auth.password()))
        .await
        && let Ok(data) = response.json::<Value>().await
        && let Some(version) = data["INFO"]["CompileTime"]
            .as_str()
            .and_then(parse_version_date)
    {
        return Some(version);
    }

    // Older stock firmware (including Z15) has no summary.cgi, but reports
    // the build date through get_system_info.cgi.
    let response: Response = client
        .get(format!("http://{ip}/cgi-bin/get_system_info.cgi"))
        .send_digest_auth((auth.username(), auth.password()))
        .await
        .ok()?;
    let data = response.json::<Value>().await.ok()?;
    data["system_filesystem_version"]
        .as_str()
        .and_then(parse_version_date)
}
```

Regression test — grounds the legacy backend selection on the real Z15 date string, and a negative case:

```rust
#[test]
fn legacy_system_info_date_selects_legacy_backend() {
    let version = parse_version_date("Fri Jul 3 11:39:06 CST 2020").unwrap();
    assert_eq!(version, semver::Version::new(2020, 7, 3));
    assert!(crate::backends::v2020::AntMinerV2020::validate(Some(&version)));

    assert!(parse_version_date("FR-1.12(251009-S21)").is_none());
}
```

Telemetry endpoint chain this enables on legacy stock firmware: `get_system_info.cgi` → `system_kernel_version` (Xilinx board detection per #411) and `system_filesystem_version` (backend version selection here).
