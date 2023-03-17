import numpy as np
def FDCT(s):
    # 离散余弦变换
    # FDCT和IDCT都会用到的那个矩阵C
    C = np.ones([8, 8])
    C[0, :] = np.sqrt(0.5) * C[0, :]
    C[:, 0] = np.sqrt(0.5) * C[:, 0]
    S = np.zeros([8, 8])
    for v in range(8):
        for u in range(8):
            for x in range(8):
                for y in range(8):
                    S[v, u] = S[v, u] + \
                              C[u, v]*(s[y, x] * np.cos((2*x+1)*u*np.pi/16)*np.cos((2*y+1)*v*np.pi/16))
    S = S/4
    return S