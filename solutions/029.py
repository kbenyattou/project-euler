def list_of_distincts(a,b):
    powers = []
    for i in range(2,a+1):
        for j in range(2,b+1):
            powers.append(i**j)
    return len(set(powers))

print(f'''There are {list_of_distincts(100,100)} distinct terms generated by the sequence
a^b for integers 1 < a,b < 101.''')