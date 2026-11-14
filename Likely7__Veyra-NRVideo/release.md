tag: v2.1.5
name: Veyra 2.1.5
published_at: 2026-11-10T15:31:15Z
prerelease: False

## Veyra 2.1.5 更新说明

## 采集预览

- **改善开启去重后的补帧节奏。** 例如 40 FPS 游戏通过 60 Hz 采集时，去重后相邻有效画面的到达间隔会在约 17 和 33 ms 之间交替。现在图内补帧按去重后的内容时间轴安排呈现，减少相邻帧忽快忽慢的情况。
- **校正部分采集设备报告的异常帧时间戳。** 当原始采集回调稳定、驱动时间戳持续明显偏离时，预览按实际采集节奏推进。正常的 59.94 / 60 Hz 时间戳照常使用。音频同步继续读取驱动原始时间。
- **本机数据。** T911 采集 4K60 NV12、约 40 FPS 内容、VFG 3 倍的 A/B 中，提交帧率保持约 120 FPS，提交间隔 P99 从 17.33 ms 降到 9.04 ms，界面 1% low 中位数从 57.66 升到 110.03 FPS。真实帧从采集回调到呈现提交返回的中位耗时由 24.12 ms 增至 31.54 ms。以上为软件侧计时。

## 下载与设置

选择与 Veyra 实际使用显卡匹配的 **NVIDIA** 或 **AMD** 便携包，完整解压并运行 veyra_qml_ui.exe。可在退出 2.1.4 后覆盖解压同显卡包。若解压到新目录，复制旧目录的 runtime_local/user-data-2.0.0 和自定义 runtime_local/luts。自定义数据目录以「设置 → 关于」显示为准。

已安装的 VB-CABLE 可继续使用。便携包中的社区实验增强运行时、版本、许可和哈希见包内清单。

## English

- Improved frame pacing after duplicate-frame removal for capture preview. Graph-based frame generation now schedules presentation on the deduplicated content timeline, reducing uneven delivery when capturing 40 FPS content at 60 Hz.
- Raw capture preview corrects timestamps when the device reports a persistent mismatch against stable callback cadence. Valid 59.94 / 60 Hz timestamps pass through, and audio sync retains the original driver timing.
- In a T911 4K60 NV12 test with approximately 40 FPS content and VFG 3×, the P99 interval between presentation submissions fell from 17.33 to 9.04 ms at roughly 120 submitted FPS. Median capture callback to Present return for real frames rose from 24.12 to 31.54 ms.
- Exit Veyra before overwriting 2.1.4 with the matching GPU package, or extract to a new folder and copy runtime_local/user-data-2.0.0 and any custom runtime_local/luts. Existing VB-CABLE installations are reused.

[完整提交记录](https://github.com/Likely7/Veyra-NRVideo/compare/v2.1.4...v2.1.5) · [对应源码](https://github.com/Likely7/Veyra-NRVideo/releases/tag/v2.1.5-sources)

## 支持与反馈 / Support & feedback

<p align="center">
  <a href="https://discord.gg/qetVZTRkC"><img src="https://img.shields.io/badge/Discord-Join%20Community-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Join Veyra on Discord" height="36"></a>
  &nbsp;&nbsp;
  <a href="https://www.patreon.com/cw/Likely7" title="Patreon 主页 / Creator page"><img src="https://raw.githubusercontent.com/Likely7/Veyra-NRVideo/main/docs/images/support/patreon-home.svg" alt="Patreon 主页 / Creator page" height="36"></a>
  &nbsp;&nbsp;
  <a href="https://www.patreon.com/Likely7/posts/buy-me-coffee-175018110" title="请我喝杯咖啡 · US$5 / Coffee support"><img src="https://raw.githubusercontent.com/Likely7/Veyra-NRVideo/main/docs/images/support/patreon-coffee.svg" alt="☕ 请我喝杯咖啡 · US$5 / Coffee support" height="36"></a>
</p>

<p align="center">
  Patreon 主页查看作者动态；☕ 咖啡按钮直达 US$5 赞助页面。<br>
  Visit the creator page for updates, or open the US$5 coffee support page.
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/Likely7/Veyra-NRVideo/v1.4.0/docs/images/1.4.0/donate-wechat.jpg" alt="微信赞助" width="220">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://raw.githubusercontent.com/Likely7/Veyra-NRVideo/fdc626547b4020b888efd8d420d6dc28743b0d88/docs/images/community/group-10-20261111.png" alt="Veyra 交流群 10" width="220">
</p>

左：微信赞助（自愿，不影响功能）；右：交流群 10。群码按图片标注于 **2026-11-18 前**有效，过期请查看仓库更新。

Left: optional donation; right: community group 10. QR valid before 2026-11-18.

[Veyra 软件知识库 / Knowledge base](https://qcnv4i7tnd7l.feishu.cn/wiki/space/7688258025282358221?ccm_open_type=lark_wiki_spaceLink&open_tab_from=wiki_home)：四个群聊汇总的使用文档，涵盖软件与采集卡常见问题。

[加入 Veyra Discord](https://discord.gg/qetVZTRkC)
