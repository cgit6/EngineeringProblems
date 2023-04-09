import math
import numpy as np


# 设置参数(主要)
# 種群數量
pop = 50  
# 維度
dim = 15 # 维度
# 最大迭代次數
MaxIter = 100  
# 下邊界
lb = -1*np.ones(dim)
# 上邊界
ub = 1*np.ones(dim)


def truss_15_fitness(X):
    nodes = [
        X[0],
        X[1],
        X[2],
        X[3],
        X[4],
        X[5],
        X[6],
        X[7],
        X[8],
        X[9],
        X[10],
        X[11],
        X[12],
        X[13],
        X[14],
    ]
    bars = [
        (0, 5),
        (0, 6),
        (1, 6),
        (1, 7),
        (2, 7),
        (2, 8),
        (3, 8),
        (3, 9),
        (4, 9),
        (0, 10),
        (1, 10),
        (1, 11),
        (2, 11),
        (2, 12),
        (3, 12),
        (3, 13),
        (4, 13),
        (4, 14),
        (3, 14),
        (2, 14),
        (1, 14),
        (0, 14),
    ]
    support_nodes = [10, 11, 12, 13, 14]
    force_node = 5
    force = (1000, 90)
    areas = [0.01 * x for x in X]
    E = 70000
    rho = 2700
    lengths = [math.sqrt((nodes[b[1]][0] - nodes[b[0]][0]) **
                         2 + (nodes[b[1]][1] - nodes[b[0]][1]) ** 2) for b in bars]
    angles = [math.atan2(nodes[b[1]][1] - nodes[b[0]][1],
                         nodes[b[1]][0] - nodes[b[0]][0]) for b in bars]

    # TODO: 計算適應度

    return fitness





# 這個函數定義了一個名為 fun 的函數，用來構建一個 15杆桁架問題。這個問題由以下參數組成：
# nodes: 節點座標列表，每個元素是一個包含兩個浮點數的元組，分別表示節點的 x 和 y 坐標。
# bars: 杆件連接的節點，每個元素是一個包含兩個整數的元組，分別表示杆件連接的兩個節點的索引。
# support_nodes: 支撐節點的索引列表，表示這些節點被固定不動。
# force_node: 受力節點的索引，表示在這個節點施加一個力。
# force: 受力節點施加的力，是一個包含兩個浮點數的元組，分別表示施加的力的大小和方向。
# areas: 杆件的斷面面積，是一個與 bars 長度相同的列表，每個元素表示對應杆件的斷面面積。
# E: 材料的弾性模量，一個浮點數。
# rho: 材料的密度，一個浮點數。
# lengths: 每個杆件的長度，是一個與 bars 長度相同的列表，每個元素表示對應杆件的長度。
# angles: 每個杆件的角度，是一個與 bars 長度相同的列表，每個元素表示對應杆件的角度。
# 這個函數返回一個包含上述參數的字典，表示構建出的 15杆桁架問題。這個函數並沒有求解問題的功能，只是用來構建問題。




