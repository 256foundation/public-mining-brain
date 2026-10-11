# emberone-usbserial-fw PR #2: merge emberone/00 v2 specific changes

> Source: https://github.com/256foundation/emberone-usbserial-fw/pull/2
> Collected: 2026-10-10
> Published: 2025-02-27
> Registry ID: emberone-usbserial-fw

State: closed | Merged: 2025-02-27 | Author: skot | Type: PR
Closed: 2025-02-27 (merged as 8884c4c64b7a0ea447c9153ea116dea1c7f9d876)
Branch: 256foundation:pinout_changes → main

## Body

(no body)

## Comments

(none)

## Files changed (PRs only)

- src/main.rs (+8/-8) — retargets firmware to the EmberOne/00 v2 board: ASIC UART moved from UART0 (PIN_0/PIN_1) to UART1 (PIN_8/PIN_9); asic_resetn moved PIN_25→PIN_11; asic_pwr_en moved PIN_26→PIN_0 and now boots Low (active-high enable); USB identity strings changed from "OSMU"/"Ember One" to "256F"/"EmberOne00".

Key hunks verbatim:

```diff
-pub type AsicUart = UART0;
+pub type AsicUart = UART1;
```

```diff
-static MANUFACTURER: &str = "OSMU";
-static PRODUCT: &str = "Ember One";
+static MANUFACTURER: &str = "256F";
+static PRODUCT: &str = "EmberOne00";
```

```diff
-        let (tx_pin, rx_pin, uart) = (p.PIN_0, p.PIN_1, p.UART0);
+        let (tx_pin, rx_pin, uart) = (p.PIN_8, p.PIN_9, p.UART1);
```

```diff
-        asic_resetn: gpio::Output::new(p.PIN_25, gpio::Level::High),
-        asic_pwr_en: gpio::Output::new(p.PIN_26, gpio::Level::High),
+        asic_resetn: gpio::Output::new(p.PIN_11, gpio::Level::High),
+        asic_pwr_en: gpio::Output::new(p.PIN_0, gpio::Level::Low),
```

```diff
-    UART0_IRQ => embassy_rp::uart::BufferedInterruptHandler<UART0>;
+    UART1_IRQ => embassy_rp::uart::BufferedInterruptHandler<UART1>;
```
