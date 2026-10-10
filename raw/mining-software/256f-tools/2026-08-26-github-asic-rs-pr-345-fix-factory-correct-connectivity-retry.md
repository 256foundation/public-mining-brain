# 256foundation/asic-rs pull request #345: fix(factory): correct connectivity retry semantics

> Source: https://github.com/256foundation/asic-rs/pull/345
> Collected: 2026-10-07
> Published: 2026-08-26

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 345
- State: closed
- Author: DanNicolau
- Opened: 2026-08-26
- Closed: 2026-08-27
- Labels: none

## Description


part of #319 

---

## Summary

  Fix MinerFactory::connectivity_retries so it performs the configured number of retries.

  Previously, the value only acted as a Boolean gate:

  - Values 0 and 1 skipped connectivity probing entirely.
  - Values greater than 1 performed exactly one probe pass.
  - No connectivity retries were actually attempted.

  This change defines connectivity_retries as additional attempts after one mandatory initial probe.

  ## Behavior

  - 0 means one initial connectivity attempt and no retries.
  - 1 means one initial attempt plus one retry.
  - Retries use exponential backoff starting at 100 ms and capped at 2 seconds.
  - Initial attempts and retries remain within the same per-address operation and existing scan concurrency bound.
  - The existing asic-rs default of 3 is preserved.
  - Port order, port concurrency, connectivity timeout, and identification behavior are unchanged.

  No additional retry-concurrency or public backoff settings are introduced.

  ## Benchmark

  Tested against a routed /22 network with 467 expected miners.

  Three alternating trials compared equivalent one-pass behavior:

  - Upstream b17670f: connectivity_retries = 3, which currently gates one probe pass.
  - This branch: connectivity_retries = 0, meaning one initial attempt with no retries.

   Trial    Upstream                  This branch
  ━━━━━━━  ━━━━━━━━━━━━━━━━━━━━━━━━  ━━━━━━━━━━━━━━━━━━━━━━━━
   1        466 devices / 18.672 s    466 devices / 18.330 s
  ───────  ────────────────────────  ────────────────────────
   2        465 devices / 18.348 s    465 devices / 18.956 s
  ───────  ────────────────────────  ────────────────────────
   3        466 devices / 18.188 s    466 devices / 18.886 s

  Median discovery time was 12.582 seconds upstream and 12.808 seconds with this change. Every matched trial found the same
  number of devices. No retry or backoff ran in either configuration, showing no material change to one-pass performance or
  recall.

  ## Validation

  - Tests cover zero retries, exact attempt counts, recovery, exhaustion, the preserved default, and bounded exponential
    backoff.

  - Full workspace tests and doctests passed before rebase.
  - All factory tests passed after rebasing over master.
  - Strict workspace Clippy passed with warnings denied.
  - Formatting and diff checks passed.

  ## Scope

  This PR does not add concurrent port probing, separate TCP concurrency controls, staged scanning, or identification
  retries. Those are intentionally left for independent follow-up PRs.
