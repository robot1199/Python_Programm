from random import randint


class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return self.value == 0


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.size = 3
        self.win = 0
        self.pole = tuple(tuple(Cell() for _ in range(self.size)) for _ in range(self.size))

    def __check_index(self, index):
        if type(index) not in (tuple, list) or len(index) != 2:
            raise IndexError('некорректно указанные индексы')

        r, c = index
        if not (0 <= r < self.size) or not (0 <= c < self.size):
            raise IndexError('некорректно указанные индексы')

    def __update_win_status(self):
        for row in self.pole:
            if all(x.value == self.HUMAN_X for x in row):
                self.win = 1
                return
            if all(x.value == self.COMPUTER_O for x in row):
                self.win = 2
                return

        for i in range(self.size):
            if all(x.value == self.HUMAN_X for x in (row[i] for row in self.pole)):
                self.win = 1
                return
            if all(x.value == self.COMPUTER_O for x in (row[i] for row in self.pole)):
                self.win = 2
                return
        if all(self.pole[i][i] == self.HUMAN_X for i in range(self.size)) or \
                all(self.pole[i][-1 - i] == self.HUMAN_X for i in range(self.size)):
            self.win = 1
            return
        if all(self.pole[i][i] == self.COMPUTER_O for i in range(self.size)) or \
                all(self.pole[i][-1 - i] == self.COMPUTER_O for i in range(self.size)):
            self.win = 2
            return
        if all(x.value != self.FREE_CELL for row in self.pole for x in row):
            self.win = 3

    def __getitem__(self, item):
        self.__check_index(item)
        r, c = item
        return self.pole[r][c].value

    def __setitem__(self, key, value):
        self.__check_index(key)
        r, c = key
        self.pole[r][c].value = value
        self.__update_win_status()
