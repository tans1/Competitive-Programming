#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    
    for i in range(n):
        j = i

        while j > 0 and arr[j] < arr[j-1]:
            temp = arr.copy()
            temp[j] = temp[j-1]

            arr[j], arr[j-1] = arr[j-1] , arr[j]
            print(*temp)
            
            j -= 1

    print(*arr)
    return 
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
