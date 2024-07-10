# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 02:18:54 2024

@author: t460
"""



import pandas as pd

def read_grades(file_name):
    df = pd.read_csv(file_name, delim_whitespace=True, header=None, names=['Student', 'Grade'])
    return df

def calculate_statistics(df):
    average = df['Grade'].mean()
    maximum = df['Grade'].max()
    minimum = df['Grade'].min()
    max_students = df[df['Grade'] == maximum]['Student'].tolist()
    min_students = df[df['Grade'] == minimum]['Student'].tolist()
    return average, maximum, minimum, max_students, min_students

def write_statistics(file_name, average, maximum, minimum, max_students, min_students):
    with open(file_name, 'w') as file:
        file.write(f"Average Grade: {average:.2f}\n")
        file.write(f"Maximum Grade: {maximum}\n")
        file.write(f"Minimum Grade: {minimum}\n")
        file.write(f"Students with Maximum Grade ({maximum}): {', '.join(max_students)}\n")
        file.write(f"Students with Minimum Grade ({minimum}): {', '.join(min_students)}\n")

input_file = 'c:/Users/t460/Desktop/AI_Course/Task_1/Student2/student.txt'
output_file = 'studentoutput.txt'

df = read_grades(input_file)

average, maximum, minimum, max_students, min_students = calculate_statistics(df)

write_statistics(output_file, average, maximum, minimum, max_students, min_students)

print(f"Grades statistics have been written to {output_file}")
