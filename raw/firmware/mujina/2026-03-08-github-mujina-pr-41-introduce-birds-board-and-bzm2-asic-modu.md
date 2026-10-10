# 256foundation/mujina pull request #41: Introduce BIRDS board and BZM2 asic modules

> Source: https://github.com/256foundation/mujina/pull/41
> Collected: 2026-10-07
> Published: 2026-03-08

- Repository: 256foundation/mujina
- Type: pull request
- Number: 41
- State: closed
- Author: johnny9
- Opened: 2026-03-08
- Closed: 2026-07-27
- Labels: none

## Description

This PR adds end-to-end BIRDS/BZM2 support to mujina-miner.

It introduces the BIRDS board implementation and BZM2 protocol stack, including 9-bit serial transport, protocol encoding/decoding, chip bring-up, WRITEJOB support, task dispatch, READRESULT mapping, and share validation. It also wires BIRDS into the board inventory/registration path, initializes the BIRDS data port over BZM2, and creates the BZM2 hash thread.

The hash thread makes use of bring-up, hashing, work, and tracking modules to make the thread module a bit more maintainable.

Fan, Voltage regulator, and dynamic frequency adjustments are not currently implemented.

To test this out, you need a bitaxeBIRDS board, the voltage regulator needs to be set properly with an initialization script (https://github.com/skot/bzm-raw-py/blob/birds/vr-bringup.py), and your the pico on the birds device needs the appropriate firmware. 

## Comments

### johnny9 on 2026-03-09

Converting the PR to a draft as the BIRDS is just being used for testing and review. When ready, the bitaxeBonanza+bitaxe raw will replace the BIRDS board and at that time this PR should be ready for full review.

The bzm2 and nine_bit modules, are ready to be reviewed.

### johnny9 on 2026-07-27

Published the first beta versions of the bonanza-bridge-fw and the esp-miner-bonanza firmware and will be rebulding the BZM boards based on the bitaxeBonanza raw that will use the new and reliable bonanza-bridge. The new PR will be based on this but want to take a fresh look.
