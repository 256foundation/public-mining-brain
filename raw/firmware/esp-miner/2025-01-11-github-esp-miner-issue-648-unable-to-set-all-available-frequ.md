# bitaxeorg/ESP-Miner issue #648: Unable to set all available frequencies above 750 MHz

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/648
> Collected: 2026-10-07
> Published: 2025-01-11

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 648
- State: closed
- Author: jtsmith0101
- Opened: 2025-01-11
- Closed: 2025-01-12
- Labels: none

## Description

![image](https://github.com/user-attachments/assets/287d0de6-d8dc-4eb9-b650-61c6194a2e55)

Observing logs on startup. appears either chip issue or some unexpected behavior when attempting to set frequencies above 750 MHz.

## Comments

### jtsmith0101 on 2025-01-11

for lots of testing above 750 MHz, it reliably cannot lock all frequencies above 750.

### skot on 2025-01-11

Due to the overlap of the two PLL registers on the ASIC, not all frequencies will be available. You should be able to ramp up well over 1 GHz, it's just not all intermediate frequencies along the way are available.

tl;dr, this isn't a problem.

### jtsmith0101 on 2025-01-12

Sweet!  Thanks!

On Sun, 12 Jan 2025, 10:50 Skot, ***@***.***> wrote:

> Due to the overlap of the two PLL registers on the ASIC, not all
> frequencies will be available. You should be able to ramp up well over 1
> GHz, it's just not all intermediate frequencies along the way are available.
>
> tl;dr, this isn't a problem.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/skot/ESP-Miner/issues/648#issuecomment-2585482466>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ACPVG7D62MGP25QSSJ6EFLT2KGU4DAVCNFSM6AAAAABVALGS3OVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDKOBVGQ4DENBWGY>
> .
> You are receiving this because you authored the thread.Message ID:
> ***@***.***>
>
