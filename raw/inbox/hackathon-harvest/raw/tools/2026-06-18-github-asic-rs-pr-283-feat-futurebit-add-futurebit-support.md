# 256foundation/asic-rs pull request #283: feat(futurebit): add futurebit support

> Source: https://github.com/256foundation/asic-rs/pull/283
> Collected: 2026-10-07
> Published: 2026-06-18

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 283
- State: closed
- Author: b-rowan
- Opened: 2026-06-18
- Closed: 2026-06-18
- Labels: none

## Description

(no description)

## Comments

### b-rowan on 2026-06-18

cc @plebhash

### plebhash on 2026-06-18

tACK

testing methodology:
- check out [`GitGab19:asic-rs-data-in-tproxy`](https://github.com/GitGab19/sv2-apps/tree/asic-rs-data-in-tproxy) branch locally (from PR https://github.com/stratum-mining/sv2-apps/pull/553)
- point to [`b-rowan:futurebit-support`](https://github.com/b-rowan/asic-rs/tree/futurebit-support) branch for `asic-rs` /  `asic-rs-core` deps
- spawn tProxy and connect FutureBit Apollo II to it
- probe tProxy's `/api/v1/sv1/clients` HTTP API endpoint on port 9092

```
$ curl -s "http://127.0.0.1:9092/api/v1/sv1/clients" | jq
{
  "offset": 0,
  "limit": 25,
  "total": 1,
  "items": [
    {
      "client_id": 1,
      "channel_id": 1,
      "connection_ip": "192.168.15.7",
      "authorized_worker_name": "apollo",
      "user_identity": "apollo",
      "target_hex": "000000000003c4abcada7e10c6f2c4187239a1128aff9f5260b3bb52e471378f",
      "hashrate": 7469654300000.0,
      "stable_hashrate": false,
      "extranonce1_hex": "0101b7ea000000000000000000000000",
      "extranonce2_len": 4,
      "version_rolling_mask": "1fffe000",
      "version_rolling_min_bit": "00000010",
      "miner_telemetry": {
        "ip": "192.168.15.7",
        "make": "FutureBit",
        "model": "Apollo2",
        "firmware_version": "2.0.2",
        "reported_hashrate_hs": 0.0,
        "power_consumption_w": 263.0,
        "efficiency_j_per_th": null,
        "average_temperature_c": 76.0,
        "uptime_secs": 357,
        "is_mining": true
      }
    }
  ]
}
```
