# bitaxeorg/ESP-Miner issue #169: API System Info JSON does return similar / duplicate key "fanSpeed" and "fanspeed" / Powershell DuplicateKeysInJsonString Error

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/169
> Collected: 2026-10-07
> Published: 2024-04-25

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 169
- State: closed
- Author: pixeldoc2000
- Opened: 2024-04-25
- Closed: 2024-04-27
- Labels: bug, good first issue

## Description

If one query the System Info via API it will return "fanSpeed" and "fanspeed".

Powershell can't parse the JSON, because it handels the returned JSON key as case-insensitive. Powershell will treat "fanSpeed" and "fanspeed" as a dupicate Key in the returned JSON Data.

# Example JSON Data from API
```json
{
	"power":	2.7899999618530273,
	"voltage":	5280,
	"current":	530,
	"fanSpeed":	5320,
	"temp":	48,
	"hashRate":	0,
	"bestDiff":	"13M",
	"freeHeap":	182012,
	"coreVoltage":	1250,
	"coreVoltageActual":	1306,
	"frequency":	575,
	"ssid":	"XXX",
	"wifiStatus":	"Connected!",
	"sharesAccepted":	2,
	"sharesRejected":	0,
	"uptimeSeconds":	13,
	"ASICModel":	"BM1366",
	"stratumURL":	"sha256-eu.unmineable.com",
	"stratumPort":	3333,
	"stratumUser":	"BTC:bc1xxxxx.bitaxe01#kc3w-drzs",
	"version":	"v2.1.3",
	"boardVersion":	"0.11",
	"runningPartition":	"ota_1",
	"flipscreen":	1,
	"invertscreen":	0,
	"invertfanpolarity":	1,
	"autofanspeed":	1,
	"fanspeed":	100
}
```

# Example Powershell API Query
```powershell
$targetip = "192.168.0.239"

# Get JSON Data from API
$WebResponse = Invoke-WebRequest -Uri "http://$($targetip)/api/system/info"

# Convert JSON to PowerShell object
$WebObject = ConvertFrom-Json $WebResponse.content
```
# Powershell Error Message
```
ConvertFrom-Json : Die JSON-Zeichenfolge kann nicht konvertiert werden, weil ein aus der Zeichenfolge 
konvertiertes Wörterbuch die doppelten Schlüssel "fanSpeed" und "fanspeed" enthält.
In Zeile:14 Zeichen:14
+ $WebObject = ConvertFrom-Json $WebResponse.content
+              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (:) [ConvertFrom-Json], InvalidOperationException
    + FullyQualifiedErrorId : DuplicateKeysInJsonString,Microsoft.PowerShell.Commands.ConvertFromJsonCommand
```
Error: DuplicateKeysInJsonString "fanSpeed" and "fanspeed" in JSON Data the API returns.

# Suggested Fix
- Maybe change `fanSpeed` to `fanSpeedRpm` for example
