# bitaxeorg/ESP-Miner issue #308: Unify the firmware images

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/308
> Collected: 2026-10-07
> Published: 2024-08-28

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 308
- State: closed
- Author: skot
- Opened: 2024-08-28
- Closed: 2025-11-29
- Labels: enhancement, help wanted, good first issue

## Description

right now we have two firmware images required for an update; `esp-miner.bin` and `www.bin`

It's nice because the `www.bin` image is much bigger and you don't always need it. 

But it's really complicated for end users. especially if one of the updates fails and they don't notice it.

I'd like to unify the images into one bigger one to simplify the update process.

## Comments

### tdb3 on 2024-11-17

I won't have time to implement this for at least a few weeks, but I looked into it a little bit.  Some thoughts/options below:

### Option 1: Embed Axe-OS web files into OTA partitions
- Embed Axe-OS files into `ota_0`/`ota_1`. These files are normally stored in `www` (spiffs partition)
- [This page](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/build-system.html?highlight=binary%20data#embedding-binary-data) describes a bit on how this might be done. [Here's an example](https://github.com/espressif/esp-idf/blob/c9763f62dd00c887a1a8fafe388db868a7e44069/examples/protocols/http_server/file_serving/main/file_server.c#L102-L108) of an application doing something similar.
- Might need to remove the `factory` partition (or make it smaller) to free up space, and operate solely from `ota_0`/`ota_1` (e.g. using `CONFIG_BOOTLOADER_APP_ROLLBACK_ENABLE`)
- OTA updates would then consist of a single file containing both the main app and axe-os web interface
- Rollback for a bad OTA update adds resiliency/redundancy for axe-os (in addition to the main app)

### Option 2: Package `esp-miner.bin` and `www.bin` together
- User sees and works with one firmware file (e.g. `esp-miner.zip`), but in reality, both firmware files are archived within it
- The archive is automatically extracted client-side in the web app, then the web app posts each file to the respective endpoints (`api/system/OTAWWW`, `api/system/OTA`) in sequence (e.g. `www.bin`, then `esp-miner.bin`)
- Could keep the single `www-data` partition
- Might be more prone to failure (more edge cases, less atomic)


##### Other links
https://developer.espressif.com/blog/ota-updates-framework/


### tdb3 on 2025-01-12

In #649, the recovery page is refactored to use the approach described in the second bullet of option 1. Seems to work well, which is promising for the approach of embedding the web files into the OTA parition.

The next steps would include: updating http_server to serve the full web interface files this way (looks like the files might be < 1MB so could fit into the 4MB ota partition, adjusting partitioning to deprecate/remove the `www` partition, adjust building, etc.

### tdb3 on 2025-01-12

Some thinking out loud:

The axe-os web UI gzip files generated in main/http_server/axe-os/dist/axe-os/ are dynamically named based on hashes of the contents of the files (to defeat caching). This makes it a bit trickier to embed the files directly into esp-miner.bin.
Maybe CMake could be instructed to discover the filenames, then add them.

Playing around with something like:

```cmake
file(GLOB WEB_FILES LIST_DIRECTORIES false CONFIGURE_DEPENDS ${CMAKE_SOURCE_DIR}/main/http_server/axe-os/dist/axe-os/*.gz)
foreach(FILE ${WEB_FILES})
  get_filename_component(FILENAME ${FILE} NAME)
  message(STATUS "Adding file: ${FILENAME}")
  target_add_binary_data(esp-miner ${FILENAME} BINARY)
endforeach()
```

There would also be another piece needed. Currently, `rest_common_get_handler()` (`http_server.c`) is blissfully unaware of the specific filenames, and attempts to open/serve these files from the SPIFFS partition upon request (e.g. GET). The `EMBED_FILES`/`target_add_binary_data()` approach involves creation of pointers to the file data to use it, specifically with knowledge of the mutated file names ("_binary" prepended, special characters replaced with underscores, "_start"/"_end").

```c
    extern const unsigned char recovery_page_start[] asm("_binary_recovery_page_html_start");
    extern const unsigned char recovery_page_end[] asm("_binary_recovery_page_html_end");
    const size_t recovery_page_size = (recovery_page_end - recovery_page_start);
```

The C code won't have this info ahead of time for the dynamically generated web UI gzips, so maybe we need a CMake initiated step to replace keyword text in `http_server.c`?

### WantClue on 2025-11-29

Community agreement atm is to keep it in for potential alternative WebUI like AxeWellUi
