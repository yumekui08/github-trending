tag: v0.1.1
name: EGM v0.1.1
published_at: 2026-11-06T21:50:31Z
prerelease: False

EGM v0.1.1 updates the plugin listing and packages the current Claude and OpenAI runtimes.

- Clarifies listing copy, adds three OpenAI plugin starter prompts, and separates publisher policy destinations (#316, #314).
- Adds the TRIZ inventive catalyst reviewer and improves review context handling and severity preservation (#299, #289, #279).
- Adds experimental Cursor, OpenCode V1, and GitHub Copilot adapters (#164, #165, #163).

Existing skill names, descriptions, and per-skill prompt files are unchanged by the listing update. No migration is required for that update. The experimental adapters have separate installation and support guidance.

The ZIP checksums and GitHub Actions attestations were verified against the workflow-built artifacts from commit `dea7761de06ce5b51c177ebb9bba0469f24af5a4`. Native end-to-end verification of these exact release ZIPs remains open in #60. Marketplace rollout is tracked separately.
