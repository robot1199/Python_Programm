class Matrix:
    def __init__(self, rows_or_list, cols=0, fill_value=0):
        if type(rows_or_list) == list:
            self._rows = len(rows_or_list)
            self._cols = len(rows_or_list[0])
            if not all(len(r) == self._cols for r in rows_or_list) or \
                not all(self.__is_digit(x) for row in rows_or_list for x in row):
                raise TypeError('список должен быть прямоугольным, состоящим из чисел')

            self._lst = rows_or_list

        else:
            if type(rows_or_list) != int or type(cols) != int or type(fill_value) not in (float, int):
                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')

            self._rows = rows_or_list
            self._cols = cols
            self._lst = [[fill_value for _ in range(cols)] for _ in range(rows_or_list)]

    @staticmethod
    def __is_digit(x):
        return type(x) in (float, int)

    def __check_index(self, index):
        r, c = index
        if not(0 <= r < self._rows) or not(0 <= c < self._cols):
            raise IndexError('недопустимые значения индексов')

    def __check_dinension(self, n):
        rows = n._rows
        cols = n._cols
        if self._rows != rows or self._cols != cols:
            raise ValueError('операции возможны только с матрицами равных размеров')




    def __getitem__(self, item):
        self.__check_index(item)
        r, c = item
        return self._lst[r][c]

    def __setitem__(self, key, value):
        self.__check_index(key)

        if not self.__is_digit(value):
            raise TypeError('значения матрицы должны быть числами')
        r, c = key
        self._lst[r][c] = value

    def __add__(self, other):
        if type(other) == type(self):
            self.__check_dinension(other)
            return Matrix([[self[i, j] + other[i, j] for j in range(self._cols)] for i in range(self._rows)])
        else:
            self.__is_digit(other)
            return Matrix([[self[i, j] + other for j in range(self._cols)] for i in range(self._rows)])

    def __sub__(self, other):
        if type(other) == type(self):
            self.__check_dinension(other)
            return Matrix([[self[i, j] - other[i, j] for j in range(self._cols)] for i in range(self._rows)])
        else:
            self.__is_digit(other)
            return Matrix([[self[i, j] - other for j in range(self._cols)] for i in range(self._rows)])











