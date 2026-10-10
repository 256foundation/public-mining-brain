# 256foundation/asic-rs pull request #409: feat(antminer): add S21/S23 hydro models and aliases

> Source: https://github.com/256foundation/asic-rs/pull/409
> Collected: 2026-10-07
> Published: 2026-10-07

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 409
- State: closed
- Author: dtyg0d
- Opened: 2026-10-07
- Closed: 2026-10-07
- Labels: none

## Description

Stock S21 XP Hyd, S21j XP Hyd and S23 Hyd labels previously fell back to unknown models. This adds distinct SHA256 model identities and exact aliases, leaving existing parsing behavior unchanged.

Hardware metadata was verified with read-only telemetry from 14 physical miners across all eight firmware cohorts in the supplied inventory:

| Model | Boards | ASICs per board | Miners checked | Firmware cohorts |
| --- | ---: | ---: | ---: | ---: |
| S21 XP Hyd | 3 | 160 | 6 | 4 |
| S21j XP Hyd | 3 | 42 | 4 | 2 |
| S23 Hyd | 3 | 84 | 4 | 2 |

Every checked miner reported the expected exact model, three populated chains, and consistent `chain_acn1/2/3` counts matching the number of working `o` markers. Read-only `stats.cgi` also confirmed three indexed boards and matching `asic_num` values on one representative of each model. Formatting padding in the RPC ASIC-status strings was not counted as chips. No private addresses, MACs, pool settings or workers are included.

No telemetry parser, schema, binding, packaging or control changes are included. Validation: seven existing Antminer tests, Rust formatting and generated-device documentation checks passed. These counts describe the sampled stock hardware and do not establish control compatibility.
