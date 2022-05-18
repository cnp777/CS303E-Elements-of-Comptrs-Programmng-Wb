# CS 303E Mock Exam 1
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters
import math

# Problem 1: Poisson Probability
def poissonProbability():
    b = float(input())
    k = int(input())
    if(k==0):
        kFactorial = 1
    else:
        kFactorial = 1
        for i in range(1, k + 1):
            kFactorial *= i
    print( format((math.e**(-b) * b**k ) / kFactorial, ".3f") )

# Problem 2: Swap Case
def swapCase():
    charInput = input()
    if (ord(charInput) >= 97 and ord(charInput) <= 122): print( chr( ord(charInput) - 32)) # convert to upper case
    elif(ord(charInput) >= 65 and ord(charInput) <= 90): print( chr( ord(charInput) + 32)) # convert to lower case
    else: print(charInput)

# Problem 3: Sum Series
def sumSeries():
    n = int(input())
    value = 0
    for i in range(2, n+1):
        value += (i-1)*i
    print(value)

# Problem 4: Sort Three Integers
def sortThreeIntegers():
    int1 = int(input())
    int2 = int(input())
    int3 = int(input())

    if (int1 <= int2 and int1 <= int3):
        if(int2 >= int3):
            print(int1, int3, int2)
        else:
            print(int1, int2, int3)

    elif (int2 <= int1 and int2 <= int3):
        if(int1 >= int3):
            print(int2, int3, int1)
        else:
            print(int2, int1, int3)

    elif (int3 <= int1 and int3 <= int2):
        if(int1>=int2):
            print(int3,int2,int1)
        else:
            print(int3, int2, int1)

# Problem 5: Sum Positive Floats
def sumPositiveFloats():
    num = float(input())
    sum = num
    while (num!= 0):
        num = float(input())
        if(num>0):
            sum += num
    print(format(sum, ".3f"))

# Problem 6: Range Computation
def rangeComputation():
    start = int(input())
    end = int(input())
    count = 0
    sum = 0
    for i in range(start, end+1):
        sum += i
        count += 1
        if(count>=3):
            sum = sum*2
            count = 0
    print(sum)

# Problem 7: Largest Square
def largestSquare():
    n = int(input())
    k = 1
    while (k**2 < n):
        k += 1
    if(k**2 <= n): print(k)
    else: print(k-1)

# Problem 8: Collatz Conjecture
def collatzConjecture():
    n = int(input())
    terms = 1
    while (n > 1):
        if (n % 2 == 0):
            n = n/2
            terms += 1
        else:
            n = 3*n + 1
            terms += 1
    print(terms)

if __name__=="__main__":
    """
    If you want to test your code on your computer, uncomment the respective
    function call(s) below.
    
    DO NOT CALL YOUR FUNCTIONS ANYWHERE OUTSIDE OF THIS AREA
    """

    # poissonProbability()
    # swapCase()
    # sumSeries()
    # sortThreeIntegers()
    # sumPositiveFloats()
    # rangeComputation()
    # largestSquare()
    # collatzConjecture()


    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT