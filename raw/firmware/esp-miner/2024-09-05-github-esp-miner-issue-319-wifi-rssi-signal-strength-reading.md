# bitaxeorg/ESP-Miner issue #319: WiFi RSSI signal strength reading/indicator

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/319
> Collected: 2026-10-07
> Published: 2024-09-05

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 319
- State: closed
- Author: CryptoIceMLH
- Opened: 2024-09-05
- Closed: 2025-03-26
- Labels: enhancement, good first issue, accepted

## Description


I Think it would be very useful both for support issues but also for user monitoring 
to modify the code to export the ESP32 wifi modules RSSI ( also known as the wifi signal strength )

The RSSI (Received Signal Strength Indicator) can be checked by the ESP32 to determine the WiFi connection strength between the ESP32 and the specific WiFi network you’re trying to connect to (e.g. home router or any access point). This can be useful in case you’re having some issues with the WiFi connection or keeps disconnecting sporadically or for some upcoming applications to monitor the max distance usable for a bitaxe away from the Access point. 
You can then check the RSSI for the network and judge if the WiFi signal power needs adjusting or if you simply need to place the ESP32 closer to the access point.

Generally speaking, the lower the RSSI value, the weaker the signal is, and vice versa. The range for RSSI value is from 0 down to -120 dBm. Having a 0 dBm is hard to achieve and it means you’ve got an amazingly strong connection. And low values from -90 down to -120 dBm are unusable at all
RSSI is an estimated measure of the WiFi signal strength for a specific network (router or access point). The return value has the following form and unit (-x dBm). Which means a lower absolute value indicates a more powerful connection. 

RSSI > -30 dBm | Amazing
RSSI < – 55 dBm | Very good signal
RSSI < – 67 dBm | Fairly Good
RSSI < – 70 dBm | Okay
RSSI < – 80 dBm | Not good
RSSI < – 90 dBm | Extremely weak signal (unusable)


WiFi.RSSI();  

ref doc: [ https://www.arduino.cc/reference/en/libraries/wifi/wifi.rssi/](url)

## Comments

### CryptoIceMLH on 2025-02-23

Nudging this again as a non urgent reminder ! 

### skot on 2025-02-23

I agree, exposing the current RSSI to AxeOS would be really helpful.

Maybe even show it in the new SSID chooser @WantClue ?

### WantClue on 2025-03-26

The RSSI has been added to the API endpoint

### CryptoIceMLH on 2025-03-29

thanks
