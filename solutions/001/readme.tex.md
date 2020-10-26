# 1. Multiples of 3 and 5

## Problem

If we list all the natural numbers below $10$ that are multiples of 3 or 5, we
get $3$, $5$, $6$ and $9$. The sum of these multiples is $23$. Find the sum of all the multiples of $3$ or $5$ below $1000$.

## Solution

```py
def factorsum(upper_bound, numbers):
    '''Input type is (integer, list of integers)'''
    return sum(x for x in range(1,upper_bound) if any([x%number == 0 for number in numbers]))

print(factorsum(1000,[3,5]))
```
