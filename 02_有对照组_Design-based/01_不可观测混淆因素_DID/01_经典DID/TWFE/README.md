# TWFE — 双向固定效应估计

## 方法简介

**Two-Way Fixed Effects (TWFE)** 是经典 DID 的标准回归实现，通过同时控制个体固定效应和时间固定效应，在平行趋势假设下识别 ATT（Average Treatment Effect on the Treated）。

## 基本模型

$$Y_{it} = \alpha_i + \lambda_t + \beta \cdot D_{it} + \varepsilon_{it}$$

- $\alpha_i$：个体固定效应（控制不随时间变化的不可观测异质性）
- $\lambda_t$：时间固定效应（控制共同时间趋势）
- $\beta$：处理效应估计量（ATT）
- $D_{it}$：处理变量（是否受到干预）

## 关键假设

1. **平行趋势（Parallel Trends）**：若没有干预，处理组与对照组的结果变量随时间的变化趋势相同
2. **无预期效应**：处理前个体不会提前改变行为
3. **SUTVA**：处理对个体的影响不受其他个体处理状态影响

## 事前趋势检查（Event Study）

使用事件研究法（Event Study）验证平行趋势：

$$Y_{it} = \alpha_i + \lambda_t + \sum_{k \neq -1} \beta_k \cdot \mathbf{1}[t - T_i^* = k] + \varepsilon_{it}$$

- **$k < 0$ 的系数（事前）应不显著且接近零**（平行趋势成立）
- $k \geq 0$ 的系数反映处理效应随时间的动态变化

## 子目录导航

| 子目录 | 描述 |
|--------|------|
| `通过事前趋势检查/` | 平行趋势成立，TWFE 结果可用，进入稳健性检验 |
| `未通过事前趋势_调整后重试/` | 通过加入控制变量、函数形式变换、PSM 预处理等方式修复后重试 |
| `无法调平行趋势_转SCM_SDID/` | 无法修复，转向合成控制方法 |

## 参考资料

- Angrist & Pischke (2009), *Mostly Harmless Econometrics*
- Callaway & Sant'Anna (2021), *Journal of Econometrics*

