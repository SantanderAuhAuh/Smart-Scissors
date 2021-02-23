import cv2
import numpy as np
from enum import Enum
from Utils import *
from Constants import *

StateList = Enum('StateList', ('INITIAL', 'ACTIVE', 'EXPANDED'))


class Node:
    def __init__(self, args):
        self.column_index = args.get('column_index', 0)
        self.row_index = args.get('row_index', 0)
        self.pre_node = args.get('pre_node', None)
        self.state = args.get('state', StateList.INITIAL)
        self.link_cost = args.get('link_cost', [0, 0, 0, 0, 0, 0, 0, 0])
        self.total_cost = args.get('total_cost', 0)

    def __lt__(self, other):
        if self.total_cost < other.total_cost:
            return True
        else:
            return False


class Scissor:
    _instance = None

    def __new__(cls, origin_image):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, origin_image):
        # 原始输入图像
        self.origin_image = origin_image
        # 是否已开始分割
        self.isSetSeed = False
        # 图像行数
        self.row_num = self.origin_image.shape[0]
        # 图像列数
        self.col_num = self.origin_image.shape[1]
        # 图像通道数
        self.channels = self.origin_image.shape[2] if len(self.origin_image.shape) > 2 else 1
        # 拉普拉斯算子卷积后的图像
        self.FzCostMap = filter_image(self.origin_image, LaplaceZeroCrossingOp)
        self.FgCostMap = np.zeros((self.row_num, self.col_num))
        # x方向卷积计算梯度后的图像
        self.Ix = filter_image(self.origin_image, IxOp)
        # y方向卷积计算梯度后的图像
        self.Iy = filter_image(self.origin_image, IyOp)
        # 图像的计算属性
        self.nodes = [[Node({'row_index': i, 'column_index': j}) for j in range(self.col_num)] for i in range(self.row_num)]
        self.compute_cost()

    def compute_cost(self):
        # 如果是灰度图像
        if self.channels == 1:
            self.FzCostMap = np.where(self.FzCostMap < 0.00001, Wz * 1, Wz * 0)
            self
        # 如果是多通道图像
        else:
            temp = np.zeros((self.row_num, self.col_num))
            for i in range(self.row_num):
                for j in range(self.col_num):
                    temp[i][j] = max(self.FzCostMap[i][j]) * Wz
            self.FzCostMap = temp
        pass
