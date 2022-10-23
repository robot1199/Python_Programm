from abc import ABC, abstractmethod


class CountryInterface(ABC):

    @property
    @abstractmethod
    def name(self):
        return self.name

    @name.setter
    @abstractmethod
    def name(self, value):
        self.name = value

    @property
    @abstractmethod
    def population(self):
        return self.population

    @population.setter
    @abstractmethod
    def population(self, value):
        self.population = value

    @property
    @abstractmethod
    def square(self):
        return self.square

    @square.setter
    @abstractmethod
    def square(self, value):
        self.square = value


class Country(CountryInterface):
    def __init__(self, name, population, square):
        self._name = name
        self._population = population
        self._square = square

    def get_info(self):
        return f'{self._name}: {self._square}, {self._population}'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, value):
        self._population = value

    @property
    def square(self):
        return self._square

    @square.setter
    def square(self, value):
        self._square = value


country = Country("Россия", 140000000, 324005489.55)

