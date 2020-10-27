def pandigital_check(n):
    rules = [n.count(str(i)) == 1 for i in range(1,10)]
    if all(rules) and n.count(str(0)) == 0:
        return True
    else:
        return False

# 10000 because n > 1 (i.e. n >= 2) and 9999 is the largest number by which
# one can multiply by 2 and still have a 9 digit concatenated product.

# The 10 is chosen for j's upper bound as 10-1 = 9 the largest n for which a
# 1-digit number may be multiplied 1 through n to get a 9 digit concatenated
# product.

pandigitals = []
for i in range(1,10000):
    x = ''
    for j in range(1,10):
        y = i*j
        x += str(y)
        if len(x) == 9 and pandigital_check(x) == True:
            pandigitals.append(int(x))
        else:
            pass

pandigitals.sort(reverse = True)
print(f'''The largest concatenated product of an integer with [1,...n] is
{pandigitals[0]}.''')