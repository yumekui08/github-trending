tag: v0.28.64
name: v0.28.64
published_at: 2026-11-13T17:24:36Z
prerelease: False

Follow [@plannotator](https://x.com/plannotator) on X for updates

<details>
<summary><strong>Missed recent releases?</strong></summary>

| Release | Highlights |
|---|---|
| [v0.28.63](https://github.com/backnotprop/plannotator/releases/tag/v0.28.63) | Pair Grok Bot and other cloud agents from Settings, Hermes Agent, OpenClaw and Muse Code can use the Inbox, add a thread to Priority to keep it on top, tag threads, and find each tag in the sidebar, Pull requests board as a table, with bulk Merge |
| [v0.28.62](https://github.com/backnotprop/plannotator/releases/tag/v0.28.62) | Agents started from the Inbox now work on Windows, pick a model and effort when you start an agent, rules for your agents, written in your own words, post a thread's decisions on its pull request, the Inbox loads faster on a slow connection |
| [v0.28.61](https://github.com/backnotprop/plannotator/releases/tag/v0.28.61) | Updates now update the Claude Code plugin too, an agent's chosen face shows on every icon of it, filter the Inbox list by pull request state, Modern dark shows section bands and the Reply button, one conversation no longer shows as two agents |
| [v0.28.60](https://github.com/backnotprop/plannotator/releases/tag/v0.28.60) | Click a word to highlight it, a one-time Themes dialog, Settings → Rows rebuilt, tell your agent how you want your rows, starred threads as pills above the list, a pill for new messages out of view, a half-circle face picker with ten Glass colours, a new phone sidebar and reply box |
| [v0.28.59](https://github.com/backnotprop/plannotator/releases/tag/v0.28.59) | A quieter Agents section in the sidebar, machine names only when agents run on more than one machine, agent icons that are always gently alive and lean toward your pointer |
| [v0.28.58](https://github.com/backnotprop/plannotator/releases/tag/v0.28.58) | Start Codex from New message, an Agents section in the sidebar, start an agent in a folder on any drive, play audio attachments and comment at a moment, Claude Code's Plannotator tools work on Windows |
| [v0.28.57](https://github.com/backnotprop/plannotator/releases/tag/v0.28.57) | Pin artifacts, and see every artifact on one page, filter the list by project, date or agent, a thread shows its pull requests and their state, choose what the sidebar shows, and in what order, Ask AI starts from Side in the selection bar |
| [v0.28.56](https://github.com/backnotprop/plannotator/releases/tag/v0.28.56) | Questions can show trade-offs and a prototype to try, a thread with many big pictures no longer crashes the tab, Escape closes New message and keeps your draft, read threads stop being bold and keep their place, agent messages that name no thread start a new one |
| [v0.28.55](https://github.com/backnotprop/plannotator/releases/tag/v0.28.55) | Floating reply drafts, now a setting under Experimental, open questions sit next to Reply again, a comment box that keeps unsent comments as Drafts, choose how your list looks: Minimal, Balanced or Detailed, update an older linked machine from this Inbox |
| [v0.28.53](https://github.com/backnotprop/plannotator/releases/tag/v0.28.53) | Start an agent in a new folder, or from a git URL, "+" on each project row starts a session there, a reaction tray, a thread's Links, Settings → Activity, New message offers the open thread's files, Bro mode: agents write to you in plain words |
| [v0.28.52](https://github.com/backnotprop/plannotator/releases/tag/v0.28.52) | Start agents from the Inbox, on by default, a new reply box, Ask AI for everyone, Insights in Settings → Decision data, Plannotator reloads itself after an update |
| [v0.28.51](https://github.com/backnotprop/plannotator/releases/tag/v0.28.51) | Starred threads, a note when an agent's session has ended, "Back from snooze", Ask about a past decision, expand arrows in guided reviews |

</details>

## What's New in v0.28.64

### TL;DR

- **Changed:** Installs and updates download a smaller, compressed copy
- **New:** A Videos filter on the Artifacts page
- **Changed:** GitLab comments on a whole file get their own thread
- **Off by default:** Pull request pictures and videos show in the Inbox

0.28.64 is a small release. Installs and updates now download a compressed copy of Plannotator, the Artifacts page can show only videos, and a GitLab comment on a whole file posts as its own thread. It has 5 PRs, all from the maintainer.

### Smaller downloads for installs and updates

Each release now carries compressed copies of the Plannotator binary next to the plain one: a `.tar.xz` for macOS and Linux, and a `.gz` for every platform. On macOS (Apple silicon) the download goes from 195.6 MB to 44.9 MB as `.tar.xz`, or 73.9 MB as `.gz`.

The installers try them in order. On macOS, the install script takes the `.tar.xz`, then the `.gz`, then the plain file. On Linux it takes the `.tar.xz` only when `xz` is installed, and otherwise starts with the `.gz`. On Windows, both `install.ps1` and `install.cmd` take the `.gz`, then the plain file. Each copy is unpacked and checked against the same SHA-256 as the plain binary before anything is replaced. If a copy is missing, fails to download or unpack, or does not match, the installer quietly moves on to the next one. Only the plain file can fail the install, with the same messages as before. The installer prints one new line that names the file it used, such as `Downloaded plannotator-darwin-arm64.tar.xz.`

In a test on a Mac, with the download limited to 2 MB/s, an update took about 24 s with the `.tar.xz`, 36 s with the `.gz` and 94 s with the plain file. Updates from inside Plannotator run the same install script, so they get the smaller download too. Older releases have no compressed copies, so installing one of them downloads the plain file as before. To force the plain download, set `PLANNOTATOR_SKIP_COMPRESSED_DOWNLOAD=1`.

[#3302](https://github.com/backnotprop/plannotator/pull/3302)

### A Videos filter on the Artifacts page

The Artifacts page (the Artifacts row in the sidebar) listed videos, but its filters were Images, Pages, Documents and Other files, and every video counted as an image. There was no way to see only the clips. The page now has a **Videos** filter after Images, and an mp4 or webm sits there instead of under Images. Audio stays under Other files. A thread's own Artifacts grid is unchanged.

[#3304](https://github.com/backnotprop/plannotator/pull/3304)

### GitLab: a comment on a whole file gets its own thread

On a GitLab merge request, a comment on a whole file used to be folded into the review's main note as `**path:** text`. It now posts as its own thread on that file, as it already did on GitHub. This works from `plannotator review` and from the Inbox's Post to GitLab, and was checked on gitlab.com, where each one shows as "started a thread on a file".

If GitLab refuses a file thread, as an older self-hosted GitLab may, that comment goes into the main note as before, so nothing is lost. If the file threads go and the note then fails, a retry sends only what is left, so no file thread is posted twice.

[#3245](https://github.com/backnotprop/plannotator/pull/3245)

### Code review in the Inbox: off by default

This shows only with Code review turned on in Settings → Capabilities.

- **A pull request's own pictures and videos.** On a PR from github.com, the pictures in its description, comments and line threads now show in place, on the PR page and in a thread's full review. Before, each one was a chip saying it opens on the forge. Screenshots written as `<img>` tags, such as before and after pairs in a table, show as pictures too. A click, or Enter or Space, opens a picture full screen in the attachment viewer, and a video GitHub saved as a link plays there on a plain click. The Inbox fetches each file through your own `gh` sign-in, only from GitHub's attachment hosts and only when the PR's text names it. A picture that fails to load stays a chip. GitLab merge requests keep their ch