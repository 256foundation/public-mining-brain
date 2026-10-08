# bitaxeorg/ESP-Miner issue #96: Bitaxetool - Python v3.12 no longer supports 'distutils' module

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/96
> Collected: 2026-10-07
> Published: 2024-01-22

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 96
- State: closed
- Author: qubyt3
- Opened: 2024-01-22
- Closed: 2024-02-17
- Labels: bug

## Description

Hello Team! I noticed when playing around with the new firmware release 2.0.7 yesterday, that if we try and use the bitaxetool to update it will no longer work if users have installed the latest Python v3.12. 
The 'distutils' module has been depreciated, see PEP 632 - Deprecate distutils module. 

I'm not sure if you guys already knew about this but I thought I would let you know just in case. 

Take care! 

## Comments

### skot on 2024-02-16

I seem to remember there is a fix for this. @johnny9 do you remember?

### johnny9 on 2024-02-16

Fix is to use an older python. This affects windows users primarily. I should fix this asap. It's trivial to fix just need to stop forgetting. 

### johnny9 on 2024-02-17

This should now be fixed with the latest version of bitaxetool. `pip install --upgrade bitaxetool` to get the latest version


### qubyt3 on 2024-02-17

Works like a charm, thanks @johnny9!
