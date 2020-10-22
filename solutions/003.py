import math

def primefactors(n):
    primefactorlist = set()
    i = 1
    while i < math.ceil(math.sqrt(n))+1:
        j = 0
        if n%i == 0:
            k = 1
            while k <= i:
                if i%k == 0:
                    j += 1
                k += 1
            if j == 2:
                primefactorlist.add(i)
        i += 1
    return primefactorlist

print(f'''The largest prime factor of 600851475143 is {sorted(primefactors(600851475143))[-1]}.''')