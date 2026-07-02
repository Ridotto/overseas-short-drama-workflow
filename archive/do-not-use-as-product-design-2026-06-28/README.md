# 旧设计隔离说明

日期：2026-06-28

这个目录里的文件不要作为当前产品设计继续使用。

它们保留的原因是：后续 Claude 或其他 reviewer 可能需要看我们之前怎么走偏、哪些实验失败、哪些概念产生过误导。

## 为什么隔离

这些文件共同的问题：

- 把产品定义、分析器、评判器、改写器、生成器、多 agent 架构混在一起。
- 过早进入工程语言，脱离产品/编剧工作流。
- V1/V2/V3 rubric 的 blind eval 结果不稳定，不能继续当标准。
- `public gold set` 方向已经废弃，不能再作为参考真值。
- 部分 Claude review 是在有偏 brief 上产生的，只能当历史意见看。

## 使用规则

可以看：

- 为了理解旧路线为什么失败
- 为了找具体反例
- 为了复盘哪些术语和结构会误导

不要用：

- 不要从这些文件复制产品架构
- 不要继承里面的评分维度
- 不要把里面的模块拆分当成 agent 设计
- 不要把里面的“结论”当成当前共识

## 文件类型

- `script-transformation-agent-spec-2026-06-28.md`
  旧大 spec，范围过大，容易误导。

- `script-agent-architecture-and-eval-plan-2026-06-28.md`
  旧架构/评估修正文档，工程视角过重。

- `claude-review-brief-2026-06-28.md`
  给 Claude 的旧 brief，本身带有当时错误框架。

- `claude-review-report-2026-06-28.md`
  基于旧 brief 的 Claude review，有参考价值但不应当成当前设计。

- `blind-eval-protocol-2026-06-28.md`
  旧盲测协议，已经不能作为下一轮产品定义入口。

- `common-rubric-v1.md` / `common-rubric-v2.md` / `common-rubric-v3.md`
  旧评分说明。V3 在第二批样本上塌成全 medium，不可继续作为标准。

- `comparison-template.md` / `comparison-v2.md`
  旧对比模板，保留作失败记录。
