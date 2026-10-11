# Avalon A14 series (1446 / 1466)

> Sources: Canaan A14 series page (Wayback snapshot 2026-05-12); ASIC Miner Value + MiningNow snapshots (values as of 2026-10-10)
> Raw: [A14 series page](../../raw/hardware/canaan/2026-05-12-wayback-canaan-miner-a14-series.md); [AMV Canaan](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-canaan.md); [MiningNow Canaan](../../raw/hardware/miningnow/2026-10-10-miningnow-canaan.md); [Canaan miner index](../../raw/hardware/canaan/2026-04-12-wayback-canaan-miner-index.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

## Specs (maker series cards, snapshot 2026-05-12)

- Card: Avalon Miner 1446 — "Quite a Bitcoin Harvester" — "From $1248 (Bulk Order)": 133T · 3 Work Modes · "PSU @ 3600W" · 27.1J/TH ("a very low Power Consumption") · -5 - 35 ℃ · 2 x 12050 Fan · L271mm x W192mm x H292mm · 13Kg (the "PSU @ 3600W" unit).
- Card: Avalon Miner 1466 — "Quite a Bitcoin Harvester" — "From $1603.8 (Bulk Order)": 162T · 3 Work Modes · "PSU @ 3500W" · 23.3 J/TH · same chassis/fans/13Kg.
- Naming quirk (capture note): the series cards drop the "A" prefix — "1446"/"1466", i.e. A14-series models.
- Series claims: "Most powerful chip ever", stable "in desert heat, ice, snow, or other extreme environments"; immersion variants marketed as "Noiseless and Eco-friendly" with "The mining module is fully immersed in liquid coolant, eliminating any possibility of dust absorption within the miner."

## Cross-check (AMV vs MiningNow, 2026-10-10)

| Source | Hashrate | Power | Efficiency | Price | Release |
|---|---|---|---|---|---|
| Maker card 1446 | 133T | PSU @ 3600 W | 27.1 J/TH | From $1,248 (bulk) | — |
| [AMV](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-canaan.md) | 135 Th/s (A1446) | 3310 W | — | — | Sep 2023 |
| [MiningNow](../../raw/hardware/miningnow/2026-10-10-miningnow-canaan.md) | 150TH/s (A1466) | 3230 W | 21.53 j/Th | $1,755.38 | Sep 2023 |
| [AMV](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-canaan.md) A1466 | 150 Th/s | 3230 W | — | — | Sep 2023 |

> **Status: Disputed** — 1446: maker 133T @ "PSU @ 3600W" vs AMV 135 Th/s @ 3310 W (PSU rating vs wall draw conflation — the card says PSU capacity, the DBs wall draw); 1466: maker 162T @ PSU @ 3500 W vs AMV/MiningNow 150 Th/s @ 3230 W (higher-bin card vs shipped DB row; Canaan's own shop later listed A1466 up to 162T per Wayback URL inventory, quoted in the capture). Efficiency only exists as computed DB values here (21.53 j/Th MiningNow vs maker 23.3 J/TH card).

## Field scale (IR corroboration, from the capture)

- Nov 20, 2024 PR: "approximately 3,480 Avalon A14 series mining machines with an average hash rate of 150 terahash per second"; Feb 19, 2025 PR: Panther Creek deployment of 6,000 A14 units (0.9→0.93 EH/s).

## Heat-reuse notes

- Prior-generation air units (PSU ratings 3310–3600 W per the DB rows, 13 kg); the A1366I-122T immersion box sits in Clearance per the 2026-04 index snapshot — the cheap-heat tier of the Canaan line.
- AMV shows both A14 models mining at a loss at its $0.10/kWh assumption (−$7.75 to −$7.94/day) — heat-first deployments are the use case where that arithmetic flips (see [Hashrate heating economics](../economics/hashrate-heating-economics.md)).

## See Also

- [Avalon overview](avalon-overview.md), [A15Pro](avalon-a15pro.md), [A16XP](avalon-a16xp.md)
