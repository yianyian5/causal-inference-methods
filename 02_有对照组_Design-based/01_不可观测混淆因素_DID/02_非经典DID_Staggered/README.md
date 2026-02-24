# 非经典 DID — Staggered DID 等

## 适用条件

- 存在不可观测混淆因素，需要使用 DID 框架
- **处理时间不统一**：不同单元（如不同城市、用户群体）在**不同时间点**开始接受干预（Staggered Treatment）
- 经典 TWFE 在此场景下会产生有偏估计（Goodman-Bacon 分解揭示的问题）

## 问题背景

当处理时间错落时，经典 TWFE 会将**早期处理组**当作**晚期处理组**的"对照"，导致估计量是多个 ATT 和**负权重**的混合，可能严重偏误。

## 主要方法

| 方法 | 关键思想 | 参考 |
|------|----------|------|
| **Callaway & Sant'Anna (CS)** | 分队列（cohort）估计每个处理时间组的 ATT，再聚合 | Callaway & Sant'Anna (2021) |
| **Sun & Abraham (SA)** | 基于交互效应的 TWFE，避免负权重 | Sun & Abraham (2021) |
| **Borusyak, Jaravel & Spiess (BJS)** | 直接估计反事实，imputation estimator | Borusyak et al. (2024) |
| **Roth et al. 综述** | 全面比较各方法 | Roth et al. (2023) |
| **Goodman-Bacon 分解** | 诊断工具，分解 TWFE 估计量 | Goodman-Bacon (2021) |

## 使用建议

1. **先用 Goodman-Bacon 分解** 诊断经典 TWFE 是否存在负权重问题
2. 使用 **Callaway-Sant'Anna** 或 **Sun-Abraham** 进行稳健估计
3. 进行事前趋势检查（同样适用于 Staggered 设计）
4. 对结果进行聚合（按时间、按队列、整体平均）

## 工具包

- Python: `pyfixest`, `csdid`
- R: `did` (Callaway-Sant'Anna), `fixest` (Sun-Abraham), `bacondecomp`
- Stata: `csdid`, `eventstudyinteract`, `did_imputation`

## 参考资料

- Callaway & Sant'Anna (2021), *Journal of Econometrics*
- Sun & Abraham (2021), *Journal of Econometrics*
- Roth, Sant'Anna, Bilinski & Poe (2023), *Journal of Econometrics*
- [混淆指南：What's Trending in Difference-in-Differences](https://jonathandroth.github.io)

