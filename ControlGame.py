# File: ControlGame.py
# Student: Clara Torslov
# UT EID: ct32699
# Course Name: CS303E
#
# Date: April 8th 2022
# Description of Program: Class to be used in the Control Game.

class ControlGame:

    def __init__(self, turnsToPlay=64):
        # This initializes the game with an empty board, the current
        # player set to 'Red' and the number of turns
        # specified by the user (defaults to 64).  turnsToPlay must
        # be an even number in the range [2..64].
        self.__turnsToPlay = turnsToPlay
        self.__currentPlayer = "Red"
        self.__game = [["", "0", "1", "2", "3", "4", "5", "6", "7"],
                       ["0", ".", ".", ".", ".", ".", ".", ".", "."],
                       ["1", ".", ".", ".", ".", ".", ".", ".", "."],
                       ["2", ".", ".", ".", ".", ".", ".", ".", "."],
                       ["3", ".", ".", ".", ".", ".", ".", ".", "."],
                       ["4", ".", ".", ".", ".", ".", ".", ".", "."],
                       ["5", ".", ".", ".", ".", ".", ".", ".", "."],
                       ["6", ".", ".", ".", ".", ".", ".", ".", "."],
                       ["7", ".", ".", ".", ".", ".", ".", ".", "."]]

    def __str__(self):
        # Permit displaying the header "Current board is:" following by the
        # board.
        print("Current board is:")
        str = ""
        for row in range(9):
            str += self.__game[row][0]
            str += " "
            for col in range(1, 9):
                str += self.__game[row][col]
                str += " "
            str += "\n"
        return str

    def getCurrentPlayer(self):
        # Return the current player, 'Red' or 'Blue'
        return self.__currentPlayer

    def swapCurrentPlayer(self):
        # If the current player is 'Red', set it to 'Blue', and
        # vice versa.
        if (self.__currentPlayer == "Red"):
            self.__currentPlayer = "Blue"
        elif (self.__currentPlayer == "Blue"):
            self.__currentPlayer = "Red"

    def getBoardState(self):
        # Return the current board.
        return self.__game

    def takeTurn(self, row, col):
        # This attempts to add the current player's token to cell
        # (row, col).  Check whether the cell is legal and is not
        # occupied.  If the checks pass add the current player's
        # token to that cell.  Finally, return a Boolean value
        # indicating whether or not the turn occurred.

        row += 1
        col += 1
        if row <= 8 and row >= 1 and col <= 8 and col >= 1:
            if self.__game[row][col] == ".":
                # Place a game piece
                if self.__currentPlayer == "Red":
                    self.__game[row][col] = "R"
                    self.swapCurrentPlayer()
                    return True
                elif self.__currentPlayer == "Blue":
                    self.__game[row][col] = "B"
                    self.swapCurrentPlayer()
                    return True
            else:
                print("Invalid turn. Cannot place piece on occupied cell.")
                return False
        else:
            print("Invalid turn. Location is out of bounds.")
            return False

    def getScore(self):
        # Calculate the sum of rows, columns, and cells controlled by
        # Red and Blue.  Return this as a pair (red, blue).  This is
        # the most complicated method, so it's probably a good idea
        # to write subsidiary functions for this.

        redScore = 0
        blueScore = 0

        # For checking columns
        redcount = [0, 0, 0, 0, 0, 0, 0, 0]
        bluecount = [0, 0, 0, 0, 0, 0, 0, 0]

        # For checking neighbors
        redNeighbor = 0
        blueNeighbor = 0

        for row in range(1, 9):

            # Check rows
            if self.__game[row].count("R") > self.__game[row].count("B"):
                redScore += 1
            if self.__game[row].count("R") < self.__game[row].count("B"):
                blueScore += 1

            for col in range(1, 9):

                # Check columns
                if self.__game[row][col] == "R":
                    redcount[col - 1] += 1
                if self.__game[row][col] == "B":
                    bluecount[col - 1] += 1

                # Check neighbors
                if self.__game[row][col] == "R":
                    # This will happen if there is a R in position row,col.

                    # Check Neighbors (has to have two or more)
                    if row < 8 and (self.__game[row + 1][col] == "R"):
                        # above neighbor self.__game[row + 1][col]. Only checks if cell has an above neighbor.
                        redNeighbor += 1

                    if row > 1 and (self.__game[row - 1][col] == "R"):
                        # below neighbor self.__game[row - 1][col]. Only checks if cell has a below neighbor.
                        redNeighbor += 1

                    if col > 1 and (self.__game[row][col - 1] == "R"):
                        # left neighbor self.__game[row][col-1]. Only checks if cell has a left neighbor.
                        redNeighbor += 1

                    if col < 8 and (self.__game[row][col + 1] == "R"):
                        # right neighbor self.__game[row][col+1]. Only checks if cell has a right neighbor.
                        redNeighbor += 1

                if self.__game[row][col] == "B":
                    # This will happen if there is a B in position row,col.

                    # Check Neighbors (has to have two or more)
                    if row > 1 and (self.__game[row - 1][col] == "B"):
                        # below neighbor self.__game[row - 1][col]. Only checks if cell has a below neighbor.
                        blueNeighbor += 1

                    if row < 8 and (self.__game[row + 1][col] == "B"):
                        # above neighbor self.__game[row - 1][col]. Only checks if cell has an above neighbor.
                        blueNeighbor += 1

                    if col > 1 and (self.__game[row][col - 1] == "B"):
                        # left neighbor self.__game[row][col-1]. Only checks if cell has a left neighbor.
                        blueNeighbor += 1

                    if col < 8 and (self.__game[row][col + 1] == "B"):
                        # right neighbor self.__game[row][col+1]. Only checks if cell has a right neighbor.
                        blueNeighbor += 1


        # Count up which player controls each row
        for i in range(8):
            if redcount[i] > bluecount[i]:
                redScore += 1
            elif redcount[i] < bluecount[i]:
                blueScore += 1

        # Count up the neighbors
        if redNeighbor > 2:  # only update score if there is two or more neighbors
            redScore += redNeighbor
        if blueNeighbor > 2:  # only update score if there is two or more neighbors
            blueScore += blueNeighbor

        return redScore, blueScore
