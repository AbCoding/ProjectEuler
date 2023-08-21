import math


def DifSqr(m):
    su = (m*(m + 1) / 2)
    sq = (2*m + 1)*(m + 1)*m/ 6

    return int(su**2-sq)


def InDifSqr(m):
    i = 0
    sqr = 0
    addsqr = 0
    while i <= m:
        addsqr += (i ** 2)
        sqr += i
        i += 1
    sqr = sqr ** 2

    return sqr - addsqr


r=100000009090909090909000
print(DifSqr(r))



