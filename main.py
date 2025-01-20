import pandas as pd


import random


random_number = random.randint(0, 1000)
# print(random_number)


# 请将文件路径替换为您的实际Excel文件路径
file_path = '/Users/cuixiaoyu/Desktop/斜率计算.xlsx'
pd.set_option('display.max_columns', None)


# 加载数据，确保使用正确的工作表名称和索引列
data = pd.read_excel(file_path, sheet_name='Sheet1', index_col=0)
print(data)

# 将数据转换为数值类型，确保计算不会因类型问题出错
data = data.apply(pd.to_numeric, errors='coerce')

# 计算各阶段的斜率
slopes = data.diff(axis=0).dropna()

# 计算累积绝对值斜率和
cumulative_absolute_slope_sum = slopes.abs().sum()
cumulative_absolute_slope_sum_sorted = cumulative_absolute_slope_sum.sort_values(ascending=False)

# 计算带符号的累积斜率和
cumulative_slope_sum = slopes.sum()

# 计算每个模型的平均准确率（Avg_Accuracy）
accuracy_data = data.mean(axis=0)

# 计算每个模型的Balance-Score (倒数转换)
balance_score = 1 / (1 + cumulative_absolute_slope_sum)

# 归一化CG-A值，防止平衡性得分过高
max_cg_a = cumulative_absolute_slope_sum.max()
normalized_cg_a = cumulative_absolute_slope_sum / max_cg_a

# 计算Balance-Score
norm_balance_score = 1 / (1 + normalized_cg_a)

# 输出结果
print("累积绝对值斜率和:")
print(cumulative_absolute_slope_sum)

print("累积绝对值斜率和（排序）:")
print(cumulative_absolute_slope_sum_sorted)

print("\n带符号的累积斜率和:")
print(cumulative_slope_sum)

print("\n各阶段斜率:")
print(slopes)

# 创建DataFrame显示最终结果
final_results = pd.DataFrame({
    'Avg_Accuracy': accuracy_data,
    'Balance-Score': balance_score,
    'norm-Balance-Score': norm_balance_score
})

print("\n最终结果 (Avg_Accuracy 和 Balance-Score):")
print(final_results)




"""
          Appscanner  FlowPrint    CUMUL      DF  GraphDApps  FS-Net  TSCRNN  2D-CNN  TFE-GNN  ET-Bert    YaTC  TrafficGPT  
ISCX-VPN                                                                       
No-EN         0.7633      0.6010  0.6022  0.7300      0.7331  0.7397  0.7985  0.7862   0.7433   0.8707   0.9049     0.8814  
EN-Field      0.7328      0.5835  0.6205  0.6844      0.6979  0.7290  0.7567  0.6832   0.6885   0.8175   0.8555     0.8423   
EN            0.7137      0.6094  0.6220  0.6920      0.6849  0.7248  0.7110  0.6068   0.6059   0.5399   0.6198     0.5927 

累积绝对值斜率和:
Appscanner    0.0496
FlowPrint     0.0434
CUMUL         0.0198
DF            0.0532
GraphDApps    0.0482
FS-Net        0.0149
TSCRNN        0.0875
2D-CNN        0.1794
TFE-GNN       0.1374
ET-Bert       0.3308
YaTC          0.2851
TrafficGPT    0.2887
dtype: float64

累积绝对值斜率和（排序）:
ET-Bert       0.3308
TrafficGPT    0.2887
YaTC          0.2851
2D-CNN        0.1794
TFE-GNN       0.1374
TSCRNN        0.0875
DF            0.0532
Appscanner    0.0496
GraphDApps    0.0482
FlowPrint     0.0434
CUMUL         0.0198
FS-Net        0.0149
dtype: float64

带符号的累积斜率和:
Appscanner   -0.0496
FlowPrint     0.0084
CUMUL         0.0198
DF           -0.0380
GraphDApps   -0.0482
FS-Net       -0.0149
TSCRNN       -0.0875
2D-CNN       -0.1794
TFE-GNN      -0.1374
ET-Bert      -0.3308
YaTC         -0.2851
TrafficGPT   -0.2887
dtype: float64

各阶段斜率:
          Appscanner  FlowPrint    CUMUL      DF  GraphDApps  FS-Net  TSCRNN  2D-CNN  TFE-GNN   ET-Bert    YaTC  TrafficGPT  
ISCX-VPN                                                                       
EN-Field     -0.0305     -0.0175  0.0183 -0.0456     -0.0352 -0.0107 -0.0418  -0.1030  -0.0548  -0.0532   -0.0494  -0.0391  
EN           -0.0191      0.0259  0.0015  0.0076     -0.0130 -0.0042 -0.0457  -0.0764  -0.0826  -0.2776   -0.2357  -0.2496  




最终结果 (Avg_Accuracy 和 Balance-Score):
            Avg_Accuracy  Balance-Score  norm-Balance-Score
Appscanner      0.736600       0.952744            0.869611
FlowPrint       0.597967       0.958405            0.884019
CUMUL           0.614900       0.980584            0.943525
DF              0.702133       0.949487            0.861458
GraphDApps      0.705300       0.954016            0.872823
FS-Net          0.731167       0.985319            0.956899
TSCRNN          0.755400       0.919540            0.790820
2D-CNN          0.692067       0.847889            0.648373
TFE-GNN         0.679233       0.879198            0.706536
ET-Bert         0.742700       0.751428            0.500000
YaTC            0.793400       0.778150            0.537100
TrafficGPT      0.772133       0.775976            0.533979




Process finished with exit code 0






          Appscanner  FlowPrint    CUMUL      DF  GraphDApps  FS-Net  TSCRNN  \
ISCX-Tor                                                                       
No-EN         0.7212      0.5507  0.5656  0.6351      0.6781  0.7500  0.7894   
EN-Field      0.6942      0.5425  0.4741  0.6216      0.5641  0.5692  0.6295   
EN            0.6941      0.5557  0.4582  0.6081      0.5922  0.6825  0.6119   

          2D-CNN  TFE-GNN  ET-Bert    YaTC  TrafficGPT  
ISCX-Tor                                                
No-EN     0.7162   0.6849   0.7162  0.7703      0.7437  
EN-Field  0.6891   0.5405   0.5811  0.6216      0.6012  
EN        0.5945   0.4826   0.5541  0.6216      0.5806  
累积绝对值斜率和:
Appscanner    0.0271
FlowPrint     0.0214
CUMUL         0.1074
DF            0.0270
GraphDApps    0.1421
FS-Net        0.2941
TSCRNN        0.1775
2D-CNN        0.1217
TFE-GNN       0.2023
ET-Bert       0.1621
YaTC          0.1487
TrafficGPT    0.1631
dtype: float64
累积绝对值斜率和（排序）:
FS-Net        0.2941
TFE-GNN       0.2023
TSCRNN        0.1775
TrafficGPT    0.1631
ET-Bert       0.1621
YaTC          0.1487
GraphDApps    0.1421
2D-CNN        0.1217
CUMUL         0.1074
Appscanner    0.0271
DF            0.0270
FlowPrint     0.0214
dtype: float64

带符号的累积斜率和:
Appscanner   -0.0271
FlowPrint     0.0050
CUMUL        -0.1074
DF           -0.0270
GraphDApps   -0.0859
FS-Net       -0.0675
TSCRNN       -0.1775
2D-CNN       -0.1217
TFE-GNN      -0.2023
ET-Bert      -0.1621
YaTC         -0.1487
TrafficGPT   -0.1631
dtype: float64

各阶段斜率:
          Appscanner  FlowPrint    CUMUL      DF  GraphDApps  FS-Net  TSCRNN  \
ISCX-Tor                                                                       
EN-Field     -0.0270     -0.0082 -0.0915 -0.0135     -0.1140 -0.1808 -0.1599   
EN           -0.0001      0.0132 -0.0159 -0.0135      0.0281  0.1133 -0.0176   

          2D-CNN  TFE-GNN  ET-Bert    YaTC  TrafficGPT  
ISCX-Tor                                                
EN-Field -0.0271  -0.1444  -0.1351 -0.1487     -0.1425  
EN       -0.0946  -0.0579  -0.0270  0.0000     -0.0206  





            Avg_Accuracy  Balance-Score  norm-Balance-Score
Appscanner      0.703167       0.973615            0.915629
FlowPrint       0.549633       0.979048            0.932171
CUMUL           0.499300       0.903016            0.732503
DF              0.621600       0.973710            0.915914
GraphDApps      0.611467       0.875580            0.674232
FS-Net          0.667233       0.772738            0.500000
TSCRNN          0.676933       0.849257            0.623622
2D-CNN          0.666600       0.891504            0.707311
TFE-GNN         0.569333       0.831739            0.592466
ET-Bert         0.617133       0.860511            0.644673
YaTC            0.671167       0.870549            0.664182
TrafficGPT      0.641833       0.859771            0.643263

"""