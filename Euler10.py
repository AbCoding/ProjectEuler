import math
import Euler7


def PrimeFinderEratMulti(MaxLim):
    PrimeNumBoolList = [True for i in range(MaxLim + 1)]
    p = 2
    PrimeList = []
    while p * p <= MaxLim:
        if PrimeNumBoolList[p]:
            for j in range(p * 2, MaxLim + 1, p):
                PrimeNumBoolList[j] = False
        p += 1
    PrimeNumBoolList[0] = False
    PrimeNumBoolList[1] = False

    for k in range(MaxLim + 1):
        if PrimeNumBoolList[k]:

            PrimeList.append(k)

    return PrimeList


print(PrimeFinderEratMulti(10000))

