import math

NumDictOne = {
    0: "",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine"

}
NumDictTens = {
    0: "Ten",
    1: "Eleven",
    2: "Twelve",
    3: "Thirteen",
    4: "Fourteen",
    5: "Fifteen",
    6: "Sixteen",
    7: "Seventeen",
    8: "Eighteen",
    9: "Nineteen"

}
NumDictTwo = {
    0: "",
    2: "Twenty",
    3: "Thirty",
    4: "Forty",
    5: "Fifty",
    6: "Sixty",
    7: "Seventy",
    8: "Eighty",
    9: "Ninety"

}


def NumberInLetters(Num):
    NumArr = []
    NumInL = ""
    for i in str(Num):
        NumArr.append(int(i))

    NumArr.reverse()
    if len(NumArr) > 3:
        NumArr[3] = NumDictOne[NumArr[3]] + "Thousand"

    if len(NumArr) > 2:
        if NumArr[2] != 0:
            if NumArr[0] or NumArr[1] != 0:
                NumArr[2] = NumDictOne[NumArr[2]] + "Hundredand"
            else:
                NumArr[2] = NumDictOne[NumArr[2]] + "Hundred"
        else:
            NumArr[2]= ""

    ## Ones and Tens Digit
    if len(NumArr) > 1:
        if NumArr[1] != 1:
            NumArr[0] = NumDictOne[NumArr[0]]
            NumArr[1] = NumDictTwo[NumArr[1]]
        else:
            NumArr[1] = NumDictTens[NumArr[0]]
            NumArr.pop(0)
    else:
        if NumArr[0] != 0:
            NumArr[0] = NumDictOne[NumArr[0]]
        else:
            NumArr[0]= "Zero"

    NumArr.reverse()
    for i in NumArr:
        NumInL+= i
    return NumInL


ArrOfNum = []
for i in range(1,10000):
    ArrOfNum.append(NumberInLetters(i))
s=0
for i in ArrOfNum:
   s += len(i)

print(NumberInLetters(1424))



