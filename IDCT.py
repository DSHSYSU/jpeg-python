import numpy as np
def IDCT(S):
    # 离散余弦变换的逆变换
    # FDCT和IDCT都会用到的那个矩阵C
    C = np.ones([8, 8])
    C[0, :] = np.sqrt(0.5) * C[0, :]
    C[:, 0] = np.sqrt(0.5) * C[:, 0]
    s = np.zeros([8, 8])
    for y in range(8):
        for x in range(8):
            for u in range(8):
                for v in range(8):
                    s[y, x] = s[y, x] + \
                              C[u, v]*(S[v, u] * np.cos((2*x+1)*u*np.pi/16)*np.cos((2*y+1)*v*np.pi/16))
    s = s/4
    return s