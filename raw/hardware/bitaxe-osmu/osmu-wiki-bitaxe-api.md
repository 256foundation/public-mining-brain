# Bitaxe API Endpoints

> Source: https://osmu.wiki/bitaxe/api/
> Collected: 2026-10-07
> Published: Unknown

# Bitaxe API Endpoints

The Bitaxe features the following endpoints:

**GET**

- `/api/system/info` Get system information
- `/api/system/asic` Get ASIC settings information
- `/api/system/statistics` Get system statistics (data logging should be activated)
- `/api/system/statistics/dashboard` Get system statistics for dashboard
- `/api/system/wifi/scan` Scan for available WiFi networks

**POST**

- `/api/system/restart` Restart the system
- `/api/system/identify` Identify the device
- `/api/system/OTA` Update system firmware
- `/api/system/OTAWWW` Update AxeOS

**PATCH**

- `/api/system` Update system settings

### Examples

[Section titled “Examples”](https://osmu.wiki#examples)

**GET**

Get system information:

Get ASIC settings information:

Get system statistics (data logging should be activated):

You can filter statistics by specific columns using the `columns` query parameter:

Get dashboard statistics:

Get available WiFi networks:

**POST**

Restart the system:

Identify the device (let it say Hi!):

Update system firmware:

Update AxeOS web interface:

**PATCH**

The PATCH functionality allows you to change settings on the Bitaxe. Some settings may require a restart, but many can be changed on-the-fly.

Change fan speed (when autofanspeed is disabled):

Enable automatic fan speed control:

Set target temperature for automatic fan control:

Update ASIC frequency (requires overclock enabled):

Update ASIC core voltage (requires overclock enabled):

Update stratum pool settings:

Update WiFi settings:

Multiple settings can be updated in a single request:

### Available Settings

[Section titled “Available Settings”](https://osmu.wiki#available-settings)

The following settings can be updated via PATCH requests to `/api/system`:

**Pool Configuration:**

- `stratumURL` - Primary stratum server URL (e.g., “stratum+tcp://pool.example.com”)
- `stratumPort` - Primary stratum server port (1-65535)
- `stratumUser` - Username for primary stratum server
- `stratumPassword` - Password for primary stratum server
- `fallbackStratumURL` - Fallback stratum server URL
- `fallbackStratumPort` - Fallback stratum server port (1-65535)
- `fallbackStratumUser` - Username for fallback stratum server
- `fallbackStratumPassword` - Password for fallback stratum server
- `useFallbackStratum` - Force use of fallback stratum pool

**WiFi Configuration:**

- `ssid` - WiFi network SSID (1-32 characters)
- `wifiPass` - WiFi network password (8-63 characters)
- `hostname` - Device hostname (alphanumeric and hyphens only)

**ASIC Configuration:**

- `coreVoltage` - ASIC core voltage in millivolts (requires `overclockEnabled: 1`)
- `frequency` - ASIC frequency in MHz (requires `overclockEnabled: 1`)
- `overclockEnabled` - Enable custom voltage/frequency (0=disabled, 1=enabled)

**Fan Control:**

- `autofanspeed` - Automatic fan speed control (0=manual, 1=auto)
- `fanspeed` - Manual fan speed percentage when autofanspeed is disabled (0-100)
- `temptarget` - Target temperature in °C for automatic fan control (0-100)

**Display Settings:**

- `rotation` - Screen rotation (0, 90, 180, 270 degrees)
- `invertscreen` - Invert screen colors (0=normal, 1=inverted)
- `displayTimeout` - Display timeout in minutes (-1=always on, 0=always off, >0=timeout)

**Advanced Settings:**

- `overheat_mode` - Overheat protection mode (0=disabled)
- `statsFrequency` - Statistics logging frequency in seconds (0=disabled)

### Response Formats

[Section titled “Response Formats”](https://osmu.wiki#response-formats)

The complete API specification with all response schemas is available in [openapi.yaml](https://github.com/bitaxeorg/ESP-Miner/blob/master/main/http_server/openapi.yaml).

#### `/api/system/info` Response

[Section titled “/api/system/info Response”](https://osmu.wiki#apisysteminfo-response)

General information about the Bitaxe can be collected using `/api/system/info`, which provides the following data:

#### `/api/system/asic` Response

[Section titled “/api/system/asic Response”](https://osmu.wiki#apisystemasic-response)

ASIC settings information can be retrieved using `/api/system/asic`, which returns:

**ASIC Models:**

- `BM1366` - Used in Bitaxe Ultra
- `BM1368` - Used in Bitaxe Supra
- `BM1370` - Used in Bitaxe Gamma
- `BM1397` - Used in Bitaxe (original)

#### `/api/system/wifi/scan` Response

[Section titled “/api/system/wifi/scan Response”](https://osmu.wiki#apisystemwifiscan-response)

WiFi network scan results can be retrieved using `/api/system/wifi/scan`:

**Authentication Modes:**

- `0` - OPEN (no security)
- `1` - WEP
- `2` - WPA\_PSK
- `3` - WPA2\_PSK
- `4` - WPA\_WPA2\_PSK
- `5` - WPA2\_ENTERPRISE
- `6` - WPA3\_PSK
- `7` - WPA2\_WPA3\_PSK
- `8` - WAPI\_PSK
- `9` - OWE (Opportunistic Wireless Encryption)
- `10` - WPA3\_ENT\_192 (Enterprise Suite-B)

**RSSI Values:**

- `-30 dBm` - Excellent signal
- `-50 dBm` - Very good signal
- `-60 dBm` - Good signal
- `-67 dBm` - Fair signal
- `-70 dBm` - Weak signal
- `-80 dBm` - Very weak signal
- `-90 dBm` - Unusable signal

#### `/api/system/statistics` Response

[Section titled “/api/system/statistics Response”](https://osmu.wiki#apisystemstatistics-response)

System statistics can be retrieved using `/api/system/statistics`. This endpoint supports filtering by specific columns using the `columns` query parameter.

Available columns include:

- `hashrate`, `hashrate_1m`, `hashrate_10m`, `hashrate_1h` - Hashrate measurements
- `asicTemp`, `vrTemp` - Temperature readings
- `asicVoltage`, `voltage` - Voltage measurements
- `power`, `current` - Power consumption metrics
- `fanSpeed`, `fanRpm`, `fan2Rpm` - Fan speed information
- `wifiRssi` - WiFi signal strength
- `freeHeap` - Available memory
- `responseTime` - Pool response time

Response format:

### HTTP Status Codes

[Section titled “HTTP Status Codes”](https://osmu.wiki#http-status-codes)

The API returns standard HTTP status codes:

- `200 OK` - Request successful
- `400 Bad Request` - Invalid request parameters or settings
- `401 Unauthorized` - Client not in allowed network range
- `500 Internal Server Error` - Server error occurred

- All API endpoints return JSON responses except for OTA update endpoints
- The `/api/system/statistics` endpoint requires data logging to be enabled (`statsFrequency` > 0)
- Some settings changes via PATCH may require a system restart to take effect
- WiFi and stratum password fields are write-only and will not be returned in GET responses
- Temperature values are returned in Celsius
- Voltage values are typically in millivolts for ASIC settings
- Power values are in watts
- Hashrate values are in GH/s (Gigahashes per second)
