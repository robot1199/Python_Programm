class TupleLimit(tuple):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, lst, max_length):

        if len(lst) > max_length:
            raise ValueError('число элементов коллекции превышает заданный предел')
        self.lst = lst
        self.max_length = max_length

    def __str__(self):
        return ' '.join(map(str, self.lst))

    def __repr__(self):
        return ' '.join(map(str, self.lst))


digits = list(map(float, input().split()))

try:
    c = TupleLimit(digits, 5)
    print(c)
except ValueError as r:
    print(r)
