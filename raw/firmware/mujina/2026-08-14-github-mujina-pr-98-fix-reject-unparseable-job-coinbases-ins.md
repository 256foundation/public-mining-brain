# 256foundation/mujina pull request #98: fix: reject unparseable job coinbases instead of idling silently

> Source: https://github.com/256foundation/mujina/pull/98
> Collected: 2026-10-07
> Published: 2026-08-14

- Repository: 256foundation/mujina
- Type: pull request
- Number: 98
- State: closed
- Author: Schnitzel
- Opened: 2026-08-14
- Closed: 2026-09-28
- Labels: none

## Description

## Problem

A `mining.notify` whose `coinb1`/`coinb2` hex-decode fine (passing the job parser) but do not form a deserializable transaction is accepted and assigned to hash threads. The CPU backend's merkle computation then fails **silently**: the task is installed with no cached merkle root, the hasher spins its duty loop doing nothing, and no message at any log level names the cause. A malicious pool or stratum MITM (the transport is plaintext) can pin a miner in this looks-alive-but-idle state indefinitely — API up, pool connected, jobs arriving, zero shares.

Found during hostile-pool fuzzing (stratum-v1 battery with dummy coinbases): every pool-fed run produced zero shares and zero diagnostics, while the dummy (fixed-merkle) source mined fine.

## Fix (one commit per change)

- **`fix(job_source): reject jobs whose coinbase does not parse`** — probe the merkle computation once at template conversion; on failure the job is rejected with a visible error through the existing per-job error path (warn-and-continue, same as an invalid extranonce2 size). Test fixtures that unknowingly used unparseable coinbases (`"aa"`/`"bb"` — which is how the gap stayed invisible) now assemble a structure-valid 1-in/0-out transaction. New tests: bad coinbase rejected, valid coinbase accepted.
- **`fix(cpu_miner): warn when a task's coinbase cannot be mined`** — the hasher now warns once per offending task instead of idling silently, so any current or future job path that bypasses validation still leaves a trace. Contract tests: unparseable coinbase yields `None`, valid coinbase yields a root.

## Tests

`cargo fmt`, `cargo clippy` (no new warnings), `cargo test` (361 passed) green; each commit passes on its own. Dynamic A/B before/after on a local CPU-backend daemon: invalid coinbase → `shares=0` with zero diagnostics (before) → job rejected with `job coinbase does not parse` warning (after); valid coinbase → shares flow in both.

## Comments

### j-kon on 2026-09-15

Nice defense-in-depth here. Rejecting the coinbase during template conversion is much better than allowing an unmineable task to reach the hash threads, and keeping the CPU-side warning provides a useful fallback if another path bypasses validation.

One thing I noticed while reviewing the probe:

`Extranonce2::new(0, state.extranonce2_size as u8)?`

This still depends on narrowing `extranonce2_size` to `u8`. PR #90 makes that safe by validating the size at subscription time, but #98 is currently a separate PR.

Is the intention that #90 lands before this one? If these can merge independently, would it be worth avoiding the unchecked narrowing here as well so this validation path does not depend on #90 for that invariant?

Otherwise the valid/invalid coinbase coverage looks good, and I like that the failure becomes visible instead of leaving the miner alive but idle.

### rkuester on 2026-09-28

@Schnitzel Good catch, and it's not just the CPU backend. The BM13xx thread drops the same error, so real hardware also idles silently.

Closing in favor of #113, which uses this case as an example. There the source rejects such a job when it arrives from the upstream, so the hash threads never see it.
