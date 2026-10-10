# bitaxeorg/ESP-Miner issue #1119: SupraHex devices identified as GammaHex in Swarm page in v2.9.0

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1119
> Collected: 2026-10-07
> Published: 2025-07-04

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1119
- State: closed
- Author: Hylinus
- Opened: 2025-07-04
- Closed: 2025-07-05
- Labels: none

## Description

**Describe the bug**
SupraHex devices are identified and their IP address colored as a GammaHex device, even though the correct ASIC is listed (BM1368)

**To Reproduce**
Steps to reproduce the behavior:
1. Go to 'Swarm' page
2. At the bottom of list of devices, notice that SupraHex devices are listed as GammaHex

**Expected behavior**
Since the correct ASIC on the multi-chip devices is identified, the name listed should match.

**Screenshots & Photos**
v2.9.0
![Image](https://github.com/user-attachments/assets/ddb30816-3404-476f-8dce-65c169b276cb)
![Image](https://github.com/user-attachments/assets/d1107977-7b18-4d66-b00b-f3b169c538c8)

v2.7.0-TCH-All-In-One
![Image](https://github.com/user-attachments/assets/684c5d2d-d39a-4b0a-8821-006517a72fdf)
![Image](https://github.com/user-attachments/assets/a1160bd4-6c1c-4c02-acee-029120b7e821)

**Hardware (please complete the following information):**
 - Bitaxe HW version: Gamma 602
 - Bitaxe HW vendor: Altair
 - ESP-Miner FW version: v2.9.0

## Comments

### mutatrum on 2025-07-04

Can you call `http://192.168.111.246/api/system/info`  and paste that here? You can leave out bitcoin addresses and such.

### duckaxe on 2025-07-04

@mutatrum Is it possible that the SupraHex definition is missing in `/main/device_config.h`?

### Hylinus on 2025-07-04

I've blanked out some information to protect the innocent. ;-)

{
	"power":	60.368900299072266,
	"voltage":	12062.5,
	"current":	15890.625,
	"temp":	37.5999984741211,
	"vrTemp":	60,
	"maxPower":	145,
	"nominalVoltage":	12,
	"hashRate":	3544.7940677791275,
	"bestDiff":	"193G",
	"bestSessionDiff":	"9.54M",
	"stratumDiff":	131072,
	"isUsingFallbackStratum":	0,
	"isPSRAMAvailable":	1,
	"freeHeap":	8390104,
	"coreVoltage":	1166,
	"coreVoltageActual":	1162,
	"frequency":	490,
	"ssid":	"",
	"macAddr":	"94:A9:90:07:F4:D8",
	"hostname":	"",
	"wifiStatus":	"Connected!",
	"wifiRSSI":	-56,
	"apEnabled":	0,
	"sharesAccepted":	291,
	"sharesRejected":	0,
	"sharesRejectedReasons":	[],
	"uptimeSeconds":	45689,
	"asicCount":	6,
	"smallCoreCount":	1276,
	"ASICModel":	"BM1368",
	"stratumURL":	"192.168.111.130",
	"fallbackStratumURL":	"mine.ocean.xyz",
	"stratumPort":	23334,
	"fallbackStratumPort":	3334,
	"stratumUser":	"",
	"fallbackStratumUser":	"",
	"version":	"2.7.0-TCH-All-In-One",
	"idfVersion":	"v5.4",
	"boardVersion":	"702",
	"runningPartition":	"ota_0",
	"flipscreen":	1,
	"overheat_mode":	0,
	"overclockEnabled":	0,
	"invertscreen":	0,
	"invertfanpolarity":	1,
	"autofanspeed":	1,
	"fanspeed":	38,
	"fanrpm":	2536,
	"chipSubmitStr":	"[25757, 26165, 25975, 26053, 26114, 26037]"
}

### mutatrum on 2025-07-04

Thank you for the info endpoint result. The device model is taken from this, and if it's not available, there is a bit of code in the swarm page that tries to deduce device model based off `boardVersion`. For 7xx board versions, this fallback code has the wrong deviceModel field.

I've opted to remove this for the 7xx boardVersion, as they are outside of these repositories. The cleanest way would be if TCH would add a `deviceModel` field, similar to what Bitaxe and NerdAxe now have, as it will get messy quickly if we have to keep a list of boardVersion to deviceModel from other repositories.

### Hylinus on 2025-07-05

> Thank you for the info endpoint result. The device model is taken from this, and if it's not available, there is a bit of code in the swarm page that tries to deduce device model based off `boardVersion`. For 7xx board versions, this fallback code has the wrong deviceModel field.
> 
> I've opted to remove this for the 7xx boardVersion, as they are outside of these repositories. The cleanest way would be if TCH would add a `deviceModel` field, similar to what Bitaxe and NerdAxe now have, as it will get messy quickly if we have to keep a list of boardVersion to deviceModel from other repositories.

Thank you for the feedback. I will open an issue on TCH's Issues page.

### Hylinus on 2025-07-05

I've opened up a case on the TCH Repo: https://github.com/TinyChipHub/ESP-Miner-TCH/issues/14
