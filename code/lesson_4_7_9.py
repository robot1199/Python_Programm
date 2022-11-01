class Note:
    __notes = ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')

    def __init__(self, name, ton):
        self._name = name
        self._ton = ton

    def __setattr__(self, key, value):
        if key == '_name' and value not in self.__notes:
            raise ValueError('недопустимое значение аргумента')

        if key == '_ton' and value not in (-1, 0, 1):
            raise ValueError('недопустимое значение аргумента')

        object.__setattr__(self, key, value)


class Notes:
    __slots__ = ('_do', '_re', '_mi', '_fa', '_solt', '_la', '_si')
    __notes = ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        Notes.__instance = None

    def __init__(self):
        for k, v in zip(self.__slots__, self.__notes):
            setattr(self, k, Note(v, 0))



    @staticmethod
    def __check_num(item):
        if not (0 <= item <= 6):
            raise IndexError('недопустимый индекс')

    def __getitem__(self, item):
        self.__check_num(item)
        return getattr(self, self.__slots__[item])


notes = Notes()