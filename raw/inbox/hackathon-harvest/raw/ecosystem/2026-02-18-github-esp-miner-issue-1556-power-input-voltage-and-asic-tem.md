# bitaxeorg/ESP-Miner issue #1556: Power, Input Voltage, and ASIC Temp not showing

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1556
> Collected: 2026-10-07
> Published: 2026-02-18

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1556
- State: closed
- Author: jdmcroy
- Opened: 2026-02-18
- Closed: 2026-02-18
- Labels: none

## Description

Note: Issues are not for customer support, configuration or discussion. For those topics please consult with your HW vendor or the OSMU Discord at: https://osmu.bitaxe.org

**Describe the bug**
After updating to v2.13.0b8 the dashboard doesn't show Power, Input Voltage, and ASIC Temp data

**To Reproduce**
Steps to reproduce the behavior:
1. Install v2.13.0b8
2. Go to dashboard page
3. See no Power, Input Voltage, and ASIC Temp  data showing


**Expected behavior**
Expect to see Power, Input Voltage, and ASIC Temp data displayed on dashboard page.

**Screenshots & Photos**
If applicable, add AxeOS screenshots and/or photos of your Bitaxe to help explain your problem.

**Hardware (please complete the following information):**
 - Bitaxe HW version: 800 Gamma Turbo
 - Bitaxe HW vendor: Amazon vendor - vnish

![Image](https://github.com/user-attachments/assets/dcabd2d7-ae63-4b58-b0c5-c5ca7f0722d9)

 - ESP-Miner FW version: v2.13.0b8
 - Hash Frequency: 600
 - Voltage: 1200
 - Pool URL, Port, User: solo.ckpool.org, 3333, 3GCi32MAesPCm5nzTDambSoiu4zuSeH3uR.My-Bitaxe-1

**Additional context**
v2.13.0b1 works but every beta release after that has this issue.


## Comments

### jdmcroy on 2026-02-18

Closing as it is a duplicate. See https://github.com/bitaxeorg/ESP-Miner/issues/1521#issuecomment-3787400158 for context.

### jayjaywoo2 on 2026-02-26

V211.1 TCH IS THE VERSION YOUR LOOKING FOR !!  i myself accidently updated the firm =ware on my 800 Bitaxe Gt 1 At this time i havent figured out a away of fixing the display! i was hoping you found a solution? someone told me to hook up usb and revert to old firmware. i havent figured out yet if thats possible. good luck please respond if you figure out a fix. 
 thank you 

### jdmcroy on 2026-03-02

> V211.1 TCH IS THE VERSION YOUR LOOKING FOR !! i myself accidently updated the firm =ware on my 800 Bitaxe Gt 1 At this time i havent figured out a away of fixing the display! i was hoping you found a solution? someone told me to hook up usb and revert to old firmware. i havent figured out yet if thats possible. good luck please respond if you figure out a fix. thank you

I went to the vendor and got their dirty version of 2.12.2 that worked on my 800xxx units. You can also use the bitaxetool like so and load the current production release. It should work also if you load the current 801 config file. This will put your settings back to factory, so you'll need to change them with the miner UI to you specific settings.
bitaxetool --config config-801.cvs --firmware esp-miner-factory-801-v2.13.0.bin

### jdmcroy on 2026-03-17

I went to the vendor and got their dirty version of 2.12.2 that worked on
my 800xxx units.

You can also use the bitaxetool to load the current production release. It
should work if you load the current 801 config file. This will put your
settings back to factory, so you'll need to change them with the miner UI
to you specific settings.
bitaxetool --config config-801.cvs --firmware
esp-miner-factory-801-v2.13.0.bin

On Wed, Feb 25, 2026 at 8:48 PM jayjaywoo2 ***@***.***> wrote:

> *jayjaywoo2* left a comment (bitaxeorg/ESP-Miner#1556)
> <https://github.com/bitaxeorg/ESP-Miner/issues/1556#issuecomment-3963395286>
>
> V211.1 TCH IS THE VERSION YOUR LOOKING FOR !! i myself accidently updated
> the firm =ware on my 800 Bitaxe Gt 1 At this time i havent figured out a
> away of fixing the display! i was hoping you found a solution? someone told
> me to hook up usb and revert to old firmware. i havent figured out yet if
> thats possible. good luck please respond if you figure out a fix.
> thank you
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/bitaxeorg/ESP-Miner/issues/1556#issuecomment-3963395286>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AB6ANZSUUDXCTSTN6QG6SLT4NZGF7AVCNFSM6AAAAACVSG455SVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZTSNRTGM4TKMRYGY>
> .
> You are receiving this because you modified the open/close state.Message
> ID: ***@***.***>
>
