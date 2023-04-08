# 设计参数的范围和初值
gear_ratio_min = 5  # 減速比的最小值
gear_ratio_max = 15  # 減速比的最大值
output_torque_min = 1000  # 输出扭矩的最小值
input_power_max = 10000  # 输入功率的最大值
design_parameters = [1, 10, 2, 10, 2, 5, 2]  # 设计参数的初值

# 检查減速比是否在范围内
if design_parameters[0] / design_parameters[1] < gear_ratio_min:
    print("減速比过小")
elif design_parameters[0] / design_parameters[1] > gear_ratio_max:
    print("減速比过大")
else:
    print("減速比在范围内")

# 检查输出扭矩是否达到要求
if 2 * design_parameters[2] * design_parameters[3] * design_parameters[1] / (design_parameters[0] * design_parameters[5]) < output_torque_min:
    print("输出扭矩不足")
else:
    print("输出扭矩达到要求")

# 检查输入功率是否超过要求
if design_parameters[0] * design_parameters[1] * design_parameters[5] > input_power_max:
    print("输入功率超过要求")
else:
    print("输入功率在范围内")
