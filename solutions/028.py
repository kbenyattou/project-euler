# I created the circle(,) function to return the sum of four numbers,
# starting with a square number on the top right diagonal and adding the three
# corner numbers around it.

# e.g. if we start with 1 = 1^2, it returns the sum of 1, 3, 5 and 7.
# e.g. if we start with 9 = 3^2, it returns the sum of 9, 13, 17 and 21.

def circle(n,s):
    return 4*n + 6*s

# spiral_sum() finds the sum of the diagonals in an nxn grid.

def spiral_sum(n):
    m = int((n-1)/2)
    total = (n**2)
    for i in range(0,m):
        total += circle(((2*i)+1)**2,(2*i)+1+1)
    return total

x = 1001

print(f'''\nThe sum of the diagonal numbers on a {x}x{x} grid is {spiral_sum(x)}.''')