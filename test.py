from cell import Cell
from spreadsheet import Spreadsheet
from datetime import date

class Tester:

    @staticmethod
    def test_to_int(value):
        cell1 = Cell(value)
        cell1.toInt()

        if type(cell1.toInt()) == int:
            return "Passed toInt()"

        return "Failed toInt()"

    @staticmethod
    def test_to_float(value):
        cell1 = Cell(value)
        cell1.toDouble()

        if type(cell1.toDouble()) == float:
            return "Passed toFloat()"

        return "Failed toFloat()"

    @staticmethod
    def test_to_date(data):
        cell1 = Cell(data)
        cell1.toDate()

        return "Passed toDate" if type(cell1.toDate) == date else "Failed toDate"

    @staticmethod
    def test_reset(value):
        cell1 = Cell(value)
        cell1.reset()

        if cell1 == "":
            return "Passed reset()"

        return "Failed reset()"

    @staticmethod
    def test_setCellAt(row, column, value):
        spreadshit = Spreadsheet(3, 4)
        spreadshit.setCellAt(row, column, value)

        return "Passed secCellAt()" if spreadshit.get_table()[row][column].get_value() == value else "Failed SetCellAt()"

    @staticmethod
    def test_getCellAt(row, column, value):
        spreadshit = Spreadsheet(4, 5)
        spreadshit.get_table()[row][column].set_value(value)

        return "Passed getCellAt()" if spreadshit.get_table()[row][column].get_value() == value else "Failed getCellAt()"

    @staticmethod
    def test_addRow(number):
            spreadshit = Spreadsheet(4, 5)
            spreadshit.addRow(number)

            return "Passed addRow()" if len(spreadshit.get_table()) - 1 == 4 else "Failed addRow()" 

    @staticmethod
    def test_removeRow(number):
            spreadsheet = Spreadsheet(4, 5)
            spreadsheet.removeRow(number)

            return "Passed removeRow()" if len(spreadsheet.get_table()) + 1 == 4 else "Failed removeRow()" 

    @staticmethod
    def test_addColumn(number):
            spreadsheet = Spreadsheet(5, 7)
            spreadsheet.addColumn(number)

            return "Passed addColumn()" if len(spreadsheet.get_table()[0]) - 1 ==  7 else "Failed addColumn()" 

    @staticmethod
    def test_removeColumn(number):
            spreadsheet = Spreadsheet(4, 5)
            spreadsheet.removeColumn(number)

            return "Passed removeColumn()" if len(spreadsheet.get_table()[0]) + 1 ==  5 else "Failed removeColumn()" 

    @staticmethod
    def test_swapRows(row1, row2):
            spreadsheet = Spreadsheet(6, 9)
            first = spreadsheet.get_table()[row1]
            second = spreadsheet.get_table()[row2]
            spreadsheet.swapRows(row1, row2)
            
            return "Passed swapRows()" if first == spreadsheet.get_table()[row2] and second == spreadsheet.get_table()[row1] else "Failed swapRows()"

    @staticmethod
    def test_swapColumns(column1, column2):
            spreadsheet = Spreadsheet(6, 9)
            first = spreadsheet.get_table()[0][column1]
            second = spreadsheet.get_table()[0][column2]
            spreadsheet.swapColumns(column1, column2)
            
            return "Passed swapColumns()" if first == spreadsheet.get_table()[0][column2] and second == spreadsheet.get_table()[0][column1] else "Failed swapColumns()"

def all_passed():
    x = Tester()
    print(x.test_to_int("45"))
    print(x.test_to_float("5.7"))
    print(x.test_setCellAt(0,1,2))
    print(x.test_getCellAt(2, 3, 4))
    print(x.test_addRow(2))
    print(x.test_removeRow(2))
    print(x.test_addColumn(3))
    print(x.test_removeColumn(2))
    print(x.test_swapRows(1, 3))
    print(x.test_swapColumns(2, 4))