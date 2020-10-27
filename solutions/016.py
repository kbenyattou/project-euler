def sum_of_constituents(n):
    output = 0
    for i in range(0,len(str(n))):
        output += int(str(n)[i])
    return output

print(f'''The sum of the constituent digits of 2^1000 is {sum_of_constituents(2**1000)}.''')