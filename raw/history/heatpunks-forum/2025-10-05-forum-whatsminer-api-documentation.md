# Whatsminer API Documentation

> Source: https://forum.heatpunks.org/t/whatsminer-api-documentation/202
> Collected: 2026-10-10
> Published: 2025-10-05
> Registry ID: heatpunks-forum

tylerkstevens | 2025-10-05 17:35:15 UTC | #1

All,

Please see the following links for quick access to Whatsminer API documentation from MicroBT.

[https://support.whatsminer.com/en-US/category/28](https://support.whatsminer.com/en-US/category/28)

[whatsminer.com](https://www.whatsminer.com/src/views/firmware-download.html#Document)

### [WhatsMiner](https://www.whatsminer.com/src/views/firmware-download.html#Document)

-------------------------

patrick-patel | 2025-10-05 23:34:44 UTC | #2

Haven’t looked at the whatsminer api docs in a while but they seem to be only slightly easier to digest :sweat_smile:

-------------------------

tylerkstevens | 2025-10-15 13:31:16 UTC | #3

It’s wild how adversarial the pleb relationship is with the OEMs.

-------------------------

Bitckle | 2025-11-23 23:44:01 UTC | #4

Hi. I think I got Home Assistant to work with this M64…

# Whatsminer Home Assistant Setup Guide

This document summarizes the setup of Home Assistant Core with the Whatsminer integration for remote miner control.

## Overview

- Date Setup

  : November 23, 2025

- Home Assistant Version

  : 2025.1.4

- Miner

  : Whatsminer HTM40X (IP: XXX.XXX.X.X)

- Location

  :

  /home/dsthermal/home_assistant/

## Directory Structure

```auto
/home/dsthermal/home_assistant/
├── venv/                          # Python virtual environment
├── config/                        # Home Assistant configuration
│   ├── configuration.yaml         # Main config
│   ├── automations.yaml           # Mining schedule
│   ├── custom_components/         # Symlink to integration
│   └── home-assistant.log         # Log file
├── custom_components/
│   └── whatsminer/                # Whatsminer integration
│       ├── __init__.py
│       ├── api.py                 # API client (with encryption fix)
│       ├── sensor.py
│       ├── switch.py
│       ├── const.py
│       └── manifest.json
├── README.md
├── SETUP_GUIDE.md                 # This file
├── configuration_example.yaml
├── automations_example.yaml
├── install.sh
└── WhatsMiner_API_Manual.pdf

```

## Installation Steps Performed

### 1. Created Python Virtual Environment

```bash
cd /home/dsthermal/home_assistant
/usr/bin/python3 -m venv venv
./venv/bin/pip install --upgrade pip wheel

```

### 2. Installed Home Assistant Core

```bash
./venv/bin/pip install homeassistant pycryptodome numpy

```

### 3. Set Up Configuration Directory

```bash
mkdir -p config
ln -s /home/dsthermal/home_assistant/custom_components config/custom_components

```

### 4. Created Configuration Files

**config/configuration.yaml:**

```yaml
homeassistant:
  name: Home
  unit_system: metric
  time_zone: America/Chicago

frontend:
api:

logger:
  default: info
  logs:
    custom_components.whatsminer: debug

automation: !include automations.yaml

whatsminer:
  - host: "XXX.XXX.X.X"
    name: "Miner 1"
    password: "root"
    port: 4028
    scan_interval: 30

```

## API Encryption Fix

The original Whatsminer API implementation used simple MD5 hashing, but the actual Whatsminer API requires **Unix MD5-crypt** (`$1$` format) for authentication.

### Key Changes to `api.py`:

1. **Password Key Derivation**: Changed from `MD5(salt + password)` to:

  ```python

  pwd_hash = crypt.crypt(password, "$1$" + salt + "$")

  key = pwd_hash.split('$')[3]

  ```

2. **Sign Token Generation**: Uses MD5-crypt with newsalt:

  ```python

  sign_hash = crypt.crypt(key + time_val, "$1$" + newsalt + "$")

  sign = sign_hash.split('$')[3]

  ```

3. **AES Key**: SHA256 hash of the key, converted to bytes:

  ```python

  aes_key = binascii.unhexlify(hashlib.sha256(key.encode()).hexdigest())

  ```

4. **Command Format**: Token goes inside the JSON command before encryption:

  ```python

  command = {"cmd": "power_off", "token": sign}

  ```

## Miner Configuration Required

**Important**: The Whatsminer API write access must be enabled on the miner itself.

1. Open Whatsminer Tool or miner web interface

2. Enable API access / Remote Control

3. Ensure write permissions are enabled (not read-only)

Without this, commands return: `"can't access write cmd"` (Code 45)

## Mining Schedule

**Current Schedule** (in `config/automations.yaml`):

| Day | Pause | Resume |
|---|---|---|
| Monday-Friday | 8:00 AM | 1:00 PM |
| Saturday-Sunday | No pause | Runs 24/7 |

**Holiday Exceptions** (miner runs all day):

- November 27-28, 2025 (Thanksgiving)

- December 24-25, 2025 (Christmas)

**Schedule End Date**: May 31, 2026

## Starting Home Assistant

### Start Command

```bash
cd /home/dsthermal/home_assistant
./venv/bin/hass -c ./config &

```

### Stop Command

```bash
pkill -f "hass -c ./config"

```

### Check Status

```bash
ps aux | grep hass
tail -f ./config/home-assistant.log

```

## Accessing Home Assistant

- Local

  :

  http://localhost:8123

- Network

  :

  http://XXX.XXX.X.X:8123

## Entities Created

### Sensors (7 per miner)

- sensor.miner_1_power

  - Power consumption (W)

- sensor.miner_1_hashrate

  - Hash rate (MH/s)

- sensor.miner_1_temperature_env

  - Environmental temp (°C)

- sensor.miner_1_temperature_chip_avg

  - Avg chip temp (°C)

- sensor.miner_1_temperature_chip_max

  - Max chip temp (°C)

- sensor.miner_1_fan_speed_in

  - Inlet fan (RPM)

- sensor.miner_1_fan_speed_out

  - Outlet fan (RPM)

### Switch (1 per miner)

- switch.miner_1_mining

  - Toggle mining on/off

## Troubleshooting

### “can’t access write cmd” Error

- Enable API write access on the miner via Whatsminer Tool

### “enc json load err” Error

- Encryption format is wrong - ensure api.py uses MD5-crypt

### Miner not responding

- Check network connectivity:

  ping XXX.XXX.X.X

- Verify port 4028 is open:

  nc -zv XXX.XXX.X.X 4028

### Automation not triggering

- Check timezone in configuration.yaml

- Verify automation conditions in Developer Tools

- Check logs:

  grep automation ./config/home-assistant.log

## Dependencies

- Python 3.12+

- homeassistant

- pycryptodome (AES encryption)

- numpy

- crypt (built-in, deprecated in Python 3.13)

-------------------------

Cardiac | 2025-12-13 12:23:36 UTC | #5

Are y’all familiar with [pyasic/pyasic/miners/whatsminer/btminer at master · UpstreamData/pyasic · GitHub](https://github.com/UpstreamData/pyasic/tree/master/pyasic/miners/whatsminer/btminer)?
