# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def isPrime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

n = int(input("Enter the number: "))
prime = isPrime(n)
if prime:
    print("The number is Prime")
else:
    print("The number is Not Prime")

    