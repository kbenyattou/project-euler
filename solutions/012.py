import math

def nth_triangular(n):
    tri = 0
    for i in range(1,n+1):
        tri += i
    return tri

# A function that counts the number of divisors of n.

def divisorctr(n):
    setofdivisors = {n}
    for i in range(1,int(math.ceil(math.sqrt(n)))):
        if n%i == 0:
            setofdivisors.add(i)
            setofdivisors.add(n/i)
    return len(setofdivisors)

# A function that tests successive triangular numbers for their number of
# divisors until the input (desired) number of divisors.

def at_least(y):
    i = 0
    n = nth_triangular(i)
    while divisorctr(n) < y:
        i += 1
        n = nth_triangular(i)
    return n

print(f'''The first triangular number with at least {500} divisors is {at_least(500)}.''')