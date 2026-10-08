# 256foundation/mujina pull request #90: fix: validate pool-controlled extranonce2_size and bound its consumers

> Source: https://github.com/256foundation/mujina/pull/90
> Collected: 2026-10-07
> Published: 2026-08-07

- Repository: 256foundation/mujina
- Type: pull request
- Number: 90
- State: closed
- Author: Schnitzel
- Opened: 2026-08-07
- Closed: 2026-09-28
- Labels: none

## Description

## Problem

The pool-supplied `extranonce2_size` (from `mining.subscribe`) flowed into job construction and work splitting with two lossy/assuming steps, all reachable by a malicious pool or a MITM (the stratum transport is plaintext):

1. **`as u8` truncation** in `job_to_template`: a size of 0 or >8 made *every* job fail template conversion — the miner stayed connected but mined nothing; a value like 264 silently wrapped to 8, mining an extranonce2 space the pool never offered (all shares invalid at the pool).
2. **`expect()` on `Extranonce2Range::split`** in the scheduler: `split` returns `None` when the range holds fewer values than there are eligible threads. Pathological size (e.g. 1 byte = 256 values) + 257+ threads → the scheduler task panicked, and since nothing supervises it, mining silently halted while the API kept serving stale telemetry.
3. **Unbounded `MUJINA_CPUMINER_THREADS`** made such thread counts trivial to reach (CPU backend) and turned typos into resource problems.

Found during a source review of pool-facing input handling.

## Fix (one commit per change)

- **`fix(stratum_v1): reject out-of-range extranonce2_size at subscribe`** — accept only the 1–8 byte range `Extranonce2` supports; fail the subscription otherwise (reconnect with the usual backoff). This also makes the downstream `as u8` provably lossless.
- **`fix(scheduler): skip jobs too small to split across threads`** — replace the `expect` with a let-else that logs (source, thread count, EN2 space) and skips the job. Regression test included: 257 stub threads vs a 1-byte EN2 space.
- **`fix(cpu_miner): clamp MUJINA_CPUMINER_THREADS to 4096`** — warning on clamp; far above any real core count.

## Tests

- `test_subscribe_rejects_out_of_range_extranonce2_size` (0, 9, 264 → `SubscriptionFailed`)
- `test_subscribe_accepts_valid_extranonce2_size` (1, 4, 8 → state set)
- `assign_job_skips_when_en2_space_smaller_than_thread_count` (no panic; no tasks assigned)
- `test_thread_count_clamped_to_max`

`cargo fmt`, `cargo clippy` (no new warnings), and `cargo test` (356 passed) are green; each commit passes on its own (verified individually).

## Comments

### j-kon on 2026-09-15

Reviewed the changes. I like the defense-in-depth approach here.

Validating `extranonce2_size` at the Stratum boundary prevents the lossy conversion from becoming reachable, while keeping the scheduler-side `split()` handling defensive means another source still cannot turn an undersized EN2 space into a scheduler panic.

The 257-thread / 256-value regression test is especially useful because it captures the exact boundary that previously reached the `expect()`.

From the code path and tests, this looks like a solid way to turn pool-controlled input from a potential silent mining halt into a handled failure.

### rkuester on 2026-09-28

@Schnitzel Good catch. This points at a larger problem, how a job source should handle and report upstream errors in general, so I wrote that up as #113 with this case as an example. Closing in favor of it.

A valid size too small to split among the hash threads is a scheduler problem, now #114.
