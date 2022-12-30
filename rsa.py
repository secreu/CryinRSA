# -*- coding: UTF-8 -*-

import time
import random
from prime import *
from modulo import *

# 存储本地密钥
LocalKey = []

# 从文件读出 bytes 数据
def read_data(file):
    with open(file, mode='rb') as f:
        plain_bytes = f.read()
    return plain_bytes

# 将 bytes 数据写入文件
def write_data(file, data):
    with open(file, mode='wb') as f:
        f.write(data)
    return

# 生成一组密钥, 存放进 LocalKey, 返回序号 index
def gen_key(bitlen):
    p = get_prime(bitlen)
    q = get_prime(bitlen)
    while q == p:
        q = get_prime(bitlen)

    n = p * q
    n_len = n.bit_length()
    if (n_len % 8 == 0):
        block = n_len // 8
    else:
        block = n_len // 8 + 1

    fn = (p - 1) * (q - 1)
    
    d = 0
    while d == 0:
        e = random.randrange(2, fn)
        g, d, _ = ext_gcd(e, fn)
        if g != 1:
            d = 0
    d = d % n

    LocalKey.append([e, d, n, block])

    return len(LocalKey) - 1

# 从 LocalKey 删除序号为 index 的一组密钥
# 成功返回 true, 失败返回 false
def del_key(index):
    if (len(LocalKey) < index):
        return False
    else:
        del(LocalKey[index])
        return True

# 加密, 按 block - 1 字节读, 扩展为 block 字节存
def encrypt(in_file, out_file, ki):
    e = LocalKey[ki][0]
    n = LocalKey[ki][2]
    block = LocalKey[ki][3]
    cipher_bytes = bytes()
    plain_bytes = read_data(in_file)
    length = len(plain_bytes)
    step = block - 1
    for i in range(0, length, step):
        j = (i + step) if (i + step < length) else length
        m = int.from_bytes(plain_bytes[i:j], 'big')
        c = mont_pow(m, e, n)
        c = c.to_bytes(block, 'big')
        cipher_bytes += c
    write_data(out_file, cipher_bytes)
    return

# 解密, 按 block 字节读, 缩减为 block - 1 字节存
def decrypt(in_file, out_file, ki):
    d = LocalKey[ki][1]
    n = LocalKey[ki][2]
    block = LocalKey[ki][3]
    plain_bytes = bytes()
    cipher_bytes = read_data(in_file)
    length = len(cipher_bytes)
    step = block
    for i in range(0, length, step):
        j = (i + step) if  (i + step < length) else length
        c = int.from_bytes(cipher_bytes[i:j], 'big')
        m = mont_pow(c, d, n)
        m = m.to_bytes(block - 1, 'big')

        if (j == length - 1):
            k = 0
            for i in range(block):
                if m[i:i+1] == b'\x00':
                    k += 1
                else:
                    break
            m = m[k:j]

        plain_bytes += m
    write_data(out_file, plain_bytes)
    return

if __name__ == '__main__':
    ki = gen_key(12)

    begin = time.time()
    encrypt("1.txt", "enc.txt", ki)
    end = time.time()
    print("%.6f"%(end - begin))

    begin = time.time()
    decrypt("enc.txt", "dec.txt", ki)
    end = time.time()
    print("%.6f"%(end - begin))

