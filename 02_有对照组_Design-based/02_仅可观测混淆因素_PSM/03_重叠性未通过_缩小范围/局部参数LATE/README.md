# 局部参数 LATE — Local Average Treatment Effect

## 适用条件

- 重叠性未通过，且无明确业务分组（或需要更严格的因果识别）
- 转向估计**局部因果效应**：仅估计在干预作用下"边际"改变行为的那部分人群的处理效应

## LATE 的含义

**LATE（Local Average Treatment Effect）** = **Compliers（顺从者）** 的 ATE

- Compliers：因为干预的存在而改变了处理状态的人（有工具变量 Z=1 才接受处理，Z=0 则不接受）
- 不是所有人的平均效应（ATE），而是局部的

## 决策分支

```
转向估计局部参数 LATE
  ├── 是否存在自然断点（如触发策略的门槛值）？
  │     ├── Y → 是否存在明显的操纵行为（Manipulation）？
  │     │       ├── N → RDD（见子目录 RDD/）
  │     │       └── Y → Bunching Analysis（见子目录 Bunching分析/）
  │     └── N → 是否可找到工具变量？
  │               ├── Y → IV（见子目录 IV工具变量/）
  │               └── N → 回退到分组匹配估计（见上级 分组匹配估计/）
```

## 子目录说明

| 子目录 | 方法 | 识别来源 |
|--------|------|----------|
| `RDD/` | 断点回归 | 策略触发门槛（如积分达到某阈值） |
| `Bunching分析/` | Bunching Analysis | 存在操纵时的密度堆积分析 |
| `IV工具变量/` | Instrumental Variables | 外生工具变量（如政策随机分配） |

