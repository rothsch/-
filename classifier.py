import os
import glob #for loading images from a directory
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import cv2
import random
import numpy as np

def standardize_input(image):
    
    # 调整图像大小并进行预处理，使所有“标准”图像大小相同
    standard_im = cv2.resize(image, (1100, 600))
    
    return standard_im
# 查找图像的平均值或亮度
def avg_brightness(rgb_image):
    # 将图像转换为HSV
    hsv = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)

    # 将V通道中的所有像素值相加
    sum_brightness = np.sum(hsv[:,:,2])
    area = 600*1100.0  # 像素
    
    # 求平均值
    avg = sum_brightness/area
    
    return avg
  
def estimate_label(rgb_image, threshold):
    
    # 从RGB图像中提取平均亮度特征
    avg = avg_brightness(rgb_image)
        
    # 使用平均亮度特征来预测标签 (0, 1)
    predicted_label = 0
    #threshold = 120
    if(avg > threshold):
        # 如果平均亮度高于阈值，我们将其归类为“白天”
        predicted_label = 1
    # 否则，pred-ted_label可以保持0（预测为“夜间”）
    
    return predicted_label    
    
def preprocess(image_list):
    
    #对输入数据进行标准化和编码
    standard_list = []
    
    # 遍历所有图像标签对
    for item in image_list:
        image = item
        # 标准化图像
        standardized_im = standardize_input(image)
        
        # 将图像附加到经过处理的完整图像数据列表中，这是一个热编码标签
        standard_list.append((standardized_im,estimate_label(standardized_im)))
    
    return standard_list