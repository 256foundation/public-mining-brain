# 256foundation/mujina pull request #89: fix(stratum_v1): bound pool reads by length and idle time

> Source: https://github.com/256foundation/mujina/pull/89
> Collected: 2026-10-07
> Published: 2026-08-07

- Repository: 256foundation/mujina
- Type: pull request
- Number: 89
- State: closed
- Author: Schnitzel
- Opened: 2026-08-07
- Closed: 2026-08-14
- Labels: none

## Description

## Problem

Two related robustness gaps in the stratum client, both reachable by a malicious pool or a MITM (the transport is plaintext):

1. **Unbounded read buffer** — `Connection::read_message` loops `BufReader::read_line` into a growable `String` with no length cap. A peer that never sends `\n` grows the daemon's memory until the OOM killer ends it (≈1 GB per 25 s at 100 Mbps, or arbitrarily slowly via a drip).
2. **No idle timeout** — the main event loop awaits pool messages with no timeout. A dead or deliberately silent connection leaves the miner neither working nor reconnecting; TCP keepalive takes hours to notice.

Found during a source review of the pool-facing input handling.

## Fix

- **Cap messages at 64 KiB** (`MAX_MESSAGE_LEN`): the read goes through a length-limited adapter, and a line that fills the cap without a terminating newline is rejected with a new `StratumError::MessageTooLarge`. 64 KiB is ~10× the largest legitimate message (`mining.notify` with a big coinbase and many merkle branches). The error terminates the connection; the source reconnects with the usual jittered backoff.
- **20-minute idle timeout** (`POOL_IDLE_TIMEOUT`) around pool reads in the client main loop. Pools send `mining.notify` at least as often as new blocks arrive (10 min average), so 20 minutes of silence means the connection is dead; a timeout errors the connection and triggers the normal reconnect path.

Neither change affects the handshake/submit paths, which already have 30 s request timeouts.

## Tests

- `test_oversized_message_rejected`: an unterminated 64 KiB+1 line is rejected with `MessageTooLarge`.
- `test_max_length_message_accepted`: a well-formed message just under the cap still parses.
- `test_silent_pool_recycles_connection`: paused-time test; after a mock handshake the pool says nothing and the client exits with `Timeout`, i.e. the caller reconnects.

`cargo fmt`, `cargo clippy` (no new warnings), and `cargo test` (355 passed) are green; each commit passes on its own.

## Comments

### rkuester on 2026-08-13

@Schnitzel Ahoy, 256 red team ;). Rather than send review comments back and forth, I reworked the series myself and force-pushed it to this PR. You're still the author on the length-cap commit and a co-author on the rest, so please review when you have a chance.

What I changed and why:

**Message length cap**: kept essentially as is, but simplified it a bit, and documented the implications for the largest allowable coinbase transaction.

**Idle timeout**: a good idea to protect against broken or malicious pools, but the implementation was flawed. As @jayrmotta points out, it would have considered the connection busy simply due to share submissions, acknowledged or not.

Along the road to fixing the trigger, I moved the detection of idle up a layer into the job source, which operates the Stratum client, because the Stratum protocol itself doesn't require any specific timing. The source now enforces an expectation that jobs arrive no more than two minutes apart (much shorter than the original twenty minutes).

Relatedly, the Stratum client itself now disconnects (rather than just logging the failure) when the pool fails to respond to a share submission. Responding to a request is required by the JSON-RPC framing Stratum uses.


### jayrmotta on 2026-08-13

@rkuester @Schnitzel 

Please read my comments above as nits, from a behavioral point of view it looks good to me 161c82296eea44d54eabde4bcd9f8582624d6147.

### rkuester on 2026-08-13

Force-pushed two small changes for the nits: dropped the misleading comment on the submit disconnect (3cc4f1d) and renamed last_job to gap_start (7b0602a). The series is otherwise unchanged.
