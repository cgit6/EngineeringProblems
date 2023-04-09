# # 设计参数的范围和初值
# gear_ratio_min = 5  # 減速比的最小值
# gear_ratio_max = 15  # 減速比的最大值
# output_torque_min = 1000  # 输出扭矩的最小值
# input_power_max = 10000  # 输入功率的最大值
# design_parameters = [1, 10, 2, 10, 2, 5, 2]  # 设计参数的初值

# # 检查減速比是否在范围内
# if design_parameters[0] / design_parameters[1] < gear_ratio_min:
#     print("減速比过小")
# elif design_parameters[0] / design_parameters[1] > gear_ratio_max:
#     print("減速比过大")
# else:
#     print("減速比在范围内")

# # 检查输出扭矩是否达到要求
# if 2 * design_parameters[2] * design_parameters[3] * design_parameters[1] / (design_parameters[0] * design_parameters[5]) < output_torque_min:
#     print("输出扭矩不足")
# else:
#     print("输出扭矩达到要求")

# # 检查输入功率是否超过要求
# if design_parameters[0] * design_parameters[1] * design_parameters[5] > input_power_max:
#     print("输入功率超过要求")
# else:
#     print("输入功率在范围内")

# Speed Reducer
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
lb = np.array([2.6,0.7,17,7.3,7.8,2.9,5]) 
#上边界
ub = np.array([3.6,0.8,28,8.3,8.3,3.9,5.5])

def fun(X):
    # 變數
    # W
    x1 = X[0]
    # M 
    x2 = X[1]
    # N
    x3 = X[2]
    # L_1
    x4 = X[3]
    # L_2
    x5 = X[4]
    # D_1
    x6 = X[5]
    # D_2
    x7 = X[6]
    # 約束條件
    

    g1 = 27 / (x1 * x2**2 * x3)
    g2 = 397.5 / (x1* x2**2 * x3**2)
    g3 = (1.93 * x5**3) / (x2*x3*x7**4)
    g4 = (1.93 * x4**3) / (x2*x3*x6**4)
    g5 = np.sqrt(1.57*10**8+(745*x5 / (x2*x3))**2) / (85*x7**3)
    g6 = np.sqrt(1.69*10**7+(745*x4 / (x2*x3))**2) / (110*x6**3)
    g7 = x2*x3 / 40
    g8 = x1 / 12*x2
    g9 = 5*x2 / x1
    g10 = (1.5*x6+1.9) / x4
    g11 = (1.1*x7+1.9) / x5
    

    if g1<=1 and g2<=1 and g3<=1 and g4<=1 and g5<=1 and g6<=1 and g7<=1 and g8<=1 and g9<=1 and g10<=1 and g11<=1:
        # 計算適應值
        print("可行解限制函數: ",g1,g2,g3,g4,g5,g6,g7,g8,g9,g10,g11)
        fitness = 0.7854*x1*x2**2*(14.9334*x3+3.3333*x3**2 - 43.0934)+7.4777*(x6**3+x7**3)-1.508*x1*(x6**2+x7**2)+0.7854*(x4*x6**2+x5*x7**2)
    else:
        # print("不可行解限制函數: ",g1,g2,g3,g4,g5,g6,g7,g8,g9,g10,g11)
        fitness = 10E32
    
    return fitness

def fun2(X):
        # 變數
    # W
    x1 = X[0]
    # M 
    x2 = X[1]
    # N
    x3 = X[2]
    # L_1
    x4 = X[3]
    # L_2
    x5 = X[4]
    # D_1
    x6 = X[5]
    # D_2
    x7 = X[6]
    # 約束條件