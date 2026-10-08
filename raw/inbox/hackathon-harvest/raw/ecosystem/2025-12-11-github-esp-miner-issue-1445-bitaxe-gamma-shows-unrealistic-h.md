# bitaxeorg/ESP-Miner issue #1445: Bitaxe Gamma shows unrealistic high hashrate

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1445
> Collected: 2026-10-07
> Published: 2025-12-11

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1445
- State: open
- Author: Beebop-Luffy
- Opened: 2025-12-11
- Closed: n/a
- Labels: bug

## Description

Note: Issues are not for customer support, configuration or discussion. For those topics please consult with your HW vendor or the OSMU Discord at: https://osmu.bitaxe.org

**Describe the bug**
My Bitaxe shows sometimes around 200 TH/s - after a couple restart it turns back to normal again
Anyone else experiencing this?



**Screenshots & Photos**

<img width="338" height="229" alt="Image" src="https://github.com/user-attachments/assets/b9298a8b-f4a6-487e-8e34-5c9a223e558e" />

**Hardware (please complete the following information):**
 - Bitaxe HW version: Bitaxe Gamma 601
 - Bitaxe HW vendor: Solosatoshi
 - ESP-Miner FW version:
 - Hash Frequency: 636
 - Voltage: 1125
 


## Comments

### mutatrum on 2025-12-12

Did you also update `www.bin`? An update needs both files. And make sure to do a full page refresh after the update.

### AxeMiner on 2025-12-16

I have the same issue with my Bitaxe Gamma 601. With the version v2.10.1 hashrate is shown ok. With the upgrade to the 2.11 or 2.12 version hashrate is wrong. Sometimes it show correct data but mostly it shows random high numbers.
I tried to flash the factory versions even update the www.bin and esp-miner.bin manually but the result is the same. I had to downgrade back to v2.10.1.
The invalid hashrate is also showing on the display. So the problem is with the esp-miner.bin
I have noticed that one value from hash register is reading invalid data.

<img width="917" height="120" alt="Image" src="https://github.com/user-attachments/assets/9a6a1719-e080-49b6-9e1b-bb64583ea703" />
<img width="400" height="173" alt="Image" src="https://github.com/user-attachments/assets/513a1f49-e254-4d24-bcbb-1da0ebfd38dd" />
<img width="308" height="187" alt="Image" src="https://github.com/user-attachments/assets/06a1a8ae-e5eb-49d4-ba42-01fc8d894c36" />

### mutatrum on 2025-12-16

I've never seen this before. Did the domain continue to show these high values? It looks like it's just 3 orders off, but that's really weird as each domain is handled the same. Does this also happen on stock frequency and voltage?

### AxeMiner on 2025-12-16

The domain continue to show these high numbers. When i check the /api/system/info endpoint it is every time the 3 domain. Others show the data ok. It looks like some kind of overflow. It happens with the stock frequency and voltage (525/1150). I tried to change these values as well, but the result is the same. Is there something that i can provide to help you investigate the issue?

### mutatrum on 2025-12-16

@Beebop-Luffy is this the same for you, that a single domain hashrate is off?

Two more questions:
 * What hashrate does the pool report?
 * Can you capture the logs during boot and post these here?

### LSgeo on 2026-01-22

I have the same issue. I think it's a power issue with low input voltage - undervolting the asic helps. Even still, during the day when it's hot, I will get 2 domains blacked out at 0 GH/s, two show high errors, and eventually a power fault. 

I have a custom DC PSU from solar power.
Purchased from AliExpress, "Bitsoloplayer Official Store".

```
Device Model | Gamma
Board Version | 601
ASIC Type | BM1370
Uptime | 7 minutes, 3 seconds
Wi-Fi Status | Connected!
Wi-Fi RSSI | -91 dBm
Free Heap Memory | 8.17 MB
• Internal | 104 kB
• Spiram | 8.10 MB
Firmware Version | v2.11.0
AxeOS Version | v2.11.0
ESP-IDF Version | v5.5.1
```

I can find the boot logs/ etc if it helps too.

I'm going to bandaid it with a hashrate watchdog that triggers a restart, using `/api/system/restart`
