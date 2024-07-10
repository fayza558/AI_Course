# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 02:06:01 2024

@author: t460
"""

def read_grades(file_name):
    students = []
    grades = []
    with open(file_name, 'r') as file:
        for line in file:
            name, grade = line.strip().split()
            students.append(name)
            grades.append(float(grade))
    return students, grades

def calculate_statistics(students, grades):
    average = sum(grades) / len(grades)
    maximum = max(grades)
    minimum = min(grades)
    max_students = [students[i] for i in range(len(grades)) if grades[i] == maximum]
    min_students = [students[i] for i in range(len(grades)) if grades[i] == minimum]
    return average, maximum, minimum, max_students, min_students

def write_statistics(file_name, average, maximum, minimum, max_students, min_students):
    with open(file_name, 'w') as file:
        file.write(f"Average Grade: {average:.2f}\n")
        file.write(f"Maximum Grade: {maximum}\n")
        file.write(f"Minimum Grade: {minimum}\n")
        file.write(f"Students with Maximum Grade ({maximum}): {', '.join(max_students)}\n")
        file.write(f"Students with Minimum Grade ({minimum}): {', '.join(min_students)}\n")

input_file = 'c:/Users/t460/Desktop/AI_Course/Task_1/Student/student.txt'
output_file = 'studentoutput.txt'

students, grades = read_grades(input_file)

average, maximum, minimum, max_students, min_students = calculate_statistics(students, grades)

write_statistics(output_file, average, maximum, minimum, max_students, min_students)

print(f"Grades statistics have been written to {output_file}")
