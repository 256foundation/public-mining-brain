# bitaxeorg/ultraHex issue #19: rackable version !

> Source: https://github.com/bitaxeorg/ultraHex/issues/19
> Collected: 2026-10-07
> Published: 2024-02-12

- Repository: bitaxeorg/ultraHex
- Type: issue
- Number: 19
- State: closed
- Author: phil31
- Opened: 2024-02-12
- Closed: 2024-03-24
- Labels: none

## Description

Hi

i just discover your project and imagin already a rackable version ..
i mean a daughter board with 8 ASICS and PSU and a connector to chain several boards ..
we can design a "mother board" with a single ESP32, a TFT screen and something to share / buffer links with each daughter boards..
maybe an FPGA, with 8 UARTs inside and some fifo .. 
or use 8 software UART in the ESP32 ..?

a watercooling system maybe a better option too.. avoid some noise !

what is the actual status of your design ?

regards
phil


## Comments

### warchiefmarkus on 2024-03-23

Yes, just want to say the same, 6 chips on board - not enough ! We need the ability to add a few hundreds 😁 maybe via increasing size of pcb (maybe a few level  pcbs stack?) or via adding some type of connectors to main control pcb with esp32 and ability to connect additional pcbs with Asics to it 

### macphyter on 2024-03-24

These are all great ideas, but they involve a new project, not for the Hex board.  There may be projects like this down the road.  If not, feel free to start your own, its fun!


### phil31 on 2024-03-24

yes ! i started my fork project with a rackable architecture .. 
work in progress, will keep you in touch when/if something materializes !

but anyway, this project is for fun... no profitability expected !

regards
