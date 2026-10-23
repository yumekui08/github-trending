tag: v4.0-13d
name: 紫微斗数开源解读数据集 v4.0 · 67.5 万命盘 × 13 维（2026-10-15）
published_at: 2026-10-15T15:24:32Z
prerelease: False

## 紫微斗数开源解读数据集 v4.0（2026-10-15）

**674,976 张命盘 × 13 维 = 8,774,688 段解读**，公历 1950–2026 年每一个真实日期 × 12 时辰 × 男女。

用 2026-10-15 版网站断语库确定性生成（不经 AI），13 个分析维度已按倪海厦《天纪》逐字稿与《紫微斗数全书》原文逐句校正：查不到出处的引文删去或换成逐字可查的原话（倪师原话注明《天纪》集数与时间码），不会发生的四化相关句子删去，有条件的断语写明条件。

### 文件
- `year-1950.jsonl.zst` … `year-2026.jsonl.zst`：每年一个，每行一张盘（JSON Lines），单个约 2MB，解压后约 700MB
- `ziwei-interp-v4-all.tar`：以上全部 + 清单，一次下载（161MB）
- `MANIFEST.json`：每年的盘数、大小、SHA-256；`SHA256SUMS.txt`：校验
- 合计：压缩后 161MB，解压后约 57GB

### 解压
```bash
zstd -d --long=27 year-1990.jsonl.zst     # --long=27 必须带
shasum -a 256 -c SHA256SUMS.txt --ignore-missing
```

字段说明、口径与引用方式见仓库 README「二·新」一节。

### 许可
**CC BY 4.0，可自由商用，唯一要求是保留来源标注**（见 DATASET-LICENSE）。解读里引用的倪海厦《天纪》原话不属于本数据集的授权范围：它们是注明集数与时间码的简短引用，著作权归原权利人；要单独成批使用这些原话，按仓库第五章倪师原话的 CC BY-NC-SA 4.0 处理。《紫微斗数全书》原文属公有领域。

---

**Ziwei Doushu open interpretation dataset v4.0** — 674,976 charts × 13 topics (8,774,688 readings), every real solar date 1950–2026 × 12 double-hours × male/female. Generated deterministically (no AI) by the 2026-10-15 judgment library, revised sentence by sentence against the verbatim transcripts of Ni Haixia's *Tian Ji* and the original *Complete Book of Zi Wei Dou Shu*. 161 MB compressed (zstd, decompress with `--long=27`), about 57 GB uncompressed. License: CC BY 4.0 with attribution. Quotations from *Tian Ji* inside the readings are not covered by this license (short cited excerpts; copyright remains with the rights holder; bulk reuse falls under the repo's CC BY-NC-SA 4.0 terms for Master Ni's words).
