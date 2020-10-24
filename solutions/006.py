def sumsqdiff(n):
    return ((n*(n+1))/2)**2 - (n*(n+1)*((2*n)+1))/6

print(f'''The difference is {sumsqdiff(100)}.''')