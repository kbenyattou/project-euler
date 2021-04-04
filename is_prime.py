import math

def is_prime(n):
    if n in [0,1]:
        return False
    elif n == 2:
        return True
    for i in range(2,int(math.ceil(math.sqrt(n)))+1):
        if n % i == 0:
            return False
    else:
        return True