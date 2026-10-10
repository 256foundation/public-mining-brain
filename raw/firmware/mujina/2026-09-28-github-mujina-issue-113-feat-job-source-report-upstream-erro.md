# 256foundation/mujina issue #113: feat(job_source): report upstream errors and latch faults

> Source: https://github.com/256foundation/mujina/issues/113
> Collected: 2026-10-07
> Published: 2026-09-28

- Repository: 256foundation/mujina
- Type: issue
- Number: 113
- State: open
- Author: rkuester
- Opened: 2026-09-28
- Closed: n/a
- Labels: none

## Description

Mujina is headless, and its API is the user's view of the miner. Errors from an upstream arrive asynchronously, apart from any API call, and today they reach only the log. Three examples on main (019d1b0):

- An upstream answers `mining.subscribe` with an out-of-range `extranonce2_size` (#90). Every job then fails conversion to a job template and is logged and dropped, so the source gives the scheduler nothing to work on. Each dropped job still resets the job-gap watchdog, so the source never notices.
- An upstream rejects `mining.authorize` (#99). The Stratum v1 source treats this as fatal, logs it, and exits. `/sources` still lists the source, though it will never give the scheduler another job.
- An upstream URL is malformed. The error comes back as a connection failure, so the source retries it forever.

This issue proposes one design for the whole class.

### Three kinds of error

The design sorts upstream errors into three kinds, by what would fix them, and handles each kind its own way.

- **Transient errors.** Refused, timed out, dropped. Time fixes these. Reconnect forever with capped backoff, as the source does today, and never latch a fault.
- **Deterministic errors.** The upstream's answer at setup is out of spec or refuses us: an impossible `extranonce2_size`, a malformed `extranonce1`, a rejected authorization, an unparseable URL. Reconnecting gets the same answer. Latch a fault, stop using the upstream, and retest it slowly (every 10--30 minutes). A successful session clears the fault.
- **Per-message errors.** One message is bad: a malformed `mining.notify`, a job that fails conversion. Drop it and count it by reason. If they keep coming, reconnect. If they persist across reconnects, latch the same fault as a deterministic error.

A slow retest matters for a headless miner. A fault that only a person can clear leaves the source out of service until someone looks.

### Who judges what

Some errors are best caught by a high-level watchdog instead of a specific check. The three kinds above cover errors the job source can recognize in a message. An upstream can also fail in ways no check anticipates, with every message well formed. A watchdog on the end result catches those too. It checks whether the upstream accepts shares as often as it should.

The scheduler is the right place for this watchdog, because only the scheduler knows the hashrate working on each upstream's jobs, and so how often shares should arrive. It needs share results from the source, which `SourceEvent` does not report yet (#65 (28caccb) adds them for SV2).

The job source keeps the checks only it can make. It knows whether a message is well formed and whether negotiation succeeded, so it raises deterministic and per-message faults. Its job-gap watchdog should count only jobs it could convert, not every `mining.notify`.

### How faults are reported and cleared

A latched fault is useful only if the user can see it in the API and clear it. Sources are not in the systree today. The API serves them as a separate `/sources` document that gives only each source's name, URL, and difficulty, and nothing about errors.

Proposed: add each source to the systree as a member under `/sources`, as boards and threads are, reporting:

- `status`, the existing `MemberStatus`: `present`, `absent`, or `faulted`. Nothing sets `faulted` yet; this would be its first use.
- `conditions`, a list of what is wrong. Each condition has a `reason` (a fixed CamelCase word for programs, such as `InvalidExtranonce2Size`), a `message` for people, a `since` time, and a `count`. Kubernetes reports status the same way, and the design follows its rule that conditions describe the current state, not a history of events.
- `accepted_shares` and `rejected_shares`, as MIP-0001 sketches.

A fault clears when a retest succeeds or when the user changes the source's settings. The user also needs a way to clear a fault by hand and retest at once. One possibility is a DELETE on the condition. That needs thought, because DELETE already has a meaning in the tree, where it forgets a saved setting.

### The cases in #90 and #98

PR #90 proposes a fix for one error of this class, an out-of-range `extranonce2_size`. On main (019d1b0), the Stratum v1 source accepts any `extranonce2_size` from the subscribe response and later converts it with `as u8`. A value of 0 or 9--255 makes every job fail conversion, so the connection stays up while the source gives the scheduler nothing to work on. A value above 255 wraps (264 becomes 8), so the source gives the scheduler jobs with an extranonce2 size the upstream never offered, and the upstream rejects every share found in them.

Under this design the value is a deterministic error. The source should check it at subscribe, fail the session, and report `faulted` with a condition such as `InvalidExtranonce2Size` and the value it received. It should then retest slowly. With the check in place, the later `as u8` becomes lossless. #90 proposes the same check at subscribe, but not the fault reporting.

A small but valid size that cannot be split among the hash threads is not an upstream error. It is the scheduler's problem, covered in #114.

PR #98 proposes a fix for another error of this class, a job whose coinbase does not parse as a transaction. On main (019d1b0), the source hands such a job to the scheduler anyway. Each hash thread then fails to compute a merkle root and drops the error, so the thread hashes nothing and logs nothing. The BM13xx thread does this as well as the CPU hasher that #98 describes.

Under this design the job is a per-message error. The source should parse the coinbase when it converts the job to a job template, drop a job that fails, and count it by reason, escalating as it would for any per-message error. A hash thread should never see such a job. #98 proposes the same check, but not the counting or escalation. It also adds a warning in the CPU hasher, which this design makes unnecessary.

#99 (authorization failures) is a deterministic error under this design.
