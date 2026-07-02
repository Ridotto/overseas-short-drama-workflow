# 海外短剧洗稿器 · workflow spec v12 短剧底盘接入候选版

> 日期：2026-07-01  
> 状态：候选重构方案，用于和 v11 小修版对照验证；不替换 PRD，不替换正式 workflow。  
> 上游：`PRD_v4.md`、`workflow_spec_v11_写作前故事包候选版.md`、`架构接线审计_参考资产接入_2026-07-01.md`。  
> 执行协议：必须配合 `workflow_execution_protocol_v1.md`，manifest-first。  

---

## 0. 这版要验证什么

v11 小修版验证的是：

```text
在原流程关键交接点补 4 个存活问，能不能防止短剧能力半路死掉。
```

v12 候选版验证的是：

```text
如果把 0xsline 的短剧生产底盘更明确地接入，
但仍保留本项目的洗稿迁移层，
产物是否比 v11 小修版更有短剧感、更能追、更不丢源本有效性。
```

这版不是从零原创流程。

这版的核心关系是：

```text
本项目 = 洗稿迁移层
0xsline = 短剧创作底盘
oh-story = 状态追踪 / 去 AI 味
how-to-make-script = 剧本输出契约 / 表达 lens
shortdrama-pipeline = 审核门 / issue suggestion / warning 分级
```

---

## 1. 不做什么

- 不照搬 0xsline 的固定比例、总分评分、四层反派硬配、原创剧流程。
- 不把所有外部 reference 塞给 writer。
- 不新增大变量矩阵。
- 不把商业平台字段照抄进流程。
- 不把 reviewer 变成无限挑刺器。
- 不把最终正文写成带内部标签的说明书。

---

## 2. 总 workflow

```text
0. Run Manifest + Minimal Need
1. Source Bible / 源本有效性包
2. Adaptation Boundary / 洗稿边界包
3. Short Drama Creative Plan / 短剧创作方案
4. Character & Opposition Bible / 角色关系与对抗发动机
5. Stage Rhythm Plan / 阶段节奏与追问计划
6. Episode Pursuit Directory / 分集追剧目录
7. Scene Carrier Pack / 场面承载包
8. Playable Writer Brief / 可写剧本简报
9. Screenplay Draft / 首批正文
10. Author Quality Pass / 作者自检与表达返修
11. Story Memory / 状态追踪
12. Clean Reviewer / 干净审稿
13. Controller Delivery Judgment / 主控交付判断
```

和 v11 的差异：

```text
v11：在原链路里补存活问。
v12：把短剧底盘拆出 3 个更清楚的产物：
  Short Drama Creative Plan
  Character & Opposition Bible
  Stage Rhythm Plan
```

---

## 3. Stage 0. Run Manifest + Minimal Need

必须先建 manifest。

最小需求仍按 v11：

```text
源本：
新壳：
目标市场：
集数是否变化：
改写力度：
输出语言：
动作/场景描述语言：
正文用途：
已知禁区：
```

默认：

```text
台词英文；
动作和场景描述中文；
内部分析中文；
目标是 AI 出海短剧剧本文字。
```

但必须显式确认输出语言和正文用途。

---

## 4. Stage 1. Source Bible / 源本有效性包

目标：读出源本为什么能追、为什么能付费。

输出必须包括：

```text
一句话故事核；
核心期待；
首批分集功能；
高价值节点；
源本钩子 / 卡点；
源本付费追问；
爽点 / 压抑释放；
情绪节奏；
关系 / 拉扯 / 权力变化；
信息差 / 真相路径；
反派压力；
写作手法 / 表达手法；
水分 / 烂点 / 禁止复用外形。
```

每个高价值节点必须写：

```text
客观事件；
观众体验功能；
强度来源；
钩子类型；
爽点类型；
压抑如何形成；
释放如何发生；
关系 / 权力变化；
信息差状态；
卡点停法；
源本高辨识外形；
下游写作抓手。
```

如果源本自身事实冲突，必须标出，不得原样下传。

---

## 5. Stage 2. Adaptation Boundary / 洗稿边界包

目标：把源本有效性压成洗稿边界。

输出：

```text
必须保留的体验功能；
必须保留的追看惯性；
必须保留的压抑-释放结构；
必须保留的关系 / 权力变化；
必须避开的源本外形；
可自由改的外壳变量；
必须删除 / 修复的烂点；
新壳承载风险；
用户拍板项。
```

通过标准：

```text
下游知道什么不能丢，也知道什么不能像源本。
```

---

## 6. Stage 3. Short Drama Creative Plan / 短剧创作方案

目标：让新壳不是一层背景，而是一个能兑现短剧承诺的故事方案。

阶段参考：

```text
0xsline: genre-guide, rhythm-curve, satisfaction-matrix, paywall-design
```

注意：只读对应阶段 reference，不把 reference 全塞给 writer。

输出：

```text
Genre Promise：这版新本承诺哪种短剧体验；
Audience Promise：目标观众等什么，不写泛泛人群画像；
Core Satisfaction：主爽感是什么，辅爽感是什么；
Core Pursuit：全剧主追问是什么；
Core Truth Ledger：真实事实 / 对外谎言 / 伪造层；
Initial Misbelief：主要角色初始错信；
Initial Audience Gap：观众开局知道 / 误信 / 不知道什么；
Payoff Logic：兑现一次之后，如何生成下一轮追问；
Tone Boundary：台词、尺度、情绪外放程度；
Overseas Boundary：出海常识、本地化、不能中式硬套的点。
```

通过标准：

```text
核心真相自洽；
题材承诺能具体影响场面和台词；
爽感不是口号，能落到后续行动；
不会把 0xsline 模板压过源本有效性。
```

不通过则不能进入 Stage Rhythm Plan。

---

## 7. Stage 4. Character & Opposition Bible / 角色关系与对抗发动机

目标：解决“人物为什么这么做、反派为什么还能继续作死、关系为什么有拉扯”。

阶段参考：

```text
0xsline: villain-design
oh-story: 角色状态 / 关系追踪思想
```

输出：

```text
主角欲望：
主角误判：
主角底线：
主角行动方式：

核心关系张力：
谁靠近：
谁后退：
谁压谁：
谁误会谁：
谁想控制谁：

反派 / 阻力发动机：
反派想要什么：
反派有什么资源：
反派为什么现在还不能彻底输：
反派下一阶段还能用什么筹码反扑：
反派失败后会转向哪种新策略：

关系变化目标：
首批结束前必须发生的关系 / 权力变化：
不能提前完成的关系变化：
```

通过标准：

```text
每个主要角色都能推出行动；
反派不是只负责作恶台词；
本批结束后仍有对抗燃料，除非本批就是结局段。
```

---

## 8. Stage 5. Stage Rhythm Plan / 阶段节奏与追问计划

目标：把全剧/首批切成阶段，不让每集各写各的，也不让 7-10 集一次性花光追看资产。

阶段参考：

```text
0xsline: rhythm-curve, paywall-design, hook-design, satisfaction-matrix
```

输出：

```text
阶段范围；
阶段起点状态；
阶段主追问；
阶段压抑来源；
阶段兑现；
阶段新追问；
阶段 End Button 类型；
阶段不可提前消费；
阶段反派 / 外部阻力；
阶段结束后剩余追看资产。
```

不硬套固定比例。

通过标准：

```text
每个阶段都有追问、压抑、兑现、留白；
每个阶段结束后仍有后续动力；
不提前消费后续火葬场、关系击穿、真相、反扑。
```

---

## 9. Stage 6. Episode Pursuit Directory / 分集追剧目录

目标：每集写“为什么继续看”，不是只写“发生了什么”。

阶段参考：

```text
0xsline: hook-design, paywall-design, rhythm-curve, satisfaction-matrix
```

字段：

```text
Episode：
Title：
Summary：
Opening Hook：
Hook Type：
Core Friction：
Pressure Setup：
Max Spike：
Satisfaction Type：
Visible Loss / Gain：
Change：
End Button：
Next-Episode Payoff：
Do Not Consume：
Source Function Ref：
Forbidden Shape：
Opposition Fuel：
```

通过标准：

```text
追问还在；
压抑释放还在；
下一集兑现义务清楚；
本集结束后仍有对抗燃料；
不把源本外形整串带入。
```

---

## 10. Stage 7. Scene Carrier Pack / 场面承载包

目标：高压节点先做候选，再选最能承载源本体验的新壳场面。

阶段参考：

```text
0xsline: opening-rules, hook-design, satisfaction-matrix
how-to-make-script: visual language / screenplay contract
```

只做高风险节点：

```text
前 1-3 集；
每集结尾卡点；
身份揭露；
强羞辱 / 强危机 / 强误会 / 强打脸；
关系质变；
同构风险高的源本桥段；
上版 reviewer / 用户指出失败点。
```

每个候选写：

```text
候选名；
场面一句话；
对应源本体验功能；
谁压谁；
谁旁观；
谁被迫选择；
压抑怎么形成；
释放动作是什么；
可见后果；
卡点停在哪个画面 / 动作 / 声音；
删掉屏幕 / 文件 / 报告后，现场戏还剩什么；
同构风险；
短剧降级风险；
AI 成片可视化风险。
```

通过标准：

```text
现场戏还在；
证据触发人物行动，不替代人物行动；
有可见后果；
不是源本桥段改名。
```

---

## 11. Stage 8. Playable Writer Brief / 可写剧本简报

目标：writer 只拿可写戏的信息，不拿审计噪音。

writer brief 可见：

```text
Run Contract；
Current Story State；
Episode Pursuit；
Selected Scene Carrier；
Character Pressure；
Action Chain；
Scene Sequence；
Information Boundary；
Last Frame / Sound / Action；
Screenplay Contract。
```

writer brief 必须带 4 个短答案：

```text
追问还在吗？答案是什么；
压抑释放还在吗？答案是什么；
现场戏还在吗？答案是什么；
对抗燃料还在吗？答案是什么。
```

writer brief 不可见：

```text
完整 Source Bible；
完整 external reference；
manifest；
reviewer 报告；
版本对比；
历史失败清单；
证明链；
所有候选淘汰过程。
```

通过标准：

```text
writer 能只看 brief 写正文；
brief 给场面发动机，不给检查表；
brief 不让 writer 重新解释外部资料；
brief 不把内部标签带进最终正文。
```

---

## 12. Stage 9. Screenplay Draft / 首批正文

目标：输出真正剧本，不是说明书。

正文合同：

```text
正文页上写出来的东西，应该基本等于最终 AI 成片里能看见和听见的东西。
```

格式：

```text
# Episode N: Title

INT. / EXT. LOCATION - DAY / NIGHT

可被观众看见或听见的动作、环境、物件、身体反应、空间变化。
每段动作行尽量短，只写正在发生的事情，不写作者解释。

CHARACTER
(必要时才写简短括号提示)
英文台词，除非需求确认指定中文或双语。

SFX: 必要声音。
ON SCREEN: 必要屏幕文字。
```

要求：

- 高压场不能只靠文件、屏幕、录音、报告或对白完成高潮；
- 角色不能站桩聊天；
- 台词必须推动关系、权力、信息、选择或卡点；
- 情绪必须落到动作、身体、空间、声音、物件或当众后果；
- 每场结束时，关系、权力、信息、情绪或局势至少有一项发生可见变化。

---

## 13. Stage 10. Author Quality Pass / 作者自检与表达返修

目标：主创先判断失败层，不直接润色。

输出：

```text
Failure Layer；
四个存活问是否活着；
Root Symptoms；
Prioritized Actions；
Rollback Point；
Dialogue / Expression polish。
```

表达层参考：

```text
how-to-make-script: expression lens
oh-story: 去 AI 味
```

注意：

```text
台词 polish 只修表达；
结构、场面、追问断了，不能靠台词 polish 解决。
```

---

## 14. Stage 11. Story Memory / 状态追踪

目标：防后续批次状态漂移。

参考：

```text
oh-story: 角色状态、时间线、伏笔、上下文追踪
```

记录：

```text
角色状态；
关系距离；
权力位置；
信息差；
已兑现追问；
未兑现追问；
后续不可提前消费；
反派资源 / 反扑筹码；
伏笔和物件状态；
下一批安全入口。
```

---

## 15. Stage 12. Clean Reviewer / 干净审稿

目标：审稿不是评分器，也不是无限挑刺。

Reviewer 两轮：

```text
Round 1：只读最小需求 + 正文，判断新本独立效果。
Round 2：再读源本有效性包、边界包、开发包、阶段计划、writer brief、必要源本片段。
```

Reviewer lens：

```text
三红线：没洗飞 / 不是改名复刻 / 新本自己能追；
短剧底盘：节奏、爽点、台词、格式、连贯性；
四个存活问：追问、压抑释放、现场戏、对抗燃料；
表达：台词水、站桩、AI 味；
continuity：事实、角色状态、伏笔、信息边界。
```

输出：

```text
pass / revise / block；
workflow execution 判断；
creative outcome 判断；
source carry-through 判断；
delivery outcome 判断；

fatal blockers；
should-fix risks；
optional optimizations；

每条 finding 必须带：
回滚层级；
证据；
修改建议；
是否需要重审全稿。
```

判定：

```text
致命阻断才能打成 revise / block；
风险项不能自动升级成新一轮重审；
可选优化不得阻断交付；
reviewer 不能只写“更短剧 / 更好看”。
```

---

## 16. Stage 13. Controller Delivery Judgment / 主控交付判断

主控必须看：

```text
manifest；
Source Bible；
Adaptation Boundary；
Short Drama Creative Plan；
Character & Opposition Bible；
Stage Rhythm Plan；
Episode Pursuit Directory；
Scene Carrier Pack；
Writer Brief；
Screenplay；
Author Quality Pass；
Story Memory；
Reviewer 两轮；
和旧版本整体对比。
```

交付判断分开写：

```text
workflow execution：
creative outcome：
source carry-through：
delivery outcome：
```

manifest complete 只说明流程执行完成，不说明剧本质量 pass。

---

## 17. 验证方式

本候选版必须和 v11 小修版对照。

同一源本、同一新壳、同一需求下，比较：

```text
V5；
V22；
V23 小修版；
V24 v12 候选版。
```

比较维度：

```text
是否洗飞；
是否改名复刻；
短剧感；
追看动力；
付费卡点；
压抑释放；
关系拉扯；
反派压力；
信息边界；
page-to-screen；
台词；
后续追看资产；
整体可读性。
```

如果 v12 只是更复杂但产物没有明显更好，则不正式化。

