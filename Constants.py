import numpy as np

# 拉普拉斯算子
LaplaceZeroCrossingOp = np.mat([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
# x方向梯度算子
IxOp = np.mat([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
# y方向梯度算子
IyOp = np.mat([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
# 权重变量
Wz = 0.3
Wg = 0.3
Wd = 0.1
