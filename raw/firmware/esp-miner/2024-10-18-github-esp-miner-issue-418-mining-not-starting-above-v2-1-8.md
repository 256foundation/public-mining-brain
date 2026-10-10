# bitaxeorg/ESP-Miner issue #418: Mining not starting above V2.1.8

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/418
> Collected: 2026-10-07
> Published: 2024-10-18

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 418
- State: closed
- Author: mountainlove
- Opened: 2024-10-18
- Closed: 2024-11-28
- Labels: none

## Description

Up to V2.1.8 there were no problems to connect to "sha256.poolbinance.com". Every FW Version above is not working anymore on this pool. Log:

<img width="675" alt="Screenshot 2024-10-18 111841" src="https://github.com/user-attachments/assets/33bba72f-ab21-4ade-b8a8-79ea4a924680">


## Comments

### skot on 2024-10-18

Interesting... from your screenshot it looks like it's working. can you provide more log output; ideally starting earlier on?

### mountainlove on 2024-10-20

Sure. Also found something interesting.

With V2.1.8, everything works like expected:

<img width="601" alt="V2 1 8_1" src="https://github.com/user-attachments/assets/8584c0a8-c472-452c-af9c-b985549e450d">
<img width="617" alt="V2 1 8_2" src="https://github.com/user-attachments/assets/7adbc3a8-652e-43bf-9a96-8c10b8694570">
<img width="635" alt="V2 1 8_3" src="https://github.com/user-attachments/assets/81878d48-6a51-4f9c-b02d-f1a4a855d997">
<img width="311" alt="V2 1 8_4" src="https://github.com/user-attachments/assets/cf75cde9-7a26-476d-ac1a-0109378a8232">

When i upgrade the Firmware without any Powercycle, i'm able to mining on with V2.3.0 (or any other above 2.1.8):

<img width="649" alt="V2 3 0_pwr_1" src="https://github.com/user-attachments/assets/c2a5721f-acda-4abd-9458-edab2c320a97">
<img width="647" alt="V2 3 0_pwr_2" src="https://github.com/user-attachments/assets/c9c67084-2f65-491c-a358-905b93346a50">
<img width="493" alt="V2 3 0_pwr_3" src="https://github.com/user-attachments/assets/d40453b7-1a9e-46cc-9925-c14e41fc5356">

And after a complete reboot with taking away the Power, the Miner i stucking in that Loop from the first post:

<img width="644" alt="V2 3 0_1" src="https://github.com/user-attachments/assets/fdce32a3-750c-4ce8-962e-b916e74da604">
<img width="646" alt="V2 3 0_2" src="https://github.com/user-attachments/assets/ccdf02ef-e7b5-48c2-8e3a-8d7761001edf">
<img width="652" alt="V2 3 0_3" src="https://github.com/user-attachments/assets/721823e2-cef5-482b-88bd-c3063a19a2d6">

Connection is:
sha256.poolbinance.com / port 8888

Thank you.

### sstativa on 2024-10-21

I had something similar in the past, nothing worked for me except 2.1.8.
Playing around with new firmware I "bricked" my miner and had to flash v2.1.10 using Python via serial port.
This has not only "unbricked" my miner but also fixed issues I had with 2.1.10 in the past. 
Currently, I installed 2.3.0 via Web UI and it works without issues.

### mountainlove on 2024-10-21

I had also to reflash my miner with v2.1.10 first (with wantclue web-flasher). Then i followed similar steps as @sstativa, but i had no Luck to get it mining. For me only a Downgrade to v2.1.8 helps.

### matlen67 on 2024-10-21

Which bitaxe is it? Or is it a LuckyMiner?

### LupusPluvia on 2024-11-23

I have the same problem. It was previously on version 2.3.0. I wanted to update to 2.4.0. It didn't work anymore. I went back to 2.3.0. It doesn't work anymore either. Anything above 2.1.8 doesn't work either. With version 2.1.8 it only takes a few hours and then you have to restart it to get it running again. It's a (Lucky miner lv 6 ) 

The other lucky miner that I haven't touched is still running stable on 2.3.0.

### skot on 2024-11-23

esp-miner does not (and will not) support luckyminer.

### LupusPluvia on 2024-11-23

Thank you! Für die info

### sstativa on 2024-11-28

I run 2.4.0 on LuckyMiner LV06 without issues.
