# class Discriptor_animal:
#     def __set_name__(self, owner, name):
#         self.name = '__' + name
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return property()
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         instance.__dict__[self.name] = value



class Animal:
    # name = Discriptor_animal()
    # kind = Discriptor_animal()
    # old = Discriptor_animal()

    def __init__(self, name, kind, old):
        self.__name = name # если делать через дескриптор то прописывать "__" не надо > self.name = name
        self.__kind = kind
        self.__old = old

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, value):
        self.__kind = value

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, value):
        self.__old = value


animals = [
    Animal('Васька', 'дворовый кот', 5),
    Animal('Рекс', 'немецкая овчарка', 8),
    Animal('Кеша', 'попугай', 3)
]
