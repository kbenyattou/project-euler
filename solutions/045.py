import math

def t(n):
    return (1/2)*n*(n+1)

def is_pentagonal(n):
    if ((1/6)*(1+math.sqrt((24*n)+1))) % 1 == 0:
        return True
    return False

def is_hexagonal(n):
    if ((1/4)*(1+math.sqrt(1+(8*n)))) % 1 == 0:
        return True
    return False

i = 286
while not(is_pentagonal(t(i)) and is_hexagonal(t(i))):
    i += 1

print(i, t(i))