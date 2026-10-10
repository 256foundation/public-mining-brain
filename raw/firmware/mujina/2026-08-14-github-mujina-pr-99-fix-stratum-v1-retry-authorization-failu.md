# 256foundation/mujina pull request #99: fix(stratum_v1): retry authorization failures instead of giving up

> Source: https://github.com/256foundation/mujina/pull/99
> Collected: 2026-10-07
> Published: 2026-08-14

- Repository: 256foundation/mujina
- Type: pull request
- Number: 99
- State: open
- Author: Schnitzel
- Opened: 2026-08-14
- Closed: n/a
- Labels: none

## Description

## Problem

`AuthorizationFailed` was one of only two fatal errors in the stratum stack: a pool that answers `mining.authorize` with an error (or `result: false`) made the source task exit **permanently** — no retry, no backoff, no process exit, no API alarm. The daemon stays alive (API serving, boards registered) but never mines again until manually restarted.

Because stratum v1 is plaintext, an on-path attacker who sees the `mining.authorize` request can race the real pool with a forged error response and stop a miner — or a whole fleet — with a single packet. Worse than a crash: `systemd`/`Restart=always` sees a healthy process, so only hashrate monitoring notices.

Found during hostile-pool fuzzing (handshake-variant battery): after one auth-error response the miner made zero further connection attempts for the rest of the run while `Mining status` heartbeats continued.

## Fix

Remove `AuthorizationFailed` from `is_fatal()`; auth failures now take the same jittered exponential backoff reconnect path as any other disconnect. Truly wrong credentials cost a reconnect a minute and a repeating log line; forged or transient rejections no longer halt production. `InvalidUrl` stays fatal — a malformed address genuinely won't fix itself.

## Tests

- `authorization_failure_retries` (replaces `fatal_error_stops_retrying`): auth-rejected source must produce a second connection after the backoff window; a timeout turns "no retry" into a clean failure instead of a hang.
- `only_invalid_urls_are_fatal` (new error.rs unit test): pins the remaining fatal set.

`cargo fmt`, `cargo clippy` (no new warnings), `cargo test` (358 passed) green.

## Comments

### j-kon on 2026-09-15

The retry behavior makes sense to me, especially for Stratum V1 where an authorization rejection cannot necessarily be treated as trustworthy enough to permanently stop the source.

I also like that `InvalidUrl` remains fatal while `AuthorizationFailed` goes through the existing backoff path.

One possible test gap: the PR description mentions both an authorization `result: false` and an authorization error response, but `authorization_failure_retries` currently appears to exercise the `result: false` case only.

Would it be worth parameterizing this test, or adding another case, for an explicit JSON-RPC error response as well? That would pin both paths described in the threat model and make sure they continue to reach the retry behavior.
