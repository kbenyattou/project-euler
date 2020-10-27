import math

def remove_duplicates(x):
    sifted = []
    for elt in x:
        if elt not in sifted:
            sifted.append(elt)
    return sifted

def pythagorean_triples(n):
    list_of_triples = []
    for i in range(1,int(n/2) + 1):
        for j in range(1,int(n/2) + 1):
            k = math.sqrt(i**2 + j**2)
            if k%1 == 0 and i+j+k == n:
                list_of_triples.append(sorted([i,j,int(k)]))
    return remove_duplicates(list_of_triples)

def takeSecond(elem):
    return elem[1]

def number_of_triples(p):
    perimeter_tuples = []
    for i in range(1,p+1):
        perimeter_tuples.append([i,len(pythagorean_triples(i))])
    perimeter_tuples.sort(key=lambda x: x[1])
    return perimeter_tuples

print(f'''The desired [perimeter, solution] pair that maximises the number of
solutions is {number_of_triples(1000)[-1]}.''')