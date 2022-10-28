class ItemAttrs:
    def __getitem__(self, item):
        return self.__dict__[list(self.__dict__)[item]]

    def __setitem__(self, key, value):
        self.__dict__[list(self.__dict__)[key]] = value


class Point(ItemAttrs):
    def __init__(self, x, y):
        self.x = x
        self.y = y





pt = Point(2,4)
