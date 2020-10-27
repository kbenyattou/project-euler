def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False

sum_of_palindromes = 0

for i in range(0,1000000):
    if is_palindrome(i) and is_palindrome(str(bin(i))[2:]):
        sum_of_palindromes += i
    else:
        pass

print(f'''The sum of all numbers, less than one million, that are palindromic
in both base 2 and 10 is {sum_of_palindromes}.''')