# Hydrapool

> Sources: 256 Foundation (projects page), collected 2026-10-07; Hydrapool project (GitHub README), collected 2026-10-07; 256 Foundation (telehash page), collected 2026-10-07; 256 Foundation (newsroom: MARA Foundation), collected 2026-10-07; Hydrapool project (hydrapool.org home page), collected 2026-10-07
> Raw: [256foundation.org projects](../../raw/foundation/256foundation-org-projects.md); [256foundation/hydrapool README](../../raw/hydrapool/github-256foundation-hydrapool.md); [256foundation.org telehash](../../raw/foundation/256foundation-org-telehash.md); [MARA Foundation $100,000](../../raw/foundation/256foundation-org-newsroom-mara-foundation-tier1-supporter.md); [hydrapool.org](../../raw/hydrapool/hydrapool-org-home.md)
> Updated: 2026-10-07

## Overview

Hydrapool is the 256 Foundation's open-source Bitcoin mining pool. It is built as a platform: payout and accounting logic are plug-ins, and it deploys with one command. Payouts are made directly from the coinbase, so the pool operator never holds miners' funds. It is written in Rust and licensed AGPLv3.

## The gap it fills

Pools are the server side of mining, and they are concentrated. A pool can filter which transactions get mined, custody payouts, and hide its accounting. There has been no permissionless way to aggregate hashrate without trusting an operator.

## What it is

The foundation's comparison is WordPress for pools: a core platform with payouts as plug-ins.

- Solo and PPLNS accounting today, with more payout schemes (Lightning, Ark) planned on the same core.
- Non-custodial payouts from the coinbase.
- Users can download and validate the accounting of shares through an API.
- Prometheus and Grafana dashboards for pool, user and worker hashrates and uptimes.
- Works with any Bitcoin node that supports Bitcoin RPC.
- Docker and docker compose files for deployment.
- A P2Pool V2 path aims at pooling with no operator to trust at all.

The README notes a current limit of up to 100 users, for coinbase and block weight reasons. Workers are limited only by hardware.

> **Status: Disputed**
> The GitHub README says the pool only accommodates up to 100 users. The hydrapool.org home page says 100 unique users in the coinbase is a default that the user can configure. See [Running Your Own Hydrapool](running-hydrapool.md).

## Where it runs

- The foundation's instance is live at pool.256foundation.org:3333.
- [Telehash](../foundation/telehash.md) events point community hashrate at this instance in solo mining mode.
- At Bitcoin 2026 it ran on the DOOMAXE demo miner itself. See [Libre Board](../hardware/libre-board.md).

## People

Jungly is the core architect and lead maintainer.

## See Also

- [Telehash](../foundation/telehash.md)
- [Mujina Firmware](../mujina/mujina-firmware.md)
- [Running Your Own Hydrapool](running-hydrapool.md)
- [Hydrapool Hardware Tests](hydrapool-hardware-tests.md)
- [GridPool](gridpool.md)
