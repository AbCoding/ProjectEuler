import math
import Euler10

def TriangleNumList(Limit):
    TriangleArr = []
    j = 0
    for i in range(Limit):
        j += i
        TriangleArr.append(j)

    del TriangleArr[0]
    return TriangleArr


def Factors(Number):
    ListOfFactors = []
    j = 1
    while j < ((Number) + 1):
        if Number % j == 0:

            ListOfFactors.append(j)
            j += 1
        else:
            j += 1

    return len(ListOfFactors)


def TriFindMostFac(NumberofFactors):
    FacArr = []
    val = 0
    j = 0
    MaxFac = 0
    i = 1
    while MaxFac < NumberofFactors:


        if (Factors(j)*2) > MaxFac:

            MaxFac = (Factors(j)*2)
            val = j
        i += 1
    return val


