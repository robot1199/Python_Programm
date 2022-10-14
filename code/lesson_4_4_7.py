class Furniture:
    def __init__(self, name, weight):
        self.__verify_name(name)
        self.__verify_weight(weight)
        self._name = name
        self._weight = weight

    # def __setattr__(self, key, value):
    #     verify = {'_name': self.__verify_name, '_weight': self.__verify_weight}
    #     if key in verify:
    #         verify[key](value)
    #     object.__setattr__(self, key, value)

    def __verify_name(self, value):
        if type(value) != str:
            raise TypeError('название должно быть строкой')

    def __verify_weight(self, num):
        if num <= 0:
            raise TypeError('вес должен быть положительным числом')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, item):
        self.__verify_name(item)
        self._name = item

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, item):
        self.__verify_weight(item)
        self._weight = item


class Closet(Furniture):
    def __init__(self, name, weight, tp, doors):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors

    def get_attrs(self):
        return self._name, self._weight, self._tp, self._doors


class Chair(Furniture):
    def __init__(self, name, weight, height):
        super(Chair, self).__init__(name, weight)
        self._height = height

    def get_attrs(self):
        return self._name, self._weight, self._height


class Table(Furniture):
    def __init__(self, name, weight, height, square):
        super(Table, self).__init__(name, weight)
        self._height = height
        self._square = square

    def get_attrs(self):
        return self._name, self._weight, self._height, self._square
