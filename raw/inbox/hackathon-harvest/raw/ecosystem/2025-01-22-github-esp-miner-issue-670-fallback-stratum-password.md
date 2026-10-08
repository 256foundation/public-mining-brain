# bitaxeorg/ESP-Miner issue #670: Fallback Stratum Password

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/670
> Collected: 2026-10-07
> Published: 2025-01-22

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 670
- State: closed
- Author: matlen67
- Opened: 2025-01-22
- Closed: 2026-05-29
- Labels: question

## Description

I currently use the stratum fallback to switch between different pools. To switch to the fallback, I change the URL of the first stratum host and save the setting, then I restart the mine by means of a reset. After the restart, the fallback is used because the server IP was not found. It looks as if the assigned fallback stratum password is not read out and entered in the password field when the Settings page is opened, but the string 'password' is entered here, which is then accepted after saving. However, I have saved the difficulty . Example password: d=1200

![Image](https://github.com/user-attachments/assets/fbbab8fb-fd4e-489a-9cca-29d318ab37f6)



## Comments

### w3irdrobot on 2025-02-21

it appears we always [set that form field's value to "password"](https://github.com/skot/ESP-Miner/blob/b21cd505048dd5fc3059901e1fd312834af82741/main/http_server/axe-os/src/app/components/pool/pool.component.ts#L56) when the form loads, regardless of if it was set once before. however, unlike the `stratumPassword` field that [is excluded when its value is not changed](https://github.com/skot/ESP-Miner/blob/b21cd505048dd5fc3059901e1fd312834af82741/main/http_server/axe-os/src/app/components/pool/pool.component.ts#L64-L66), this `fallbackStratumPassword` default value will be used if the form is submitted again without changing its value again. this seems like less than ideal functionality. 

it would probably benefit us to exclude this field if unchanged as well. I can do this work if the powers that be want it done.

### skot on 2025-02-21

I thought we changed this to set the password to "******"? Was this just WiFi? There was a bug when someone's password actually was "password"

### w3irdrobot on 2025-02-21

it looks like we do it for the stratum password and [the wifi password](https://github.com/skot/ESP-Miner/blob/b21cd505048dd5fc3059901e1fd312834af82741/main/http_server/axe-os/src/app/components/network-edit/network.edit.component.ts#L61) but not the backup stratum password. 

### WantClue on 2026-05-29

This should no longer be the case, this should have been addressed. If this is still the case please reopen an issue
