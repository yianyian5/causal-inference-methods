# Bunching Analysis — 密度堆积分析

## 适用条件

- 存在自然断点（如政策门槛）
- **操纵检验显著**：个体可以精确控制自己在断点附近的位置（如刚好卡在门槛值上）
- 此时 RDD 的局部随机假设被违反，需要用 Bunching 方法处理

## 方法简介

当个体可以精确操纵运行变量时，断点附近会出现**密度堆积（Bunching）**现象——大量个体"堆"在门槛值一侧。Bunching Analysis 利用这一堆积现象来**识别行为弹性**，而非直接估计处理效应。

### 核心思想

1. **反事实密度**：估计"若无政策门槛"时运行变量的分布（平滑密度）
2. **超额质量（Excess Mass）**：实际密度与反事实密度之差 = 因政策而改变行为的人群
3. **弹性估计**：通过超额质量推断个体对政策的行为弹性

$$B = \int_{z_l}^{z_u} \left[h(z) - h_0(z)\right] dz$$

其中 $h(z)$ 为实际密度，$h_0(z)$ 为反事实密度，$B$ 为超额质量（Excess Bunch）。

## 与 RDD 的对比

| 特征 | RDD | Bunching Analysis |
|------|-----|-------------------|
| 操纵行为 | 不允许 | 依赖操纵行为存在 |
| 估计对象 | 断点处处理效应（LATE） | 个体行为弹性 |
| 识别来源 | 断点两侧的不连续 | 断点处密度堆积 |
| 业务解读 | 政策有效果吗？ | 个体对政策反应有多敏感？ |

## 典型应用场景

- **税收政策**：纳税人刚好把应税收入控制在税率门槛以下
- **平台激励**：商家/骑手刚好完成门槛单量以获得奖励
- **信用评分**：借款人刚好将分数维持在某个档位门槛上

## 工具包

- R: [`bunchr`](https://cran.r-project.org/web/packages/bunchr/), `bunching`
- Python: 手动实现或参考 Chetty et al. 复现代码

## 参考资料

- Saez (2010), *American Economic Journal* — 税收弹性 Bunching 奠基论文
- Chetty, Friedman et al. (2011), *QJE* — EITC Bunching
- Kleven (2016), *Annual Review of Economics* — Bunching 方法综述

