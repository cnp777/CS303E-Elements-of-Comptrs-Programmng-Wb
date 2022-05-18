# CS 303E Mock Exam 2
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

# Problem 1 - Student Class
# DO NOT CHANGE ANYTHING IN THE COURSE CLASS
import math


class Course:
    """A course with a name, professor, and number of credit hours"""
    def __init__(self, name, professor, hours):
        """Create a new course with the given name (a string), professor (a string), and hours (an integer)"""
        self.__name = name
        self.__professor = professor
        self.__hours = hours
    
    def getName(self):
        """Returns the name of this course"""
        return self.__name
    
    def getProfessor(self):
        """Returns the professor for this course"""
        return self.__professor
    
    def getHours(self):
        """Returns the number of credit hours this course counts for"""
        return self.__hours
    
    def __str__(self):
        """Returns the string representation of this course"""
        return "{} with {}".format(self.__name, self.__professor)

# Complete the Student class below
class Student:
    def __init__(self, name, year, major, courses):
        self.__name = name
        self.__year = year
        self.__major = major
        self.__courses = courses

    def numCourses(self):
        return len(self.__courses)

    def isUpperClassman(self):
        if self.__year == 1 or self.__year == 2:
            return False
        elif self.__year == 3 or self.__year == 4:
            return True

    def totalHours(self):
        total = 0
        for course in self.__courses:
            total += course.getHours()
        return total

    def __str__(self):
        student_year = "freshman" if (self.__year == 1) else "sophomore" if (self.__year == 2) else "junior" if (self.__year == 3) else "senior"

        return "{} is a {} {} major.".format(self.__name, student_year, self.__major)


# Problem 2 - ASCII List to String
def asciiListToString(lst):
    word = ""
    for nb in lst:
        word += chr(nb)
    return word

# Problem 3 - Essay Character Count
def essayCharacterCount(sentence, words):
    lst = sentence.split()
    count = 0
    for word in lst:
        if word.lower() not in words:
            count += len(word)
    return count

# Problem 4 - Dueling Tanks
def duelingTanks(grid): ## NOT CORRECT

    columns = len(grid[0])
    rows = len(grid)

    count = [0]*rows
    attacks = 0

    # count how many tanks
    for row in range(rows):
        count[row] = grid[row].count("T")

    for i in count:
        attacks += i - 1

    return attacks*2


# Problem 5 - Even Elements Dictionary
def evenElementsDict(tups):
    dictionary = {}
    for tup in tups:
        evens = list()
        for t in tup:
            if(t % 2) == 0:
                evens.append(t)

        dictionary[tup] = len(evens)

    return dictionary

# Problem 6 - Set of Common Factors
def setOfCommonFactors(lst):
    divisors = set()

    amount = len(lst)

    a = lst[0]

    for i in range(1, amount):
        a = math.gcd(lst[i], a)

    for b in range(1, a + 1):
        if b * b > a:
            break
        if (a % b == 0):
            divisors.add(b)
            if (a // b != b):
                divisors.add(a // b)

    return divisors

# Problem 7 - Recursive Character Last Index Dictionary
def characterLastIndexDictionary(string, index):

    dictionary = {}

    #if index >= len(string):
    #    return dictionary
    #else:
    # dictionary[string[index]] = index
    #characterLastIndexDictionary(string, index + 1)

    return {i: letter for letter, i in enumerate(string)}

# Problem 8 - Recursive Divisible by 3 and 5
def divBy3And5(lst):

    if not lst:
        return 0,0

    elif lst[0] % 3 == 0 and not lst[0] % 5 == 0:
        x, y = divBy3And5(lst[1:])
        return x + 1,y
    elif lst[0] % 5 == 0 and not lst[0] % 3 == 0:
        x, y = divBy3And5(lst[1:])
        return x,y + 1
    elif lst[0] % 3 == 0 and lst[0] % 5 == 0:
        x, y = divBy3And5(lst[1:])
        return x + 1, y + 1
    else:
        x, y = divBy3And5(lst[1:])
        return x,y


if __name__ == '__main__':
    # uncomment the following lines to run the given test cases

    # s = Student('Candice', 1, 'Chemistry', [Course('CH 301', 'Laude', 3), \
    #     Course('CS 303E', 'Young', 3), Course('UGS 303', 'Murry', 3), \
    #     Course('M 408C', 'Davis', 4), Course('GOV 310L', 'Moser', 3)])
    # print(s.isUpperClassman())
    # print(s.numCourses())
    # print(s.totalHours())
    # print(str(s))

    # print(asciiListToString([72, 101, 108, 108, 111]))
    # print(asciiListToString([]))
    # print(asciiListToString([123, 116, 114, 51, 51, 32, 37, 33, 125]))

    # print(essayCharacterCount('In conclusion the United States of America is a country', \
    #     {'the', 'a', 'an', 'at', 'but', 'by', 'in', 'for', 'of', 'on', 'to'}))
    # print(essayCharacterCount('Ultimately we shall see that history is not my strongest subject', \
    #     {'this', 'that', 'these', 'those', 'I', 'you', 'he', 'she', 'it', 'we', 'they', 'me', \
    #     'him', 'her', 'us', 'them', 'my', 'his', 'hers'}))
    # print(essayCharacterCount('nOne Of thiS actually cOuntS', {'words', 'actually', 'are', \
    #     'none', 'of', 'your', 'business', 'this', 'counts', 'as', 'poetry'}))

    #print(duelingTanks([['T', '.', '.', 'T', '.', 'T'], ['T', 'T', '.', '.', '.', '.'],['.', '.', 'T', 'T', '.', 'T'], ['.', 'T', '.', '.', '.', '.'], ['T', '.', '.', 'T', '.', '.']]))
    #print(duelingTanks([['T', '.', 'T'], ['.', 'T', '.'], ['T', '.', 'T']]))
    #print(duelingTanks([['.', '.', 'T', '.'], ['T', '.', '.', '.'], ['.', '.', '.', 'T'], ['.', 'T', '.', '.']]))

    # print(evenElementsDict({(1, 2, 3, 4, 5), (2, 222, 2), (17,)}))
    # print(evenElementsDict(set()))
    # print(evenElementsDict({(0,), (1, 3, 5, 7, 9), (3, 1, 4, 1, 5, 9), (98, 76, 54, 32, 10)}))

    #print(setOfCommonFactors([50, 100]))
    #print(setOfCommonFactors([18]))
    #print(setOfCommonFactors([210, 770, 2730, 1015]))

    #print(characterLastIndexDictionary('Hello World!', 0))
    #print(characterLastIndexDictionary('', 0))
    #print(characterLastIndexDictionary('CS303E is fun CS303E is fun CS303E is fun', 0))

    #print(divBy3And5([15, 9, 7, 5, 3]))
    #print(divBy3And5([]))
    #print(divBy3And5([32, 47, -200, 5, 20]))


    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT