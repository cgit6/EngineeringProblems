# 工字樑結構設計
import numpy as np

# 设置参数(主要)
# 種群數量
#设置参数
#种群数量
pop = 30
#最大迭代次数
MaxIter = 1000
#维度
dim = 7
#下边界
lb = np.array([10,10,0.9,0.9]) 
#上边界
ub = np.array([80,50,5,5])

def fun (X):
    # 變數
    x1 = X[0]
    x2 = X[1]
    x3 = X[2]
    x4 = X[3]
    # 約束條件

    if():
        # 聯立方程式求解
        pass
