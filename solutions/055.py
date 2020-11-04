def reverse_and_add(x):
    return x + int(str(x)[::-1])

def palindrome_check(y):
    if str(y) == (str(y))[::-1]:
        return True
    return False

not_lychrel = 0
for i in range(1,10000):
    n = 1
    while n < 50:
        i = reverse_and_add(i)
        if palindrome_check(i):
            not_lychrel += 1
            break
        else:
            pass
        n += 1

print(f'''There are {9999-not_lychrel} Lychrel numbers less than 10000.''')