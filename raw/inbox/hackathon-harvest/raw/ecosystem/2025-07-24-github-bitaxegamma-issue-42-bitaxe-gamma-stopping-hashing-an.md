# bitaxeorg/bitaxeGamma issue #42: Bitaxe Gamma Stopping Hashing and Unreachable Web Interface

> Source: https://github.com/bitaxeorg/bitaxeGamma/issues/42
> Collected: 2026-10-07
> Published: 2025-07-24

- Repository: bitaxeorg/bitaxeGamma
- Type: issue
- Number: 42
- State: open
- Author: cedrickoch
- Opened: 2025-07-24
- Closed: n/a
- Labels: none

## Description

Description:
I've been operating a Bitaxe Gamma for a few weeks now and have encountered a recurring issue where it stops hashing every few days, requiring a restart. When the device enters this state, the web interface also becomes unreachable. I've logged the output from the USB interface, which is attached for review.

Observations:
- The initial part of the log shows everything working smoothly.
- In the middle of the log, there are multiple WiFi resets. It's worth noting that the WiFi repeater is positioned right next to the Bitaxe and is stable.
- The final phase in the log indicates when the Bitaxe stops functioning.

Steps to Reproduce:
- Operate the Bitaxe Gamma over several days.
- Observe the hashing process and periodically check accessibility to the web interface.
- Monitor for an eventual halt in operation and loss of web interface access.

Expected Outcome:
- Continuous hashing and accessible web interface without the need for frequent restarts.
- Actual Outcome: Hashing stops intermittently every few days, requiring a restart, and the web interface becomes unavailable during this period.

Attached Log: Please find the USB interface log attached for further investigation.


[debug.log](https://github.com/user-attachments/files/21402074/debug.log)

## Comments

### gihu2023 on 2025-10-12

i´ve a similar problem, but within firewall logs i see that Bitaxe Gamma changed its IP adress to the gateway adress and try to took over also other ip adreses.
Normal setup Bitaxe f4:12:fa:46:28:58  got 192.168.7.114 from DHCP Server, after some time, cant say if its random, it uses the Gateway IP 192.168.7.1 and then wanna overtake 192.168.7.100

<img width="828" height="67" alt="Image" src="https://github.com/user-attachments/assets/ad844f69-6ea8-4142-ac4c-92c524054cde" />
