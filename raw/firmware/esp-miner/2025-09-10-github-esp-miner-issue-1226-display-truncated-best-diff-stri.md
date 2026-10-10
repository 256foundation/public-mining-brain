# bitaxeorg/ESP-Miner issue #1226: Display: Truncated best diff string

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1226
> Collected: 2026-10-07
> Published: 2025-09-10

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1226
- State: closed
- Author: duckaxe
- Opened: 2025-09-10
- Closed: 2025-11-02
- Labels: bug

## Description

The `Best:` string on the display is truncated if it gets too long. The issue occurred after we [added](https://github.com/bitaxeorg/ESP-Miner/discussions/1085) a space after the number.

**Expected**
`Best: 400.08 M/200.54 G`

**Displayed**
`Best: 400.08 M/200.54`

@mutatrum suggested to add a half space (3 pixels wide instead of 6). It's a good idea to wait until his PR https://github.com/bitaxeorg/ESP-Miner/pull/1214 is merged and benefit from his change to add the half space `\u2009` to the font.

**User Image 1**
![Image](https://github.com/user-attachments/assets/7eafd5cb-b07a-4d09-889b-7118a3baf5f1)

**User Image 2**
![Image](https://github.com/user-attachments/assets/8546c883-dc5b-4f55-8513-2d61ea96962d)

## Comments

### mutatrum on 2025-09-14

Alternative solution would be to do #1202 and have the numbers be integers internally and have a separate formatter in AxeOS and for the display.

### duckaxe on 2025-10-23

@mutatrum I added the thin space and that would fix the issue that is mentioned in the user photos above.
Now 9 digits fit completely on the display. 10 digits don't fit. 

https://github.com/bitaxeorg/ESP-Miner/pull/1202 is merged and I would say we remove the space completely from `suffixString` so that we don't have a space after digits only on display (as we had it before). Any other thoughts?

![Image](https://github.com/user-attachments/assets/70e1a8d4-f1f9-430b-ae83-c86bb792487c)

![Image](https://github.com/user-attachments/assets/764dce73-8998-418b-9c5b-9da89da79be3)

### mutatrum on 2025-10-23

Yeah, display is too small to have spaces. Same as with the temperature, looks weird with the huge wide gap between the digits and °C.

Looking at it more, it's a weird layout on the display, with some units before and some after the value.
```
|---------------------| (21 chars max)
|Hash: 512.31Gh/s     |
|Eff.: 22.12J/Th      |
|Best: 839.36M/739.76M|
|Temp: 55.0°C         |
|---------------------|
```

### duckaxe on 2025-10-23

If we remove the space from `suffixString`, `networkDifficulty` also loses the space. What was the reason for `networkDifficulty` delivering a formatted string to AxeOS?

<img width="299" height="214" alt="Image" src="https://github.com/user-attachments/assets/edebdba5-de7e-408a-9d95-9d800bd312eb" />

### duckaxe on 2025-10-24

Is "Hash" a good shortcut for hashrate? 512.31Gh/s is very difficult to read. Personally, I found the old spelling `Gh/s: digits` much better.
