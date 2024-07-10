# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 01:29:25 2024

@author: t460
"""

def countOccurence(lst):
    occurences = {}
    for item in lst:
        if item in occurences:
            occurences[item] += 1
        else:
            occurences[item] = 1
    return occurences

lst = [1, 1, 2, 3, 2, 3, 1, "c", 5, "c"]
occurences = countOccurence(lst)

for key, value in occurences.items():
    print(f"{key} exists: {value} times")

