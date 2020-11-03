def factorial(n):
    prod = 1
    while n > 0:
        prod *= n
        n -= 1
    return prod

def binom(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))

binom_exceed_million = 0
for n in range(1,101):
    for r in range(1,101):
        if binom(n,r) > 1000000:
            binom_exceed_million += 1

print(binom_exceed_million)