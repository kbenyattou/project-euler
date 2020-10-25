import math

def pythag(n):
    triples = []
    for i in range(1,n):
        for j in range(1,n):
            k = math.sqrt(i**2 + j**2)
            if k%1 == 0 and i+j+k == n:
                triples.append(sorted([i,j,int(k)]))
    return map(list,(set(map(tuple,triples))))

def prod(x):
    prod = 1
    for i in range(0,len(x)):
        prod *= x[i]
    return prod

print(f'''The pythagorean triples (adding up to {1000}) and their products are:
Triple \t\t\t Product''')

for triple in pythag(1000):
    print(f'''{triple} \t {prod(triple)}''')