# A modified 6-ASIC version of Bitaxe.Open sources

> Source: https://osmu.xyz/t/a-modified-6-asic-version-of-bitaxe-open-sources/99
> Collected: 2026-10-10
> Published: 2026-09-26
> Registry ID: osmu-forum

TDX33029 | 2026-09-26 17:47:45 UTC | #1

This is a modified version. Since I have a large stock of STM32 chips on hand, I opted to use Ethernet to control multiple Bitaxe units rather than having them operate independently via ESP32s. This setup allows a single PC to control up to 220 Bitaxe units, monitoring metrics such as temperature, real-time hashrate, submitted shares, and rejection rates, while also enabling the remote power control of individual units. The PC takes over the tasks previously handled by the ESP32s, managing pool connectivity and job distribution; all you need is a network switch and the necessary Ethernet cables to connect them. I rewrote the firmware to accommodate the different chips and functionality. Both the hardware and software have been tested and are fully operational. All files—covering both hardware and software—are open-source; this was a massive undertaking. I would like to thank the community for their significant contributions in reverse-engineering the chip communication protocols, which made our work much easier.

I also modified the power supply scheme and removed certain components to further reduce costs.![image](https://osmu.xyz/uploads/default/original/1X/4a45fcca982e9b011179a434880a47d6c7de75e8.jpeg)

Feel free to check out my repository.[Github Repository](https://github.com/TDX33029/BTCMinerControl)，an English version of the README file is provided here.

-------------------------

WantClue | 2026-09-27 07:15:41 UTC | #2

This is awesome! I’ll def. look into this
