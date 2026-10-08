# bitaxeorg/ESP-Miner issue #1206: VS Code + Espressif IDF extension 1.10.1 (ESP-IDF 5.5) or newer is using esptool dev versions (esptool v4.10.dev1 or esptool v4.10.dev2).

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1206
> Collected: 2026-10-07
> Published: 2025-08-24

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1206
- State: closed
- Author: ghost
- Opened: 2025-08-24
- Closed: 2025-09-21
- Labels: none

## Description

Just putting this out there for Windows users that use VS Code + Espressif IDF extension 1.10.1 / 1.10.2 (ESP-IDF v5.5) or newer as I was having build issues (slow or PC would lock up) with esptool v4.10.dev1 or v4.10.dev2.
https://github.com/bitaxeorg/ESP-Miner/pull/1201

Maintainers need to pay attention here as well with this (workflows are using esptool v4.9.0 and esptool v5.0.2). 

<img width="1461" height="326" alt="Image" src="https://github.com/user-attachments/assets/6901b1df-a7dc-46e1-b63f-48ce7a912646" />

<img width="1360" height="957" alt="Image" src="https://github.com/user-attachments/assets/8e57e3f8-208b-453e-ac61-4ea81365bf1e" />

<img width="902" height="470" alt="Image" src="https://github.com/user-attachments/assets/39d0f9a6-f4db-4734-9129-2b51bdf39bd6" />

If you want / need to revert to using esptool v4.9.0 within VS Code ESP-IDF (v5.5) Terminal

**pip install esptool==4.9.0**

Then edit "**espidf.constraints.v5.5.txt**", look for

**esptool~=4.10.dev1**  or   **esptool~=4.10.dev2**

Change it to

**esptool~=4.9.0**

Save the file and restart VS Code.

<img width="1291" height="570" alt="Image" src="https://github.com/user-attachments/assets/eb47792c-d8f1-4d99-bbaa-6050f778cddb" />

esptool v5.x.x (the tools) have breaking changes (not sure what's changed with these v4.10.dev versions), this is why I have reverted to using esptool v4.9.0 within VS Code (windows system) so that there are no chances of any breaking changes with these "dev versions" of esptool 4.10.dev"x" or with esptool v5.x.x (not ESP-IDF v5.5).

esptool v5.x.x and it's breaking changes, these should be checked to make sure these will not cause issues when building the firmware (any stage of it).

https://docs.espressif.com/projects/esptool/en/latest/esp32s3/migration-guide.html

These breaking changes do cause the BitaxeTool to fail with flashing any device and has been updated to use esptool v4.9.0 only.
https://github.com/bitaxeorg/ESP-Miner/issues/1184#issuecomment-3192235430



## Comments

### ghost on 2025-08-25

Adding this here for extra info for those that use Windows 10/11
VS Code with ESP-IDF extension version 1.10.1 or 1.10.2 (ESP-IDF v5.5) installed.

espidf.constraints.v5.5.txt  (it's amended content - esptool~=4.9.0)

```# --------- CORE ----------

# setuptools: version 21 is required to handle PEP 508 environment markers
# 71.0.1 introduced bug https://github.com/pypa/setuptools/issues/4480
setuptools>=21,<71.0.1

# click: Min. version was set to support the API used in idf.py and auto-completion
click>=7.0,<8.2

# pyserial: Min. version was set to support the used API
pyserial>=3.3

# cryptography: Min. version was set to support all functionality of ESP-IDF
# Only binary for cryptography is here to make it work on ARMv7 architecture
# We do have cryptography binary on https://dl.espressif.com/pypi for ARM
# On https://pypi.org/ are no ARM binaries as standard now
cryptography>=2.1.4,<45
--only-binary cryptography

# pyparsing: Min version was set based on https://github.com/pyparsing/pyparsing/issues/482
pyparsing>=3.1.0,<4

# pyelftools

idf-component-manager~=2.1
urllib3<2

esptool~=4.9.0

esp-coredump~=1.10

# esp-idf-kconfig: Config name was extended from 40 to 50 chars since 2.0.2 version
esp-idf-kconfig>=2.0.2,<3.0.0

freertos_gdb~=1.0

esp-idf-monitor>=1.6.2,<2

# 1.4.0 contains support for empty output sections in linker's map file
esp-idf-size>=1.4.0

esp-idf-nvs-partition-gen~=0.1.9

# --------- CORE ends ----------

# --------- GDBGUI -------------

gdbgui==0.13.2.0; python_version < "3.11" and sys_platform == 'win32'
# Windows is not supported since 0.14.0.0. See https://github.com/cs01/gdbgui/issues/348
# pygdmi dependency is shared between gdbgui, coredump and py_debug_backend
# pygdbmi 0.10 have breaking changes
# The pygdbmi required max version 0.9.0.2 since 0.9.0.3 is not compatible with latest gdbgui (>=0.13.2.0)
pygdbmi<=0.9.0.2; python_version < "3.11" and sys_platform == 'win32'
# A compatible Socket.IO should be used. See https://github.com/miguelgrinberg/python-socketio/issues/578
python-socketio<5; python_version < "3.11" and sys_platform == 'win32'
jinja2<3.1; python_version < "3.11" and sys_platform == 'win32'
itsdangerous<2.1; python_version < "3.11" and sys_platform == 'win32'

gdbgui>=0.15.2.0; python_version >= "3.11"

# --------- GDBGUI ends ---------

# --------- CI ---------
idf-build-apps~=2.0
# https://github.com/minio/minio-py/issues/1382
minio!=7.2.1

# --------- CI ends ---------

# --------- PYTEST -------------

pytest-embedded-serial-esp~=1.0
pytest-embedded-idf~=1.0
pytest-embedded-qemu~=1.0

# 1.3.2 is not supported in 3.11. See https://gitlab.freedesktop.org/dbus/dbus-python/-/issues/45
dbus-python<1.3; python_version > "3.10"

# paho mqtt 2.0
# https://github.com/eclipse/paho.mqtt.python/blob/master/ChangeLog.txt#L1
# got a few breaking changes
paho-mqtt<2

# IDFCI-2426
# https://github.com/secdev/scapy/issues/4512
scapy<2.6

# --------- PYTEST ends ---------

# --------- DOCS -------------

esp-docs~=2.1.0
linuxdoc==20210324

# --------- DOCS ends ---------

# --------- esp_prov -------------

# https://github.com/protocolbuffers/protobuf/issues/10075
protobuf<=3.20.1

# --------- esp_prov ends ---------
```
Firmware builds properly without issues now that I've reverted to using esptool v4.9.0 with ESP-IDF extension version 1.10.1 or 1.10.2 (ESP-IDF v5.5.0)
** **
<img width="1414" height="878" alt="Image" src="https://github.com/user-attachments/assets/f4ae71a9-bc75-45cf-b6c1-12842e63d746" />

** **

<img width="2699" height="1967" alt="Image" src="https://github.com/user-attachments/assets/dd3c02ec-0928-4892-b450-89e41ce5536e" />


### ghost on 2025-09-21

The build issue caused by esptool v4.10.dev2 is now resolved for me by the official release of esptool v4.10.0. It seems the problem was related to the pre-release version (dev version) of the tool. I will close this issue as resolved. Thank you
