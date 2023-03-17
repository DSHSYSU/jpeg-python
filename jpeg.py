import numpy as np
from Encoder import encoder
from Decoder import decoder
import cv2

def jpeg(s):
    # 把原始的8x8的8bit（0-255整数）灰度矩阵转换成numpy格式
    s = np.array(s)
    # 转换成int就是为了不保留原来的uint8，方便后面做计算不出错
    s = s.astype(int)
    # 每个像素减去128使得矩阵的每个元素分布在-128到127之间
    s = s - 128
    # 编码s得到一列短的z_prime（通常长度只有十几）
    z_prime = encoder(s)
    # 最后得到的是解码后的s_pred，也是8x8的
    s_pred = decoder(z_prime)
    # 由于第一步减去了128，现在要把128加回来，使得结果位于0-255之间
    s_pred = s_pred + 128
    return s_pred

img = cv2.imread("testimg.png")
s = img[50:58, 60:68, 1]
s_pred = jpeg(s)
