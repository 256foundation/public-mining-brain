# 256foundation/asic-rs release notes (20 releases)

> Source: https://github.com/256foundation/asic-rs/releases
> Collected: 2026-10-07
> Published: Unknown

## v0.8.5 (v0.8.5)

- Published: 2026-09-29
- Link: https://github.com/256foundation/asic-rs/releases/tag/v0.8.5
- Prerelease: False

## [0.8.5] - 2026-09-29

### 🚀 Features

- Add hashboard enable controls ([#394](https://github.com/256-foundation/asic-rs/issues/394))

### 🐛 Bug Fixes

- *(braiins)* Refresh expired bearer token on 401 in v26_04 backend ([#391](https://github.com/256-foundation/asic-rs/issues/391))
- *(scanner)* Reduce local port pressure during discovery ([#397](https://github.com/256-foundation/asic-rs/issues/397))
- *(braiins)* Derive board activity from frequency ([#399](https://github.com/256-foundation/asic-rs/issues/399))
- *(release)* Break publish cycle and retry registry rate limits ([#400](https://github.com/256-foundation/asic-rs/issues/400))

### 📚 Documentation

- Add ePIC 1.38.3 powerplay OpenAPI spec ([#390](https://github.com/256-foundation/asic-rs/issues/390))

### 🧪 Testing

- *(antminer)* Add live pause test ([#393](https://github.com/256-foundation/asic-rs/issues/393))


## v0.8.1 (v0.8.1)

- Published: 2026-09-10
- Link: https://github.com/256foundation/asic-rs/releases/tag/v0.8.1
- Prerelease: False

## [0.8.1] - 2026-09-10

### 🚀 Features

- *(epic)* Support hashrate-split pool status ([#348](https://github.com/256-foundation/asic-rs/issues/348))
- *(presets)* Native named autotune/overclock presets (SupportsPresets) ([#291](https://github.com/256-foundation/asic-rs/issues/291))
- *(firmware)* On-demand firmware-update check ([#294](https://github.com/256-foundation/asic-rs/issues/294))
- *(timezone)* Get / set / list miner timezone ([#295](https://github.com/256-foundation/asic-rs/issues/295))
- Add best_share and session_best_share to MinerData ([#351](https://github.com/256-foundation/asic-rs/issues/351))
- *(data)* Expose detailed firmware operating state ([#357](https://github.com/256-foundation/asic-rs/issues/357))
- *(epic)* Add timezone config ([#358](https://github.com/256-foundation/asic-rs/issues/358))
- *(firmware)* Add non-mutating preflight API ([#360](https://github.com/256-foundation/asic-rs/issues/360))
- Add bitaxe 2.14.0 and update bitaxe functionality ([#361](https://github.com/256-foundation/asic-rs/issues/361))

### 🐛 Bug Fixes

- *(antminer)* Update stock firmware bundles ([#343](https://github.com/256-foundation/asic-rs/issues/343))
- *(factory)* Bound miner discovery operations ([#344](https://github.com/256-foundation/asic-rs/issues/344))
- *(factory)* Correct connectivity retry semantics ([#345](https://github.com/256-foundation/asic-rs/issues/345))
- *(tuning)* Represent disabled ptune as manual target ([#355](https://github.com/256-foundation/asic-rs/issues/355))
- *(epic)* Parse structured summary errors ([#359](https://github.com/256-foundation/asic-rs/issues/359))
- *(ci)* Add publish-interval to publish to prevent crates.io rate limiting

### 📚 Documentation

- Update README

### ⚡ Performance

- *(factory)* Race miner ports under scan limit ([#346](https://github.com/256-foundation/asic-rs/issues/346))

### 🧪 Testing

- *(braiins)* Add live auto-detection data test


## v0.8.0 (v0.8.0)

- Published: 2026-08-25
- Link: https://github.com/256foundation/asic-rs/releases/tag/v0.8.0
- Prerelease: False

## [0.8.0] - 2026-08-25

### 🚀 Features

- *(antminer)* Add L11 support ([#323](https://github.com/256-foundation/asic-rs/issues/323))
- *(types)* Derive TypeScript bindings for shared models ([#329](https://github.com/256-foundation/asic-rs/issues/329))
- *(core)* Name the algorithms this crate's miners actually mine ([#337](https://github.com/256-foundation/asic-rs/issues/337))
- *(core)* Let HashAlgorithm and HashRateUnit compare against their names ([#338](https://github.com/256-foundation/asic-rs/issues/338))
- Add S21++ ([#341](https://github.com/256-foundation/asic-rs/issues/341))

### 🐛 Bug Fixes

- *(antminer)* Send both keys when setting sleep mode ([#312](https://github.com/256-foundation/asic-rs/issues/312))
- Fallback to `get_system_info.cgi` when `miner_type.cgi` fails when identifying antminers ([#321](https://github.com/256-foundation/asic-rs/issues/321))
- *(antminer)* Read chain rate and board temps on newer stock firmware ([#324](https://github.com/256-foundation/asic-rs/issues/324))
- *(epic)* Report the miner serial rather than the control board CPU serial ([#327](https://github.com/256-foundation/asic-rs/issues/327))
- *(antminer)* Send `new_api` as a top-level flag rather than a `parameter` ([#328](https://github.com/256-foundation/asic-rs/issues/328))
- *(antminer)* Read power draw from the `new_api` stats payload ([#325](https://github.com/256-foundation/asic-rs/issues/325))
- *(braiins)* Report why a pool write was refused instead of returning false ([#331](https://github.com/256-foundation/asic-rs/issues/331))
- *(python)* Raise when a pool write fails instead of returning None ([#332](https://github.com/256-foundation/asic-rs/issues/332))
- *(epic)* Implement set_scaling_config instead of reporting false support ([#333](https://github.com/256-foundation/asic-rs/issues/333))
- *(braiins)* Report why a power-target write was refused instead of returning false ([#334](https://github.com/256-foundation/asic-rs/issues/334))
- *(hashrate)* Read algorithm and unit from the miner instead of assuming SHA-256 ([#335](https://github.com/256-foundation/asic-rs/issues/335))
- *(antminer)* Declare the algorithms #335 could not name ([#340](https://github.com/256-foundation/asic-rs/issues/340))

### 🚜 Refactor

- *(core)* Make HashRate.algo a HashAlgorithm instead of a String ([#339](https://github.com/256-foundation/asic-rs/issues/339))
- *(models)* Ensure every model has a valid algo property ([#342](https://github.com/256-foundation/asic-rs/issues/342))

### 🧪 Testing

- *(epic)* Add live perpetual tuning test ([#330](https://github.com/256-foundation/asic-rs/issues/330))

### ⚙️ Miscellaneous Tasks

- Ignore the build artifacts the test scripts generate ([#336](https://github.com/256-foundation/asic-rs/issues/336))


### New Contributors ❤️

* @cryptographicturk made their first contribution in #339

* @Erisli made their first contribution in #329


## v0.7.3 (v0.7.3)

- Published: 2026-07-29
- Link: https://github.com/256foundation/asic-rs/releases/tag/v0.7.3
- Prerelease: False

## [0.7.3] - 2026-07-29

### 🚀 Features

- *(avalonminer)* Add litestats telemetry and support new Avalon models ([#307](https://github.com/256-foundation/asic-rs/issues/307))
- *(antminer)* Add L3++ support ([#313](https://github.com/256-foundation/asic-rs/issues/313))
- Add support for elphapex DG series miners ([#311](https://github.com/256-foundation/asic-rs/issues/311))
- Add miner listener to python bindings ([#316](https://github.com/256-foundation/asic-rs/issues/316))
- Add `Validate` trait and `revalidate` function ([#314](https://github.com/256-foundation/asic-rs/issues/314))

### 🐛 Bug Fixes

- Epic volcminer control board parsing ([#308](https://github.com/256-foundation/asic-rs/issues/308))
- Map AxeOS VR temp to board, chip temp to chain ([#315](https://github.com/256-foundation/asic-rs/issues/315))

### 📚 Documentation

- Update README


### New Contributors ❤️

* @adamdecaf made their first contribution in #315


## v0.7.2 (v0.7.2)

- Published: 2026-06-30
- Link: https://github.com/256foundation/asic-rs/releases/tag/v0.7.2
- Prerelease: False

## [0.7.2] - 2026-06-30

### 🚀 Features

- *(auth)* Support custom credentials for authenticated actions ([#293](https://github.com/256-foundation/asic-rs/issues/293))
- *(throttle)* Native manual throttle (SetThrottle + throttle_percent) ([#289](https://github.com/256-foundation/asic-rs/issues/289))
- *(volcminer)* Add stock firmware support ([#298](https://github.com/256-foundation/asic-rs/issues/298))

### 🐛 Bug Fixes

- *(avalonminer)* Avoid panic when Avalon Q HBinfo is incomplete ([#300](https://github.com/256-foundation/asic-rs/issues/300))
- Derive EPic coin from model hash algorithm ([#306](https://github.com/256-foundation/asic-rs/issues/306))
- *(is-mining)* Ensure `is_mining` represents a paused state rather than hashrate ([#301](https://github.com/256-foundation/asic-rs/issues/301))

### 📚 Documentation

- Add miner support review guidelines ([#305](https://github.com/256-foundation/asic-rs/issues/305))


### New Contributors ❤️

* @gzw13999 made their first contribution in #300


## v0.7.1 (v0.7.1)

- Published: 2026-06-24
- Link: https://github.com/256foundation/asic-rs/releases/tag/v0.7.1
- Prerelease: False

## [0.7.1] - 2026-06-24

### 🚀 Features

- *(temp)* Configured thermal limits (min_startup/restart_temperature) ([#290](https://github.com/256-foundation/asic-rs/issues/290))
- *(power)* Expose factory default / min / max power target ([#292](https://github.com/256-foundation/asic-rs/issues/292))

### 🐛 Bug Fixes

- *(python)* Improve the type hinting outputs of the pydantic macros
- Ensure uptime/Duration can parse from iso8601 duration

### 📚 Documentation

- Add vnish v1.3.4 API schema

### ⚙️ Miscellaneous Tasks

- *(ci)* Ensure ci release works the first time


## v0.7.0 (v0.7.0)

- Published: 2026-06-22
- Link: https://github.com/256foundation/asic-rs/releases/tag/v0.7.0
- Prerelease: False

## [0.7.0] - 2026-06-22

### 🚀 Features

- *(vnish)* Implement SetPowerLimit (preset-based) ([#284](https://github.com/256-foundation/asic-rs/issues/284))
- *(vnish)* Surface miner_state as messages (self-managed alarm passthrough) ([#287](https://github.com/256-foundation/asic-rs/issues/287))
- *(temp)* 4-field temperature model (per-board chip inlet/outlet + miner coolant inlet/outlet) ([#286](https://github.com/256-foundation/asic-rs/issues/286))
- Add a logo ([#288](https://github.com/256-foundation/asic-rs/issues/288))

### 🐛 Bug Fixes

- *(pydantic)* Serialize Duration as timedelta, not float ([#282](https://github.com/256-foundation/asic-rs/issues/282))

### 📚 Documentation

- Update README

### ⚙️ Miscellaneous Tasks

- Fix missing tag value


## v0.6.2 (v0.6.2)

- Published: 2026-06-18
- Link: https://github.com/256foundation/asic-rs/releases/tag/v0.6.2
- Prerelease: False

## [0.6.2] - 2026-06-18

### 🚀 Features

- *(futurebit)* Add futurebit support ([#283](https://github.com/256-foundation/asic-rs/issues/283))

### 🐛 Bug Fixes

- *(features)* Weak `?` python features so firmwares actually gate ([#278](https://github.com/256-foundation/asic-rs/issues/278)) ([#281](https://github.com/256-foundation/asic-rs/issues/281))
- Fix regression in device info and hardware with getters
- Ensure generated .pyi type hints are accurate with pyO3
- *(makes)* Ensure that miner models/makes are all and checked for unknowns ([#279](https://github.com/256-foundation/asic-rs/issues/279))

### ⚙️ Miscellaneous Tasks

- *(ci)* Update upload artifact action
- *(python)* Fix license so pypi will allow publishing


## v0.6.0 (v0.6.0)

- Published: 2026-06-09
- Link: https://github.com/256foundation/asic-rs/releases/tag/v0.6.0
- Prerelease: False

## [0.6.0] - 2026-06-09

### 🚀 Features

- Add scaled tuning target support ([#267](https://github.com/256-foundation/asic-rs/issues/267))
- *(epic)* Parse summary status messages ([#268](https://github.com/256-foundation/asic-rs/issues/268))
- Parse control boards from data values ([#269](https://github.com/256-foundation/asic-rs/issues/269))
- Convert board data into vec containing chip counts
- Add proto backend and rig support ([#266](https://github.com/256-foundation/asic-rs/issues/266))
- Add support for Avalon A15, and add chips for Avalon A1466

### 🐛 Bug Fixes

- *(epic)* Calculate v1 expected hashrate ([#270](https://github.com/256-foundation/asic-rs/issues/270))

### 📚 Documentation

- Update README

### ⚙️ Miscellaneous Tasks

- *(ci)* Ensure readme is properly update on release
- Reformat json and fix tests
- Ensure all hashrate values are using the default unit when returned


### New Contributors ❤️

* @jpcomps made their first contribution in #266


## v0.5.4 (v0.5.4)

- Published: 2026-06-02
- Link: https://github.com/256foundation/asic-rs/releases/tag/v0.5.4
- Prerelease: False

## [0.5.4] - 2026-06-02

### 🚀 Features

- *(whatsminer)* Parse timestamps for error messages ([#257](https://github.com/256-foundation/asic-rs/issues/257))
- Create `MinerComponent` and python bindings ([#261](https://github.com/256-foundation/asic-rs/issues/261))
- *(antminer)* Add S21 Pro+ model mapping ([#263](https://github.com/256-foundation/asic-rs/issues/263))

### 📚 Documentation

- Add unified zensical documentation and github pages ([#262](https://github.com/256-foundation/asic-rs/issues/262))
- Add supported devices list ([#264](https://github.com/256-foundation/asic-rs/issues/264))

### ⚙️ Miscellaneous Tasks

- Limit to 5 keyword tags for crate


## v0.5.3 (v0.5.3)

- Published: 2026-05-25
- Link: https://github.com/256foundation/asic-rs/releases/tag/v0.5.3
- Prerelease: False

## [0.5.3] - 2026-05-25

### 🚀 Features

- Allow selecting data for the `get_data` return ([#252](https://github.com/256-foundation/asic-rs/issues/252))

### 🐛 Bug Fixes

- Make async cleanup cancellation safe
- *(braiins)* Swap to always using graphql appeals for errors ([#258](https://github.com/256-foundation/asic-rs/issues/258))
- *(antminer)* Preserve 2020 miner config updates ([#260](https://github.com/256-foundation/asic-rs/issues/260))


## v0.5.2 (v0.5.2)

- Published: 2026-05-21
- Link: https://github.com/256foundation/asic-rs/releases/tag/v0.5.2
- Prerelease: False

## [0.5.2] - 2026-05-21

### 🚀 Features

- Add whatsminer v3 unlock
- *(passwords)* Create `ChangePassword` trait
- Add read logs and factory reset traits
- *(braiins)* Add support for changing password
- *(epic)* Add support for changing password
- *(vnish)* Add support for changing password
- *(braiins)* Add support for factory reset
- *(vnish)* Add support for factory reset
- *(braiins)* Add support for reading logs
- *(epic)* Add support for reading logs
- *(vnish)* Add support for reading logs
- *(python)* Add new control functions to python bindings

### 🐛 Bug Fixes

- *(antminer)* Make v2020 sleep mode writes effective ([#249](https://github.com/256-foundation/asic-rs/issues/249))
- *(braiins)* Handle 401 Unauthorized response and re-authenticate
- *(vnish)* Handle 401 Unauthorized response and re-authenticate
- *(braiins)* Split 25.07 and 26.04 web APIs

### ⚙️ Miscellaneous Tasks

- *(epic)* Update firmware name to umc os from epic ([#250](https://github.com/256-foundation/asic-rs/issues/250))
- *(ci)* Fix sealminer web api dead code warning ([#253](https://github.com/256-foundation/asic-rs/issues/253))
- *(ci)* Ensure tests get run on PRs
- *(ci)* Fix missing cargo.lock commit when running release


### New Contributors ❤️

* @aleksander-rudolf made their first contribution in #255

* @matt-jtdahlgren made their first contribution in #250


## v0.5.1 (v0.5.1)

- Published: 2026-05-05
- Link: https://github.com/256foundation/asic-rs/releases/tag/v0.5.1
- Prerelease: False

## [0.5.1] - 2026-05-05

### 🚀 Features

- *(braiins)* Add serial data to hashboards, and ensure all data is being returned correctly
- Add listen_ip_only to listener
- Add support for sealminer

### 🐛 Bug Fixes

- Fix tests for python bindings ([#240](https://github.com/256-foundation/asic-rs/issues/240))
- Fix bos 26.04/25.07 hashboard parsing
- *(epic)* Detect xilinx control boards in v1 backend ([#247](https://github.com/256-foundation/asic-rs/issues/247))

### 📚 Documentation

- Add vnish v1.2.7 API schema

### 🧪 Testing

- *(partial)* Add braiins test values and meta docs
- *(braiins)* Add tests for all braiins backends

### ⚙️ Miscellaneous Tasks

- Fix python tests by removing the other macro crate ([#242](https://github.com/256-foundation/asic-rs/issues/242))
- Add pre-commit hook to reformat json and reformat json files
- Add local pre-commit tests and fix unused test items
- *(release)* Use workflow dispatch for release instead of manual steps ([#248](https://github.com/256-foundation/asic-rs/issues/248))


## v0.5.0 (v0.5.0)

- Published: 2026-04-17
- Link: https://github.com/256foundation/asic-rs/releases/tag/v0.5.0
- Prerelease: False

## [0.5.0] - 2026-04-17

### 🚀 Features

- *(firmware)* Add upgrade options and ePIC system update upload ([#228](https://github.com/256-foundation/asic-rs/issues/228))
- Re-export core and firmware crates via asic-rs features ([#231](https://github.com/256-foundation/asic-rs/issues/231))
- Add support for luxOS events as messages ([#229](https://github.com/256-foundation/asic-rs/issues/229))
- Add Auradine support ([#230](https://github.com/256-foundation/asic-rs/issues/230))
- *(python)* [**breaking**] Expose pydantic models from rust ([#234](https://github.com/256-foundation/asic-rs/issues/234))

### 🐛 Bug Fixes

- Fix mining mode not existing in python tuning config ([#227](https://github.com/256-foundation/asic-rs/issues/227))
- Fix luxos chip count parsing when chips show status "Unknown" ([#226](https://github.com/256-foundation/asic-rs/issues/226))
- *(factory)* Bound miner discovery timeouts ([#232](https://github.com/256-foundation/asic-rs/issues/232))
- *(core)* Divide average_temperature by board count with data, not total boards
- *(core)* Guard against NaN/infinity in efficiency calculation when hashrate is zero
- *(core)* Return None for expected_chips when hardware specs are unavailable
- *(core)* Remove duplicate match arm in test discovery utility
- Avoid panics and repair PyO3 linking ([#235](https://github.com/256-foundation/asic-rs/issues/235))
- Resolve timeout refactor merge conflicts ([#236](https://github.com/256-foundation/asic-rs/issues/236))
- Fix tuning target formatting in python ([#239](https://github.com/256-foundation/asic-rs/issues/239))

### 🚜 Refactor

- *(antminer)* Replace is_none check and unwrap with let-else
- *(core)* Derive Copy for HashRateUnit and remove unnecessary clones
- *(firmware)* Ensure all backends have consistent hashboard parsing

### 🎨 Styling

- *(firmwares)* Standardize HashRate algo field to use to_string() consistently
- *(antminer)* Simplify MinerMode Display impl, remove needless String allocations
- *(firmwares)* Replace extract().map() with extract_map() for consistency
- *(antminer)* Simplify get_version_with_auth using early return with ?
- Use char literals instead of single-char strings in replace() calls

### ⚙️ Miscellaneous Tasks

- Allow use of pre-commit.ci ([#237](https://github.com/256-foundation/asic-rs/issues/237))


## v0.4.2 (v0.4.2)

- Published: 2026-04-08
- Link: https://github.com/256foundation/asic-rs/releases/tag/v0.4.2
- Prerelease: False

## [0.4.2] - 2026-04-08

### 🚀 Features

- Add Unknown(String) fallback to all model enums ([#222](https://github.com/256-foundation/asic-rs/issues/222))
- *(factory)* Support auth during miner discovery ([#224](https://github.com/256-foundation/asic-rs/issues/224))

### 🐛 Bug Fixes

- *(python)* Avoid hangs accessing miner message severity ([#220](https://github.com/256-foundation/asic-rs/issues/220))
- *(avalonminer)* Serialize ascset parameters as comma-separated string ([#223](https://github.com/256-foundation/asic-rs/issues/223))
- *(python)* Fix `into_unit` in the python bindings ([#221](https://github.com/256-foundation/asic-rs/issues/221))


## v0.4.1 (v0.4.1)

- Published: 2026-04-07
- Link: https://github.com/256foundation/asic-rs/releases/tag/v0.4.1
- Prerelease: False

## [0.4.1] - 2026-04-07

### 🚀 Features

- *(epic)* Add PowerPlay tuning setter with scaling input ([#210](https://github.com/256-foundation/asic-rs/issues/210))
- *(whatsminer)* Add error code lookup for GetMessages ([#201](https://github.com/256-foundation/asic-rs/issues/201)) ([#211](https://github.com/256-foundation/asic-rs/issues/211))
- Expose miner IP in python ([#217](https://github.com/256-foundation/asic-rs/issues/217))
- Add all rust control functions and config functions to python API ([#215](https://github.com/256-foundation/asic-rs/issues/215))

### 🐛 Bug Fixes

- *(whatsminer)* Surface actual error when V2 privileged RPC returns unencrypted response ([#212](https://github.com/256-foundation/asic-rs/issues/212))
- Eliminate runtime panics and add robustness guardrails ([#214](https://github.com/256-foundation/asic-rs/issues/214))
- *(antminer)* Map zynq7007 subtype to Xilinx control board ([#216](https://github.com/256-foundation/asic-rs/issues/216))
- *(python)* Fix uptime serialization in python bindings when uptime is `None` ([#218](https://github.com/256-foundation/asic-rs/issues/218))


## v0.4.0 (v0.4.0)

- Published: 2026-04-01
- Link: https://github.com/256foundation/asic-rs/releases/tag/v0.4.0
- Prerelease: False

## [0.4.0] - 2026-04-01

### 🚀 Features

- Replace wattage_limit with tuning_target enum
- *(core)* Add HashRateUnit string parsing ([#174](https://github.com/256-foundation/asic-rs/issues/174))
- Add pool config support
- Add scaling config support for epic backend ([#177](https://github.com/256-foundation/asic-rs/issues/177))
- Add tuning config support across miner traits and backends ([#183](https://github.com/256-foundation/asic-rs/issues/183))
- Add firmware upgrade for antminer stock ([#182](https://github.com/256-foundation/asic-rs/issues/182))
- *(antminer)* Support stock firmware pool configuration ([#185](https://github.com/256-foundation/asic-rs/issues/185))
- *(whatsminer)* Implement SupportsTuningConfig with MiningMode and V2 fallback ([#194](https://github.com/256-foundation/asic-rs/issues/194))
- *(epic)* Parse pools config from summary and hashrate split ([#197](https://github.com/256-foundation/asic-rs/issues/197))
- *(config)* Add fan config support and ePIC parsing ([#198](https://github.com/256-foundation/asic-rs/issues/198))
- *(marathon+luxos)* Add set pools config ([#203](https://github.com/256-foundation/asic-rs/issues/203))
- *(auth)* Add per-miner auth credentials ([#195](https://github.com/256-foundation/asic-rs/issues/195))

### 🐛 Bug Fixes

- *(python)* Rename wattage limit API to tuning target
- *(epic)* Set hashboard tuned from perpetual tune optimization
- *(python)* Silence type_complexity warnings in factory streams
- Fix send_rpc_command panic on error ([#181](https://github.com/256-foundation/asic-rs/issues/181))
- *(antminer)* Recognize BBCTRL control board alias
- *(whatsminer)* Correct inverted is_mining logic across all backends ([#187](https://github.com/256-foundation/asic-rs/issues/187))
- *(antminer)* Allow `BHB42XXX` to be found as an unknown stock antminer model
- Replace read_to_end with bounded stream reading and TCP shutdown ([#199](https://github.com/256-foundation/asic-rs/issues/199))
- *(factory)* Include all IPv4 subnet addresses during discovery ([#205](https://github.com/256-foundation/asic-rs/issues/205))
- *(factory)* Auto-adjust nofile limits before scans
- *(luxminer)* Prevent empty pools config test hang
- Fix tuning target parsing in python

### 💼 Other

- *(antminer)* Correct firmware version source ([#189](https://github.com/256-foundation/asic-rs/issues/189))

### 🚜 Refactor

- Rename wattage limit trait to tuning target
- Seperate parsing from getting for config ([#178](https://github.com/256-foundation/asic-rs/issues/178))
- *(epic)* Map Generic AM33XX control boards correctly to BeagleBoneBlack ([#207](https://github.com/256-foundation/asic-rs/issues/207))

### 🎨 Styling

- Apply workspace-wide formatting cleanup
- Normalize grouped imports across core and firmwares
- *(python)* Run black on python files

### ⚙️ Miscellaneous Tasks

- Format


### New Contributors ❤️

* @ankitgoswami made their first contribution in #204


## v0.3.0 (v0.3.0)

- Published: 2026-03-12
- Link: https://github.com/256foundation/asic-rs/releases/tag/v0.3.0
- Prerelease: False

## [0.3.0] - 2026-03-12

### 🚀 Features

- Add `SetPools` for braiins 25.07
- Add control functionality for VNish
- Implement ePIC pool and hashrate split updates ([#166](https://github.com/256-foundation/asic-rs/issues/166))
- [**breaking**] Use workspaces to speed up compile time and decouple types
- Add support for AMCB07 parsing in mara firmware
- Improve control board parse handling on mara
- *(python)* Add control board version to python data

### 🐛 Bug Fixes

- Fix failed `model_validate` call when calling `get_data` from python
- Assume hashrate returned from GetExpectedHashrate on LuxMinerV1 can be missing
- Add Unknown model/make variants to handle unrecognized models
- Handle VNish uptime format without days prefix
- Treat VNish auto-tuning state as mining
- Populate working_chips count for EPic hashboards
- Merge VNish hashboard data from both endpoints by board ID
- Merge VNish hashboard data from both endpoints by board ID
- Fix python code to work with workspace

### 🚜 Refactor

- Improve control board type handling

### 📚 Documentation

- Add ePIC 1.30.0 powerplay OpenAPI spec
- Update README

### ⚡ Performance

- Reuse shared HTTP client for discovery requests
- Parallelize data collection API commands

### 🧪 Testing

- Add live auto-detect epic miner parse test ([#165](https://github.com/256-foundation/asic-rs/issues/165))

### ⚙️ Miscellaneous Tasks

- Fix ci readme handling when releasing a new version
- Format
- Update version bump script
- Fix release to work with workspacing
- Add descriptions to cargo.toml so that the crates can publish


### New Contributors ❤️

* @cfilipescu made their first contribution in #166

* @DanNicolau made their first contribution in #156


## v0.2.1 (v0.2.1)

- Published: 2026-02-25
- Link: https://github.com/256foundation/asic-rs/releases/tag/v0.2.1
- Prerelease: False

## [0.2.1] - 2026-02-25

### ⚙️ Miscellaneous Tasks

- Remove macos 13


## v0.2.0 (v0.2.0)

- Published: 2026-02-25
- Link: https://github.com/256foundation/asic-rs/releases/tag/v0.2.0
- Prerelease: False

## [0.2.0] - 2026-02-25

### 🚀 Features

- Add auto-unlock for whatsminer V2 privileged commands
- Add support for braiinsOS from 21.09 to 25.07
- Add `SetPools` trait
- [**breaking**] Change pools in data to be a vec of PoolGroupData
- *(python)* Use new `PoolGroupData` in python bindings
- *(python)* Allow setting pools from python bindings
- Allow converting from `PoolGroupData` to `PoolGroup` for configuration
- Add pool group parsing for Braiins OS 21.09
- Add set pools implementation for whatsminer V3
- Add set pools implementation for whatsminer V2
- Implement `SetPools` for braiins 21.09

### 🐛 Bug Fixes

- Fix issue with some pools not being parsed properly if they start with `stratum.`, such as `stratum.braiins.com`
- Fix whatsminer set led functions not working properly
- *(python)* Fix incorrect typing and return type of scan streams
- *(python)* Fix incorrect return type for firmware in py miner
- Fix set power limit for whatsminers sending invalid power

### 📚 Documentation

- Add conventional commits badge to readme

### ⚙️ Miscellaneous Tasks

- Add git cliff integration to generate changelog on releases
- Add pre-commit hook to enforce conventional commits
- Add conventional commits check to PR checks
- Fix readme autogeneration
- Unify rust and python release workflows
- Add empty SetPools impl for Braiins OS 21.09
- Add tests for braiins 21.09
- Add meta files for braiins 21.09 graphql schema
