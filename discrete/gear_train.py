# 齒輪系設計問題(離散型)

import numpy as np

# 種群數量
#设置参数
#种群数量
pop = 30
#最大迭代次数
MaxIter = 100
#维度
dim = 7
#下边界
lb =  12*np.ones(dim)
#上边界
ub =  60*np.ones(dim)

def fun(X):
    x1 = int(X[0])
    x2 = int(X[1])
    x3 = int(X[2])
    x4 = int(X[3])
    fitness = (1/6.931 - x2*x3/(x1*x4))**2
    return fitness
