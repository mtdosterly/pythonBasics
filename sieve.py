def prime_sieve(limit):
    primes = [num for num in range(2,limit + 1)] #list of numbers to work on
    for test in primes[0:]:  #testing each number still in the list
        for x in range(2,int((limit+1)/test)): #iterating through a multiplier
            if (test * x) in primes: # if multiple of confirmed prime in list
                primes.remove(test * x)  #delete it
    return primes

limit = int(input("Enter the upper limit for determining primes: "))
primeList = prime_sieve(limit)
f = open(f"primelist_{limit}.txt", "w")
f.write(str(primeList))
f.close()
