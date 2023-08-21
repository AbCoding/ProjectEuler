import math
from ProjectEulerUsefulFunctions import *


def ConvertFileToArray(name):
    file = open(name)
    lines = file.readlines()
    newarr = []
    for i in lines:
        line = []
        num = ""
        for j in i:
            if j.isspace():
                line.append(int(num))
                num = ""
            else:
                num += j
        newarr.append(line)

    return newarr


v = ConvertFileToArray("p067_triangle.txt")
print(FindMaxPath(v))
