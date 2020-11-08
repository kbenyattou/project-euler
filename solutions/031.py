blocks = [1, 2, 5, 10, 20, 50, 100, 200]
total = 200

combinations = [1] + ([0]*total)

def combination_finder(x,y):
    for i in range(len(y)):
        for j in range(len(x)):
            if j >= blocks[i]:
                x[j] += x[j-y[i]]
    return x[-1]

print(combination_finder(combinations,blocks))