# SCM / SDID — 合成控制法 / 合成双重差分

## 适用条件

- 经典 DID 设计，但**平行趋势假设无法满足**
- 处理单元数量少（通常只有 1 个处理单元），对照单元数量相对较多
- 有足够长的处理前时间序列（建议 ≥ 处理后期数的 3 倍）

## 方法简介

### SCM — Synthetic Control Method

通过对多个对照单元进行**加权**，构造一个"合成对照组"，使其在处理前尽可能拟合处理单元的结果变量路径。

$$\hat{Y}_{1t}^{(0)} = \sum_{j=2}^{J+1} w_j^* Y_{jt}, \quad t < T_0$$

权重 $w^*$ 通过最小化处理前拟合误差得到，处理效应为：

$$\hat{\tau}_t = Y_{1t} - \hat{Y}_{1t}^{(0)}, \quad t \geq T_0$$

**推断**：通过置换检验（Permutation / Placebo Test）对每个对照单元重复同样过程，构造参照分布。

### SDID — Synthetic Difference-in-Differences

结合 SCM（单元加权）和 DID（时间加权）：
- 对**对照单元**加权（使处理前拟合最好，类似 SCM）
- 对**时间期**加权（给处理前接近处理期的时点更大权重）
- 使用 DID 估计量，获得比纯 SCM 更稳定的标准误

## 与 TWFE/DID 的比较

| 特征 | TWFE/DID | SCM | SDID |
|------|----------|-----|------|
| 对照组构造 | 等权 | 加权 | 加权（双重） |
| 平行趋势要求 | 严格 | 宽松（近似满足） | 宽松 |
| 推断方法 | 标准SE / 聚类SE | 置换检验 | Bootstrap / 置换 |
| 适用单元数 | 多 | 少（1个处理单元） | 多或少均可 |

## 参考资料

- Abadie, Diamond & Hainmueller (2010), *JASA* — SCM 原始论文
- Arkhangelsky et al. (2021), *AER* — SDID 论文
- [synth R package](https://cran.r-project.org/web/packages/Synth/)
- [sdid Python/R package](https://github.com/synth-inference/synthdid)

