# Hydrapool Hardware Tests

> Sources: 256 Foundation (Hydra Pool hardware tests page), collected 2026-10-07; 256 Foundation (hydrapool.org home page), collected 2026-10-07
> Raw: [Hydra Pool hardware tests](../../raw/hydrapool/hydrapool-org-hardware-tests-html.md); [hydrapool.org home](../../raw/hydrapool/hydrapool-org-home.md)
> Updated: 2026-10-07

## Overview

The Hydrapool site keeps a table of mining hardware and whether each model has been tested against the pool. It is a community effort: owners of untested machines are asked to point them at a test server for a few minutes, and the maintainers update the table from the server logs. The table also lists a hash power and efficiency figure for each model.

## How the table works

Each row has a make, a model, a firmware version, a hash power and an efficiency. Cell colour carries the result:

- Green: tested with success.
- Yellow: not tested yet. Help is wanted.
- Red: tested and failed.

The collected copy of the page is plain text, so the colours are lost. This article cannot say which models passed or failed.

## How to help

If you own a model from a yellow cell, point the miner at `stratum+tcp://test.hydrapool.org:3333` for 5 to 10-minutes. The server logs are monitored and the table is updated.

The Hydrapool home page gives a second test address, `stratum+tcp://pool.256foundation.org:3333`. On that one, any vanity username or Nostr npub works and no BTC address is needed. That test pool is set to pay 100% to the 256 Foundation if a block is found. Pool statistics are at dash.256f.org.

## What is on the list

The table covers these makes: Antminer, Avalon, Bitaxe, Bitfury, Blockscale, Dragonmint, Innosilicon, Sealminer, Futurebit, Ember One and Whatsminer. Antminer and Whatsminer have the most rows.

Only four rows name a firmware version:

| Make | Model | Firmware | Hash Power | Efficiency |
|------|-------|----------|------------|------------|
| Bitaxe | Gamma | ESP Miner v2.7.1 | 1.2 Th/s | 15 J/Th |
| Bitaxe | Supra | ESP Miner v2.7.1 | 0.8 Th/s | 17.5 J/Th |
| Futurebit | Apollo I | Apollo API v2.0.6 | 3.5 Th/s | 45 J/Th |
| Ember One | 00 | test firmware | 3 Th/s | 33.3 J/Th |

### Open-hardware and small miners

| Make | Model | Hash Power | Efficiency |
|------|-------|------------|------------|
| Bitaxe | Max | 0.4 Th/s | 30 J/Th |
| Bitaxe | Ultra | 0.5 Th/s | 21 J/Th |
| Bitaxe | Supra | 0.8 Th/s | 17.5 J/Th |
| Bitaxe | Gamma | 1.2 Th/s | 15 J/Th |
| Bitaxe | UltraHex | 3 Th/s | 21.5 J/Th |
| Ember One | 00 | 3 Th/s | 33.3 J/Th |
| Futurebit | Apollo I | 3.5 Th/s | 45 J/Th |
| Futurebit | Apollo II | 10 Th/s | 28 J/Th |

### The range of the list

- Smallest: the Bitaxe Max at 0.4 Th/s.
- Largest: the Antminer U3S19XPH at 860 Th/s and 13 J/Th.
- Most efficient figure listed: the Antminer S21 XP+ Hydro at 500 Th/s and 11 J/Th.
- Least efficient figure listed: the Antminer T9+ at 10 Th/s and 136.4 J/Th.
- The first row of the table is the Antminer S9, at 13.5 Th/s and 98.5 J/Th.
- One row is listed under the make Blockscale with the model BZM2, at 135 Th/s and 26 J/Th.

The Whatsminer M66 Immersion appears twice in the table with the same figures.

## See Also

- [Hydrapool](hydrapool.md)
- [Running Your Own Hydrapool](running-hydrapool.md)
- [Ember One Hardware Details](../hardware/ember-one-hardware.md)
- [Bitaxe and Open Source Miners United](../ecosystem/bitaxe-and-osmu.md)
