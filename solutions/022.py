def letter_score(n):
    return ord(str(n))-64

def name_score(n):
    score = 0
    for i in range(len(n)):
        score += letter_score(n[i])
    return score

def total_score(x):
    total_score = 0
    for name in x:
        total_score += ((x.index(name)+1)*(name_score(name)))
    return total_score

# Now we import the text file of names to use and organise them into a list
# that's in alphabetical order.

f = open('022.txt')
sorted_namelist = (f.read()).replace('"','').split(',')
sorted_namelist.sort()

print(f'''The total of all name scores in the file euler22names.txt is {total_score(sorted_namelist)}.''')