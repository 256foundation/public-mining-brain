# bitaxeorg/ESP-Miner issue #1493: poolAddrFamily returned but not documented

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1493
> Collected: 2026-10-07
> Published: 2026-01-05

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1493
- State: closed
- Author: adamdecaf
- Opened: 2026-01-05
- Closed: 2026-01-09
- Labels: documentation

## Description

**Describe the bug**
A JSON field `"poolAddrFamily":	2,` is returned from `GET /api/system/info` on my bitaxe gamma running v2.12.0, but the field is [not documented in the OpenAPI spec](https://github.com/bitaxeorg/ESP-Miner/blob/master/main/http_server/openapi.yaml).

**To Reproduce**
Steps to reproduce the behavior:
1. Fetch `/api/system/info` on a miner
2. Verify there's a field `poolAddrFamily` returned. 

**Expected behavior**
I can't seem to find [this field defined in the project](https://github.com/search?q=repo%3Abitaxeorg%2FESP-Miner+poolAddrFamily&type=code) so it's probably generated somehow. 

**Hardware (please complete the following information):**
 - Bitaxe HW version: Gamma 601
 - ESP-Miner FW version: v2.12.0


## Comments

### 0xf0xx0 on 2026-01-09

that key got renamed to `poolConnectionInfo`, heres your docs for `poolAddrFamily`: https://github.com/bitaxeorg/ESP-Miner/blob/a10e206b54831715a6babfb2dc0f4fc768adf386/main/http_server/openapi.yaml#L315

### adamdecaf on 2026-01-09

Gotcha, thanks

### adamdecaf on 2026-01-09

I'm still seeing poolAddrFamily returned in the json on v2.12.2

```json
{
	"power":	22.2116699,
	"voltage":	5039.0625,
	"current":	13843.75,
	"temp":	59.875,
	"temp2":	-1,
	"vrTemp":	75,
	"maxPower":	40,
	"nominalVoltage":	5,
	"hashRate":	1263.5794678,
	"hashRate_1m":	1274.7462158,
	"hashRate_10m":	1272.0834961,
	"hashRate_1h":	1272.0834961,
	"expectedHashrate":	1275,
	"errorPercentage":	0,
	"bestDiff":	6702259710,
	"bestSessionDiff":	46346,
	"poolDifficulty":	8192,
	"isUsingFallbackStratum":	0,
	"poolAddrFamily":	2,
	"isPSRAMAvailable":	1,
	"freeHeap":	8166224,
	"freeHeapInternal":	104127,
	"freeHeapSpiram":	8094068,
	"coreVoltage":	1250,
	"coreVoltageActual":	1246,
	"frequency":	625,
	"ssid":	"RightOnTarget",
	"macAddr":	"E4:B0:63:86:69:F8",
	"hostname":	"bitaxe_69F9",
	"ipv4":	"192.168.12.184",
	"ipv6":	"FD6D:FD25:2174:0:E6B0:63FF:FE86:69F8",
	"wifiStatus":	"Connected!",
	"wifiRSSI":	-52,
	"apEnabled":	0,
	"sharesAccepted":	19,
	"sharesRejected":	0,
	"sharesRejectedReasons":	[],
	"uptimeSeconds":	303,
	"smallCoreCount":	2040,
	"ASICModel":	"BM1370",
	"stratumURL":	"public-pool.io",
	"stratumPort":	21496,
	"stratumUser":	"bc1qsyz6ehyjqzfs478un8vyks9l3mfwn26alqh6fs.bitaxe",
	"stratumSuggestedDifficulty":	1000,
	"stratumExtranonceSubscribe":	0,
	"fallbackStratumURL":	"solo.ckpool.org",
	"fallbackStratumPort":	3333,
	"fallbackStratumUser":	"bc1qsyz6ehyjqzfs478un8vyks9l3mfwn26alqh6fs.bitaxe",
	"fallbackStratumSuggestedDifficulty":	1000,
	"fallbackStratumExtranonceSubscribe":	0,
	"responseTime":	134.091,
	"version":	"v2.12.2",
	"axeOSVersion":	"v2.12.2",
	"idfVersion":	"v5.5.1",
	"boardVersion":	"601",
	"resetReason":	"Software reset via esp_restart",
	"runningPartition":	"ota_0",
	"overheat_mode":	0,
	"overclockEnabled":	0,
	"display":	"SSD1306 (128x32)",
	"rotation":	0,
	"invertscreen":	0,
	"displayTimeout":	1,
	"autofanspeed":	1,
	"fanspeed":	35.3848763,
	"manualFanSpeed":	55,
	"minFanSpeed":	25,
	"temptarget":	60,
	"fanrpm":	3859,
	"fan2rpm":	0,
	"statsFrequency":	60,
	"blockFound":	0,
	"blockHeight":	931558,
	"scriptsig":	"Public-Pool",
	"networkDifficulty":	146472570619930,
	"hashrateMonitor":	{
		"asics":	[{
				"total":	1263.5794678,
				"domains":	[329.8535156, 305.8016663, 322.9815369, 305.8016663],
				"errorCount":	1281
			}]
	}
}
```

### 0xf0xx0 on 2026-01-09

yea, the rename occured after v2.12.2, see commit 50bebdc6 (https://github.com/bitaxeorg/ESP-Miner/commit/50bebdc6d557df499e1aa40df107b1ed8de7d68a#diff-b92a1982bb82df47ec29d7c8b425023f334ec820176646b59970905c61ebc5e40

### adamdecaf on 2026-01-09

Alright thanks. I believe https://github.com/bitaxeorg/ESP-Miner/pull/1495 is the only outstanding discrepancy I see.
