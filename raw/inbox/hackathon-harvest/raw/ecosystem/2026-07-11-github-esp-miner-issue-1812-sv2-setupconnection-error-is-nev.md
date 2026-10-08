# bitaxeorg/ESP-Miner issue #1812: SV2: SetupConnection.Error is never handled; error code discarded, retries wasted, and fallback flaps

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1812
> Collected: 2026-10-07
> Published: 2026-07-11

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1812
- State: open
- Author: cbyam
- Opened: 2026-07-11
- Closed: n/a
- Labels: none

## Description

**Describe the bug**

`SV2_MSG_SETUP_CONNECTION_ERROR` (0x02) is defined in `sv2_protocol.h` but no handler references it. When a pool rejects an SV2 connection at setup, `stratum_v2_task.c` only checks `hdr.msg_type != SV2_MSG_SETUP_CONNECTION_SUCCESS`, logs the raw message type, and sets the pool status to "SV2: Pool rejected config". The `SetupConnection.Error` payload is never decoded, so the spec-defined `error_code` string (`unsupported-feature-flags`, `unsupported-protocol`, `protocol-version-mismatch`) is thrown away. The firmware already parses and surfaces `SubmitShares.Error` codes, so setup errors are the one remaining error string it discards.

The miner then retries the identical configuration up to `MAX_RETRY_ATTEMPTS` (3) times. Each retry is a full reconnect plus Noise handshake against a deterministic rejection, so it fails three times slowly before handing off to the protocol coordinator.

With a fallback pool configured this also causes permanent flapping. After failover the coordinator's heartbeat probes the primary every 60 seconds, but `probe_pool_sv2()` is a TCP-connect probe only (a full Noise handshake is too expensive there). A pool that accepts TCP but deterministically rejects SetupConnection always passes the probe, so the coordinator switches back, burns three reconnect+handshake retries against the same rejection, fails over again, and repeats indefinitely. Each flap also runs `reset_share_stats()`, wiping the session's share counters.

**To Reproduce**

1. Set the SV2 channel type to "standard" and point the primary at an SV2 pool that only serves extended channels (e.g. an SRI pool role without standard-job support, which rejects `REQUIRES_STANDARD_JOBS` with `unsupported-feature-flags`), plus any working fallback pool
2. Watch the device retry the same rejected SetupConnection three times, fail over to the fallback, then get pulled back to the primary by the ~60s heartbeat and repeat the cycle
3. UI shows only "SV2: Pool rejected config"; serial log shows only the numeric msg_type; the pool's stated reason appears nowhere

**Expected behavior**

The error code from `SetupConnection.Error` is logged and shown in the pool status (e.g. "SV2: protocol-version-mismatch"), and a parsed setup rejection is treated as terminal for that configuration so fallback happens immediately instead of after three identical failures.

To be upfront about what this does and doesn't resolve: a setup rejection is a configuration mismatch the device cannot fix on its own, and none of this makes the primary pool start accepting the connection. The point is that the pool already tells the device exactly what's wrong and the firmware discards it. Surfacing the string turns "SV2: Pool rejected config" plus guesswork into "SV2: unsupported-feature-flags" plus a one-minute config change (flip the channel type, update firmware, or report the pool). Human-in-the-loop is the only resolution available here; this gives the operator what they need. The retry and flapping changes are damage control around that: the device spends more time mining on the fallback and less time re-handshaking against a known rejection while the user fixes the config.

Proposed fix, small and contained:

1. Add a parser in `sv2_protocol.c` mirroring the existing `sv2_parse_submit_shares_error` (same shape: fixed fields plus an error string), with the prototype in `sv2_protocol.h` next to the already-defined constant:

```c
// SetupConnection.Error: flags(4) + error_code STR0_255(1+N) = min 5 bytes
int sv2_parse_setup_connection_error(const uint8_t *payload, uint32_t len,
                                     uint32_t *flags, char *error_code,
                                     size_t error_code_size)
{
    if (len < 5) return -1;
    *flags = read_u32_le(payload);
    return read_str0255(payload + 4, len - 4, error_code, error_code_size) < 0 ? -1 : 0;
}
```

2. In `stratum_v2_task.c`, on `msg_type == SV2_MSG_SETUP_CONNECTION_ERROR`, parse it, log the error code and flags, and put the string in the UI status. Other unexpected message types keep the current path.

3. Set `retry_attempts = MAX_RETRY_ATTEMPTS` on a parsed error so the outer loop hands off to the coordinator immediately. This cuts each flap cycle from three reconnect+handshake attempts to one, though it doesn't stop the flapping itself.

Fully stopping the flap would need the heartbeat probe to detect a setup-level rejection, which means completing a Noise handshake plus SetupConnection in `probe_pool_sv2()`, or having the coordinator back off a primary that repeatedly fails right after a successful probe. Either is a larger change and probably a separate issue; flagging the interaction here so the scope choice is deliberate.

Happy to submit a PR for the three parts above if the approach looks right.

**Hardware (please complete the following information):**
 - Bitaxe HW version: n/a (found by code inspection, affects all SV2-capable devices)
 - Bitaxe HW vendor: n/a
 - ESP-Miner FW version: master @ e9903b7
 - Hash Frequency: n/a
 - Voltage: n/a
 - Pool URL, Port, User: n/a

**Additional context**

Most Bitaxes ship preconfigured for public pools and many stay on them. Public SV2 pools are largely SRI-derived and do send a proper `SetupConnection.Error` frame before closing, so the information is already on the wire; the default-config users who can't read pool-side logs are exactly the ones who only have the AxeOS status line to go on.

Out of scope: the spec's flag-downgrade retry on `unsupported-feature-flags`. The firmware only sets `REQUIRES_STANDARD_JOBS` for standard channels, and silently downgrading would override the user's explicit channel-type choice. Version negotiation is moot while 2 is the only SV2 protocol version ever defined (SV2's version field starts at 2 and does not refer to Stratum V1, which is a separate protocol).
