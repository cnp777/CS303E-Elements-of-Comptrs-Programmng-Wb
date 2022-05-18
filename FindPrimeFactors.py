# File: FindPrimeFactors.py
# Student: Clara Torslov
# UT EID: ct32699
# Course Name: CS303E
#
# Date: April 1st 2022
# Description of Program: Asks user to input a series of arbitrary positive integers
# and returns for each a list of its prime factors. Exits when the user enters 0.

# Functions to be used
from math import *

def isPrime( num ): # From slideset 6 slide number 27
    """ Test whether num is prime. """
# Deal with evens and numbers < 2.
    if (num < 2 or num % 2 == 0 ):
        return ( num == 2 )
# See if there are any odd divisors # up to the square root of num.
    divisor = 3
    while (divisor <= sqrt( num )):
        if ( num % divisor == 0 ):
            return False
        else:
            divisor += 2
    return True

def findNextPrime ( num ): # From slideset 6 slide number 26
    """ Find the first prime > num. """
    if ( num < 2 ):
        return 2
# If (num >= 2 and num is even), the
# next prime after num is at least (num - 1)
    if (num % 2 == 0):
        num -= 1
    guess = num + 2

    while( not isPrime(guess) ):
        guess += 2
    return guess


print("Find Prime Factors:")

# We can assume that the input will be an integer
num = int(input("Enter a positive integer (or 0 to stop): "))

if(num == 0):
    print("Goodbye!")

while num != 0:

    if(num == 1):
        print("1 has no prime factorization.")

    elif(num<0):
        print("Negative integer entered.  Try again.")

    elif(num > 1):
        # print the prime factorization as a list. If the number is a prime, print a list with just that number.
        primes = []

        if(isPrime(num)):
            primes.append(num)
            print("The prime factorization of", num, "is:", primes)

        else:
            d = 2
            num1 = num
            while num1 > 1:
                while(num1 % d == 0):
                    primes.append(d)
                    num1 = num1 // d # integer division
                d = findNextPrime(d)

            print("The prime factorization of", num, "is:", primes)

    print("")
    num = int(input("Enter a positive integer (or 0 to stop): "))

    print("Goodbye!")

