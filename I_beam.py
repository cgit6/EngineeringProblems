# 工字樑結構設計
import numpy as np

import scipy as sp

# 设置参数(主要)
# 種群數量
#设置参数
#种群数量
pop = 30
#最大迭代次数
MaxIter = 10
#维度
dim = 7
#下边界
lb = np.array([10,10,0.9,0.9]) 
#上边界
ub = np.array([80,50,5,5])

def fun (X):
    # 變數
    x1 = int(X[0])
    x2 = X[1]
    x3 = X[2]
    x4 = X[3]
    # 約束條件
    g1 = 180000*x1/(x3*(x1-2*x4)**3+2*x2*x4*[4*x4**2+3*x1*(x1-2*x4)])+15000*x2/((x1-2*x4)*x3**3+2*x4*x2**3)

    if(g1<=16):
        # 聯立方程式求解
        def fit(X):
            finess = sp


    else:
        fitness = 10E32
    
    return fitness
