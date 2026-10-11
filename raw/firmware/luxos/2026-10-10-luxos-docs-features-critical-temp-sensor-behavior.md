# LuxOS Docs — Critical Temperature Sensor Behavior

> Registry ID: luxos-docs
> Source: https://docs.luxor.tech/firmware/features/criticaltempsensorbehavior
> Collected: 2026-10-10
> Published: n/d
> Posture: verbatim
> As-Of: 2026-10-10


## Critical Temperature Sensor Behavior Overview [#critical-temperature-sensor-behavior-overview]

This page documents how LuxOS decides whether to keep hashing, reboot a board, or shut the miner down based on the working temperature sensors available on each hashboard. The behavior depends on the operator-configured [`min_per_board`](../api/luxminer/tempsensorset) floor, the miner's hardware (cooling type and ASIC die-temperature coverage), and which sensors are marked as critical.

## At a glance [#at-a-glance]

* **Hydro water-sensor failure always reboots the affected board**, regardless of `min_per_board` or die-temp coverage.
* **`min_per_board > 0`** enforces an operator-configured floor — a board drops below it ⇒ board reboot.
* **ASIC on-die temps and water sensors are fallback protections** — either one alone is enough to keep the miner hashing when critical board sensors are gone.
* **The miner only shuts itself down** when `min_per_board == 0` *and* no critical board sensors, no die-temp coverage, and no working water sensors remain anywhere.

## Decision Table Column definitions [#decision-table-column-definitions]

* **Water Temps (Hydro):** `N/A` (air-cooled), `OK` (≥1 working), `FAIL` (any failed). Water is only ever critical on hydro.
* **ASIC Die Temp Coverage:** on-die overheat coverage — `Yes` for `BM1368` / `BT1978` / `BM1746`, `No` otherwise. See [`HasDieTempOverheatCoverage`](../api/cgminer/config) in `config`.
* **Critical Board Temps:** working critical (hot-side, non-water) board sensors on *this* board; `min` = `min_per_board`. See `IsCritical` in [`temps`](../api/cgminer/temps).
* **`min_per_board`:** configured floor; `0` disables per-board minimum enforcement and enables the miner-level shutdown check.
* **Any critical board temps left miner-wide:** `≥1` if *any* board still has a working critical board sensor, die coverage, or working water sensor; `0` if none anywhere.

## Decision table [#decision-table]

| # | Water Temps (Hydro) | ASIC Die Temp Coverage | Critical Board Temps        | `min_per_board`      | Any critical board temps left miner-wide | Board action                | Miner action       |
| - | ------------------- | ---------------------- | --------------------------- | -------------------- | ---------------------------------------- | --------------------------- | ------------------ |
| 1 | FAIL                | any                    | any                         | any                  | —                                        | **Reboot board**            | Running            |
| 2 | any                 | any                    | `< min`                     | `> 0`                | —                                        | **Reboot board**            | Running            |
| 3 | N/A or OK           | No                     | `0` (all hot-side failed)   | any                  | —                                        | **Reboot board** †          | Running            |
| 4 | N/A or OK           | Yes                    | `0` (all hot-side failed)   | `≥ min` (i.e. min=0) | —                                        | Keep hashing (die coverage) | Running            |
| 5 | N/A                 | No                     | `0` on every board          | `0`                  | `0`                                      | —                           | **Miner shutdown** |
| 6 | OK anywhere         | No                     | `0` on every board          | `0`                  | `≥ 1` (water OK somewhere)               | Keep hashing                | Running            |
| 7 | any                 | Yes on any board       | `0` on every board          | `0`                  | `≥ 1` (die coverage)                     | Keep hashing                | Running            |
| 8 | N/A or OK           | any                    | `≥ min` and ≥ 1 hot-side OK | any                  | —                                        | Keep hashing                | Running            |

† Row 3 has a pre-existing exception for hashboards with a PIC (`has_pic_on_hashboard == true`): the PIC provides an independent on-chip overtemp backstop, so the critical-failure check tolerates "all hot-side failed" on those boards and the row-3 reboot does not fire. Affected classes: `S19j`, `S19jpro`, `S19k Pro`, older PIC S19 variants, `S19 Pro+ Hydro`, `S19 XP Hydro`, `S21 Hydro`.

## How each cooling type and ASIC chip combination maps to the Decision Table [#how-each-cooling-type-and-asic-chip-combination-maps-to-the-decision-table]

| Class                                    | Example models                                                 | Water Temps (Hydro) | ASIC Die Temp Coverage | Reachable rows  |
| ---------------------------------------- | -------------------------------------------------------------- | ------------------- | ---------------------- | --------------- |
| **Air, no chip die temp coverage**       | `S19j`, `S19jpro`, `S19k Pro`, older `T19`/`S19` PIC boards    | N/A                 | No                     | 2, 3 †, 5, 8    |
| **Air, die temp coverage (BM1368)**      | `S19 XP+`, `S21`, `T21`                                        | N/A                 | Yes                    | 2, 4, 7, 8      |
| **Air, no die temp coverage (BM1370)**   | `S21 Pro`, `S21 XP`, `S21+`                                    | N/A                 | No                     | 2, 3, 5, 8      |
| **Air, die temp coverage (BM1746)**      | Antminer `Z15 Pro`                                             | N/A                 | Yes                    | 2, 4, 7, 8      |
| **Air, die temp coverage (BT1978)**      | Whatsminer `M50` / `M50S` / `M50S+` / `M60` / `M60s`           | N/A                 | Yes                    | 2, 4, 7, 8      |
| **Hydro, die temp coverage (BM1368)**    | `S19 XP+ Hydro`, `S21 Hydro`                                   | OK/FAIL             | Yes                    | 1, 2, 4, 7, 8   |
| **Hydro, no die temp coverage**          | `S19 Pro+ Hydro`, `S19 XP Hydro`                               | OK/FAIL             | No                     | 1, 2, 3 †, 6, 8 |
| **Hydro, no die temp coverage (BM1370)** | `S21+ Hydro`, `S21 XP Hydro`, `S21e Hydro`, `U3 S21e XP Hydro` | OK/FAIL             | No                     | 1, 2, 3, 6, 8   |

## Key invariants [#key-invariants]

* **Row 1** fires before any other check on hydro: water-sensor loss always reboots the board, regardless of `min_per_board` or die coverage.
* **Row 2** is the only path that can reboot a board for "below the operator's configured minimum"; it is disabled when `min_per_board == 0`.
* **Row 5** is the only path that can shut the *miner* down from this subsystem; it requires `min_per_board == 0` **and** zero working critical board sensors miner-wide **and** no die coverage **and** no working water sensors anywhere.
* Rows 4, 6, 7 are the fallback protections: **ASIC die temps** and **water temps**, each of which individually keeps the miner hashing when critical board temps are gone.

## Related [#related]

* [`tempsensor`](../api/luxminer/tempsensor) and [`tempsensorset`](../api/luxminer/tempsensorset) — read and configure `min_per_board`.
* [`temps`](../api/cgminer/temps) — per-sensor metadata including `IsCritical`.
* [`config`](../api/cgminer/config) — `HasDieTempOverheatCoverage` for the running miner.
* [Advanced Features → Required Sensors per Board](./advancedfeatures#required-critical-temperature-sensors-per-board) — GUI control for `min_per_board`.
