# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 01:15:42 2024

@author: t460
"""
"""
numbers = [3, 5, 7, 2, 8, 6]
largest_number=max(numbers)
print("The largest number in the list is:", largest_number)
"""
def largestNumber (lst):
    if not lst:
        return None
    largest=lst[0]
    for num in lst:
        if num>largest:
            largest=num
    return largest 
numbers=[3, 5, 7, 2, 8, 6]
largest_number=largestNumber(numbers)
print("The largest number in the list is:", largest_number)