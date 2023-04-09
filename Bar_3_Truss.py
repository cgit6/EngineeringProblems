import numpy as np


# 设置参数(主要)
# 種群數量
pop = 30
# 維度
dim = 2 # 维度
# 最大迭代次數
MaxIter = 100  
# 下邊界
lb = 0.001*np.ones(dim)
# 上邊界
ub = 1*np.ones(dim)

# 三桿桁架設計問題
def fun(X):
        # 變數
        x1 = X[0]
        x2 = X[1]
        # x1=x3

        # 長度
        l = 100
        # 荷載
        P = 2
        # 應力
        sigma = 2

        #限制式
        g1 = (np.sqrt(2)*x1+x2)*P/(np.sqrt(2)*x1**2+2*x1*x2)-sigma
        g2 = x2*P/(np.sqrt(2)*x1**2+2*x1*x2) - sigma
        g3 = P/(np.sqrt(2)*x2+x1)-sigma
        if g1<=0 and g2<=0 and g3<=0:
            #如果满足限制条件则计算适应度值
            fitness = (2*np.sqrt(2)*x1+x2)*l
        else:
            #如果不满足限制条件，则设置适应度值为很大的一个惩罚数
            fitness = 10E32
        
        return fitness
