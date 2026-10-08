# bitaxeorg/ESP-Miner issue #1769: Nerdos ip address missing on swarm

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1769
> Collected: 2026-10-07
> Published: 2026-06-17

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1769
- State: closed
- Author: mutatrum
- Opened: 2026-06-17
- Closed: 2026-08-24
- Labels: none

## Description

There's a slight mismatch on the API between Nerdos and AxeOS, as the IP address is missing.

Screenshot is from #1240, but I suspect this is also for `master`.

<img width="1282" height="452" alt="Image" src="https://github.com/user-attachments/assets/f2851255-2e2d-49da-aa0c-52024323ca94" />

## Comments

### mutatrum on 2026-06-17

From @bonifacio123:
> This is output from firmware: v1.1.0-beta1:

```
{
  "asicCount": 4,
  "smallCoreCount": 2040,
  "deviceModel": "NerdQAxe++",
  "hostip": "172.17.1.4",
  "macAddr": "AC:A7:04:FB:77:D0",
  "wifiRSSI": -63,
  "power": 103,
  "maxPower": 100,
  "minPower": 52,
  "maxVoltage": 13,
  "minVoltage": 11,
  "current": 8437.5,
  "currentA": 8.4375,
  "minCurrentA": 0,
  "maxCurrentA": 8,
  "temp": 59.875,
  "vrTemp": 55.9375,
  "vrTempInt": 58.75,
  "hashRateTimestamp": 43170450,
  "hashRate": 5455.551,
  "hashRate_1m": 5511.287,
  "hashRate_10m": 5512.898,
  "hashRate_1h": 5509.091,
  "hashRate_1d": 2748.972,
  "coreVoltage": 1150,
  "defaultCoreVoltage": 1150,
  "coreVoltageActual": 1150,
  "fanspeed": 54,
  "manualFanSpeed": 100,
  "fanrpm": 1796,
  "fanrpm2": 1557,
  "fanspeed2": 40,
  "fanCount": 2,
  "lastpingrtt": 1.285714286,
  "recentpingloss": 0,
  "shutdown": false,
  "duplicateHWNonces": 0,
  "stratum": {
    "poolMode": 0,
    "activePoolMode": 0,
    "poolBalance": 50,
    "totalBestDiff": 13790464144,
    "usingFallback": false,
    "pools": [
      {
        "connected": true,
        "verifyBlocked": "",
        "poolDifficulty": 16384,
        "networkDifficulty": 124932866000000,
        "poolDiffErr": false,
        "accepted": 3492,
        "rejected": 3,
        "pingRtt": 1.285714286,
        "pingLoss": 0,
        "bestDiff": 14137811,
        "activeProtocol": 0,
        "encrypted": false
      }
    ]
  },
  "poolDifficulty": 16384,
  "networkDifficulty": 124932866000000,
  "foundBlocks": 0,
  "totalFoundBlocks": 0,
  "sharesAccepted": 3492,
  "sharesRejected": 3,
  "bestDiff": 13790464144,
  "bestSessionDiff": 14137811,
  "asicTemps": [
    0,
    0,
    0,
    0
  ],
  "pidTargetTemp": 60,
  "pidP": 6,
  "pidI": 0.1,
  "pidD": 10,
  "fans": [
    {
      "label": "M2",
      "mode": 2,
      "manualSpeed": 100,
      "overheatTemp": 70,
      "rpm": 1796,
      "speedPerc": 54,
      "pid": {
        "targetTemp": 60,
        "p": 6,
        "i": 0.1,
        "d": 10
      }
    },
    {
      "label": "M1",
      "mode": 0,
      "manualSpeed": 40,
      "overheatTemp": 80,
      "rpm": 1557,
      "speedPerc": 40,
      "pid": {
        "targetTemp": 65,
        "p": 6,
        "i": 0.1,
        "d": 10
      }
    }
  ],
  "hostname": "qaxe6",
  "ssid": "peachpit",
  "stratumURL": "172.17.1.6",
  "stratumPort": 2018,
  "stratumUser": "abc.qaxe6",
  "stratumEnonceSubscribe": true,
  "stratumTLS": false,
  "fallbackStratumURL": "solo.ckpool.org",
  "fallbackStratumPort": 3333,
  "fallbackStratumUser": "abc.qaxe6",
  "fallbackStratumEnonceSubscribe": true,
  "fallbackStratumTLS": false,
  "stratumProtocol": 0,
  "fallbackStratumProtocol": 0,
  "sv2AuthorityPubkey": "",
  "fallbackSv2AuthorityPubkey": "",
  "sv2ChannelType": 0,
  "fallbackSv2ChannelType": 0,
  "voltage": 12250,
  "frequency": 680,
  "defaultFrequency": 600,
  "jobInterval": 500,
  "stratumDifficulty": 1000,
  "overheat_temp": 70,
  "flipscreen": 0,
  "invertscreen": 0,
  "autoscreenoff": 1,
  "invertfanpolarity": 0,
  "autofanspeed": 2,
  "stratum_keep": 1,
  "vrFrequency": 25011,
  "defaultVrFrequency": 25011,
  "otp": false,
  "ASICModel": "BM1370",
  "uptimeSeconds": 43173,
  "lastResetReason": "SYSTEM.RESET_SOFTWARE",
  "wifiStatus": "WiFi Connected!",
  "freeHeap": 6890556,
  "freeHeapInt": 148248,
  "version": "v1.1.0-beta1",
  "runningPartition": "ota_0",
  "defaultTheme": "cosmic"
}
```

### mutatrum on 2026-06-17

@bonifacio123  Does Nerdos also have an `asic` endpoint?

### bonifacio123 on 2026-06-17

> [@bonifacio123](https://github.com/bonifacio123) Does Nerdos also have an `asic` endpoint?

Yes, /api/system/asic

```
{
  "ASICModel": "BM1370",
  "deviceModel": "NerdQAxe++",
  "asicCount": 4,
  "defaultFrequency": 600,
  "defaultVoltage": 1150,
  "absMaxFrequency": 800,
  "absMaxVoltage": 1400,
  "ecoFrequency": 0,
  "ecoVoltage": 0,
  "swarmColor": "#e700d8",
  "frequencyOptions": [500, 515, 525, 550, 575, 590, 600],
  "voltageOptions": [1120, 1130, 1140, 1150, 1160, 1170, 1180, 1190, 1200]
}

### mutatrum on 2026-06-17

Ok, this is dependent on #1240, as swarm changes quite a bit there but it seems quite trivial to look for the `hostip` in case the `ipv4` field is not available.

### WantClue on 2026-08-22

this is also missing the ip of bitforge.
