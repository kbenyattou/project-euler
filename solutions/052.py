# It can be seen that the number, 125874, and its double, 251748, contain
# exactly the same digits, but in a different order.
# 
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
# contain the same digits.

def same_digits(number_one,number_two):
    if len(str(number_one)) == len(str(number_two)) and all((str(number_one).count(str(i)) == str(number_two).count(str(i)) for i in range(1,10))):
        return True
    else:
        return False

keep_going = True
start = 0
while keep_going:
    start += 1
    if all(same_digits(start,j*start) for j in range(2,7)):
        keep_going = False
        print(start)
    else:
        continue