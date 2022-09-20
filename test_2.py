class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.__count_obj = 0

    def up(self):
        return self.top

    def pr(self):
        return f'привет'



