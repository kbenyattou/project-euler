import math

def proper_divisor_sum(n):
    s = 1
    i = 2
    while i <= math.sqrt(n):
        if n%i == 0:
            if n/i == i or n/i == n:
                s += i
            else:
                s += (i + n/i)
        i += 1
    return int(s)

def abundant_list(n):
    abundants = []
    for i in range(1,n):
        if i < proper_divisor_sum(i):
            abundants.append(i)
    return abundants

def natural_sum(n):
    return int(n*(n+1)/2)

def combinations(n):
    abundants = abundant_list(n)
    combs = []
    for i in range(0,len(abundants)):
        for j in range(i,len(abundants)):
            abundantsum = abundants[i]+abundants[j]
            if abundantsum <= 28123:
                combs.append(abundantsum)
    return sum(set(combs))

print(f'''The sum of all numbers less than {28123} which cannot be expressed
as the sum of two abundant numbers is {natural_sum(28123)-combinations(28123)}.''')