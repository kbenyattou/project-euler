def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

# This function tests the divisibility of a number x by 1, ..., n.

def divtest(x,n):
    for i in range(1,n+1):
        if x%i != 0:
            return 0
    return 1

# This function tests even divisibility. Take n = 20. We consider i in 20Z
# (because we're looking for numbers divisible by 20 and 19, 18, ..., 2) where
# i <= 20! (upper bound) and test their even divisibility.

def evendivtest(n):
    for i in range(n,int(factorial(n)+1),n):
        if divtest(i,n) == 1:
            return i

print(f"The smallest number that is evenly divisible by 1 through {20} is {evendivtest(20)}.")