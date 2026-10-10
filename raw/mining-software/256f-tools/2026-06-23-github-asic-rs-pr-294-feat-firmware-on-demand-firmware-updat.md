# 256foundation/asic-rs pull request #294: feat(firmware): on-demand firmware-update check

> Source: https://github.com/256foundation/asic-rs/pull/294
> Collected: 2026-10-07
> Published: 2026-06-23

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 294
- State: closed
- Author: pos-ei-don
- Opened: 2026-06-23
- Closed: 2026-08-31
- Labels: none

## Description

Adds an on-demand "is newer firmware available?" check, separate from the telemetry poll (it hits the vendor's release server) — a UI can call it on a slow cadence (e.g. an HA `update` entity, ~daily) instead of every poll.

- New `FirmwareUpdate` result (current/latest version, `update_available`, release date/url) from `UpgradeFirmware::check_firmware_update` (default: unsupported).
- **BraiinsOS** 26.04 reads `bos.checkForUpgrade` + `bos.info.version` over the authenticated GraphQL client — a fully local check.
- Python: `Miner.check_firmware_update()` + `supports_check_firmware_update`.

**VNish — how its GUI does it, and an open question.** VNish works differently: it shows the installed version locally, but "are you up to date?" compares that against the vendor's **cloud changelog** — `GET partner.anthill.farm/api/client/releases-notes` returns a list of releases (`series` / `version` / `stage`), and the UI marks the latest stable vs. what's installed. There is **no local API field** for update-availability, so covering VNish means the lib making an **external vendor-cloud call**, unlike BraiinsOS's local check.

On our side (a Home Assistant integration alpha) we'd surface the VNish installed version there and could do the cloud comparison consumer-side. But we could also imagine putting it in the lib so `check_firmware_update` is uniform across firmwares. **What's your preference** — should a vendor-cloud lookup like VNish's live in asic-rs, or stay on the consumer side? I kept this PR to the local BraiinsOS check; happy to add VNish whichever way you'd like.


## Comments

### pos-ei-don on 2026-06-24

Thanks for the review — but before reworking I'd push back on this direction, because a couple of parts don't hold up across the firmwares:

**semver won't work as the comparison basis.** Miner firmware versions aren't semver: BraiinsOS is CalVer (`26.04`, `25.07`), and Antminer/stock builds carry arbitrary version strings. `semver::Version::parse("26.04")` fails outright, so an `update_available()` built on semver would *silently stop comparing* for most backends — including the BOS ones this PR targets. I'd rather not bake in an assumption that breaks the majority case.

**Folding the check result into a `Local(FirmwareImage)` / `Remote(URL)` enum overloads it.** The check result and the *apply* source are different concerns. For VNish the check is vendor-cloud metadata (a version + a release-notes URL) — there's no downloadable `FirmwareImage` to return, so `Local/Remote` doesn't map onto a check at all. And dropping the release URL throws away the one actionable thing a check usually produces: where to get the firmware.

What I'd suggest instead: keep this as a small read-only check result (happy to rename it `FirmwareStats`), versions as plain strings, keep the optional URL, and leave a `Local/Remote` upgrade-source as a separate type for the actual upgrade path rather than fusing it into the check. The backport to the other Braiins versions I'm glad to do once the shape is settled.

If you do want the enum/semver route, could you sketch how `update_available()` is meant to behave for CalVer (`26.04`) and arbitrary version strings? That's the part I don't see working.

### b-rowan on 2026-06-24

> **semver won't work as the comparison basis.** Miner firmware versions aren't semver: BraiinsOS is CalVer (`26.04`, `25.07`), and Antminer/stock builds carry arbitrary version strings. `semver::Version::parse("26.04")` fails outright, so an `update_available()` built on semver would _silently stop comparing_ for most backends — including the BOS ones this PR targets. I'd rather not bake in an assumption that breaks the majority case.

It already does work as our comparison basis :laughing:..

https://github.com/256foundation/asic-rs/blob/548fdf83aab5a54daafa0300a21d0f6e6790d0e7/asic-rs-firmwares/braiins/src/backends/mod.rs#L24-L35

https://github.com/256foundation/asic-rs/blob/548fdf83aab5a54daafa0300a21d0f6e6790d0e7/asic-rs-firmwares/braiins/src/firmware.rs#L113-L141

We just append a `PATCH` version if one doesn't exist, it doesn't need to be exactly semver, it just needs to be comparable, and calver is close enough.  Some versions don't even need the extra value appended (see https://downloads.braiins.com/braiins-os/#6de99434-9996-4c9a-819b-e4121db4b3ca)



> And dropping the release URL throws away the one actionable thing a check usually produces: where to get the firmware.

Not exactly what I meant.

```rust
struct FirmwareStats {
    current_version: Option<SemVer>,
    latest_version: Option<SemVer>,
    firmware: Option<FirmwareUpdate>
}

impl FirmwareStats {
    fn update_available {
        // compare current to latest
        ...
    }
}

enum FirmwareUpdate {
    Local(FirmwareImage),
    Remote(URL)
}
```

### pos-ei-don on 2026-06-24

Done in `fd3990e` — reworked to your shape:
- `FirmwareUpdate` → `FirmwareStats { current_version, latest_version: Option<Version>, firmware: Option<FirmwareUpdate> }`
- `update_available()` is now derived from comparing the versions
- `enum FirmwareUpdate { Local(FirmwareImage), Remote(String) }` for the source; dropped `release_date`

You were right on the version point — the `.0`-pad approach handles CalVer fine, so I pulled the BOS parse out of `get_version` into a shared `parse_bos_version` helper and use it for both the installed and latest versions. As a bonus the derived comparison fixes a latent bug: the old `latest != current` string check flagged an update even when `latest` was *older*; `latest > current` is correct.

One note: nothing populates `Local(FirmwareImage)` today — the BOS check returns a URL, so it maps to `Remote`. I kept `Local` for the download-then-flash path (and to line up with `upgrade_firmware(FirmwareImage)`), but happy to drop it if you'd rather keep the enum to just what's produced now.

CI green (Cargo + Python).

### pos-ei-don on 2026-08-30

Rebased onto v0.8.0 — reconciled with the new power_target_capabilities in the braiins util and dropped a now-duplicate parse_configured_tuning_target (the algo-aware version is upstream now). cargo check is green.

### b-rowan on 2026-08-31

@cfilipescu Can I get a second opinion on this one?  Just want to confirm this is the direction we want to go...
