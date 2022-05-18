# File: WordleAssistant.py
# Student: Clara Torslov
# UT EID: ct32699
# Course Name: CS303E
#
# Date: April 15, 2022
# Description of Program: preliminary work towards the task of implementing Wordle and build some tools that might help you be a better Wordle player
import os.path

def createWordlist(filename):
    """ Read words from the provided file and store them in a list.
    The file contains only lowercase ascii characters, are sorted
    alphabetically, one word per line. Filter out any words that are
    not 5 letters long, have duplicate letters, or end in 's'. Return
    the list of words and the number of words as a pair. """
    while not os.path.isfile(filename):
        print("File does not exist. Try again!")
        filename = input("Enter the name of the file from which to extract the wordlist: ").strip()
    infile = open(filename, "r")
    text = infile.read().split()
    Wordlist = list()

    for word in text:
        if len(word) == 5 and len(set(word)) == len(word) and not word.endswith("s"):
            Wordlist.append(word)

    return Wordlist, len(Wordlist)


def containsAll(wordlist, include):
    """ Given your wordlist, return a set of all words from the wordlist
    that contain all of the letters in the string included.
    """
    s = set()

    for word in wordlist:
        if set(list(include)).issubset(set(list(word))):
            s.add(word)

    return s


def containsNone(wordlist, exclude):
    """ Given your wordlist, return a set of all words from the wordlist
    that do not contain any of the letters in the string exclude.
    """
    s = set()
    count = 0
    for word in wordlist:
        for ch in exclude:
            if ch not in word:
                count = 0
            else:
                count = 1
                break
        if (count == 0):
            s.add(word)
    return s

def containsAtPositions(wordlist, posInfo):
    """ posInfo is a dictionary that maps letters to positions.
    You can assume that the positions are in [0..4]. Return a set of
    all words from the wordlist that contain the letters from the
    dictionary at the indicated positions. For example, given posInfo
    {'a': 0, 'y': 4}.  This function might return the set:
    {'angry', 'aptly', 'amply', 'amity', 'artsy', 'agony'}. """

    s = set()

    for word in wordlist:
        count = 0
        for key in posInfo:
            if word.startswith(key, posInfo[key]):
                count +=1

        if count == len(posInfo):
            s.add(word)

    return s


def getPossibleWords(wordlist, posInfo, include, exclude):
    """ Finally, given a wordlist, dictionary posInfo, and
    strings include and exclude, return the set of all words from
    the wordlist that contains the words that satisfy all of
    the following:
    * has letters in positions indicated in posInfo
    * contains all letters from string include
    * contains none of the letters from string exclude.
    """

    s = set()

    for word in wordlist:
        if word in containsAtPositions(wordlist, posInfo) and word in containsAll(wordlist, include) and word in containsNone(wordlist, exclude):
            s.add(word)

    return s

