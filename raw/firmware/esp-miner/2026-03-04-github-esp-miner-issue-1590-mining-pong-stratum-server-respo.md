# bitaxeorg/ESP-Miner issue #1590: mining.pong stratum server response register as shares

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1590
> Collected: 2026-10-07
> Published: 2026-03-04

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1590
- State: closed
- Author: scottwalter
- Opened: 2026-03-04
- Closed: 2026-03-25
- Labels: none

## Description

Summary (v2.13.0)

When a stratum host sends mining.ping to an AxeOS miner, the following exchange occurs:

Stratum host sends: {"id": N, "method": "mining.ping", "params": []}

AxeOS correctly identifies it as MINING_PING and responds with pong: {"id": N, "method": "pong", "params": []} ([stratum_api.c:491]

Stratum host acknowledges the pong with a standard JSON-RPC response: {"id": N, "result": true, "error": null}

AxeOS receives the acknowledgment. Since it has no "method" field and "result" is boolean true, the parser at [stratum_api.c:264-268] classifies it as STRATUM_RESULT.

STRATUM_RESULT with response_success = true reaches [stratum_task.c:597-600], which calls SYSTEM_notify_accepted_share() — incrementing the accepted share counter.

The parser in STRATUM_V1_parse() treats any response with a boolean "result" and no "method" field as a share submission result. It has no way to distinguish a pong acknowledgment from an actual share acceptance because it doesn't track which message IDs originated from the miner's own share submissions.

Impact: Every mining.ping / pong cycle inflates the accepted share count by one. With a typical ping interval of a few minutes, this adds several phantom "accepted shares" per hour that don't correspond to any actual work.

Suggested fix: Track outbound share submission message IDs so that only responses matching a known share submission are counted. Responses to IDs the miner didn't originate (like pong acknowledgments) should be ignored or handled separately.


## Comments

### mutatrum on 2026-03-04

Which pool or pool implementation did you connect to? As not many pools actually send ping pongs,

### scottwalter on 2026-03-04

Hi Mutatrum, I am connecting to GoSlimStratum (GSS), which is a locally hosted solo mining solution developed by MMFP Solutions (https://www.mmfpsolutions.io). GSS uses mining.ping as well as other advanced stratum V1 protocols, it is an awesome stratum host. Thank you for looking at this issue.

### scottwalter on 2026-03-06

accidentally closed this issue.
