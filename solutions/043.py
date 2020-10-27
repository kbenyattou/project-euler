import itertools

def tuple_to_int_list(L):
    new_list = []
    for elem in L:
        elem = ''.join(elem)
        if elem[0] == '0':
            continue
        else:
            new_list.append(elem)
    return new_list

def list_sum(L):
    s = 0
    for elem in L:
        s += elem
    return s

def divtest(x):
    primes = [2,3,5,7,11,13,17]
    for i in range(7):
        if int(x[i+1:i+4]) % primes[i] != 0:
            return False
    return True

pandigitals = []
pandigitals.extend(list(itertools.permutations('0123456789',10)))
pandigitals = tuple_to_int_list(pandigitals)

special_pandigitals = []
for pandigital in pandigitals:
    if divtest(pandigital):
        special_pandigitals.append(int(pandigital))
    else:
        pass

print(list_sum(special_pandigitals))