# bitaxeorg/ESP-Miner issue #183: [Feature] Colour error and warning messages on the serial output

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/183
> Collected: 2026-10-07
> Published: 2024-05-25

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 183
- State: closed
- Author: HypeLaser
- Opened: 2024-05-25
- Closed: 2024-12-27
- Labels: none

## Description

Having spent the last few hours watching my monitor with 4x browser pages open on 4 different Bitaxe Realtime Log pages at the same time, it was difficult to keep up with the messages as they appeared, or to see when errors may have come up.

A useful feature would be to have certain messages be colour coded to match severity, or at least different enough for a human to parse information easier.

An example realtime log currently looks like this:

₿ (1420041) bm1366Module: RX Job ID: 48
₿ (1420041) asic_result: Nonce difficulty 1008.48 of 2048.
₿ (1420151) bm1366Module: RX Job ID: 48
₿ (1420151) asic_result: Nonce difficulty 2710.55 of 2048.
₿ (1420161) stratum_api: tx: {"id": 74, "method": "mining.submit", "params": ["thisiswheremybitcoinaddresswouldbebutiveremoved.Bitaxe", "18e7553", "0c000000", "66526e0a", "ce0601b4", "07e56000"]}
₿ (1420321) bm1366Module: RX Job ID: 48
₿ (1420321) asic_result: Nonce difficulty 562.80 of 2048.
₿ (1420341) stratum_task: rx: {"id":74,"error":null,"result":true}
₿ (1420351) stratum_task: message result accepted
₿ (1420791) bm1366Module: RX Job ID: 48
₿ (1420791) asic_result: Nonce difficulty 3731.43 of 2048.
₿ (1420801) stratum_api: tx: {"id": 75, "method": "mining.submit", "params": ["thisiswheremybitcoinaddresswouldbebutiveremoved.Bitaxe", "18e7553", "0c000000", "66526e0a", "a9a80282", "0d970000"]}
₿ (1421011) stratum_task: rx: {"id":75,"error":null,"result":true}
₿ (1421021) stratum_task: message result accepted
₿ (1421341) bm1366Module: RX Job ID: 48
₿ (1421343) ERROR
₿ (1421343) Restarting System because of API Request


But with colour coded warnings it could look like this:

<img width="641" alt="Screenshot 2024-05-26 at 00 26 18" src="https://github.com/skot/ESP-Miner/assets/110939572/26c0db64-77bf-40bc-9f82-58f3e4754e08">



## Comments

### pixeldoc2000 on 2024-06-20

This may not be so easy on the Web Log.

The serial Log (via USB) has color depending on the severity of the log message, if the terminal supports it (build in esp-idf serial log function).

### WantClue on 2024-12-27

implemented, errors are red, warnings yellow and normal processing green
