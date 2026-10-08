# bitaxeorg/ultraHex issue #43: unrouted tracks on board

> Source: https://github.com/bitaxeorg/ultraHex/issues/43
> Collected: 2026-10-07
> Published: 2024-06-27

- Repository: bitaxeorg/ultraHex
- Type: issue
- Number: 43
- State: closed
- Author: chenyang2151
- Opened: 2024-06-27
- Closed: 2024-07-02
- Labels: bug

## Description

![屏幕截图 2024-06-27 080553](https://github.com/skot/bitaxeHex/assets/6297019/17efdfcf-4d96-4f7a-8af3-da2d775078e0)


## Comments

### chenyang2151 on 2024-06-27

![屏幕截图 2024-06-27 081106](https://github.com/skot/bitaxeHex/assets/6297019/1ab1640d-6172-49f3-9249-aec7ece496de)


### chenyang2151 on 2024-06-27

U15 /vdd1 have hole

### skot on 2024-06-30

Another airwire ![image](https://github.com/skot/bitaxeHex/assets/140785/92ae1ffb-a0ac-4bb3-95b4-106e45484df3)

### chenyang2151 on 2024-07-01

hex use espminer 2.1.9 direct？ what is named broad version ？

### macphyter on 2024-07-02

This is very strange.  Those missing connections don't show up on my KiCad DRC.  I don't know why.

### macphyter on 2024-07-02

Fixed.  

### chenyang2151 on 2024-07-02

the next table is not connects' 

### aaron3481 on 2024-07-03

same, my drc does not notice me too. we found this airwrie by eye T_X

### chenyang2151 on 2024-07-03

is here 
![image](https://github.com/skot/bitaxeHex/assets/6297019/44802c32-c2de-47d4-98f6-bdb2c6679d16)
