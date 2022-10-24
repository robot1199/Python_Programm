class Food:
    def __init__(self, name, weight, calories):
        self._name = name
        self._weight = weight
        self._calories = calories


class BreadFood(Food):
    def __init__(self, name, weight, calories, white):
        super(BreadFood, self).__init__(name, weight, calories)
        self._white = white


class SoupFood(Food):
    def __init__(self, name, weight, calories, dietary):
        super(SoupFood, self).__init__(name, weight, calories)
        self._dietary = dietary


class FishFood(Food):
    def __init__(self, name, weight, calories, fish):
        super(FishFood, self).__init__(name, weight, calories)
        self._fish = fish
