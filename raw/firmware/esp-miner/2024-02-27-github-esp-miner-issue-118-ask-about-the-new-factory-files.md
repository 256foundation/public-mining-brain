# bitaxeorg/ESP-Miner issue #118: Ask about the new factory files

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/118
> Collected: 2026-10-07
> Published: 2024-02-27

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 118
- State: closed
- Author: kakawlala
- Opened: 2024-02-27
- Closed: 2024-02-29
- Labels: none

## Description

Hello, I'm soldering bitaxeUltra205(BM1366) and Bitaxe Supra(BM1368).  

Since I am not familiar with the command operation, whether to add spaces or "-" symbols.  I tried many times and finally successfully installed Python and pip on the computer, and updated bitaxetool.
The screen shows the progress of bitaxetool installation and update.

And modify the corresponding version of the "config.cvs" content.
In the end, I still couldn't operate the "bitaxetool --config ./config.cvs --firmware ./esp-miner-factory-v2.0.7.bin" command.  

Whether the "esp-miner-factory-205-v2.0.7.bin" and "esp-miner-factory-400-v2.0.7.bin" files will be updated in the future. 

Using a flasher such as https://espressif.github.io/esptool-js/ instead of bitaxetool and flashing to the address 0x0 is a task I am familiar with.

![P_20240228_163619](https://github.com/skot/ESP-Miner/assets/89348834/89b75bd5-8366-4eaa-850d-4a46f0af346b)

![P_20240228_164255](https://github.com/skot/ESP-Miner/assets/89348834/9069a55a-b92d-459a-9d38-0c0ad292e6a3)

Did I enter the wrong command?  Or which folder should the files be placed in?

![P_20240228_165209](https://github.com/skot/ESP-Miner/assets/89348834/bd314a73-7342-41f8-a642-bfada2d7cff9)

Changing the file location to C: seems to have flashed

![Screenshot_20240228-185723_Chrome (1)](https://github.com/skot/ESP-Miner/assets/89348834/1481a04f-fc46-4c78-803b-c763aa149756)
