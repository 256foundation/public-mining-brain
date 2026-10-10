# bitaxeorg/ESP-Miner issue #1573: Bitaxe Gamma 601 shows empty dashboard with firmware 2.13.0 and high error rate with firmware 2.12.2

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1573
> Collected: 2026-10-07
> Published: 2026-02-23

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1573
- State: closed
- Author: mekler22
- Opened: 2026-02-23
- Closed: 2026-02-24
- Labels: none

## Description

Note: Issues are not for customer support, configuration or discussion. For those topics please consult with your HW vendor or the OSMU Discord at: https://osmu.bitaxe.org

**Describe the bug**
I have just received the miner. From the start (it arrived with firmware 2.12.1 if I am not mistaken), as I set it up to run solo mining, it showed **very** high error rate (99.8% - 100.x%). So I have tried to update it to the latest firmware hoping it would resolve the issue. It did not. It actually made it worse as the dashboard was empty with both firmware 2.13.b08 and the final firmware 2.13.0

**To Reproduce**
Steps to reproduce the behavior:
1. configured the miner as per the instructions, through its private wifi network, and connected it to my home network, where it received a local IP.
2. Entered all the pool parameters for solo mining with my BTC address as user (used addresses solo.ckpool.org, ausolo.ckpool.org, and eusolo.ckpool.org for solo mining). saved and restarted.
3. entered the dashboard, and saw the error rate spikes immediately to 99-100+ percent, and fluctuates there.
4. downloaded updated firmware for both the OS and the miner, and installed them. Then post reboot, saw the dashboard as empty with the hourglass (fans logo) turning without any result. tested with a newer firmware (2.13 non beta) and got the same. When I reverted to 2.12.2 I got the original working dashboard but with the errors.

**Expected behavior**
Mining should work without errors, or with a low error rate.

**Screenshots & Photos**

![Image](https://github.com/user-attachments/assets/767a4052-923e-4583-abcd-656293c3b7b1)
![Image](https://github.com/user-attachments/assets/bc5ed07e-47bd-46ec-9517-4de9d1acb8b5)

**Hardware (please complete the following information):**
 - Bitaxe HW version: Gamma 601
 - Bitaxe HW vendor: https://minerfixes.com/ via AliExpress
 - ESP-Miner FW version: 2.12.1 , 2.12.2 , 2.13b08, 2.13.0b1
 - Hash Frequency: 880Gh/s
 - Voltage: 5.1V
 - Pool URL, Port, User: ausolo.ckpool.org:3333 , bc1q7qkmuv9qcyjxjevxgkyy97qde8endysq9xu4zs

**Additional context**
I have played with the frequency and the core voltage - both up and down - other than increase or decreast the hash rate and elevate or reduce the temperature and fan speeds, it made no big difference to the error rate. currently set frequency to 625 and core voltage to 1200 with automatic fan control enabled, target temperature set to 60c and minimum fan speed to 25%


## Comments

### mekler22 on 2026-02-23

I believe I found the solution (at least for the 2.12.2 firmware, as the 2.13 issue is another - so I am not closing this issue), after turning off AI protection in my ASUS router (as per advice from the discord channel), the errors dropped to close to 0, and the miner is mining as it should.

### Notmyprob487-png on 2026-02-24

People who call out wantclue for hacking them and stealing their designs
get banned from the discord. Everyone take a good look at what they are
doing. They're taking an open source project and using the 256 foundation
to centralize the open source project creating a closed source. They say
it's for safety but their products are just as unsafe as the guys made in a
shed. They are fakes. Look at the way they covered up the repos in March of
2025.they covered my involvement in the project. Bitaxeorg/gamma has me as
the first author justnate787-lang. This project is as big as it is because
of my work. Anyone who wants the Truth get ahold of me before you are
locked into a product that is proprietary.

On Mon, Feb 23, 2026, 6:49 PM mekler22 ***@***.***> wrote:

> *mekler22* left a comment (bitaxeorg/ESP-Miner#1573)
> <https://github.com/bitaxeorg/ESP-Miner/issues/1573#issuecomment-3947994329>
>
> I believe I found the solution (at least for the 2.12.2 firmware, as the
> 2.13 issue is another - so I am not closing this issue), after turning off
> AI protection in my ASUS router (as per advice from the discord channel),
> the errors dropped to close to 0, and the miner is mining as it should.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/bitaxeorg/ESP-Miner/issues/1573#issuecomment-3947994329>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/BVQGA6PQW7NUZGJFCOPN2DT4NOGZ7AVCNFSM6AAAAACV4JRZH6VHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZTSNBXHE4TIMZSHE>
> .
> You are receiving this because you are subscribed to this thread.Message
> ID: ***@***.***>
>


### WantClue on 2026-02-24

Good that you found the issue. These asus routers have a history of blocking averything mining related
