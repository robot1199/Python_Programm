class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume

    @staticmethod
    def weith_body(ro, volume):
        return ro * volume

    @classmethod
    def choose(cls, other):
        if type(other) in (float, int):
            return other

        elif isinstance(other, Body):
            return cls.weith_body(other.ro, other.volume)

        raise ValueError('не дури голову')

    def __eq__(self, other):
        return self.weith_body(self.ro, self.volume) == self.choose(other)

    def __lt__(self, other):
       return self.weith_body(self.ro, self.volume) < self.choose(other)
