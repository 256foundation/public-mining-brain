# Bitaxe Gamma Hex

> Source: https://osmu.xyz/t/bitaxe-gamma-hex/77
> Collected: 2026-10-10
> Published: 2026-08-20
> Registry ID: osmu-forum

WantClue | 2026-08-20 21:23:17 UTC | #1

The Bitaxe Gamma Hex is the newest Hex model of the Bitaxe family and can be found here: [GitHub - bitaxeorg/BitaxeGammaHex: Bitaxe Gamma Hex 6x BM1370 ASIC ESP32 powered Bitcoin miner · GitHub](https://github.com/bitaxeorg/BitaxeGammaHex)

-------------------------

engrHasanRizvi | 2026-09-18 02:37:05 UTC | #2

Very nice design. I am wondering if it is possible to build a similar miner with higher number of ASICs, say 50 BM1370 chips. We would need to be able to implement multiple power domains and probably group 4 or 5 Asics per domain and handle heat dissipation accordingly. But my question is that Bitaxe ESP32 controller can handle that many chips daisy chained?

-------------------------

WantClue | 2026-09-18 06:30:24 UTC | #3

It should be able to do so.

Ideally it should be an increase gradually, like 10 → 20 → 30 chips and so on. But just from the capability the esp32s3 should be able to handle a good amount of chips
