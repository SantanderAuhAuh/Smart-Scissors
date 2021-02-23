# -*- coding: utf-8 -*-
import numpy as ny
import cv2
from Scissor import Scissor


def main():
    # 读入图片
    img = cv2.imread('demo.png')
    img_drawing = cv2.cvtColor(img, cv2.COLOR_RGB2RGBA)
    # img_drawing = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img_instance = Scissor(img_drawing)
    # 创建窗口并展示图片
    cv2.imshow('image', img_drawing)
    # 等待任意一个按键按下
    cv2.waitKey(0)
    # 关闭所有的窗口
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
