class ShopInterface:
    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')


class ShopItem(ShopInterface):
    __ID = 1

    def __init__(self, name, weight, price):
        self._name = name
        self._weight = weight
        self._price = price
        self._id = self.__ID
        ShopItem.__ID += 1



    def get_id(self):
        return self._id


a = ShopItem('fdff', 25, 23)
b = ShopItem('sdv', 36, 45)
