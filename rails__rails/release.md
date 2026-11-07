tag: v8.1.4.1
name: 8.1.4.1
published_at: 2026-11-04T02:46:00Z
prerelease: False

## Active Support

*   `ActiveSupport::MessagePack` no longer deserializes an unsafe
    `ActiveSupport::SafeBuffer` as `html_safe`.

    A `SafeBuffer` that was no longer `html_safe?`, for example after an
    in-place `gsub!`, was deserialized as an `html_safe` `SafeBuffer`. It is now
    serialized with an unsafe marker and deserialized as a `String`. Earlier
    versions of Rails cannot read an unsafe buffer serialized this way.

    [GHSA-2w9f-fxwj-w2qf]

    *Jean Boussier*

*   `ActiveSupport::Inflector#safe_constantize` matches the constant name in a
    `LoadError` message as a literal string instead of building a `Regexp`
    from it.

    The name's segments were interpolated unescaped into the pattern, so input
    that reaches `safe_constantize`, such as the channel identifier in an Action
    Cable subscribe command, chose the source passed to the regexp compiler.

    [GHSA-8474-xrp6-wh69]

    *Jeremy Daer*

## Active Model

*   No changes.


## Active Record

*   No changes.


## Action View

*   Skip attribute names in tag helpers that are blank once converted to a
    string.

    A Symbol such as `:" "` is not blank, because `Symbol#blank?` is
    `Symbol#empty?`, so it reached the escaping step and produced an attribute
    with no name. The asset helpers symbolize their keys, so an ordinary String
    key reached the same place.

    [GHSA-68p9-83h6-5wpj]

    *Mike Dalessio*

*   Fix `strip_tags` to encode `"` and `'` in its output.

    `strip_tags` returns an `html_safe` string, but was not encoding quotation
    marks. The method now encodes all five HTML-significant characters (`&`,
    `<`, `>`, `"`, `'`), consistent with the existing `html_safe` convention.

    Output used outside HTML, such as in a text template or JSON, now contains
    `&quot;` and `&#39;` where it contained `"` and `'`. `CGI.unescapeHTML`
    decodes them.

    [GHSA-rq8q-p985-fjq7]

    *Mike Dalessio*

*   Escape the matched phrase before substituting it into `highlight`'s
    `:highlighter`.

    A match was copied into each `\1` of the highlighter as it appeared in
    the sanitized text, which keeps `"` and `'` as they are, so a match
    containing a quote ended a quoted attribute value such as the
    documented `'<a href="search?q=\1">\1</a>'` and added attributes of
    its own. Each substituted group now goes through
    `ERB::Util.html_escape_once`, so quotes in a match render as `&quot;`
    and `&#39;`. Only the numbered placeholders `\0` to `\9` are expanded,
    and a match never replaces the `>` that closes a tag.

    [GHSA-v6rj-xm57-3p59]

    *Jeremy Daer*

*   Require rails-html-sanitizer 1.7.2 or later.

    With the HTML5 sanitizer, Nokogiri before 1.19.5 left `<` and `>`
    unescaped in attribute values. `highlight` and `simple_format`, which
    edit the sanitized HTML as a string, could then turn markup inside an
    attribute value into live elements. rails-html-sanitizer 1.7.2 requires
    Loofah 2.25.3, which requires Nokogiri 1.19.5.

    [GHSA-2p2f-4rq4-gjwc]

    *Mike Dalessio*

## Action Pack

*   Apply `config.action_dispatch.cookies_same_site_protection` to every session
    store.

    `ActionDispatch::Session::CacheStore`, `MemCacheStore` and third-party
    stores built on `AbstractStore` or the session mixins sent session cookies
    with no `SameSite` attribute. Only `CookieStore` applied the configured
    default.

    [GHSA-gmj8-hvj3-49mw]

    *Jean Boussier*

*   Prevent `ActionController::Live` streams from blocking when a full buffer is
    closed or aborted.

    [GHSA-rwvh-fw6r-pwvp]

    *Jeremy Daer*

*   Set and extend the `Vary` header for rendered responses according to the
    request headers used in format negotiation.

    `Vary: Accept` was only added when the request carried a usable `Accept`
    header. A response to a request without one, negotiated to HTML or
    JavaScript, could be stored by a shared cache and served to later clients
    that requested a different representation.

    Responses now vary on `Accept` and `X-Requested-With` whenever the format is
    not given by the URL. XHR requests without `Accept` also vary on
    `Content-Type`, which Rails uses as a legacy format fallback. When
    `config.action_dispatch.ignore_accept_header` is enabled, responses vary
    only on `X-Requested-With`.

    These fields are appended to an existing `Vary` value without duplicating
    fields case-insensitively. `Vary: *` remains unchanged.

    [GHSA-r9jg-fmfx-2gv6]

    *Jeremy Daer*

*   Skip writing a `CacheStore` session that another request deleted while this
    one ran.

    A request that loaded a session from `ActionDispatch::Session::CacheStore`
    wrote it back when it finished, even after a concurrent `reset_session` or a
    server-side delete had removed it, so the old session ID worked again.

    [GHSA-2586-8ghr-69fj]

    *Mike Dalessio*

*   Don't write upgraded cookies to a response that skips the session.

    Reading a signed or encrypted cookie written under a rotated secret, or in
    the format a `:hybrid` serializer migrates from, writes it back in the
    current format. That write ignored `request.session_options[:skip]`, so a
    response that skips the session, such as the Active Storage proxy's
    public, cacheable response, could still carry the session cookie in
    `Set-Cookie`. Such a response now leaves the cookie unchanged, and a later
    request that does not skip the session upgrades it. An application that
    skips the session on every request no longer upgrades its signed or
    encrypted cookies. Cookies the application sets are still written.

    [GHSA-x6mj-8jx9-qhqv]

    *Mike Dalessio*

*   Detect conflicts between the `Forwarded` and `X-Forwarded-For` headers in
    `ActionDispatch::RemoteIp`.

    When `ip_spoofing_check` is enabled (the default), requests carrying both
    headers with conflicting client addresses now raise
    `ActionDispatch::RemoteIp::IpSpoofAttackError`.

    [GHSA-2gff-2mmg-m73p]

    *Gannon McGibbon*, *Mike Dalessio*

*   `ActionController::Parameters#each_key` returns `self` when given a block.

    It returned the internal `ActiveSupport::HashWithIndifferentAccess`, which
    does not respond to `permitted?`, so passing that return value to mass
    assignment skipped the Strong Parameters check. `each`, `each_pair` and
    `each_value` already return `self`.

    Document that `ActionController::Parameters#as_json` returns every
    parameter, permitted or not, in a hash that mass assignment does not check.

    [GHSA-wm3x-v3qw-4jh3]

    *Mike Dalessio*

## Active Job

*   No changes.


## Action Mailer

*   No changes.


## Action Cable

*   No changes.


## Active Storage

*   Preserve committed proxy responses when a storage error interrupts a
    streamed download.

    [GHSA-4v2w-w6g6-f8f8]

    *Jeremy Daer*

*   Derive `ActiveStorage::Filename#base` and `#extension` from the sanitized
    filename.

    This prevents null bytes and invalid byte sequences in stored filename
    metadata from raising when a blob is opened or represented. Existing blob
    records are handled without a data migration.

    [GHSA-p2pm-g2h6-7j5j]

    *Jeremy Daer*

*   Ship an ImageMagick security policy and apply it to every ImageMagick
    process MiniMagick spawns.

    ImageMagick chooses a coder from the content of the file it is given, and
    some coders act on files named inside the image rather than on the image
    itself. Active Storage constrained none of them, so an uploaded file could
    reach any coder the host's policy allowed, through the ImageMagick analyzer
    at attach time, with no variant or `analyze` call in the application.

    Active Storage now ships a `policy.xml