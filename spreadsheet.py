from cell import Cell

class Spreadsheet:

    def __init__(self, row: int, column: int) -> None:
        self.__row = row
        self.__column = column
        self.__table = [[Cell() for y in range(column)] for x in range(row)]
    
    def get_table(self):
        return self.__table

    def setCellAt(self, row: int, column: int, value: int) -> None:
        self.__table[row][column].set_value(value)

    def getCellAt(self, row: int, column: int) -> str:
        return self.__table[row][column].get_value()

    def addRow(self, number: int) -> None:
        self.__table[number:number] = [[Cell() for x in range(self.__column)]]

    def removeRow(self, number: int) -> None:
        del self.__table[number]


    def addColumn(self, number: int) -> None:
        [self.__table[i].insert(number, Cell()) for i in range(self.__row)]

    def removeColumn(self, number: int) -> None:
        [self.__table[i].pop(number) for i in range(self.__row)]

    def swapRows(self, row1: int, row2: int) -> None:
        self.__table[row1], self.__table[row2] = self.__table[row2], self.__table[row1]

    def swapColumns(self, column1: int, column2: int) -> None:
        for i in range(self.__row):
            self.__table[i][column1], self.__table[i][column2] = self.__table[i][column2], self.__table[i][column1]