def find_primes(num):
    primes = [2]
    for val in range(3,num,2):
        for div in range(2,int(val**.5)+1):
            if val % div == 0:
                break
        else:
            primes.append(val)
    return primes

limit = int(input("Enter the upper limit for determining primes: "))
choice = input("Do you want me to display the numbers or save them to a file? Enter 'file' or 'display': ")
primeList = find_primes(limit)
if choice == 'file':
    f = open(f"primelist_{limit}", "w")
    f.write(str(primeList))
    f.close()
else:
    print(primeList)
