# IPW / DR — 逆概率加权 / 双重稳健估计

## 适用条件

以下情况之一触发此路径：
1. PSM 匹配导致**样本损失不可接受**
2. PSM 匹配后**平衡性检查未通过**
3. 重叠性检查未通过且**无法缩小结论范围**（直接从上游跳转）

## 方法简介

### IPW — Inverse Probability Weighting

通过倾向得分 $e(X)$ 对样本重新加权，构造伪随机化数据集：

$$\hat{\tau}_{IPW} = \frac{1}{n}\sum_i \left[ \frac{D_i Y_i}{e(X_i)} - \frac{(1-D_i)Y_i}{1-e(X_i)} \right]$$

- ✅ 保留全部样本，无匹配损失
- ❌ 对极端倾向得分值敏感（权重爆炸问题）

### DR — Doubly Robust Estimator

结合**结果回归模型** $\mu(X)$ 和 **IPW**，只要两个模型之一正确即可一致：

$$\hat{\tau}_{DR} = \frac{1}{n}\sum_i \left[ \frac{D_i(Y_i - \hat{\mu}_1(X_i))}{e(X_i)} - \frac{(1-D_i)(Y_i - \hat{\mu}_0(X_i))}{1-e(X_i)} + \hat{\mu}_1(X_i) - \hat{\mu}_0(X_i) \right]$$

- ✅ 双重保险，更稳健
- ✅ 可达到半参数效率下界

## 子目录说明

| 子目录 | 方法 | 说明 |
|--------|------|------|
| `OR_DML/` | Outcome Regression / Double ML | 使用机器学习提升 DR 估计量的灵活性 |

## 参考资料

- Robins, Rotnitzky & Zhao (1994) — DR 原始论文
- Farrell (2015), Chernozhukov et al. (2018) — DML

