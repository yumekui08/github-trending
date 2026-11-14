tag: v0.7.0
name: v0.7.0
published_at: 2026-09-20T00:37:32Z
prerelease: False

# tailcat changelog

## v0.7.0 (2026-09-19)

- `--serve=exit-node` servers now forward UDP flows; previously only
  TCP was forwarded, so DNS, QUIC, and other UDP traffic through an
  exit node went nowhere.
- Serving local ports works from Windows: the server resolves
  `localhost` itself instead of using the hosts file, which Windows
  ships without localhost entries, so the name no longer escapes to
  real DNS servers. It also dials both 127.0.0.1 and ::1, reaching
  services bound to only one loopback address. Official binaries also
  no longer build with the `netgo` tag that forced Go's pure resolver
  on Windows and macOS; they now use the operating system's resolver
  there, like a default `go build` does.
  ([#108](https://github.com/tailscale/tailcat/issues/108), reported
  by [@Sammy-T](https://github.com/Sammy-T))
- `tailcat cp` now works with OpenSSH 8.7 through 8.9 clients, such
  as Ubuntu 22.04's. Those versions still speak the legacy SCP
  protocol unless `scp -s` asks for SFTP, which is all tailcat file
  services accept, so copies failed. tailcat now checks whether the
  installed scp understands `-s` and passes it when it does; older
  clients without the flag are unchanged.
  ([#114](https://github.com/tailscale/tailcat/issues/114), fixed in
  [#123](https://github.com/tailscale/tailcat/pull/123) by
  [@BreezeDelegate](https://github.com/BreezeDelegate))
- Go library: `Server.Status()` now includes a `Peer` entry per
  connected client, with `CurAddr` and `Relay` to tell a direct path
  from a DERP-relayed one.
  ([#116](https://github.com/tailscale/tailcat/issues/116), reported
  by [@Mo3he](https://github.com/Mo3he))
- Go library: the new `Server.Listen(ctx, network, address)` serves
  TCP and UDP ports in the standard `net.Listener` shape, as an
  alternative to the `OnTCP` and `OnUDP` hooks; for UDP, each Accept
  returns one client flow as a `net.Conn`. Listeners claim their
  specific ports ahead of the wildcard hooks, and Listen starts the
  server if it isn't running yet.
- `tailcat forward` takes an `--open-browser` flag that opens a web
  browser to the forwarded local port; `tailcat browse <tc-addr>` is
  an alias for `tailcat forward --open-browser <tc-addr> 0:80`.
- `exec` service: `tailcat serve exec -- <command>` runs the command
  for each incoming connection with the connection as its stdin and
  stdout, like inetd. With the `ssh` or `no-auth-ssh` service, the
  command after `--` instead replaces the shell for every session,
  like OpenSSH's `ForceCommand`, with no shell, client-chosen command,
  or SFTP offered.
- `tailcat ssh` to a DNS-named destination first probes the server the
  way a stranger would, with no credentials, and refuses to connect if
  the server hands out a shell to anyone, since an address published
  in DNS is public; `--skip-dns-safety-check` opts out. The README,
  the root help's DNS section, and `serve no-auth-ssh` startup now all
  warn that DNS-published addresses need `--allow` or
  `--ssh-authorized-keys`.
  ([#100](https://github.com/tailscale/tailcat/issues/100))
- Fixed argument parsing under Termux on Android, whose loader inserts
  the executable's path as an extra argument.
  ([#92](https://github.com/tailscale/tailcat/pull/92), [@shaunlee](https://github.com/shaunlee))
- The linux binaries now work when run directly on Android, under
  Termux, `adb shell`, or a rooted shell. Android has no
  `/etc/resolv.conf`, so a plain Go binary there could not resolve any
  name and failed at startup fetching the DERP map; it also found no
  CA roots and could not enumerate network interfaces. tailcat now
  links tailscale.com's `androiddns` and `androidbin` features, which
  detect Android at runtime, resolve names through Android's DNS
  resolver daemon, use the system certificate store, and fall back to
  a synthetic single interface. On regular Linux they do nothing.
  ([#117](https://github.com/tailscale/tailcat/issues/117), reported
  by [@risharde](https://github.com/risharde))
- Updated the tailscale.com dependency to its 2026-09-16 main branch,
  which brings data path performance work from wireguard-go and
  gVisor. wireguard-go now moves each batch of packets through one
  buffer of about 128 KiB instead of a separate buffer per packet,
  which in upstream's iperf3 benchmarks between two Linux machines
  raised throughput by 7% to 35% depending on the workload and cut
  peak memory for TCP transfers by half to three quarters. Small
  outbound packets such as keepalives and handshakes now use 2 KiB
  buffers, so packets waiting on a peer with no active session hold
  at least 97% less memory than before. gVisor's TCP stack, which
  carries every tailcat connection, now uses CUBIC congestion control
  and RACK loss detection; both had been switched off because of
  gVisor bugs that have since been fixed upstream.
- tailcat is on the [Snap Store](https://snapcraft.io/tailcat) as a
  community-maintained, strictly confined snap; see INSTALL.md for
  where its config lives.
- tailcat now has a Bluesky account for release and project news:
  [@tailcat.dev](https://bsky.app/profile/tailcat.dev).

## Changelog
* 15ab9e68bfc6534a61797d7af28cedd42b54a3a5 tailcat: report peers in Server.Status so callers can see direct vs relayed
* 6b106129b8877006744f19082cb6d0d02a3d2b15 cmd/tailcat: use SFTP when scp supports it
* 79dc7eff30d78fbe9a2c69c725eb05c82d0d542d all: bump tailscale.com, run on Android, fix e2e test deadlock
* 9777a392e9f845d1223751d68b399485c14e893d cmd/tailcat: fix nil Process crash in two e2e test timeouts
* 6b73a2691cb6ff3a8ef0f8a99055762466ffd772 INSTALL.md: drop -t from the docker run example
* cbbabaf30e18efbb02b28ac1a8126193354c7f19 README.md, INSTALL.md: move install instructions to their own page
* ece58d81946ea830b8c17a3372a18fb4ce0ae8ef cmd/tailcat: fix ETXTBSY flake starting test-built binaries
* 57b8ce5743d4471f65ad0334574505a0625bb9bf CHANGELOG.md: add unreleased entries for changes since v0.6.0
* d0d599161bde327fb41db30cfd8da84c8715d47c cmd/tailcat: forward UDP through --serve=exit-node
* 5ceb16639064e52064589d1c4be5d26dae585477 cmd/tailcat, internal/localhostdns: fix serving local ports from Windows
* fd101889796a947ac514e9d86ec731af2965fad3 tailcat: add Server.Listen for net.Listener-style TCP and UDP serving
* 91dc4979bd4ae88af6ae2c8bb549616de4bcaa5a cmd/tailcat: add a browse command and a forward --open-browser flag
* 7a50a1abd8bca63432afbcc5c04dd278c7029e31 cmd/tailcat, tailcat: add an exec service and an SSH forced command
* 12339608d78cae95598803da203ad8f8b4178557 cmd/tailcat: warn about public DNS in root help and at no-auth-ssh startup
* 5a83b9f9e119aad6b558cbc122d94efdca87452d cmd/tailcat, README.md: warn when a DNS-named SSH destination is wide open
* b3aeffb34d8f51c30143911e5e0fa06fd7f28ff9 cmd/tailcat: fix argument parsing under Termux on Android

