# bitaxeorg/ESP-Miner issue #945: Unconfuse sensor readings and configuration settings

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/945
> Collected: 2026-10-07
> Published: 2025-05-23

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 945
- State: closed
- Author: mutatrum
- Opened: 2025-05-23
- Closed: 2026-10-02
- Labels: none

## Description

Currently, the API endpoints have one bag for everything, sensor readings and configuration settings. This leads to confusing field names, such as `maxTemp` and `tempHighest`, and a few others.

One idea would be to separate these out, either in the JSON struct, or into separate endpoints. One for configuration, the other for sensor readings. Or maybe in another division, needs to be investigated.

It's also sort of continuation of the `asic` endpoint, which has hardware configuration. So separate endpoints would make sense IMO.

https://github.com/bitaxeorg/ESP-Miner/pull/888/files#r2103884794

## Comments

### 0xf0xx0 on 2025-06-03

here's my proposal:

## `/api/system/info` renamed to `/api/system/status`
live stats snapshot
```json
{
  "bestDiff",
  "bestSessionDiff",
  "coreVoltageActual",
  "current",
  "expectedHashrate",
  "fanrpm",
  "fanspeed",
  "freeHeap",
  "hashRate",
  "power",
  "sharesAccepted",
  "sharesRejected",
  "sharesRejectedReasons",
  "stratumDiff",
  "temp",
  "uptimeSeconds",
  "voltage",
  "vrTemp",
  "wifiRSSI"
}
```
`wifiStatus` should be dropped, it's kinda a useless key. if you can see it, the axe is already connected to wifi.

## `/api/system/asic` -> `/api/system/board`
General board info, mostly static
```json
{
  "ASICModel",
  "apEnabled",
  "asicCount",
  "boardVersion",
  "defaultFrequency",
  "defaultVoltage",
  "frequencyOptions",
  "display",
  "idfVersion",
  "isPSRAMAvailable",
  "macAddr",
  "maxPower",
  "nominalVoltage",
  "runningPartition",
  "smallCoreCount",
  "version",
  "voltageOptions"
}
```
i feel like `isPSRAMAvailable` and `apEnabled` fit here better, they're not runtime things
`apEnabled` might be a pointless key like `wifiStatus`, the only usecase i can think of is a semi-automated setup process where you connect to the axe and run a script? but that could be done without needing `apEnabled`.

`display` also shouldn't change at runtime. that's... i'd be concerned for anyone that would hot-swap a display. why *is* it mutable?


## `/api/system/config` (or `/api/system/info`)
```json
{
  "autofanspeed",
  "coreVoltage",
  "displayTimeout",
  "fallbackStratumPort",
  "fallbackStratumURL",
  "fallbackStratumUser",
  "flipscreen",
  "frequency",
  "hostname",
  "invertscreen",
  "isUsingFallbackStratum",
  "overclockEnabled",
  "overheat_mode",
  "ssid",
  "statsDuration",
  "statsLimit",
  "stratumPort",
  "stratumURL",
  "stratumUser",
  "temptarget"
}
```
this one's my wildcard, i feel stuff that can be configured at runtime should be on it's own endpoint. it makes `/status` a lil weird though, with keys like `expectedHashrate` and `stratumDiff` being left up there. `hostname` can be updated, but requires a reboot to apply.

### mutatrum on 2025-06-04

The `display` is a work in progress. Most boards have a pin header for the display, and you can swap them. Not hot-swap, that'll probably break something (maybe we should add a warning there!). `display` belongs to `invertscreen` and `flipscreen`.

`isUsingFallbackStratum` is read only, so that should be on status 

`overheat_mode` should maybe be on `config` as well as on `status`.

There was some talk on a `v2` for the API, and then there is also your PR #667. That might make sense, but if there's a `v2`, we need to keep the current api as-is for a version or 2.

### 0xf0xx0 on 2025-06-04

> There was some talk on a v2 for the API, and then there is also your PR https://github.com/bitaxeorg/ESP-Miner/pull/667. That might make sense, but if there's a v2, we need to keep the current api as-is for a version or 2.

yeah, has there been any consensus on the best way to go about that? imo deprecating the current api for a version and then switching to v2 would be best, having both at the same time would be a lot of duplicated code.

### 0xf0xx0 on 2025-06-09

@kha1n3vol3 @hurllz @remcoros @KillerInk looking for your inputs on my proposal uwu  
feel free to tag other api users, i tried to get a variety of usecases

### KillerInk on 2025-06-09

would splitt the config even more into pool wifi oc stats

### remcoros on 2025-06-09

for telemetry, it would be easiest and most performant to have everything on a single endpoint, so it needs to hit the http server only once per measurement interval.

Ideally, a service that exposes metrics would have a '/metrics' endpoint, exposing all metric and config values in prometheus/opentelemtry compatible format, specifically for scraping. And create '/api/*' (json) endpoints for use in UIs.

Also, if you're going to create new endpoints, and keep it json, could a few of those values that are now strings be send as numbers instead (like bestDiff and bestSessionDiff), this makes scraping and storing them in a time series db and showing them by 'max value' much easier.

### 0xf0xx0 on 2025-06-16

667 is in a testable state and has most of your suggestions, other than prometheus as i'm not sure how best to add that. i didn't split the config, but i did order the keys. feedback is welcome uwu

### 0xf0xx0 on 2025-10-23

updating my proposal with the current api and my opinions poking it:

# `/api/v2/status`
live mining/asic data, nothings changed

```
"power"
"current"
"voltage"
"coreVoltageActual"

"temp"
"temp2"
"vrTemp"
"fanRPM"
"fanSpeed"

"hashrate"
"expectedHashrate"
"hashrateMonitor"

"poolDifficulty"
"bestDiff"
"bestSessionDiff"
"blockFound"

"isUsingFallbackStratum"
"sharesAccepted"
"sharesRejected"
"sharesRejectedReasons"
"responseTime"

"blockHeight"
"scriptSig"
"networkDifficulty"

"overheatMode"
```

# `/api/v2/asic`

ASIC-specific keys, like name, count, and default settings

```
"asicModel"
"asicCount"
"hashDomains"
"smallCoreCount"

"defaultFrequency"
"defaultVoltage"

"frequencyOptions"
"voltageOptions"
```

# `/api/v2/board`

Non-mining runtime and board info, like hostname, swarm color, versions, and uptime

```
"hostname"
"ssid"
"apEnabled"

"deviceModel"
"boardVersion"
"swarmColor"
"display"

"maxPower"
"nominalVoltage"

"freeHeap"
"freeHeapInternal"
"freeHeapSpiram"
"isPSRAMAvailable"

"ipv4"
"ipv6"
"macAddr"
"wifiRSSI"

"runningPartition"
"uptimeSeconds"

"axeOSVersion"
"idfVersion"
"version"
```

# `/api/v2/config`

static config info, also the PATCH to update the config  
the `overheatMode` here could be removed in favor of the one in `/status`

```
"frequency"
"coreVoltage"
"autoFanSpeed"
"tempTarget"

"stratumURL"
"stratumUser"
"stratumPort"
"stratumSuggestedDifficulty"
"stratumExtranonceSubscribe"
"fallbackStratumURL"
"fallbackStratumUser"
"fallbackStratumPort"
"fallbackStratumSuggestedDifficulty"
"fallbackStratumExtranonceSubscribe"

"displayTimeout"
"invertScreen"
"rotation"
"statsFrequency"
"overclockEnabled"
"overheatMode"
```

# `/api/v2/statistics`
# `/api/v2/restart`
# `/api/v2/wifi/scan`
# `/api/v2/ota/webui`
or `/axeos`? keep the `/www`?
# `/api/v2/ota/firmware`
or `/fw`
# `/api/v2/ws`
`/logs` is more descriptive, unless we want to eventually have multiple websockets, in which case id propose `/ws/*` to group them.

### mutatrum on 2025-10-31

Apologies for the late comments, I was pondering this for quite a while. Some suggestions:

- Have a top level structure and put content in a `data` field, so you can handle errors uniformly with an `errors` array;
- Add units to all fields. `power` -> `power_w`, `voltage_mv`, etc;
- Personally i would prefect snake_case, instead of CamelCase, but that's a style thing;
- `overheatMode` in `status`, change to a `status` array with objects. each `message` string and  string and `status` . Currently there's also `power_fault`, also to status.
- Maybe add a bit more structure with nesting:
  - status: group fields into power/temperature/hashrate/difficulty/shares objects
  - board: wifi/hardware/power_limits/memory/network/firmware/tuning_options
  - config: mining/stratum/display
- config/stratum: make this a `pools` array (0 = primary, 1 = secondary) so we can later on extend to > 2. Change `isUsingFallbackStratum` (now in status) and put it into `config/stratum`. Similar for temperatures and fans.
- Change restart to `control` with an `action` payload, so we can later on add `mining_stop` and `mining_start`, maybe others (`clear_overheat` maybe?)

Thinking about it further, there's specific roles for each endpoint. F.e. the dashboard should not have to consult the config endpoint, that would defeat the purpose. So that means that it should f.e. also show the current connected stratum server. I think that should be leading.

So, looking over the dashboard, I see the following items, for `status`:

```
{
  "api_version": "v2",
  "timestamp": "string", 
  "data": {
    "status": [
      {
         "code": "string", // overheat power_failury block_found etc
         "message": "string",
         "severity": "string", // info warning error
      },
    ]
    "network": {
      "hostname": "string",
      "wifi_rssi_dbm": "number",
      "uptime_ms": "number",
    },
    "mining": {
      "asic_frequency": "number",
      "hashrate_ghs": "number",
      "expected_hashrate_ghs": "number",
      "average_hashrate_ghs": "number", // this should ideally be calculated in the backend
      "error_count": "number",
      "asics": [
        {
          "total_ghs": "number",
          "domains_ghs": [
            "number",
            "number",
            "number",
            "number",
          ],
          "error_ghs": "number",
        }
      ],
      "best_difficulty": "number",
      "best_session_difficulty": "number",
    },
    "power": {
      "power_w": "number",
      "input_voltage_v": "number",
      "nominal_voltage_v": "number",
      "asic_voltage_v": "number",
      "efficiency_j_per_ghs": "number",
      "expected_efficiency_j_per_ghs": "number",
      "average_efficiency_j_per_ghs": "number", // preferable from backend
    },
    "thermal": {
      "temperatures": [
        {
          "sensor": "string", // asic voltage_regulator board
          "index": "number",
          "value_c": "number",
        }
      ]
    },
    "fans": {
      "fan_speed_pct": [ // Currently only one but could be more in the future.
        "number",
      ],
      "fan_rpm": [
        "number",
      ]
    },
    "shares": {
      "accepted": "number",
      "rejected": "number",
      "rejected_reasons": [
        {
          "message": "string",
          "count": "number",
        }
      ]
    },
    "pool": {
      "current_pool": "number",
      "stratum_url": "string",
      "stratum_port": "number",
      "stratum_user": "string",
      "ping_ms": "number",
      "connected": true,
    },
    "block_header": {
      "block_height": "number",
      "network_difficulty": "number",
      "scriptsig": "string",
    }
  },
  "errors": [], // only for http/rest/fatal errors
}
```
This way, the dashboard only needs this endpoint.

The other endpoints in a similar vain, structured, with units, and expandable for the future.

I understand this is a major undertaking, and to make it easier I would opt for _not_ replacing the current api, but slowly building out the v2 api, field for field, until it's complete. This has the benefit of having swarm still work, and it won't be a 100 file PR in one go. I can also do a proposal for the other endpoints, if you want.

### 0xf0xx0 on 2025-10-31

> * Have a top level structure and put content in a `data` field, so you can handle errors uniformly with an `errors` array;

hm, but if we have an error we'd be short-circuiting through a 500 error response, which would hold an error object like the 404 response. sending a data and error object complicates clients as they cant rely on a 200 to always be ok.

> * Add units to all fields. `power` -> `power_w`, `voltage_mv`, etc;

i like that for the shorter units, but `_j_per_ghs`/`jPerGHs` is kinda clunky imo. any reason we cant rely on the openapi spec to define the units?

> * Personally i would prefect snake_case, instead of CamelCase, but that's a style thing;

yea, we can do either/or, as long as its consistent :3
      
> * `overheatMode` in `status`, change to a `status` array with objects. each `message` string and  string and `status` . Currently there's also `power_fault`, also to status.

ooo yee that works

> * Maybe add a bit more structure with nesting:
>       
> * status: group fields into power/temperature/hashrate/difficulty/shares objects
> * board: wifi/hardware/power_limits/memory/network/firmware/tuning_options
> * config: mining/stratum/display

> * config/stratum: make this a `pools` array (0 = primary, 1 = secondary) so we can later on extend to > 2. Change `isUsingFallbackStratum` (now in status) and put it into `config/stratum`. Similar for temperatures and fans.

this could tie into #1146 as we would have the pool struct there :3

> * Change restart to `control` with an `action` payload, so we can later on add `mining_stop` and `mining_start`, maybe others (`clear_overheat` maybe?)


> 
> Thinking about it further, there's specific roles for each endpoint. F.e. the dashboard should not have to consult the config endpoint, that would defeat the purpose. So that means that it should f.e. also show the current connected stratum server. I think that should be leading.

ehh, that kinda re-confuses the main endpoint though. the separation in my proposal separates the live, polled data from the less used semi-static data. for example, the dashboard main page only needs to update the mining info; it doesnt need to re-fetch, say, the nominal voltage or ssid.

> 
> So, looking over the dashboard, I see the following items, for `status`:
> 
> ```
> {
>   "api_version": "v2",
>   "timestamp": "string", 
>   "data": {
>     "status": [
>       {
>          "code": "string", // overheat power_failury block_found etc
>          "message": "string",
>          "severity": "string", // info warning error
>       },
>     ]
>     "network": {
>       "hostname": "string",
>       "wifi_rssi_dbm": "number",
>       "uptime_ms": "number",
>     },
>     "mining": {
>       "asic_frequency": "number",
>       "hashrate_ghs": "number",
>       "expected_hashrate_ghs": "number",
>       "average_hashrate_ghs": "number", // this should ideally be calculated in the backend
>       "error_count": "number",
>       "asics": [
>         {
>           "total_ghs": "number",
>           "domains_ghs": [
>             "number",
>             "number",
>             "number",
>             "number",
>           ],
>           "error_ghs": "number",
>         }
>       ],
>       "best_difficulty": "number",
>       "best_session_difficulty": "number",
>     },
>     "power": {
>       "power_w": "number",
>       "input_voltage_v": "number",
>       "nominal_voltage_v": "number",
>       "asic_voltage_v": "number",
>       "efficiency_j_per_ghs": "number",
>       "expected_efficiency_j_per_ghs": "number",
>       "average_efficiency_j_per_ghs": "number", // preferable from backend
>     },
>     "thermal": {
>       "temperatures": [
>         {
>           "sensor": "string", // asic voltage_regulator board
>           "index": "number",
>           "value_c": "number",
>         }
>       ]
>     },
>     "fans": {
>       "fan_speed_pct": [ // Currently only one but could be more in the future.
>         "number",
>       ],
>       "fan_rpm": [
>         "number",
>       ]
>     },
>     "shares": {
>       "accepted": "number",
>       "rejected": "number",
>       "rejected_reasons": [
>         {
>           "message": "string",
>           "count": "number",
>         }
>       ]
>     },
>     "pool": {
>       "current_pool": "number",
>       "stratum_url": "string",
>       "stratum_port": "number",
>       "stratum_user": "string",
>       "ping_ms": "number",
>       "connected": true,
>     },
>     "block_header": {
>       "block_height": "number",
>       "network_difficulty": "number",
>       "scriptsig": "string",
>     }
>   },
>   "errors": [], // only for http/rest/fatal errors
> }
> ```
> 
> This way, the dashboard only needs this endpoint.

hmm, some nits:

- `api_version` complicates json parsing in stricter languages like go, as you have to unmarshal in one step to get the version and then unmarshal again to the correct api type. versioning in the url is easier for consumers and also rest api convention (https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design#implement-versioning).
- whats `timestamp` for?
- im not sure about the nesting, for example `thermals` could be a `temperatures` object,like so:
```json
"temperatures": {
    "temp1": 69,
    "temp2": 420,
    "vreg": 9000000
}
```
- `fans` is a similar nit, it could be an array like
```json
"fans": [
    {"pct": 50, "rpm": 9876543},
    {"pct": 20, "rpm": 80},
    {"pct": 100, "rpm": 1},
]
```

> The other endpoints in a similar vain, structured, with units, and expandable for the future.
> 
> I understand this is a major undertaking, and to make it easier I would opt for _not_ replacing the current api, but slowly building out the v2 api, field for field, until it's complete. This has the benefit of having swarm still work, and it won't be a 100 file PR in one go. I can also do a proposal for the other endpoints, if you want.

isnt swarm a frontend thing? the transition i have in mind is swarm will fallback to the old api for a time before dropping it.


### 0xf0xx0 on 2025-11-01

another thing, we should rename `bestSessionDiff` to `bestDiffSinceBoot`, and maybe `bestDiff` to `athDiff` or something similar.

### 0xf0xx0 on 2025-11-23

some tweaks to your /status proposal:

```
{
    "mining": {
        "asic_frequency": "number",
        "hashrate": "number",
        "expected_hashrate": "number",
        "average_hashrate": "number", // this should ideally be calculated in the backend
        "error_count": "number",
        "asics": [
            {
                "total": "number",
                "domains": ["number", "number"],
                "error": "number",
            },
        ],
        "shares": {
            "accepted": "number",
            "rejected": "number",
            "rejected_reasons": [
                {
                    "message": "string",
                    "count": "number",
                },
            ],
        },
        "pool": {
            "current_pool": "number",
            "stratum_url": "string",
            "stratum_port": "number",
            "stratum_user": "string",
            "ping": "number",
            "connected": "boolean",
        },
        "current_job": {
            "height": "number",
            "network_difficulty": "number",
            "scriptsig": "string",
        }, 
        "best_difficulty": "number",
        "best_session_difficulty": "number",
    },
    "power": {
        "power": "number",
        "input_voltage": "number",
        "nominal_voltage": "number",
        "asic_voltage": "number",
        "efficiency": "number",
        "expected_efficiency": "number",
        "average_efficiency": "number", // preferable from backend
    },
    "temperatures": {
        "sensors": [
            {
                "name": "string", // asic voltage_regulator board
                "temp": "number",
            },
        ],
    },
    "fans": [
        { "pct": 50, "rpm": 9876543 },
        { "pct": 20, "rpm": 80 },
        { "pct": 100, "rpm": 1 },
    ],
    "status": [
        {
            "code": "string", // overheat power_failury block_found etc
            "message": "string",
            "severity": "string", // info warning error
        },
    ],
    "network": {
        "hostname": "string",
        "wifi_rssi": "number",
        "uptime": "number",
    },
}
```

id love to see your ideas for the other endpoints.

### mutatrum on 2026-10-02

Not worth the maintenance and support hassle considering this not only touches Bitaxes, but also NerdOS, external scripts, apps, etc.
