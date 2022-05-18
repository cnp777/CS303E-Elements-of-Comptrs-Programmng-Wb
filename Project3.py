# File: Project3.py
# Student: Clara Torslov
# UT EID: ct32699
# Course Name: CS303E
#
# Date: May 2nd 2022
# Description of Program: Implementation of a version of Wordle.
# Answer will be a 5-letter word that is selected either randomly or manually from a wordlist.

from string import *
from random import *
import os.path

# 1. Create the wordlist
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

    return len(Wordlist), Wordlist

# 2. Check if a word is on the wordlist
def BinarySearch(wordlist, word):
    """ Search for word in sorted word list. From slideset 10, CS303E."""
    low = 0
    high = len(wordlist) - 1
    while high >= low:
        mid = (low + high) // 2
        if word < wordlist[mid]:
            high = mid - 1
        elif word == wordlist[mid]:
            return True  # mid
        else:
            low = mid + 1
    return False  # -low - 1

# 3. Welcome message

print("")
print("Welcome to WORDLE, the popular word game. The goal is to guess a "
      "\nfive letter word chosen at random from our wordlist. None of the "
      "\nwords on the wordlist have any duplicate letters.")

print("You will be allowed 6 guesses. Guesses must be from the allowed \nwordlist. We'll tell you if they're not.")
print("")
print("Each letter in your guess will be marked as follows:")
print("")
print("   x means that the letter does not appear in the answer")
print("   ^ means that the letter is correct and in the correct location")
print("   + means that the letter is correct, but in the wrong location")
print("")
print("Good luck!")
print("")

# 4. Get filename
filename = input("Enter the name of the file from which to extract the wordlist: ").strip()

# 5. Select answer
numberOfWords, wordlist = createWordlist(filename)
print("")

# 6. Accept and parse guesses from the user.
def split(word):
    """Helper function to playWordle()."""
    return list(word)

def playWordle(answer = None):
    """Function to play Wordle. If no input function will choose answer randomly from the wordlist."""
    if not answer:
        answer = choice(wordlist)
    else:
        x = 1
        while x <= 6:
            guess = input("Enter your guess (" + str(x) + "): ")
            if guess.lower() == answer:
                # 7. End the game, first option.
                return "CONGRATULATIONS! You win!"
            elif guess.lower() in wordlist:
                x += 1
                i = 0
                LetterList = list()
                SymbolList = list()
                for letter in split(guess.lower()):
                    if letter == answer[i]:
                        LetterList.append(letter)
                        SymbolList.append("^")
                        i += 1
                    elif letter in answer:
                        LetterList.append(letter)
                        SymbolList.append("+")
                        i += 1
                    else:
                        LetterList.append(letter)
                        SymbolList.append("x")
                        i += 1

                for letter in LetterList:
                    print(letter.upper(), end=" ")
                print("")
                for symbol in SymbolList:
                    print(symbol, end=" ")
                print("")

            else:
                print("Guess must be a 5-letter word in the wordlist. Try again!")
        # 7. End the game, second option.
        if guess.lower() != answer:
            return "Sorry! The word was " + str(answer) + ". Better luck next time!"
