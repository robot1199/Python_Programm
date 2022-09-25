class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return self.value == 0

    # @property
    # def value(self):
    #     return self.value
    #
    # @value.setter
    # def value(self, item):
    #     self.value = item


class TicTacToe:
    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))