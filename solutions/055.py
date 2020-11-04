def reverse_and_add(x):
    return x + int(str(x)[::-1])

def palindrome_check(y):
    if str(y) == (str(y))[::-1]:
        return True
    return False

total_lychrels = 0
for i in range(1,10000):
    print(f'''\t {i}''')
    n = 1
    while n < 50:
        i = reverse_and_add(i)
        print(i)
        if palindrome_check(i):
            total_lychrels += 1
            break
        else:
            pass
        n += 1

print(f'''There are {9999-total_lychrels} Lychrel numbers less than 10000.''')