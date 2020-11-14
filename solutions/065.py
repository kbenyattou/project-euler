import fractions

def sum_of_digits(s):
    s = str(s)
    temp = 0
    for i in range(len(s)):
        temp += int(s[i])
    return temp

def nth_convergent(x,n):
    n = n-1
    convergent = 2
    j = n-1
    f = 0
    while j >= 0:
        f = fractions.Fraction(1,x[j]+f)
        j -= 1
        convergent = 2 + f
    return convergent

y = []
for i in range(1,51):
    y.append(1)
    y.append(2*i)
    y.append(1)

for i in range(1,11):
    print(nth_convergent(y,i))

print(f'''The sum of digits in the numerator of the 100th convergent of the
continued fraction for e is {sum_of_digits(nth_convergent(y,100).numerator)}.''')