# bitaxeorg/ESP-Miner issue #1174: Feature request: Show active ASIC count, task distribution, and per-unit error reporting

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1174
> Collected: 2026-10-07
> Published: 2025-07-29

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1174
- State: closed
- Author: janix12
- Opened: 2025-07-29
- Closed: 2025-08-21
- Labels: none

## Description

Hi,

I’d like to suggest a feature enhancement for the ESP-based miner software.

I am using a NerdQaxe++ device.

🧩 Feature idea:
Display the number of active ASIC units in real-time.
This could be shown either on the main dashboard or on a separate diagnostics/status page.

🔍 Why it matters:
When running multiple ASICs (e.g. 5 units), it's important to see how the mining load is distributed across them — ideally showing a per-ASIC task share, e.g. in 20% steps.

This would help in performance monitoring and early detection of hardware degradation or load imbalance.

⚠️ Bonus suggestion:
If an ASIC unit becomes unresponsive or encounters an error, the software could indicate which specific unit is faulty.
This would be extremely useful for troubleshooting and reducing downtime.

Let me know if I can help with testing or provide logs.

Thanks for the great work!

## Comments

### skot on 2025-07-29

I agree these would be great features! Just fyi, this is not the repo for NerdQAxe firmware.

### bonifacio123 on 2025-07-30

janix12, This is the NerdQaxe++ repo

https://github.com/shufps/ESP-Miner-NerdQAxePlus



### WantClue on 2025-08-21

Please move this over to the nerdqaxeplusplus repo, this issue will be closed here.
Thank you
