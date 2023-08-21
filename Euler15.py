import math


def LatticePath(PointArr):

    numerator = 0
    denominater=1
    for i in range(len(PointArr)):
        numerator += PointArr[i]
        denominater *= math.factorial(PointArr[i])

    return math.factorial(numerator)/denominater


