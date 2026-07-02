# Claude Review Brief

日期：2026-06-28

## 1. 项目真正目标

项目不是泛化写剧本工具。

当前真实目标是：

1. 从用户自有旧剧本中提取“爆款短剧的强机制”
2. 支持按甲方要求做深度重构，而不是低级改名洗稿
3. 最终能生成新的海外真人短剧剧本
4. 后续还能交给 AI 视频生产链继续拆分镜、资产和提示词

核心优先级顺序应为：

```text
分析强机制
-> 判断什么强什么弱
-> 做重构方案
-> 再考虑完整生成
```

## 2. 用户关键约束

- 目标市场：海外真人短剧
- 生产方式：AI 视频生产
- 用户不接受：
  - 空泛大而全评分器
  - 一上来就从零写一整套大系统
  - 只靠私有样本和拍脑袋标准
  - 只看电影/长片那套资料
- 用户接受：
  - 参考现成项目/平台/框架
  - 用多 agent 做独立判断
  - 先把问题理清再做下一步

## 3. 已经做过的事

### 3.1 外部研究

已做了这些文档：

- `/Users/jiakun/Codex/自动化编剧/research/short-drama-script-agent-external-research-2026-06-28.md`
- `/Users/jiakun/Codex/自动化编剧/research/short-drama-agent-landscape-2026-06-28.md`

内容包括：

- 海外 analysis / coverage 平台
- 中文短剧诊断/生产平台
- 开源 AI 短剧生产链
- 海外短剧市场

### 3.2 私有样本接入

通过飞书 Base 接入了 4 份剧本样本。

当前已有：

- `灰烬新生`
- `真心错付的冰刀女王`
- `阿尔法的命定孕妻`
- `流放3年归来-1-30集-中英台词对照`

### 3.3 已做 blind-style 评测探索

已有：

- V1 blind rubric
- V2 blind rubric
- V3 blind rubric
- blind eval protocol
- first-pass feature discovery
- blind comparison v2

文档：

- `/Users/jiakun/Codex/自动化编剧/analysis/blind-eval-protocol-2026-06-28.md`
- `/Users/jiakun/Codex/自动化编剧/analysis/blind-eval-2026-06-28/common-rubric-v1.md`
- `/Users/jiakun/Codex/自动化编剧/analysis/blind-eval-2026-06-28/common-rubric-v2.md`
- `/Users/jiakun/Codex/自动化编剧/analysis/blind-eval-2026-06-28/common-rubric-v3.md`
- `/Users/jiakun/Codex/自动化编剧/analysis/blind-eval-2026-06-28/comparison-v2.md`

## 4. 当前已经确认的问题

### 4.1 不是不会分析，而是判别器拉不开强弱

blind 测试结果显示：

- V1：4 份样本全是 `medium`
- V2：只有一份掉到 `weak`
- 其余仍然在 `medium`

说明：

- 稳定性还行
- 区分度不够

### 4.2 主要症结

我们怀疑根因包括：

1. 目标函数混了  
   叙事强度、AI视频适配、合规、市场全揉在一起

2. 主评分维度不对  
   `hook_strength / stakes / retention` 在强弱稿里都可能很高

3. 真正有区分力的维度还没被提到最核心  
   如：
   `choice_density`
   `agency_balance`
   `anti_repetition`
   `control_without_relationship_growth`

5. 现有文档和探索结果变多了，但还没有一个真正收束的主规范

### 4.3 用户刚刚新增的关键反馈

用户认为：

- `能不能拍` 在当前阶段不重要，应聚焦 `AI视频适配`
- `合规风险` 和 `市场适配` 目前不是核心评分项
- 真正担心的不是“过拟合”这个词，而是：
  如果什么维度都想兼顾，最终会变得臃肿、难看、逻辑冲突
- 需要你帮忙判断：
  到底是不是项目方向本身已经乱了

## 5. 关于“要不要从头做”的初步判断

当前初步判断是：

- orchestration 不必从零写
- 可考虑 `LangGraph` 做底座
- 开源工作台里：
  - `LocalMiniDrama` 最像能直接借
  - `Jellyfish` / `Toonflow` 适合拆模块
  - 闭源平台里 `Coze` / `LibTV` 有一定接口价值

但这仍是我们自己的判断，用户希望再做外部复核。

## 6. 你需要重点审查的东西

请你不要再泛泛讲行业，而是重点看以下问题：

1. **项目是否已经偏离主目标？**
   当前项目到底是在做：
   - 剧本分析器
   - 剧本重构器
   - judge pipeline
   - 生产工作台
   还是已经全混了？

2. **当前评判器的问题到底是什么？**
   - 是维度太多？
   - 是加权不对？
   - 是 schema 不对？
   - 是根本不该先做 absolute scoring？

3. **V3 方向对不对？**
   当前 V3 想做的是：
   - 主引擎优先
   - 只保留 5 个核心 narrative 维度
   - AI视频适配 / 合规 / 市场改为约束/标签
   - 加 `pseudo_strength_penalty`
   - 后续引入 pairwise comparison

   请你判断这个方向是否靠谱，还是还有更好的拆法。

4. **现成框架到底该怎么借？**
   我们当前判断是：
   - 不整仓接盘
   - 模块级复用
   - orchestration 直接借成熟框架
   请你判断这个方向是否正确。

5. **接下来唯一最值的一步是什么？**
   不要给 10 个建议，只给最值的 1-3 个。

## 7. 你可以直接看的文件

优先看这些：

- `/Users/jiakun/Codex/自动化编剧/docs/script-transformation-agent-spec-2026-06-28.md`
- `/Users/jiakun/Codex/自动化编剧/docs/script-agent-architecture-and-eval-plan-2026-06-28.md`
- `/Users/jiakun/Codex/自动化编剧/docs/决策与变更.md`
- `/Users/jiakun/Codex/自动化编剧/analysis/blind-eval-protocol-2026-06-28.md`
- `/Users/jiakun/Codex/自动化编剧/analysis/blind-eval-2026-06-28/common-rubric-v2.md`
- `/Users/jiakun/Codex/自动化编剧/analysis/blind-eval-2026-06-28/common-rubric-v3.md`
- `/Users/jiakun/Codex/自动化编剧/analysis/blind-eval-2026-06-28/comparison-v2.md`
- `/Users/jiakun/Codex/自动化编剧/research/short-drama-agent-landscape-2026-06-28.md`

## 8. 输出要求

请你按下面顺序回答：

1. 你认为当前项目最核心的问题是什么
2. 现有方向里哪些是对的，哪些该砍
3. 评判器到底应该怎么收缩
4. 是不是应该继续走“模块级复用，不整仓接盘”
5. 下一步最值的 1-3 个动作

## 9. 可读材料总索引

你可以自由决定读哪些，但不要抱着“只看一个文件就下结论”的方式。下面这些都在本地：

### A. 主文档

- `/Users/jiakun/Codex/自动化编剧/docs/script-transformation-agent-spec-2026-06-28.md`
- `/Users/jiakun/Codex/自动化编剧/docs/script-agent-architecture-and-eval-plan-2026-06-28.md`
- `/Users/jiakun/Codex/自动化编剧/docs/决策与变更.md`

### B. 评估相关

- `/Users/jiakun/Codex/自动化编剧/analysis/blind-eval-protocol-2026-06-28.md`
- `/Users/jiakun/Codex/自动化编剧/analysis/blind-eval-2026-06-28/common-rubric-v1.md`
- `/Users/jiakun/Codex/自动化编剧/analysis/blind-eval-2026-06-28/common-rubric-v2.md`
- `/Users/jiakun/Codex/自动化编剧/analysis/blind-eval-2026-06-28/common-rubric-v3.md`
- `/Users/jiakun/Codex/自动化编剧/analysis/blind-eval-2026-06-28/comparison-template.md`
- `/Users/jiakun/Codex/自动化编剧/analysis/blind-eval-2026-06-28/comparison-v2.md`
- `/Users/jiakun/Codex/自动化编剧/analysis/blind-eval-2026-06-28/script-manifest.yaml`

### C. 第一轮样本抽取

- `/Users/jiakun/Codex/自动化编剧/analysis/first-pass-2026-06-28/first-pass-structured-extraction.md`
- `/Users/jiakun/Codex/自动化编剧/analysis/first-pass-2026-06-28/first-pass-structured-extraction.yaml`

### D. 外部研究

- `/Users/jiakun/Codex/自动化编剧/research/short-drama-script-agent-external-research-2026-06-28.md`
- `/Users/jiakun/Codex/自动化编剧/research/short-drama-agent-landscape-2026-06-28.md`

### E. 当前样本文本

- `/Users/jiakun/Codex/自动化编剧/input/feishu-base-samples-2026-06-28/[修改版]灰烬新生.txt`
- `/Users/jiakun/Codex/自动化编剧/input/feishu-base-samples-2026-06-28/Ice Blade Queen Love in Vain_双语台词版_全集.txt`
- `/Users/jiakun/Codex/自动化编剧/input/feishu-base-samples-2026-06-28/[修改版]阿尔法的命定孕妻-1-31集-中英台词.txt`
- `/Users/jiakun/Codex/自动化编剧/input/feishu-base-samples-2026-06-28/流放3年归来-1-30集-中英台词对照.txt`

### F. 当前样本原始文件

- `/Users/jiakun/Codex/自动化编剧/input/feishu-base-samples-2026-06-28/[修改版]灰烬新生.docx`
- `/Users/jiakun/Codex/自动化编剧/input/feishu-base-samples-2026-06-28/Ice Blade Queen Love in Vain_双语台词版_全集.docx`
- `/Users/jiakun/Codex/自动化编剧/input/feishu-base-samples-2026-06-28/[修改版]阿尔法的命定孕妻-1-31集-中英台词.docx`
- `/Users/jiakun/Codex/自动化编剧/input/feishu-base-samples-2026-06-28/流放3年归来-1-30集-中英台词对照.docx`

### G. 目录本身

- `/Users/jiakun/Codex/自动化编剧/docs/`
- `/Users/jiakun/Codex/自动化编剧/analysis/`
- `/Users/jiakun/Codex/自动化编剧/research/`
- `/Users/jiakun/Codex/自动化编剧/input/feishu-base-samples-2026-06-28/`
