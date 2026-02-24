# DID 路径 — 存在不可观测混淆因素

## 适用条件

- 有对照组
- **存在明显的不可观测混淆因素**（如个体固定效应、地区文化差异等无法观测的变量）
- 关键识别假设：**平行趋势（Parallel Trends）**

## 决策分支

```
存在不可观测混淆因素 → DID
  ├── 是否为经典 DID 设计（两期、一次性干预）？
  │     ├── Y → TWFE 估计（见子目录 01/TWFE）
  │     │       ├── 通过事前趋势检查 → 进入稳健性检验
  │     │       ├── 未通过，但可调整 → 重新尝试 TWFE
  │     │       └── 无法调整 → SCM / SDID（见子目录 01/SCM_SDID）
  │     └── N → Staggered DID 等（见子目录 02）
```

## 子目录说明

| 目录 | 方法 | 适用场景 |
|------|------|----------|
| `01_经典DID/TWFE` | Two-Way Fixed Effects | 两期或多期但同时干预，平行趋势成立 |
| `01_经典DID/SCM_SDID` | Synthetic Control / Synthetic DID | 平行趋势难以满足，需要构造合成对照 |
| `02_非经典DID_Staggered` | Callaway-Sant'Anna, Sun-Abraham 等 | 不同单元在不同时期接受处理 |

