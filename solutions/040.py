def fractional_part(length):
    s = ''
    i = 1
    while len(s) <= length:
        s += str(i)
        i += 1
    return s

def product_expression(n):
    product = 1
    for i in range(0,7):
        print(-1+(10**i),n[-1+(10**i)])
        product = product*int(n[-1+(10**i)])
    return product

print(product_expression(fractional_part(1000000)))