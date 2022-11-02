class Basic:
    _item = None

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if type(value) != self._item or not (self.min_value <= value <= self.max_value):
            raise ValueError('значение не прошло валидацию')


class FloatValidator(Basic):
    _item = float


class IntegerValidator(Basic):
    _item = int


# def is_valid(lst, validators):
#     res = []
#     for x in lst:
#         for v in validators:
#             try:
#                 v(x)
#                 res.append(x)
#                 break
#             except:
#                 pass
#
#     return res

def is_valid(lst, validators):
    rec = [func(v, value) for value in lst for v in validators if func(v, value) != None]
    return rec


def func(f, value):
    try:
        f(value)
        return value
    except:
        pass


fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])

print(lst_out)
