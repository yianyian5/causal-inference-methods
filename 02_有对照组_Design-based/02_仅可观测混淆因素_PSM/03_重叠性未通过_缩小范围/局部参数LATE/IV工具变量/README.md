# IV — 工具变量估计

## 适用条件

- 需要估计局部参数 LATE
- **不存在自然断点**（无法用 RDD）
- **可以找到满足条件的工具变量 Z**

## 工具变量的三个核心条件

| 条件 | 含义 | 检验方式 |
|------|------|----------|
| **相关性（Relevance）** | Z 与处理变量 D 强相关 | 第一阶段 F 统计量 > 10（经验阈值）；Kleibergen-Paap 检验 |
| **外生性（Exogeneity）** | Z 与误差项无关，仅通过 D 影响 Y | 不可直接检验（需理论论证）；过度识别检验（多 IV 时） |
| **排他性限制（Exclusion Restriction）** | Z 不直接影响 Y，只通过 D 起作用 | 同上，理论论证为主 |

## 估计量：2SLS

**Two-Stage Least Squares（两阶段最小二乘）**

$$\text{第一阶段：} \quad \hat{D}_i = \alpha_0 + \alpha_1 Z_i + \alpha_2 X_i + u_i$$

$$\text{第二阶段：} \quad Y_i = \beta_0 + \beta_1 \hat{D}_i + \beta_2 X_i + \varepsilon_i$$

- $\beta_1$ 即为 LATE（Complier ATE）的 2SLS 估计量

## LATE 的解释

IV 估计的是 **Compliers** 的平均处理效应：

$$\text{LATE} = \frac{E[Y|Z=1] - E[Y|Z=0]}{E[D|Z=1] - E[D|Z=0]}$$

- **Compliers**：因工具变量 Z 由 0 变 1 而改变处理状态（D: 0→1）的那部分人
- 不包括 Always-takers（无论 Z 如何都接受处理）和 Never-takers

## 常见工具变量来源

| 场景 | 工具变量例子 |
|------|------------|
| 政策评估 | 政策随机分配（抽签、随机化推广）、法律改变时间 |
| 平台实验 | 系统随机推送、服务器随机分流 |
| 地理研究 | 地理距离、气候变量 |
| 经济研究 | 出生顺序、兄弟姐妹性别组合（Angrist） |

## 弱工具变量问题

若第一阶段 F 统计量 < 10，工具变量"弱"，2SLS 有有限样本偏差：
- 使用 **LIML（有限信息最大似然）** 代替 2SLS
- 使用 **Anderson-Rubin 置信区间**（弱 IV 稳健）
- 重新寻找更强的工具变量

## 工具包

- R: `AER::ivreg`, `fixest::feols(... | D ~ Z)`
- Python: `linearmodels`（IV2SLS）, `statsmodels`
- Stata: `ivregress 2sls`, `ivreg2`

## 参考资料

- Angrist & Imbens (1994), *JASA* — LATE 框架
- Angrist & Pischke (2009), *Mostly Harmless Econometrics* — 第四章
- Stock & Yogo (2005) — 弱工具变量检验

