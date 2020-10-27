import itertools

def list_to_string(x):
    outputstring = ''
    for elem in x:
        outputstring += elem
    return outputstring

print(f'''The millionth lexicographic permutation of [0,1,...,9] is
{list_to_string(list(itertools.permutations('0123456789',10))[1000000-1])}''')