# bitaxeorg/ESP-Miner issue #833: Building binary files for firmware yourself.

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/833
> Collected: 2026-10-07
> Published: 2025-04-10

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 833
- State: closed
- Author: vaavdeev
- Opened: 2025-04-10
- Closed: 2025-04-16
- Labels: none

## Description

Building binary files for firmware yourself.

I have:
- Bitax Gamma 601
- esp32s3
- Windows 11
- esp-idf-v5.4.1
- Visual Studio Code 1.99.1
- Python 3.11.2
- Noda v22.14.0.
- Ninja version ("1.12.1")
- PowerShell 7.5.0

I cloned the project
https://github.com/bitaxeorg/ESP-Miner

Made a Build Project from the original files.
I didn't change anything.

Received my files:
- www.bin
- esp-miner.bin

www.bin - everything is fine. Its size corresponds to the original developer.
esp-miner.bin - **1 149 KB**. Original file size - **1,163 KB**

There are problems with applying Share deviations on the Dashboard screen.
Problems with displaying Power and input voltage.

The device is mining.

Can you tell me what could be the problem with the build?
Thanks.

## Comments

### skot on 2025-04-10

Did you use bitaxetool to write a cvs file to the ESP32 nvm? Can you post some screenshots of the issue?

### skot on 2025-04-10

Did you use bitaxetool to write a cvs file to the ESP32 nvm? Can you post some screenshots of the issue?

### vaavdeev on 2025-04-11

> Did you use bitaxetool to write a cvs file to the ESP32 nvm? Can you post some screenshots of the issue?

I don't quite understand what you're talking about.
I receive two binary files in my program.
I flash the device in the standard way through the browser.
I upload my files.

I am sending a photo of the problem with displaying parameters.

![Image](https://github.com/user-attachments/assets/a35acbb8-fd49-4ece-aa0f-f5a9ab70760c)

![Image](https://github.com/user-attachments/assets/d3da1982-cd69-494a-98b7-67eace5669c4)

### mutatrum on 2025-04-11

Can you clear the browser cache and reload the page? Might be some old stuff lingering the in browser? Just want to rule out that. I do all my updates through self-built firmware, so they should be ok.

### vaavdeev on 2025-04-11

> Can you clear the browser cache and reload the page? Might be some old stuff lingering the in browser? Just want to rule out that. I do all my updates through self-built firmware, so they should be ok.

Refreshing the page didn't help.
The problem, as I wrote above, is that I am building a binary file different from the size of the original.
I can't help you figure out the reason.

### skot on 2025-04-11

> > Did you use bitaxetool to write a cvs file to the ESP32 nvm? Can you post some screenshots of the issue?
> 
> I don't quite understand what you're talking about.
> I receive two binary files in my program.
> I flash the device in the standard way through the browser.
> I upload my files.
> 
> I am sending a photo of the problem with displaying parameters.
> 
> ![Image](https://github.com/user-attachments/assets/a35acbb8-fd49-4ece-aa0f-f5a9ab70760c)
> 
> ![Image](https://github.com/user-attachments/assets/d3da1982-cd69-494a-98b7-67eace5669c4)

Ah, ok I thought you were flashing a new device.

What version did you have loaded before flashing your own self-built images?

Are you building from a locally cloned git repo? Your version number looks strange.

### ghost on 2025-04-12

@vaavdeev 

VS Code, bottom of the window, do you see this ?

![Image](https://github.com/user-attachments/assets/8d633c8a-cfdb-4179-8e29-2b34e0fd4a76)

### WantClue on 2025-04-16

please move this over to the discussion tab, introduced it today to this repo 🚀
