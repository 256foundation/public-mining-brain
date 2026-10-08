# 256foundation/asic-rs issue #190: Power mode support (Low/Normal/High).

> Source: https://github.com/256foundation/asic-rs/issues/190
> Collected: 2026-10-07
> Published: 2026-03-19

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 190
- State: closed
- Author: ankitgoswami
- Opened: 2026-03-19
- Closed: 2026-03-20
- Labels: none

## Description

We have a use-case for switching miners between power modes (Low/Normal/High). My service maps user-facing performance profiles (like "max hashrate" or "efficiency") to the underlying firmware mode so I need a generic way to call set.miner.mode on WhatsMiner and the equivalent on Antminer.

I noticed the Antminer backend already has a MinerMode enum internally but it's only wired up for pause/resume. And WhatsMiner's status JSON includes power_mode but it's not parsed.

SetPowerLimit and TuningConfig don't exactly cover this they're continuous values, not discrete firmware profiles. Was this left out on purpose, or just hasn't been built yet? I'm thinking of adding a SetPowerMode trait to HasMinerControl if that's welcome.

## Comments

### b-rowan on 2026-03-19

Hasn't been built yet, definitely planned.  It should be implemented as part of the (relatively new) `SupportsTuningConfig` method (and probably also updated in `GetTuningMode`).

Here is an example implementation from the ePIC firmware - https://github.com/256foundation/asic-rs/blob/574574d144111c9b4d7d7e6fd9c4f480840b8abd/asic-rs-firmwares/epic/src/backends/v1/mod.rs#L1134-L1155

`High`/`Normal`/`Low` variants will also need to be added to `TuningConfig`/`TuningMode`, likely like this:

```rust
enum MiningMode {
	High,
	Normal,
	Low
}

enum TuningConfig {
	...
	MiningMode(MiningMode)
}

```
