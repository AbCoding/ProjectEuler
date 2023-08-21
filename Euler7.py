import math


def PrimeFinderErat(MaxLim):
    PrimeNums = [2]
    i = 3
    while i < MaxLim:
        PrimeNums.append(i)
        i += 2
    a = 0
    j = 0
    while j * j <= len(PrimeNums):
        a = 0

        while a < len(PrimeNums):
            if PrimeNums[a] % PrimeNums[j] == 0:
                if PrimeNums[a] != PrimeNums[j]:
                    del PrimeNums[a]
            a += 1
        j += 1
    return PrimeNums


