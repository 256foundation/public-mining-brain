# bitaxeorg/bitaxe-web-flasher issue #29: status.flashingFailed: Failed to download firmware from GitHub. Please try again.

> Source: https://github.com/bitaxeorg/bitaxe-web-flasher/issues/29
> Collected: 2026-10-07
> Published: 2025-12-25

- Repository: bitaxeorg/bitaxe-web-flasher
- Type: issue
- Number: 29
- State: closed
- Author: jesusinsomnio
- Opened: 2025-12-25
- Closed: 2025-12-30
- Labels: none

## Description

Hello,

I have a Bitaxe Gamma 601 that has been mining well for 2 months without any issues. Yesterday, I turned it off by unplugging it and moved it to a different location. When I plugged it back in, it no longer worked properly: the Bitaxe continues mining correctly, and I can see it on public-pool, but I can't access it through the Bitaxe web page. I can see the IP on the screen, but I can't connect to it as I did before. Also, on the screen, I see the SSID of the Wi-Fi it's connected to, but on the bottom line, it shows the SSID it has when it connects for the first time (BITAXE_XXXX).

I’ve tried flashing it through the web interface, with the USB-C connected, powering it on, pressing RESET and BOOT simultaneously, releasing RESET first and then BOOT, and when trying to flash through the web, I get the error: status.flashingFailed: Failed to download firmware from GitHub. Please try again. I’ve also tried pressing BOOT, connecting the USB-C, releasing BOOT, and the error while flashing is the same. It's like it can’t find GitHub’s DNS. I’ve pinged GitHub from my PC, and it responds. I’ve tried changing DNS settings on the router, changed the Bitaxe IP, and it still does the same. It mines, but I can’t access the web page to modify settings, and on the screen, part of the factory settings and part of the current configuration appear.

What else can I do?

## Comments

### coderabbitai[bot] on 2025-12-25

<!-- This is an auto-generated issue plan by CodeRabbit -->


### 📝 CodeRabbit Plan Mode
Generate an implementation plan and prompts that you can use with your favorite coding agent.

- [ ] <!-- {"checkboxId": "8d4f2b9c-3e1a-4f7c-a9b2-d5e8f1c4a7b9"} --> Create Plan

<details>
<summary>Examples</summary>

- [Example 1](https://github.com/coderabbitai/git-worktree-runner/issues/29#issuecomment-3589134556)
- [Example 2](https://github.com/coderabbitai/git-worktree-runner/issues/12#issuecomment-3606665167)

</details>

---

<details>
<summary><b>🔗 Similar Issues</b></summary>

**Possible Duplicates**
- https://github.com/bitaxeorg/bitaxe-web-flasher/issues/20

**Related Issues**
- https://github.com/bitaxeorg/bitaxe-web-flasher/issues/25
- https://github.com/bitaxeorg/bitaxe-web-flasher/issues/26
- https://github.com/bitaxeorg/bitaxe-web-flasher/issues/2
</details>
<details>
<summary><b>👤 Suggested Assignees</b></summary>

- [LAU-ETH](https://github.com/LAU-ETH)
- [Bradvani](https://github.com/Bradvani)
- [Uefi1](https://github.com/Uefi1)
- [w3irdrobot](https://github.com/w3irdrobot)
</details>


---
<details>
<summary> 🧪 Issue enrichment is currently in open beta.</summary>


You can configure auto-planning by selecting labels in the issue_enrichment configuration.

To disable automatic issue enrichment, add the following to your `.coderabbit.yaml`:
```yaml
issue_enrichment:
  auto_enrich:
    enabled: false
```
</details>

💬 Have feedback or questions? Drop into our [discord](https://discord.gg/coderabbit)!

### WantClue on 2025-12-30

has been fixed
