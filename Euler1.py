import math


def AddArr(Array):
    Val = 0
    for i in Array:
        Val += i
    return Val


def FindMultiple(multiple, range):
    i = 0
    Temp = 0
    TempArr=[]
    while i < range:
        TempArr.append(i)
        Temp += i
        i += multiple

    return TempArr
r=1000

sum3 = FindMultiple(3, r)
sum5 = FindMultiple(5, r)
TotMult = list(set(sum5+sum3))


print(AddArr(TotMult))


# OR
