z = int(input('''We'll find the largest palindrome made from the product of two
n-digit numbers. Choose your n: '''))

# The list of products of two nxn digit numbers will be sifted through to
# find the largest palindrome.

products = []
for i in range(10**(z-1),10**z):
    for j in range(i,10**z):
        products.append(i*j)

palindromes = []
for product in products:
    if str(product) == str(product)[::-1]:
        palindromes.append(product)

print(f'''\nThe largest such palindrome is {sorted(palindromes)[-1]}.''')