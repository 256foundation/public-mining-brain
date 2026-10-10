# 256foundation/asic-rs pull request #398: perf(factory): cap firmware identification concurrency

> Source: https://github.com/256foundation/asic-rs/pull/398
> Collected: 2026-10-07
> Published: 2026-09-28

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 398
- State: open
- Author: cfilipescu
- Opened: 2026-09-28
- Closed: n/a
- Labels: none

## Description

## Summary

- Add a separate firmware-identification concurrency limit to `MinerFactory` scans.
- Let address workflows continue through TCP probing while firmware identification remains bounded.
- Preserve existing behavior when callers do not configure the new limit.
- Expose `MinerFactory::probe_stream_with_ip()` to run candidate-port connectivity checks without firmware identification.
- Add `MinerFactory::probe_ports_stream_with_ip()` for per-port TCP connection timings.
- Add `MinerFactory::probe_ports_stream_with_ip_retry_timeouts()` to retry timed-out port connections with fresh sockets. It retries only timeouts, stops on the first success, and stops immediately on other connect errors or socket allocation failures. Every attempt shares the configured connection limit and timeout.
- Classify OS-reported timeouts and successful connects observed after their configured deadline as timeouts, so callers do not accept late completions as successes.
- Treat OS-reported timeouts as timeouts, and reject successful connects observed after the configured deadline so they proceed through timeout recovery.
- Include initial timeout, retry, connect error, socket allocation error, and successful latency data in each `PortProbeResult`.

This supports the UMC scanner's staged scan: it schedules up to 512 address workflows while limiting firmware identification to 128 concurrent miners. The probe stream measures TCP connection establishment, not an application-level response. The CLI uses a 100 ms per-attempt timeout and up to three timeout retries by default; there is no longer a longer fallback attempt after retry exhaustion.

On the test network, the staged scan avoided the long full-range retry and scanned one `/22` in 10.1 seconds (251 devices) and the combined 12 `/22` ranges in 87.8–97.3 seconds (5,366–5,407 devices). Results varied between consecutive runs, and the timings include device reads. A separate 500 ms probe before this strict-deadline change reported some successful connects above 500 ms; that observation motivated the deadline enforcement added here.

## Validation

- `cargo fmt --all`
- `cargo check --all-features --locked -p asic-rs`
- `cargo check --locked --features engineering -p rig-runner-cli` with this branch pinned
- `cargo check --locked -p rig-runner-cli`
- No tests were run.


## Comments

### cfilipescu on 2026-09-30

still a work in progress, trying to speed up the scan. not sure if we even need this
