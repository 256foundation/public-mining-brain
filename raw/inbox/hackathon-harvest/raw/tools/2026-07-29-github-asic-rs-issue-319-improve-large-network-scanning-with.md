# 256foundation/asic-rs issue #319: Improve large-network scanning with staged TCP probing

> Source: https://github.com/256foundation/asic-rs/issues/319
> Collected: 2026-10-07
> Published: 2026-07-29

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 319
- State: open
- Author: DanNicolau
- Opened: 2026-07-29
- Closed: n/a
- Labels: none

## Description

### Problem

  asic-rs scans become unreliable under high concurrency. On a /22 network:

  - Nmap found 478 hosts with ports 80 or 4028 open in 18 seconds.
  - asic-rs found 461 miners with concurrency 64 and a 10-second timeout, but took 9 minutes.
  - Higher concurrency was faster but missed many devices.
  - Retrying misses at lower concurrency recovered most devices.

  Address concurrency can also produce multiple simultaneous HTTP/RPC requests per host, increasing the actual network load.

  ### Proposal

  Use a two-stage scan:

  1. Concurrently probe miner TCP ports with a short timeout and dedicated concurrency limit.
  2. Run application-level identification only on responsive hosts, using a lower independent concurrency limit.

  The scanner should distinguish between:

  - Identified miners.
  - TCP-responsive but unidentified hosts.
  - Unresponsive hosts.

  The existing port check is not ideal for this because it checks ports sequentially and acts as a hard gate.

Before selecting defaults, I can benchmark probe timeout, probe concurrency, identification concurrency, and retries across repeated scans and select some statistically supported values to minimize time to detect all miners on the large network through a vpn (which is a common use case) 

---

 Would this design fit MinerFactory, or is another separate scanner abstraction preferred?


## Comments

### b-rowan on 2026-07-29

This seems to be an ongoing thing, I swear I can never nail down what causes these inconsistencies.  I have no issues on a /22 with a small number of miners, but it seems related to the number of machines on a network possibly?  Open to changes here, but nothing I've tried has worked consistently AND fast.  Let me know what your ideas are and we can run some tests.

RE whether it belongs in `MinerFactory`, I think that makes sense.  At the very least it would be nice to improve the logic there, but not sure about adding a 3rd "responsive but unknown" type.  That would likely only show up in the case of an unknown firmware, which should ideally just be reported and fixed...

### DanNicolau on 2026-07-29

I'm currently working on a slower /22 network with about 450 miners. I'm collecting some data and I'll have some changes with results in a PR soon.
