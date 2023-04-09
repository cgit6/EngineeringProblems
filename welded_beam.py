# Welded beam structure problem(焊樑結構問題)
import numpy as np

# 设置参数(主要)
# 種群數量
pop = 30
# 維度
dim = 2 # 维度
# 最大迭代次數
MaxIter = 100  
# 下邊界
lb = [0.1,0.1,0.1,0.1]
# 上邊界
ub = [2,10,10,2]

# 參考焊接樑設計問題>問題模型(四)
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
    P = 60001 
    L = 14
    delta_max = 0.25
    E = 30*10**6
    G = 12 * 10**6
    t_max = 13600
    sigma_max = 30000 

    # 問題變數

    M = P * (L+(x2/2))
    R = np.sqrt(x2**2/4+((x1+x3)/2)**2)
    J = 2*(np.sqrt(2)*x1*x2*((x2**2/4)*((x1+x3)/2)**2))

    # 樑的彎曲應力(s)
    sigma = 6*P*L / (x4*x3**2)
    # 梁的末端挠度(d)
    delta = 4*P*L**3 / (E*x3**2+x4)
    # 杆件上的屈曲载荷
    P_c = 4.013*E*np.sqrt(x3**2 * x4**6/36) / L**2*(1-(x3/2*L)*np.sqrt(E/4*G))

    # 剪應力(t)
    t1 = P / (np.sqrt(2) * x1 * x2)
    t2 = (M*R) / J
    t = np.sqrt(t1**2+2*t1*t2*x2/(2*R)+t2**2)
    # 約束條件



    if():
        # 計算適應值
        