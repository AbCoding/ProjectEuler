import math


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


def PalMult(Max):
    NextNums =0
    i = Max-1
    while i >=100:

        if i % 11 == 0:
            j = 999
            dj=1

        else:
            j=990
            dj=11

        while j >=100:
            TempNum = i * j
            if (NextNums < i * j):
                if PalindromeCheck(TempNum):

                    NextNums =i*j


            j -= dj
        i -= 1

    return NextNums
