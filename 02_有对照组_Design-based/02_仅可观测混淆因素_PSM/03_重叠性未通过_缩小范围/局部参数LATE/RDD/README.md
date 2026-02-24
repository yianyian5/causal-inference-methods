# RDD — 断点回归设计

## 适用条件

- 存在**自然断点（Threshold）**：处理状态由某个连续变量是否超过某个门槛决定
- **不存在明显的操纵行为**：个体无法精确控制自己在断点两侧的位置
- 关键假设：在断点附近，被分配到处理组和对照组的个体**局部随机**（As-if Random）

## 方法简介

**Sharp RDD**（硬断点）：处理完全由规则决定

$$D_i = \mathbf{1}[X_i \geq c]$$

$$\hat{\tau}_{RDD} = \lim_{x \to c^+} E[Y|X=x] - \lim_{x \to c^-} E[Y|X=x]$$

**Fuzzy RDD**（软断点）：跨越断点后处理概率发生跳变，但不是 0/1 切换（类似 IV）

$$\hat{\tau}_{Fuzzy} = \frac{\text{结果变量在断点处的跳变}}{\text{处理概率在断点处的跳变}}$$

## 实施步骤

1. **确定运行变量（Running Variable）和断点**
2. **操纵检验（Manipulation Test）**：
   - McCrary (2008) 密度检验：检验运行变量在断点处密度是否连续
   - Cattaneo et al. rddensity 检验
   - ⚠️ 若检验**显著**→ 存在操纵行为 → 转向 `../Bunching分析/`
3. **带宽选择（Bandwidth Selection）**：
   - MSE 最优带宽（Imbens-Kalyanaraman / Calonico et al. CCT 方法）
4. **局部多项式回归估计**断点两侧的条件期望
5. **协变量连续性检验**：在断点处，其他协变量应无跳变（平衡性）
6. **稳健性检验**：不同带宽、不同多项式阶数的敏感性分析

## 外部有效性注意事项

RDD 估计的是**断点附近样本的 LATE**，不能外推到远离断点的人群。

## 工具包

- R: [`rdrobust`](https://cran.r-project.org/web/packages/rdrobust/), `rddensity`, `rdlocrand`
- Python: `rdrobust`（PyPI）
- Stata: `rdrobust`, `rddensity`

## 参考资料

- Hahn, Todd & Van der Klaauw (2001), *Econometrica* — RDD 奠基论文
- Imbens & Lemieux (2008), *Journal of Econometrics* — RDD 实践指南
- Calonico, Cattaneo & Titiunik (2014), *Econometrica* — CCT 带宽选择

