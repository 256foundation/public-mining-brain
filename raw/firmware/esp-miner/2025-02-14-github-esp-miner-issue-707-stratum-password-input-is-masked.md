# bitaxeorg/ESP-Miner issue #707: Stratum Password Input is Masked and Cannot Be Edited in Settings

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/707
> Collected: 2026-10-07
> Published: 2025-02-14

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 707
- State: open
- Author: borzaka
- Opened: 2025-02-14
- Closed: n/a
- Labels: wontfix

## Description

**Describe the bug**  
On the Settings page, the mining pool password field is masked using the HTML input `type="password"`, making it impossible to view or edit **after** saving. However, mining pool "passwords" are not actual passwords; they are configuration settings that can be frequently changed.

For example, my current mining pool password is:
`c=BCH,mc=BCH,sd=2913,m=solo,ID=bitaxegamma`

Since the input is masked after saving, retrieving or modifying long settings becomes difficult.

**To Reproduce**  
Steps to reproduce the behavior:  
1. Go to the **Settings** page.  
2. Enter a mining pool password (e.g., `c=BCH,mc=BCH,sd=2913,m=solo,ID=bitaxegamma`).  
3. Save the settings.  
4. Observe that the password field is masked and cannot be viewed or edited without entering the whole password again.

**Expected behavior**  
The mining pool password should always be visible and editable since it is a configuration setting rather than a sensitive password. Changing it should be straightforward without requiring the user to remember or re-enter the entire setting manually.  

**Hardware:**  
- **Bitaxe HW version:** Gamma 601  
- **Bitaxe HW vendor:** Gobrrr  
- **ESP-Miner FW version:** v2.5.1  
- **Hash Frequency:** 525  
- **Input Voltage:** 5.2V
- **Measured ASIC Voltage:** 1.14V
- **Pool URL, Port, User:** sha256.mine.zergpool.com:3333  

**Additional context**  
A potential fix could be to change the password input field to a standard text input (`type="text"`) or provide a toggle to show/hide the value. This would allow users to quickly modify their mining pool settings without frustration.

## Comments

### MyOwn2C on 2025-02-14

Only issues for pools that require long and complex string for password. 
For most pools it is just x or not even used. 

### skot on 2025-02-14

The reason why you can't edit the password field after saving is because it's write-only (no route to read the password back from a Bitaxe). This makes sense if the password is actually a password, as some pools do. Kinda silly since it's all sent in the clear. 

I guess we could have the option to retrive this config if the user enables that.. but this is starting to get kinda hacky. (like using the password field for config settings)

### borzaka on 2025-02-14

Thanks for the explanation! I understand that the password field is write-only and that some pools use it for actual passwords. But I think it's a minority.
However, in many cases (like mine), it's just a configuration string that needs to be visible and editable.

A potential solution could be:
- Keep the existing password input (`type="password"`) for saving the value, but make it a hidden input.
- Add a new separate text input field (`type="text"`) that always displays the last entered password/config.
- When the user updates the new password text field, the hidden password input gets updated as well (value copied from the password text input) before submission.

This way:
- The user always sees their entered config/password.
- No need to introduce a read route, keeping the existing security model intact.

Would this approach make sense? Or do you see potential issues with it?

### skot on 2025-02-14

I think we could do something like this to make the password persist in the same session.. but as soon as you reload the browser tab it's going to go away unless we have a route to read (which we don't really want to do)

### borzaka on 2025-02-15

Would it be possible to add a new configuration input that can store and display the entered value? This input could remain in sync with the password field, allowing it to be read later without modifying the existing write-only behavior.

### skot on 2025-02-15

the issue is loading the password from the non-volatile storage on the bitaxe.. not which field it goes into
