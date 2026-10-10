# bitaxeorg/ESP-Miner issue #944: Move notifications from top bar to toaster

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/944
> Collected: 2026-10-07
> Published: 2025-05-23

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 944
- State: closed
- Author: mutatrum
- Opened: 2025-05-23
- Closed: 2025-05-25
- Labels: none

## Description

From comment: https://github.com/bitaxeorg/ESP-Miner/pull/926#pullrequestreview-2857332983

The toaster is a better place for other warnings as well, makes for a cleaner UX. Should also work on all screens then, if I'm not mistaken.

## Comments

### duckaxe on 2025-05-25

@mutatrum I don't think it's a good idea to include other warnings in Toastr. Let me explain.

There are still warnings and errors in the application:

```
<p-message *ngIf="info.overheat_mode" severity="error" styleClass="w-full mb-4 py-4 border-round-xl"
    text="Bitaxe has overheated - See settings">
</p-message>

<p-message *ngIf="!info.frequency || info.frequency < 400" severity="warn" styleClass="w-full mb-4 py-4 border-round-xl"
    text="Bitaxe frequency is set low - See settings">
</p-message>

<p-message *ngIf="info.power_fault" severity="error" styleClass="w-full mb-4 py-4 border-round-xl"
    text="{{info.power_fault}} Check your Power Supply.">
</p-message>

<p-message *ngIf="info.isUsingFallbackStratum" severity="warn" styleClass="w-full mb-4 py-4 border-round-xl"
    text="Using fallback pool - Share stats reset. Check Pool Settings and or / reboot Bitaxe">
</p-message>

<p-message *ngIf="settingsUnlocked" severity="warn" styleClass="w-full mb-3 py-4 border-round-xl"
    text="Custom settings can cause damage & system instability. Only modify these settings if you understand the risks of running outside designed parameters.">
    </p-message>
```

In my opinion, these are messages that must be permanently visible and cannot be dismissed by the user like Toastr notifications.

However, Toastr notifications disappear automatically after a while. This is not ideal for important messages. Yes, you can place sticky Toastr notifications that do not disappear. However, these notifications lie on top of the content in the mobile view and cover part of the dashboard. This is also not good.

Toastr notifications are perfect for confirming an action, such as "it was saved" or "you should restart." Toastr notifications are not ideal for important, sticky notifications, such as overheating or pool switch alerts.

In short, I think the current way we show messages is good.

_Sticky Toastr Message on Mobile_
<img width="463" alt="Image" src="https://github.com/user-attachments/assets/3b52b405-90bb-48b4-8cbc-69e480a45288" />

### mutatrum on 2025-05-25

Agreed, thanks for looking into it!
