# bitaxeorg/bitaxeGamma issue #21: Failure to find select PLL frequencies when overclocking

> Source: https://github.com/bitaxeorg/bitaxeGamma/issues/21
> Collected: 2026-10-07
> Published: 2025-01-11

- Repository: bitaxeorg/bitaxeGamma
- Type: issue
- Number: 21
- State: closed
- Author: jtsmith0101
- Opened: 2025-01-11
- Closed: 2025-03-03
- Labels: none

## Description

Investingating higher frequencies.  On startup, there are several frequency failure messages above 750 MHz.  Please see attached. 

![image](https://github.com/user-attachments/assets/c2e6e4af-f9b8-4db5-ab61-aa7e54fc027a)

Does this mean my hashing on a 600 gamma is capped?  Can it be fixed with a new firmware or does it indicate a hardware anomaly?

My firmware is v2.4.4

## Comments

### skot on 2025-03-03

No your frequency is not capped. Due to the way (we think the) BM1370 registers work, not all frequencies are available. All that really matters here is that it can find the last one.
