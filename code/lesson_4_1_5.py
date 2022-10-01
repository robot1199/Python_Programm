class Tuple(tuple):
    def __add__(self, other):
        if len(other):
            if not isinstance(other, tuple):
                return Tuple(tuple(self) + tuple(other))
            return Tuple(tuple(self) + other)