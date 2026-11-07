tag: v1.27.0
name: v1.27.0
published_at: 2026-11-04T17:04:23Z
prerelease: False

This week's release includes syntax highlighting for Go 1.27 generic methods, an option to open README files by default, and AI commit messages that follow your repository's recent commit style.

## Features

### AI

- Improved Agent Panel memory usage by loading tool-call diffs and parsing thread message Markdown only when first viewed, instead of when loading a thread. ([#65444](https://github.com/zed-industries/zed/pull/65444), [#65470](https://github.com/zed-industries/zed/pull/65470); thanks [Vanuan](https://github.com/Vanuan))
- Improved AI commit message generation by using the three most recent repository commit messages as style examples. ([#61528](https://github.com/zed-industries/zed/pull/61528); thanks [matheuslrd](https://github.com/matheuslrd))
- Improved CPU usage and disk reads while the agent was working, especially with a long thread history. ([#66015](https://github.com/zed-industries/zed/pull/66015))

### Git

- Added missing tooltips to the close, commit message, and "View on" buttons in the Git Graph's commit details panel. ([#66016](https://github.com/zed-industries/zed/pull/66016); thanks [skmanoj322](https://github.com/skmanoj322))
- Improved Git Graph rendering performance. ([#66180](https://github.com/zed-industries/zed/pull/66180); thanks [RemcoSmitsDev](https://github.com/RemcoSmitsDev))
- Improved the Git Panel's error message when a push was rejected because the local branch was behind the remote, explaining that remote changes must be fetched and integrated before pushing again. ([#47296](https://github.com/zed-industries/zed/pull/47296); thanks [Aladiah96](https://github.com/Aladiah96))

### Languages

- Added syntax highlighting for Go 1.27 generic methods. ([#64562](https://github.com/zed-industries/zed/pull/64562); thanks [ndellosa95](https://github.com/ndellosa95))

### Other

- Added an option to open README files by default by setting `on_new_window` to `"readme"`. ([#65389](https://github.com/zed-industries/zed/pull/65389))
- Improved the Project Panel error message when moving a file or folder onto a location where one with the same name already existed. ([#64344](https://github.com/zed-industries/zed/pull/64344); thanks [zaugust4891](https://github.com/zaugust4891))

## Bug Fixes

- Fixed Solargraph completions crashing Zed in certain cases. ([#66157](https://github.com/zed-industries/zed/pull/66157))
- Fixed "Zed quit unexpectedly" appearing when quitting with `cmd-q` on macOS. ([#66158](https://github.com/zed-industries/zed/pull/66158))
- Fixed a crash when Tree-sitter syntax highlighting failed. ([#66474](https://github.com/zed-industries/zed/pull/66474))
- Fixed a crash when adding surrounding characters (`m s`) to adjacent selections in Helix mode. ([#66107](https://github.com/zed-industries/zed/pull/66107); thanks [bugprone](https://github.com/bugprone))
- Fixed a hang in Vim visual-block mode at the end of a wrapped file. ([#66118](https://github.com/zed-industries/zed/pull/66118))
- Fixed child filesystem watches losing events when a covering parent watch was removed. ([#65998](https://github.com/zed-industries/zed/pull/65998))
- Fixed collapsed inline diff hunks producing invalid word-diff highlights for multibyte UTF-8 text. ([#65829](https://github.com/zed-industries/zed/pull/65829); thanks [Blazearth](https://github.com/Blazearth))
- Fixed external agents' tool call locations opening one line below the line the agent reported. ([#66110](https://github.com/zed-industries/zed/pull/66110))
- Fixed Git Graph rendering lagging behind when opening or closing the commit details panel. ([#66132](https://github.com/zed-industries/zed/pull/66132); thanks [RemcoSmitsDev](https://github.com/RemcoSmitsDev))
- Fixed inline review switching to a subagent's edits when the subagent started. ([#66093](https://github.com/zed-industries/zed/pull/66093))
- Fixed language server formatting requests sometimes applying incorrect changes. ([#65856](https://github.com/zed-industries/zed/pull/65856))
- Fixed language server setup failing with `EBADDEVENGINES` in Yarn and pnpm projects. ([#65280](https://github.com/zed-industries/zed/pull/65280); thanks [latin-1](https://github.com/latin-1))
- Fixed language servers receiving change and save notifications for files outside their dynamically registered document selectors, including unrelated files in the project. ([#65253](https://github.com/zed-industries/zed/pull/65253); thanks [aviatesk](https://github.com/aviatesk))
- Fixed LLM credentials being read when `disable_ai` was set to `true`. ([#66029](https://github.com/zed-industries/zed/pull/66029))
- Fixed missed filesystem events for case-insensitive watches registered with trailing separators or equivalent path spellings. ([#65995](https://github.com/zed-industries/zed/pull/65995))
- Fixed missing Git repository, worktree, and branch names in the title bar for Windows remote projects opened in a repository subfolder. ([#66142](https://github.com/zed-industries/zed/pull/66142); thanks [lingyaochu](https://github.com/lingyaochu))
- Fixed missing thinking output from OpenAI-compatible Responses endpoints that emitted reasoning-text events. ([#65938](https://github.com/zed-industries/zed/pull/65938))
- Fixed on-type formatting after pressing `enter` being applied before the new line's indentation, which left the cursor after text inserted by language servers such as Ruby LSP. ([#65769](https://github.com/zed-industries/zed/pull/65769); thanks [JacobNWolf](https://github.com/JacobNWolf))
- Fixed remote projects (SSH, WSL) becoming unresponsive when loading an agent thread that referred to many files outside the project. ([#65189](https://github.com/zed-industries/zed/pull/65189); thanks [coinman-dev](https://github.com/coinman-dev))
- Fixed renaming files, creating files, and renaming terminal tabs being cancelled when `focus_follows_mouse` was enabled and the mouse moved. ([#66167](https://github.com/zed-industries/zed/pull/66167))
- Fixed retryable provider failures in OpenAI-compatible chat streams not being recognized as retryable. ([#66038](https://github.com/zed-industries/zed/pull/66038))
- Fixed right-click menus and popup pickers closing when the mouse moved to another pane with `focus_follows_mouse` enabled. ([#66173](https://github.com/zed-industries/zed/pull/66173))
- Fixed sandboxed agent terminal commands incorrectly reporting failure under dash on Linux. ([#64439](https://github.com/zed-industries/zed/pull/64439); thanks [NHendrickson9616](https://github.com/NHendrickson9616))
- Fixed SSH connections failing when usernames containing `/` or `\` were percent-encoded. ([#64744](https://github.com/zed-industries/zed/pull/64744); thanks [ryanabx](https://github.com/ryanabx))
- Fixed status bar panel buttons doing nothing when another panel in the same dock was zoomed. ([#66119](https://github.com/zed-industries/zed/pull/66119); thanks [ybelmach](https://github.com/ybelmach))
- Fixed streaming connection failures being classified as non-retryable errors for Google AI and OpenAI Responses model requests. ([#65940](https://github.com/zed-industries/zed/pull/65940))
- Fixed the automatically installed Delve debugger for Go not updating after its initial installation. ([#66025](https://github.com/zed-industries/zed/pull/66025))
- Fixed changes to `focus_follows_mouse` not applying to docks until Zed was restarted. ([#66161](https://github.com/zed-industries/zed/pull/66161))
- Fixed deleted files remaining in the File Finder's history. ([#65660](https://github.com/zed-industries/zed/pull/65660))
- Fixed duplicating files or folders in the Project Panel overwriting clipboard contents. ([#60894](https://github.com/zed-industries/zed/pull/60894); thanks [shindgew](https://github.com/shindgew))
- Fixed external stash renames not being reflected in the stash picker. ([#55294](https://github.com/zed-industries/zed/pull/55294))
- Fixed failed model-list fetches, such as