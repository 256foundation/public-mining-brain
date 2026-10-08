# bitaxeorg/ESP-Miner issue #1507: Skip midstates for BM1366/1368/1370

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1507
> Collected: 2026-10-07
> Published: 2026-01-14

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1507
- State: open
- Author: mutatrum
- Opened: 2026-01-14
- Closed: n/a
- Labels: none

## Description

This TODO in `mining.c`:

https://github.com/bitaxeorg/ESP-Miner/blob/9d1e1cb109c0d11eba5a014b64e03d333773cf2f/components/stratum/mining.c#L124

This will only work for BM1397. For the other ASICs they are not needed for sending work to the ASIC. So when constructing the jobs for any other ASIC, we can skip preparing midstates in `construct_bm_job`. Also, the midstate cannot be used for verification in `test_nonce_value`, as the version part, the first 4 bytes of the header that's part of the pre-midstate hash - is rolled. Hence they are called version-rolling ASICs.

For the BM1397, the midstate _can_ be used to speed up verification of the share, but not sure if that's actually worth the extra code path, as it needs logic to select the correct midstate from the 4 in the job. Something like:
```
    const uint8_t *selected_midstate = job->midstate;
    if (job->num_midstates > 1) {
        uint32_t current_version = job->version;
        int index = 0;
        while (current_version != rolled_version && index < job->num_midstates - 1) {
            current_version = increment_bitmask(current_version, job->version_mask);
            index++;
        }
        switch (index) {
            case 0: selected_midstate = job->midstate; break;
            case 1: selected_midstate = job->midstate1; break;
            case 2: selected_midstate = job->midstate2; break;
            case 3: selected_midstate = job->midstate3; break;
        }
    }
```

## Comments

### adammwest on 2026-02-24

its a little complicated, to speed up the verification use the midstate, that code path needs to be added to `test_nonce_value`
and `utils.c`

sources
https://github.com/bitaxeorg/ESP-Miner/blob/master/components/stratum/utils.c
https://siliconlabs.github.io/Gecko_SDK_Doc/mbedtls/html/structmbedtls__sha256__context.html
https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf 
https://github.com/ARMmbed/mbed-crypto/blob/development/library/sha256.c#L109

the following function 

you cant use mbed full SHAs as we have a 'midstate' which means a partial computation of sha so we need a special initialization, I believe the following in principle should work,



```c
/*
 * Continue SHA-256 from an existing midstate.
 * midstate must contain 8 uint32_t words in native-endian
 */
int mbedtls_sha256_starts_from_midstate(
    mbedtls_sha256_context *ctx,
    const uint32_t midstates[8])
{
    SHA256_VALIDATE_RET(ctx != NULL);
    SHA256_VALIDATE_RET(midstates != NULL);

    // We are continuing after exactly one 64-byte block
    ctx->total[0] = 64; // im not sure about this
    ctx->total[1] = 0; // im not sure about this

    ctx->state[0] = midstates[0]; // we have to start SHA256 with midsatetes, NO IV (initialisation vector)
    ctx->state[1] = midstates[1];
    ctx->state[2] = midstates[2];
    ctx->state[3] = midstates[3];
    ctx->state[4] = midstates[4];
    ctx->state[5] = midstates[5];
    ctx->state[6] = midstates[6];
    ctx->state[7] = midstates[7];

    return 0;
}
```
we need a custom padding aswell in python HEX the correct padding
is '8' + '0'*92 * '280'

so we start SHA from midstate and ahve 
header = merkleroot tail + ntime + nbits + nonce + padding (the second block of the first SHA), that is what makes `data`

```c
void double_sha256_from_midstate(const uint8_t *data, uint32_t midstates[8], const size_t data_len, uint8_t dest[32])
{
    mbedtls_sha256_context ctx;

    uint8_t hash1[32]

    // Calculate hash1 from midstate
    mbedtls_sha256_init(&ctx);
    mbedtls_sha256_starts_no_iv(&ctx, midstates);
    mbedtls_sha256_update(&ctx, data, 64);
    mbedtls_sha256_finish( &ctx, hash1[32] )
    mbedtls_sha256_free(&ctx);
   
// full normal sha
   mbedtls_sha256(hash1, 32, dest, 0);
}
```
to test assert
double_sha(header) = double_sha_from_midstate(sha_midstate(header0)+header1))
