# bitaxeorg/ESP-Miner issue #83: Release v2.0.5 froze during www.bin load. Now the miner won't start up.

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/83
> Collected: 2026-10-07
> Published: 2024-01-10

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 83
- State: closed
- Author: scoaste
- Opened: 2024-01-10
- Closed: 2024-01-15
- Labels: question

## Description

Bitaxe Ultra miner was at v2.0.4.  Downloaded the esp-miner.bin & www.bin files for v2.0.5 to my local PC.  Went to the settings tab and uploaded the esp-miner.bin file.  Attempted to load the www.bin file.  After 2% it froze and never resumed after several minutes.  I attempted to refresh the page and the site was not longer accessible.  I hard-booted the miner and it doesn't come back up.  Now what?

## Comments

### benjamin-wilson on 2024-01-13

Which version bitaxe do you have, who made it and what version were you updating from?

### scoaste on 2024-01-13

Bitaxe Ultra from D-Central.  Came with v2.0.0.  I upgraded to v2.0.4 with
no issues.  v2.0.5 of esp-miner.bin appeared to upload without issue, but
www.bin froze.  They provided me with a rough guide to flash via bitaxetool
(link below).  I flashed the esp-miner again but don't know what to do with
www.bin which seems to be the problem.

https://d-central.tech/troubleshooting/bitaxe-troubleshooting-guide-solving-operational-challenges/

I translated the above to these:

# install pip, pipx, and bitaxetool (needs its own environment)
sudo aptitude install python3-pip -vy
sudo aptitude install pipx -vy
pipx install bitaxetool

# download bin files, config file example, change to that directory
# modify config
cp config.cvs.example  config.cvs
vi config.cvs

# connect USB, get port, execute flash command
ls -lart /dev/tty*
sudo /home/$USER/.local/bin/bitaxetool -p /dev/ttyACM0 -c ./config.cvs -f
./esp-miner.bin

Regards,
Scott




On Sat, Jan 13, 2024, 1:48 PM Benjamin Wilson ***@***.***>
wrote:

> Which version bitaxe do you have, who made it and what version were you
> updating from?
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/skot/ESP-Miner/issues/83#issuecomment-1890751125>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AGN2YQQ5KFPTWITOWWYOPRDYOLQH5AVCNFSM6AAAAABBVNR2OCVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMYTQOJQG42TCMJSGU>
> .
> You are receiving this because you authored the thread.Message ID:
> ***@***.***>
>


### WantClue on 2024-01-15

Hey Scott,

if your Bitaxe failes during the update process, the partition might be bricked and needs to be reflashed using the bitaxetool or the espressif software.
You can also watch videos about how to do this on my channel. Or follow the guide in the bitaxe repo. 

With this information now, I do close this issue labeled as a question. 

### scoaste on 2024-01-15

As I noted in my previous email, bitaxetool does not solve the problem,
probably because the esp-miner.bin updates without apparent issue, whereas
the www.bin seems to be the cause (i.e
where it froze).

On Mon, Jan 15, 2024, 4:54 AM WantClue ***@***.***> wrote:

> Hey Scott,
>
> if your Bitaxe failes during the update process, the partition might be
> bricked and needs to be reflashed using the bitaxetool or the espressif
> software.
> You can also watch videos about how to do this on my channel. Or follow
> the guide in the bitaxe repo.
>
> With this information now, I do close this issue labeled as a question.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/skot/ESP-Miner/issues/83#issuecomment-1891891303>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AGN2YQSCCMRGF7JIHBWTIP3YOUDH3AVCNFSM6AAAAABBVNR2OCVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMYTQOJRHA4TCMZQGM>
> .
> You are receiving this because you authored the thread.Message ID:
> ***@***.***>
>


### scoaste on 2024-01-15

This command worked:

sudo /home/$USER/.local/bin/bitaxetool -p /dev/ttyACM0 -c ./config.cvs
-f *./esp-miner-factory-v2.0.6.bin
*

On Mon, Jan 15, 2024 at 11:17 AM Scott Steimle ***@***.***> wrote:

> As I noted in my previous email, bitaxetool does not solve the problem,
> probably because the esp-miner.bin updates without apparent issue, whereas
> the www.bin seems to be the cause (i.e
> where it froze).
>
> On Mon, Jan 15, 2024, 4:54 AM WantClue ***@***.***> wrote:
>
>> Hey Scott,
>>
>> if your Bitaxe failes during the update process, the partition might be
>> bricked and needs to be reflashed using the bitaxetool or the espressif
>> software.
>> You can also watch videos about how to do this on my channel. Or follow
>> the guide in the bitaxe repo.
>>
>> With this information now, I do close this issue labeled as a question.
>>
>> —
>> Reply to this email directly, view it on GitHub
>> <https://github.com/skot/ESP-Miner/issues/83#issuecomment-1891891303>,
>> or unsubscribe
>> <https://github.com/notifications/unsubscribe-auth/AGN2YQSCCMRGF7JIHBWTIP3YOUDH3AVCNFSM6AAAAABBVNR2OCVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMYTQOJRHA4TCMZQGM>
>> .
>> You are receiving this because you authored the thread.Message ID:
>> ***@***.***>
>>
>
