# 256foundation/mujina issue #49: bug: clamp being used incorrectly after hours running

> Source: https://github.com/256foundation/mujina/issues/49
> Collected: 2026-10-07
> Published: 2026-03-12

- Repository: 256foundation/mujina
- Type: issue
- Number: 49
- State: closed
- Author: rkuester
- Opened: 2026-03-12
- Closed: 2026-03-13
- Labels: none

## Description


### Discussed in https://github.com/256foundation/mujina/discussions/48

<div type='discussions-op-text'>

<sup>Originally posted by **johnnyasantoss** March 12, 2026</sup>
Hello,

I couldn't create an issue so I'll be using this discussion thread to report a bug.

Yesterday I was testing and reviewing #33, after sending the review I left my bitaxe 602 mining the whole night on that branch to gather more data to plot (it was pretty stable after modifications).
I woke up and found this log:
```
thread 'tokio-runtime-worker' (31152351) panicked at /Users/johnny/.rustup/toolchains/nightly-aarch64-apple-darwin/lib/rustlib/src/rust/library/core/src/cmp.rs:1094:9:
assertion failed: min <= max
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
```

Unfortunately I was running without backtrace (shame), but after a quick repo wide search I only found one place were clamp is used with dynamic inputs: 

https://github.com/256foundation/mujina/blob/491acacfcce4e81152e82e707573dff2ce367ac8/mujina-miner/src/scheduler.rs#L268-L271

The miner continued mining but I'm not sure that it should. I'm not that familiar with the codebase to tell just by looking at this piece of code to say which thread was running this. Maybe an essential actor?</div>

## Comments

### rkuester on 2026-03-12

Doh 🤦🏼‍♂️, I thought I fixed this one. Can you please double-check that you were running code newer than 4059d89. @johnnyasantoss

### johnnyasantoss on 2026-03-12

I was running on top of the #39 with merged #33 merged, so no. That's why.

### rkuester on 2026-03-13

Ah, good. Please reopen if you see it in versions newer than 4059d89.
