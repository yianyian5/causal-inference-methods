# PSM — 倾向得分匹配

## 方法简介

**Propensity Score Matching (PSM)** 通过估计每个个体接受处理的概率（倾向得分），在处理组和对照组之间进行一对一或多对一匹配，从而构造可比的对照样本。

$$e(X) = P(D=1 | X)$$

## 使用流程

```
1. 估计倾向得分 e(X)（通常用 Logistic Regression）
       ↓
2. 重叠性检查（Overlap / Common Support Check）
       ├── 通过 → 继续
       └── 未通过 → 见 03_重叠性未通过_缩小范围/
       ↓
3. 执行匹配（1:1, 1:k, Kernel 等）
       ↓
4. 检查样本损失（Sample Loss Check）
       ├── 可接受 → 继续
       └── 不可接受 → 见 02_IPW_DR/
       ↓
5. 平衡性检查（Covariate Balance Check）
       ├── 通过（SMD < 0.1 或 < 0.25）→ 可信结果，进入稳健性检验
       └── 未通过 → 见 02_IPW_DR/ 或调整匹配参数重试
```

## 两个关键检查

### 重叠性检查（Overlap / Common Support）
- **目的**：确保处理组和对照组在倾向得分分布上有充分重叠
- **工具**：倾向得分分布直方图/密度图对比；统计重叠比例
- **标准**：重叠区域应覆盖绝大多数处理组样本

### 平衡性检查（Balance Check）
- **目的**：匹配后，处理组与对照组在协变量分布上应高度相似
- **工具**：标准化均值差（SMD / Standardized Mean Difference）、Love Plot
- **标准**：通常要求 SMD < 0.1（严格）或 SMD < 0.25（宽松）

## 子目录说明

| 子目录 | 描述 |
|--------|------|
| `通过重叠性和平衡性检查/` | 两项检查均通过，匹配结果可信 |
| `重叠性或平衡性未通过_转IPW_DR/` | 检查未通过，需要改用加权方法 |

## 参考资料

- Rosenbaum & Rubin (1983), *Biometrika* — PSM 原始论文
- Ho, Imai, King & Stuart (2007), *Political Analysis* — MatchIt 包
- Stuart (2010), *Statistical Science* — 匹配方法综述

