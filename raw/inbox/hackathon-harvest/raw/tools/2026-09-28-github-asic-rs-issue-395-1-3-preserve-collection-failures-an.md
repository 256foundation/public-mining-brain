# 256foundation/asic-rs issue #395: [1/3] Preserve collection failures and retry failed transient requests

> Source: https://github.com/256foundation/asic-rs/issues/395
> Collected: 2026-10-07
> Published: 2026-09-28

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 395
- State: open
- Author: cfilipescu
- Opened: 2026-09-28
- Closed: n/a
- Labels: none

## Description

## Execution order

**1 of 3: correctness and observability first.** Complete this before tuning connection budgets or discovery throughput. The next two work items will use these outcomes to measure reliability.

## Problem and evidence

`asic-rs-core/src/data/collector.rs`, `DataCollector::collect`, runs the required API commands concurrently and caches only successful responses. Failed responses are discarded. Field parsing can consequently produce partial `MinerData` without exposing why fields are missing.

In a macOS fleet scan covering 12 /22 ranges, independent TCP checks recorded 102 local EADDRNOTAVAIL/error-49 failures during the data phase. The scan returned 2,528 device rows without MAC addresses, clustered around that period. A low-concurrency recheck recovered MACs for all 20 sampled affected devices. This supports resource-related incomplete collection, but does not establish that every absent field has the same cause.

A complete discovery count therefore does not establish complete metadata or telemetry. Legitimately unsupported fields must also remain distinguishable from failed reads.

## Proposed scope

- Preserve request/command failures with endpoint/operation context and the underlying error category, including OS errors where available. Do not expose credentials or response payloads in diagnostics.
- Represent incomplete collection through the existing collection result/model; preserve successful fields and command-level status. Choose a backward-compatible additive representation where possible and document any API impact.
- Classify transient local resource failures, connection/read deadlines, authentication errors, unsupported commands, and parse failures. Do not retry permanent failures indiscriminately.
- Retry only failed transient commands with bounded attempts and backoff after pressure falls. Keep successful command results, respect the overall deadline, and release resources on cancellation.
- Keep retries coordinated with the operation-wide budget introduced in step 2; retries must not multiply traffic during exhaustion.
- Propagate completeness/failure information through the Rust API, serialization, generated bindings, and downstream CLI's existing collect path. Do not create a second collection concept or model.

## Acceptance criteria

- [ ] A failed API request cannot silently become an indistinguishable successful complete collection.
- [ ] Successful fields survive partial failure and retry; unsupported fields are not reported as transport failures.
- [ ] Injected/local resource errors and deadlines expose actionable categories without sensitive data.
- [ ] Transient-command retries are bounded, cancelable, deadline-aware, and preserve already successful results.
- [ ] Rust and supported bindings/serialization describe the same collection outcomes.
- [ ] Add regression coverage to suites that run in this repository's existing PR CI; document platform-specific/live coverage gaps.
- [ ] Live validation compares expected available fields as well as IP counts, including a recovery check for previously incomplete devices.

## Dependency

This issue is separate from the small discovery-socket fix: backend collection clients have their own lifecycles and need explicit failure reporting. Completion is the prerequisite for the operation-wide connection-management issue (step 2).

## Related work

- Next, after this issue: https://github.com/256foundation/asic-rs/issues/396.
- Incremental discovery-only transport fix: https://github.com/256foundation/asic-rs/pull/397. This issue remains open after that PR merges.
