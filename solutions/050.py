# The prime 41, can be written as the sum of six consecutive primes:
# 
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below
# one-hundred.
# 
# The longest sum of consecutive primes below one-thousand that adds to a
# prime, contains 21 terms, and is equal to 953.
# 
# Which prime, below one-million, can be written as the sum of the most
# consecutive primes?

import numpy
import os

os.system('clear')

def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

upper_bound = 1000000
primes = primesfrom2to(upper_bound)

highest_prime = 0
consecutive = 0
for i in range(len(primes)):
    sum = primes[i]
    consec = 1
    for j in range(i+1,len(primes)):
        sum += primes[j]
        consec += 1
        if sum >= upper_bound:
            break
        if (sum in primes) and consec > consecutive:
            highest_prime = sum
            consecutive = consec

print(f'''{consecutive} is the length of the longest sum of consecutive primes
below {upper_bound} that sums up to a prime (namely {highest_prime}) below {upper_bound}.''')