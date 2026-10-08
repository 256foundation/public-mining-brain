# bitaxeorg/ESP-Miner issue #582: Design challenge: RPM value is null for fans that do not support RPM data

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/582
> Collected: 2026-10-07
> Published: 2024-12-13

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 582
- State: open
- Author: alltheseas
- Opened: 2024-12-13
- Closed: n/a
- Labels: none

## Description

_what happens_

RPM displays zero ("0 RPM"), when %fan speed is non-zero, and I can see and hear the fan spinning. 

![rpm (1)](https://github.com/user-attachments/assets/eca8b2cf-a44b-4c04-bc88-b88c2a55411b)

_suggestion_

remove x RPM, or add a value

_device & OS_

gamma 601 gekkoscience
2.4.1 firmware & website



## Comments

### alltheseas on 2024-12-13

sidehack advises:

> Likely the fan isn't reporting RPM, so hardware not software

How might we handle unhappy path of fans that do not return data needed to calculate RPM?

### alltheseas on 2024-12-13

Is it possible to not display RPMs field if fan is not returning data needed for RPM calculation?

### MyOwn2C on 2024-12-13

> Is it possible to not display RPMs field if fan is not returning data needed for RPM calculation?

What is the benefit?
It complicates the codes, and you will not see any signs of issues if a previously working fan reporting RPM suddenly stops reporting.
If the register value is 0, show it as 0 so there is no confusion what it is at.
From your pic, the PWM is at 74%, and the RPM signal from fan is 0.
I don't see anything wrong the way it is now.

### alltheseas on 2024-12-13

> What is the benefit?

By removing useless visual elements, clarity improves and focus falls on the useful elements. Conversely, if you dont remove useless elements, and do not simplify, the useful elemen ts will be muddled with useless elements. 

> you will not see any signs of issues if a previously working fan reporting RPM suddenly stops reporting.

This is potential unhappy path you have identified. If there is such an error, it should be surfaced to the bitaxe enjoyer. This does not preclude removing a metric that is useless for hardware that do not support reporting the relevant info.

> I don't see anything wrong the way it is now.

For you, and the current Bitaxe enjoyers there is no problem, probably.

What is the mission of Bitaxe? If it is to distribute mining and make it accessible to more folks than the current set simplification, and ease of use matters. 

If you'd like to learn more about UI and usability, nngroup has great resources:

![image](https://github.com/user-attachments/assets/0977fde6-4daa-4400-800a-7c02affd3623)
https://www.nngroup.com/articles/ten-usability-heuristics/


### MyOwn2C on 2024-12-13

> By removing useless visual elements, clarity improves and focus falls on the useful elements. Conversely, if you dont remove useless elements, and do not simplify, the useful elemen ts will be muddled with useless elements.

It is better to report the values as they are, or don't report at all. 
Selectively hiding them only confuses users.
No software has ever implemented fan UI like you suggested.
Look at fan UI for mobos or any other implementation. 
If fan speed is 0, display 0 or N/A.
If the value is hidden, users cannot know what is happening.

I think the UI now is fine for the fans. No need to change. 
If you want to, source code is available for you to make the change yourself. 




### alltheseas on 2024-12-13

It could be that hardware dashboard UI cannot be simplified past the current state. 

Consider it a design challenge.



### skot on 2024-12-13

I do think there is some room for improvement here. We need to express the setpoint (74% in this case) and the actual measured value (0 RPM in this case). and then someway to show that the fan is not working. @alltheseas can you think of a better way to express this? We need to appear to technical users and new users alike.

### alltheseas on 2024-12-13

@skot do yall have a design contributor?

As a left-curve product contributor I can put together wireframes, and low fidelity mockups, and I know expert design is not my skillset. I might miss the trees for the forest with any design suggestions I conjure beyond problem statements. 

For example on Damus we have the great @robagreda contributing designs, and we've had a few design pros from Bitcoin Design Community contribute reviews and piecemeal suggestions as well. 

Outside of the specific question at hand, I think if there is no design contributor, it would be a fun exercise to organize a design challenge for AxeOS with the pretext of "how might we improve usability of AxeOS, as to reduce to the barrier of wider mining adoption". 

Let me know if this sounds interesting, happy to test interest from designers, and help organize.
