def is_pandigital(n):
    for i in str(n):
        if int(i) > len(str(n)):
            return False
    rules = [n.count(str(i)) == 1 for i in range(1,len(str(n)))]
    if all(rules) and n.count(str(0)) == 0:
        return True
    else:
        return False
