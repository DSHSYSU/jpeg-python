import numpy as np
z_prime = np.array([1, 114, 1, 0, 1, 8, 1, -5, 5, 0, 1, 5, 1, -3, 9, 0, 1, 2])

def rld(z_prime):
    # 按照游程编码的规则进行解码
    i = 0
    z = np.array([])
    z_prime = np.array(z_prime)
    z_prime = z_prime.astype(int)
    z_prime_length = z_prime.size
    while i < z_prime_length:
        z_i = z_prime[i]
        z_i_plus_1 = z_prime[i+1]
        z = np.append(z, z_i_plus_1 * np.ones(z_i))
        i = i + 2
    z_length = z.size
    z = np.append(z, np.zeros(64-z_length))
    return z

z = rld(z_prime)