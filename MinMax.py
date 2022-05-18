# File: MinMax.py
# Student: Clara Torslov
# UT EID: ct32699
# Course Name: CS303E
#
# Date: February 25th 2022
# Description of Program: Finds the minimum and maximum value among user inputted values.

num = input("Enter an integer or 'stop' to end: ")

if(num == 'stop'):
    print("You didn't enter any numbers")
else:
    maxNum = int(num)
    minNum = int(num)
    while (num != 'stop'):
        num = int(num)
        if (num < minNum): minNum = num
        if (num > maxNum): maxNum = num
        num = input("Enter an integer or 'stop' to end: ")
        continue

    print("The maximum value is", maxNum)
    print("The minimum value is", minNum)

