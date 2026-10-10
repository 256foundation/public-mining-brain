# bitaxeorg/bitaxeGamma issue #2: Wrong display connector

> Source: https://github.com/bitaxeorg/bitaxeGamma/issues/2
> Collected: 2026-10-07
> Published: 2024-08-27

- Repository: bitaxeorg/bitaxeGamma
- Type: issue
- Number: 2
- State: closed
- Author: marplukiwi
- Opened: 2024-08-27
- Closed: 2024-09-19
- Labels: none

## Description

The display Connector NPTC041KFXC-RC in the BOM File is wron

## Comments

### marplukiwi on 2024-08-27

<img width="295" alt="Bildschirmfoto 2024-08-27 um 22 12 03" src="https://github.com/user-attachments/assets/8443efd0-8d94-4e84-9612-c01000d671b0">


### yellowpi on 2024-09-19

> The display Connector NPTC041KFXC-RC in the BOM File is wron

And what is the truth? Did you find out?



### yellowpi on 2024-09-19

> The display Connector NPTC041KFXC-RC in the BOM File is wron

It's the same component used in the 401 Supra. Compatible with the 600 model and the 601 model? I don't understand why you made such a comment. So far, none of the professional sellers who have assembled this project have written a comment on this subject.
I would like you to share your experience and evaluation and the solution you have produced with us. 



### marplukiwi on 2024-09-19

I soldered the display directly to the PCB without a connector. This is also better because the display only has a small distance to the PCB and cannot bend.

### yellowpi on 2024-09-19

> I soldered the display directly to the PCB without a connector. This is also better because the display only has a small distance to the PCB and cannot bend.

Hello, you can use the screen reinforcement in the link below by printing it from your 3D printer and use it compatible with your screen.
 with love.

link

https://github.com/IamGPIO/Bitaxe201-204-ScreenSaver




### skot on 2024-09-19

Hey, sorry about that. There is no connector needed on the PCB for the display. Get a OLED with male pins and it will friction-fit into the holes on the Bitaxe PCB -- or you can solder them in.

I'll get this fixed on the BOM

### yellowpi on 2024-09-19

> Hey, sorry about that. There is no connector needed on the PCB for the display. Get a OLED with male pins and it will friction-fit into the holes on the Bitaxe PCB -- or you can solder them in.
> 
> I'll get this fixed on the BOM

Mr. skot, is there no need to buy this? Should we buy this component?

### skot on 2024-09-19

J3 part number has been removed from schematic and BOM. There is no need for a part on this footprint.
