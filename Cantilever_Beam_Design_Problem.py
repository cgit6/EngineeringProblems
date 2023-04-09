# Cantilever Beam Design Problem
import numpy as np

# 设置参数(主要)
# 種群數量
pop = 30
# 維度
dim = 5 # 维度
# 最大迭代次數
MaxIter = 1000
# 下邊界
lb = 0.01*np.ones(dim)
# 上邊界
ub = 100*np.ones(dim)

# input 
def fun(X):
    # 變數
    x1 = X[0]
    x2 = X[1]
    x3 = X[2]
    x4 = X[3]
    x5 = X[4]

    # 限制函式
    g1 = 60/x1**3+27/x2**3+19/x3**3+7/x4**3+1/x5**3
    if (g1 <= 1):
        # 計算適應值
        fitness = 0.6224*sum(X)
    else:
        # 如果不滿足約束條件，則設置適應度值為很大的一個懲罰數
        fitness = 10E32
        # 或是調整到可行範圍，怎麼調?

    return fitness