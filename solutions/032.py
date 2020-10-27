def pandigital_check(n):
    rules = [n.count(str(i)) == 1 for i in range(1,10)]
    if all(rules) and n.count(str(0)) == 0:
        return 1
    else:
        return 0

pandigital_list = set()
pandigital_triples = []

for i in range(1,1000):
    for j in range(1,10000):
        k = i*j
        converted_str = str(i)+str(j)+str(k)
        if len(converted_str) > 9:
            pass
        else:
            if pandigital_check(converted_str) == 1:
                pandigital_list.add(k)
                pandigital_triples.append([i,j,k])

print('''The list of all such identities is:\n''')
for tup in pandigital_triples:
    print('''{} x {} = {}'''.format(tup[0],tup[1],tup[2]))

print(f'''\nThe sum of all such products is {sum(pandigital_list)}.''')