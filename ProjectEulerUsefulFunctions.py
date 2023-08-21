import math


# Euler1
def AddArr(Array):
    Val = 0
    for i in Array:
        Val += i
    return Val


# 2
def FibbSeq(numberOfValues):
    Fib = [0, 1, ]
    i = 2
    while i < (numberOfValues + 2):
        Fib.append(Fib[i - 2] + Fib[i - 1])
        i += 1
    return Fib


# 3
def CheckPrime(number):
    PrimeNess = True
    j = 2
    while j < number and PrimeNess is True:

        if number % j == 0:
            PrimeNess = False

        j += 1
    return PrimeNess


def PrimeFactors(Number):
    ListOfFactors = []
    j = 3
    while j < math.sqrt(Number):
        if Number % j == 0:
            if CheckPrime(j):
                ListOfFactors.append(j)
            j += 2
        else:
            j += 2

    return ListOfFactors


# 4
def SplitList(List):
    half = len(List) // 2
    return List[:half], List[half:]


def PalindromeCheck(num):
    NumArr = []
    for x in str(num):
        NumArr.append(int(x))

    FirstHalf = SplitList(NumArr)[0]
    SecondHalf = SplitList(NumArr)[1]
    SecondHalf.reverse()

    if SecondHalf == FirstHalf:
        return True
    else:
        return False


# 5
def FindGCMEff(MaxVal):
    # PrimeArray
    ListOfPrimes = PrimeFinderEratMulti(MaxVal)
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


# 10
def PrimeFinderEratMulti(MaxLim):
    PrimeNumBoolList = [True for i in range(MaxLim + 1)]
    p = 2
    PrimeList = []
    while p * p <= MaxLim:
        if PrimeNumBoolList[p]:
            for j in range(p * 2, MaxLim + 1, p):
                PrimeNumBoolList[j] = False
        p += 1
    PrimeNumBoolList[0] = False
    PrimeNumBoolList[1] = False

    for k in range(MaxLim + 1):
        if PrimeNumBoolList[k]:
            PrimeList.append(k)

    return PrimeList


# 11
def FindGreatstAdj(TwoDList, NumOfAdj):
    GreatestNum = -1
    num = -2

    for i in range(len(TwoDList) - NumOfAdj):
        for j in range(len(TwoDList[i]) - NumOfAdj):
            if TwoDList[i][j] != 0:
                GreatestNum = max(AddHorizontal(i, j, NumOfAdj, TwoDList),
                                  AddVertical(i, j, NumOfAdj, TwoDList),
                                  AddDiagonal(i, j, NumOfAdj, TwoDList),
                                  GreatestNum)

    return GreatestNum


def AddHorizontal(i, j, NumOfAdj, Arr):
    RVal = 1
    LVal = 1
    for r in range(NumOfAdj):
        RVal *= Arr[i][j + r]
    for l in range(NumOfAdj):
        LVal *= Arr[i][j - l]
    return max(RVal, LVal)


def AddVertical(i, j, NumOfAdj, Arr):
    UVal = 1
    DVal = 1
    for u in range(NumOfAdj):
        UVal *= Arr[i + u][j]
    for d in range(NumOfAdj):
        DVal *= Arr[i - d][j]
    return max(UVal, DVal)


def AddDiagonal(i, j, NumOfAdj, Arr):
    RUVal = 1
    RDVal = 1
    LUVal = 1
    LDVal = 1
    for ru in range(NumOfAdj):
        RUVal *= Arr[i + ru][j + ru]
    for rd in range(NumOfAdj):
        RDVal *= Arr[i - rd][j + rd]
    for lu in range(NumOfAdj):
        LUVal *= Arr[i + lu][j - lu]
    for ld in range(NumOfAdj):
        LDVal *= Arr[i - ld][j - ld]
    return max(RUVal, RDVal, LUVal, LDVal)


# 12
def Factors(Number):
    ListOfFactors = []
    j = 1
    while j < ((Number) + 1):
        if Number % j == 0:

            ListOfFactors.append(j)
            j += 1
        else:
            j += 1

    return ListOfFactors


def TriangleNumList(Limit):
    TriangleArr = []
    j = 0
    for i in range(Limit):
        j += i
        TriangleArr.append(j)

    del TriangleArr[0]
    return TriangleArr


# 14
def CollatzSequence(num):
    seq = [num]
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = 3 * num + 1
        seq.append(int(num))
    return seq


def LongestCollatz(minNum, maxNum):
    MaxLen = -1

    for i in range(minNum, int(maxNum / 2), 2):
        if len(CollatzSequence(i)) > MaxLen:
            MaxLen = len(CollatzSequence(i))
            MC = CollatzSequence(i)
    return MC


# 15
def LatticePath(PointArr):
    numerator = 0
    denominater = 1
    for i in range(len(PointArr)):
        numerator += PointArr[i]
        denominater *= math.factorial(PointArr[i])

    return math.factorial(numerator) / denominater


# 16

def AddDigits(Num):
    s = 0
    for i in str(Num):
        s += int(i)
    return s


# 18
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


def NextSum(arr, val, pos):
    NL = arr[pos]
    NR = arr[pos + 1]
    return max(NL, NR) + val


def UpdateTriangle(Num_Triangle):
    r = CombineRows(Num_Triangle[-2], Num_Triangle[-1])
    Num_Triangle.pop()
    Num_Triangle.pop()
    Num_Triangle.append(r)
    return Num_Triangle


def CombineRows(Top, Bottom):
    NewRow = []
    for i, e in enumerate(Top):
        s = NextSum(Bottom, e, i)
        NewRow.append(s)
    return (NewRow)


def FindMaxPath(arr):
    while len(arr) > 1:
        arr = UpdateTriangle(arr)
    return arr

# 19










# 67
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
