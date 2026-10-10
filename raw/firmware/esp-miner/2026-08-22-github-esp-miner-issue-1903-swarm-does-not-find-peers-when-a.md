# bitaxeorg/ESP-Miner issue #1903: Swarm does not find peers when accessed via web address vs IP address

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1903
> Collected: 2026-10-07
> Published: 2026-08-22

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1903
- State: closed
- Author: scul86
- Opened: 2026-08-22
- Closed: 2026-09-14
- Labels: none

## Description

Note: Issues are not for customer support, configuration or discussion. For those topics please consult with your HW vendor or the OSMU Discord at: https://osmu.bitaxe.org

**Describe the bug**
Swarm page is not able to find peer bitaxe or nerdQaxe when Bitaxe is accessed via web address in TLD of **.lan** (ie http://bitaxe-gamma-0.lan ).  If I manually type in the peer address (bitaxe-gamma-1.lan), the *Add* button is disabled.  Also, if I enter the IP address directly, there is an error that pops up (see picture in screenshot section).

Seems that if I attempt to add a peer via webaddress that has TLD of **.local**, the *Add* button is enabled.

When pool is access via IP address, the peers are automatically found as expect.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to bitaxe swarm page accessed via web address (ie http://bitaxe-gamma-0.lan )
2. Click on autoscan
3. No peer BitAxe or NerdQAxe are found
4. Attempt to add peer on swarm page
4.1. Cannot add peer via web address
4.2. Error when attempting to add peer via IP address

**Expected behavior**
Peers on the network are automatically found, **.lan** TLD enabled for manual peer addition.

**Screenshots & Photos**
[Can't add via web address](https://i.imgur.com/qgy8akJ.png)
[Error when adding via IP address (peer BitAxe is upgrade to 2.15.0 also)](https://i.imgur.com/99kFYdy.png)


**Hardware (please complete the following information):**
 - Bitaxe HW version: BitAxe Gamma 601 and 602
 - Bitaxe HW vendor: 601 - unknown.  602 - SoloSatoshi
 - ESP-Miner FW version: 2.15.0
 - Hash Frequency:
 - Voltage:
 - Pool URL, Port, User:

**Additional context**
Add any other context about the problem here.


## Comments

### mutatrum on 2026-08-24

Can you share a screenshot?

This is how it looks for me. First this:
<img width="1926" height="372" alt="Image" src="https://github.com/user-attachments/assets/e8fe19a7-508c-484b-85fb-427810c5bd0f" />

And after 10 seconds or so:
<img width="1924" height="905" alt="Image" src="https://github.com/user-attachments/assets/848f8fc0-1a79-4a0b-b443-23079f9f66e5" />

Make sure the dashboard page is fully refreshed, IIRC the text on the scan screen has changed in 2.15, so you should be able to see if it's updated or not. Sometimes the browser cache can be stubborn.

### scul86 on 2026-08-25

Lots of screenshots here, tried to be descriptive in them.

Accessed via web address, and waited for ~90 seconds:

<img width="2560" height="1600" alt="Image" src="https://github.com/user-attachments/assets/84196306-947c-41d5-a444-42cdc8f6f400" />

After clicking the "scan" button.  Only NerdMiners (shameful, I know) were found via scan:

<img width="2560" height="1600" alt="Image" src="https://github.com/user-attachments/assets/4089e3f0-4de9-498c-af5a-e1a51238e379" />

Attempt to add Bitaxe-Gamma-1 as a peer via web address.  'Add' button disabled:

<img width="2560" height="1600" alt="Image" src="https://github.com/user-attachments/assets/d673c9b2-d943-4d04-95f1-a9bae3561259" />

Change TLD to `.local`, and 'Add' button is enabled.  Wrong TLD for my LAN, however. 
(_Just thought to **actually** click 'Add'... same error as next picture, even though if I navigate to the .local address, I get a 'server not found' from FireFox._)

<img width="2560" height="1600" alt="Image" src="https://github.com/user-attachments/assets/56f4f085-eb72-44c4-90ab-67ae3ec716af" />

Attempt to add peer via IP Address - error:

<img width="2560" height="1600" alt="Image" src="https://github.com/user-attachments/assets/a330748f-9356-4b65-841f-4d42d3b89b86" />

Other Bitaxe is updated:

<img width="2560" height="1600" alt="Image" src="https://github.com/user-attachments/assets/8941028a-5d8c-4ac2-af85-125f458f78e0" />

When accessed initially via IP Address, everything works as expected, and peers found as soon as I accessed the swarm page:

<img width="2560" height="1600" alt="Image" src="https://github.com/user-attachments/assets/023b0599-4440-4c2e-a574-7fa7810731ec" />

### mutatrum on 2026-08-25

Can you try to access the dashboard without TLD, just hostname?

### scul86 on 2026-08-25

Cannot access bitaxe with `.local` TLD:
```
Server Not Found
Firefox can’t connect to the server at bitaxe-gamma-0.local.
```

Hostname only:

<img width="2560" height="1600" alt="Image" src="https://github.com/user-attachments/assets/ebfec6ee-a7da-4c2d-8db2-d09ce923e48e" />
