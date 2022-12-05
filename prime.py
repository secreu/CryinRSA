# -*- coding: UTF-8 -*-

import random

# Miller-Rabin Algorithm
def miller_rabin(p):
	# p - 1 = (2 ^ k) * t
	t = p - 1
	k = 0
	while t % 2 == 0:
		t = t // 2
		k += 1

	# Test 6 times
	for _ in range(6):
		a = random.randrange(2, p - 1)
		temp1 = pow(a, t, p)
		if temp1 != 1:
			temp2 = temp1
			for i in range(k):
				temp2 = (temp1 ** 2) % p
				# Quadratic detection
				if temp2 == 1 and temp1 != 1 and temp1 != p - 1:
					return False
				temp1 = temp2
			# Final detection
			if temp2 != 1:
				return False
	return True

# Filter: initial detection
def is_prime(num):
    # exclude 0, 1 and negative number
    if num < 2:
        return False

    # if it is small prime, return true
    if num in SmallPrimes:
        return True

    # if it is a multiple of small prime, return true
    for prime in SmallPrimes:
        if num % prime == 0:
            return False

    # Further detection
    return miller_rabin(num)

# Generate a bitlen-bit(default) number and tt is tested for primality
def get_prime(bitlen):
    while True:
        num = random.randrange(2 ** (bitlen - 1), 2 ** bitlen)
        if is_prime(num):
            return num

# Some prime numbers less than 1000
SmallPrimes = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 
    101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 
    211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 
    307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 
    401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 
    503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 
    601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 
    701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 
    809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 
    907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997
]


# if __name__ == '__main__':
# 	# if miller_rabin(97):
# 	# 	print("yes")
# 	num = get_prime(256)
# 	print(num)

