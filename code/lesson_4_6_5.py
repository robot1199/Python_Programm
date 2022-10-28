class Digit:
    def __init__(self, value):
        self.check_digit(value)
        self.value = value

    @staticmethod
    def check_digit(value):
        if type(value) not in (float, int):
            raise TypeError('значение не соответствует типу объекта')



class Integer(Digit):
    def __init__(self, value):
        self.check_int(value)
        super(Integer, self).__init__(value)

    @staticmethod
    def check_int(value):
        if type(value) != int:
            raise TypeError('значение не соответствует типу объекта')


class Float(Digit):
    def __init__(self, value):
        self.check_fl(value)
        super(Float, self).__init__(value)

    @staticmethod
    def check_fl(value):
        if type(value) != float:
            raise TypeError('значение не соответствует типу объекта')


class Positive(Digit):
    def __init__(self, value):
        self.check_pos(value)
        super(Positive, self).__init__(value)

    @staticmethod
    def check_pos(value):
        if value < 0:
            raise TypeError('значение не соответствует типу объекта')


class Negative(Digit):
    def __init__(self, value):
        self.check_neg(value)
        super(Negative, self).__init__(value)

    @staticmethod
    def check_neg(value):
        if value >= 0:
            raise TypeError('значение не соответствует типу объекта')


class PrimeNumber(Integer, Positive):
    pass


class FloatPositive(Float, Positive):
    pass


digits = [PrimeNumber(2), PrimeNumber(6), PrimeNumber(10),
          FloatPositive(3.5), FloatPositive(5.3), FloatPositive(6.4), FloatPositive(9.2), FloatPositive(7.1)]

lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))

