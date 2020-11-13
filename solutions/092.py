def sum_digits_square(x):
    result = 0
    for j in range(len(str(x))):
        result += int(str(x)[j])**2
    return result

# Since the largest possible value after one step in the chain is (9^2)*7
# = 567, we can store the first 567 values.

first_step = [0] + 567*[0]

for i in range(1,568):
    temp = i
    while not((temp == 89) or (temp == 1)):
        temp = sum_digits_square(temp)
        #print(temp)
        if temp == 89 or temp == 1:
            break
    if temp == 89:
        first_step[i] = 1

ctr = 0
for s in range(1,10000000):
    ctr += first_step[sum_digits_square(s)]

print(f'''There are {ctr} numbers below 10 million that arrive at 89.''')