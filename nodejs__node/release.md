tag: v26.12.1
name: 2026-10-21, Version 26.12.1 (Current), @aduh95 prepared by @RafaelGSS
published_at: 2026-10-21T10:38:29Z
prerelease: False




This is a security release.

### Notable Changes

* (CVE-2026-106069, CVE-2026-106072) tls: reject non-canonical IP addresses (Matteo Collina) – High
* (CVE-2026-105482) dns: validate resolve inputs for null bytes (James M Snell) – High
* (CVE-2026-105483) tls: fix ip normalization regression (James M Snell) – High
* (CVE-2026-111497) src: expose `BROTLI_DECODER_ERROR_FORMAT_BLOCK_SWITCH` (Antoine du Hamel) – High
* (CVE-2026-111497) deps: brotli: cherry-pick 0ed4268a4401abcb44720963 (Evgenii Kliuchnikov) – High
* (CVE-2026-105481) http: ensure agent data guard works without I/O (James M Snell) – Medium
* (CVE-2026-106074) crypto: reset random caches across snapshots (Filip Skokan) – Medium
* (CVE-2026-106070) zlib: avoid caching invalid ZIP local headers (Matteo Collina) – Low
* (CVE-2026-106071) src: fix the fs permission tree node on wildcard nodes (James M Snell) – Low
* (CVE-2026-106073) permission: check permission model in realpathSync (RafaelGSS) – Low
* deps: V8: backport 93cd21e8254b (Joyee Cheung)
* crypto: update root certificates to NSS 3.131.1 (Antoine du Hamel)
* tls: reject chains containing blocked public keys (Ulises Gascon)
* deps: update c-ares to 1.34.9 (Node.js GitHub Bot)
* tools: retry Gatekeeper check and stapling after notarization (Ryan Aslett)
* crypto: harden X.509 conversion and formatting (Filip Skokan)

### Commits

* \[[`818e4ca061`](https://github.com/nodejs/node/commit/818e4ca061)] - **crypto**: update root certificates to NSS 3.131.1 (Antoine du Hamel) [#66877](https://github.com/nodejs/node/pull/66877)
* \[[`fd3c87ed43`](https://github.com/nodejs/node/commit/fd3c87ed43)] - **crypto**: harden X.509 conversion and formatting (Filip Skokan) [nodejs-private/node-private#966](https://github.com/nodejs-private/node-private/pull/966)
* \[[`acffa610db`](https://github.com/nodejs/node/commit/acffa610db)] - **crypto**: reset random caches across snapshots (Filip Skokan) [nodejs-private/node-private#987](https://github.com/nodejs-private/node-private/pull/987)
* \[[`7895a5cd2d`](https://github.com/nodejs/node/commit/7895a5cd2d)] - **deps**: update undici to 8.12.2 (Node.js GitHub Bot) [#66721](https://github.com/nodejs/node/pull/66721)
* \[[`12daa54d2e`](https://github.com/nodejs/node/commit/12daa54d2e)] - **deps**: V8: backport 93cd21e8254b (Joyee Cheung) [nodejs-private/node-private#999](https://github.com/nodejs-private/node-private/pull/999)
* \[[`6a8b3db7e2`](https://github.com/nodejs/node/commit/6a8b3db7e2)] - **deps**: update c-ares to 1.34.9 (Node.js GitHub Bot) [#66868](https://github.com/nodejs/node/pull/66868)
* \[[`a6040b50d9`](https://github.com/nodejs/node/commit/a6040b50d9)] - **deps**: brotli: cherry-pick 0ed4268a4401abcb44720963 (Evgenii Kliuchnikov) [nodejs-private/node-private#1002](https://github.com/nodejs-private/node-private/pull/1002)
* \[[`6b78ea171d`](https://github.com/nodejs/node/commit/6b78ea171d)] - **dns**: validate resolve inputs for null bytes (James M Snell) [nodejs-private/node-private#984](https://github.com/nodejs-private/node-private/pull/984)
* \[[`0683ee5f7d`](https://github.com/nodejs/node/commit/0683ee5f7d)] - **http**: ensure agent data guard works without I/O (James M Snell) [nodejs-private/node-private#983](https://github.com/nodejs-private/node-private/pull/983)
* \[[`e5cae10148`](https://github.com/nodejs/node/commit/e5cae10148)] - _**Revert**_ "**module**: synchronously load most ES modules" (Antoine du Hamel) [#66786](https://github.com/nodejs/node/pull/66786)
* \[[`cc244131aa`](https://github.com/nodejs/node/commit/cc244131aa)] - **permission**: check permission model in realpathSync (RafaelGSS) [nodejs-private/node-private#973](https://github.com/nodejs-private/node-private/pull/973)
* \[[`0392385841`](https://github.com/nodejs/node/commit/0392385841)] - **src**: expose `BROTLI_DECODER_ERROR_FORMAT_BLOCK_SWITCH` (Antoine du Hamel) [nodejs-private/node-private#1002](https://github.com/nodejs-private/node-private/pull/1002)
* \[[`c273a408c9`](https://github.com/nodejs/node/commit/c273a408c9)] - **src**: fix the fs permission tree node on wildcard nodes (James M Snell) [nodejs-private/node-private#986](https://github.com/nodejs-private/node-private/pull/986)
* \[[`a2caddd20e`](https://github.com/nodejs/node/commit/a2caddd20e)] - **tls**: reject chains containing blocked public keys (Ulises Gascon) [#66871](https://github.com/nodejs/node/pull/66871)
* \[[`ad788ccd07`](https://github.com/nodejs/node/commit/ad788ccd07)] - **tls**: reject non-canonical IP addresses (Matteo Collina) [nodejs-private/node-private#982](https://github.com/nodejs-private/node-private/pull/982)
* \[[`cd4b05469c`](https://github.com/nodejs/node/commit/cd4b05469c)] - **tls**: fix ip normalization regression (James M Snell) [nodejs-private/node-private#985](https://github.com/nodejs-private/node-private/pull/985)
* \[[`5fa440e0d7`](https://github.com/nodejs/node/commit/5fa440e0d7)] - **tools**: retry Gatekeeper check and stapling after notarization (Ryan Aslett) [#66855](https://github.com/nodejs/node/pull/66855)
* \[[`745ad77156`](https://github.com/nodejs/node/commit/745ad77156)] - **zlib**: avoid caching invalid ZIP local headers (Matteo Collina) [nodejs-private/node-private#981](https://github.com/nodejs-private/node-private/pull/981)

