from abc import ABC, abstractmethod


class StackInterface(ABC):

    @abstractmethod
    def push_back(self, obj):
        pass

    @abstractmethod
    def pop_back(self):
        pass


class Stack(StackInterface):
    def __init__(self):
        self._top = None
        self.__count_obj = 0

    def push_back(self, obj):
        last = self[self.__count_obj - 1] if self.__count_obj > 0 else None

        if last:
            last.next = obj
        if self._top is None:
            self._top = obj
        self.__count_obj += 1

    def pop_back(self):
        if self.__count_obj == 0:
            return None

        last = self[self.__count_obj - 1]

        if self.__count_obj == 1:
            self._top = None
        else:
            self[self.__count_obj - 2].next = None

        self.__count_obj -= 1
        return last

    def __check_index(self, item):
        if type(item) != int or not (0 <= item < self.__count_obj):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__check_index(item)

        count = 0
        h = self._top
        while h and count < item:
            h = h.next
            count += 1

        return h

    def __setitem__(self, key, value):
        self.__check_index(key)

        obj = self[key]
        prev = self[key - 1] if key > 0 else None

        value.next = obj.next
        if prev:
            prev.next = value


class StackObj:
    def __init__(self, data):
        self._data = data
        self._next = None
