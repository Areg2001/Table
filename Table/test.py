from cell import Cell
from spreadsheet import Spreadsheet


class Tester:

    @staticmethod
    def test_to_int(value):
        cell1 = Cell(value)
        cell1.toInt()

        if type(cell1.toInt()) == int:
            print("Passed")

        else:
            print("Failed")

    @staticmethod
    def test_to_float(value):
        cell1 = Cell(value)
        cell1.toDouble()

        if type(cell1.toDouble()) == float:
            print("Passed")

        else:
            print("Failed")

    @staticmethod
    def test_to_date(data):
        cell1 = Cell(data)

        cell1.toDate()
        return "Passed" if cell1.toDate() else "Failed"

    @staticmethod
    def test_reset(value):
        cell1 = Cell(value)
        cell1.reset()

        if cell1 == "":
            print("Passes")

        else:
            print("Failed")

    @staticmethod
    def setCellAt(row, column):
        spreadshit = Spreadsheet(3, 4)



