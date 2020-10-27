def fib(n):
    a = 1
    b = 0
    while n > 1:
        a,b = a+b,a
        n -= 1
    return a

def index_finder(l):
    i = 1
    while len(str(fib(i))) < l:
        i += 1
    return i

print(f'''The index of the first Fibonacci number to contain 1000 digits is {index_finder(1000)}.''')