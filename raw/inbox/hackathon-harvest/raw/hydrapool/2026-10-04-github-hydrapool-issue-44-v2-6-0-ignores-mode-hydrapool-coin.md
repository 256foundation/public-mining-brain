# 256foundation/hydrapool issue #44: v2.6.0 ignores mode = "hydrapool": coinbase pays 99% to genesis NUMS address and shares are rejected

> Source: https://github.com/256foundation/hydrapool/issues/44
> Collected: 2026-10-07
> Published: 2026-10-04

- Repository: 256foundation/hydrapool
- Type: issue
- Number: 44
- State: open
- Author: LuLuDiscord
- Opened: 2026-10-04
- Closed: n/a
- Labels: none

## Description

## Summary

The Hydrapool v2.6.0 binary does not apply `mode = "hydrapool"` from the config. It always runs the share chain payout and the P2Poolv2 stratum mode. On testnet4 this produces a coinbase that sends 99% of the reward to the genesis share's NUMS address (unspendable), and every share is rejected with "Low difficulty share".

If a block were found on mainnet with this setup, almost all of the reward would be burned.

## Environment

- Hydrapool v2.6.0, official release binary `hydrapool-x86_64-unknown-linux-gnu` (SHA256 verified)
- p2poolv2_lib v0.12.0 (as pinned in Cargo.toml)
- Bitcoin Core 31.1, testnet4, Ubuntu 24.04
- Config based on `docker/config-example.toml` with `network = "testnet4"`, `mode = "hydrapool"`, `fee = 100`, `fee_address` and `bootstrap_address` set to the operator's address, no donation

## What happens

1. Fresh store, no shares yet. The `/metrics` endpoint shows:

```
coinbase_output{index="0",address="<fee_address>"} 50000004
coinbase_output{index="1",address="tb1qx6e0gj7q7xurl08cwnpmeve6w6zf4tw6vfwe3f"} 4950000445
coinbase_total 5000000449
```

`tb1qx6e0gj7q7xurl08cwnpmeve6w6zf4tw6vfwe3f` is the miner address of the testnet4 genesis share (NUMS pubkey), not an address from the config.

2. A CPU miner (pooler cpuminer, difficulty 1) connects with a valid testnet4 address. Every share is rejected:

```
{"id":4,"result":null,"error":[23,"Low difficulty share",""]}
```

`/pplns_shares` stays empty.

## Expected

With no shares, 100% to `bootstrap_address` (simple PPLNS behaviour). With shares, 1% fee plus outputs to miners proportional to share difficulty. No share chain difficulty check in hydrapool mode.

## Cause

In `src/main.rs`:

- Line 19 imports `p2poolv2_lib::accounting::payout::sharechain_pplns::Payout` and line 204 always builds it, regardless of `mode`. The share chain window includes the genesis share, so its NUMS address gets the reward.
- The `StratumServerBuilder` (around line 245) never calls `.mode(...)`, so `StratumServer` falls back to `PoolMode::default()`, which is `P2poolv2`. That enables the pool difficulty check in `stratum/message_handlers/submit.rs`, which rejects the shares.

This seems to have started in v2.5.3 (commit c6f2a14, "Update to latest p2poolv2 libs"). The 2.5.9 changelog entry "Ignore pool ASERT difficulty used in P2Poolv2 when running a hydrapool PPLNS instance" does not take effect in the binary for the same reason.

## Suggested fix

Do the same as `p2poolv2_node/src/main.rs` in p2poolv2 v0.12.0:

- Use `p2poolv2_lib::accounting::payout::build_payout_for_mode(stratum_config.mode, network)` instead of `sharechain_pplns::Payout::new(network)` (see p2poolv2#559).
- Pass `.mode(stratum_config.mode)` to `StratumServerBuilder`.

## Verification

I built `p2poolv2_node` from the v0.12.0 tag (commit 8eca024b) with `--features p2poolv2_lib/hydrapool-pplns-accounting` and used the same config. On testnet4 with two CPU miners:

- shares accepted and listed in `/pplns_shares`
- coinbase: exactly 1% to `fee_address`, the remainder split 60/40 between the two miners (3 and 2 shares of difficulty 1); the outputs add up exactly to the total

Side note: the released `p2poolv2_node` v0.12.0 binary is built without `hydrapool-pplns-accounting`, so in hydrapool mode it discards PPLNS shares and pays everything to `bootstrap_address`. That is probably expected for that binary, but it means it is not a drop-in workaround.
