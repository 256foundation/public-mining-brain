# 256foundation/asic-rs pull request #397: fix(scanner): reduce local port pressure during discovery

> Source: https://github.com/256foundation/asic-rs/pull/397
> Collected: 2026-10-07
> Published: 2026-09-28

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 397
- State: closed
- Author: cfilipescu
- Opened: 2026-09-28
- Closed: 2026-09-28
- Labels: none

## Description

## Summary

Reduce local TCP port pressure during large discovery scans and preserve connection diagnostics.

- Create IPv4/IPv6 reachability probes with `TcpSocket` and set zero linger before connecting. These temporary probes exchange no application data; close/cancellation can reset them without keeping local ports in TIME_WAIT.
- Ask the peer to close HTTP connections with `Connection: close` in the discovery client and shared utility HTTP client. Both already use `pool_max_idle_per_host(0)`; the shared utility client also serves non-discovery utility requests.
- Log socket allocation failures, connect errors including raw OS codes, probe timeouts, successful identification, and underlying RPC connect errors.

Firmware command selection, identification order, timeouts, and public APIs are unchanged. Backend-specific HTTP clients and their pools are outside this patch.

## Why

Instrumented macOS scans over 12 /22 ranges (12,288 addresses) recorded thousands of EADDRNOTAVAIL/error-49 failures. These previously became failed reachability without preserving the cause. The configured ephemeral range contained 16,384 ports, and a snapshot showed 12,340 TIME_WAIT plus 3,800 established connections. Raising file-descriptor limits does not address this separate resource limit.

Probe cleanup alone was insufficient at higher concurrency. With zero-linger probes but without the HTTP close change, one 512-concurrency scan reported 10,843 allocation failures. With both changes, a corresponding scan identified 5,374 devices and instrumented discovery probes reported no allocation failures, versus 4,017 devices in the probe-only experiment. These are observed runs under variable conditions, not a controlled statistical benchmark.

No sudo or system-setting changes were needed.

## Validation

- `cargo fmt --all -- --check` passes.
- `git diff upstream/master...HEAD --check` passes.
- Release consumer builds and repeated live fleet scans exercised the combined changes on macOS. Experimental builds used LTO disabled and 16 codegen units; compilation time was excluded from scan timings.
- Existing unit/binding tests were not run locally in this investigation; the upstream PR workflows provide Rust, Python, and Go coverage. No new tests are included. Cross-platform close behavior and deterministic socket-lifecycle regression coverage remain review/validation gaps.

## Known remaining work

This patch is an incremental discovery fix. Later instrumentation found port exhaustion during backend data collection, where some failed API responses are silently discarded. A zero allocation-error count from discovery probes does not establish error-free or complete collection.

- https://github.com/256foundation/asic-rs/issues/395 — first expose collection failures and bound retries.
- https://github.com/256foundation/asic-rs/issues/396 — then coordinate connection lifecycles and budgets across discovery and collection.

Separate pacing/deadline work is also needed: packet capture observed responsive miners replying after a caller's 500 ms probe deadline. This PR does not claim complete discovery under arbitrary load or a 50-second full-fleet scan.
