# 匯入
import numpy as np
from matplotlib import pyplot as plt

import import_ipynb
import numpy as np

# 定義節點坐標(nodes)
nodes = np.array([
    [0, 0], [0, 3], [1, 1], [1, 2], [2, 0], [2, 3], [3, 1], [3, 2],
    [4, 0], [4, 3], [5, 1], [5, 2], [6, 0], [6, 3], [7, 1], [7, 2],
    [8, 0], [8, 3], [9, 1], [9, 2], [10, 0], [10, 3], [11, 1], [11, 2],
    [12, 0], [12, 3]
])

# 定義連接矩陣(members)
members = np.array([
    [0, 2], [0, 4], [1, 3], [1, 5], [2, 3], [2, 6], [3, 7], [4, 6],
    [4, 8], [5, 7], [5, 9], [6, 10], [6, 11], [7, 12], [8, 10], [8, 13],
    [9, 11], [9, 14], [10, 11], [10, 15], [11, 16], [12, 15], [12, 17], [13, 16],
    [13, 18], [14, 17], [14, 19], [15, 16], [15, 20], [16, 21], [17, 20],
    [17, 22], [18, 21], [18, 23], [19, 22], [19, 24], [20, 21], [20, 23],
    [21, 24], [22, 23], [23, 24]
])


# 定義邊界條件和載荷
supports = [0, 1, 4, 5, 8, 9, 12, 17, 22, 23, 24]
loads = np.zeros(len(nodes)*2)
loads[8*2+1] = -5000 # 節點 8 處施加的載荷（向下）
# 計算適應值函數
def fitness(x, nodes, members, E, A, supports, loads):
    # 更新節點坐標

    new_nodes = nodes + x.reshape(-1, 2)
    # 計算連接長度
    dx = new_nodes[members[:, 1]] - new_nodes[members[:, 0]]
    L = np.sqrt(np.sum(dx**2, axis=1))
    # 計算連接力
    K = np.zeros((len(nodes)*2, len(nodes)*2))
    for i, (n1, n2) in enumerate(members):
        dx = new_nodes[n2] - new_nodes[n1]
        L = np.sqrt(np.sum(dx**2))
        cos_theta = dx[0]/L
        sin_theta = dx[1]/L
        k = np.array([
            [cos_theta**2, cos_theta*sin_theta, -
                cos_theta**2, -cos_theta*sin_theta],
            [cos_theta*sin_theta, sin_theta**2, -
                cos_theta*sin_theta, -sin_theta**2],
            [-cos_theta**2, -cos_theta*sin_theta,
                cos_theta**2, cos_theta*sin_theta],
            [-cos_theta*sin_theta, -sin_theta**2,
                cos_theta*sin_theta, sin_theta**2]
        ])
        K[np.ix_([2*n1, 2*n1+1, 2*n2, 2*n2+1],
                 [2*n1, 2*n1+1, 2*n2, 2*n2+1])] += k*(E*A/L)
    # 應用邊界條件
    K_red = np.delete(np.delete(K, supports, axis=0), supports, axis=1)
    f_red = loads[np.logical_not(
        np.isin(np.arange(len(nodes)*2), supports))]
    u_red = np.linalg.solve(K_red, f_red)
    u = np.zeros(len(nodes)*2)
    u[np.logical_not(np.isin(np.arange(len(nodes)*2), supports))] = u_red
    # 計算連接力
    f = np.zeros(len(members))
    for i, (n1, n2) in enumerate(members):
        dx = new_nodes[n2] - new_nodes[n1]
        L = np.sqrt(np.sum(dx**2))
        cos_theta = dx[0]/L
        sin_theta = dx[1]/L
        k = np.array([
            [cos_theta**2, cos_theta*sin_theta, -
                cos_theta**2, -cos_theta*sin_theta],
            [cos_theta*sin_theta, sin_theta**2, -
                cos_theta*sin_theta, -sin_theta**2],
            [-cos_theta**2, -cos_theta*sin_theta,
                cos_theta**2, cos_theta*sin_theta],
            [-cos_theta*sin_theta, -sin_theta**2,
                cos_theta*sin_theta, sin_theta**2]
        ])
        f[i] = np.dot(
            k*(E*A/L), np.array([u[2*n1], u[2*n1+1], u[2*n2], u[2*n2+1]]))
    # 計算結構成本
    return np.sum(A*L*E)


# 問題參數設定
maxIter = 100
dim = 2
# 生成個數
nodes = 26
members = 41
supports = 11


# 定义材料属性
E = 200e9  # 杨氏模量Young's modulus
A = 0.01  # 横截面面积cross-sectional area
