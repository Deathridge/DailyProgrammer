from math import sqrt

def primeSieve(largestPrime):
    possiblePrimeList = list(range(largestPrime+1))
    isPrimeList = [True for x in range(largestPrime+1)]    

    for i in range(2, int(sqrt(largestPrime))):
        if isPrimeList[i]:
            for j in range(i**2, largestPrime, i):
                isPrimeList[j] = False
    isPrime = []
    for x in range(len(isPrimeList)):
        if isPrimeList[x]:
            isPrime.append(possiblePrimeList[x])

    return isPrime
