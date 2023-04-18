# Welded beam structure problem(焊樑結構問題)
import numpy as np

# 设置参数(主要)
# 種群數量
pop = 30
# 維度
dim = 4 # 维度
# 最大迭代次數
MaxIter = 1000
# 下邊界
lb = np.array([0.1,0.1,0.1,0.1])
# 上邊界
ub = np.array([2,10,10,2])

# 參考焊接樑設計問題>問題模型(五)
def fun(X):
    # 焊縫厚度(h)
    x1 = X[0]
    # 鋼筋連接部分長度(l)
    x2 = X[1]
    # 鋼筋高度(t)
    x3 = X[2]
    # 鋼筋厚度(b)
    x4 = X[3]

    # 問題參數
    P = 6000
    L = 14
    delta_max = 0.25
    E = 30*10**6
    G = 12 * 10**6
    t_max = 13600
    sigma_max = 30000 

    # 問題變數

    M = P * (L+x2/2)
    R = np.sqrt(x2**2/4+((x1+x3)/2)**2)
    J = 2*(np.sqrt(2)*x1*x2*((x2**2/12)+((x1+x3)/2)**2))

    # 樑的彎曲應力(s)
    sigma = 6*P*L / (x4*x3**2)
    # 梁的末端挠度(d)
    delta = 4*P*L**3 / (E*x3**3*x4)
    # 杆件上的屈曲载荷
    P_c = (4.013*E*np.sqrt(x3**2*x4**6/36) / L**2)*(1-(x3/(2*L)*np.sqrt(E/(4*G))))

    # 剪應力(t)
    t1 = P / (np.sqrt(2) * x1 * x2)
    t2 = M*R / J
    t = np.sqrt(t1**2+(2*t1*t2*x2/(2*R))+t2**2)
    # 約束條件
    g1 = t-t_max

    g2 = sigma - sigma_max
    g3 = x1 - x4
    g4 = 0.10471*x1**2 + 0.04811*x3*x4*(14+x2)-5
    g5 = 0.125-x1
    g6 = delta - delta_max
    g7 = P - P_c


    if(g1<=0 and g2<=0 and g3<=0 and g4<=0 and g5<=0 and g6<=0 and g7<=0):
        # 計算適應值
        # print("可行解限制函數: ",g1,g2,g3,g4,g5,g6,g7)
        fitness = 1.10471*x1**2*x2+0.04811*x3*x4*(14+x2)
    else:
        # print("不可行解限制函數: ",g1,g2,g3,g4,g5,g6,g7)
        fitness = 10E32
    
    return fitness