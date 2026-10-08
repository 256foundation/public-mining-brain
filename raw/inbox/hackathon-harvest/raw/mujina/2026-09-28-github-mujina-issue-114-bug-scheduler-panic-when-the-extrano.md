# 256foundation/mujina issue #114: bug(scheduler): panic when the extranonce2 space is too small to split among threads

> Source: https://github.com/256foundation/mujina/issues/114
> Collected: 2026-10-07
> Published: 2026-09-28

- Repository: 256foundation/mujina
- Type: issue
- Number: 114
- State: open
- Author: rkuester
- Opened: 2026-09-28
- Closed: n/a
- Labels: none

## Description

On main (019d1b0), the scheduler splits each job's extranonce2 space evenly among the eligible hash threads and calls `expect()` on the result (`scheduler.rs:471`). The split fails when the space holds fewer values than there are threads, for example a 1-byte `extranonce2_size` (256 values) with 257 or more threads. The scheduler task then panics. The daemon keeps running, so the API stays up while no thread gets new work.

The size is valid, so this is not an upstream error. The scheduler should handle it gracefully. When the upstream allows version rolling, the scheduler can divide the work along the version bits as well as extranonce2, so every thread still gets a distinct share of the search space. `ntime` is another dimension. Splitting along either one brings complications that would have to be dealt with. Failing both, the scheduler should give the space to as many threads as it can hold, leave the rest idle, and report that on the source. Only the CPU miner reaches this thread count today.

PR #90 reported this panic and proposes that the scheduler skip such a job.


## Comments

### j-kon on 2026-09-28

I’d be interested in taking this one if nobody is already working on it.

I’ve been following the related work in #90 and reviewed the scheduler path around `Extranonce2Range::split`.

My initial plan would be to:

- reproduce the 1-byte EN2 / 257-thread panic on current main;
- change the scheduler so the available EN2 space is assigned to as many eligible threads as it can safely support instead of panicking or dropping the whole job;
- leave the remaining threads idle;
- add regression tests around the boundary, especially 256 vs 257 threads for a 1-byte EN2 space.

Since #113 is also defining how source conditions and faults should be reported, I’d avoid introducing a separate reporting mechanism here and keep this PR focused on the scheduler behavior unless you’d prefer otherwise.

If that scope sounds right, I’m happy to take this.

### rkuester on 2026-09-28

@j-kon Yes, please take it. The scope sounds right, including leaving the reporting to #113.

The first goal should be to stop the panic. As a general rule for the project, we don't want panics anywhere. The system should be robust enough to recover on its own.

Splitting along the version bits or `ntime` can wait for a later PR. That gets into more complicated scheduler behavior we haven't worked on yet.

It might be worth logging a warning when the scheduler leaves threads idle, with the source, the number of eligible threads, and the size of the extranonce2 space. Until #113 is done, the log is the only place the idle threads would show up.

When responding to a bug report like this one, it's nice to have a first commit that demonstrates the bug with a test, marked `#[should_panic]` so CI stays green. That commit may do a little refactoring to create a seam for the test, but it shouldn't fix the bug. The commits after it fix the bug and remove the annotation, and the test stays as a regression test. A reported bug should always leave behind a test that catches it if it comes back. [CONTRIBUTING.md](https://github.com/256foundation/mujina/blob/main/CONTRIBUTING.md#documenting-known-bugs-with-should_panic) describes the pattern. In general, we take a bug like this as a cue to leave the code better than we found it, rather than make only a surgical fix. I don't expect this test to take major work. If a test is ever too hard to write, it can wait for a later PR.


### j-kon on 2026-09-28

Thanks, that makes sense.

I’ll keep this focused on the scheduler behavior and leave the reporting work to #113.

I’ll start with a regression test that reproduces the current panic using `#[should_panic]`, then follow with the fix so the available EN2 space is assigned safely and excess threads remain idle. I’ll also add the warning with the source, eligible thread count, and EN2 space size.

I’ll leave version-bit / ntime splitting for a separate follow-up.
