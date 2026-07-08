# EP005 Scene Decision Packet

- mode: compile_only
- fallback_hits: 0
- forbidden_source_hits: 0
- forbidden_runtime_inputs_read: none

## Scene 1

- source constraints: Celeste 仍处高位；Rose 胸针必须可见；资金真相不能提前爆。 `[source: ED_EP5_WRITER_DIRECT, ED_BATCH_HEADER, CHARACTERS]`
- blueprint role: 先把“小家庭生日”布成假温情陷阱。 `[source: ED_EP5_WRITER_DIRECT, ED_EP5_SYSTEM_CHECK]`
- analysis signals: 家人集体围绕 Celeste 运转，Evelyn 刚经历生日被忘和真相压回。 `[source: ED_EP5_SYSTEM_CHECK, EP4_STATE]`
- commercial signals: 先卖“桌上所有爱都给了谁”，再进入身体伤害。 `[source: ED_EP5_SYSTEM_CHECK]`
- power contest: Celeste 发邀请；Victor 定位；Evelyn 被安排到边缘位。 `[source: ED_EP5_WRITER_DIRECT, DIALOGUE_FORCE_KERNEL]`
- dramatic carrier: 小圆桌、芒果蛋糕、烛火、胸针、边缘座位。 `[source: ED_EP5_WRITER_DIRECT, PERFORMANCE_KERNEL]`
- pressure dialogue direction: 先软邀，再把“拒绝”预热成扫兴。 `[source: ED_EP5_SYSTEM_CHECK, DIALOGUE_FORCE_KERNEL]`
- unpaid debt: Evelyn 坐下后，这桌到底要她付出什么。 `[source: ED_EP5_WRITER_DIRECT]`
- anti-contamination constraints: 不写作者总结句；先让桌面、座位、物件承压。 `[source: PERFORMANCE_KERNEL, DIALOGUE_FORCE_KERNEL]`

## Scene 2

- source constraints: Evelyn 必须明确说过敏；家人必须短暂停一下；最终仍选择 Celeste。 `[source: ED_EP5_WRITER_DIRECT, ED_EP5_SYSTEM_CHECK]`
- blueprint role: 把身体边界改写成扫兴 / 不给面子。 `[source: ED_EP5_SYSTEM_CHECK]`
- analysis signals: Celeste 的眼泪必须掐灭 Nathan / Margaret 的迟疑。 `[source: ED_EP5_SYSTEM_CHECK, CHARACTERS]`
- commercial signals: 核心卖“误判变伤害”，不是医学知识。 `[source: ED_EP5_SYSTEM_CHECK]`
- power contest: Evelyn 说边界 -> Celeste 装无辜 -> 家人补刀 -> Victor 封口。 `[source: ED_EP5_WRITER_DIRECT, ED_EP5_SYSTEM_CHECK, DIALOGUE_FORCE_KERNEL]`
- dramatic carrier: 被推近的蛋糕盘、Rose 胸针、烛火、全桌短暂停顿。 `[source: ED_EP5_SYSTEM_CHECK, PERFORMANCE_KERNEL]`
- pressure dialogue direction: “我不能吃”被翻译成“今天扫兴”“不给面子”“大家都在哄你”。 `[source: ED_EP5_SYSTEM_CHECK, DIALOGUE_FORCE_KERNEL]`
- unpaid debt: 她最后会不会吃；吃了之后伤害会有多严重。 `[source: ED_EP5_WRITER_DIRECT, ED_EP5_SYSTEM_CHECK]`
- anti-contamination constraints: 不长讲道理；不让所有角色同声线；不让 Celeste 直接承认故意。 `[source: ED_EP5_WRITER_DIRECT, DIALOGUE_FORCE_KERNEL]`

## Scene 3

- source constraints: Evelyn 必须自己吃下去；当桌发作；Victor 不能真正心软。 `[source: ED_EP5_WRITER_DIRECT, ED_EP5_SYSTEM_CHECK]`
- blueprint role: 把“她最后还是顺从了”转成观众怒点和身体代价。 `[source: ED_EP5_WRITER_DIRECT, ED_EP5_SYSTEM_CHECK]`
- analysis signals: 旧家要把发作继续解释成破坏生日，为 EP6 医生证明仍被反咬做铺垫。 `[source: ED_EP5_SYSTEM_CHECK, EP6_DEBT_OR_HOOK]`
- commercial signals: 钩子不在医生进门，而在“她都见血了，旧家还不信”。 `[source: ED_EP5_SYSTEM_CHECK, EP6_DEBT_OR_HOOK]`
- power contest: Evelyn 失去最后拒绝权 -> 身体开始失控 -> Victor 仍先守桌上秩序。 `[source: ED_EP5_WRITER_DIRECT, ED_EP5_SYSTEM_CHECK, DIALOGUE_FORCE_KERNEL]`
- dramatic carrier: 吞咽、桌沿、气音、冷汗、血点溅白桌布。 `[source: ED_EP5_SYSTEM_CHECK, PERFORMANCE_KERNEL]`
- pressure dialogue direction: 吃之前所有人等她证明顺从；发作后继续压成“又在闹”。 `[source: ED_EP5_SYSTEM_CHECK, DIALOGUE_FORCE_KERNEL]`
- unpaid debt: EP6 医生证明能不能击穿他们。 `[source: EP6_DEBT_OR_HOOK, ED_EP5_SYSTEM_CHECK]`
- anti-contamination constraints: 不写“希望碎了”之类作者句；必须落在呼吸、手、血、桌布。 `[source: PERFORMANCE_KERNEL]`
