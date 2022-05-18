# CS 303E Exam 2B
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

# Problem 1: Class Behavior

class ClassBehavior:
    def __init__(self, dictionary):
        self.__dictionary = dictionary

    def updateBehavior(self, name, behavior):
        if name in self.__dictionary:
            self.__dictionary[name] = self.__dictionary[name] + behavior
        else:
            self.__dictionary[name] = behavior

    def getBehavior(self, name):
        if name in self.__dictionary:
            return self.__dictionary[name]
        else:
            return None

    def getBehavedStudents(self, behavior):
        students = set()
        for name in self.__dictionary:
            if self.__dictionary[name][-1] == behavior:
                students.add(name)
        return students

# Problem 2: Unique First Trigrams
def uniqueFirstTrigrams(s1, s2):
    set1 = set()
    set2 = set()

    for i in range(len(s1) - 2):
        set1.add(s1[i:i + 3])

    for i in range(len(s2) - 2):
        set2.add(s2[i:i + 3])

    return set1.difference(set2)


# Problem 3: Weekly Low
def weeklyLow(lst, city):

    for i in range(len(lst[0])):
        if lst[i][0] == city:
            return min(lst[i][1:])


# Problem 4: Create List Encoding Key
def createListEncodingKey(s, d):
    dictionary = {}

    for i in range(0,len(s)-1,2):
        dictionary[(s[i],s[i+1])] = (d[i],d[i+1])

    return dictionary


# Problem 5: Quicksort Pivot
def quicksortPivot(lst, idx):

    less = []
    pivot = []
    greater = []

    for nb in lst:
        if nb < lst[idx]:
            less.append(nb)
        elif nb > lst[idx]:
            greater.append(nb)
        else:
            pivot.append(nb)

    return less + pivot + greater



# Problem 6: String Error Correction
def stringErrorCorrection(string, dictionary):
    newstring = ""
    for i in range(len(string)):
        if i in dictionary:
            newstring += dictionary[i]
        else:
            newstring += string[i]

    return newstring



# Problem 7: Recursive Delete Non Alphanumeric
def deleteNonAlphanumeric(string):
    if len(string) <= 1: # base case
        if string[0].isalnum():
            return string
        else:
            return ""
    else:
        if string[0].isalnum():
            return string[0] + deleteNonAlphanumeric(string[1:])
        else:
            return deleteNonAlphanumeric(string[1:])


# Problem 8: Set of Big Integers
def setOfBigIntegers(lst1):
    if not lst1:
        return set()
    else:
        set1 = setOfBigIntegers(lst1[1:])
        nb = lst1[0]
        if abs(nb) > 20:
            set1.add(nb)
        return set(set1)


if __name__ == "__main__":
    """
    If you want to test your code on your computer, uncomment the respective
    function call(s) below.

    DO NOT CALL YOUR FUNCTIONS ANYWHERE OUTSIDE OF THIS AREA
    """

   #cb = ClassBehavior({'Tzuyu': 'SNFS', 'Sana': 'NFNF', 'Dahyun': 'SSSS', 'Mina': 'SFSS'})
    #print(cb.getBehavior('Tzuyu'))
    #print(cb.getBehavedStudents('S'))

    #cb = ClassBehavior({'Pouiz': 'FFFF', 'Aerovale':'SFS', 'Jadkareen':'NSFSS'})
    #cb.updateBehavior('Mart', 'N')
    #cb.updateBehavior('Pouiz', 'N')
    #print(cb.getBehavior('Xariul'))
    #print(cb.getBehavedStudents('N'))

    # cb = ClassBehavior({'Jungkook':'SSFS', 'Tae-hyung':'NFNF', 'RM':'SNFS', 'Suga':'SFNN'})
    # print(cb.getBehavedStudents('N'))
    # cb.updateBehavior('Tae-hyung', 'N')
    # print(cb.getBehavedStudents('N'))

    # print(uniqueFirstTrigrams('CACTTAG', 'CGAGCTTA'))
    # print(uniqueFirstTrigrams('ACAGCAATT', 'TAC'))
    # print(uniqueFirstTrigrams('ACGT', 'TATACGTAC'))

    # lst = [['', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], \
    # ['Austin', 71, 73, 72, 73, 72, 73, 70], \
    # ['Dallas', 69, 70, 68, 69, 67, 66, 63], \
    # ['San Antonio', 71, 73, 73, 74, 73, 73, 71], \
    # ['Houston', 73, 74, 75, 75, 76, 75, 74], \
    # ['El Paso', 64, 63, 64, 59, 59, 61, 62]]

    #print(weeklyLow(lst, 'Dallas'))
    # print(weeklyLow(lst, 'Houston'))
    # print(weeklyLow([['', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], ['Plano', 72, 72, 72, 0, 24, 30, 35], ['Frisco', 98, 95, 49, 59, 59, 63, 62]], 'Plano'))

    #print(createListEncodingKey([72, 101, 108, 108, 111, 87, 111, 114, 108, 100], [102, 71, 109, 97, 120, 65, 102, 104, 77, 122]))
    #print(createListEncodingKey([1, 2, 3, 4], [4, 3, 2, 1]))
    #print(createListEncodingKey([1, 2, 1, 2], [3, 4, 3, 4]))

    #print(quicksortPivot([7, 8, 38, -3, -2, 28, -11, -12, -9, 35], 1))
    # print(quicksortPivot([5, 4, 3, 2, 1], 2))
    # print(quicksortPivot([16, 49, 70, 58, 24], 3))

    # print(stringErrorCorrection('xedloWVrly', {0: 'H', 2: 'l', 9: 'd', 6: 'o'}))
    # print(stringErrorCorrection('Iblo3eZLzuBu?', {1: ' ', 4: 'v', 7: 'T', 6: ' ', 10: 'y', 12: '!'}))
    # print(stringErrorCorrection('Al2o3tbdopL!', {2: 'm', 4: 's', 7: 'D', 6: ' ', 9: 'n', 10: 'e'}))

    # print(deleteNonAlphanumeric("1+2=3 & I'm sure of it!"))
    # print(deleteNonAlphanumeric("I'm seeing TWICE in 8 days LET'S GOO!!!"))
    # print(deleteNonAlphanumeric('!!Congrats on finishing CS 303e!'))

    # print(setOfBigIntegers([38, 5, 10, -11, 20, 49, -19, 38, -11, 29, 0, -28]))
    # print(setOfBigIntegers([86, 6, 25, 78, 99, 50, 74, 87, 97, 86]))
    # print(setOfBigIntegers([-20, 0, 20]))

    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT
