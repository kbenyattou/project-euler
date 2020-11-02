def digital_sum(n):
    digi = 0
    for i in range(len(str(n))):
        digi += int(str(n)[i])
    return digi

highest_digi = 0
for a in range(100):
    for b in range(100):
        if digital_sum(a**b) > highest_digi:
            highest_digi = digital_sum(a**b)

print(f'''The maximum digital sum of numbers of the form a^b, where a,b < 100,
is {highest_digi}.''')