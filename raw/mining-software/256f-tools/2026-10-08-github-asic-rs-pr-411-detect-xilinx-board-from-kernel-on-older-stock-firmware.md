# asic-rs PR #411: fix(antminer): detect Xilinx board from kernel on older stock firmware

> Source: https://github.com/256foundation/asic-rs/pull/411
> Collected: 2026-10-10
> Published: 2026-10-08
> Registry ID: asic-rs

State: closed | Merged: 2026-10-08 | Author: cfilipescu | +81/-14 | Commits: 1

## Body

## Summary

Older Antminer stock firmware can return 404 for `miner_type.cgi`, leaving `control_board_version` unset even when `get_system_info.cgi` identifies a Xilinx kernel. This occurs on an Antminer Z15 running stock firmware with `Linux 4.6.0-xilinx-g0387054-dirty`.

Collect both the miner subtype and the system kernel version. Prefer a recognized subtype; when it is absent or unrecognized, identify Xilinx from the `-xilinx` kernel marker. Other kernels remain unidentified.

## Validation

- `cargo test -p asic-rs-firmwares-antminer --locked` (38 passed, 3 ignored)
- `cargo fmt --all --check`
- `git diff --check`
- Regression test covers the Z15 kernel fallback, subtype precedence, and a kernel without a Xilinx marker.

## Files changed

- asic-rs-firmwares/antminer/src/backends/v2020/mod.rs (+81/-14) — `ControlBoardVersion` now collects both `miner_type.cgi` `/subtype` and `get_system_info.cgi` `/system_kernel_version`; board parse falls back to Xilinx on `-xilinx` kernel marker; regression test added

## Key patch excerpts

Data collection: two sources for one field (`DataField::ControlBoardVersion` locations in `AntMinerV2020`):

```rust
DataField::ControlBoardVersion => vec![
    (
        WEB_MINER_TYPE,
        DataExtractor {
            func: get_by_pointer,
            key: Some("/subtype"),
            tag: Some("subtype"),
        },
    ),
    (
        WEB_SYSTEM_INFO,
        DataExtractor {
            func: get_by_pointer,
            key: Some("/system_kernel_version"),
            tag: Some("kernel_version"),
        },
    ),
],
```

Fallback logic — subtype wins, kernel marker is the fallback (`impl GetControlBoardVersion for AntMinerV2020`):

```rust
let subtype = data.extract_nested::<String>(DataField::ControlBoardVersion, "subtype");
let board = subtype.as_deref().and_then(|cb_type| {
    if cb_type.to_ascii_uppercase().contains("AML") {
        Some(AntMinerControlBoard::AMLogic)
    } else {
        AntMinerControlBoard::parse(cb_type.split('_').next()?)
    }
});

board
    .or_else(|| {
        let kernel_version = data
            .extract_nested::<String>(DataField::ControlBoardVersion, "kernel_version")?;
        kernel_version
            .to_ascii_lowercase()
            .contains("-xilinx")
            .then_some(AntMinerControlBoard::Xilinx)
    })
    .map(Into::into)
```

Regression test cases (kernel strings grounding the behavior):

```rust
(None, "Linux 4.6.0-xilinx-g0387054-dirty #45 SMP PREEMPT", Some("Xilinx")),
(Some("BeagleBoneBlack_B"), "Linux 4.6.0-xilinx", Some("BeagleBoneBlack")),
(None, "Linux 4.9.113 #1 SMP PREEMPT", None),
```

i.e. subtype `BeagleBoneBlack_B` still wins over a Xilinx kernel marker; a non-Xilinx kernel (`Linux 4.9.113`) stays unidentified.
