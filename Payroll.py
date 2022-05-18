# File: Payroll.py
# Student: Clara Torslov
# UT EID: ct32699
# Course Name: CS303E
#
# Date: 02/11/22
# Description of Program: Reads in the following information and prints a payroll statement.

print("")
name = str(input("Enter employee's name: "))
hours = float(input("Enter number of hours worked in a week: "))
payRate = float(input("Enter hourly pay rate: "))
fedTax = float(input("Enter federal tax withholding rate: "))
stateTax = float(input("Enter state tax withholding rate: "))

fedWith = fedTax*payRate*hours
stateWith = stateTax*payRate*hours

print("")
print("Employee Name: " + name)
print("Hours Worked: " + str("%.1f" % hours))
print("Pay Rate: $" + str("%.2f" % payRate))
print("Gross Pay: $" + str("%.2f" % float(payRate*hours)))
print("Deductions: ")
print("  Federal Withholding (" + str("%.1f" % float(fedTax*100)) + "%): $" + str("%.2f" % fedWith))
print("  State Withholding (" + str("%.1f" % float(stateTax*100)) + "%): $" + str("%.2f" % stateWith))
print("  Total Deduction: $" + str("%.2f" % float(stateWith+fedWith)))
print("Net Pay: $" + str("%.2f" % float(payRate*hours - (stateWith + fedWith))))

