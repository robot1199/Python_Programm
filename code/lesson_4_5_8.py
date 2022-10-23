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
        if self.top is None:
            self.top = obj
        self.__count_obj += 1

    def pop_back(self):
        if self.__count_obj == 0:
            return None

        last = self[self.__count_obj - 1]
        if self.__count_obj == 1:
            self.top = None
        else:
            self[self.__count_obj - 2].next = None
        self.__count_obj -= 1
        return last


class StackObj:
    def __init__(self, data):
        self._data = data
        self._next = None
