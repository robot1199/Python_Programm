class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


# здесь объявляйте классы ShopGenericView и ShopUserView
class ShopGenericView:
    def __str__(self):
        return '\n'.join([f'{i[0]}: {i[1]}' for i in self.__dict__.items()])


class ShopUserView:
    def __str__(self):
        return '\n'.join([f'{i[0]}: {i[1]}' for i in self.__dict__.items()][1:])



class Book(ShopItem):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year


book = Book("Python ООП", "Балакирев", 2022)
print(book)
