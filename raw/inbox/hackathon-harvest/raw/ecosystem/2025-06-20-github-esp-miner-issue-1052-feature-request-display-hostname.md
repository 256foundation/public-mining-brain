# bitaxeorg/ESP-Miner issue #1052: Feature Request: Display HOSTNAME in <title> and top of AxeOS page

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1052
> Collected: 2026-10-07
> Published: 2025-06-20

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1052
- State: closed
- Author: homecryptominer
- Opened: 2025-06-20
- Closed: 2025-06-26
- Labels: none

## Description

Not a bug, but to help improve UX. There are many people out there with many Bitaxes. When having multiple tabs opened in a browser, hovering over the tab just shows AxOS and the IP. It would be really useful to also include the actual HOSTNAME in the <title> tag.

In addition to this, it would also be useful to render the HOSTNAME at the top of the AxeOS Dashboard somewhere - perhaps to the right hand side of the hamburger menu?

Thank you so much for your continued support team! :-)
Steve

## Comments

### mutatrum on 2025-06-20

You're in luck, this will be added in the next version: #996 

Not sure if the addition of hostname in the hamburger menu adds anything, the URL bar in the browser is there. We might need to revisit #657 for this.

### duckaxe on 2025-06-20

Maybe like that. Hostname & ASIC added to the page header. Mobile hostname only.

<img width="1152" alt="Image" src="https://github.com/user-attachments/assets/d67b30ce-69b9-4963-8e94-c3b2bd26b0e4" />

<img width="396" alt="Image" src="https://github.com/user-attachments/assets/86748b03-c373-4089-9b91-60432bca5cba" />

### duckaxe on 2025-06-20

I would prefer the following solution: We should show the hostname and Wi-Fi signal strength because that information is much more important and helpful than the ASIC.

On desktop, we display this information in the top right corner. Since there isn't enough space for it on mobile, we display it in the menu.

**Desktop**

https://github.com/user-attachments/assets/9935fa36-8d68-4272-aad3-bd88a3981d67

**Mobile**

https://github.com/user-attachments/assets/59b71a39-38e7-4482-9bff-c03a315b7e27



### mutatrum on 2025-06-20

I like that.

### skot on 2025-06-20

I like this too. My only suggestion is that the icon for hostname should be something looks like a bitaxe and not a computer (since it's the Bitaxe hostname)

### duckaxe on 2025-06-20

@skot We use [PrimeNg Icons](https://primeng.org/icons#list). There are not many icons that match this.

### skot on 2025-06-20

hmm, yeah no ideal icons in there. If we really can't have a Bitaxe icon, then maybe one of these?

<img width="109" alt="Image" src="https://github.com/user-attachments/assets/07860db2-c7fb-4767-a32d-917330edc6c0" />

<img width="88" alt="Image" src="https://github.com/user-attachments/assets/dda8e1b8-8d20-4097-baa0-821bdf084bc1" />

<img width="128" alt="Image" src="https://github.com/user-attachments/assets/d6c7b862-880d-4396-a19a-f22d3efd605b" />

<img width="105" alt="Image" src="https://github.com/user-attachments/assets/41932140-d8f2-481a-8753-35ef65f9980a" />

<img width="78" alt="Image" src="https://github.com/user-attachments/assets/040558c1-ea46-4408-b193-ca86d61cd356" />

### skot on 2025-06-20

maybe we could sneak a lil' Bitaxe icon in there? Something like a simplified version of the one on bitaxe.org? 

![Image](https://github.com/user-attachments/assets/0292afde-db08-4ab9-a849-1dfca5cec7f3)


### duckaxe on 2025-06-20

Check this. 

<img width="1084" alt="Image" src="https://github.com/user-attachments/assets/66d4cc2a-e635-49b9-8304-3a4a50fcd6ca" />

Found on bitaxe.org 

<img width="525" alt="Image" src="https://github.com/user-attachments/assets/07774d56-6d59-4fe1-8d93-f8d2e4b3a437" />

### duckaxe on 2025-06-20

> hmm, yeah no ideal icons in there. If we really can't have a Bitaxe icon, then maybe one of these?

We use many of them in the sidebar. I wouldn't reuse them so as not to confuse users.

### mutatrum on 2025-06-20

Made a quick and dirty outline of the above image. Maybe this can be used as a custom icon?

![Image](https://github.com/user-attachments/assets/21bbd94c-81ac-49aa-8854-2393ac0c8a16)

### duckaxe on 2025-06-20

@mutatrum Your svg is good, but not optimal for a very small icon. I made a clean pixel art icon that looks good as a tiny icon. What do you think?

![Image](https://github.com/user-attachments/assets/93be52c0-5998-4870-b8a6-59b7eddfdd61)

**Yours**
<img width="271" alt="Image" src="https://github.com/user-attachments/assets/de6f71b9-e66f-44d4-ace7-9f557fc1af9b" />

**Mine**
<img width="1084" alt="Image" src="https://github.com/user-attachments/assets/35b10727-8b02-42a3-949a-aab8ee5420ce" />


### mutatrum on 2025-06-20

Can you see if you get this working?
```
    <ng-template #bitaxeicon>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
            <g id="bitaxe">
                <path d="M5 3A1 1 0 004 4V25a1 1 0 001 1H20a1 1 0 001-1V4A1 1 0 0020 3H17V2A1 1 0 0016 1H9A1 1 0 008 2V3ZM5 4H8V5a1 1 0 001 1h7a1 1 0 001-1V4h3V8H17v2h3v1H19v1h1V25H5Zm4-2h7V5H9ZM7 18a1 1 0 0111 0A1 1 0 017 18Zm1 0a1 1 0 009 0 1 1 0 00-9 0ZM9 8H7A1 1 0 006 9v2a1 1 0 001 1H9a1 1 0 001-1V9A1 1 0 009 8ZM9 9v2H7V9Z"/>
            </g>
        </svg>
    </ng-template>
```

It should be an svg version of your pixelart:

![Image](https://github.com/user-attachments/assets/1e9ff262-1536-406e-8b72-308db677f249)

According to https://primeng.org/customicons#svg, this is supported with PrimeNG, but not sure how it'll fit into Axe-OS.

### duckaxe on 2025-06-21

Inline embedding will work, but we can't use it because we embed the SVG file in several places. That is why I have saved it as an image file, see my PR.

Let me know if you want me to change anything else.

### mutatrum on 2025-06-21

That's not bad for a few minutes fiddling 😆 
![Image](https://github.com/user-attachments/assets/df45e194-9e48-457f-a6e0-f7ed0a6a23a7)

FYI, I used this to make it: https://yqnn.github.io/svg-path-editor/

Fun shared effort, this icon 🤣 

### duckaxe on 2025-06-21

Awesome tool. Props to you.

### homecryptominer on 2025-06-22

You guys are BRILLIANT! I love the changes. This change with the HOSTNAME also in the web <title> bar will help me quickly identify which Bitaxe I am looking at without having to scroll to the bottom of the screen to check my pool where I have my BTC-ADDRESS.HOSTNAME. 

### skot on 2025-06-22

Very nice!!
