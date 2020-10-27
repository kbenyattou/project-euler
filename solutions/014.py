pairs = dict()

def collatz(n):
    y = n
    if n%2 == 0:
        return n/2
    elif n%2 == 1:
        return (3*n) + 1

def sequence_length(n):
    chain = 1
    while n != 1:
        n = collatz(n)
        chain += 1
    return chain

z = 1000000

for i in range(1,z+1):
    pairs.update({i:sequence_length(i)})

# To sort the pairs by their key, we can use a lambda.

sortedpairs = sorted(pairs.items(), key=lambda item: item[1])

print(f'''The longest Collatz chain for a starting number less than {z} has
length {(sortedpairs[-1])[1]} and its starting number is {(sortedpairs[-1])[0]}.''')