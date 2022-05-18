# File: MyStringFunctions.py
# Student: Clara Torslov
# UT EID: ct32699
# Course Name: CS303E
#
# Date: Monday, March 28, 2022
# Description of Program: Library of functions to use on strings.

def myAppend( str, ch ):
    # Return a new string that is like str but with
    # character ch added at the end
    return str + ch

def myCount( str, ch ):
    # Return the number of times character ch appears
    # in str.
    count = 0

    for i in str:
        if(i == ch):
            count += 1

    return count

def myExtend( str1, str2 ):
    # Return a new string that contains the elements of
    # str1 followed by the elements of str2, in the same
    # order they appear in str2.
    return myAppend(str1,str2)

def myMin( str ):
    # Return the character in str with the lowest ASCII code.
    # If str is empty, print "Empty string: no min value"
    # and return None.
    if str == "":
        print("Empty string: no min value")
        return None
    else:
        min = str[0]
        for i in str:
            if(ord(i)<ord(min)): min = i
        return min

def myInsert( str, i, ch ):
    # Return a new string like str except that ch has been
    # inserted at the ith position.  I.e., the string is now
    # one character longer than before. Print "Invalid index" if
    # i is greater than the length of str and return None.
    if(i > len(str)):
        print("Invalid index")
        return None
    else:
        str_new = myAppend(str[:i], ch)
        str_new = myAppend(str_new, str[i:])
        return str_new

def myPop( str, i ):
    # Return two results:
    # 1. a new string that is like str but with the ith
    #    element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is greater than or
    # equal to len(str), and return str unchanged and None
    if(i > len(str)):
        print("Invalid index")
        return str, None
    else:
        str_new = ""
        for j in range(len(str)):
            if (j != i):
                str_new = myAppend(str_new, str[j])
            elif(j == i):
                charac = str[j]
    return str_new, charac

def myFind( str, ch ):
    # Return the index of the first (leftmost) occurrence of
    # ch in str, if any.  Return -1 if ch does not occur in str.
    for i in range(len(str)):
        if(str[i] == ch):
            return i
    return -1

def myRFind( str, ch ):
    # Return the index of the last (rightmost) occurrence of
    # ch in str, if any.  Return -1 if ch does not occur in str.
    pos = -1
    for i in range(len(str)):
        if(str[i] == ch):
            pos = i
    return pos

def myRemove( str, ch ): # FAILS
    # Return a new string with the first occurrence of ch
    # removed.  If there is none, return str.
    pos = myFind(str, ch)

    if(pos == -1):
        return str
    else:
        x,y = myPop(str,pos)
        return x

def myRemoveAll( str, ch ):
    # Return a new string with all occurrences of ch.
    # removed.  If there are none, return str.

    str_new = ""
    for i in str:
        if(i != ch):
            str_new = myAppend(str_new, i)

    return str_new

def myReverse( str ):
    # Return a new string like str but with the characters
    # in the reverse order.
    str_new = ""
    for i in str:
        str_new = myAppend(i,str_new)
    return str_new