# bitaxeorg/ESP-Miner issue #794: Initial page load causes multiple inconsistent GET responses

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/794
> Collected: 2026-10-07
> Published: 2025-03-25

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 794
- State: closed
- Author: etkaar
- Opened: 2025-03-25
- Closed: 2025-04-22
- Labels: bug

## Description

From the developer tools in Firefox I can see that the server sends back the same `/api/theme` response multiple times (7) on an initial page load. The responses are inconsistent, which for instance causes invalid theme settings being sent back to the client. Under some circumstances, that even leads to settings being _changed_ without the user knowing.

(The responses with 875 Bytes are `colorScheme` "dark", the ones with 876 Bytes are "light")

![Image](https://github.com/user-attachments/assets/f4e91e62-3cbb-45c1-b839-5cb774624e3f)

## Comments

### mutatrum on 2025-04-06

~I can't reproduce this, can you try with 2.6.1 or 2.6.2?~

Reading the linked issue now.

I tried reproducing it, but I can't. I only see one complete response of `theme`, then 2 more but they only contain an `ok` messages, not a full payload.

### mutatrum on 2025-04-06

Oh, I can reproduce it, but it's something else. The `payload` is flipping between dark and light, so it's what is being sent from the browser to the backend. That's weird.

### mutatrum on 2025-04-08

Reproduction is easy. Start from the dark theme. Go to Customization, select the Light colorScheme. Then F5 to reload the page. There are 3 requests to `/api/theme`: a `GET` request followed by 2 `POST` requests. The `GET` is fine, the result shows the `light` colorScheme:

![Image](https://github.com/user-attachments/assets/6c38f62d-3f88-4d1a-ab2d-97941ce6c4ca)

But then, the first `POST` _sends_ the following payload:

![Image](https://github.com/user-attachments/assets/86cb201d-2573-405d-a488-89551504ff77)

and the seconds `POST` _sends_ the correct payload:

![Image](https://github.com/user-attachments/assets/24e522d2-aba3-4a01-9076-87d1c7e06523)

However, the setting is reverted to `dark` theme.

Side question: why is there a `theme` and a `colorScheme` field?

### mutatrum on 2025-04-08

I can't follow the Angular code, not sure why there are 2 POSTs. I did remove the `theme` field, which cleans it up a bit but doesn't fix it.

https://github.com/mutatrum/ESP-Miner/commit/0f07a7212b7befcd319023f595566895a2dec9dc

### AxisRay on 2025-04-12

> I can't follow the Angular code, not sure why there are 2 POSTs.

I think the reason is this: the `onConfigUpdate` method in `app.layout.service.ts` automatically saves the config whenever it changes. 
When the page loads, it first uses the default config, and then switches to the nvs config once it's retrieved. 
This triggers `onConfigUpdate` twice, resulting in two POST requests. 
Depending on the order of these two requests, it causes the nvs config to revert back to the default dark theme.

### AxisRay on 2025-04-12

Here's my fix: 
`onConfigUpdate` won't update the nvs config anymore. 
Only clicking the radio button will trigger a refresh of the nvs config.

https://github.com/AxisRay/ESP-Miner/commit/026b64d468ba2b8277514e5dd6208560964c966e

update: Completely removed configUpdate
https://github.com/AxisRay/ESP-Miner/commit/48a8efa1eb607c92014e4ae186bd44ee0ca3ae03

### NilByte on 2025-04-14

I have noticed a theme inconsistency that might be related. 

To replicate, go to Customization menu and then to Dashboard menu. The legend color for ASIC Temp is leight color as expected:

![Image](https://github.com/user-attachments/assets/b117048c-11e0-4a9f-996e-1277e74ba627)

Refresh page and the legend color for ASIC Temp has changed to a darker color:

![Image](https://github.com/user-attachments/assets/b74ac58b-b8d4-4452-91aa-1373923fe7de)

 

### AxisRay on 2025-04-15

It's fixed, but I don't think it's related to this issue.
https://github.com/AxisRay/ESP-Miner/commit/559aba1682d026b03927aa73c0435144595a5a35



### WantClue on 2025-04-17

@AxisRay would you mind PR them to the repo ?

### AxisRay on 2025-04-18

> [@AxisRay](https://github.com/AxisRay) would you mind PR them to the repo ?

Done

### skot on 2025-04-19

(issue closing topic moved to [discussions](https://github.com/bitaxeorg/ESP-Miner/discussions/856))

### etkaar on 2025-04-19

@WantClue Why did you remove the labels _[bug]_ and _[critical]_?

### etkaar on 2025-04-19

Ah – again deleting a comment and suppressing the concerns WantClues behaviour has caused.

Being against censorship as a Bitcoin related project, but of course only as long as it is used by the other side. If you use it yourself, you will always find a reason to justify it to yourself and others.

### WantClue on 2025-04-19

> [@WantClue](https://github.com/WantClue) Why did you remove the labels _[bug]_ and _[critical]_?

It has been pointed out to you earlier on another issue that you opened and that got closed that this behavior is not appearing in general and seems to be an issue on your end. I don't know what your goal of pointing towards me is but this has no room in here.
This behavior is not critical, AxisRay's PR is currently under review.

### etkaar on 2025-04-19

The bug is easily reproducable in a few seconds if you follow my instructions, is reflected in the developer tools in Firefox and Chrome and has already been confirmed by other users. That is why I point toward you, because you're ignoring that and thus interfering with my work. Not only development, also testing and writing reports takes time. If you personally don't want to process bug reports then that's absolutely fine, but then please don't close them for no valid reason.

If you could please accept that, we have no problem. I would kindly ask you to re-add the _[bug]_ flag since this issue is confirmed even if you personally didn't encounter it in your daily use.

### etkaar on 2025-04-25

I can confirm this is now fixed in [v2.7.0b2](https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.7.0b2). Thank you @mutatrum and @AxisRay!
