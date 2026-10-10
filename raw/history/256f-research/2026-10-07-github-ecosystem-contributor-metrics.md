# GitHub ecosystem contributor metrics — Bitaxe / open-source mining galaxy (2026-10-07)

> Source: GitHub REST API via `gh api` (`/users/{u}/repos`, `/orgs/{o}/repos`, `/repos/{r}/contributors?anon=true`)
> Collected: 2026-10-07
> Published: N/A (live point-in-time snapshot)

Method: contributor counts include anonymous contributors (`anon=true`); totals derived from `Link: rel="last"` page counts. Unique-contributor union = case-insensitive union of login/name across the contributor lists of 25 key repos below (paginated, `per_page=100`). Counts are as of collection time and **lower bounds**: repos not in the sample, forks, and Gitea/off-GitHub work are not captured.

## Headline metrics

- **Unique contributors across the 25-repo galaxy sample: 244** (from 404 contributor-repo pairs)
- **bitaxeorg org total: 1931 stars / 751 forks** (36 repos)
- **256foundation org total: 292 stars / 143 forks** (40 repos)
- Largest single repos by stars: BitMaker-hub/NerdMiner_v2 (2805), skot/bitaxe (1371), bitaxeorg/ESP-Miner (969), benjamin-wilson/public-pool (451), bitaxeorg/bitaxeGamma (420)
- `skot/bitaxe` created **2022-05-16** (earliest public GitHub trace of the Bitaxe project found in this snapshot; confirm the true "public release" moment with Skot)

## Per-repo contributor counts (incl. anonymous)

| repo | contributors |
|---|---|
| skot/bitaxe | 5 |
| skot/BM1397 | 3 |
| skot/bitcrane | 1 |
| bitaxeorg/ESP-Miner | 86 |
| bitaxeorg/bitaxeGamma | 7 |
| bitaxeorg/ultraHex | 7 |
| bitaxeorg/BitaxeGT | 5 |
| bitaxeorg/bitaxe-web-flasher | 14 |
| bitaxeorg/osmu-wiki | 17 |
| bitaxeorg/legitlist | 31 |
| BitMaker-hub/NerdMiner_v2 | 49 |
| BitMaker-hub/NerdAxe | 6 |
| BitMaker-hub/ESP-Miner-NerdAxe | 27 |
| shufps/qaxe | 2 |
| shufps/ESP-Miner-NerdQAxePlus | 58 |
| shufps/piaxe | 6 |
| shufps/piaxe-miner | 4 |
| benjamin-wilson/public-pool | 19 |
| benjamin-wilson/public-pool-ui | 9 |
| Patsch91/NerdOCTAXE-Gamma | 2 |
| Patsch91/NerdOCTAXE-Plus | 1 |
| WantClue/forge-os | 3 |
| 256foundation/mujina | 10 |
| 256foundation/hydrapool | 6 |
| 256foundation/asic-rs | 24 |
| 256foundation/emberone00-pcb | 4 |
| 256foundation/libreboard | 2 |

## Key ecosystem contributors and their repos (mining-relevant, by stars)

### skot (Skot — Bitaxe inventor)

| repo | created | pushed | stars | forks |
|---|---|---|---|---|
| skot/bitaxe | 2022-05-16 | 2025-08-27 | 1371 | 216 |
| skot/BM1397 | 2022-11-21 | 2024-01-12 | 65 | 27 |
| skot/hashat | 2023-04-22 | 2023-06-09 | 28 | 10 |
| skot/bitcrane | 2023-10-23 | 2026-08-28 | 28 | 9 |
| skot/bitaxe-doc | 2023-12-14 | 2023-12-26 | 26 | 6 |
| skot/bitcart | 2023-09-14 | 2024-03-28 | 23 | 4 |
| skot/aditBoard | 2024-03-26 | 2025-06-10 | 16 | 4 |
| skot/Loriques | 2025-07-12 | 2025-07-13 | 16 | 1 |
| skot/bm1387_scripts | 2022-05-26 | 2022-06-10 | 11 | 9 |
| skot/cgminer-bitaxe | 2023-06-01 | 2023-06-10 | 8 | 5 |
| skot/pool_checkr | 2025-11-27 | 2026-06-19 | 7 | 4 |
| skot/nano3ble | 2026-02-25 | 2026-02-25 | 7 | 0 |

### BitMaker-hub (NerdMiner / NerdAxe)

| repo | created | pushed | stars | forks |
|---|---|---|---|---|
| BitMaker-hub/NerdMiner_v2 | 2023-03-20 | 2026-06-14 | 2805 | 646 |
| BitMaker-hub/NerdAxe | 2022-11-17 | 2025-04-15 | 174 | 17 |
| BitMaker-hub/ESP32_NerdMiner | 2022-05-28 | 2022-05-28 | 52 | 15 |
| BitMaker-hub/NerdQaxe | 2024-09-11 | 2024-08-31 | 46 | 5 |
| BitMaker-hub/ESP-Miner-NerdAxe | 2023-01-24 | 2025-01-27 | 45 | 8 |
| BitMaker-hub/Seeder | 2022-12-12 | 2026-09-11 | 24 | 8 |
| BitMaker-hub/orangePill | 2022-10-27 | 2022-11-22 | 17 | 1 |
| BitMaker-hub/StackSatsGame | 2023-02-16 | 2023-02-16 | 11 | 2 |
| BitMaker-hub/NerdOCTAXE-Gamma | 2025-09-28 | 2025-11-20 | 8 | 0 |
| BitMaker-hub/ESP-Miner-NerdQAxePlus | 2025-01-26 | 2026-10-07 | 6 | 0 |

### shufps (PiAxe / NerdQAxe+ / NerdQAxe++)

| repo | created | pushed | stars | forks |
|---|---|---|---|---|
| shufps/qaxe | 2024-01-15 | 2026-01-21 | 244 | 52 |
| shufps/ESP-Miner-NerdQAxePlus | 2024-08-09 | 2026-10-07 | 235 | 116 |
| shufps/piaxe | 2023-10-21 | 2024-01-30 | 59 | 2 |
| shufps/piaxe-miner | 2023-11-19 | 2024-12-23 | 53 | 13 |
| shufps/0xaxe | 2024-04-03 | 2024-08-23 | 28 | 8 |
| shufps/nerdqaxe-web-flasher | 2025-01-26 | 2026-06-14 | 7 | 3 |
| shufps/flexaxe | 2024-03-13 | 2025-12-29 | 5 | 1 |
| shufps/NerdNOS | 2024-08-12 | 2024-10-31 | 4 | 3 |

Note: shufps also has non-mining repos (projector clocks) excluded above.

### benjamin-wilson (Public Pool)

| repo | created | pushed | stars | forks |
|---|---|---|---|---|
| benjamin-wilson/public-pool | 2023-06-10 | 2026-09-16 | 451 | 158 |
| benjamin-wilson/public-pool-ui | 2023-06-20 | 2026-08-26 | 57 | 73 |
| benjamin-wilson/public-pool-app | 2024-07-12 | 2024-07-14 | 17 | 4 |
| benjamin-wilson/qaxe | 2025-06-01 | 2026-06-11 | 15 | 6 |
| benjamin-wilson/NerdNOS | 2024-04-03 | 2024-08-12 | 13 | 8 |
| benjamin-wilson/mining-pools | 2024-02-18 | 2025-03-23 | 3 | 1 |

Note: benjamin-wilson/qaxe hosts the NerdQAxe++ rev.7 branch (see bitaxeorg/foss-miner-list).

### Patsch91 (NerdOCTAXE)

| repo | created | pushed | stars | forks |
|---|---|---|---|---|
| Patsch91/NerdOCTAXE-Gamma | 2024-09-05 | 2026-04-27 | 93 | 17 |
| Patsch91/NerdOCTAXE-Plus | 2024-08-14 | 2024-10-14 | 33 | 3 |
| Patsch91/8Iaxe | 2024-06-30 | 2024-09-05 | 20 | 1 |
| Patsch91/NerdHAXE-Gamma | 2025-01-16 | 2025-07-21 | 15 | 1 |

### WantClue (BitForge Nano / ForgeOS / community tooling)

| repo | created | pushed | stars | forks |
|---|---|---|---|---|
| WantClue/bitaxe-web-flasher | 2024-01-12 | 2024-11-26 | 18 | 8 |
| WantClue/piaxe-miner | 2024-01-25 | 2024-02-18 | 7 | 0 |
| WantClue/NerdMiner_v2 | 2023-05-14 | 2026-05-04 | 6 | 0 |
| WantClue/pool-investigator | 2025-11-28 | 2025-12-05 | 5 | 2 |
| WantClue/forge-os | 2025-09-11 | 2026-09-26 | 5 | 5 |
| WantClue/bitaxe-viewer-ext | 2024-08-25 | 2024-09-08 | 5 | 1 |
| WantClue/ESP-Miner-WantClue | 2023-11-23 | 2026-09-23 | 5 | 3 |
| WantClue/Influx-Grafana-Nerd-Axe | 2025-04-07 | 2025-05-09 | 3 | 2 |

### TinyChipHub org (supraHex / bitaxeHex-TCH)

| repo | created | pushed | stars | forks |
|---|---|---|---|---|
| TinyChipHub/ESP-Miner-TCH | 2024-06-13 | 2026-08-31 | 27 | 4 |
| TinyChipHub/supraHex | 2024-09-09 | 2024-09-09 | 4 | 1 |
| TinyChipHub/bitaxeHex-TCH | 2024-08-09 | 2025-03-10 | 4 | 2 |
| TinyChipHub/ESP-Miner-Zyber | 2025-04-17 | 2026-08-22 | 2 | 1 |

## Notes

- **OSMU has no central GitHub org** (searched `type:org` for "osmu"). Its hubs are the osmu.wiki site, the OSMU Discord (discord.gg/osmu, per bitaxeorg/legitlist), and `bitaxeorg/osmu-wiki`. OSMU-labeled lab content lives there.
- **Proto (Block-affiliated mining company): no public GitHub org found** via org/repo search ("proto mining", proto rig) as of this snapshot; `block` org shows no obviously mining-related public repos except `block/mcp-council-of-mine` (description empty, relevance unverified). Treat Proto's public-repo status as UNVERIFIED pending direct confirmation.
- Fork genealogy (forks of skot/bitaxe, ESP-Miner, NerdMiner_v2 with created dates) was not collected in this pass; it is the cheapest way to quantify descendant projects and should be collected next via `GET /repos/{o}/{r}/forks?sort=oldest`.
- Star-history timelines require the stargazers endpoint with star timestamps (`Accept: application/vnd.github.star+json`); not collected.
