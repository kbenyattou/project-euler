import math
import itertools

# A number is divisible by 3 if the sum of its consitutent digits are
# divisible by 3. Since (1 + ... + 8) and (1 + ... + 9) are divisible by
# 3, there aren't any 8 and 9 digit pandigital primes. This reduces our search
# to at most 7 digit pandigital primes.

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

def tuple_to_int_list(L):
    new_list = []
    for elem in L:
        new_list.append(int(''.join(elem)))
    return new_list

pandigitals = []
pandigital_primes = []

digits = ''
for i in range(1,8):
    digits += str(i)
    pandigitals.extend(list(itertools.permutations(digits,i)))

# Since list(itertools.permutations) creates a list of tuples of the form
# [('1','2','4','3')], we use tuple_to_int_list() to convert the list to one of
# integers e.g. [1243]:

pandigitals = tuple_to_int_list(pandigitals)

# Sifting the list of pandigitals to leave only primes

for pandigital in pandigitals:
    if is_prime(pandigital):
        pandigital_primes.append(pandigital)

pandigital_primes.sort()
print(pandigital_primes[-1])