import numpy as np
from cell import Cell


class Spreadsheet:

    def __init__(self, row: int, column: int) -> None:
        self.__row = row
        self.__column = column
        self.__table = row * [column * [x:=Cell()]]

    def setCellAt(self, row, column, value):
        print(self.__table)
        self.__table[row][column].set_value(value)
        print(self.__table[row][column])

    def getCellAt(self, row, column):
        return self.__table[row][column]

    def addRow(self, number):
        self.__table[number:number] = np.empty(self.__column, dtype="")

    def removeRow(self, number):
        self.__table[number:number] = ""

    def addColumn(self, number):
        pass

    def removeColumn(self, number):
        pass

    def swapRows(self, row1, row2):
        pass

    def swapColumns(self, column1, column2):
        pass


cell = Cell(2)
x = Spreadsheet(3, 4)
x.setCellAt(2, 2, 4)