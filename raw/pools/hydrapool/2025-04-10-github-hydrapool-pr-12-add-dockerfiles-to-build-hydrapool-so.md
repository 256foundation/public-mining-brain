# 256foundation/hydrapool pull request #12: Add dockerfiles to build hydrapool solo

> Source: https://github.com/256foundation/hydrapool/pull/12
> Collected: 2026-10-07
> Published: 2025-04-10

- Repository: 256foundation/hydrapool
- Type: pull request
- Number: 12
- State: closed
- Author: pool2win
- Opened: 2025-04-10
- Closed: 2025-04-10
- Labels: none

## Description

Includes a docker compose to build all services and run them in required order with healthchecks.

Services included are:

1. bitcoind for local signet and testnet4 setup
2. ckpool-solo (fork with hydrapool support) for providing stratum services that always pay to the pool address.
3. A p2poolv2 node for capturing shares submitted by users. This will allow us to provide different payout mechanisms.
4. cpuminer for local development work.


Ref #1
