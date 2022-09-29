class Vector:
    _allowed_types = (int, float)

    def __init__(self, *args):
        self.__check_coords(args)
        self.coords = args

    def __check_coords(self, coords):
        if not all(type(x) in self._allowed_types for x in coords):
            raise ValueError('неверный тип координат')

    def __len__(self):
        return len(self.coords)

    @staticmethod
    def __is_vector(other):
        if not isinstance(other, Vector):
            raise TypeError('операнд должен быть объектом класса Vector')

    def __check_vector_dims(self, other):
        if len(self.coords) != len(other.get_coords()):
            raise TypeError('размерности векторов не совпадают')

    def __make_vector(self, coords):
        try:
            return self.__class__(*coords)
        except ValueError:
            return Vector(*coords)

    def __add__(self, other):
        self.__is_vector(other)
        self.__check_vector_dims(other)

        coords = tuple(a + b for a, b in zip(self.coords, other.get_coords()))
        return self.__make_vector(coords)

    def __sub__(self, other):
        self.__is_vector(other)
        self.__check_vector_dims(other)

        coords = tuple(a - b for a, b in zip(self.coords, other.get_coords()))
        return self.__make_vector(coords)

    def get_coords(self):
        return tuple(self.coords)


class VectorInt(Vector):
    _allowed_types = (int,)


