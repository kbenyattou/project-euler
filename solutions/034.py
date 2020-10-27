# An algorithm to check the condition is quite simple. The only issue here is
# to know when to stop checking. For a d-digit number n, we can bound it above
# by 10^{d}. Let's use F(n) to denote the sum of the factorials of the digits
# of n. At most, S(n) can be d x 9!. It's known that factorials grow faster
# than exponentials (with a fixed base). The equation d(9!) = 10^{d-1} has
# real solutions d in [7.4308, 2.75573 x 10^{-7}]. Thus we need only check
# for n < 10^{6.36} ~ 2230000.

def factorial(n):
    s = 1
    for i in range(1,n+1):
        s *= i
    return s

def fifth_power_sum(n):
    fifth_power_list = []
    for i in range(3,n+1):
        temp = 0
        for j in range(len(str(i))):
            temp += factorial(int(str(i)[j]))
        if i == temp:
            fifth_power_list.append(i)
    return sum(set(fifth_power_list))

print(f'''The sum of all curious numbers, excluding 1! = 1 and 2! = 2 which
are not sums, is {fifth_power_sum(2230000)}.''')