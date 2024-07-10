# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 01:04:38 2024

@author: t460
"""
def sumOfSquares(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * i
    return sum

n = int(input("Enter a number to calculate the sum of squares up to this number: "))
mysum = sumOfSquares(n)
print("The sum of squares up to", n, "is", mysum)

