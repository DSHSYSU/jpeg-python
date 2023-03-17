import numpy as np
z = np.array([3, 3, 3, 3, 3, 3, 2, 2, 2, 4, 4, 4, 4, 4, 1, 1, 114, 114])
def rlc(z):
    # 本函数的目的是把一列数进行游程编码，也就是比如说对于
    # z = np.array([3, 3, 3, 3, 3, 3, 2, 2, 2, 4, 4, 4, 4, 4, 1, 1, 114, 114])
    # 里面有6个3,3个2,5个4,2个1,2个114.
    # 所以得到的结果应该为
    # z_prime = array([  6.,   3.,   3.,   2.,   5.,   4.,   2.,   1.,   2., 114.])
    z = z.astype(int)
    z_size = z.size
    z = np.append(z, [np.nan])
    i = 0
    j = 1
    z_prime = np.array([])
    while i < z_size:
        if z[j] == z[i]:
            j = j + 1
        else:
            z_prime = np.append(z_prime, [j - i, z[i]])
            i = j
    return z_prime

z_prime = rlc(z)