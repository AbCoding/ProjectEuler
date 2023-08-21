import math
import Euler3


def FindGCMEff(MaxVal):
    # PrimeArray
    ListOfPrimes = Euler3.FindPrimes(MaxVal)
    Num = 1
    # Initialises Power Array; Power = the Power the prime is multiplied by
    Power = []

    for b in ListOfPrimes:
        Power.append(1)
    i = 0

    # Calculates which Value Each Number in Power Has to have

    while i < len(ListOfPrimes):
        Power[i] = math.floor(math.log10(MaxVal) / math.log10(ListOfPrimes[i]))
        i += 1
    # Calculates the Final Number
    a = 0
    for j in ListOfPrimes:
        Num *= j ** Power[a]
        a += 1

    return Num
print(FindGCMEff(100))