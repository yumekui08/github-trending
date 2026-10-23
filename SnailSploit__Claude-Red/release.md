tag: v0.3.0
name: v0.3.0 — 78 Skills, 23 Categories, Full Wireless Suite
published_at: 2026-08-30T11:02:25Z
prerelease: False

## What's New

Major expansion — claude-red goes from 37 skills in flat directories to **78 skills across 23 organized categories**. This release adds full-spectrum offensive coverage from container escapes to wireless protocol attacks.

### 20 New Skills Across 10 Categories

- **container/** — Docker/containerd breakout, runc CVEs, K8s RBAC abuse, etcd, kubelet API, pod escape
- - **cicd/** — GitHub Actions injection, Jenkins RCE, GitLab CI, secret extraction, OIDC federation
- - **api/** — OWASP API Top 10, REST/gRPC/WebSocket, batching attacks, webhook hijacking
- - **crypto/** — Padding oracle, ECB, hash extension, RSA, POODLE/DROWN/Heartbleed, pinning bypass
- - **privesc/** — Linux SUID/capabilities/sudo/kernel + Windows Potato family, DLL hijacking, UAC bypass
- - **post-exploitation/** — Lateral movement (PTH/PTT/NTLM relay), persistence (Golden/Silver tickets), data exfiltration (DNS/HTTPS/ICMP tunneling)
- - **forensics/** — Anti-forensics (timestomping, ADS, anti-VM) + C2 frameworks (Cobalt Strike, Sliver, Mythic, Havoc)
- - **supply-chain/** — Dependency confusion, typosquatting, build pipeline attacks
- - **social-engineering/** — GoPhish, EvilGinx2, MFA phishing, pretexting, vishing, USB drops
- - **network/** — ARP spoofing, LLMNR/NBT-NS poisoning, VLAN hopping, IPv6 attacks, MITM
### Wireless Suite — 14 Dedicated Skills

Split the monolithic `offensive-wifi` into per-surface skills covering the full wireless attack surface:

`wifi-recon` · `wpa2-psk` · `wpa3-sae` · `wpa-enterprise` · `wps` · `evil-twin` · `krack-fragattacks` · `deauth-disassoc` · `bluetooth-ble` · `bluetooth-classic` · `zigbee-thread-matter` · `z-wave` · `lorawan-sub-ghz` · `wifi` (comprehensive)

### Deep Rewrites (2-4x More Content)

- **offensive-deserialization** — 183 → 781 lines. Java/PHP/.NET/Python/Node/Ruby, K8s vectors, WAF bypass
- - **offensive-graphql** — 207 → 946 lines. Introspection bypass, batching, subscription abuse, CrackQL/BatchQL
- - **offensive-advanced-redteam** — 146 → 640 lines. C2 tradecraft, OPSEC, evasion, engagement planning
- - **offensive-ssti** — 347 → 758 lines. 10+ engine-specific exploits, filter bypass, blind exploitation, chaining
### Infrastructure & Tooling

- Skills reorganized into 23 category subdirectories
- - `claude-skills.json` manifest for programmatic access
- - `install.sh` one-liner installer
- - `convert_skills.py` for Claude Console compatibility (community contribution)
- - GitHub Actions: CodeQL scanning + automated skill review on PRs
- - `SECURITY.md`, `CONTRIBUTING.md`, `LICENSE` (MIT)
### Community Contributions

Thanks to @yogesh-tessl for the skill-review GitHub Action and @LvL23HT for the bulk skill converter.

---

```bash
git clone https://github.com/SnailSploit/claude-red ~/.claude/skills/claude-red
```