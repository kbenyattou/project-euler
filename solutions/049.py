        # The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
        # increases by 3330, is unusual in two ways: (i) each of the three terms
        # are prime, and, (ii) each of the 4-digit numbers are permutations of one
        # another.

        # There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
        # primes, exhibiting this property, but there is one other 4-digit increasing
        # sequence.

        # What 12-digit number do you form by concatenating the three terms in this
        # sequence?

import math
import itertools

        # Summary
        # 1. Generate all 4-digit primes.
        # 2. Generate a list of (prime, [permutations]).
        # 3. Sift the [permutations] to only include primes.
        # 4. Search for an arithmetic sequence by checking to see if the same difference
        #    between one term and the rest in [prime permutations] shows up.
        # 5. Remove duplicates in (arithmetic difference, [permutations])
        # 6. Inspect manually -_- to find the arithmetic sequence.

        # I'm confident there's a better way to do all this.

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

# List of 4-digit primes
four_primes = []
for i in range(1000, 10000):
    if is_prime(i):
        four_primes.append(i)

def permutation_of(given_string):
    return [''.join(i) for i in itertools.permutations(given_string)]

def string_to_int_list(x):
    new_list = []
    for i in range(len(x)):
        if int(x[i]) > 1000:
            new_list.append(int(x[i]))
        else:
            continue
    return new_list

testlist = list(set(string_to_int_list(permutation_of(str(four_primes[0])))))
def sift(x):
    y = []
    for i in range(len(x)):
        if x[i] in four_primes:
            y.append(x[i])
        else:
            continue
    return sorted(y)

def difference(i,x):
    diff_list = []
    for j in range(len(x)):
        diff_list.append(abs(x[j]-x[i]))
    return diff_list

def arithmetic_search(x):
    for i in range(1,len(x)):
        if x[i] == 0:
            continue
        elif (2*x[i] in x) or (x.count(x[i]) >= 3):
            #print(x[i])
            return x[i],True
    return 0, False

prime_perm_pairs = []
for prime in four_primes:
    sifted_list = sift(list(set(string_to_int_list(permutation_of(str(prime))))))
    for i in range(len(sifted_list)):
        diff_list = difference(i,sifted_list)
        if (len(sifted_list) >= 3) and arithmetic_search(diff_list)[1]:
            prime_perm_pairs.append((arithmetic_search(diff_list)[0], sifted_list))
        else:
            continue

prime_perm_pairs_no_dups = []
for pair in prime_perm_pairs:
    if pair not in prime_perm_pairs_no_dups:
        prime_perm_pairs_no_dups.append(pair)
    else:
        continue

for pair in prime_perm_pairs_no_dups:
    print(pair)