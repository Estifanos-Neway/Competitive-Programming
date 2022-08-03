# Grading Students
# https://www.hackerrank.com/challenges/grading/problem
# Easy

#!/bin/python3

def round(num):
    if num < 38 or num % 5 < 3:
        return num
    return num + 5 - num % 5

def gradingStudents(grades):
    return [round(g) for g in grades]


if __name__ == '__main__':
    print(gradingStudents([73, 67, 38, 33, 80,20]))
