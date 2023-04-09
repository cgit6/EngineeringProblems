# Pressure Vessel Design Problem
import numpy as np

# 设置参数(主要)
# 種群數量
#设置参数
#种群数量
pop = 50 
#最大迭代次数
MaxIter = 500 
#维度
dim = 4 
#下边界
lb = np.array([0,0,10,10]) 
#上边界
ub = np.array([99,99,100,100])

# 壓力容器設計
def fun(X):
        x1 = X[0] #Ts
        x2 = X[1] #Th
        x3 = X[2] #R
        x4 = X[3] #L      
        #约束条件判断
        g1 = -x1+0.0193*x3
        g2 = -x2+0.00954*x3
        g3 = -np.math.pi*x3**2-4*np.math.pi*x3**3/3+1296000
        g4 = x4-240
        if g1<=0 and g2<=0 and g3<=0 and g4<=0:
            #如果满足约束条件则计算适应度值
            fitness = 0.6224*x1*x3*x4 + 1.7781*x2*x3**2 + 3.1661*x1**2*x4 + 19.84*x1**2*x3
        else:
            #如果不滿足約束條件，則設置適應度值為很大的一個懲罰數
            fitness = 10E32
        
        return fitness
