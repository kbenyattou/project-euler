def sieve_of_eratosthenes(n):
    n = n+1
    A = [True]*n
    A[0] = False
    A[1] = False

    i = 2
    while i*i <= n:
        if A[i] == False:
            i += 1
            continue

        j = 2*i
        while j < n:
            A[j] = False
            j += i
        
        i += 1

    primes = []
    for i in range(1,n):
        if A[i] == True:
            primes.append(i)
    return primes