import math


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

    for i in range(minNum, int(maxNum/2), 2):
        if len(CollatzSequence(i)) > MaxLen:
            MaxLen = len(CollatzSequence(i))
            MC = CollatzSequence(i)
    return MC


print(LongestCollatz(77031, 1000000))
