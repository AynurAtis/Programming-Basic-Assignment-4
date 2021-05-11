# 250201092

import math


def minNumOfTrials(H, N):
    if N == 1:
        return H
    if H < 1:
        return 0
    else:
        total = 0
        L = H       # L is Level
        N_copy = N  # value of N
        num = N_copy
        for i in range(num):   # this loop is executing until number of num
            if L == 1:
                L -= 1
                break
            if N_copy >= 2:  # Until one device remains, it is done binary search.
                L = math.ceil(L/2)  # Divides the height of platform to two. (Binary search)
                total += 1   # trial number is increasing 1 by 1.
                N_copy -= 1  # number of devices is decreasing 1 by 1.
            else:            # İf one device remains, it doesn't binary search and pass the next level.
                L -= 1       # Level is decreasing 1 by 1.
                total += 1   # trial number is increasing 1 by 1.
                N_copy -= 1  # number of devices is decreasing 1 by 1.
    x = minNumOfTrials(L, N)
    return total + x   # number of minimum Trials


def numOfWays(L):

    # A function is created to find num of ways. This function ;
    # for level 1= 0*11+8 = 8 and for level 2= 8*11+1 = 89 and for level 3= 89*11+8 = 987 etc.
    if L == 0:
        return 1
    if L == 1:
        return 8
    else:
        x = numOfWays(L-1) * 11 + numOfWays(L-2)
    return x


def bfNumOfTrials(H, N):
    if H == 1:
        return 1
    else:
        total = 1
        x = bfNumOfTrials(H-1, N)
        return total + x


def main():
    print("minNumOfTrials(10, 3) =", minNumOfTrials(10, 3))
    print("numOfWays(4) =", numOfWays(4))
    print("bfNumOfTrials(10, 3) =", bfNumOfTrials(10, 3), "\n")

    print("minNumOfTrials(7, 5) =", minNumOfTrials(7, 5))
    print("numOfWays(3) =", numOfWays(3))
    print("bfNumOfTrials(7, 5) =", bfNumOfTrials(7, 5), "\n")

    print("minNumOfTrials(9, 1) =", minNumOfTrials(9, 1))
    print("numOfWays(2) =", numOfWays(2))
    print("bfNumOfTrials(9, 1) =", bfNumOfTrials(9, 1), "\n")

    print("minNumOfTrials(12, 2) =", minNumOfTrials(12, 2))
    print("numOfWays(5) =", numOfWays(5))
    print("bfNumOfTrials(12, 2) =", bfNumOfTrials(12, 2), "\n")

    print("minNumOfTrials(6, 5) =", minNumOfTrials(6, 5))
    print("numOfWays(1) =", numOfWays(1))
    print("bfNumOfTrials(6, 5) =", bfNumOfTrials(6, 5), "\n")


main()
