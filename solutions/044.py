# I'm unhappy with this "solution" and I will come back to it

import math

def P(n):
    return n*((3*n)-1)/2

# The inverse of f(n) = n(3n-1)/2 is g(n) = (1 + sqrt(24n +1))/6

def pentagonal_check(n):
    if (1/6)*(1 + math.sqrt((24*n) + 1)) % 1 == 0:
        return True
    return False

def minimal_D():
    j = 1
    k = 1
    status = True
    while status:
    
        for k in range(1,j+1):
            D = abs(P(j) - P(k))
            S = (P(j) + P(k))
            #print(k,j,x,y, pentagonal_check(x),pentagonal_check(y))
            if (pentagonal_check(D) == True) and (pentagonal_check(S) == True):
                combi = '''P({}) = {}\nP({}) = {}\nD = |P({}) - P({})| = {}'''.format(j,P(j),k,P(k),j,k,D)
                status = False
            else:
                pass
        j += 1
    return combi

print(minimal_D())