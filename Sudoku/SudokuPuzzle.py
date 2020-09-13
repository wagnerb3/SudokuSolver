import math


class Sudoku:
    size = 4
    sqrt = int(math.sqrt(size))
    possValues = [*range(1, size+1, 1)]

    def __init__(self):
        self.puzzle = []
        for i in range(Sudoku.size):
            self.puzzle.append(['']*10)
        self.getFrame()

    def addAt(self, row, column, value):
        '''
        Addes the given value at the given row and column
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
        for num in trio:
            if int(num)>Sudoku.size or len(trio) != 3:
                print("Invalid Values. Try Again:\n")
                return
        self.addAt(trio[0], trio[1], trio[2])

    def getRow(self, row):
        '''
        Get the list of values in a given row
        :param row: Row to be gotten
        :return: List containing values in given row
        '''
        return self.puzzle[row]

    def getColumn(self, column):
        '''
        Get the list of values in a given column
        :param column: Column to be gotten
        :return: List containing values in given row
        '''
        col = []
        for i in range(Sudoku.size):
            col.append(self.puzzle[i][column])
        return col

    def hasDuplicates(self, list):
        '''
        Checks to see if given list has duplicates.
        :param list: List of values in the puzzle.
        :return: True if there are duplicates, False if there are not
        '''
        remAll(list, '')
        if len(list) == len(set(list)):
            return False
        else:
            return True

    def hasDuplicates(self):
        '''
        Checks every row and column for duplicates
        :return: True if there are duplicates, False if there are not
        '''
        for i in range(Sudoku.size):
            if self.hasDuplicates(self.getRow(i)):
                return True
            if self.hasDuplicates(self.getColumn(i)):
                return True
        return False

    def getFrame(self):
        print('''Enter the starting values in your puzzle.
The top is row 1 and the left is column 1.
To add a value, enter row, column, and value, each separated by a space.
For example, to add the number 1 to row 3, column 4, enter \'3 4 1\'
When you are finished, enter the word \'Done\'''')
        escape = "done"
        entered = input("Add a Value:\n")
        while entered.lower() != escape:
            if (entered == ''):
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
        row = (reg//Sudoku.sqrt) * Sudoku.sqrt
        col = (reg%Sudoku.sqrt) * Sudoku.sqrt
        rMax = row + Sudoku.sqrt
        cMax = col + Sudoku.sqrt
        for r in range(row, rMax):
            for c in range(col, cMax):
                dim.append(self.puzzle[r][c])
        return dim

    def getRegion(self, row, col):
        return self.getRegion((col//Sudoku.sqrt) + ((row//Sudoku.sqrt) * Sudoku.sqrt))


    def printBoard(self):
        '''
        Prints text version of the Sudoku board.
        :return: Void
        '''
        for i in range(Sudoku.size):
            for j in range(Sudoku.size):
                if self.puzzle[i][j] == '':
                    print('x', end='')
                else:
                    print(self.puzzle[i][j], end='')
            print("\n")

    def validate(self, row, col):
        '''
        Determines if the value at the given location is valid.
        :param row: Row of value
        :param col: Column of value
        :return: True if the value is valid, False if the value is invalid
        '''
        reg = self.hasDuplicates(self.getRegion(row, col))
        r = self.hasDuplicates(self.getRow(row))
        c = self.hasDuplicates(self.getColumn(col))
        return reg and r and c

    #TODO - Possible values for given cell

def remAll(list, value):
    '''
    Removes all of a selected value from a given list
    :param list: Given list to remove values
    :param value: Value to be removed
    :return: List with all instances of value removed
    '''
    removed = []
    for i in list:
        if i != value:
            removed.append(i)
    return removed

x = Sudoku()
x.printBoard()
print(x.getRegion(0))
