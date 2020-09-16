import math
import random
from tkinter import *


class Sudoku:

    def __init__(self, size):
        self.size = size
        self.sqrt = int(math.sqrt(size))
        self.possValues = [*range(1, size + 1, 1)]
        self.puzzle = []
        self.empties = []
        for i in range(size):
            self.puzzle.append(['']*size)
            for j in range(size):
                self.empties.append((i, j))
        random.shuffle(self.empties)
        self.getFrame()

    def addAt(self, row, column, value):
        '''
        Adds the given value at the given row and column
        :param row: Row for the value to be placed
        :param column: Column for the value to be placed
        :param value: Value to be placed at the given row and column
        :return: Void
        '''
        self.puzzle[int(row)][int(column)] = value

    def addValue(self, entered):
        '''
        Add value to puzzle based on what the user entered
        :param entered: String the user entered
        :return: Void
        '''
        trio = entered.split(" ")
        try:
            self.addAt(int(trio[0]), int(trio[1]), int(trio[2]))
        except ValueError:
            print("Invalid Value. Please Try Again:\n")
            return
        except IndexError:
            print('''Invalid Value. Please Try Again:
Input the row, column, and value in the form of \'# # #\'\n''')
            return
        try:
            self.empties.remove((int(trio[0]), int(trio[1])))
        except ValueError:
            return

    def getRow(self, row):
        '''
        Get the list of values in a given row
        :param row: Row to be gotten
        :return: List containing values in given row
        '''
        r = self.puzzle[row]
        r = [i for i in r if i != '']
        return r

    def getColumn(self, column):
        '''
        Get the list of values in a given column
        :param column: Column to be gotten
        :return: List containing values in given row
        '''
        col = []
        for i in range(self.size):
            if self.puzzle[i][column] == '':
                continue
            col.append(self.puzzle[i][column])
        return col

    def getFrame(self):
        print('''Enter the starting values in your puzzle.
The top is row 1 and the left is column 1.
To add a value, enter row, column, and value, each separated by a space.
For example, to add the number 1 to row 3, column 4, enter \'3 4 1\'
When you are finished, enter the word \'Done\'''')
        escape = "done"
        entered = input("Add a Value:\n")
        while entered.lower() != escape:
            if entered == '':
                print("3 numbers must be entered or the word \'done\'")
                entered = input("Add another value or enter \'Done\'\n")
                continue
            self.addValue(entered)
            entered = input("Add another value or enter \'Done\'\n")

    def getRegion(self, reg):
        '''
        Gives sqrt size region from given reg
        :param reg: Region to be gotten
        :return: A one dimensional list of the given region
        '''
        dim = []
        row = (reg//self.sqrt) * self.sqrt
        col = (reg % self.sqrt) * self.sqrt
        rMax = row + self.sqrt
        cMax = col + self.sqrt
        for r in range(row, rMax):
            for c in range(col, cMax):
                if self.puzzle[r][c] == '':
                    continue
                dim.append(self.puzzle[r][c])
        return dim

    def getRegNbr(self, row, col):
        '''
        Determine which region the cell is in.
        :param row: Row of given Cell
        :param col: Column of given cell
        :return: Region Number of given cell
        '''
        return (col//self.sqrt) + ((row//self.sqrt) * self.sqrt)

    def printBoard(self):
        '''
        Prints text version of the Sudoku board.
        :return: Void
        '''
        for i in range(self.size):
            for j in range(self.size):
                if self.puzzle[i][j] == '':
                    print('x', end='')
                else:
                    print(self.puzzle[i][j], end='')
            print("\n")


    def getPossValues(self, row, col):
        '''
        Determines which values have not been used in the row, column, or region
        :param row: Row the of the given cell
        :param col: Column of the given cell
        :return: Set containing the possible values of the cell
        '''
        if self.puzzle[row][col] != '':
            return {int(self.puzzle[row][col])}
        poss = set()
        poss |= set(int(i) for i in self.getRow(row))
        poss |= set(int(i) for i in self.getColumn(col))
        poss |= set(int(i) for i in self.getRegion(self.getRegNbr(row, col)))
        poss = poss.symmetric_difference(self.possValues)
        return poss

    def finish(self, cell):
        '''
        Creates a solution for a partially filled out Sudoku board. Uses backtracking.
        :param cell: Cell location to fill in.
        :return: Boolean - True if the Sudoku is complete, and false if it is not.
        '''
        row = cell[0]
        col = cell[1]
        for num in self.getPossValues(row, col):
            self.puzzle[row][col] = num
            if not self.empties:
                return True
            if self.finish(self.empties.pop(0)):
                return True
            self.puzzle[row][col] = ''

        self.empties.insert(0, cell)
        return False


def remAll(lst, value):
    '''
    Removes all of a selected value from a given list
    :param lst: Given list to remove values
    :param value: Value to be removed
    :return: List with all instances of value removed
    '''
    removed = []
    for i in lst:
        if i != value:
            removed.append(i)
    return removed
