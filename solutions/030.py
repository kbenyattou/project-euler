# An algorithm to check the condition is quite simple. The only issue here is
# to know when to stop checking.

# For a d-digit number $n$, we can bound it below by 10^{d-1} e.g. 112 is
# bounded below by 100. Let's use S(n) to denote the sum of the fifth powers
# of the digits of n. At most, S(n) can be d x 9^5. It's clear that
# 10^{d-1} grows much faster than S(n) so there exists an n_0 after which
# 10^{d-1} exceeds S(n). To find the crossing point, we can solve
# S(n) = 10^{d-1} for d.

# The real solutions (via Wolfram) are d = 1.69352 x 10^{-6} and
# d = 6.5901. This means that for d <= 7 i.e. n > 10^6, we have
# that S(n) != n. Thus, we can choose our upper bound to be 10^6.

def fifth_power_sum(n):
    fifth_power_list = []
    for i in range(2,n+1):
        temp = 0
        for j in range(len(str(i))):
            temp += int(str(i)[j])**5
        if i == temp:
            fifth_power_list.append(i)
    return sum(set(fifth_power_list))

print(fifth_power_sum(1000000))