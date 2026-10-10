# 256foundation/asic-rs pull request #320: fix: improve large subnet scan reliability

> Source: https://github.com/256foundation/asic-rs/pull/320
> Collected: 2026-10-07
> Published: 2026-07-29

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 320
- State: closed
- Author: DanNicolau
- Opened: 2026-07-29
- Closed: 2026-08-26
- Labels: none

## Description

Closes #319 

## Summary

  - Fixed connectivity retry semantics.
  - Probe all four ports concurrently rather than sequentially.
  - Complete TCP probing across the range before starting identification.
  - Use separate TCP and identification concurrency limits.
  - Correct connectivity_retries, which previously acted more like a boolean gate and did not perform the configured number of
    attempts.
  - Added separate TCP/identification concurrency, timeout, retry, and strict-gating controls.
  - Set measured defaults: TCP 256/500 ms, identification 128/3 s, construction 5 s, no retries.
  - Probe common miner ports concurrently and stream identifications as they finish.
  - Added HTTP request deadlines and a miner-construction deadline.
  - Added matching Rust/Python builder APIs and documentation.

 ## Performance

11.7s to scan a /22 subnet with 441 target devices

  ## Reliability considerations

  The initial benchmark ran Nmap immediately before each test, which warmed neighbor and ARP state. Cold end-to-end scans demonstrated that
  TCP probing could still miss responsive miners transiently. For this reason, TCP results are not a hard exclusion by default.

  Strict filtering is still available for callers that prefer minimum scan time and can tolerate possible false negatives.

  ## Validation

  - cargo test -p asic-rs
  - All asic-rs doctests
  - cargo clippy -p asic-rs --all-targets --all-features -- -D warnings
  - Python builder methods and type stubs updated
  - End-to-end validation on the target /22 network


## Comments

### b-rowan on 2026-07-29

50 seconds to scan a /22 seems really high to me?  Gotta be some way to improve past that...

### DanNicolau on 2026-07-29

Yeah, I'm not thrilled about that result either (it's closer to 2m with the tcp probe and the miner discovery added together). I'll move it from a draft once I get something I think is effective.

### b-rowan on 2026-07-29

Not sure if its just me or what, scanning a local network, /20 subnet (~4k addresses), it seems to have no consistency issues AFTER an initial run.  For some reason that first run just wants to miss stuff.  Is there anything we can do to make the ARP table less garbage at its job?

### DanNicolau on 2026-07-29

I also do see significant improvements once the ARP table/cache starts getting filled out.

### b-rowan on 2026-07-29

Some sloppified suggestions, maybe somewhere to start looking.   I have curated out the irrelevant ones, but some things to look into here possibly.


---

## Scan reliability and concurrency findings

After reviewing `factory.rs`, the relevant issues are:

### Confirmed issues

1. **`connectivity_retries` does not perform retries**

   The current check only determines whether the configured value is greater than one. Regardless of the configured value, each port is probed at most once.

   This can cause false negatives during transient packet loss, initial ARP resolution, or network congestion.

2. **Sequential port checks can be slow, while parallel checks could amplify concurrency**

   Ports `80`, `4028`, `4029`, and `8889` are checked sequentially, with an early return after the first successful connection.

   The early-return behavior is intentional, but on an unreachable or filtered host, each timeout is incurred in sequence. With the default one-second timeout, a host can take roughly four seconds to reject.

   Simply checking all ports concurrently would improve latency but could multiply the number of simultaneous connections by four. A globally bounded or staggered port race may provide a better balance.

### Possible contributing issues

3. **The configured concurrency limit applies to hosts, not individual connections**

   `buffer_unordered` limits the number of hosts being scanned, but each responsive host can then execute multiple discovery commands concurrently.

   As a result, the actual number of active sockets may be several times higher than the configured host concurrency. The existing file-descriptor estimate accounts for some fan-out, but it does not enforce a hard socket limit.

   Possible changes include:

   * Reducing the default host concurrency.
   * Adding a separate global connection semaphore.
   * Deriving the host limit from the number of expected connections per host.

4. **There is no connection-start rate limit**

   A large concurrency value allows many connections—and potentially many ARP requests—to begin in a short burst.

   Even when the scanner has sufficient file descriptors, this can overload network queues, neighbor discovery, firewalls, or embedded devices and lead to intermittent false negatives.

   A connection-rate limiter may improve accuracy without substantially reducing throughput.

### Lower-priority follow-ups

5. **Discovery configuration is rebuilt for each responsive host**

   The firmware registry and deduplicated discovery-command set could be calculated once per scan and shared between host scans. This would reduce allocations and repeated setup work, though it is unlikely to be the main cause of the current scanning problem.

6. **HTTP discovery responses are read without an explicit size limit**

   Reading the complete response is useful for some device identification methods, but unrelated web services could return large responses. A configurable or sufficiently generous response limit may be worth considering.

## Suggested initial changes

The highest-priority change is to fix `connectivity_retries` so it performs the configured number of attempts.

After that, testing should compare:

* Lower host concurrency.
* A separate global socket limit.
* Staggered or bounded concurrent port checks.
* A connection-start rate limit.

Metrics for timeouts, refused connections, unreachable hosts, resource errors, and retry recoveries would help determine whether missed devices are caused by transient network loss or local resource exhaustion.


### b-rowan on 2026-07-29

Maybe also worth looking at the relevant scanning section from btctools, it seems pretty consistent.

https://github.com/btccom/libbtctools/blob/master/src/miner/MinerScanner.cpp

### DanNicolau on 2026-07-29

I'll take a look, I appreciate the direction.

### DanNicolau on 2026-07-31

Benchmarks significantly improved with these defaults, and changes to the tcp retries. Sometimes on a cold network scan it will drop considerable miners, but I don't see a simple way to get around that. In this test environment over a vpn to another farm the ARP caching happens downstream so just running it again is the best I can do.

I found that there was a potential unlimited wait for certain umcos endpoints for the identification stage, and those now time out. I was unable to reproduce those situations running repeated scans for 6 hours but it's the only place I see the potential for multi-minute scans to get stuck.

Probably best for other issues so I didn't include the changes here:
- global semaphore -- right now because we parallelize the tcp-probe ports (which has an observable benefit rather than serializing all the ports) we can spawn more connections than our tcp concurrency. to be more correct we would probably need to take connections from a global semaphore.
- connection start rate limiting -- I couldn't isolate this from ARP table warming up downstream so it may or may not have a benefit. It is probably also dependent on downstream networking hardware.

---

## Update summary

  ### Updated defaults

  - TCP probe concurrency: 256 addresses
  - Firmware-identification concurrency: 128 hosts
  - TCP probe timeout: 500 ms
  - TCP retries: 0 additional attempts
  - Identification retries: 1 additional attempt
  - Identification retry concurrency: 8
  - Identification retry backoff: 250 ms
  - Strict TCP filtering enabled by default
  - Firmware-identification timeout: 3 seconds
  - Miner-construction timeout: 5 seconds
  - Discovery HTTP connect timeout: 2 seconds
  - Discovery HTTP total timeout: 3 seconds

  TCP ports 80, 4028, 4029, and 8889 are checked concurrently for each address. TCP probing and firmware identification remain separate bounded stages.

  The connectivity retry behavior was corrected so that configuring zero retries still performs the initial TCP attempt.

  APIs.

  ### Benchmark results

  Testing used a routed /22 network with approximately 461 supported devices.

  The selected configuration consistently found 460 devices in five consecutive end-to-end release scans, completing in approximately 19.6–21.5 seconds.

  Identification concurrency remained above 99% recall through 256, but degraded at higher values:

   Concurrency    Mean detected    Minimum recall    Mean duration
  ━━━━━━━━━━━━━  ━━━━━━━━━━━━━━━  ━━━━━━━━━━━━━━━━  ━━━━━━━━━━━━━━━
           128            460.0            99.78%           20.5 s
  ─────────────  ───────────────  ────────────────  ───────────────
           256            460.0            99.78%           20.8 s
  ─────────────  ───────────────  ────────────────  ───────────────
           320            459.3            99.57%           36.7 s
  ─────────────  ───────────────  ────────────────  ───────────────
           384            457.0            97.83%           22.3 s

  A separate TCP-probe benchmark produced 100% recall across five runs at concurrency 256 and averaged approximately 1.58 seconds. Misses began appearing at concurrency 478.

  Latency measurements across roughly 4,500 successful device constructions supported the new timeout bounds. Miner construction had a p99.9 of approximately 2.7 seconds and a maximum of approximately 3.0 seconds, leaving meaningful
  headroom beneath the five-second deadline.

  A global socket semaphore and connection-start rate limiter were not added. The current evidence did not isolate connection-start rate as a problem independently of network and neighbour-cache warm-up effects.

  ### Validation

  - 9 unit tests passed
  - 10 doctests passed
  - Strict Clippy passed with warnings denied
  - Formatting and diff checks passed
  - Repeated end-to-end validation completed on the target /22 network

### DanNicolau on 2026-07-31

I'd also like some input on the desired scope of PRs. I can subdivide PRs into more atomic changes like update constants, make tcp port scan parallel etc if that would make review easier. In my head these are all scan improvements so they belong together.

These current changes are full of AI slop so I still have to review them before I take this out of draft -- but I am happy with what the benchmarking shows.

### DanNicolau on 2026-08-26

Closing this and will be superceded by more focused PRs
