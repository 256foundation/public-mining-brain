# bitaxeorg/ESP-Miner issue #303: Add MQTT Support

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/303
> Collected: 2026-10-07
> Published: 2024-08-20

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 303
- State: closed
- Author: ffrediani
- Opened: 2024-08-20
- Closed: 2024-10-10
- Labels: none

## Description

MQTT is a pretty versatile, lightweight and simple protocol which allows data export to platforms in order to improve monitoring, specially where there are a reasonable number of devices in order to identify faults or improve efficiency.

MQTT code is well developed for ESP32 and doesn't increase much the binary size or consumes any significant resources in terms of CPU and Memory. Tasmota firmware uses it widely for both ESP8266 and ESP32.

A few new lines in settings would be enough such as: Destination Host, ClientID, Username, Password and Topic.

References: https://tasmota.github.io/docs/MQTT/

## Comments

### skot on 2024-08-20

This is an interesting idea. We could maybe expand the monitoring/control options while not increasing the HTTP overhead?

Of course we'd need to figure out how to interface with this. Can web apps talk MQTT directly?

### ffrediani on 2024-08-20

Hi skot
Adding MQQT support doesn't have any reasons to increase anything in terms of HTTP overhead. MQTT is a separate protocol with readily available code for ESP32 and as lightweight will only consume a little extra resources if used, but should not increase HTTP overhead. As a separate protocol apps talk to MQTT directly.

### Webranger2 on 2024-08-29

That would be a cool idea. This way you could get information in the vis from the iobroker or homeassist.

### pixeldoc2000 on 2024-09-03

@Webranger2 
FYI, Home Assistant Integration is already possible via [hass-miner](https://github.com/Schnitzel/hass-miner) Integration (using [pyasic](https://github.com/UpstreamData/pyasic)).

MQTT Support +1

### ffrediani on 2024-10-10

@skot what happened ? Is it because nobody volunteered so far or you think that is not useful ?

### skot on 2024-10-10

I'm not sure I see the benefit considering we already have a full-featured HTTP API (which we need for AxeOS)

### ffrediani on 2024-10-10

For using HTTP API monitoring systems have to do some minimal work to adapt and consume that information from the device and aggregate it. MQTT is a very simple and well stabilized protocol that is easier to get and aggregate data from multiple devices and get alerted in near real time for events with very little CPU cost and complexity.
Fine. Perhaps someone can catch up this, implement and submit a pull request at some point.

### MadNBG on 2024-10-23

mqtt would be nice. Library for ESP is easy, the dashbords Infos sent in a jason would be enough. Maybe Errors, too..
Edit:  blocking may be an issue If the mqtt-server ist offline

### krecik on 2025-03-21

If there is an API, same JSON could be publish as a MQTT message, so no need to change this.
MQTT sounds good - easier integration with ex. HomeAssistant

hass-miner and pyasic doesnt provide all information from API.
