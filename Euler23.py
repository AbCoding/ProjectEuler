import math

LIMIT = 28123


def GetFactors(num):
    factors = [1]
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            factors.append(i)
            factors.append((num // i))
    return factors


def IsNumAbundant(num):
    Factors = GetFactors(num)
    s = 0
    for i in Factors:
        s += i
    return (s > num)


def GenerateListOfAbundantNumbers(limit):
    nums = []
    for i in range(1, limit):
        if IsNumAbundant(i):
            nums.append(i)
    return nums


def IsSummableByTwoAbundantNumbers(num, ListOfAbundantNums):
    for i in ListOfAbundantNums:
        if i < num//2+1:
            if (num - i) in ListOfAbundantNums:
                return True
        else:
            return False

def GetListOfNonSummable(limit,ListOfAbundantNums):
    possibleSums=[]
    totalArr=[]
    for i in range(1,limit+1):
        totalArr.append(i)
    for i in ListOfAbundantNums:
        for j in ListOfAbundantNums:
            if (i+j)<=limit:
                possibleSums.append(i+j)
    sumAbun=sum(set(possibleSums))
    print(totalArr)
    sumTot=sum(totalArr)
    return sumTot-sumAbun
ListOfAbundantNums = GenerateListOfAbundantNumbers(LIMIT)
# 4179871
print(GetListOfNonSummable(LIMIT,ListOfAbundantNums))