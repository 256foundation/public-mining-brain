# 256foundation/asic-rs issue #105: Antminer S21 serial_number is always null

> Source: https://github.com/256foundation/asic-rs/issues/105
> Collected: 2026-10-07
> Published: 2025-11-22

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 105
- State: closed
- Author: glitchpixelz
- Opened: 2025-11-22
- Closed: 2025-11-25
- Labels: none

## Description

Issue:
On Antminer S21 (2025 firmware), the serial_number field in MinerData is always null.
The get_system_info endpoint on the S21 exposes the serial as serinum, not serial_no.

Proposed fix:
DataField::SerialNumber currently only uses /serial_no:

            DataField::SerialNumber => vec![(
                system_info_cmd,
                DataExtractor {
                    func: get_by_pointer,
                    key: Some("/serial_no"), // Cant find on 2022 firmware, does exist on 2025 firmware for XP
                    tag: None,
                },
            )],

Given the existing fallback behavior in fn extract_field(&self, field: DataField) -> Option<Value>, we can support both keys by adding a second extractor for /serinum and cloning the shared system_info_cmd so it can be reused:

            DataField::SerialNumber => vec![(
                system_info_cmd.clone(),
                DataExtractor {
                    func: get_by_pointer,
                    key: Some("/serial_no"), // Cant find on 2022 firmware, does exist on 2025 firmware for XP
                    tag: None,
                },
            ),
                (
                system_info_cmd.clone(),
                DataExtractor {
                    func: get_by_pointer,
                    key: Some("/serinum"), // exist on 2025 firmware for s21
                    tag: None,
                },
            )],

I’ve tested this change locally against the S21 and confirmed that MinerData.serial_number is now populated correctly, while retaining compatibility with the existing /serial_no path.

## Comments

### b-rowan on 2025-11-25

Fixed in #106
