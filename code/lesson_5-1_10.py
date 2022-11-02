class Triangle:
    def __init__(self, a, b, c):
        self._check(a)
        self._check(b)
        self._check(c)
        self._check_line(a, b, c)

        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def _check(x):
        if type(x) not in(float, int) or x <= 0:
            raise TypeError('стороны треугольника должны быть положительными числами')

    @staticmethod
    def _check_line(a, b, c):
        if a + b < c or a + c < b or b + c < a:
            raise ValueError('из указанных длин сторон нельзя составить треугольник')






input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]

lst_tr = []
for i in input_data:
    try:
        lst_tr.append(Triangle(*i))
    except:
        continue
