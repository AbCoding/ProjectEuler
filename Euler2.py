import math


def FibbSeq(numberOfValues):
    Sum2 = 0
    Fib = [0, 1, ]
    i = 2
    while i < (numberOfValues + 2):
        Fib.append(Fib[i - 2] + Fib[i - 1])
        i += 1
    i=0
    while i < (numberOfValues + 2) and Fib[i]<4000000:

        Sum2 += Fib[i]
        i += 3
    return Sum2


print(FibbSeq(100))
