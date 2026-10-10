# bitaxeorg/ESP-Miner issue #1350: after 2.11.0b6, reading "http://192.168.5.105/api/system/info" response throws an error

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1350
> Collected: 2026-10-07
> Published: 2025-11-13

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1350
- State: closed
- Author: EricDimitri
- Opened: 2025-11-13
- Closed: 2026-06-02
- Labels: none

## Description

I was using some automation to restart bitaxe gamma 601 if hashrate was the same for n consnecutive times.

Now, after that beta version installed, when I am tryign to deserialize JSON i get this 

"Deserialize JSON 105: Input string '96.758674621582031' is not a valid integer. Path 'fanspeed', line 68, position 31." 

HAve you changed anything there?

I cant figure out what is wrong...

Thanks!!

LEts clarify that I did 0 change in the code. It was working fine, and started throwing that error on the beta version stated.

   Eric

## Comments

### jns-codeworks on 2025-11-13

There was a commit regarding the fan speed: [ Fix manual fan speed setting #1331 ](https://github.com/bitaxeorg/ESP-Miner/pull/1331) . 
Perhaps it has something to do with that. However, if you look at the code the fanspeed number seems to be still of type integer, which is also the type that is listed in the openapi.yaml for fanspeed.


### EricDimitri on 2025-11-13

> There was a commit regarding the fan speed: [ Fix manual fan speed setting #1331 ](https://github.com/bitaxeorg/ESP-Miner/pull/1331) . Perhaps it has something to do with that.

I saw the changes, and I dont see how that could affect but, for sure something happened, since I had the bot running, until updated to the beta version, then it started throwing that error :(

### mutatrum on 2025-11-15

There's also #1334, but AFAIK what's in the `fanspeed` field on the info endpoint hasn't changed. It's a bit messy that so many digits are printed in that number, maybe that triggered an error in the script?

What could help is if you show the output of the info endpoint on this version, and then out an older firmware on which was working, to double check. You can remove any fields you don't want public, of course.

### remcoros on 2025-11-15

If I had to take a guess: this commit https://github.com/bitaxeorg/ESP-Miner/commit/8919d020e5e26d45484adaba503fdc5444bbf4e3#diff-96479524377a73d94d656d0f0f886a6627af526461da3f9dd2e90095384cf6afR224-R260 removed the cast to uint, so it now keeps the decimal numbers, and your script assumes it's an integer, while it's actually a floating point number.

### EricDimitri on 2025-11-15

> If I had to take a guess: this commit [8919d02#diff-96479524377a73d94d656d0f0f886a6627af526461da3f9dd2e90095384cf6afR224-R260](https://github.com/bitaxeorg/ESP-Miner/commit/8919d020e5e26d45484adaba503fdc5444bbf4e3#diff-96479524377a73d94d656d0f0f886a6627af526461da3f9dd2e90095384cf6afR224-R260) removed the cast to uint, so it now keeps the decimal numbers, and your script assumes it's an integer, while it's actually a floating point number.

Yeah, but the thing is, I changed nothing in the code, and the problem is inside a "deserialize json" function I am calling... so there nothing I can do to fix that... 

### remcoros on 2025-11-15

> > If I had to take a guess: this commit [8919d02#diff-96479524377a73d94d656d0f0f886a6627af526461da3f9dd2e90095384cf6afR224-R260](https://github.com/bitaxeorg/ESP-Miner/commit/8919d020e5e26d45484adaba503fdc5444bbf4e3#diff-96479524377a73d94d656d0f0f886a6627af526461da3f9dd2e90095384cf6afR224-R260) removed the cast to uint, so it now keeps the decimal numbers, and your script assumes it's an integer, while it's actually a floating point number.
> 
> Yeah, but the thing is, I changed nothing in the code, and the problem is inside a "deserialize json" function I am calling... so there nothing I can do to fix that...

How does your deserializing code look? It's trying to deserialize to an 'integer', which is not possible if it's a floating point number. Depending on the language you use, you should use a floating point type (float / double, not 'integer')

### EricDimitri on 2025-11-15

> There's also [#1334](https://github.com/bitaxeorg/ESP-Miner/pull/1334), but AFAIK what's in the `fanspeed` field on the info endpoint hasn't changed. It's a bit messy that so many digits are printed in that number, maybe that triggered an error in the script?
> 
> What could help is if you show the output of the info endpoint on this version, and then out an older firmware on which was working, to double check. You can remove any fields you don't want public, of course.

Ok, here we go. You will see in the 

> > > If I had to take a guess: this commit [8919d02#diff-96479524377a73d94d656d0f0f886a6627af526461da3f9dd2e90095384cf6afR224-R260](https://github.com/bitaxeorg/ESP-Miner/commit/8919d020e5e26d45484adaba503fdc5444bbf4e3#diff-96479524377a73d94d656d0f0f886a6627af526461da3f9dd2e90095384cf6afR224-R260) removed the cast to uint, so it now keeps the decimal numbers, and your script assumes it's an integer, while it's actually a floating point number.
> > 
> > 
> > Yeah, but the thing is, I changed nothing in the code, and the problem is inside a "deserialize json" function I am calling... so there nothing I can do to fix that...
> 
> How does your deserializing code look? It's trying to deserialize to an 'integer', which is not possible if it's a floating point number. Depending on the language you use, you should use a floating point type (float / double, not 'integer')

I cant do nothing... I am using Uipath. the "deserialize JSON"
  is an internal fucntion that i dont have access to the code... I guess there must b something there that tells the deserialize what type of data each field is, and how to cast, but I know nothing about this so, I am not that helpful :(

### EricDimitri on 2025-11-15

> There's also [#1334](https://github.com/bitaxeorg/ESP-Miner/pull/1334), but AFAIK what's in the `fanspeed` field on the info endpoint hasn't changed. It's a bit messy that so many digits are printed in that number, maybe that triggered an error in the script?
> 
> What could help is if you show the output of the info endpoint on this version, and then out an older firmware on which was working, to double check. You can remove any fields you don't want public, of course.

Ok, here it goes... first is the WORKING one with version 2.10.1 Second one is crashing one, with 2.11.0b6

{
	"power":	30.587522506713867,
	"voltage":	4968.75,
	"current":	20031.25,
	"temp":	63,
	"temp2":	0,
	"vrTemp":	68,
	"maxPower":	40,
	"nominalVoltage":	5,
	"hashRate":	1658.6653179715183,
	"expectedHashrate":	1632,
	"bestDiff":	"572.14 M",
	"bestSessionDiff":	"11.90 M",
	"poolDifficulty":	1000,
	"isUsingFallbackStratum":	0,
	"isPSRAMAvailable":	1,
	"freeHeap":	8381900,
	"coreVoltage":	1280,
	"coreVoltageActual":	1248,
	"frequency":	800,
	"ssid":	"XXXX",
	"macAddr":	"XX:XX:XX:XX:XX:XX",
	"hostname":	"bitaxe 105",
	"wifiStatus":	"Connected!",
	"wifiRSSI":	-69,
	"apEnabled":	0,
	"sharesAccepted":	14,
	"sharesRejected":	0,
	"sharesRejectedReasons":	[],
	"uptimeSeconds":	132,
	"smallCoreCount":	2040,
	"ASICModel":	"BM1370",
	"stratumURL":	"public-pool.io",
	"stratumPort":	21496,
	"stratumUser":	"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.bitaxe 01",
	"stratumSuggestedDifficulty":	1000,
	"stratumExtranonceSubscribe":	0,
	"fallbackStratumURL":	"solo.ckpool.org",
	"fallbackStratumPort":	3333,
	"fallbackStratumUser":	"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.bitaxe 01",
	"fallbackStratumSuggestedDifficulty":	1000,
	"fallbackStratumExtranonceSubscribe":	0,
	"responseTime":	253.353,
	"version":	"v2.10.1",
	"axeOSVersion":	"v2.10.1",
	"idfVersion":	"v5.5",
	"boardVersion":	"601",
	"runningPartition":	"ota_1",
	"overheat_mode":	0,
	"overclockEnabled":	1,
	"display":	"SSD1306 (128x32)",
	"rotation":	0,
	"invertscreen":	0,
	"displayTimeout":	-1,
	"autofanspeed":	1,
	"fanspeed":	78,
	"minFanSpeed":	30,
	"temptarget":	62,
	"fanrpm":	3428,
	"statsFrequency":	0
}



{
	"power":	30.62738037109375,
	"voltage":	4960.9375,
	"current":	20062.5,
	"temp":	62.75,
	"temp2":	-1,
	"vrTemp":	69,
	"maxPower":	40,
	"nominalVoltage":	5,
	"hashRate":	1620.061767578125,
	"expectedHashrate":	1632,
	"errorPercentage":	0.31813362240791321,
	"bestDiff":	572141152,
	"bestSessionDiff":	45037351,
	"poolDifficulty":	16384,
	"isUsingFallbackStratum":	0,
	"poolAddrFamily":	2,
	"isPSRAMAvailable":	1,
	"freeHeap":	8211800,
	"freeHeapInternal":	103363,
	"freeHeapSpiram":	8140408,
	"coreVoltage":	1280,
	"coreVoltageActual":	1275,
	"frequency":	800,
	"ssid":	"XXXX",
	"macAddr":	"XX:XX:XX:XX:XX:XX",
	"hostname":	"bitaxe 105",
	"ipv4":	"192.168.5.105",
	"ipv6":	"XXXX::XXXX:XXXX:XXXX:XXXX",
	"wifiStatus":	"Connected!",
	"wifiRSSI":	-68,
	"apEnabled":	0,
	"sharesAccepted":	2500,
	"sharesRejected":	5,
	"sharesRejectedReasons":	[{
			"message":	"Job not found",
			"count":	5
		}],
	"uptimeSeconds":	92290,
	"smallCoreCount":	2040,
	"ASICModel":	"BM1370",
	"stratumURL":	"public-pool.io",
	"stratumPort":	21496,
	"stratumUser":	"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.bitaxe 01",
	"stratumSuggestedDifficulty":	1000,
	"stratumExtranonceSubscribe":	0,
	"fallbackStratumURL":	"solo.ckpool.org",
	"fallbackStratumPort":	3333,
	"fallbackStratumUser":	"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.bitaxe 01",
	"fallbackStratumSuggestedDifficulty":	1000,
	"fallbackStratumExtranonceSubscribe":	0,
	"responseTime":	251.439,
	"version":	"v2.11.0b6",
	"axeOSVersion":	"v2.11.0b6",
	"idfVersion":	"v5.5.1",
	"boardVersion":	"601",
	"runningPartition":	"ota_0",
	"overheat_mode":	0,
	"overclockEnabled":	1,
	"display":	"SSD1306 (128x32)",
	"rotation":	0,
	"invertscreen":	0,
	"displayTimeout":	-1,
	"autofanspeed":	1,
	"fanspeed":	100,
	"manualFanSpeed":	74,
	"minFanSpeed":	30,
	"temptarget":	62,
	"fanrpm":	3419,
	"fan2rpm":	0,
	"statsFrequency":	0,
	"blockFound":	0,
	"blockHeight":	923765,
	"scriptsig":	"Public-Pool",
	"networkDifficulty":	152271405447597,
	"hashrateMonitor":	{
		"asics":	[{
				"total":	1620.061767578125,
				"domains":	[390.84201049804688, 428.63775634765625, 409.73989868164062, 389.9830322265625],
				"errorCount":	170846
			}]
	}
}

Please share your thoughts.

THANKS A LOT!!!!

    ERic

### remcoros on 2025-11-15

In both responses, 'fanspeed' doesn't contain any decimal numbers, so I'm not sure what's going on. A bug in UiPath maybe? I don't know UiPath, so not sure about that.

But this message: "Deserialize JSON 105: Input string '96.758674621582031' is not a valid integer." is very clear, it should not be parsed as an integer, but as a floating point number.

You'll have to figure out why UiPath is trying to deserialize it as an integer instead of a floating point.

Maybe someone else knows.

### EricDimitri on 2025-11-15

> In both responses, 'fanspeed' doesn't contain any decimal numbers, so I'm not sure what's going on. A bug in UiPath maybe? I don't know UiPath, so not sure about that.
> 
> But this message: "Deserialize JSON 105: Input string '96.758674621582031' is not a valid integer." is very clear, it should not be parsed as an integer, but as a floating point number.
> 
> You'll have to figure out why UiPath is trying to deserialize it as an integer instead of a floating point.
> 
> Maybe someone else knows.

No no no... I didnt check, and I guess was an incredible coincidence...

look an extrac of other bitaxe with beta version....

"fallbackStratumExtranonceSubscribe":	0,
	"responseTime":	248.545,
	"version":	"v2.11.0b6",
	"axeOSVersion":	"v2.11.0b6",
	"idfVersion":	"v5.5.1",
	"boardVersion":	"601",
	"runningPartition":	"ota_0",
	"overheat_mode":	0,
	"overclockEnabled":	1,
	"display":	"SSD1306 (128x32)",
	"rotation":	0,
	"invertscreen":	0,
	"displayTimeout":	-1,
	"autofanspeed":	1,
	"fanspeed":	63.239650726318359,
	"manualFanSpeed":	51,
	"minFanSpeed":	30,
	"temptarget":	62,
	"fanrpm":	3049,

### remcoros on 2025-11-15

:)

Then something in UiPath still thinks it is an integer, does UiPath have some setting/config screen for this? Check to see how 'responseTime' is parsed in UiPath, if that works, do the same for fanspeed.

Must be some schema/setting in UiPath

### EricDimitri on 2025-11-15

Believe me, there is nothing that you can configure...

On Sat, Nov 15, 2025 at 2:12 PM Remco Ros ***@***.***> wrote:

> *remcoros* left a comment (bitaxeorg/ESP-Miner#1350)
> <https://github.com/bitaxeorg/ESP-Miner/issues/1350#issuecomment-3536684756>
>
> :)
>
> Then something in UiPath still thinks it is an integer, does UiPath have
> some setting/config screen for this? Check to see how 'responseTime' is
> parsed in UiPath, if that works, do the same for fanspeed.
>
> Must be some schema/setting in UiPath
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/bitaxeorg/ESP-Miner/issues/1350#issuecomment-3536684756>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AHPUZ6NH3VLFILWYBGTY3DL345NIVAVCNFSM6AAAAACMBF4QK6VHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZTKMZWGY4DINZVGY>
> .
> You are receiving this because you authored the thread.Message ID:
> ***@***.***>
>


### remcoros on 2025-11-15

You'll have to ask UiPath for an example how to parse it as a 'double', not an 'Int32'. I was just looking at the UiPath documentation, but can only find "Int32" variable types, but that doesn't work for floating points. 

https://docs.uipath.com/studio/standalone/2023.4/user-guide/the-variables-panel they do not seem to have a type for floating point numbers, which is SUPER WEIRD. Maybe ask UiPath how to deal with floating point number?

### EricDimitri on 2025-11-15

There must be some sort of bug, because there are other double values in
this same JSON, and those are not a problem.
Anyway, I guess yous hould drop this, since looks like a UiPath problem,
not the Api.

Thanks a lot!! Will load the final version of firmware. Would you mind
adding the uptime to the dashboard? It is really helpful to know if it
restarted!!!

THANKS!!!!!

On Sat, Nov 15, 2025 at 2:24 PM Remco Ros ***@***.***> wrote:

> *remcoros* left a comment (bitaxeorg/ESP-Miner#1350)
> <https://github.com/bitaxeorg/ESP-Miner/issues/1350#issuecomment-3536695561>
>
> You'll have to ask UiPath for an example how to parse it as a 'double',
> not an 'Int32'. I was just looking at the UiPath documentation, but can
> only find "Int32" variable types, but that doesn't work for floating points.
>
>
> https://docs.uipath.com/studio/standalone/2023.4/user-guide/the-variables-panel
> they do not seem to have a type for floating point numbers, which is SUPER
> WEIRD. Maybe ask UiPath how to deal with floating point number?
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/bitaxeorg/ESP-Miner/issues/1350#issuecomment-3536695561>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AHPUZ6OUZIVVNKJDBWZCGXL345OVRAVCNFSM6AAAAACMBF4QK6VHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZTKMZWGY4TKNJWGE>
> .
> You are receiving this because you authored the thread.Message ID:
> ***@***.***>
>


### EricDimitri on 2025-11-15

Since I am here, @remcoros , whats the meaning of "Error: "to the right of the Th/s ? I saw the tooltip, but do you have a better explanation? I have some Bitaxes with 0 there all the tiome, and other, that has 0.5%, 0.8% there all the time. What exaxctly is that? Or tell me a place where to check it. Sorry if this is not the roight place for that question. Thanks!!!!

<img width="906" height="436" alt="Image" src="https://github.com/user-attachments/assets/f189b9e0-8cdb-4eea-bf1c-279fdd12df2f" />

### mutatrum on 2025-11-16

@EricDimitri please ask your question on Discord or on the Discussions tab on here. As for uptime on the dashboard, please open a new issue so it won't get lost in history.

### EricDimitri on 2025-11-16

> [@EricDimitri](https://github.com/EricDimitri) please ask your question on Discord or on the Discussions tab on here. As for uptime on the dashboard, please open a new issue so it won't get lost in history.

Good. @mutatrum  Which is the Discord Channel? Thanks!!
