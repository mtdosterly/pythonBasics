def find_primes(num):
    primes = []
    for val in range(3,num):
        for div in range(2,val-1):
            if val % div == 0:
                break
        else:
            primes.append(val)
    return primes

limit = int(input("Enter the upper limit for determining primes: "))
primeList = find_primes(limit)
print(primeList)
