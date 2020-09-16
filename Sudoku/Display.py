from tkinter import *
import os
from Sudoku.SudokuPuzzle import Sudoku


class Table:

    def __init__(self, root, sudoku):
        root.title("Sudoku")
        root.iconphoto(False, PhotoImage(file=os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "/Resources/Into.png"))
        self.table = {}
        for i in range(len(sudoku)):
            for j in range(len(sudoku[0])):
                self.e = Entry(root, width=3, fg='blue',
                               font=('Arial', 16, 'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, sudoku[i][j])
                self.table[(i, j)] = self.e

    def changeValue(self, row, col, val):
        '''
        Changes value at given row and column to the given value.
        :param row: Given row
        :param col: Given column
        :param val: New Value
        :return: void
        '''
        ent = self.table.pop((row, col))
        ent.delete(0)
        ent.insert(END, val)
        self.table[(row, col)] = val


# find total number of rows and
# columns in list


board = Tk()
sud = Sudoku(4)
sud.finish(sud.empties.pop(0))
t = Table(board, sud.puzzle)
board.mainloop()
