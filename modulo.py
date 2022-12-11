# -*- coding: UTF-8 -*-

import time

# 求两个数字的最大公约数 (欧几里得算法)
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# 扩展欧几里的算法
# 计算 ax + by = 1 中的 x 与 y 的整数解 ( a 与 b 互素)
def ext_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        r, x1, y1 = ext_gcd(b, a % b)
        x = y1
        y = x1 - a // b * y1
        return r, x, y

# 模反复平方算法
# 计算 x ^ k mod n
def rep_quad_mod_pow(x, k, n):
    a = 1
    b = x
    bit_array = bin(k)[2:][::-1]
    for i in bit_array:
        if i == '1':
            a = a * b % n
        b = b * b % n
    return a

# 蒙哥马利约减,
# 计算 X / R mod N (R = 2 ^ k 且 R > N 且 R 和 N 互素)
def mont_red(x, r, k, n):
    assert (r == 1 << k)
    gcd, inv_r, inv_n = ext_gcd(r, n)
    assert (gcd == 1)
    m = x * (-inv_n) % r
    y = (x + m * n) >> k
    return (y - n) if (y > n) else y

# 蒙哥马利模乘
# 计算 a * b mod n
def mont_mul(a, b, n):
    k = n.bit_length()
    r = 1 << k
    a_dot = a * r % n
    b_dot = b * r % n
    x = a_dot * b_dot

    x1 = mont_red(x, r, k, n)
    y = mont_red(x1, r, k, n)

    return y

# 蒙哥马利模幂
# 计算 x ^ k mod n
def mont_pow(x, k, n):
    a = 1
    b = x
    bit_array = bin(k)[2:][::-1]
    for i in bit_array:
        if i == '1':
            a = mont_mul(a, b, n)
        b = mont_mul(b, b, n)
    return a


if __name__ == '__main__':
    print(mont_pow(12, 12, 37))
