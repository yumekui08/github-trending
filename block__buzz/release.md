tag: desktop-v0.5.30
name: Buzz Desktop v0.5.30
published_at: 2026-11-14T00:31:43Z
prerelease: False


### Desktop and shared changes

- feat(db): label advisory-lock metrics with the locked event kind ([#9472](https://github.com/block/buzz/pull/9472)) ([`359839f70b6ec2401207c9fb29116efc87b75701`](https://github.com/block/buzz/commit/359839f70b6ec2401207c9fb29116efc87b75701))

### Other repository changes

- perf(mobile): parse each event's thread reference once ([#9460](https://github.com/block/buzz/pull/9460)) ([`bf422ac8e1a34893e15c91bfc86a74d990547feb`](https://github.com/block/buzz/commit/bf422ac8e1a34893e15c91bfc86a74d990547feb))
- perf(mobile): load only the directory when search opens ([#9466](https://github.com/block/buzz/pull/9466)) ([`c97c85d8faee7aee989f5a110e38cd38eff551b2`](https://github.com/block/buzz/commit/c97c85d8faee7aee989f5a110e38cd38eff551b2))
- perf(mobile): stop rebuilding Home's channel list when a route covers it ([#9459](https://github.com/block/buzz/pull/9459)) ([`5f1cd679853b6623582f97154dd0352ccdd1caa3`](https://github.com/block/buzz/commit/5f1cd679853b6623582f97154dd0352ccdd1caa3))
- perf(mobile): ask typing subscriptions only for the typing window ([#9454](https://github.com/block/buzz/pull/9454)) ([`3764a2e4d500bf36c434670b2597b02b289354ee`](https://github.com/block/buzz/commit/3764a2e4d500bf36c434670b2597b02b289354ee))
- perf(mobile): skip avatar URL parsing for non-HTTP URLs ([#9448](https://github.com/block/buzz/pull/9448)) ([`11ea8c928efb17528ed6033dbeb8e6035d135203`](https://github.com/block/buzz/commit/11ea8c928efb17528ed6033dbeb8e6035d135203))
- perf(mobile): download the identity archive list only when it changed ([#9445](https://github.com/block/buzz/pull/9445)) ([`5e52fa98313a7e646e994e47c5a36a88f4cd707f`](https://github.com/block/buzz/commit/5e52fa98313a7e646e994e47c5a36a88f4cd707f))
- perf(mobile): don't treat a Control Center pull as a resume ([#9443](https://github.com/block/buzz/pull/9443)) ([`9e40bf5d795848927547d5d6dd21ba0c9e37a40d`](https://github.com/block/buzz/commit/9e40bf5d795848927547d5d6dd21ba0c9e37a40d))
- fix(mobile): keep a superseded roster read out of the offline snapshot ([#9452](https://github.com/block/buzz/pull/9452)) ([`15c65c76d93ac677c17001b4337b0e608cf810ed`](https://github.com/block/buzz/commit/15c65c76d93ac677c17001b4337b0e608cf810ed))
- perf(mobile): read channel bot roles from the member list ([#9451](https://github.com/block/buzz/pull/9451)) ([`99e65b6c22dcd78658715b6dae06aa9febf14ed3`](https://github.com/block/buzz/commit/99e65b6c22dcd78658715b6dae06aa9febf14ed3))
- perf(mobile): read Activity once per reconnect ([#9455](https://github.com/block/buzz/pull/9455)) ([`3dcdf1c0562fb77cc724d9cb425f9156db24204b`](https://github.com/block/buzz/commit/3dcdf1c0562fb77cc724d9cb425f9156db24204b))
- fix(mobile): offer role controls for agents ([#9475](https://github.com/block/buzz/pull/9475)) ([`04af7081c87ac14cabc61bd8b4f95aa2ef0ce809`](https://github.com/block/buzz/commit/04af7081c87ac14cabc61bd8b4f95aa2ef0ce809))
- perf(mobile): stop rebuilding the native nav bar on every scrolled frame ([#9458](https://github.com/block/buzz/pull/9458)) ([`b6db61faa0fcb467ce523e1bacae917f1f588fb9`](https://github.com/block/buzz/commit/b6db61faa0fcb467ce523e1bacae917f1f588fb9))
- perf(mobile): keep verified-name batches open as people are added ([#9450](https://github.com/block/buzz/pull/9450)) ([`93bbd452a71827d1905a44ceafc687c1f93dcf9f`](https://github.com/block/buzz/commit/93bbd452a71827d1905a44ceafc687c1f93dcf9f))
- perf(mobile): read only changed custom emoji sets on reconnect ([#9446](https://github.com/block/buzz/pull/9446)) ([`9fc2b333202cd94f9a29538950f29e1420411095`](https://github.com/block/buzz/commit/9fc2b333202cd94f9a29538950f29e1420411095))
- perf(mobile): keep latest-message times on a directory load ([#9457](https://github.com/block/buzz/pull/9457)) ([`237a39fe765d9ffd7848ed4a6036cd78a955d5cf`](https://github.com/block/buzz/commit/237a39fe765d9ffd7848ed4a6036cd78a955d5cf))
- perf(mobile): don't refetch profiles that are already on the wire ([#9447](https://github.com/block/buzz/pull/9447)) ([`a540e7bd3067a036329fefa52b48b7f12761b660`](https://github.com/block/buzz/commit/a540e7bd3067a036329fefa52b48b7f12761b660))
- perf(mobile): use HTTP/2 on Android through app-wide Cronet engines ([#9435](https://github.com/block/buzz/pull/9435)) ([`d1a8c3607dfbaf69ce34f2c765dc69279a92c62b`](https://github.com/block/buzz/commit/d1a8c3607dfbaf69ce34f2c765dc69279a92c62b))
- perf(mobile): subscribe to presence only for people on screen ([#9444](https://github.com/block/buzz/pull/9444)) ([`36fa0fe318e34eeb916a77e5833a7fbd736ad24c`](https://github.com/block/buzz/commit/36fa0fe318e34eeb916a77e5833a7fbd736ad24c))
- fix(mobile): require Builderlab consent for existing identities ([#8823](https://github.com/block/buzz/pull/8823)) ([`59ae028a360242d43ffbfdafca8a76eda00484d9`](https://github.com/block/buzz/commit/59ae028a360242d43ffbfdafca8a76eda00484d9))
- feat(mobile): use HTTP/2 on iOS through app-wide URLSessions ([#8897](https://github.com/block/buzz/pull/8897)) ([`a2d4ba02677f157a95ae0d84ef3be37953a7ed24`](https://github.com/block/buzz/commit/a2d4ba02677f157a95ae0d84ef3be37953a7ed24))
- fix(relay): publish a git push only when refs changed; check the protocol by refinement ([#9425](https://github.com/block/buzz/pull/9425)) ([`1fb33e4545660196d4c863daf70e1d3bc245f164`](https://github.com/block/buzz/commit/1fb33e4545660196d4c863daf70e1d3bc245f164))
- fix(mobile): show shared chats under Solo ([#9348](https://github.com/block/buzz/pull/9348)) ([`642ce4165cc84d67b99f25b05444dbfff456bce7`](https://github.com/block/buzz/commit/642ce4165cc84d67b99f25b05444dbfff456bce7))

[Compare desktop-v0.5.29...desktop-v0.5.30](https://github.com/block/buzz/compare/desktop-v0.5.29...desktop-v0.5.30)

