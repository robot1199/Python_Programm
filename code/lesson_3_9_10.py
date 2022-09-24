class Cell:
    def __init__(self, data=0):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class TableValues:
    def __init__(self, rows: int, cols: int, type_data=int):
        self.__rows = rows
        self.__cols = cols
        self.__type_data = type_data
        self.__cells = tuple(tuple(Cell() for _ in range(cols)) for _ in range(rows))

    def __check_index(self, index):
        r, c = index
        if not (0 <= r < self.__rows) or not (0 <= c < self.__cols):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__check_index(item)
        r,c = item
        return self.__cells[r][c].data

    def __setitem__(self, key, value):
        self.__check_index(key)
        if type(value) != self.__type_data:
            raise TypeError('неверный тип присваиваемых данных')
        r,c = key
        self.__cells[r][c].data = value

    def __iter__(self):
        for row in self.__cells:
            yield (x.data for x in row)




