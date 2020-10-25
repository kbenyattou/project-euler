import math

def prime_test(p):
    if p == 1:
        return 0
    elif p in [2,3]:
        return 1
    for i in range(2,int(math.ceil(math.sqrt(p)))+1):
        if p%i == 0:
            return 0
    else:
        return 1

def kth_prime(k):
    primes = []
    i = 2
    while len(primes) <= k-1:
        if prime_test(i) == 1:
            primes.append(i)
        i += 1
    return primes[-1]

print(f'''Prime number {10001} is {kth_prime(10001)}.''')