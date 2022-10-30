class MoneyOperators:
    def __add__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money + other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money + other.money)


    def __sub__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money - other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money - other.money)
    # здесь объявляйте еще один метод


class Money:
    def __init__(self, value):
        self.__veriffy_value(value)
        self._money = value

    @staticmethod
    def __veriffy_value(value):
        if type(value) not in (int, float):
            raise TypeError('сумма должна быть числом')

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, item):
        self.__veriffy_value(item)
        self._money = item


class MoneyR(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyR: {self.money}"


class MoneyD(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyD: {self.money}"