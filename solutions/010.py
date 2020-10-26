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

def prime_sum(n):
    ps = 0
    for i in range(2,n):
        if prime_test(i) == 1:
            ps += i
    return ps

print(f'''The sum of all prime numbers below {2000000} is {prime_sum(2000000)}.''')