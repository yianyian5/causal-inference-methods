# OR / DML — 结果回归 / 双重机器学习

## 方法简介

### OR — Outcome Regression

直接对结果变量建模，通过回归方法估计处理效应：

$$\hat{\tau}_{OR} = \frac{1}{n}\sum_i \left[\hat{\mu}_1(X_i) - \hat{\mu}_0(X_i)\right]$$

- 使用任意（机器学习）模型拟合 $E[Y|D=1,X]$ 和 $E[Y|D=0,X]$
- 简单直观，但对模型设定敏感

### DML — Double / Debiased Machine Learning

**解决正则化偏差问题**：直接用机器学习估计处理效应时，正则化会引入偏差。DML 通过交叉拟合（Cross-fitting）和残差化（Partialling-out）消除偏差。

#### Partialling-out 步骤（Robinson 1988 思想）

1. 用 ML 模型拟合 $\hat{E}[Y|X]$，得到残差 $\tilde{Y} = Y - \hat{E}[Y|X]$
2. 用 ML 模型拟合 $\hat{E}[D|X]$，得到残差 $\tilde{D} = D - \hat{E}[D|X]$
3. 对残差进行回归：$\tilde{Y} \sim \tilde{D}$，得到无偏的 $\hat{\tau}$

#### 交叉拟合（Cross-fitting）
- 将数据分为 K 折，在折外数据上预测残差，避免过拟合引入的偏差

## 优势

- ✅ 可使用任意机器学习模型（随机森林、XGBoost、神经网络等）
- ✅ 在高维协变量下仍能一致估计
- ✅ 达到半参数效率下界（渐近正态，标准推断有效）
- ✅ 可扩展至异质处理效应（CATE）估计

## 工具包

- Python: [`econml`](https://github.com/microsoft/EconML)（Microsoft）, `doubleml`
- R: `DoubleML`, `grf`
- Stata: `ddml`

## 参考资料

- Chernozhukov et al. (2018), *The Econometrics Journal* — DML 核心论文
- Robinson (1988), *Econometrica* — Partially Linear Model
- [EconML 文档](https://econml.azurewebsites.net/)

