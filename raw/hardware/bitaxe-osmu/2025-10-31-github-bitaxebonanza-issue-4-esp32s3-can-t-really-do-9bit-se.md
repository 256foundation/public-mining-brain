# bitaxeorg/bitaxeBonanza issue #4: ESP32S3 can't really do 9bit serial as required by the BZM2

> Source: https://github.com/bitaxeorg/bitaxeBonanza/issues/4
> Collected: 2026-10-07
> Published: 2025-10-31

- Repository: bitaxeorg/bitaxeBonanza
- Type: issue
- Number: 4
- State: closed
- Author: skot
- Opened: 2025-10-31
- Closed: 2026-02-12
- Labels: bug

## Description

The Intel BZM2 ASIC serial communication is 9bit. 

> The UART interface in Intel® Blockscale™ 1000 series ASIC operates in a 9 bit mode; the parity bit is used as the 9th bit and is added to each transmitted bytes between the MSB of the data byte and the STOP bit. The 9th bit indicates the use of the preceding 8 bits and if the 9th bit is ‘1’ it’s address byte and ‘0’ is data byte.

<img width="715" height="128" alt="Image" src="https://github.com/user-attachments/assets/68bcf552-11d9-44af-8d2d-c9209faa143b" />

9bit uart serial format and is **not** natively supported by the ESP32 UART peripheral hardware. The Intel docs suggest that it's just the parity bit, but that's not how the parity bit works; 

> The parity bit is an optional error-detection bit added to a UART data frame to help the receiver detect simple transmission errors (like a single bit flip due to noise).

The ESP32 UART peripheral supports adding the parity bit, but it's hardcoded to be used as an error detection bit, not an additional arbitrary mode data bit like the BZM2 wants. I initally though we could (ab)use the ESP32 UART parity bit to be the mode bit. Initial tests suggested this would work; but it doesn't really. We can use the ESP32 CPU to change the parity bit, but being under CPU control causes this additional bit to be asynchronous with the 8bit data register in the UART. This really starts to fall apart at the high data rates needed by the BZM2.

The other hack that seemed possible is using the ESP32's RMT peripheral to emulate a 9bit UART. There are two proof-of-concepts out there for this approach;
- https://github.com/qqqlab/ESP32-Serial-RMT-UART
- https://github.com/naffej/esp32-rmt-uart

The issue here is the datarate and the number of bytes to be transmitted. These are both limited with the RMT. The solution used by the qqqlab RMT UART implementation is a buffer, but that is done in software, potentially affecting the datarate. It could still work, but it would take a lot of effort for what is still a gnarly hack.

I looked into using a separate HW UART, but chips supporting this old school method are either expensive and/or out of production.

There are certainly other MCUs that have native 9bit serial-capable UART peripherals, like the STM32F4 and the RP2030/RP2350. A sidecar FPGA could also easily handle 9bit serial. I think the solution going forward is to either use a sidecar RP2040 or FPGA with the ESP32, or just switch the whole controller to a RP2350. The issue with switching to a RP2350 is that it does not have WiFi. The RaspberryPi Pico 2 solves this by adding a separate Infineon CYW43439 WiFi module. That module isn't really practical to use on it's own, but maybe there is something similar.

## Comments

### skot on 2026-02-12

fixed with 1002x
