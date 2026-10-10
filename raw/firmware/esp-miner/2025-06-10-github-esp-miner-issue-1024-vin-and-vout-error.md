# bitaxeorg/ESP-Miner issue #1024: vin and vout error

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1024
> Collected: 2026-10-07
> Published: 2025-06-10

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1024
- State: closed
- Author: rene-72
- Opened: 2025-06-10
- Closed: 2025-06-10
- Labels: none

## Description

I had a lv07 miner with 1.10 firmware
I flashed custom firmware but after that I get these vin/vou errors
Also I see danger low voltage input 0V ??!!
Did try several versions but issues still is here. Could someone help me with this ?

₿ (176260) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (176270) i2c_bitaxe: Device TPS546.c (0x24)
₿ (176820) stratum_task: rx: {"params":["683056a60000d45d","cfb3d048b0051135298af4f85b91ad4c52f9ea89000217a60000000000000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff3503febd0d0004f20c486804aeabda060c","0a636b706f6f6c112f736f6c6f2e636b706f6f6c2e6f72672fffffffff034062741200000000160014cf3815a968c8d3cd9e58facfdb7f85c3762159db7e6a60000000000016001451ed61d2f6aa260cc72cdf743e4e436a82c010270000000000000000266a24aa21a9eda61a05c43534790570d44d629729ff36f4c97006481b6f5ef02ec87281eb7ecc00000000",["7e188e0edef9f230d2f82c38b890ed8ceb03caecc79b78d48ad0e84c9a6fee6b","20717fe3ccafc02c1399d1c723134049565e6f0dc61616881888e41fd794ddab","45af847d29958c7c3cf361c62b3e63f48d470146db6aa6a0f276236e65dffeaf","ff4962344475c37a6a35abfb829a1405c606dee0003e6e861d86c5c90f7f148f","9490225aae49fd5871f06770ef7dc84620ca7a771fdac96551fb6e377607b75e","63686c269dd98b6a0bb2f6a5a648c474411c085d0315d635d82d64bae46964db","e735acbd8e9f4485f9a674948d7d1194d5d9be5e254f39874d778256a3cb06a7","eb17fa8c3c234d3083d3d8de147f897c0c75c0bda95c6fb8f25cf33056528418","c53236993e5c6b12fa5d06ab62e82382ae4f2ce2ff29b12c2454e0db838438b0","d9c1413c6fdc005fc009068df120e6318d6b76af8fc3d76b93cea742e69b1d9c","c4cea015e9600e8d07bd3fd0768c50e3f2c448d5fcc2f1a7a0b792ef4968a815","2c475aef0e3bfa046f5533627176fd1e4e6f07458376b10ba7fed606c2136e5d","01a19fc68531f9d88a168d210570daa854299c683aa54a0beb7f9581dd8f4178"],"20000000","17023774","68480cf2",false],"id":null,"method":"mining.notify"}
₿ (177000) create_jobs_task: New Work Dequeued 683056a60000d45d
₿ (178270) i2c.master: I2C transaction unexpected nack detected
₿ (178270) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (178270) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (178280) i2c_bitaxe: Device TPS546.c (0x24)
₿ (178280) TPS546.c: Could not read VIN
₿ (178290) i2c.master: I2C transaction unexpected nack detected
₿ (178290) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (178300) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (178310) i2c_bitaxe: Device TPS546.c (0x24)
₿ (178320) TPS546.c: Could not read Iout
₿ (178320) i2c.master: I2C transaction unexpected nack detected
₿ (178330) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (178330) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (178340) i2c_bitaxe: Device TPS546.c (0x24)
₿ (178350) TPS546.c: Could not read Vout
₿ (178350) i2c.master: I2C transaction unexpected nack detected
₿ (178360) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (178370) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (178370) i2c_bitaxe: Device TPS546.c (0x24)
₿ (180040) i2c.master: I2C transaction unexpected nack detected
₿ (180040) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (180050) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (180050) i2c_bitaxe: Device TPS546.c (0x24)
₿ (180060) TPS546.c: Could not read Vout
₿ (180380) i2c.master: I2C transaction unexpected nack detected
₿ (180380) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (180380) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (180390) i2c_bitaxe: Device TPS546.c (0x24)
₿ (180390) TPS546.c: Could not read VIN
₿ (180400) i2c.master: I2C transaction unexpected nack detected
₿ (180400) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (180410) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (180420) i2c_bitaxe: Device TPS546.c (0x24)
₿ (180430) TPS546.c: Could not read Iout
₿ (180430) i2c.master: I2C transaction unexpected nack detected
₿ (180440) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (180440) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (180450) i2c_bitaxe: Device TPS546.c (0x24)
₿ (180460) TPS546.c: Could not read Vout
₿ (180460) i2c.master: I2C transaction unexpected nack detected
₿ (180470) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (180480) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (180490) i2c_bitaxe: Device TPS546.c (0x24)
₿ (182490) i2c.master: I2C transaction unexpected nack detected
₿ (182490) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (182490) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (182500) i2c_bitaxe: Device TPS546.c (0x24)
₿ (182500) TPS546.c: Could not read VIN
₿ (182510) i2c.master: I2C transaction unexpected nack detected
₿ (182510) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (182520) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (182530) i2c_bitaxe: Device TPS546.c (0x24)
₿ (182540) TPS546.c: Could not read Iout
₿ (182540) i2c.master: I2C transaction unexpected nack detected
₿ (182550) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (182550) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (182560) i2c_bitaxe: Device TPS546.c (0x24)
₿ (182570) TPS546.c: Could not read Vout
₿ (182570) i2c.master: I2C transaction unexpected nack detected
₿ (182580) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (182590) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (182600) i2c_bitaxe: Device TPS546.c (0x24)
₿ (184600) i2c.master: I2C transaction unexpected nack detected
₿ (184600) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (184600) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (184610) i2c_bitaxe: Device TPS546.c (0x24)
₿ (184610) TPS546.c: Could not read VIN
₿ (184620) i2c.master: I2C transaction unexpected nack detected
₿ (184620) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (184630) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (184640) i2c_bitaxe: Device TPS546.c (0x24)
₿ (184650) TPS546.c: Could not read Iout
₿ (184650) i2c.master: I2C transaction unexpected nack detected
₿ (184660) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (184660) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (184670) i2c_bitaxe: Device TPS546.c (0x24)
₿ (184680) TPS546.c: Could not read Vout
₿ (184680) i2c.master: I2C transaction unexpected nack detected
₿ (184690) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (184700) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (184700) i2c_bitaxe: Device TPS546.c (0x24)
₿ (186710) i2c.master: I2C transaction unexpected nack detected
₿ (186710) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (186710) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (186720) i2c_bitaxe: Device TPS546.c (0x24)
₿ (186720) TPS546.c: Could not read VIN
₿ (186730) i2c.master: I2C transaction unexpected nack detected
₿ (186730) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (186740) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (186750) i2c_bitaxe: Device TPS546.c (0x24)
₿ (186760) TPS546.c: Could not read Iout
₿ (186760) i2c.master: I2C transaction unexpected nack detected
₿ (186770) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (186770) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (186780) i2c_bitaxe: Device TPS546.c (0x24)
₿ (186790) TPS546.c: Could not read Vout
₿ (186790) i2c.master: I2C transaction unexpected nack detected
₿ (186800) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (186810) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (186810) i2c_bitaxe: Device TPS546.c (0x24)
₿ (188820) i2c.master: I2C transaction unexpected nack detected
₿ (188820) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (188820) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (188830) i2c_bitaxe: Device TPS546.c (0x24)
₿ (188830) TPS546.c: Could not read VIN
₿ (188840) i2c.master: I2C transaction unexpected nack detected
₿ (188840) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (188850) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (188860) i2c_bitaxe: Device TPS546.c (0x24)
₿ (188870) TPS546.c: Could not read Iout
₿ (188870) i2c.master: I2C transaction unexpected nack detected
₿ (188880) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (188880) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (188890) i2c_bitaxe: Device TPS546.c (0x24)
₿ (188900) TPS546.c: Could not read Vout
₿ (188900) i2c.master: I2C transaction unexpected nack detected
₿ (188910) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (188920) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (188920) i2c_bitaxe: Device TPS546.c (0x24)
₿ (188990) i2c.master: I2C transaction unexpected nack detected
₿ (188990) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (189000) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (189000) i2c_bitaxe: Device TPS546.c (0x24)
₿ (189010) TPS546.c: Could not read Vout
₿ (189830) i2c.master: I2C transaction unexpected nack detected
₿ (189830) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (189840) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (189840) i2c_bitaxe: Device TPS546.c (0x24)
₿ (189850) TPS546.c: Could not read Vout
₿ (190930) i2c.master: I2C transaction unexpected nack detected
₿ (190930) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (190930) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (190940) i2c_bitaxe: Device TPS546.c (0x24)
₿ (190940) TPS546.c: Could not read VIN
₿ (190950) i2c.master: I2C transaction unexpected nack detected
₿ (190950) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (190960) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (190970) i2c_bitaxe: Device TPS546.c (0x24)
₿ (190980) TPS546.c: Could not read Iout
₿ (190980) i2c.master: I2C transaction unexpected nack detected
₿ (190990) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (190990) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (191000) i2c_bitaxe: Device TPS546.c (0x24)
₿ (191010) TPS546.c: Could not read Vout
₿ (191010) i2c.master: I2C transaction unexpected nack detected
₿ (191020) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (191030) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (191030) i2c_bitaxe: Device TPS546.c (0x24)
₿ (193040) i2c.master: I2C transaction unexpected nack detected
₿ (193040) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (193040) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (193050) i2c_bitaxe: Device TPS546.c (0x24)
₿ (193050) TPS546.c: Could not read VIN
₿ (193060) i2c.master: I2C transaction unexpected nack detected
₿ (193060) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (193070) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (193080) i2c_bitaxe: Device TPS546.c (0x24)
₿ (193090) TPS546.c: Could not read Iout
₿ (193090) i2c.master: I2C transaction unexpected nack detected
₿ (193100) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (193100) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (193110) i2c_bitaxe: Device TPS546.c (0x24)
₿ (193120) TPS546.c: Could not read Vout
₿ (193120) i2c.master: I2C transaction unexpected nack detected
₿ (193130) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (193140) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (193150) i2c_bitaxe: Device TPS546.c (0x24)
₿ (194880) i2c.master: I2C transaction unexpected nack detected
₿ (194880) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (194880) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (194890) i2c_bitaxe: Device TPS546.c (0x24)
₿ (194900) TPS546.c: Could not read Vout
₿ (195160) i2c.master: I2C transaction unexpected nack detected
₿ (195160) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (195170) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (195170) i2c_bitaxe: Device TPS546.c (0x24)
₿ (195180) TPS546.c: Could not read VIN
₿ (195180) i2c.master: I2C transaction unexpected nack detected
₿ (195190) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (195200) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (195210) i2c_bitaxe: Device TPS546.c (0x24)
₿ (195210) TPS546.c: Could not read Iout
₿ (195220) i2c.master: I2C transaction unexpected nack detected
₿ (195220) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (195230) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (195240) i2c_bitaxe: Device TPS546.c (0x24)
₿ (195240) TPS546.c: Could not read Vout
₿ (195250) i2c.master: I2C transaction unexpected nack detected
₿ (195250) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (195260) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (195270) i2c_bitaxe: Device TPS546.c (0x24)
₿ (197280) i2c.master: I2C transaction unexpected nack detected
₿ (197280) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (197280) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (197290) i2c_bitaxe: Device TPS546.c (0x24)
₿ (197290) TPS546.c: Could not read VIN
₿ (197300) i2c.master: I2C transaction unexpected nack detected
₿ (197300) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (197310) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (197320) i2c_bitaxe: Device TPS546.c (0x24)
₿ (197330) TPS546.c: Could not read Iout
₿ (197330) i2c.master: I2C transaction unexpected nack detected
₿ (197340) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (197340) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (197350) i2c_bitaxe: Device TPS546.c (0x24)
₿ (197360) TPS546.c: Could not read Vout
₿ (197360) i2c.master: I2C transaction unexpected nack detected
₿ (197370) i2c.master: s_i2c_synchronous_transaction(918): I2C transaction failed
₿ (197380) i2c.master: i2c_master_transmit_receive(1214): I2C transaction failed
₿ (197390) i2c_bitaxe: Device TPS546.c (0x24)

## Comments

### MyOwn2C on 2025-06-10

LV07 is not supported. 

### skot on 2025-06-10

LuckyMiner is a scam product and is not supported by esp-miner.
