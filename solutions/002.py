# Given an integer n, fibb() returns the nth Fibonacci number.

def fibb(n):
    a = 0
    b = 1
    while n > 0:
        (a,b) = (a+b, a)
        n -= 1
    return a

def even_fibonacci_sum(z):
    x = 0
    sum = 0
    while fibb(x) < z:
        x += 1
        if fibb(x)%2 == 0:
            sum += fibb(x)
        else:
            continue
    return sum

print(f'''The sum of the even-valued Fibonnaci sequence elements that don't
exceed 4 million is {even_fibonacci_sum(4000000)}.''')