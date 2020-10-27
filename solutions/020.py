def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def sum_of_constituent_digits(n):
    s = 0
    for i in range(0,int(len(str(n)))):
        s += int(str(n)[i])
    return s

print(f'''The sum of the digits in {100}! is {sum_of_constituent_digits(factorial(100))}.''')