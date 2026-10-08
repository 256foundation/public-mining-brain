# bitaxeorg/ESP-Miner issue #262: Bitaxe httpd crashes

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/262
> Collected: 2026-10-07
> Published: 2024-07-29

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 262
- State: closed
- Author: IO-igiannako
- Opened: 2024-07-29
- Closed: 2024-08-14
- Labels: none

## Description

**Describe the bug**
After a couple of days (2-3 max) the Bitaxe http server stops responding to http requests. I can't access the web interface and therefore no further information on Bitaxe condition, change settings, check logs, etc. I bought it a week ago and this is the third time in a row it crashes. Bitaxe reponds to ping but doesn't serve http at all. Unfortunately, only hardware restart solves the issue.

**To Reproduce**
N/A, http interface is unavailable after 48-72 hours of uptime. Some performance statistics are available via ckpool worker only (all the screenshots attached taken at the same time).

**Expected behavior**
Theoretically, I expect the web server to constantly serve content, dashboard, settings, logs etc

**Screenshots & Photos**
<img width="1561" alt="image" src="https://github.com/user-attachments/assets/478f3849-b284-49c6-8348-6d6b4fbf5cda">
<img width="1561" alt="image" src="https://github.com/user-attachments/assets/432a585c-dc63-4f95-b219-bcbaccc95b40">
<img width="1557" alt="image" src="https://github.com/user-attachments/assets/6a3a8c9e-8f69-4f31-8a83-c1f4ffe8b71b">

**Hardware (please complete the following information):**
 - Bitaxe HW version: Ultra 204
 - Bitaxe HW vendor: Bitronics, Spain
 - ESP-Miner FW version: 2.1.8
 - Hash Frequency: ~450 daily average
 - Voltage: 5 (default)
 - Pool URL, Port, User: solo.ckpool.org, 3333, bc1qhsp5y8evd2d4s0axezqn45sqpenm7vzvnzk4tv.Bitaxe

**Additional context**
Add any other context about the problem here.


## Comments

### MyOwn2C on 2024-07-29

I had similar issue. After adding heatsinks to ESP32 the webpage is now always available 

### IO-igiannako on 2024-07-30

Easy, I'll try that. Cheers

### benjamin-wilson on 2024-07-30

What type of wireless router do you have?

### IO-igiannako on 2024-07-30

The default one the local internet provider offers. It's the Sercomm SHG3060 or Vodafone Power Station WiFi6, as it's branded. I'm not quite sure of the question to be honest, I find it to be a decent WiFi 6 router, quite stable. I'm on the 2.4 band, statistics are stable as well, the ping with ckpool is not excellent but good enough (120-160ms) and I have only 1 share rejected out of 1000 on average, meaning ~0,1%. 

Let me know if there's something more specific, happy to share with you.

### IO-igiannako on 2024-07-31

I installed a heatsink to ESP32 and now seems to be stable. Thanks @19201003080114 

### kakawlala on 2024-08-08

Replacing esp32 still doesn't work.
I am placing metal clips
![Screenshot_20240803-201614_Chrome_1](https://github.com/user-attachments/assets/f17b3b20-2e74-4aab-89a6-532b9ccd7ae1)
![Screenshot_20240803-201720_Chrome_1](https://github.com/user-attachments/assets/3ef07b7d-c854-4709-b4ee-5c8304b4396a)
![P_20240805_180122_1](https://github.com/user-attachments/assets/9c858e23-7584-4413-a131-0fdff3c4951b)



### skot on 2024-08-10

there are some memory leak fixes in https://github.com/skot/ESP-Miner/tree/219-leak_hunting that might fix this. can you give it a try?

[esp-miner.bin.zip](https://github.com/user-attachments/files/16568480/esp-miner.bin.zip)
