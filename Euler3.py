import math


def FindPrimes(MaxVal):
    ListOfPrimes = []
    num = 4
    i = 2
    while i < MaxVal:

        if CheckPrime(i):

            ListOfPrimes.append(i)
            i += 1
        else:

            i += 1
    return ListOfPrimes


def CheckPrime(number):
    PrimeNess = True
    j = 2
    while j < number and PrimeNess is True:

        if number % j == 0:
            PrimeNess = False

        j += 1
    return PrimeNess


def PrimeFactors(Number):
    ListOfFactors = []
    j = 3
    while j < math.sqrt(Number):
        if Number % j == 0:
            if CheckPrime(j):
                ListOfFactors.append(j)
            j += 2
        else:
            j += 2

    return ListOfFactors



