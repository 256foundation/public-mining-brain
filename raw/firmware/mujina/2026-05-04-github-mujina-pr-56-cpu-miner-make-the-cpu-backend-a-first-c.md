# 256foundation/mujina pull request #56: cpu-miner: make the CPU backend a first-class citizen for API/tooling

> Source: https://github.com/256foundation/mujina/pull/56
> Collected: 2026-10-07
> Published: 2026-05-04

- Repository: 256foundation/mujina
- Type: pull request
- Number: 56
- State: open
- Author: Schnitzel
- Opened: 2026-05-04
- Closed: n/a
- Labels: none

## Description

## Summary

Three small, related changes that take the CPU mining backend from "runs and hashes" to "shows up correctly in the public API," so it's actually usable for exercising mujina end-to-end without ASIC hardware — developing against the REST API, testing UIs, prototyping integrations like exporters or message-bus bridges, etc.

- **`board/cpu.rs`** — keep the board's telemetry sender alive and publish per-thread telemetry from it.
  Previously the watch sender was bound to `_telemetry_tx` and dropped immediately on construction. `BoardRegistry::boards()` evicts any registration whose senders have all gone away, so the CPU board silently disappeared from `/api/v0/boards` (and from `MinerTelemetry.boards`) as soon as the registry was first queried. The board now snapshots each thread's status handle before handing the threads to the scheduler, then runs a small task that owns the sender and refreshes `BoardTelemetry.threads` from those handles every two seconds. Aborting the task on shutdown drops the sender, letting the registry clean up the board normally.

- **`cpu_miner/thread.rs`** — expose `status_handle()` so the board layer can read each thread's live `HashThreadStatus` (which the hasher already populates every five seconds with measured hashrate, share counts, etc.) without taking ownership of the thread itself. Ownership still goes to the scheduler.

- **`scheduler.rs`** — in `measured_hashrate()` and `operational_hashrate()`, fall back to `entry.thread.status().hashrate` when the share-based estimator has no settled value. The CPU backend measures hashrate directly from cycle counts, but at typical CPU rates against any reasonable source target it would essentially never produce shares fast enough for the estimator to settle, so the API field stayed at zero forever. ASIC backends that don't self-report keep falling through to the existing `capabilities().hashrate_estimate` constant exactly as before — this is purely an additional fallback, ordered *after* the truthful estimator and *before* the static guess.

## Why

The CPU backend exists in the tree for exactly the kind of work where you don't want to plug in (or own) real hashing hardware: developing against the API, testing the daemon end-to-end, and building tools that consume mujina's output. Today, even though the threads do hash, an API consumer sees \`{\"hashrate\": 0, \"boards\": []}\` indefinitely — which is indistinguishable from "nothing is running." That makes the CPU backend a poor base for any of those use cases. These changes close the gap so the API reflects what the backend is actually doing.

## Net effect

- On a CPU-only host: \`/api/v0/miner\` reports a non-zero aggregate \`hashrate\` within ~5s of startup, \`boards[0]\` shows up with per-thread \`hashrate\` and \`is_active\` populated.
- On ASIC hardware: behaviour is unchanged for boards whose threads don't write \`HashThreadStatus.hashrate\`. The new fallback in \`measured_hashrate()\` / \`operational_hashrate()\` only kicks in when both the share-based estimator is unsettled *and* the thread self-reports — neither condition holds for current ASIC backends.

## Test plan

- [x] \`cargo test -p mujina-miner --lib\` — existing scheduler and registry tests still pass.
- [x] Cross-built per #55 and deployed to an Antminer S19 control board (aarch64 musl):
  - Start: \`MUJINA_CPUMINER_THREADS=2 MUJINA_CPUMINER_DUTY=50 MUJINA_USB_DISABLE=1 MUJINA_API_LISTEN=0.0.0.0:7785 ./mujina-minerd\`
  - \`curl /api/v0/miner\` after ~12s:
    \`\`\`json
    {\"uptime_secs\":10,\"hashrate\":174652,\"shares_submitted\":0,\"paused\":false,
     \"boards\":[{\"name\":\"cpu-2x50%\",\"model\":\"CPU Miner\",\"serial\":\"cpu-2x50%\",
       \"fans\":[],\"temperatures\":[],\"powers\":[],
       \"threads\":[
         {\"name\":\"CPU Core 0\",\"hashrate\":89974,\"is_active\":true},
         {\"name\":\"CPU Core 1\",\"hashrate\":89964,\"is_active\":true}
       ]}],
     \"sources\":[{\"name\":\"dummy\",\"difficulty\":2328}]}
    \`\`\`
  - \`curl /api/v0/boards\` — previously \`[]\`, now lists the CPU board with the same per-thread detail.

## Notes

- Builds on top of #55 in spirit (same author, same hardware target), but doesn't depend on it — these changes work on glibc Linux too. Independent base for either merge order.

## Comments

### jayrmotta on 2026-06-09

Hey @Schnitzel, are you looking for reviews on this?
