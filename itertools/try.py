#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(n):

    a=bin(n)[2:]
    #print(a)
    x=32-len(a)
    bit=x*"0"+a
    #print(bit)
    flip=""
    lst=list()
    for i in range(32):
        if bit[i] is '1':
            flip=flip+'0'
        elif(bit[i] is '0'):
            flip=flip+'1'

    #print(a)
    power=31
    dec=0
    for j in range(32):
        dec=dec+(int(flip[j]))*(2**power)
        power=power-1
    return (dec)

    #break
    #return ("")
if __name__ == '__main__':
    fptr = sys.stdout

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
