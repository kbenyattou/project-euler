import math

def sum_of_proper_divisors(n):
    s = 1
    for i in range(2,int(math.ceil(math.sqrt(n)))):
        if n%i == 0:
            s += i
            s += n/i
    return int(s)

def amicable_sum(n):
    amicable_set = set()
    for i in range(1,n+1):
        j = sum_of_proper_divisors(i)
        if (sum_of_proper_divisors(j) == i) and (i != j):
            amicable_set.add(i)
            amicable_set.add(j)
    return int(sum(amicable_set))

print(f'''The sum of all amicable numbers below {10000} is {amicable_sum(10000)}.''')