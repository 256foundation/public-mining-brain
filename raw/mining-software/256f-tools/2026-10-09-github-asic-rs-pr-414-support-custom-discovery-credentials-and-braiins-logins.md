# asic-rs PR #414: fix(auth): support custom discovery credentials and Braiins logins

> Source: https://github.com/256foundation/asic-rs/pull/414
> Collected: 2026-10-10
> Published: 2026-10-09
> Registry ID: asic-rs

State: closed | Merged: 2026-10-09 | Author: dtyg0d | +333/-23 | Commits: 3

## Body

Python callers can now supply per-firmware credentials before discovery, allowing stock miners with custom passwords to be constructed and authenticated telemetry to use the same credentials. Legacy Braiins LuCI logins now form-encode usernames and passwords so reserved characters do not corrupt authentication.

Updated the existing authentication examples and generated Python stubs. Protocol regressions cover stock discovery and protected telemetry with custom credentials, and Braiins login encoding and session-cookie reuse.

Fixes #403
Fixes #404

## Files changed

- src/factory.rs (+21/-0) — `MinerFactory::with_firmware_discovery_auth_by_name(firmware_name, auth)`: per-firmware discovery credentials keyed by firmware Display name
- asic-rs-firmwares/braiins/src/backends/v21_09/web.rs (+107/-8) — LuCI login switched from hand-built body string to `.form(...)` (proper url-encoding); regression test with local TCP listener asserts exact encoded body + session-cookie reuse
- asic-rs-firmwares/braiins/Cargo.toml (+1/-1) — add form/encoding support dep
- python/pyasic-rs/src/factory.rs (+18/-1) — expose per-firmware discovery auth to Python callers
- python/pyasic-rs/tests/test_factory_auth.py (+135/-0) — stock discovery + protected telemetry with custom credentials
- python/pyasic-rs/pyasic_rs/asic_rs.pyi (+2/-1) — regenerated stub
- README.md (+15/-6) and docs-shared/guide.md (+15/-6) — authentication examples updated
- Cargo.lock (+19/-0)

## Key patch excerpts

Braiins LuCI login — reserved-character-safe form encoding (`braiins/src/backends/v21_09/web.rs`):

```rust
let url = format!("http://{}:{}/cgi-bin/luci", self.ip, self.port);
let client = self.client()?;
let response = client
    .post(&url)
    .header("User-Agent", "BTC Tools v0.1")
    .form(&[
        ("luci_username", self.auth.username()),
        ("luci_password", self.auth.password()),
    ])
    .timeout(self.timeout)
    .send()
    .await
```

Previously the body was a raw `format!("luci_username={}&luci_password={}", ...)` — a password containing `&`, `+`, `=` (or spaces/unicode) corrupted authentication. The regression test pins the exact wire encoding for `MinerAuth::new("root+operator", "custom&password=+ é")`:

```text
luci_username=root%2Boperator&luci_password=custom%26password%3D%2B+%C3%A9
```

and asserts the LuCI session cookie (`Set-Cookie: session_id=custom-session`) is reused on the follow-up `GET /cgi-bin/luci/admin/network/iface_status/lan`.

Custom discovery credentials in the Rust factory (`src/factory.rs`):

```rust
/// Set construction credentials by the registered firmware's Display name.
pub fn with_firmware_discovery_auth_by_name(
    mut self,
    firmware_name: &str,
    auth: MinerAuth,
) -> Result<Self> {
    let registry = self
        .search_firmwares
        .clone()
        .unwrap_or_else(default_firmware_registry);
    let firmware = registry
        .iter()
        .find(|firmware| firmware.to_string() == firmware_name)
        .ok_or_else(|| {
            anyhow::anyhow!("Firmware is not registered for discovery authentication")
        })?;
    self.discovery_auth_by_firmware
        .insert(firmware.to_string(), auth);
    Ok(self)
}
```

Lookup is by firmware Display name (e.g. `"ForgeOS Stock"`, `"Goldshell Stock"`), so a stock miner with a non-default password can be constructed — discovery probes and authenticated telemetry then use the same credentials.
