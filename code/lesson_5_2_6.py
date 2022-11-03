class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y


def check_num(value):
    try:
        return int(value)
    except:
        try:
            return float(value)
        except:
            pass


x, y = input().split()

if check_num(x) and check_num(y):
    tr = Point(x, y)
else:
    tr = Point()

print(f'Point: x = {tr._x}, y = {tr._y}')