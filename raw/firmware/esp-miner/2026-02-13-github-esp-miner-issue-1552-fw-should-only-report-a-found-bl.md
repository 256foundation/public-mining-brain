# bitaxeorg/ESP-Miner issue #1552: fw should only report a found block if share was submitted and accepted

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1552
> Collected: 2026-10-07
> Published: 2026-02-13

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1552
- State: open
- Author: 0xf0xx0
- Opened: 2026-02-13
- Closed: n/a
- Labels: none

## Description

**Describe the bug**
the firmware seems to treat valid shares as found blocks, even if the share was never submitted to the pool.

**To Reproduce**
Steps to reproduce the behavior:
1. Set up a regtest node
2. Set up a pool pointing to it with a high difficulty (10k is plenty, 25k at most)
3. mine on it with your axe
4. watch the "block found" banner pop up even though no shares were submitted to the pool

**Expected behavior**
I expected the block found banner to appear only with submitted shares.

## Comments

### vortexopenclaw on 2026-06-01

I reviewed this as an issue-first writeup.

The bug looks like it comes from the point where `blockFound` is incremented. The current flow calls `SYSTEM_notify_found_nonce()` when local nonce difficulty meets the active job network difficulty. At that point the firmware has found a candidate, but it does not yet know whether the corresponding share was submitted and accepted by the pool.

That means the UI can report a found block before pool acceptance confirms it.

The direction I tested was:

- keep local candidate discovery separate from accepted block reporting
- update best/session diff when the nonce is found
- track the submit request associated with a block candidate
- increment `blockFound` only after the matching pool submission is accepted
- match SV1 by JSON-RPC request ID
- match SV2 by SubmitShares sequence number

Validation I ran on the proposed approach:

- `git diff --check`
- firmware `idf.py build`
- `GITHUB_ACTIONS=true idf.py -C test-ci fullclean && GITHUB_ACTIONS=true idf.py -C test-ci build`
- Bitaxe Gamma mining smoke passed and the device was rolled back healthy

Not covered locally: a full original regtest pool reproduction of an actual network-difficulty candidate block. I validated the code path and build/test coverage, but not the full pool-side regtest scenario from the issue.

Reference implementation from the closed PR, if useful for discussion: #1741
