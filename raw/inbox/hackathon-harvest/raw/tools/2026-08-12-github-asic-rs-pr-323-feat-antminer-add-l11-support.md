# 256foundation/asic-rs pull request #323: feat(antminer): add L11 support

> Source: https://github.com/256foundation/asic-rs/pull/323
> Collected: 2026-10-07
> Published: 2026-08-12

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 323
- State: closed
- Author: cryptographicturk
- Opened: 2026-08-12
- Closed: 2026-08-12
- Labels: none

## Description

Adds the Antminer L11 to the AntMiner model enum and hardware table.

## Hardware shape

Verified against 35 live L11s (firmware `FR-1.2(251206-L11&L11Pro)`, miner version `86.48-2.0.0`), cross-checked from two independent endpoints on the same device:

| Source | Boards | Chips/board | Fans |
| --- | --- | --- | --- |
| `/cgi-bin/stats.cgi` | `chain_num: 3` | `asic_num: 88` | `fan_num: 4` |
| cgminer 4028 `stats` | `miner_count: 3` | `chain_acn1..3: 88` | `fan_num: 4` |

**3 boards × 88 chips = 264, 4 fans.**

Measured on the same miner before and after this change:

```
before:  model=ANTMINER L11 (Unknown)
         hardware: boards=None  board_count=None
         hashboards: 0
         expected_chips=None  total_chips=None

after:   model=L11
         hardware: boards=Some([Some(88), Some(88), Some(88)])  board_count=Some(3)
         hashboards: 3
           board[0] working_chips=Some(88) expected_chips=Some(88) active=Some(true)
           board[1] working_chips=Some(88) expected_chips=Some(88) active=Some(true)
           board[2] working_chips=Some(88) expected_chips=Some(88) active=Some(true)
         expected_chips=Some(264)  total_chips=Some(264)
```

An L9 on the same firmware family was used as a control and behaves identically, which is the intended outcome — the L11 now matches an already-supported sibling exactly.

## Verification

- `cargo fmt --all -- --check` — clean
- `cargo clippy --workspace --all-features` — no new diagnostics
- `cargo test -p asic-rs-makes-antminer` — passing
- `python scripts/docs/gen_supported_devices.py` — regenerated; the docs change in this PR is entirely generator output
- Live check against multiple L11s on a production farm, with an L9 on the same firmware family as a control

## Two pre-existing issues found while testing — not addressed here

Both affect the already-supported L9 identically, so they are not L11-specific and are deliberately left out of this PR. Happy to open separate issues or PRs if useful:

1. **`chain_rate{idx}` is parsed as a string, but this firmware emits a JSON number.** `parse_hashboards` does `.and_then(|v| v.as_str())`, so per-board `hashrate` is always `None` on `86.48-2.0.0`. The values are present: `"chain_rate1": 6.790325248`.

2. **`temp_pcb{idx}` does not exist on this firmware.** It reports `temp_in_pcb_1..3` / `temp_out_pcb_1..3` (and `temp_in_chip_*` / `temp_out_chip_*`), so per-board `board_temperature` is always `None`. The 4-field temperature model added in 0.7.0 looks like a natural fit for these keys.

There is also a smaller one: `get_system_info.cgi` reports `"Algorithm": "Scrypt"` for both L11 and L9, but the AntMiner make reports `SHA256` for both. Again pre-existing and not L11-specific.
