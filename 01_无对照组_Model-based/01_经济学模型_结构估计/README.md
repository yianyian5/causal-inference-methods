# 经济学模型 / 结构估计

## 适用条件

- 无对照组
- **需要深度业务洞察**：不仅要估计处理效应，还需要理解背后的经济机制、进行反事实政策模拟

## 方法简介

基于经济学理论构建可解释的**生成模型（Structural / Generative Model）**，将行为人的决策过程显式建模。

### 典型方法

| 方法 | 说明 |
|------|------|
| BLP 模型 | Berry-Levinsohn-Pakes 需求估计，常用于市场/定价研究（Amazon Economist 经典案例） |
| 供需结构模型 | 同时建模供给侧和需求侧 |
| 动态规划 / 离散选择模型 | 建模跨期决策 |

## 优势 & 局限

- ✅ 可解释、可外推、支持政策模拟
- ❌ 建模复杂，依赖假设，开发成本高

## 参考资料

- Berry, Levinsohn & Pakes (1995), *Econometrica*
- [Amazon Economist 的 BLP 需求估计实践](https://www.amazon.science)

