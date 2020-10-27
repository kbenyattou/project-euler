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

primes = primesfrom2to(1000000)

# Truncatable from either side means the number can't begin or end in 2, 4, 6
# or 8.

def truncatable_left(n):
    while len(str(n)) > 0:
        if all((int((str(n))[i:]) in primes for i in range(0, len(str(n))))):
            return True
        else:
            return False

def truncatable_right(n):
    while len(str(n)) > 0:
        if all((int((str(n))[:i]) in primes for i in range(1, len(str(n))+1))):
            return True
        else:
            return False

def sum_of_trunc_primes(x):
    list_of_truncs = []
    while len(list_of_truncs) < 15:
        for prime in x:
            #if any((int(str(prime)[i]) in [2,4,6,8,9] for i in [0,-1])):
            #    pass
            if truncatable_left(prime) and truncatable_right(prime):
                list_of_truncs.append(prime)
            else:
                continue
    return sum(list_of_truncs) - (2+3+5+7)

print(sum_of_trunc_primes(primes))