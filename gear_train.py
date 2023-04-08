from scipy.optimize import minimize
from scipy.optimize import rosen, differential_evolution

def objective_function(x):
    # x是一个包含齿轮设计参数的向量
    volume = x[0] * x[1]**2 * x[2] # 计算齿轮系统的体积
    return volume

def constraint1(x):
    # x是一个包含齿轮设计参数的向量
    strength = 2 * x[1] * x[2] / x[0]**2 - 1 # 计算齿轮强度
    return strength - 1.0

def constraint2(x):
    # x是一个包含齿轮设计参数的向量
    torque = 10 * x[2] - x[1]**2 * x[0] # 计算扭矩传递能力
    return torque - 1.0


# 定义齿轮设计参数和约束条件
bounds = [(1, 5), (10, 50), (0.1, 1.0)]
con1 = {'type': 'ineq', 'fun': constraint1}
con2 = {'type': 'ineq', 'fun': constraint2}
cons = [con1, con2]

# 使用遗传算法搜索最优解
result = differential_evolution(objective_function, bounds, constraints=cons)
print(result.x)
