import math


def AddDigits(Num):
    s=0
    for i in str(Num):
        s+= int(i)
    return s

print(AddDigits(2**1000))