import math


def FindTrip(AddVal):
    a = 0
    b = 0
    c = 0
    n = 0
    m = 0

    while m < AddVal:
        n=0
        while n < m:
            if 2 * (m ** 2) + 2 * m * n == AddVal:
                a = (m ** 2 - n ** 2)
                b = 2 * m * n
                c = m ** 2 + n ** 2
                return a, b, c
            n += 1
        m += 1


ABC = FindTrip(1000)
print(ABC)
print(ABC[0]*ABC[1]*ABC[2])