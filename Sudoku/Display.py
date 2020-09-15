from tkinter import *


class Table:

    def __init__(self, root):
        self.table = {}
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=3, fg='blue',
                               font=('Arial', 16, 'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])
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


lst = [[1, 2, 3, 4, 5, 6, 7, 8 ,9],
       [1, 2, 3, 4, 5, 6, 7, 8, 9],
       [1, 2, 3, 4, 5, 6, 7, 8, 9],
       [1, 2, 3, 4, 5, 6, 7, 8, 9],
       [1, 2, 3, 4, 5, 6, 7, 8, 9],
       [1, 2, 3, 4, 5, 6, 7, 8, 9],
       [1, 2, 3, 4, 5, 6, 7, 8, 9],
       [1, 2, 3, 4, 5, 6, 7, 8, 9],
       [1, 2, 3, 4, 5, 6, 7, 8, 9]]

# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])

# create root window
root = Tk()
t = Table(root)
t.changeValue(0,0,0)
root.mainloop()