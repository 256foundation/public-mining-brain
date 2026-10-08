# bitaxeorg/ESP-Miner issue #1438: %100 Error Rate Failed to Receive Json Rpc line

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1438
> Collected: 2026-10-07
> Published: 2025-12-10

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1438
- State: closed
- Author: Niyetiboz
- Opened: 2025-12-10
- Closed: 2025-12-11
- Labels: none

## Description

![Image](https://github.com/user-attachments/assets/94a0cba4-27d8-494b-8d7a-6ddc3df6377d)
I bought my gamma 601 today from amazon and it does not work i did not change any voltage settings ( i did not overclock etc)

![Image](https://github.com/user-attachments/assets/54f59233-6f3f-4b3c-a169-e031cc107a8e)

![Image](https://github.com/user-attachments/assets/418ce165-58c6-45a5-bb64-ae053bcbdbd2)

## Comments

### kukulle-hood on 2025-12-10

@Niyetiboz 
Besides your intention for overclocking, I think you have the wrong settings for your pool.
If you go to public pool it says:

stratum+tcp://public-pool.io:3333
stratum+tls://public-pool.io:4333

You have set 21496, what I think is wrong


Robert

### kukulle-hood on 2025-12-10

@Niyetiboz 
To activate your overclock settings you simply have to use this in your webaddress in your browser ( ?oc= )
So in your case it should be  http://YOUR_IP_ADDRESS/#/settings?oc=

### kukulle-hood on 2025-12-10

I have found a very usefull table for overclocking in terms of he right frequency to voltage.

![Image](https://github.com/user-attachments/assets/8ca3bc0f-bb29-442f-93b8-6e396cac7c98)

Good luck
Robert


### Niyetiboz on 2025-12-10

@kukulle-hood Thank you for your repond i did use my use my gamme 601 at defult settings i did not change anything also i that as well same %100 error happened to me notting changes it changes continuously fallback port 0 hash (it shows it hash but it does not)
stratum+tcp://public-pool.io:3333
stratum+tls://public-pool.io:4333

![Image](https://github.com/user-attachments/assets/34523abc-c782-46ed-a4e1-0bc539510e80)

![Image](https://github.com/user-attachments/assets/b1410bca-7b94-45b6-b42a-164e07ac480a)

### kukulle-hood on 2025-12-10

@Niyetiboz 
can you please send a screenshot from your settings in your pool tab (with advanced options shown)?
Might be the problem is there

### Niyetiboz on 2025-12-10

@kukulle-hood  Yeah sure

![Image](https://github.com/user-attachments/assets/a0aa28a0-dcc6-40d1-b819-d58cfe27444b)

### kukulle-hood on 2025-12-10

@Niyetiboz 
Hmmm, confirm as password you where using "x"

Is there something blocked in your router firewall (your port 3333 e.g.)

I do not see something wrong in the actual settings.

Maybe use your hotspot from your mobile to doublecheck if the problem is your router.

Good luck

Robert




### Niyetiboz on 2025-12-10

@kukulle-hood I found smth on my Router Robert ty for your helps router was blocking the mining.Thank you so much for your help.

### mutatrum on 2025-12-10

> [@kukulle-hood](https://github.com/kukulle-hood) I found smth on my Router Robert ty for your helps router was blocking the mining.Thank you so much for your help.

What router do you have and what setting did you change? This would be helpful if someone else also has the same issue.

### Niyetiboz on 2025-12-11

@mutatrum 
Asus Gt-Ax 11000
I Change Ai protection / and there is two way ips protecion.
I set this off.It is working fine now ty for helping.

### mutatrum on 2025-12-11

Good it's been resolved. For future reference, there's a chapter in the readme on this: 
https://github.com/bitaxeorg/ESP-Miner?tab=readme-ov-file#wi-fi-routers
