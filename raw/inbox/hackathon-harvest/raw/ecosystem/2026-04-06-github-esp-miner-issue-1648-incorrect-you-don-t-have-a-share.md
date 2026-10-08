# bitaxeorg/ESP-Miner issue #1648: Incorrect "You don't have a share in the coinbase reward" warning when using testnet4

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1648
> Collected: 2026-10-07
> Published: 2026-04-06

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1648
- State: closed
- Author: pdath
- Opened: 2026-04-06
- Closed: 2026-04-24
- Labels: none

## Description

**Description**

When mining to Bitcoin testnet4 using an address like tb1qn9quw86c6gv3642enrxaglvrqxt032kej9ydjh.bitaxe on ckpool-solo, an incorrect warning banner is displayed saying "You don't have a share in the coinbase reward".

ckpool-solo *does* correctly payout to the testnet4 address when a block is solved.

**To Reproduce**
1. Go to pool in the Bitaxe web gui.
2. Enter a testnet4 stratum host and port.
3. Enter a valid testnet4 user, such as tb1qn9quw86c6gv3642enrxaglvrqxt032kej9ydjh.bitaxe.
4. Click save, and then restart

**Expected behavior**
No warnings are expected.

**Screenshots & Photos**
If applicable, add AxeOS screenshots and/or photos of your Bitaxe to help explain your problem.

**Hardware (please complete the following information):**
 - Bitaxe Gama 601
 - ASIC BM1370
 - ESP-Miner FW version: 2.13.1
 - Hash Frequency: All settings on stock.

<img width="1042" height="87" alt="Image" src="https://github.com/user-attachments/assets/ca5d36c0-52c0-4ca7-ba9a-55415731de61" />

<img width="821" height="405" alt="Image" src="https://github.com/user-attachments/assets/515b8d07-4236-4a47-b2ec-892a795b1e11" />

## Comments

### mutatrum on 2026-04-06

This might be fixed by #1578 

### pdath on 2026-04-06

> This might be fixed by [#1578](https://github.com/bitaxeorg/ESP-Miner/pull/1578)

That does sound like it will fix it.

### mutatrum on 2026-04-23

#1578 is merged, can you check if it's fixed now?

### 0xdeadbeefnetwork on 2026-04-23

Code-level confirmation that #1578 fixes this:

The banner is driven by `getPayoutPercentage()` in `home.component.ts:931`, which divides `coinbaseValueUserSatoshis` by `coinbaseValueTotalSatoshis`. The user value is only incremented in `coinbase_process_notification` when `strncmp(user_address, output_address, ...)` matches.

Before #1578, `coinbase_decode_address_from_scriptpubkey` hardcoded mainnet (`"bc"` HRP, `0x00`/`0x05` base58 versions), so a decoded testnet4 output came back as `bc1...` while the stratum user address was `tb1...` — the strncmp always failed, `user_value_satoshis` stayed at 0, and the "no share" banner fired.

#1578 detects the network from the user address prefix (`tb1`/`bcrt1`/`m`/`n`/`2`) and passes the correct HRP and base58 version bytes down to the encoder, so the strncmp now matches on testnet4/regtest. That's the only code path that feeds this banner, so the symptom reported here should be gone.

Worth a fresh test on master to confirm and close.

### pdath on 2026-04-23

Is there a binary build of this fix I can load onto a BitAxe to test it?

### 0xdeadbeefnetwork on 2026-04-24

Yes — CI already builds these on every push. The most recent successful `master` build that includes #1578 is commit [`aa62bc4`](https://github.com/bitaxeorg/ESP-Miner/commit/aa62bc4a065e925307eeb81f9f05a037fa651ff3), run [24636422332](https://github.com/bitaxeorg/ESP-Miner/actions/runs/24636422332). Artifacts (expire 2026-07-18, GitHub login required to download):

- [`esp-miner.bin`](https://github.com/bitaxeorg/ESP-Miner/actions/runs/24636422332/artifacts/6520361436) — firmware
- [`www.bin`](https://github.com/bitaxeorg/ESP-Miner/actions/runs/24636422332/artifacts/6520361550) — AxeOS UI
- [`esp-miner-factory.bin`](https://github.com/bitaxeorg/ESP-Miner/actions/runs/24636422332/artifacts/6520361325) — merged image (only needed for a full factory reflash)

For your Gama 601 you just want `esp-miner.bin` + `www.bin` — OTA both from the AxeOS UI (System → Update Firmware / Update AxeOS). Hardware config lives in NVS and is preserved across OTA, so no need to touch the factory image.

If you'd rather pin to the exact merge commit of #1578 with nothing after it, that run is [24576328159](https://github.com/bitaxeorg/ESP-Miner/actions/runs/24576328159) (commit `8b17785`).

### pdath on 2026-04-24

I have tested the binary firmware image and can confirm the bug is fixed.
