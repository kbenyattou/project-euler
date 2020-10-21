def factorsum(upper_bound, numbers):
    '''Input type is (integer, list of integers)'''
    return sum(x for x in range(1,upper_bound) if any([x%number == 0 for number in numbers]))

print(factorsum(1000,[3,5]))