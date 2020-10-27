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

# The rotation function takes the first constituent of a string and appends
# it to the end of a string. The first variable is the string and the second
# variable is the number of rotations.

def rotation(n):
    if len(str(n)) == 1:
        return n
    else: 
        return str(n)[1:len(n)] + str(n)[0]

def repeat_rotation(n,r):
    if r == 0:
        return n
    else:
        for _ in range(r):
            n = rotation(n)
        return n

# Here we use a list comprehension to list all of the conditions we want
# to impose on the if statement.

def circular_prime_list(n):
    circular_primes = []
    for i in range(1,n+1):
        rules = [prime_test(int(repeat_rotation(str(i),j))) == 1 for
                j in range(len(str(i)))]
        if all(rules):
            circular_primes.append(i)
    return circular_primes

print(f'''\nThe number of circular primes less than 1000000 is {len(circular_prime_list(1000000))}.''')