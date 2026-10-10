# 256foundation/rhap README

> Source: https://github.com/256foundation/rhap
> Collected: 2026-10-07
> Published: Unknown

# RHAP

RHAP, the Raw Hardware Access Protocol, gives a host program direct
access to the hardware on a mining board over USB. Firmware on the
board's microcontroller takes the device role, RHAP-D. It passes the
ASIC serial bus, I2C, GPIO, and ADC through two USB serial ports. The
host drives the board through those ports.

This repository holds the protocol specification and client
libraries. Until the specification is written, the [rhapd-bitaxe-gamma
README][rhapd-bitaxe-gamma] describes the protocol.

## Implementations

Device:

- [rhapd-bitaxe-gamma]: firmware for the Bitaxe Gamma
- [emberone-usbserial-fw]: firmware for the EmberOne hashboard

Host:

- [Mujina]: open source Bitcoin mining software
- [emberone-miner]: Python miner for EmberOne testing
- [emberone-test-scripts]: EmberOne bring-up and test scripts

## License

Mozilla Public License 2.0. See [LICENSE](LICENSE).

[rhapd-bitaxe-gamma]: https://github.com/256foundation/rhapd-bitaxe-gamma
[emberone-usbserial-fw]: https://github.com/256foundation/emberone-usbserial-fw
[Mujina]: https://github.com/256foundation/mujina
[emberone-miner]: https://github.com/skot/emberone-miner
[emberone-test-scripts]: https://github.com/256foundation/emberone-test-scripts
