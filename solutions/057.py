from fractions import Fraction

# Brute force solution. Could've solved the recurrence relation for
# the numerator and denominator.

def continued_fraction(n):
    if n == 1:
        return 1
    else:
        f = 1
        while n > 1:
            f = 1 + Fraction(1,1+f)
            n -= 1
        return f

num_longer_than_denom = 0
for i in range(2,1002):
    if len(str(continued_fraction(i).numerator)) > len(str(continued_fraction(i).denominator)):
        num_longer_than_denom += 1
    else:
        continue

print(num_longer_than_denom)