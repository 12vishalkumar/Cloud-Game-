import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    e = 100
    i = 0
    L = len(c)
    while(e == 100 or i):
        i = (i+k)%L
        e -= 1+2*c[i]
    return e

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c, k)
    fptr.write(str(result) + '\n')
    fptr.close()