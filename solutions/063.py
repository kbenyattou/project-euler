# We're looking for numbers that satisfy the inequality 10^(n-1) <= a^n < 10^n
# The second equality tells us that a < 10. For the first, since a can only
# take the values 1,2,...,9, we see that 10^(n-1) eventually exceeds a^n.

# The point at which they meet is when 10^(n-1) = a^n so
# n = log(10)/(log(10)-log(a)).

# a = 1    n = 1 
# a = 2    n = 1.43..   -> 1
# a = 3    n = 1.912..  -> 1
# a = 4    n = 2.5129.. -> 2
# a = 5    n = 3.3219.. -> 3
# a = 6    n = 4.507..  -> 4
# a = 7    n = 6.455..  -> 6
# a = 8    n = 10.318.. -> 10
# a = 9    n = 21.85..  -> 21

# We round down to find the largest integer n that satisfies the inequalities
# given the values of a.

ctr = 0
for a in range(1,10):
    for n in range(1,22):
        if len(str(a**n)) == n:
            ctr += 1

print(f'''There are {ctr} numbers that are nth powers with n digits.''')