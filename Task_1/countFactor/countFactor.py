# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 01:39:30 2024

@author: t460
"""
def countFactors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

n = int(input("Enter a number to get its factors: "))
factors = countFactors(n)

print(f"The factors of {n} are:")
for factor in factors:
    print(factor)

