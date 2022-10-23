class Track:
    def __init__(self, *args):
        self.__points = []
        if len(args) == 2 and not (all((isinstance(args[0], PointTrack), isinstance(args[0], PointTrack)))):
            self.__points.append(PointTrack(args[0], args[1]))
        else:
            for i in args:
                self.__points.append(i)



    @property
    def points(self):
        return tuple(self.__points)

    def add_back(self, pt):
        self.__points.append(pt)

    def add_front(self, pt):
        self.__points.insert(0, pt)

    def pop_back(self):
        self.__points.pop(-1)

    def pop_front(self):
        self.__points.pop(0)


class PointTrack:
    def __init__(self, x, y):
        self._check_num(x)
        self._check_num(y)
        self.x = x
        self.y = y

    def __str__(self):
        return f"PointTrack: {self.x}, {self.y}"

    def _check_num(self, item):
        if not type(item) in (float, int):
            raise TypeError('координаты должны быть числами')


tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
tr.add_back(PointTrack(1.4, 0))
tr.pop_front()
for pt in tr.points:
    print(pt)


print(tr.points)