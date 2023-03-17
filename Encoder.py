import numpy as np
from FDCT import FDCT
import cv2
from matrix_to_zigzag import m2z
from run_length_encoder import rlc

def encoder(s):
    # 离散余弦变换正变换
    S = FDCT(s)
    S = S.astype(int)
    # 量化矩阵的定义
    Qt = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                  [12, 12, 14, 19, 26, 58, 60, 55],
                  [14, 13, 16, 24, 40, 57, 69, 56],
                  [14, 17, 22, 29, 51, 87, 80, 62],
                  [18, 22, 37, 56, 68, 109, 103, 77],
                  [24, 35, 55, 64, 81, 104, 113, 92],
                  [49, 64, 78, 87, 103, 121, 120, 101],
                  [72, 92, 95, 98, 112, 100, 103, 99]],
                  dtype=int)
    # 把S量化得到S1
    S1 = np.round(S/Qt)
    # 把S1进行zigzag得到z
    z = m2z(S1)
    z = z.astype(int)
    z_prime = rlc(z)
    size_z = z_prime.size
    # 以下做截断的原因是把后面全是0截断，于是encode出来的就可以少两个数字，提高压缩率。
    z_prime = z_prime[0:size_z-2]
    # 转换为整数是因为比较好看
    z_prime = z_prime.astype(int)
    return z_prime
