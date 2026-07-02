# PRD v17-v7workflow 主控判定

输入：

- `workflow_run_manifest_V17_v7workflow.md`
- `PRD_v17_v7workflow_豪门商战版_首批1-10集.md`
- `PRD_v17_v7workflow_作者问题清单.md`
- `PRD_v17_v7workflow_reviewer.md`
- `PRD_v17_v7workflow_vs_v3_v15_v16_整体对比.md`

## 1. 状态结论

```text
execution_status: complete
reviewer_status: revise
delivery_status: not final / needs revise
workflow_status: v7 候选 workflow 跑通，但不能正式化
```

V17 已按 v7 完成一次完整样本验证。

这次验证没有继续修 V15 / V16，也没有套旧 v2 的 0-15 表。v7 的 9 个步骤均有产物或执行证据。

但 reviewer 结论是 `revise`，不是 `pass`。所以 V17 不能作为导演可送审稿，也不能证明 v7 已经稳定解决质量问题。

## 2. 这轮证明了什么

### 2.1 v7 的减法没有导致洗飞

这轮没有 Source Bible / Anchor / Story State / Scene Packet 那种厚产物链，但源本主要追看机制仍然传到了正文：

- 被替代；
- 男主错误选择；
- 女主失子；
- 五年后权力反转；
- 白月光骗局公开崩；
- 男主发现自己害死亲骨肉；
- 当众跪求且被女主卡住。

说明 v7 的轻流程不是天然不够用。

### 2.2 正文比旧程序化版本更像剧本

V17 正文基本使用了剧本动作行和英文对白，没有把 `Purpose / Function / Source Ref / Gate` 这类内部标签写进正文。

E1-E3 和 E9-E10 比较成立：

- E1 的 brooch 被撕、超声影像被踩；
- E2 的玻璃中庭坍塌；
- E3 的割掉病号腕带和 Sable 徽章染血；
- E9 的旧中庭排水槽里挖出带血 brooch 和碎超声影像；
- E10 的直播前公开交权和逼他说出 “my son / my daughter”。

这些不是纯说明书。

### 2.3 干净 reviewer 能定位失败层

Reviewer 没有判 block，也没有说源本没读透。它定位在：

```text
正文执行弱；
局部台词或场面可修；
状态连续性断；
少量写作简报传递断。
```

这个定位和 v7 的设计一致：先看正文，再回源本判断失败层。

## 3. 这轮没通过在哪里

### 3.1 E4-E8 公开打脸结构偏整齐

债权拍卖、账本、护士、Bennett、孩子、Chloe 反咬这些材料有效，但连续几集容易形成：

```text
公开场合摆证据
-> 众人震惊
-> 反派否认
-> 下一证据压上
```

这不是回到 V12 的程序机器，但仍有模板痕迹。

### 3.2 部分英文台词偏金句化

例如：

```text
You always loved the loudest lie.
Adrian couldn't save you from my first bill.
Now beg where they can hear you.
```

单句有效，但连续出现会让人物像在替卡点服务。

### 3.3 E3-E4 认知状态略断

E3 暗示 Claire 可以让过去的自己死掉；E4 Chloe 又直接叫出 Claire。这里需要更清楚：

```text
她是被认为死了，还是被认为消失了？
Adrian 是第一眼没认出，还是认出了但不敢相信？
Chloe 为什么先认出？
```

### 3.4 E10 钩子有效但还不够尖

直播前逼 Adrian 说出孩子身份有效，但比源本“枪口抵额头，一命换两命”的爆炸性弱。

如果修，应增强下一集欲望，而不是简单再加一句狠话。

## 4. 主控判断

V17 应该封为：

```text
v7 候选 workflow 完整验证样本：execution complete / delivery revise
```

不应该封为：

```text
candidate checkpoint
导演可送审稿
v7 正式通过
```

## 5. 是否继续修

不建议继续无限修。

如果用户要看 v7 能不能局部修到 pass，只允许一次小范围 revise：

```text
1. 修 E3-E4 认知状态；
2. 修 E7-E8 证据台本化，让人物失控承担更多信息；
3. 修 E10 钩子，让下一集欲望更尖；
4. 不回上游重做，不扩 PRD，不改 workflow。
```

如果用户当前要判断项目方向，则更重要的是：

```text
拿 V17 和 V15 / V16 给用户或导演看，
判断 v7 的轻流程是否更接近“能稳定写出剧本”，
而不是继续在这一个样本上打磨。
```

