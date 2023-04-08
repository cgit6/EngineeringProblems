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


# 定義梁的尺寸和形狀
length = 3.0  # 梁的長度 (m)
height = 0.15  # 梁的高度 (m)
width = 0.2  # 梁的寬度 (m)

# 定義荷載需求
load = 1000.0  # 梁需要承受的荷載 (N)

# 定義材料
density = 7850.0  # 梁材料的密度 (kg/m^3)
elasticity = 2.0e11  # 梁材料的彈性模量 (Pa)
yield_strength = 250.0e6  # 梁材料的屈服強度 (Pa)

# 定義強度要求
safety_factor = 1.5  # 安全係數


def calculate_strength(length, height, width, load, density, elasticity, yield_strength, safety_factor):
    
    
    # 計算梁的斷面面積
    area = height * width

    # 計算梁的彈性變形
    moment_of_inertia = width * height ** 3 / 12.0
    max_stress = load * length ** 2 / (2.0 * moment_of_inertia * safety_factor)
    deformation = load * length ** 3 / (3.0 * elasticity * moment_of_inertia)
