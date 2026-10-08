# bitaxeorg/bitaxeGamma issue #12: Some bitaxeGamma builds are overheating at stock settings.

> Source: https://github.com/bitaxeorg/bitaxeGamma/issues/12
> Collected: 2026-10-07
> Published: 2024-10-28

- Repository: bitaxeorg/bitaxeGamma
- Type: issue
- Number: 12
- State: closed
- Author: skot
- Opened: 2024-10-28
- Closed: 2025-03-03
- Labels: bug

## Description

We have reports of some bitaxeGamma 600 builds overheating in a few minutes with recommended stock heatsink and fan, running at stock settings of 525MHz / 1150mV

<img width="1355" alt="image" src="https://github.com/user-attachments/assets/89b7a5d0-3dd8-448e-a596-7f1644fb08d5">


## Comments

### skot on 2024-10-28

There are plenty of bitaxeGamma 600/601/602 that are not overheating at stock settings, including the dozen or so I have used.

### etkaar on 2024-11-14

Just for the record: I can confirm that I have _no_ overheating problems with my 601 at stock settings:

![image](https://github.com/user-attachments/assets/e15a7ed7-630c-422e-a0f4-3887877f106c)

Could it have something to do with the soldering (cold solder joints)?


### skot on 2025-03-03

This has been fixed with better temp diode tuning on the EMC2101
