tag: 1.0.2
name: 1.0.2
published_at: 2026-10-23T09:01:02Z
prerelease: False

## Behavior changes
- JS page errors now log under a new `page_error` scope at WARN (silence with `--log-filter`).
- Each top-level page now has its own session history; a second page no longer shows up in the first page's back/forward.
- `--block-private-networks` now blocks more non-routable ranges (CGNAT, benchmarking, multicast, reserved, NAT64).
- `no-cors` fetches with a non-safelisted method are now rejected.
- An unreadable `--http-cache-dir` database is now discarded instead of exiting.
- Console values written to the log are now escaped and capped.

## New Web APIs
- Web Crypto: Ed25519, X25519, ECDSA, RSA-PSS, RSASSA-PKCS1-v1_5, `wrapKey`/`unwrapKey` + AES-KW; EC and RSA-OAEP import/export
- WebCodecs, `OfflineAudioContext`, WebVTT improvements
- XML document parsing
- `setRangeText()` on `<input>` and `<textarea>`; `textarea.textLength`
- `HTMLProgressElement` `value`/`max`/`position`; `HTMLOptionElement.index`; missing table APIs
- `document.hasFocus()`; `window.outerWidth/outerHeight/screenX/screenY/screenLeft/screenTop`
- `:nth-child(An+B of S)` and `:nth-last-child(An+B of S)`
- `PermissionStatus` is now an `EventTarget`; `DOMException` is now structured-cloneable; `ImageData` overload
- Missing global event handlers added to `window`, `document` and `body`

## Web API behavior / fixes
- Element widths are now resolved relative to their parent (block, inline, floats, %, min/max-width, basic flex)
- Client rects (`getBoundingClientRect`, `getClientRects`) are now viewport-relative
- Mouse events now reach into shadow DOM and iframes
- Escape now closes the topmost modal dialog
- Iframes inside a shadow root now load when their host connects
- `replaceWith` compliance and cross-document adoption; `isEqualNode(null)` now returns false
- `insertAdjacentHTML` now works on SVG elements
- Trusted key events now report Chrome's legacy `keyCode`/`which`/`charCode`
- Text selection offsets now count UTF-16 code units
- `TextDecoder` now only strips a BOM for UTF-8/UTF-16
- `form.elements` now lists fieldset, object and output
- Sequence arguments now accept any iterable
- Better `getComputedStyle().transform`
- Fixed CSS nested rule parsing; escapes are now decoded in unquoted attribute selectors
- Cookies are now sent longest path first, then oldest first
- 401/407 responses are now delivered as-is when no auth challenge header is present

## CDP
- `Fetch.continueRequest` `interceptResponse` is now supported
- `Fetch.continueWithAuth` with `Default`/`CancelAuth` now delivers the original 401/407, as Chrome does
- `Runtime.exceptionThrown` is now emitted for unhandled promise rejections, with the context the exception was thrown in
- `Log.entryAdded` is now emitted for resources that fail to load
- `DOM.scrollIntoViewIfNeeded` is now supported (previously a no-op)
- `LP.getPageStatus` added: page issue summary (JS errors, skipped resources, fetch stats). Also included in `fetch` output when `--json` is used
- Custom ARIA states and focusability are now exposed in the AX tree
- Non-UTF-8 status text and headers are now reported as strings rather than a byte array
- Permission overrides are now cleared when a browser context closes

## Serve / CLI
- `serve --unix-socket <path>` added: CDP over a Unix domain socket
- `--remote-allow-origins` added: allow CDP connections that send an `Origin` header (rejected by default), matching Chrome
- `serve` now honors `--cookie-jar`: the jar is saved when a connection closes. With multiple connections, last write wins
- `fetch --dump structured_data` added
- `fetch --markdown-alternate` added: follow a page's `text/markdown` alternate. `text/markdown` documents are now dumped as-is

## Tools
- `markdown` tool: `alternate` option added
- A failed `goto` now closes the page
- Tree tool: links kept inside headings, multi-line names kept on one line

## Performance / stability
- Reworked TaggedOpaque (less memory)
- The scheduler now runs from a snapshot and no longer runs after every script evaluation
- Faster forgiving base64 decode
- UAF fixes: blob navigation, attribute change, file→blob layout; recursive close during load
- Script rejects no longer run microtasks mid-evaluation