graph LR
    %% 定义起点
    Start([<b>全量评估开始</b>]) --> FindControl{是否可找到对照组}

    %% 分支一：无对照组 (Model-based)
    FindControl -- N --> ModelBased[Model-based 方法]
    ModelBased --> BusinessInsight{是否需要更深<br/>的业务洞察}
    
    BusinessInsight -- Y --> EconModel[经济学模型 / 结构估计]
    EconModel -.-> EconNote["[备注] 构建基于经济学理论的可解释生成模型<br/>例子: Amazon Economist 使用 BLP 模型估计需求"]
    
    BusinessInsight -- N --> StatModel[统计学模型]
    StatModel -.-> StatNote["[备注] 例如 BSTS (Google 的 Causal Impact)"]

    %% 分支二：有对照组 (Design-based)
    FindControl -- Y --> DesignBased[Design-based 方法]
    DesignBased --> Unobserved{是否明显存在<br/>不可观测的混淆因素}

    %% 子分支：存在不可观测因素 (DID 路径)
    Unobserved -- Y --> DID[DID]
    DID --> ClassicDID{是否为经典<br/>的 DID 设计}
    
    ClassicDID -- Y --> TWFE[TWFE 估计]
    ClassicDID -- N --> StaggeredDID[Staggered DID 等]
    
    TWFE --> PreTrend{是否通过事前趋势检查<br/>使用 Event Study 方法}
    PreTrend -- Y --> Robustness
    PreTrend -- N --> AdjustTrend{是否可通过控制变量、<br/>函数形式变换、PSM等<br/>方式将事前趋势调为平行?}
    AdjustTrend -- Y --> TWFE
    AdjustTrend -- N --> SCM[SCM / SDID 等]

    %% 子分支：仅存在可观测因素 (PSM / LATE 路径)
    Unobserved -- N --> PSM[PSM]
    PSM --> Overlap{是否可通过<br/>重叠性检查}
    
    %% 重叠性检查通过
    Overlap -- Y --> LossSample{是否可接受匹配<br/>过程中的样本损失}
    LossSample -- Y --> Balance{是否可通过<br/>平衡性检查}
    Balance -- Y --> Robustness
    Balance -- N --> IPW_DR[改用其他匹配或直接<br/>结果用 IPW / DR]
    LossSample -- N --> IPW_DR
    IPW_DR --> ORDML[OR / DML]
    
    %% 重叠性检查未通过
    Overlap -- N --> NarrowScope{是否可缩小结论适用<br/>范围以避免外推}
    NarrowScope -- Y --> Redefine[重新定义待估目标参数]
    Redefine --> BizGroup{是否有明确<br/>的业务分组}
    BizGroup -- Y --> GroupMatch[仅保留重叠性良好的<br/>分组匹配估计结果]
    BizGroup -- N --> LATE[转向估计局部参数 LATE]
    NarrowScope -- N --> ORDML

    %% 局部参数评估路径 (LATE / RDD / IV)
    LATE --> NaturalCut{是否存在自然断点<br/>如触发策略的门槛}
    NaturalCut -- Y --> Manipulation{是否存在明显<br/>操纵行为}
    Manipulation -- N --> RDD[RDD]
    Manipulation -- Y --> Bunching[Bunching Analysis]
    
    NaturalCut -- N --> FindIV{是否可找到<br/>工具变量}
    FindIV -- Y --> IV[IV]
    FindIV -- N --> GroupMatch
    
    %% 汇总至结束
    EconModel --> Robustness
    StatModel --> Robustness
    SCM --> Robustness
    ORDML --> Robustness
    GroupMatch --> Robustness
    RDD --> Robustness
    Bunching --> Robustness
    IV --> Robustness

    Robustness[稳健性检验: 基于经济理论业务直觉、数据描述、安慰剂检验、敏感性分析等] --> End([结束])