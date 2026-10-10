# bitaxeorg/ESP-Miner issue #738: Integer Division by Zero when chip_counter is 0

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/738
> Collected: 2026-10-07
> Published: 2025-02-24

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 738
- State: closed
- Author: AxisRay
- Opened: 2025-02-24
- Closed: 2025-02-24
- Labels: none

## Description

Note: Issues are not for customer support, configuration or discussion. For those topics please consult with your HW vendor or the OSMU Discord at: https://osmu.bitaxe.org

**Describe the bug**
When ASIC is poorly soldered or not properly connected, `chip_counter` becomes 0 in `_send_init()`. This leads to an Integer Division by Zero error.
https://github.com/skot/ESP-Miner/blob/b92f70d8716b25700af0058d600305ce1850f27c/components/asic/bm1366.c#L264-L266
https://github.com/skot/ESP-Miner/blob/b92f70d8716b25700af0058d600305ce1850f27c/components/asic/bm1370.c#L258-L260

**To Reproduce**
ASIC is poorly soldered or not properly connected

**Expected behavior**
- The code should handle the case when no chips are detected
- Should report error and exit gracefully instead of crashing

**Screenshots & Photos**
If applicable, add AxeOS screenshots and/or photos of your Bitaxe to help explain your problem.
<img width="541" alt="Image" src="https://github.com/user-attachments/assets/38b5b6f6-c9b7-445b-8621-c572c880916c" />

**Hardware (please complete the following information):**
N/A

**Additional context**
This issue typically occurs when:
- ASIC is poorly soldered
- Connection issues between ESP32 and ASIC
- Hardware communication problems


## Comments

### AxisRay on 2025-02-24

Known issues
