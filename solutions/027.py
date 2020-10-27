import math

def is_prime(n):
    if n < 0:
        return 0
    elif n in [0,1]:
        return 0
    elif n in [2,3]:
        return 1
    for i in range(2,int(math.ceil(math.sqrt(n)))+1):
        if n % i == 0:
            return 0
    else:
        return 1

def quadratic(a,b,n):
    return ((n**2) + (a*n) + b)

# We only want to consider |a| < 1000 and |b| <= 1000.

def conseq_prime_ctr(a,b):
    i = 0
    while is_prime(quadratic(a,b,i)):
        i += 1
    return i

list_of_conseqs = []
for a in range(-1000,1000):
    for b in range(-1001,1001):
        list_of_conseqs.append((a,b,conseq_prime_ctr(a,b)))

list_of_conseqs.sort(key = lambda x: x[2])

print(f'''(a, b, maximum number of primes) = {list_of_conseqs[-1]}''')