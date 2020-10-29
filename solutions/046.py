import math
import numpy

def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

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

def Goldbach_condition(composite, prime):
    check = math.sqrt((composite - prime)/2)
    if check % 1 == 0:
        return True
    return False

keep_going = True
i = 2
while keep_going:
    if (is_prime(i) or (i%2 == 0)) or (any((Goldbach_condition(i,j) for j in primesfrom2to(i-1)))):
        i += 1
    else:
        print(f'''{i} is the first odd composite number that disproves Goldbach.''')
        keep_going = False