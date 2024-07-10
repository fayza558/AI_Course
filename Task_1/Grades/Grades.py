# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 01:46:06 2024

@author: t460
"""

def read_grades(file_name):
    with open(file_name, 'r') as file:
        grades = [float(line.strip()) for line in file]
    return grades

def calculate_statistics(grades):
    average = sum(grades) / len(grades)
    maximum = max(grades)
    minimum = min(grades)
    return average, maximum, minimum

def write_statistics(file_name, average, maximum, minimum):
    with open(file_name, 'w') as file:
        file.write(f"Average Grade: {average:.2f}\n")
        file.write(f"Maximum Grade: {maximum}\n")
        file.write(f"Minimum Grade: {minimum}\n")

input_file = 'c:/Users/t460/Desktop/AI_Course/Task_1/Grades/grades.txt'
output_file = 'grades_summary.txt'

grades = read_grades(input_file)

average, maximum, minimum = calculate_statistics(grades)

write_statistics(output_file, average, maximum, minimum)

print(f"Grades statistics have been written to {output_file}")

