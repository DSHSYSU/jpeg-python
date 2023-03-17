import numpy as np
from zigzag_to_matrix import z2m
from IDCT import IDCT
from run_length_decoder import rld

def decoder(z_prime):
    # 转换为numpy格式
    z_prime = np.array(z_prime)
    # 把z_prime进行run length decoding（游程解码）恢复出64长的z
    z = rld(z_prime)
    # 把z进行反zigzag得到8x8的矩阵
    S1 = z2m(z)
    #量化矩阵的定义
    Qt = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                   [12, 12, 14, 19, 26, 58, 60, 55],
                   [14, 13, 16, 24, 40, 57, 69, 56],
                   [14, 17, 22, 29, 51, 87, 80, 62],
                   [18, 22, 37, 56, 68, 109, 103, 77],
                   [24, 35, 55, 64, 81, 104, 113, 92],
                   [49, 64, 78, 87, 103, 121, 120, 101],
                   [72, 92, 95, 98, 112, 100, 103, 99]],
                  dtype=int)
    # 乘以量化矩阵（哈达玛积（也就是对应元素相乘））得到恢复的离散余弦变换系数矩阵（当然有很多0）
    S2 = S1 * Qt
    # 对S2进行离散余弦变换的逆变换
    s_pred = IDCT(S2)
    s_pred = np.array(s_pred)
    s_pred = s_pred.astype(int)
    return s_pred
z_prime = np.array([1, 114, 1, 0, 1, 8, 1, -5, 5, 0, 1, 5, 1, -3, 9, 0, 1, 2])
s_pred = decoder(z_prime)