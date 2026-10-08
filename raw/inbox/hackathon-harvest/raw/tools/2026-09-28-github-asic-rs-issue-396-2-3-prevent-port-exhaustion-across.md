# 256foundation/asic-rs issue #396: [2/3] Prevent port exhaustion across discovery and backend collection

> Source: https://github.com/256foundation/asic-rs/issues/396
> Collected: 2026-10-07
> Published: 2026-09-28

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 396
- State: open
- Author: cfilipescu
- Opened: 2026-09-28
- Closed: n/a
- Labels: none

## Description

## Execution order

**2 of 3: prevent resource exhaustion throughout the operation.** Depends on https://github.com/256foundation/asic-rs/issues/395 for collection-failure reporting and bounded retry semantics. Complete before aggressive throughput tuning in step 3.

## Problem and evidence

The discovery fixes reduce port pressure for no-data TCP probes and non-pooling utility HTTP clients. Firmware backend clients still manage their own pools and requests. A large scan can retain thousands of identified miner handles before reading their data, while each data read fans out into several API requests.

During macOS fleet scans with a 16,384-port ephemeral range, independent TCP checks encountered EADDRNOTAVAIL/error 49 during data collection even when instrumented discovery probes reported no allocation errors. Socket snapshots included:

- 12,692 TIME_WAIT + 3,618 ESTABLISHED.
- 13,803 TIME_WAIT + 2,579 ESTABLISHED.
- 14,576 TIME_WAIT + 1,809 ESTABLISHED.

These counts include other local activity and are not exact one-to-one port accounting. Together with allocation failures they establish local port exhaustion. Increasing file-descriptor limits does not fix this separate resource problem.

## Proposed scope

- Audit connection creation, pooling, reuse, close behavior, and request fan-out across discovery/model building and backend data collection.
- Introduce coordinated budgets/backpressure for network operations, including backend API requests and retries. A miner-level concurrency limit alone does not bound connections when each miner starts several requests.
- Bound retained idle clients/connections while miners wait for downstream work. Coordinate with downstream pipelining so data processing can release resources promptly.
- Preserve useful reuse within a device's read sequence and repeated collection. Measure lifecycle changes rather than unconditionally disabling every backend pool.
- Keep abortive close restricted to empty reachability probes; actual application requests must complete without truncation.
- Respond to local allocation/descriptor pressure with bounded backoff and reduced load. Respect overall deadlines and cancellation.
- Implement a portable default that works under existing system settings. No required sudo, sysctl, registry edits, or raised ulimit for end users.

## Acceptance criteria

- [ ] Repeated full-fleet discovery plus collection avoids local allocation errors under the unchanged macOS ephemeral range.
- [ ] Available metadata/telemetry is complete according to step 1's outcomes; complete IP counts cannot hide partial reads.
- [ ] Measure established, connecting, and TIME_WAIT sockets through every stage, including repeated runs and cancellation.
- [ ] Bound request fan-out and retries across the complete operation; document whether limits are per factory, client, or shared operation.
- [ ] Verify HTTP/RPC response integrity and continued pooling/reuse behavior for long-lived collection callers.
- [ ] Exercise supported platforms through existing PR CI and document remaining live-platform coverage.
- [ ] Integrate downstream changes through the existing scan/collect path without introducing another telemetry collection model.

## Handoff to step 3

Publish the safe connection envelope and metrics so discovery pacing can optimize throughput without recreating data-phase exhaustion.

## Related work

Incremental discovery transport fix: https://github.com/256foundation/asic-rs/pull/397. Its utility-client changes do not cover backend collection clients, so this issue remains open after that PR merges.
