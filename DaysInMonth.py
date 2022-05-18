# File: DaysInMonth.py
# Student: Clara Torslov
# UT EID: ct32699
# Course Name: CS303E
#
# Date: 02/18/22
# Description of Program: Computes the numbers of days in a month.
# The user enters the month and year and the program displays the number of days in that month.

year = int(input("Please enter a year: "))
month = int(input("Please enter a month: "))

if (year % 400 == 0): LeapYear = True
elif (year % 100 == 0): LeapYear = False
elif (year % 4 == 0): LeapYear = True
else: LeapYear = False

if month in (1,3,5,7,8,10,12): days = 31
if (month == 2):
    if LeapYear: days = 29
    else: days = 28
else: days = 30

if (month == 1): Month = "January"
if (month == 2): Month = "February"
if (month == 3): Month = "March"
if (month == 4): Month = "April"
if (month == 5): Month = "May"
if (month == 6): Month = "June"
if (month == 7): Month = "July"
if (month == 8): Month = "August"
if (month == 9): Month = "September"
if (month == 10): Month = "October"
if (month == 11): Month = "November"
if (month == 12): Month = "December"

print(str(Month), str(year), "has", str(days), "days")
