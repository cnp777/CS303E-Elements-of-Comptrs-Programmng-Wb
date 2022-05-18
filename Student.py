# File: Student.py
# Student: Clara Torslov
# UT EID: ct32699
# Course Name: CS303E
#
# Date: Monday, March 21, 2022
# Description of Program: Definition of a Student class. Each Student object contains a name, and two exam grades,
# as well as setter, getter and print methods along with a method to get the students average.

class Student:
    def __init__(self, name, Exam1Grade = None, Exam2Grade = None):
        # Constructor for new Student object
        self.__name = name
        self.__Exam1Grade = Exam1Grade
        self.__Exam2Grade = Exam2Grade

    def getName(self):
        return self.__name

    def getExam1Grade(self):
        return self.__Exam1Grade

    def setExam1Grade(self, Exam1Grade):
        self.__Exam1Grade = Exam1Grade

    def getExam2Grade(self):
        return self.__Exam2Grade

    def setExam2Grade(self, Exam2Grade):
        self.__Exam2Grade = Exam2Grade

    def __str__(self):
        # Print student information. Executed when print(object) is called.
        return "Student: " + str(self.__name) + "\n" + "  Exam 1: " + str(self.__Exam1Grade) + "\n" + "  Exam 2: " + str(self.__Exam2Grade)

    def getAverage(self):
        if(self.__Exam1Grade != None and self.__Exam2Grade != None):
            return (self.__Exam1Grade + self.__Exam2Grade)/2
        else:
            return "Some exam grades not available."