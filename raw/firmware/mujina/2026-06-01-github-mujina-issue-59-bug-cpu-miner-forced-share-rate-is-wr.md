# 256foundation/mujina issue #59: bug(cpu_miner): forced share rate is wrong and never converges

> Source: https://github.com/256foundation/mujina/issues/59
> Collected: 2026-10-07
> Published: 2026-06-01

- Repository: 256foundation/mujina
- Type: issue
- Number: 59
- State: open
- Author: rkuester
- Opened: 2026-06-01
- Closed: n/a
- Labels: none

## Description

With the CPU backend, `MUJINA_POOL_FORCED_RATE` doesn't produce the configured share rate. At the default `MUJINA_CPUMINER_DUTY=50` it finds shares at about half the requested rate, and lower duty slows them proportionally (a forced rate of 6/min at 50% duty gives roughly 3/min). It's also off on any machine whose cores aren't near 5 MH/s. Thread count doesn't matter.

It never corrects itself: the rate is wrong from the start and stays wrong for the whole run, instead of converging as the miner measures its actual hashrate.

This looks like a side effect of `a5c3e62` (`feat(scheduler): send hashrate to sources only when boards change`), which dropped the periodic hashrate broadcast to avoid flooding the pool with difficulty suggestions. The forced-rate wrapper needed that broadcast to learn the measured hashrate. Without it, the wrapper only hears a rate at startup before any hashing happens, so it's stuck on the fallback estimate: a flat per-core guess that ignores duty cycle.

## Comments

### rkuester on 2026-06-01

Working on this now as part of a bigger fix around difficulty suggestions as hashrate changes.

### rkuester on 2026-06-15

> Working on this now as part of a bigger fix around difficulty suggestions as hashrate changes.

[rkuester:fix-cpu-forced-rate](https://github.com/256foundation/mujina/compare/main...rkuester:mujina:fix-cpu-forced-rate)

### jayrmotta on 2026-06-15

Sharing [this](https://github.com/stratum-mining/sv2-apps/issues/354#event-23869631392) here to emphasize the importance our CPU miner has for various projects.

It has been used by @plebhash during Vinteum's BDL in a mining workshop, and it seems to be used by folks at P2PoolV2 as well.

This comment doesn't add or question anything, just pointing out this is being actively used out there.
