# bitaxeorg/ESP-Miner issue #1118: Error - while update esp-miner.bin and www.bin - Unauthorized

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1118
> Collected: 2026-10-07
> Published: 2025-07-03

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1118
- State: closed
- Author: diegorodriguezv
- Opened: 2025-07-03
- Closed: 2026-06-22
- Labels: enhancement, api change

## Description

**Describe the bug**
Updates cannot be installed; they run up to 100% and then report an error.
When updating both files, I receive the following error message after the update:

[www.bin](http://www.bin/) -> Error - Http failure response for http://bitaxe/api/system/OTAWWW: 401 Unauthorized
esp-miner.bin -> Unauthorized

This is basically a copy-paste of issue #671. I can't tell if this is a regression or if the bug wasn't actually fixed.

**To Reproduce**
Steps to reproduce the behavior:

- access the web interface http://bitaxe
- install previous version:  v2.8.1
- download Latest Release: v2.9.0
- start Updates
- error message appears and update is unsuccessful

**Expected behavior**
The update should succeed. 

**Hardware (please complete the following information):**
 - Bitaxe HW version: Gamma 601
 - Bitaxe HW vendor: bitcoinmerch
 - ESP-Miner FW version: v2.8.1
 - Hash Frequency: 625
 - Voltage: 5

**Additional context**
This happens using the url: `http://bitaxe` or `http://bitaxe.lan`. I have my main router configured to use `lan` as the local domain.
I know you can use the ip address as a workaround but for not-technical-savvy people this can be frustrating. Using `http://bitaxe` is convenient for new users.
The hostname in the network configuration is the default `bitaxe`.


## Comments

### diegorodriguezv on 2025-07-03

I tried changing the hostname to `bitaxe69` and changing the url to `http://bitaxe69` and the same problem happens. 
Related to this, I can't change the hostname unless I access the web interface using the ip. Otherwise the same error message appears.
Also, the same bug is present in  v2.9.0.

### mutatrum on 2025-07-04

You have to open AxeOS with the IP address, not the hostname. Unfortunately, this is a limitation of the current version. See #657. 

### diegorodriguezv on 2025-07-04

This is a usability bug. Clearly it is unexpected behavior. There are a few possibilities that could make this better:

- The error message could say that you need to use the IP address.
- The system could auto detect the IP address and use it in the links that need it.
- There could be a warning to the user before clicking on a not-working link.

### duckaxe on 2025-07-04

When I first read about this problem on Discord, I thought that I would put a warning on the AxeOS dashboard and tell the user to access AxeOS by IP, not by hostname.

### duckaxe on 2025-07-04

<img width="1295" height="947" alt="Image" src="https://github.com/user-attachments/assets/ee7693d8-0e4e-44d1-8e44-ae3d79464fb5" />

### skot on 2025-07-04

I would like to move the Swarm feature out of AxeOS and into a separate app. AFAIK that would fix this problem.

Until then, this seems like a good warning.

### mutatrum on 2025-07-05

Moving it out into a separate app won't change the CORS issues, I guess? But I never understood why #657 was closed with 'impossible'.

### skot on 2025-07-05

IIUC we have to enable CORS to support Swarm. To prevent CSRF attacks we have esp-miner block everything except whitelisted local IP addresses.

If we remove Swarm from esp-miner (to a separate app) then we can disable CORS and support accessing AxeOS via hostname again.

Alternatively I wonder if it's possible to whitelist the bitaxe's hostname?

### diegorodriguezv on 2025-07-05

Sorry if I'm not getting the point... But I can do:
```curl -X PATCH  -H "Content-Type: application/json" -d '{"hostname": "bitaxe"}' http://bitaxe69/api/system```
So this feature is to protect from attacks within the bitaxe web interface?

### leandro25-cyber on 2025-07-06

Eu comprei um Bitaxe supra hex 701, porém quando pediu pra atualizar o parelho bugou e não ligou mais, fui até o suporte do bitaxe pra atualizar o firmware porém não achei na versão supra hex 701. Alguém pra me ajudar ?

### johnny9 on 2025-07-06


> Alternatively I wonder if it's possible to whitelist the bitaxe's hostname?

It should be possible. I believe when we wrote the network access method we just didn't consider host name.
