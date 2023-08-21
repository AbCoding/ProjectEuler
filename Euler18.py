import math

Paths = [75, 95, 64, 17, 47, 82, 18, 35, 87, 10, 20, 4, 82, 47, 65, 19, 1, 23, 75, 3, 34, 88, 2, 77, 73, 7, 63, 67, 99,
         65, 4, 28, 6, 16, 70, 92, 41, 41, 26, 56, 83, 40, 80, 70, 33, 41, 48, 72, 33, 47, 32, 37, 16, 94, 29, 53, 71,
         44, 65, 25, 43, 91, 52, 97, 51, 14, 70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57, 91, 71, 52, 38, 17, 14, 91,
         43, 58, 50, 27, 29, 48, 63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31, 4, 62, 98, 27, 23, 9, 70, 98,
         73, 93, 38, 53, 60, 4, 23]


def ArrToTri(max, Arr):
    i = 0
    s = 0
    NewArr = []
    while i <= max:

        tempArr = []
        tempi = s
        for j in range(i + 1):
            tempArr.append(Arr[tempi + j])
        NewArr.append(tempArr)
        i += 1
        s += i
    return NewArr


N = ArrToTri(14, Paths)



def NextSum(arr, val, pos):
    NL = arr[pos]
    NR = arr[pos + 1]
    return max(NL, NR) + val


def FindMaxPath(Num_Triangle):
    r=CombineRows(Num_Triangle[-2],Num_Triangle[-1])
    Num_Triangle.pop()
    Num_Triangle.pop()
    Num_Triangle.append(r)
    return Num_Triangle


def CombineRows(Top, Bottom):
    NewRow=[]
    for i,e in enumerate(Top):
        s = NextSum(Bottom, e, i)
        NewRow.append(s)
    return(NewRow)
t=N
while len(t)>1:
    t=FindMaxPath(t)
print(t)

# for i in range(len(N[-2])):
#     e = N[-2][i]
#
#     s = NextSum(e, len(N) - 2, i)
#     print(s)

# def AdjStep(Level, Array, CurrentHighestIndex):
#     try:
#         adj = [Array[Level + 1][CurrentHighestIndex], Array[Level + 1][CurrentHighestIndex + 1]]
#     except:
#         adj = [Array[Level + 1][CurrentHighestIndex]]
#     return adj

# for i in range(2):
#     ListAdj = [AdjStep(0, N, 0)]
#     x=0
#     for j in ListAdj[0]:
#         ListAdj += [AdjStep(0 + i, N, 0 + j)]
