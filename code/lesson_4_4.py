class Singleton:
    __value = None
    __value_base = None

    def __new__(cls, *args, **kwargs):
        if cls == Singleton:
            if cls.__value_base is None:
                cls.__value_base = object.__new__(cls)
            return cls.__value_base

        if cls.__value is None:
            cls.__value = object.__new__(cls)
        return cls.__value

    def __del__(self):
        self.__value = None
        self.__value_base = None


class Game(Singleton):
    def __init__(self, name):
        if 'name' not in self.__dict__:
            self.name = name
