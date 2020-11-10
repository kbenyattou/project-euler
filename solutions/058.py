import math

def is_prime(n):
    if n < 2:
        return 0
    elif n == 2:
        return 1
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i == 0:
                return False
    return True

total_diagonals = 0
prime_diagonals = 0
percentage = 100

start = 1
step = 0

while percentage >= 10:
    step += 2
    for i in range(1,5):
        start += step
        #print(start)
        total_diagonals += 1
        if is_prime(start):
            prime_diagonals += 1
        percentage = 100*prime_diagonals/total_diagonals
    #print(percentage)
        
print(f'''The side length of the square spiral for which the ratio of primes
along both diagonals first falls below 10% is {step-2+1}.''')