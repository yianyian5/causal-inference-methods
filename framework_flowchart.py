from graphviz import Digraph

# 创建有向图
dot = Digraph(comment='因果推断方法框架', format='png')
dot.attr(rankdir='LR', bgcolor='white')
dot.attr('node', shape='box', style='rounded,filled', fillcolor='lightblue', fontname='SimHei')
dot.attr('edge', fontname='SimHei')

# 定义节点
dot.node('Start', '全量评估开始', shape='ellipse', fillcolor='lightgreen')
dot.node('FindControl', '是否可找到对照组', shape='diamond', fillcolor='lightyellow')

# Model-based 路径
dot.node('ModelBased', 'Model-based 方法', fillcolor='lightcyan')
dot.node('BusinessInsight', '是否需要更深的业务洞察', shape='diamond', fillcolor='lightyellow')
dot.node('EconModel', '经济学模型 / 结构估计', fillcolor='lightcyan')
dot.node('StatModel', '统计学模型', fillcolor='lightcyan')

# Design-based 路径
dot.node('DesignBased', 'Design-based 方法', fillcolor='lightcyan')
dot.node('Unobserved', '是否明显存在不可观测的混淆因素', shape='diamond', fillcolor='lightyellow')

# DID 路径
dot.node('DID', 'DID', fillcolor='lightcyan')
dot.node('ClassicDID', '是否为经典的 DID 设计', shape='diamond', fillcolor='lightyellow')
dot.node('TWFE', 'TWFE 估计', fillcolor='lightcyan')
dot.node('StaggeredDID', 'Staggered DID 等', fillcolor='lightcyan')
dot.node('PreTrend', '是否通过事前趋势检查\n使用 Event Study 方法', shape='diamond', fillcolor='lightyellow')
dot.node('AdjustTrend', '是否可通过控制变量、\n函数形式���换、PSM等\n方式将事前趋势调为平行', shape='diamond', fillcolor='lightyellow')
dot.node('SCM', 'SCM / SDID 等', fillcolor='lightcyan')

# PSM 路径
dot.node('PSM', 'PSM', fillcolor='lightcyan')
dot.node('Overlap', '是否可通过重叠性检查', shape='diamond', fillcolor='lightyellow')
dot.node('LossSample', '是否可接受匹配\n过程中的样本损失', shape='diamond', fillcolor='lightyellow')
dot.node('Balance', '是否可通过平衡性检查', shape='diamond', fillcolor='lightyellow')
dot.node('IPW_DR', '改用其他匹配或直接\n结果用 IPW / DR', fillcolor='lightcyan')
dot.node('ORDML', 'OR / DML', fillcolor='lightcyan')

# 重叠性未通过路径
dot.node('NarrowScope', '是否可缩小结论适用\n范围以避免外推', shape='diamond', fillcolor='lightyellow')
dot.node('Redefine', '重新定义待估目标参数', fillcolor='lightcyan')
dot.node('BizGroup', '是否有明确的业务分组', shape='diamond', fillcolor='lightyellow')
dot.node('GroupMatch', '仅保留重叠性良好的\n分组匹配估计结果', fillcolor='lightcyan')
dot.node('LATE', '转向估计局部参数 LATE', fillcolor='lightcyan')

# 局部参数路径
dot.node('NaturalCut', '是否存在自然断点\n如触发策略的门槛', shape='diamond', fillcolor='lightyellow')
dot.node('Manipulation', '是否存在明显操纵行为', shape='diamond', fillcolor='lightyellow')
dot.node('RDD', 'RDD', fillcolor='lightcyan')
dot.node('Bunching', 'Bunching Analysis', fillcolor='lightcyan')
dot.node('FindIV', '是否可找到工具变量', shape='diamond', fillcolor='lightyellow')
dot.node('IV', 'IV', fillcolor='lightcyan')

# 汇总节点
dot.node('Robustness', '稳健性检验: 基于经济理论业务直觉、\n数据描述、安慰剂检验、敏感性分析等', fillcolor='lightpink')
dot.node('End', '结束', shape='ellipse', fillcolor='lightcoral')

# 定义边
dot.edge('Start', 'FindControl')
dot.edge('FindControl', 'ModelBased', label='N')
dot.edge('FindControl', 'DesignBased', label='Y')

# Model-based 分支
dot.edge('ModelBased', 'BusinessInsight')
dot.edge('BusinessInsight', 'EconModel', label='Y')
dot.edge('BusinessInsight', 'StatModel', label='N')

# Design-based 分支
dot.edge('DesignBased', 'Unobserved')
dot.edge('Unobserved', 'DID', label='Y')
dot.edge('Unobserved', 'PSM', label='N')

# DID 分支
dot.edge('DID', 'ClassicDID')
dot.edge('ClassicDID', 'TWFE', label='Y')
dot.edge('ClassicDID', 'StaggeredDID', label='N')
dot.edge('TWFE', 'PreTrend')
dot.edge('PreTrend', 'Robustness', label='Y')
dot.edge('PreTrend', 'AdjustTrend', label='N')
dot.edge('AdjustTrend', 'TWFE', label='Y')
dot.edge('AdjustTrend', 'SCM', label='N')

# PSM 分支
dot.edge('PSM', 'Overlap')
dot.edge('Overlap', 'LossSample', label='Y')
dot.edge('Overlap', 'NarrowScope', label='N')
dot.edge('LossSample', 'Balance', label='Y')
dot.edge('LossSample', 'IPW_DR', label='N')
dot.edge('Balance', 'Robustness', label='Y')
dot.edge('Balance', 'IPW_DR', label='N')
dot.edge('IPW_DR', 'ORDML')

# 重叠性未通过路径
dot.edge('NarrowScope', 'Redefine', label='Y')
dot.edge('NarrowScope', 'ORDML', label='N')
dot.edge('Redefine', 'BizGroup')
dot.edge('BizGroup', 'GroupMatch', label='Y')
dot.edge('BizGroup', 'LATE', label='N')

# 局部参数路径
dot.edge('LATE', 'NaturalCut')
dot.edge('NaturalCut', 'Manipulation', label='Y')
dot.edge('Manipulation', 'RDD', label='N')
dot.edge('Manipulation', 'Bunching', label='Y')
dot.edge('NaturalCut', 'FindIV', label='N')
dot.edge('FindIV', 'IV', label='Y')
dot.edge('FindIV', 'GroupMatch', label='N')

# 汇总至结束
dot.edge('EconModel', 'Robustness')
dot.edge('StatModel', 'Robustness')
dot.edge('StaggeredDID', 'Robustness')
dot.edge('SCM', 'Robustness')
dot.edge('ORDML', 'Robustness')
dot.edge('GroupMatch', 'Robustness')
dot.edge('RDD', 'Robustness')
dot.edge('Bunching', 'Robustness')
dot.edge('IV', 'Robustness')

dot.edge('Robustness', 'End')

# 展示
dot
# dot.render('/tmp/causal_inference_flowchart', view=False)
# print("流程图已生成: /tmp/causal_inference_flowchart.png")