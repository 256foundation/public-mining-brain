# bitaxeorg/ESP-Miner issue #993: Unable to reach Minimize Logs button once the log text fills the screen

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/993
> Collected: 2026-10-07
> Published: 2025-05-31

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 993
- State: closed
- Author: xr1140
- Opened: 2025-05-31
- Closed: 2025-06-27
- Labels: none

## Description


The ‘Minimize Logs’ button should remain visible on the screen at all times. Currently, when the screen fills with log text, the button disappears from the visible area of the browser and is difficult to access. It would be helpful for the button to stay on the screen permanently, and for the ESC key to function as an equivalent to clicking it.

The ‘Stop Scrolling’ button should also remain visible on the screen at all times.

## Comments

### ghost on 2025-06-01

I agree, these need to be set to "float" in the top right corner.



### duckaxe on 2025-06-01

I tested the close button several times bevor PR. Now I tested the button again and it works as expected. Have you guys tried it on desktop or mobile?

https://github.com/user-attachments/assets/d928dfbd-eae8-4f09-b1e1-0356e11a68fd

### ghost on 2025-06-01

@duckAxe 

Desktop - Chrome - Fullscreen, the icon does not float top right, pain to get to it as well after some time.

![Image](https://github.com/user-attachments/assets/fa42ade1-ddce-4c4a-8322-044c6c9a176c)

Here is fine, just not in "fullscreen" mode

![Image](https://github.com/user-attachments/assets/a82e52a3-0a9b-47c1-a8b0-2cb9c3a9519c)

Could also do with having the stop / start button there too in fullscreen mode.

Could you update your ESP-IDF Version to v5.4.1 as well. 

### duckaxe on 2025-06-01

The only difference between me and you: Windows. Unfortunately, I don't have Windows to test ;(

### ghost on 2025-06-01

I tested this on my android phone, when in fullscreen mode the icon does not "float" in the top right corner, it stays at the top and goes out of view when there is a lot of data presented, it needs to be made as an 'overlay' and stay visible, same with 'Stop Scrolling / Start Scrolling' which is missing there at the moment.

![Image](https://github.com/user-attachments/assets/ae1134f3-806a-4c0a-97c8-4f58e1fe0f4f)

### ghost on 2025-06-01

Set as an 'overlay' in this example (mockup) so they stay visible on the screen.

![Image](https://github.com/user-attachments/assets/45519de7-e370-4ccc-960f-3bf2b234a85c)

### xr1140 on 2025-06-01

on Android, both Chrome and Brave - the button leaves
on Windows, on Chrome - the button leaves

### duckaxe on 2025-06-02

I can't fix things until I can reproduce them on my local environment. I have just tested on Firefox and Chrome, works. 😢

### ghost on 2025-06-02

Watch the video, the icon in the top right corner goes out of view, does not float and stay visible to click on to minimize it, I have the same issue on my android phone as well.

https://github.com/user-attachments/assets/4ed6fa29-dcd5-4d08-bdfa-41751e67bf58

### xr1140 on 2025-06-02

@duckAxe maybe would work (without crossplatform testing) if you stick the buttons (add "stop scrolling" too) at the bottom of the windows instead of top.

### duckaxe on 2025-06-02

Thank you guys for help. I definitely need a real Bitaxe, not just a local environment ;)
The PR #1000 ✅ is your friend.

### duckaxe on 2025-06-03

@skot Thank you. After my comment I ordered a cheap Gamma on AE ;)

### WantClue on 2025-06-27

fixed in #1000
