import cv2


# 图像卷积
def filter_image(image, kernel):
    return cv2.filter2D(image, cv2.CV_32F, kernel)
