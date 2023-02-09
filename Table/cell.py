from datetime import date

colors: dict = {
    "red": 1,
    "blue": 2,
    "white": 3,
    "black": 4,
    "brown": 5,
    "green": 6,
    "orange": 7,
    "yellow": 8,
    "gray": 9
                }


class Cell:

    def __init__(self, value="", color="white") -> None:
        self.__value = value
        self.__color = colors[color]

    def set_value(self, new_value: str) -> None:
        self.__value = new_value

    def get_value(self) -> str:
        return self.__value

    def set_color(self, new_color: str):
        if new_color in list(colors.values()):
            self.__color = new_color

    def get_color(self) -> int:
        return self.__color

    def toInt(self) -> int:
        return int(self.__value)

    def toDouble(self) -> float:
        return float(self.__value)

    def toDate(self):
        pass

    def reset(self):
        self.__value = ""







