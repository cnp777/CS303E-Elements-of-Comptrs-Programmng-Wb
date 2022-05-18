# File: Project2.py
# Student: Clara Torslov
# UT EID: ct32699
# Course Name: CS303E
#
# Date: April 14th 2022
# Description of Program: A Fibonnaci Number laboratory, containing 6 commands with 4 different operations for Fibonacci numbers.

# Functions to be used

# command = 1
def firstNFibNumbers (n):
    """ Return a list of the first n Fibonnaci numbers. If
        n < 0, return the empty list. """
    if n <= 0:
        return []
    # Handle the cases of n == 1 and n == 2 specially.
    elif n == 1:
        return [ 0 ]
    elif n == 2:
        return [ 0, 1 ]
    # Here we know that n is at least 2.
    else:
        fib1, fib2 = 0, 1
        fibs = [ 0, 1 ]
        counter = 2
        # Use the previous two values to generate
        # and record the next value.
        for counter in range( 2, n ):
            # Update fib1 and fib2 with their new
            # values.
            fib1, fib2 = fib2, fib1 + fib2
            # Add the newest value to the list we're
            # creating.
            fibs.append( fib2 )
        return fibs

# command = 2
def ithFibNumber(i):
    """ Returns the i'th Fibonnaci number. """
    FibList = firstNFibNumbers(i+1)
    return FibList[i]

# command = 3
def FibBelowN(n):
    """Lists the Fibonnaci numbers less or equal to n.
    If n < 0, return the empty list."""
    if n < 0:
        return []
    # Handle the cases of n == 0 and n == 1 specially.
    elif n == 0:
        return [0]
    elif n == 1:
        return [0, 1, 1]
    # Here we know that n is at least 1.
    else:
        fib1, fib2 = 1, 1
        fibs = [0, 1]

        while fib2 <= n:
            fibs.append(fib2)
            fib1, fib2 = fib2, fib1 + fib2

        return fibs

# command = 4
def NumFibBelowN(n):
    """Counts how many Fibonnaci numbers are less than or equal to n"""
    if n < 0:
        return 0
    # Handle the cases of n == 0 and n == 1 specially.
    elif n == 0:
        return 1
    elif n == 1:
        return 3
    # Here we know that n is 2 or above.
    else:
        fibs = FibBelowN(n)
        return len(fibs)

# command = 5
def FibSumToN(n):
    """Finds a list of the largest Fibonnaci numbers that add up to n."""

    if n < 0:
        return []
    # Handle the cases of n == 0 and n == 1 specially.
    elif n == 0:
        return [0]
    elif n == 1:
        return [1]
    # Here we know that n is 2 or above.
    else:
        fibs = []
        while n > 0:
            k = FibBelowN(n)[-1]
            fibs.append(k)
            n -= k

        return fibs

### Program start

print("")
print("Welcome to the Fibonnaci Number laboratory!")
print("")

print("The following commands are available:")
print("  0: Exit.")
print("  1: List the first N Fibonnaci numbers.")
print("  2: Display the ith Fibonnaci number (0-based).")
print("  3: List the Fibonnaci numbers less or equal to N.")
print("  4: How many Fibonnaci numbers are less or equal to N?")
print("  5: Find a list of the largest Fibonnaci numbers that add up to N.")
print("  6: Display this help message.")
print("")

command = int(input("Please enter a command (0, 1, 2, 3, 4, 5 or 6): "))

while command:

    if(command == 1):
        N = int(input("You've asked for the first N Fibonnaci numbers. What is N? "))
        if(N < 0):
            print("ERROR: Illegal value entered.")
            print("")
        else:
            print(firstNFibNumbers(N))
            print("")

    elif(command == 2):
        I = int(input("You've asked for the ith Fibonnaci number. What is i? "))
        if(I < 0):
            print("ERROR: Illegal value entered.")
            print("")
        else:
            print(ithFibNumber(I))
            print("")

    elif (command == 3):
        N = int(input("You've asked for the Fibonnaci numbers less than or equal to N. What is N? "))

        print(FibBelowN(N))
        print("")

    elif (command == 4):
        N = int(input("You've asked how many Fibonnaci numbers are less than or equal to N. What is N? "))

        print(NumFibBelowN(N))
        print("")

    elif (command == 5):
        N = int(input("You've asked for Fibonnaci numbers that sum to N. What is N? "))
        if (N < 0):
            print("ERROR: Illegal value entered.")
            print("")
        else:
            print(FibSumToN(N))
            print("")

    elif (command == 6):
        print("The following commands are available:")
        print("  0: Exit.")
        print("  1: List the first N Fibonnaci numbers.")
        print("  2: Display the ith Fibonnaci number (0-based).")
        print("  3: List the Fibonnaci numbers less or equal to N.")
        print("  4: How many Fibonnaci numbers are less or equal to N?")
        print("  5: Find a list of the largest Fibonnaci numbers that add up to N.")
        print("  6: Display this help message.")
        print("")

    elif (not command == 0 and not command == 1 and not command == 2 and not command == 3 and not command == 4 and not command == 5 and not command == 6):
        print("ERROR: Illegal command. Try again.")
        print("")
        print("The following commands are available:")
        print("  0: Exit.")
        print("  1: List the first N Fibonnaci numbers.")
        print("  2: Display the ith Fibonnaci number (0-based).")
        print("  3: List the Fibonnaci numbers less or equal to N.")
        print("  4: How many Fibonnaci numbers are less or equal to N?")
        print("  5: Find a list of the largest Fibonnaci numbers that add up to N.")
        print("  6: Display this help message.")
        print("")

    command = int(input("Please enter a command (0, 1, 2, 3, 4, 5 or 6): "))

if (command == 0):
    print("")
    print("Thanks for using the Fibonnaci Laboratory!  Goodbye.")